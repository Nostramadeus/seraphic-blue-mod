#!/usr/bin/env python3
"""Optional Linux/Deck startup updater. Python 3 standard library only."""
import argparse
import ctypes
from contextlib import contextmanager
import errno
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import time
import urllib.request
import uuid
import zipfile

REPO = "Nostramadeus/seraphic-blue-mod"
RESERVE = 128 * 1024 * 1024
CLUSTER = 65536
HERE = Path(__file__).resolve().parent
STABLE = re.compile(r"v([0-9]+)\.([0-9]+)\.([0-9]+)\Z")
ARCHIVE = re.compile(r"seraphic-blue-fullgame-(EN-Altered|EN|JP)-(v[0-9]+\.[0-9]+\.[0-9]+)\.zip\Z")
SHA = re.compile(r"[a-f0-9]{64}\Z")
SIDECARS = ("sb-repeat-a.json", "sb-repeat-b.json")


def safe_path(value):
    path = Path(os.path.abspath(value))
    for part in [path, *path.parents]:
        if part.is_symlink():
            raise ValueError("Linked files/folders are not supported.")
        if os.name == "nt" and part.exists() and getattr(part.stat(), "st_file_attributes", 0) & 1024:
            raise ValueError("Linked files/folders are not supported.")
    return path


def digest(path):
    result = hashlib.sha256()
    with safe_path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def installation(folder):
    root = safe_path(folder)
    manifest = json.loads(safe_path(root / "fullgame-manifest.json").read_text(encoding="utf-8"))
    match = ARCHIVE.fullmatch(manifest["archive"])
    if not match or manifest["release"] != match[2]:
        raise ValueError("Not a matching supported full-game release.")
    database = [m for m in manifest["members"] if m["file"] == "RPG_RT.ldb"]
    if len(database) != 1 or digest(root / "RPG_RT.ldb") != database[0]["sha256"]:
        raise ValueError("The game database differs from its release manifest.")
    launcher = safe_path(root / "PLAY.cmd").read_text(encoding="utf-8")
    if not re.search(r'--save-path\s+"saves"', launcher) or not re.search(r'--config-path\s+"config"', launcher):
        raise ValueError("Custom save/config locations need manual updating.")
    return {"root": root, "edition": match[1], "tag": match[2]}


def version(tag):
    match = STABLE.fullmatch(tag)
    if not match:
        raise ValueError("Invalid stable release version.")
    return tuple(int(n) for n in match.groups())


def release_asset(old, release):
    if release["draft"] or release["prerelease"]:
        raise ValueError("Not a stable release.")
    tag = release["tag_name"]
    if version(tag) <= version(old["tag"]):
        return None
    name = "seraphic-blue-fullgame-" + old["edition"] + "-" + tag + ".zip"
    assets = [a for a in release["assets"] if a["name"] == name and a["state"] == "uploaded"]
    if len(assets) != 1:
        raise ValueError("The matching edition download is unavailable.")
    asset = assets[0]
    expected = "https://github.com/" + REPO + "/releases/download/" + tag + "/" + name
    if asset["browser_download_url"] != expected or not asset["digest"].startswith("sha256:") or not SHA.fullmatch(asset["digest"][7:]) or type(asset["size"]) is not int or asset["size"] <= 0:
        raise ValueError("Invalid release URL, checksum or size.")
    return {"name": name, "tag": tag, "url": expected, "sha256": asset["digest"][7:], "bytes": asset["size"]}


