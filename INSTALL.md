# Advanced patch installation and migration

For a new full-game install, use [Windows](WINDOWS.md), [Linux](LINUX.md), or [Steam Deck](STEAM-DECK.md). The complete English game includes its MOD and Players. The instructions below describe the optional patch-based route and existing installations.

# Install or update v0.1.0-test.6

## Update safely

1. Close the game and back up your actual save folder. Saves are Save*.lsd files. If your launcher includes --save-path, that folder is authoritative; otherwise locate your existing saves in the game folder.
2. Extract the test.6 Windows Player ZIP into a NEW runtime folder. Keep Player.exe and its 42 DLLs together. Keep the previous runtime for rollback.
3. Point your existing launcher at the new Player.exe. Retain its --project-path, --save-path and --config-path arguments. Keep your existing game data and EasyRPG.ini. If Player lives inside the game folder, replace only Player.exe and its matching DLLs after closing it; leave every other file alone.
4. Under the existing [SB] section of EasyRPG.ini, retain BattleUI=1, BattleMouse=1, MouseDecide=1 and ClickWalk=1. Change existing keys instead of duplicating them. Launch and check your usual saves before continuing.

This release updates the runtime only. It contains no game database, maps or saves and does not migrate save data. Do not reapply a game-data updater to an already matching test.2 game. Future releases may have different update instructions.

## What changed

- Move the mouse over selectable menu rows/buttons to update their native highlight and information immediately. A stationary pointer leaves keyboard/controller selection alone. Click chooses the pointed entry; empty or outside clicks do not confirm the previous selection.
- Battle ally targets now support hover and click. Native healing/revival rules remain authoritative; dead allies are not incorrectly excluded. Hover preserves an existing all-target choice. Enemy hover, click targeting and battle page controls from test.5 remain available.
- Item, ability, equipment, Supplement, Organize, Upgrade, shop, dictionary and native choice/title/save/load screens gain pointer controls appropriate to their layout. Hover only selects; it does not spend items, money, upgrades or an attack.
- Status / Gear / Ability quick tabs retain the selected character. Page Up/Down also cycles these tabs at stable top-level screens; native Left/Right still changes characters. Abilities remains unavailable for reserve characters. Equipment changes are written back before switching screens.
- Native hidden-key hints are preserved; Gear and the battle command screen add compact Shift hints where space permits. Shop quantity has visible -10/-1/+1/+10 and Buy/Sell buttons. Supplement has Apply; Upgrade has an Upgrade button. Hover selects amount digits; the wheel adjusts through native rules.
- Field click walking shows a white hovered-tile outline and a green accepted-destination outline. The destination clears on arrival, manual cancellation or a failed route. NPC clicking still approaches and interacts once.

## Pointer and controller behavior

Mouse movement updates focus on supported selectable controls. Descriptive text and artwork are not treated as buttons. Native number-entry digits and name-entry keyboards keep their existing controls. Native disabled/locked rules, special party restrictions and short final pages remain in charge. Up/down arrows, Enter/Decide, Escape/Back and existing shortcuts remain available. Wheel input changes pages in paged lists; it follows the native row/amount behavior in target, history and amount contexts.

Quick tabs appear only at stable top-level character screens, never during an unfinished target or equipment transaction. Tab hover is feedback only; click or Page Up/Down switches. A reserve character is retained rather than silently replaced by an active character.

## First installation

Start from the matching English or Japanese game and the existing matching test.2 game patch. Follow its edition-specific installation guide, then select this new Player runtime. Keep existing save-path arguments when upgrading an installation.

## Tested limits

Focused native replay/build evidence is listed in [COMPATIBILITY](COMPATIBILITY.html). No physical Steam Deck/Proton, full-playthrough or universal-save compatibility claim is made.

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
