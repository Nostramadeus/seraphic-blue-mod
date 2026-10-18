# Release notes — v0.1.0-test.3

## Field clicking

With ClickWalk=1 and MouseDecide=1, click the ground to follow a four-direction route around current blockers. Click an NPC/event's ground tile to approach a cardinal adjacent tile and interact once. A new click replaces the route. Keyboard arrows or right-click cancel it.

Field clicking is restricted to ordinary free movement. Dialogue, battles, menus, forced movement and scripted transitions suspend it. Event sprites can extend above their actual ground tile; click their feet. It does not choose dialogue options or repeat interaction automatically.

## Main menu mouse selection

With BattleUI=1 and MouseDecide=1 in the existing [SB] section of EasyRPG.ini, move the pointer over ITEM, ABILITY, STATUS, ARM, SUPPLEMENT, DICTIONARY, ORGANIZE, EXTEND or MOD to highlight that button immediately. Click to select and open the button under the pointer. In the ABILITY/STATUS/ARM party picker, hover or click an occupied party portrait. A stationary pointer leaves keyboard selection alone. Disabled ORGANIZE and outside/empty clicks do not confirm.

Battle categories and ability/item rows retain the test.2 hover and direct-click behavior with BattleUI=1 and BattleMouse=1. Other picture submenus keep their existing selected-command behavior.

## Enable field clicking in an existing test.2 game

1. Make an ordinary save, close the game and back up your actual save folder. If your launcher has --save-path, that exact folder holds your saves; keep using it.
2. Extract the test.3 Windows Player into a NEW runtime folder. Keep Player.exe and all 42 DLLs together. Keep the old runtime for rollback.
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

Only Windows/Proton runtime and corresponding source are new. EN/JP patches and dependency versions remain test.2. Native Ubuntu22.04 remains test.2 without field clicking or the new main-menu mouse selection; the fullgame Flatpak addon keeps test.1 data and stock-runtime limits. No Steam Deck/Proton/Flatpak hardware verification is claimed.