def snapshot(root):
    root = safe_path(root)
    result = {}
    for name in ("saves", "config"):
        folder = safe_path(root / name)
        if not folder.exists():
            continue
        pending = [folder]
        while pending:
            for entry in pending.pop().iterdir():
                safe_path(entry)
                managed = entry.parent == root / 'saves' and entry.name.casefold() in SIDECARS
                if managed and (not stat.S_ISREG(entry.stat().st_mode) or entry.stat().st_size > 8 * 1024**2):
                    raise ValueError('Repeat sidecar must be a regular file of at most 8 MiB.')
                if entry.is_dir():
                    pending.append(entry)
                elif stat.S_ISREG(entry.stat().st_mode):
                    result[entry.relative_to(root).as_posix()] = digest(entry)
                else:
                    raise ValueError("Personal data must contain regular files only.")
    for entry in root.iterdir():
        if re.fullmatch(r"Save[0-9]+\.lsd", entry.name, re.I) or entry.name.casefold() in SIDECARS:
            safe_path(entry)
            if not stat.S_ISREG(entry.stat().st_mode):
                raise ValueError("A root save is not a regular file.")
            if entry.name.casefold() in SIDECARS and entry.stat().st_size > 8 * 1024**2:
                raise ValueError("Repeat sidecar exceeds its 8 MiB limit.")
            result["root:" + entry.name] = digest(entry)
    normalized(result)  # Reject conflicting duplicate saves before any copy.
    return result


def personal_relative(key):
    rel = 'saves/' + key[5:] if key.startswith('root:') else key
    return rel.casefold() if rel.casefold() in tuple('saves/' + name for name in SIDECARS) else rel


def normalized(before):
    result = {}
    folded = {}
    for key, value in before.items():
        rel = personal_relative(key)
        prior = folded.get(rel.casefold())
        if prior and (prior != rel or result[prior] != value):
            raise ValueError("Conflicting save copies; resolve them before updating.")
        folded[rel.casefold()] = rel
        result[rel] = value
    return result


def assert_snapshot(before, after):
    if before != after:
        raise ValueError("Saves/settings changed. Close the game and try again.")


