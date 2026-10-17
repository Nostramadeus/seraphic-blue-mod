# Install the Seraphic Blue test MOD

These instructions cover the test.2 patches, which need your own supported original game. For a separate full English game with older test.1 MOD data, see STEAM-DECK-FLATPAK-TEST.html. The patch archives contain no full game, original executable, separately added RTP sounds or Windows fonts. Back up the game and saves; close the game before copying.

## Choose one edition

EN requires the exact English Director's Cut extraction identified by RPG_RT.ldb SHA256 abc355a601abb2bf1d2eb744d76a114eb1adc6e7841b5974561d18e4a4621288. JP requires the exact Japanese Director's Cut extraction identified by RPG_RT.ldb SHA256 8da84e7cd40d3a0153f6392b4a0e7bf40eb302e65ad49d5b07d3771ad2a63d53. These are exact-content fingerprints, not an independent download-provenance guarantee. The installer checks the complete supported base, not only this database.

## Apply into a new copy

Extract the matching patch separately from the untouched original. Use Python 3.10 or newer. Run commands from the extracted patch directory, not the standalone repository source copy.

Windows:
```sh
py -3 apply_patch.py --base "PATH-TO-ORIGINAL" --out "NEW-GAME-FOLDER"
```

Linux x86-64:
```sh
chmod +x tools/linux-x86_64/xdelta3decode
python3 apply_patch.py --base "PATH-TO-ORIGINAL" --out "NEW-GAME-FOLDER"
```

The output must not exist or overlap the game/patch. Wrong base or corrupt inputs stop before creating output. Original files and saves remain read-only; existing saves copy unchanged. Later decoding failure can leave a partial output: do not play it. Resolve the error and retry with a fresh output path.

## Launch the custom Player

Windows: extract the Windows Player package, keep its 42 DLLs beside Player.exe, and launch Player.exe --project-path "NEW-GAME-FOLDER" --save-path "NEW-GAME-FOLDER". Alternatively place those Player files beside RPG_RT.ldb and use the current-directory command below. Keep the patch's EasyRPG.ini.

```sh
Player.exe --project-path . --save-path .
```

Linux: the native package targets Ubuntu 22.04 x86-64 and bundles only liblcf; it is not universal. On an Ubuntu 22.04 system, install these runtime packages (APT also installs their dependencies):

```sh
sudo apt update
sudo apt install libsdl2-2.0-0 libfmt8 libicu70 libexpat1 libinih1 libpixman-1-0 libpng16-16 libfreetype6 libharfbuzz0b libmpg123-0 libvorbisfile3 libopusfile0 libfluidsynth3 libsndfile1 libspeexdsp1 libxmp4 libreadline8
```

From the extracted native Player directory, launch with:

```sh
chmod +x Player
./Player --project-path "PATH-TO-PATCHED-GAME" --save-path "PATH-TO-PATCHED-GAME"
```

These package names match the recorded Ubuntu 22.04 build environment; this installation command was not run on a new machine. If a library is missing, check runtime-dependency-names.txt and ldd ./Player. Do NOT apply these APT instructions to SteamOS. Steam Deck users follow the separate hardware-unverified Proton TEST guide/package, not an assumed native-compatible binary.

## Controls in test.2

- Click a battle category to select and enter it. Move the pointer to highlight native categories and ability/item rows. A stationary pointer leaves keyboard selection alone.
- Disabled rows may highlight, but clicking does not confirm them. Empty and outside row clicks do nothing.
- Wheel up/down cycles main commands left/right and category/ability lists vertically. During enemy selection it uses native Left/Right to cycle eligible living targets. Physical Up/Down retains the all-target toggle. Detailed data pages still use Decide/Back.
- Action-time labels show short actor/enemy names without hover. Only duplicates get numbers, ranked by occupied slots even while a marker is hidden. Native target opacity is retained.
- Left click advances text; right click is Back. Keyboard arrows/Enter/Escape remain available. Hold F/G for the built-in configurable 3x/10x fast-forward defaults.
- Other picture menus keep their existing selected-command behavior. Target-sprite clicking and click-to-walk are not included. MOD settings and optional cheats remain available.

## Update from matching test.1 and keep saves

Make an ordinary Memory Tree save and close the game. Extract the matching EN or JP test.2 patch separately. Keep your untouched pristine base, supported same-edition test.1 game and actual save folder. The --saves folder must match the old launcher's --save-path; if it used the default, use the old game folder. Do not guess a custom save location.

Windows, from the extracted patch directory:
```sh
py -3 update_game.py --base "PRISTINE-BASE" --current "OLD-TEST1-GAME" --saves "ACTUAL-OLD-SAVE-FOLDER" --out "NEW-GAME-FOLDER" --backup "NEW-SAVE-BACKUP"
```

Linux, from the extracted patch directory (first chmod +x tools/linux-x86_64/xdelta3decode):
```sh
python3 update_game.py --base "PRISTINE-BASE" --current "OLD-TEST1-GAME" --saves "ACTUAL-OLD-SAVE-FOLDER" --out "NEW-GAME-FOLDER" --backup "NEW-SAVE-BACKUP"
```

The updater prints the selected save files/count, creates a verified backup, builds a separate new game and checks copied save bytes. New output and backup paths must not exist. It supports the exact matching test.1 database only; no arbitrary-version, cross-edition or mid-event debug-save compatibility is claimed. A failed/interrupted .partial folder is unusable; keep it separate and retry with fresh paths after resolving the cause. Keep the old game and verified backup.

Launch the NEW game with its NEW save folder, not the old custom path:
```sh
Player.exe --project-path "NEW-GAME-FOLDER" --save-path "NEW-GAME-FOLDER"
./Player --project-path "NEW-GAME-FOLDER" --save-path "NEW-GAME-FOLDER"
```

## Backup, sounds and rollback

Keep untouched originals and save backups. No universal cross-version save compatibility or full playthrough is claimed. Restore your untouched backup to roll back. The 19 separately sourced RTP sounds are omitted: use the official RPG Maker 2000 RTP installation when needed: https://rpgmakerofficial.com/support/rtp/ . Preserve the original manual and complete credits. This unofficial patch does not establish game/translation republication permission.
