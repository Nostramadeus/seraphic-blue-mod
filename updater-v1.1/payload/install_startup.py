#!/usr/bin/env python3
"""Enable/disable optional checks only for the exact standard Linux launcher."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PAYLOAD = HERE / 'payload' if (HERE / 'payload/startup_update.py').is_file() else HERE
spec = importlib.util.spec_from_file_location("startup_core", PAYLOAD / 'startup_update.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
STANDARD = "05e5f5f7b6ec62f0f02fd909bc48680764764fa0e0419fd2c17041a82a88f65b"


def install(folder, disable=False, state_only=False):
    old = core.installation(folder)
    root = old["root"]
    launcher, backup = root / "play-linux.sh", root / "play-linux.pre-startup.sh"
    wrapper = HERE / 'launchers/play-linux.sh' if PAYLOAD != HERE else HERE / 'play-linux.startup.sh'
    payload = PAYLOAD
    bundle = json.loads((payload / "FILES.json").read_text(encoding="utf-8"))["files"]
    expected = dict(bundle, **{"FILES.json": core.digest(payload / "FILES.json")})

    def check(directory):
        core.safe_path(directory)
        entries = {p.name: p for p in directory.iterdir()}
        if set(entries) != set(expected):
            raise ValueError("Unknown helper directory; nothing overwritten.")
        for name, path in entries.items():
            if not core.safe_path(path).is_file() or core.digest(path) != expected[name]:
                raise ValueError("Modified helper directory; nothing overwritten.")

    check(payload)
    for path in (launcher, backup, root / ".sb-startup-updates"):
        core.safe_path(path)
    current, replacement = core.digest(launcher), core.digest(wrapper)
    if current not in (STANDARD, replacement):
        raise ValueError("Modified/custom launcher; nothing overwritten.")
    if backup.exists() and core.digest(backup) != STANDARD:
        raise ValueError("Original launcher backup differs; nothing overwritten.")
    helper = root / ".sb-startup-updates"
    if helper.exists():
        check(helper)
    if state_only:
        if current == replacement:
            if not backup.is_file() or not helper.is_dir():
                raise ValueError('Installed helper/backup missing.')
            return 'Enabled'
        return 'Disabled'
    if disable:
        if current == STANDARD:
            return "Already disabled."
        if not backup.is_file():
            raise ValueError("Original launcher backup missing.")
        data, mode = backup.read_bytes(), backup.stat().st_mode & 0o777
    else:
        if current == replacement:
            if not backup.is_file() or not helper.is_dir():
                raise ValueError("Installed helper/backup missing.")
            return "Already enabled."
        if not helper.exists():
            stage = helper.with_name(helper.name + ".installing-" + uuid.uuid4().hex)
            stage.mkdir()
            for name in expected:
                shutil.copyfile(payload / name, stage / name)
            check(stage)
            core.publish_stage(stage, helper)
        if not backup.exists():
            with launcher.open("rb") as inp, backup.open("xb") as out:
                shutil.copyfileobj(inp, out)
            backup.chmod(launcher.stat().st_mode & 0o777)
        if core.digest(backup) != STANDARD:
            raise ValueError("Original launcher backup failed verification.")
        data, mode = wrapper.read_bytes(), launcher.stat().st_mode & 0o777
    temporary = root / ("play-linux.startup-pending-" + uuid.uuid4().hex + ".tmp")
    with temporary.open("xb") as out:
        out.write(data)
    temporary.chmod(mode)
    if core.digest(launcher) != current:
        raise ValueError("Launcher changed during installation.")
    os.replace(temporary, launcher)
    return "Startup checks disabled; exact original restored, helper retained." if disable else "Optional startup checks enabled; exact original retained."


def graphical(folder=None):
    gui = core.find_gui()
    if not gui:
        print('Graphical setup needs an existing desktop session and kdialog or zenity. No dependencies were installed. See README.html for the manual limitation.', file=sys.stderr)
        return 2
    name, executable = gui
    if not folder:
        command = [executable, '--title', 'Seraphic Blue - Startup checks', '--getexistingdirectory', str(Path.home())] if name == 'kdialog' else [executable, '--file-selection', '--directory', '--title=Select the Seraphic Blue game folder']
        selected = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        if selected.returncode:
            return 0
        folder = selected.stdout.strip()
        if not folder:
            return 0
    try:
        current = install(folder, state_only=True)
        action = 'Disable startup checks' if current == 'Enabled' else 'Enable startup checks'
        message = action + '?\nThe exact original launcher is kept. Open play-linux.sh to play.\nDirect Player shortcuts bypass checks. Steam shortcuts are not changed.'
        command = [executable, '--title', 'Seraphic Blue - Startup checks', '--yesno', message, '--yes-label', action, '--no-label', 'Cancel'] if name == 'kdialog' else [executable, '--question', '--title=Seraphic Blue - Startup checks', '--text=' + message, '--ok-label=' + action, '--cancel-label=Cancel']
        if subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
            return 0
        text = install(folder, disable=(current == 'Enabled'))
        command = [executable, '--title', 'Seraphic Blue - Startup checks', '--msgbox', text] if name == 'kdialog' else [executable, '--info', '--title=Seraphic Blue - Startup checks', '--text=' + text]
        subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return 0
    except Exception as error:
        text = 'Startup checks were not changed: ' + str(error)
        command = [executable, '--title', 'Seraphic Blue - Startup checks', '--error', text] if name == 'kdialog' else [executable, '--error', '--title=Seraphic Blue - Startup checks', '--text=' + text]
        subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--game-folder")
    parser.add_argument("--disable", action="store_true")
    parser.add_argument('--state-only', action='store_true')
    parser.add_argument('--gui', action='store_true')
    args = parser.parse_args()
    if args.gui:
        raise SystemExit(graphical(args.game_folder))
    if not args.game_folder:
        parser.error('--game-folder or --gui is required')
    print(install(args.game_folder, args.disable, args.state_only))