def allocation(size):
    if size < 0:
        raise ValueError("Invalid file size.")
    return ((size + CLUSTER - 1) // CLUSTER) * CLUSTER


def free_space(parent):
    return shutil.disk_usage(safe_path(parent)).free


def require_space(parent, required):
    if free_space(parent) < required:
        raise OSError(errno.ENOSPC, "Not enough free disk space. The old game was not changed.")


def personal_allocation(root, before):
    seen = set()
    total = 0
    for key in before:
        rel = personal_relative(key)
        if rel not in seen:
            source = root / (key[5:] if key.startswith("root:") else key)
            total += allocation(safe_path(source).stat().st_size)
            seen.add(rel)
    return total


def archive_plan(archive, edition):
    prefix = "SeraphicBlue-Altered/" if edition == "EN-Altered" else "SeraphicBlue/"
    files, folded, total, reserved = {}, set(), 0, 0
    for entry in archive.infolist():
        name = entry.filename
        if not entry.is_dir():
            reserved += allocation(entry.file_size)
        if name == "IMPORTANT README (MUST READ).txt":
            continue
        if not name.startswith(prefix) or "\\" in name or ":" in name:
            raise ValueError("Unexpected archive path.")
        rel = name[len(prefix):]
        if not rel:
            continue
        for part in rel.rstrip("/").split("/"):
            if part in ("", ".", "..") or re.search(r'[<>|?*"\x00-\x1f]', part) or part.endswith((".", " ")) or re.match(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$", part, re.I):
                raise ValueError("Unsafe archive filename.")
        if (entry.external_attr >> 16) & 0o170000 == stat.S_IFLNK:
            raise ValueError("Linked archive entries are not supported.")
        if entry.is_dir():
            continue
        if rel.casefold() in folded:
            raise ValueError("Duplicate archive entry.")
        if re.search(r"^(saves|config)/|(^|/)Save[0-9]+\.lsd$|(^|/)sb-repeat-[ab]\.json$", rel, re.I):
            raise ValueError("A release must not contain personal data.")
        folded.add(rel.casefold())
        total += entry.file_size
        if total > 8 * 1024**3:
            raise ValueError("Expanded release unexpectedly large.")
        files[rel] = entry
    return files, reserved


def verify_release(stage, files, edition, tag):
    manifest = json.loads((stage / "fullgame-manifest.json").read_text(encoding="utf-8"))
    if manifest["archive"] != "seraphic-blue-fullgame-" + edition + "-" + tag + ".zip" or manifest["release"] != tag:
        raise ValueError("Downloaded edition/version does not match.")
    declared = set()
    for member in manifest["members"]:
        rel, size, checksum = member["file"], member["bytes"], member["sha256"]
        if rel.casefold() in declared or rel not in files or not SHA.fullmatch(checksum) or type(size) is not int or size < 0:
            raise ValueError("Invalid, duplicate or missing manifest member.")
        declared.add(rel.casefold())
        path = stage / rel
        if path.stat().st_size != size or digest(path) != checksum:
            raise ValueError("An extracted release file failed verification.")
    required = ("RPG_RT.ldb", "RPG_RT.lmt", "RPG_RT.ini", "Map0001.lmu", "EasyRPG.ini", "Player.exe", "PLAY.cmd", "play-linux.sh", "native-linux/Player")
    for rel in required:
        if rel.casefold() not in declared or not (stage / rel).is_file() or (stage / rel).stat().st_size <= 0:
            raise ValueError("The new release is incomplete.")
    if any(rel not in ("fullgame-manifest.json", "SHA256SUMS") and rel.casefold() not in declared for rel in files):
        raise ValueError("Extracted file absent from manifest.")


@contextmanager
def destination_parent(path):
    """Check before writes; anchor Linux opens or hold no-delete Windows directories."""
    path = safe_path(path)
    descriptors, handles = [], []
    kernel = None
    try:
        if os.name == 'nt':
            kernel = ctypes.WinDLL('kernel32', use_last_error=True)
            create = kernel.CreateFileW
            create.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p]
            create.restype = ctypes.c_void_p
            information = kernel.GetFileInformationByHandle
            information.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            information.restype = ctypes.c_int
            kernel.CloseHandle.argtypes = [ctypes.c_void_p]
            current = Path(path.anchor)
            for index, part in enumerate((path.anchor, *path.parent.parts[1:])):
                if index:
                    current = current / part
                    current.mkdir(exist_ok=True)
                handle = create(str(current), 0x80000000, 1, None, 3, 0x02200000, None)
                if handle == ctypes.c_void_p(-1).value:
                    raise ctypes.WinError(ctypes.get_last_error())
                handles.append(handle)
                info = (ctypes.c_uint32 * 13)()
                if not information(handle, ctypes.byref(info)):
                    raise ctypes.WinError(ctypes.get_last_error())
                if info[0] & 0x400 or not info[0] & 0x10:
                    raise ValueError('Linked or non-directory destination.')
            safe_path(path)
            yield None
        else:
            flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
            descriptor = os.open(path.anchor, flags)
            descriptors.append(descriptor)
            for part in path.parent.parts[1:]:
                try:
                    os.mkdir(part, dir_fd=descriptor)
                except FileExistsError:
                    pass
                descriptor = os.open(part, flags, dir_fd=descriptor)
                descriptors.append(descriptor)
            safe_path(path)
            yield descriptor
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)
        if kernel:
            for handle in reversed(handles):
                kernel.CloseHandle(handle)


def exclusive_stream(path, parent_descriptor):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_BINARY', 0) | getattr(os, 'O_NOFOLLOW', 0)
    descriptor = os.open(path.name, flags, 0o600, dir_fd=parent_descriptor) if parent_descriptor is not None else os.open(path, flags, 0o600)
    return os.fdopen(descriptor, 'wb')


@contextmanager
def destination_file(path):
    with destination_parent(path) as descriptor:
        with exclusive_stream(path, descriptor) as output:
            yield output


