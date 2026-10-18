# Install test.4 mouse controls

## Updating an existing Windows installation safely

1. Close the game. Copy your actual save folder somewhere safe. Saves are Save*.lsd files; keep Save*.sav files too if present. If your shortcut or .cmd launcher includes --save-path, use that folder. Otherwise check the game folder. Do not guess from the Player download folder.
2. Download the Windows Player ZIP for test.4 and extract it into a NEW runtime folder. It contains Player.exe and its 42 DLLs; it contains no game database, maps or saves. Keep the old runtime for rollback.
3. Point your existing shortcut/launcher at the new Player.exe. Keep its --project-path, --save-path and --config-path values exactly as they were. If your installation keeps Player.exe inside the game folder, you may instead copy ONLY Player.exe and the 42 matching DLLs there after closing the game; leave every other file alone.
4. Keep your current EasyRPG.ini. Under its existing [SB] section, BattleUI=1, BattleMouse=1 and MouseDecide=1 enable these controls. Do not replace the whole INI or duplicate keys. Launch and check that your usual saves appear before continuing.

This runtime update does not overwrite or migrate saves. A backup still protects against selecting the wrong folder or later saving over a slot. Do not reapply the test.1-to-test.2 game updater to an already updated game. Future releases that change game data may need different instructions: read that release's install guide instead of copying every ZIP over the game.

## Enemy targets and battle list pages

Click a visible enemy sprite to select and confirm it for a single-target attack. Empty background, transparent sprite pixels, missing and defeated enemies do not confirm. Clicking an enemy switches an optional all-target selection back to that enemy; forced all-target abilities keep targeting everyone. Keyboard targeting and wheel target cycling remain available.

While choosing a battle ability or item, scroll down for the next page and up for the previous page. All magic categories and battle item lists use this same paging route. Move the pointer to highlight a row; click it to choose it. Multi-page lists show < current/total > above the list, with clickable previous/next arrows. Paging wraps at the ends, matching keyboard Left/Right. Single-page lists stay on their page. Other menus retain their existing controls.


## Enable field clicking in an existing test.2 game

1. Make an ordinary save, close the game and back up your actual save folder. If your launcher has --save-path, that exact folder holds your saves; keep using it.
2. Extract the test.4 Windows Player into a NEW runtime folder. Keep Player.exe and all 42 DLLs together. Keep the old runtime for rollback.
3. Open EasyRPG.ini inside your patched GAME folder. Under its existing [SB] section, add ClickWalk=1 and keep MouseDecide=1. Change existing values instead of adding duplicate keys or a second [SB] section. Keep every other setting. RPG_RT.ini is a different file.

```ini
[SB]
MouseDecide=1
ClickWalk=1
```

4. Launch the NEW runtime with your SAME game and actual save path. Use full paths in your own launcher:

```sh
"NEW-RUNTIME/Player.exe" --project-path "EXISTING-TEST2-GAME" --save-path "ACTUAL-EXISTING-SAVE-FOLDER"
```

This changes the runtime and opt-in configuration only. Do not run the test.1-to-test.2 updater again for a test.2 game. Do not replace the game data or move saves for this runtime update. To turn field clicking off, set ClickWalk=0. Roll back by selecting the old runtime and restoring your configuration backup.

## Field clicking

With ClickWalk=1 and MouseDecide=1, click the ground to follow a four-direction route around current blockers. Click an NPC/event's ground tile to approach a cardinal adjacent tile and interact once. A new click replaces the route. Keyboard arrows or right-click cancel it.

Field clicking is restricted to ordinary free movement. Dialogue, battles, menus, forced movement and scripted transitions suspend it. Event sprites can extend above their actual ground tile; click their feet. It does not choose dialogue options or repeat interaction automatically.

## Main menu mouse selection

With BattleUI=1 and MouseDecide=1 in the existing [SB] section of EasyRPG.ini, move the pointer over ITEM, ABILITY, STATUS, ARM, SUPPLEMENT, DICTIONARY, ORGANIZE, EXTEND or MOD to highlight that button immediately. Click to select and open the button under the pointer. In the ABILITY/STATUS/ARM party picker, hover or click an occupied party portrait. A stationary pointer leaves keyboard selection alone. Disabled ORGANIZE and outside/empty clicks do not confirm.

Battle categories and ability/item rows retain the test.2 hover and direct-click behavior with BattleUI=1 and BattleMouse=1. Other picture submenus keep their existing selected-command behavior.

## Fresh game installation or older test.1 game

Use the unchanged [EN test.2 patch](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-en-patch-v0.1.0-test.2.zip) or [JP test.2 patch](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-ja-patch-v0.1.0-test.2.zip). Once your test.2 game is ready, follow the runtime-only steps above. Native Linux remains test.2 without field clicking; its unchanged setup is documented in the [test.2 install guide](https://github.com/Nostramadeus/seraphic-blue-mod/blob/v0.1.0-test.2/INSTALL.md).

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
