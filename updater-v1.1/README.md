# Seraphic Blue Updater v1.1.1

v1.1.1 (2026-10-27) fixes the Windows GUI update that stopped after downloading with "The property 'Text' cannot be found on this object".

Extract the whole ZIP into its own folder. Keep payload/ and launchers/ together. Close the game before updating. The updater supports matching full-game releases; custom launchers and linked folders need manual handling.

## Windows

1. Double-click SeraphicBlue-Update.exe.
2. Click Choose and select your current game folder.
3. Click Update to latest for a manual update. Or click Enable startup checks to check when opening PLAY.cmd.
4. To stop startup checks, select the same folder and click Disable startup checks. This restores the original launcher byte-exact.

The startup switch works without a newer release or network connection. Windows PowerShell and .NET Framework are used; no dependencies are installed.

## Linux / Steam Deck desktop

1. Open Startup-settings.desktop from this extracted folder. Your desktop may ask you to trust/run the entry.
2. Select the game folder and choose Enable startup checks.
3. Open that game's play-linux.sh. A newer matching stable release offers Install update or Play current.
4. To disable checks, open Startup-settings.desktop again, select the same folder and choose Disable startup checks.

Python 3 and an existing kdialog or zenity are required for graphical setup and prompts. No dependencies are installed. Missing desktop tools are a manual limitation; startup checks quietly continue the current game if tools are missing. There is no separate Linux Update now button: enable checks, launch play-linux.sh, and disable them afterward if you only want one check.

## What stays safe

- Updates are optional. Only a newer stable release for the same edition can prompt. Offline/error startup checks continue the current game.
- A new neighboring version folder receives verified saves/settings and the managed Auto sidecars. The old game and a verified backup are retained. The new copy keeps startup checks enabled after an accepted startup update.
- Free space is checked before download and again before backup/extraction. ZIP paths, hashes, manifest and personal-data copies are checked. Partial downloads/backups may remain after an error; use the old game.
- Direct Player.exe / Player shortcuts bypass startup checks. Steam shortcuts are not changed: point them to PLAY.cmd or play-linux.sh in the version folder you want to play. No Proton launch options are added.

Physical Steam Deck / Proton behavior has not been verified. Native Linux updater logic and dialog commands were checked with disposable fixtures and stubs.

## Included source

Runtime source is in payload/ and the root installers. Bootstrap source/build script is in source/. If rebuilding the Windows bootstrap with the existing .NET Framework compiler, run source/build_gui.ps1, then copy its generated SeraphicBlue-Startup-Settings.exe beside payload/ (it may be named SeraphicBlue-Update.exe). No debug symbols are included. MIT notice: LICENSE-MIT.txt.
