"""Apply the adjacent verified VCDIFF manifest to a new game copy, never to the source."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import stat
import subprocess
import sys
import uuid

FORMAT = 'seraphic-blue-xdelta3-v1'
HASH = re.compile(r'^[0-9a-f]{64}$')
RESERVED = {'CON', 'PRN', 'AUX', 'NUL', 'CONIN$', 'CONOUT$'} | {
    prefix + number for prefix in ('COM', 'LPT') for number in '123456789¹²³'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def relative(value):
    require(isinstance(value, str) and value and '\\' not in value and ':' not in value, 'Invalid relative path')
    path = PurePosixPath(value)
    require(path.parts and not path.is_absolute() and path.as_posix() == value and all(part not in ('', '.', '..') for part in path.parts),
            'Non-normalized or traversal path: ' + value)
    for part in path.parts:
        require(part[-1] not in ' .' and not any(ord(character) < 32 or ord(character) == 127 for character in part),
                'Unsafe path component: ' + value)
        require(not any(character in '<>"|?*' for character in part) and part.split('.')[0].upper() not in RESERVED,
                'Reserved path component: ' + value)
    return path


def no_links(path):
    for component in (path, *path.parents):
        if os.path.lexists(component):
            attributes = component.lstat()
            require(not stat.S_ISLNK(attributes.st_mode) and not (getattr(attributes, 'st_file_attributes', 0) & 0x400),
                    'Symlink/reparse point refused: ' + str(component))


def inside(path, directory):
    return path == directory or directory in path.parents


def located(directory, value):
    path = directory.joinpath(*relative(value).parts)
    no_links(path)
    require(inside(path.resolve(), directory), 'Path leaves its directory: ' + value)
    return path


def unique_paths(entries, key='path'):
    seen = set()
    for entry in entries:
        path = relative(entry[key]).as_posix()
        require(path.casefold() not in seen, 'Duplicate/case-colliding path: ' + path)
        seen.add(path.casefold())
    for path in seen:
        require(not any(parent.as_posix() in seen for parent in PurePosixPath(path).parents if parent.parts),
                'File/directory target collision: ' + path)


def checked_hash(value):
    require(isinstance(value, str) and HASH.fullmatch(value), 'Invalid SHA256 field')
    return value


def load_manifest(directory):
    manifest_path = located(directory, 'manifest.json')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    require(manifest['format'] == FORMAT and manifest['language'] in ('en', 'ja'), 'Unsupported patch manifest')
    require(isinstance(manifest['baseFiles'], list) and manifest['baseFiles'], 'Missing pristine-base fingerprint')
    require(isinstance(manifest['files'], list) and manifest['files'], 'Empty patch manifest')
    unique_paths(manifest['baseFiles'])
    unique_paths(manifest['files'])
    unique_paths(manifest['files'], 'payload')
    for entry in manifest['baseFiles']:
        checked_hash(entry['sha256'])
    for entry in manifest['files']:
        target = relative(entry['path'])
        require(target.suffix.lower() in ('.ldb', '.lmu', '.lmt', '.png') or entry['path'] == 'EasyRPG.ini',
                'Target type is not game patch data: ' + entry['path'])
        require(not target.name.casefold().startswith('save') and target.suffix.lower() != '.lsd', 'Save state cannot be patched')
        require(entry['kind'] in ('delta', 'new'), 'Unknown patch entry kind')
        require(entry['sourceSha256'] is None if entry['kind'] == 'new' else bool(HASH.fullmatch(entry['sourceSha256'])),
                'Invalid new/source file marker')
        checked_hash(entry['payloadSha256'])
        checked_hash(entry['resultSha256'])
    return manifest


def tree_snapshot(directory):
    files = []
    names = set()
    for current, directories, filenames in os.walk(directory, followlinks=False):
        for name in directories + filenames:
            path = Path(current) / name
            no_links(path)
            rel = path.relative_to(directory).as_posix()
            relative(rel)
            require(rel.casefold() not in names, 'Source tree has case-colliding paths: ' + rel)
            names.add(rel.casefold())
        for name in filenames:
            path = Path(current) / name
            require(path.is_file(), 'Non-regular source file: ' + str(path))
            files.append((path.relative_to(directory).as_posix(), digest(path)))
    return sorted(files)


def apply(base_argument, output_argument):
    directory = Path(os.path.abspath(__file__)).parent
    base = Path(os.path.abspath(base_argument))
    output = Path(os.path.abspath(output_argument))
    relative(output.name)
    for path in (directory, base, output):
        no_links(path)
    directory = directory.resolve(strict=True)
    base = base.resolve(strict=True)
    require(base.is_dir(), 'Base is not a game directory')
    require(not os.path.lexists(output), 'Output already exists; choose a new folder')
    require(output.parent.is_dir(), 'Output parent directory must already exist')
    output = output.resolve()
    require(not inside(output, base) and not inside(base, output), 'Base and output must be separate')
    require(not inside(output, directory) and not inside(directory, output), 'Output cannot overlap the patch directory')
    require(not inside(directory, base) and not inside(base, directory), 'Extract the patch separately from the game')
    manifest = load_manifest(directory)
    system = platform.system().lower()
    require(platform.machine().lower() in ('amd64', 'x86_64'), 'Bundled tool requires an x86-64 computer')
    require(system in ('windows', 'linux'), 'This patch tool supports Windows/Linux x86-64 only')
    tool_entry = manifest['tools'][system + '-x86_64']
    tool = located(directory, tool_entry['path'])
    require(tool.is_file() and digest(tool) == checked_hash(tool_entry['sha256']), 'Patch decoder missing or corrupt')
    require(system == 'windows' or os.access(tool, os.X_OK), 'Decoder is not executable; use chmod +x on its documented path')
    for entry in manifest['files']:
        payload = located(directory, entry['payload'])
        require(payload.is_file() and digest(payload) == entry['payloadSha256'], 'Patch payload missing or corrupt: ' + entry['payload'])
    snapshot = tree_snapshot(base)
    source_hashes = dict(snapshot)
    source_names = {name.casefold() for name in source_hashes}
    for entry in manifest['baseFiles']:
        require(source_hashes.get(entry['path']) == entry['sha256'], 'Unsupported or modified base file: ' + entry['path'])
    for entry in manifest['files']:
        source = located(base, entry['path'])
        if entry['kind'] == 'new':
            require(not os.path.lexists(source) and entry['path'].casefold() not in source_names,
                    'New patch file already exists in base: ' + entry['path'])
        else:
            require(source_hashes.get(entry['path']) == entry['sourceSha256'], 'Wrong source for delta: ' + entry['path'])
    output.mkdir()
    print('Verified inputs. Creating new game copy; source remains untouched.', flush=True)
    for name, expected in snapshot:
        source = located(base, name)
        destination = located(output, name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        no_links(destination)
        shutil.copy2(source, destination)
        require(digest(destination) == expected, 'Source changed during copying: ' + name)
    environment = {key: value for key, value in os.environ.items() if key.upper() != 'XDELTA'}
    options = {'creationflags': subprocess.CREATE_NO_WINDOW} if system == 'windows' else {}
    for entry in manifest['files']:
        destination = located(output, entry['path'])
        destination.parent.mkdir(parents=True, exist_ok=True)
        no_links(destination)
        payload = located(directory, entry['payload'])
        if entry['kind'] == 'new':
            shutil.copyfile(payload, destination)
        else:
            temporary = destination.parent / ('.sbpatch-' + uuid.uuid4().hex + '.tmp')
            no_links(temporary)
            require(inside(temporary.resolve(), output) and not os.path.lexists(temporary), 'Unsafe temporary output')
            process = subprocess.run([str(tool), '-d', '-D', '-R', '-s', str(located(base, entry['path'])), str(payload), str(temporary)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment, timeout=60, **options)
            require(process.returncode == 0, 'Decoder failed for ' + entry['path'] + ': ' + process.stderr.decode('utf-8', 'replace')[:500])
            require(digest(temporary) == entry['resultSha256'], 'Temporary result integrity check failed: ' + entry['path'])
            os.replace(temporary, destination)
        require(digest(destination) == entry['resultSha256'], 'Result integrity check failed: ' + entry['path'])
    print('Patch verified. Play the new copy: ' + str(output), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True, help='existing game folder; read only')
    parser.add_argument('--out', required=True, help='new, nonexistent output folder')
    arguments = parser.parse_args()
    try:
        apply(arguments.base, arguments.out)
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        parser.exit(1, 'Patch stopped: %s\nSource was not written. A partial new output may remain; do not play it.\n' % error)


if __name__ == '__main__':
    main()