def copy_personal(source, target, before):
    for key, checksum in before.items():
        rel = personal_relative(key)
        src = source / (key[5:] if key.startswith("root:") else key)
        dst = target / rel
        with destination_parent(dst) as descriptor:
            if dst.exists():
                if digest(dst) != checksum:
                    raise ValueError("Personal data destination conflicts.")
            else:
                with safe_path(src).open("rb") as inp, exclusive_stream(dst, descriptor) as out:
                    shutil.copyfileobj(inp, out)
            if digest(dst) != checksum or digest(src) != checksum:
                raise ValueError("Save/settings copy failed verification.")


def publish_stage(stage, output):
    if sys.platform.startswith("linux"):
        libc = ctypes.CDLL(None, use_errno=True)
        rename = libc.renameat2  # Missing support fails safely; no replacing fallback.
        rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
        rename.restype = ctypes.c_int
        if rename(-100, os.fsencode(stage), -100, os.fsencode(output), 1) != 0:
            code = ctypes.get_errno()
            raise OSError(code, os.strerror(code), str(output))
    elif os.name == "nt":
        os.rename(stage, output)
    else:
        raise OSError("Atomic non-overwriting publication unsupported on this platform.")


def install_update(folder, archive_path, expected, tag, status=lambda text: None):
    old = installation(folder)
    if not SHA.fullmatch(expected) or version(tag) <= version(old["tag"]):
        raise ValueError("Invalid checksum/version or attempted downgrade.")
    if digest(archive_path) != expected:
        raise ValueError("Download checksum mismatch.")
    parent = old["root"].parent
    output = safe_path(parent / ("SeraphicBlue-" + old["edition"] + "-" + tag))
    if output.exists():
        raise FileExistsError("Destination already exists; nothing overwritten.")
    stage = output.with_name(output.name + ".partial-" + uuid.uuid4().hex)
    backup = output.with_name(output.name + ".save-backup-" + uuid.uuid4().hex)
    before = snapshot(old["root"])
    expected_personal = normalized(before)
    try:
        with zipfile.ZipFile(archive_path) as archive:
            files, allocated = archive_plan(archive, old["edition"])
            require_space(parent, allocated + 2 * personal_allocation(old["root"], before) + RESERVE)
            assert_snapshot(before, snapshot(old["root"]))
            status("Making a verified save/settings backup...")
            backup.mkdir()
            copy_personal(old["root"], backup, before)
            assert_snapshot(expected_personal, snapshot(backup))
            assert_snapshot(before, snapshot(old["root"]))
            status("Extracting and checking the new game...")
            stage.mkdir()
            for rel, entry in files.items():
                target = stage / rel
                with archive.open(entry) as inp, destination_file(target) as out:
                    shutil.copyfileobj(inp, out)
                if os.name != "nt":
                    target.chmod((entry.external_attr >> 16) & 0o777 or 0o644)
            verify_release(stage, files, old["edition"], tag)
        if digest(archive_path) != expected:
            raise ValueError("Download changed during extraction.")
        status("Copying saves and settings...")
        backup_snapshot = snapshot(backup)
        assert_snapshot(expected_personal, backup_snapshot)
        copy_personal(backup, stage, backup_snapshot)
        assert_snapshot(before, snapshot(old["root"]))
        assert_snapshot(expected_personal, snapshot(backup))
        assert_snapshot(expected_personal, snapshot(stage))
        if output.exists():
            raise FileExistsError("Destination appeared during update.")
        publish_stage(stage, output)
        return {"folder": output, "backup": backup, "edition": old["edition"], "tag": tag}
    except BaseException:
        if stage.is_dir():
            try:
                with destination_file(stage / 'UPDATE-INCOMPLETE.txt') as marker:
                    marker.write(b"Incomplete update. Use the old game; backup retained.\n")
            except Exception:
                pass
        raise


