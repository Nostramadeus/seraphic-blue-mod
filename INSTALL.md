# Install the Seraphic Blue test MOD

TEST release v0.1.0-test.1. You need your own supported original game. No full game, original executable, RTP sounds or Windows fonts are supplied. Back up the game and saves; close the game before copying.

## Choose one edition

EN requires the exact English Director's Cut extraction identified by RPG_RT.ldb SHA256 abc355a601abb2bf1d2eb744d76a114eb1adc6e7841b5974561d18e4a4621288. JP requires the exact Japanese Director's Cut extraction identified by RPG_RT.ldb SHA256 8da84e7cd40d3a0153f6392b4a0e7bf40eb302e65ad49d5b07d3771ad2a63d53. These are exact-content fingerprints, not an independent download-provenance guarantee. The installer checks the complete supported base, not only this database.

## Apply into a new copy

Extract the matching patch separately from the original game. Use Python 3.10+. On Windows run: py -3 apply_patch.py --base "PATH-TO-ORIGINAL" --out "NEW-GAME-FOLDER". On Linux x86-64, chmod +x tools/linux-x86_64/xdelta3decode then run: python3 apply_patch.py --base "PATH-TO-ORIGINAL" --out "NEW-GAME-FOLDER". Run the installer from its patch ZIP, not the standalone repository source copy.

The output must not exist or overlap the game/patch. Wrong base or corrupt inputs stop before creating output. Originals and saves are never opened for writing. Existing saves copy unchanged; no saves are included in downloads. A later decoding failure may leave a partial output: do not play it. Keep it separate and use a fresh output path after resolving the error.

## Launch the custom Player

Windows: extract the Windows Player package, keep its 42 DLLs beside Player.exe, and launch Player.exe --project-path "NEW-GAME-FOLDER". Alternatively place those Player files beside RPG_RT.ldb and use the current-directory command below. Keep the patch's EasyRPG.ini.

Player.exe --project-path .

Linux: the native package targets Ubuntu 22.04 x86-64 and bundles only liblcf; it is not universal. On an Ubuntu 22.04 system, install these runtime packages (APT also installs their dependencies):

sudo apt update
sudo apt install libsdl2-2.0-0 libfmt8 libicu70 libexpat1 libinih1 libpixman-1-0 libpng16-16 libfreetype6 libharfbuzz0b libmpg123-0 libvorbisfile3 libopusfile0 libfluidsynth3 libsndfile1 libspeexdsp1 libxmp4 libreadline8

From the extracted native Player directory, launch with:

chmod +x Player
./Player --project-path "PATH-TO-PATCHED-GAME"

These package names match the recorded Ubuntu 22.04 build environment; this installation command was not run on a new machine. If a library is missing, check runtime-dependency-names.txt and ldd ./Player. Do NOT apply these APT instructions to SteamOS. Steam Deck users follow the separate hardware-unverified Proton TEST guide/package, not an assumed native-compatible binary.

## Controls and optional MOD settings

Keyboard arrows/Decide/Back remain. Left click advances text; right click is Back. Battle wheel up/down cycles main commands left/right; category and ability/item lists move vertically. A valid list-row click selects that row before confirming. Other picture menus retain selected-command confirmation. MOD settings apply immediately and save with the game; each option lists its default. Cheats and balance changes are optional.

## Backup, sounds and rollback

Keep untouched originals and save backups. No universal cross-version save compatibility or full playthrough is claimed. Restore your untouched backup to roll back. The 19 separately sourced RTP sounds are omitted: use the official RPG Maker 2000 RTP installation when needed: https://rpgmakerofficial.com/support/rtp/ . Preserve the original manual and complete credits. This unofficial patch does not establish game/translation republication permission.
