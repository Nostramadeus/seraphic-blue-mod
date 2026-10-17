"""Update a supported test.1 game into a separate copy with a verified save backup.

Close the game first and make a normal Memory Tree save. Mid-event debug saves
are not compatibility evidence. Pass --saves explicitly: normally the current
game folder; if you used --save-path, use that exact folder. For a read-only game
folder, find the writable fallback folder containing your latest SaveNN.lsd.
This tool detects writes during copying but does not lock a running game.
"""
import argparse
import contextlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_patch as patch

SUPPORTED_PREDECESSOR = 'v0.1.0-test.1'
PREVIOUS_DATABASE = {
    'en': '2e7a78503f97151006217c9d3c8dacf035846ed8cb3557e5ea87020d65cc6299',
    'ja': 'b2ee41c1a1b91c922d08640e43163a3c640f998ebe294733f9dd5084d3d75d3b',
}
SAVE_NAME = re.compile(r'Save[0-9]+\.lsd', re.IGNORECASE | re.ASCII)
BACKUP_MANIFEST = 'save-backup.json'
INCOMPLETE = 'SB_UPDATE_INCOMPLETE.txt'


def disjoint(first, second):
    return not patch.inside(first, second) and not patch.inside(second, first)


def update(base_argument, current_argument, saves_argument, output_argument, backup_argument):
    arguments = [base_argument, current_argument, saves_argument, output_argument, backup_argument]
    paths = [Path(os.path.abspath(argument)) for argument in arguments]
    directory = Path(os.path.abspath(patch.__file__)).parent
    for path in [directory, *paths]:
        patch.no_links(path)
    base, current, saves = [path.resolve(strict=True) for path in paths[:3]]
    output, backup = [path.resolve() for path in paths[3:]]
    staging = output.with_name(output.name + '.partial')
    patch.no_links(staging)
    directory = directory.resolve(strict=True)
    for source in (base, current, saves):
        patch.require(source.is_dir(), 'Source must be a directory: ' + str(source))
        patch.require(disjoint(source, directory), 'Extract the patch separately from all source folders')
    patch.require(disjoint(base, current) and disjoint(base, saves), 'Pristine base must be separate from current game and saves')
    patch.require(patch.inside(saves, current) or disjoint(saves, current), 'Save folder cannot contain the current game folder')
    for destination in (output, backup, staging):
        patch.relative(destination.name)
        patch.require(not os.path.lexists(destination), 'Destination exists; choose a new folder: ' + str(destination))
        patch.require(destination.parent.is_dir(), 'Destination parent must exist')
        patch.require(all(disjoint(destination, source) for source in (base, current, saves, directory)),
                      'Output/backup must be outside all source and patch folders')
    patch.require(disjoint(output, backup), 'Output and backup folders must be separate')
    patch.require(disjoint(staging, backup), 'Partial output and backup folders must be separate')
    manifest = patch.load_manifest(directory)
    language = manifest['language']
    database = patch.located(current, 'RPG_RT.ldb')
    patch.require(database.is_file() and patch.digest(database) == PREVIOUS_DATABASE[language],
                  'Current game is not the supported ' + language.upper() + ' ' + SUPPORTED_PREDECESSOR + ' release')
    snapshots = {source: patch.tree_snapshot(source) for source in (base, current, saves, directory)}
    selected = [(name, digest) for name, digest in snapshots[saves] if '/' not in name and SAVE_NAME.fullmatch(name)]
    patch.require(selected, 'No Save[0-9]+.lsd files found in --saves. Select the actual save folder explicitly.')
    print('Close the game before updating. Selected %d save files: %s' % (len(selected), ', '.join(name for name, _ in selected)), flush=True)
    backup.mkdir()
    for name, expected in selected:
        source = patch.located(saves, name)
        destination = patch.located(backup, name)
        shutil.copyfile(source, destination)
        patch.require(patch.digest(destination) == expected, 'Save changed during backup: ' + name)
    backup_data = {'format': 'seraphic-blue-save-backup-v1', 'files': [
        {'path': name, 'sha256': digest} for name, digest in selected]}
    (backup / BACKUP_MANIFEST).write_text(json.dumps(backup_data, indent=2) + '\n', encoding='utf-8')
    backup_snapshot = patch.tree_snapshot(backup)
    patch.require(patch.tree_snapshot(saves) == snapshots[saves], 'Source saves changed during backup; stop and close the game')
    try:
        # The base installer prints a play instruction before migration; withhold it.
        with contextlib.redirect_stdout(io.StringIO()):
            patch.apply(base, staging)
        for candidate in staging.iterdir():
            if SAVE_NAME.fullmatch(candidate.name):
                patch.no_links(candidate)
                patch.require(candidate.is_file(), 'Bundled save target is not a regular file')
                candidate.unlink()
        for name, expected in selected:
            source = patch.located(backup, name)
            patch.require(patch.digest(source) == expected, 'Backup integrity check failed: ' + name)
            destination = patch.located(staging, name)
            shutil.copyfile(source, destination)
            patch.require(patch.digest(destination) == expected, 'New save integrity check failed: ' + name)
        patch.require(patch.tree_snapshot(backup) == backup_snapshot, 'Backup changed during update')
        for source, expected in snapshots.items():
            patch.require(patch.tree_snapshot(source) == expected, 'Source changed during update: ' + str(source))
        for name, expected in selected:
            patch.require(patch.digest(patch.located(staging, name)) == expected, 'Final new save check failed: ' + name)
        patch.no_links(output)
        patch.require(not os.path.lexists(output), 'Output appeared during update; refusing to replace it')
        staging.rename(output)
    except BaseException:
        if staging.is_dir():
            patch.no_links(staging)
            (staging / INCOMPLETE).write_text('Update failed. This partial new copy is unusable. Keep the old game and verified backup.\n', encoding='ascii')
        raise
    print('Update verified. Old game and source saves were not written. Backup: ' + str(backup), flush=True)
    print('Play the new copy: ' + str(output), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--base', required=True, help='pristine same-edition game extraction, read only')
    parser.add_argument('--current', required=True, help='supported same-edition test.1 game, read only')
    parser.add_argument('--saves', required=True, help='actual folder containing latest SaveNN.lsd; current game folder by default, or exact --save-path/fallback folder')
    parser.add_argument('--out', required=True, help='new nonexistent game folder')
    parser.add_argument('--backup', required=True, help='new nonexistent save-backup folder')
    args = parser.parse_args()
    try:
        update(args.base, args.current, args.saves, args.out, args.backup)
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        parser.exit(1, 'Update stopped: %s\nOld game and source saves were not written. A partial new copy may remain; do not play it.\n' % error)


if __name__ == '__main__':
    main()