def fetch_release():
    request = urllib.request.Request("https://api.github.com/repos/" + REPO + "/releases/latest", headers={"User-Agent": "SeraphicBlue-Updater", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(request, timeout=3) as response:
        return json.load(response)


def bounded_release():
    # Separate process bounds DNS as well as socket operations. No GUI in worker.
    clock = time.monotonic()
    process = subprocess.Popen([sys.executable, str(HERE / "startup_update.py"), "--check-release"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0)
    try:
        output, _ = process.communicate(timeout=max(0, 3 - (time.monotonic() - clock)))
        return json.loads(output) if process.returncode == 0 else None
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()
        return None


def find_gui():
    if not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
        return None
    for name in ("kdialog", "zenity"):
        executable = shutil.which(name)
        if executable:
            return name, executable
    return None


def confirm_update(gui, old, asset):
    message = ("A newer " + old["edition"] + " release is available: " + asset["tag"] + ".\nInstall into a new neighboring folder, then open it?\nThe old game and a save/settings backup are kept.\nInstallation may take a few minutes.")
    name, executable = gui
    command = ([executable, "--title", "Seraphic Blue - Update available", "--yesno", message, "--yes-label", "Install update", "--no-label", "Play current"] if name == "kdialog" else [executable, "--question", "--title=Seraphic Blue - Update available", "--text=" + message, "--ok-label=Install update", "--cancel-label=Play current"])
    return subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def download(asset, parent):
    require_space(parent, asset["bytes"] + RESERVE)
    cache = parent / (".sb-update-download-" + uuid.uuid4().hex)
    cache.mkdir()
    target = cache / asset["name"]
    request = urllib.request.Request(asset["url"], headers={"User-Agent": "SeraphicBlue-Updater"})
    total = 0
    with urllib.request.urlopen(request, timeout=30) as response, target.open("xb") as output:
        if not response.geturl().startswith("https://"):
            raise ValueError("Insecure download redirect.")
        while True:
            block = response.read(1024 * 1024)
            if not block:
                break
            total += len(block)
            if total > asset["bytes"]:
                raise ValueError("Download exceeds release size.")
            output.write(block)
    if total != asset["bytes"]:
        raise ValueError("Download size mismatch.")
    return target


def launch_updated(folder):
    player = safe_path(folder / "native-linux/Player")
    for name in ("saves", "config"):
        safe_path(folder / name).mkdir(exist_ok=True)
    environment = os.environ.copy()
    environment["LD_LIBRARY_PATH"] = str(folder / "native-linux/lib") + (":" + environment["LD_LIBRARY_PATH"] if environment.get("LD_LIBRARY_PATH") else "")
    subprocess.Popen([str(player), "--project-path", ".", "--save-path", "saves", "--config-path", "config", "--encoding", "932", "--window"], cwd=folder, env=environment)


def enable_new_startup(folder):
    result = subprocess.run([sys.executable, str(HERE / 'install_startup.py'), '--game-folder', str(folder)], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0) if os.name == 'nt' else 0)
    if result.returncode:
        raise RuntimeError('Startup checks could not be kept in the new copy; play current.')


def startup(folder):
    try:
        gui = find_gui()
        if not gui:
            return 0
        old = installation(folder)
        release = bounded_release()
        if not release:
            return 0
        asset = release_asset(old, release)
        if not asset or not confirm_update(gui, old, asset):
            return 0
        archive = download(asset, old["root"].parent)
        result = install_update(old["root"], archive, asset["sha256"], asset["tag"])
        enable_new_startup(result['folder'])
        launch_updated(result["folder"])
        return 10
    except (Exception, KeyboardInterrupt):
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game-folder")
    parser.add_argument("--check-release", action="store_true")
    args = parser.parse_args()
    if args.check_release:
        try:
            print(json.dumps(fetch_release(), ensure_ascii=True))
            return 0
        except Exception:
            return 1
    return startup(args.game_folder) if args.game_folder else 0


if __name__ == "__main__":
    sys.exit(main())
