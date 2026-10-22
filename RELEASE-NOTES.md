# Release notes — v0.1.0-test.13

## Translation corrections from the comparison review

- **21 dialogue boxes corrected** after an outside check: while the [comparison page](https://nostramadeus.github.io/seraphic-blue-mod/) was being built, its reviewers compared our lines with the Japanese and flagged the few where ours was weaker (a dropped qualifier, a Japanese idiom flattened into plain English, one word read in the wrong sense). Those are fixed. 4 boxes also had a pause moved to the line end (cosmetic).
- Changed files: 21 map files. No Player, picture or save changes.

## Update safely

1. Close the game and back up the actual save folder used by your launcher.
2. Easiest: download **seraphic-blue-fullgame-EN-v0.1.0-test.13.zip**, extract it, and copy your old **saves** folder into it.
3. Or, on test.11 or test.12: extract **seraphic-blue-update-v0.1.0-test.13.zip** into the game folder containing **RPG_RT.ldb** and replace the 21 map files. On test.10 or older, apply the test.11 update first (it carries the Player).
4. Keep your saves, config, EasyRPG.ini and DLLs. Launch as usual.

## Known limits

- Map data only; the Player is unchanged since test.11.
- Verified by whole-page replay checks against the translation sources and a file-level verifier, not a full playthrough.

# Earlier: release notes — v0.1.0-test.12

## Translation corrections, part two

- **63 more dialogue boxes corrected to match the Japanese.** This completes the audit of all 3,013 "full" four-line boxes (the ones most likely to have been shortened to fit): 89 of them had lost a qualifier, a hedge, a clause or a Japanese idiom's image, and all are restored. 2 of the new corrections use two boxes instead of one shortened box.
- Changed files: 45 map files. No Player, picture or save changes.
- **Old saves work.** A save from the Japanese original, from the 2016 English patch or from any test release loads in this version: copy your SaveXX.lsd files into the **saves** folder.

## Update safely

1. Close the game and back up the actual save folder used by your launcher.
2. Easiest: download **seraphic-blue-fullgame-EN-v0.1.0-test.12.zip**, extract it, and copy your old **saves** folder into it.
3. Or, on test.11: extract **seraphic-blue-update-v0.1.0-test.12.zip** into the game folder containing **RPG_RT.ldb** and replace the 45 map files. On test.10 or older, apply the test.11 update first (it carries the Player).
4. Keep your saves, config, EasyRPG.ini and DLLs. Launch as usual.

## Known limits

- Map data only; the message-history Player from test.11 is unchanged.
- Verified by whole-page replay checks against the translation sources and a file-level verifier, not a full playthrough.

# Earlier: release notes — v0.1.0-test.11

## Message history and translation corrections

- **Message history (Windows Player):** scroll back through the last 100 message boxes you read, with the choice you picked. Open it with **mouse wheel up** or **Page Up** while a message is showing or while you walk on the field; scroll with the wheel or Up / Down, page with Page Up / Page Down, close with **Escape / B / right click**. It is cleared when you load or start a game and is never saved. The native Linux Player and the Mac Player do not have it.
- **67 dialogue boxes corrected to match the Japanese** (dropped qualifiers or hedges restored, Japanese idioms kept as their own image, 14 names and terms made consistent with the in-game dictionary). 7 of them now use two boxes instead of one shortened box. All 585 boxes whose English was identical to the 2016 patch were checked against the Japanese and found correct.
- Changed files: Player.exe and 43 map files. Saves, config and EasyRPG.ini are untouched; earlier saves load normally.

## Update safely

1. Close the game and back up the actual save folder used by your launcher.
2. Easiest: download **seraphic-blue-fullgame-EN-v0.1.0-test.11.zip**, extract it, and copy your old **saves** folder into it.
3. Or, on test.8 or newer: extract **seraphic-blue-update-v0.1.0-test.11.zip** into the game folder containing **RPG_RT.ldb** and replace **Player.exe** and the 43 map files. If your Player.exe is in a different folder (older patch installs), copy the new Player.exe there.
4. Keep your saves, config, EasyRPG.ini and DLLs. Launch as usual.

## Known limits

- Message history needs the included Windows Player (Windows, Linux/Deck through Proton). The native Linux Player and the stock Mac Player keep the older behaviour.
- The history holds completed message pages only; it never shows text you have not reached yet. It is not stored in save files.
- Verified with the Player's own automated tests and scripted off-screen runs, not a full playthrough or hardware test.

# Earlier: release notes — v0.1.0-test.8

## Early MOD access and opening fixes

- **MOD settings from the very start.** While the story still locks the game menu (the opening chapters), Cancel / Esc / controller B (Steam Deck B) opens the MOD screen directly. Cancel returns to the field at the same spot. The CHEATS page is skipped there because no party menu exists yet. After the normal unlock, Cancel opens the ordinary menu with its MOD button, exactly as before.
- Cancel inside message boxes, choices and scenes does nothing new: the Player only lets the press through while you have free control of the field (no message, no running or starting event, no map transfer).
- **Clicking to walk now works in the opening rooms.** Click-to-walk had required the unlocked game menu; it now uses only the field-control checks, so it works as soon as you can walk.
- **Opening poem card** (Picture/Ep00_Mes05-02.png): the second card of the opening poem is retranslated to match the Japanese.
- Changed files: Player.exe, RPG_RT.ldb, Map0003.lmu, Picture/Ep00_Mes05-02.png. Saves, config and EasyRPG.ini are untouched; earlier saves load normally.

## Update safely

1. Close the game and back up the actual save folder used by your launcher.
2. If you are on test.6 or older, first extract **seraphic-blue-image-update-v0.1.0-test.7.zip** from the [test.7 release](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.1.0-test.7).
3. Extract **seraphic-blue-update-v0.1.0-test.8.zip** into the game folder containing **RPG_RT.ldb** and replace the included files. If your Player.exe is in a different folder (older patch installs), copy the new Player.exe there.
4. Keep your saves, config, EasyRPG.ini and DLLs. Launch as usual.

New players can use **seraphic-blue-fullgame-EN-v0.1.0-test.8.zip**.

## Known limits

- Early MOD access and the opening click-walk fix need the included Windows Player (Windows, Linux/Deck through Proton). The native Linux Player (test.2) and the stock Mac Player keep the older behaviour: MOD opens after the story unlocks the menu, and clicks do not walk.
- English build only; the Japanese patch is not updated in this release.
- Tested with scripted, off-screen runs (new game through the opening room, existing saves, the unlocked menu). No full playthrough or hardware test.
- The Player source with these changes is **seraphic-blue-player-source-v0.1.0-test.8.zip** in this release.
