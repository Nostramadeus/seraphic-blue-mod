# Release notes — v0.1.0-test.8

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
