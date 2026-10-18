# Seraphic Blue MOD — v0.1.0-test.5

## Enemy hover selection

With BattleUI=1, BattleMouse=1 and MouseDecide=1 in the existing [SB] section of EasyRPG.ini, move the pointer over a visible enemy sprite to select it. The enemy name, target icon and cursor follow the selected enemy. Hover selects only; click to confirm the action once.

Moving over empty background, transparent sprite pixels, hidden, missing or defeated enemies leaves the choice alone. A stationary pointer leaves keyboard and wheel selection alone, and held direction keys take priority. Hover preserves optional and forced all-target selection; an explicit enemy click can return optional all-target selection to one enemy.

This is a runtime-only update. Close the game, back up your actual save folder, and extract the Windows Player ZIP into a NEW runtime folder. Keep Player.exe and all 42 DLLs together. Point your existing launcher to the new Player.exe while retaining its --project-path, --save-path and --config-path values. Preserve EasyRPG.ini, game data and saves. The detailed safe-update instructions below still apply.


## Updating an existing Windows installation safely

1. Close the game. Copy your actual save folder somewhere safe. Saves are Save*.lsd files; keep Save*.sav files too if present. If your shortcut or .cmd launcher includes --save-path, use that folder. Otherwise check the game folder. Do not guess from the Player download folder.
2. Download the Windows Player ZIP for test.5 and extract it into a NEW runtime folder. It contains Player.exe and its 42 DLLs; it contains no game database, maps or saves. Keep the old runtime for rollback.
3. Point your existing shortcut/launcher at the new Player.exe. Keep its --project-path, --save-path and --config-path values exactly as they were. If your installation keeps Player.exe inside the game folder, you may instead copy ONLY Player.exe and the 42 matching DLLs there after closing the game; leave every other file alone.
4. Keep your current EasyRPG.ini. Under its existing [SB] section, BattleUI=1, BattleMouse=1 and MouseDecide=1 enable these controls. Do not replace the whole INI or duplicate keys. Launch and check that your usual saves appear before continuing.

This runtime update does not overwrite or migrate saves. A backup still protects against selecting the wrong folder or later saving over a slot. Do not reapply the test.1-to-test.2 game updater to an already updated game. Future releases that change game data may need different instructions: read that release's install guide instead of copying every ZIP over the game.

## Enemy targets and battle list pages

Click a visible enemy sprite to select and confirm it for a single-target attack. Empty background, transparent sprite pixels, missing and defeated enemies do not confirm. Clicking an enemy switches an optional all-target selection back to that enemy; forced all-target abilities keep targeting everyone. Keyboard targeting and wheel target cycling remain available.

While choosing a battle ability or item, scroll down for the next page and up for the previous page. All magic categories and battle item lists use this same paging route. Move the pointer to highlight a row; click it to choose it. Multi-page lists show < current/total > above the list, with clickable previous/next arrows. Paging wraps at the ends, matching keyboard Left/Right. Single-page lists stay on their page. Other menus retain their existing controls.


Optional field click walking, one-time NPC interaction and direct main-menu mouse selection for the custom Windows Player and Steam Deck Proton TEST route. Existing test.2 EN/JP game patches are unchanged.

## Field clicking

With ClickWalk=1 and MouseDecide=1, click the ground to follow a four-direction route around current blockers. Click an NPC/event's ground tile to approach a cardinal adjacent tile and interact once. A new click replaces the route. Keyboard arrows or right-click cancel it.

Field clicking is restricted to ordinary free movement. Dialogue, battles, menus, forced movement and scripted transitions suspend it. Event sprites can extend above their actual ground tile; click their feet. It does not choose dialogue options or repeat interaction automatically.

## Main menu mouse selection

With BattleUI=1 and MouseDecide=1 in the existing [SB] section of EasyRPG.ini, move the pointer over ITEM, ABILITY, STATUS, ARM, SUPPLEMENT, DICTIONARY, ORGANIZE, EXTEND or MOD to highlight that button immediately. Click to select and open the button under the pointer. In the ABILITY/STATUS/ARM party picker, hover or click an occupied party portrait. A stationary pointer leaves keyboard selection alone. Disabled ORGANIZE and outside/empty clicks do not confirm.

Battle categories and ability/item rows retain the test.2 hover and direct-click behavior with BattleUI=1 and BattleMouse=1. Other picture submenus keep their existing selected-command behavior.

## Enable field clicking in an existing test.2 game

1. Make an ordinary save, close the game and back up your actual save folder. If your launcher has --save-path, that exact folder holds your saves; keep using it.
2. Extract the test.5 Windows Player into a NEW runtime folder. Keep Player.exe and all 42 DLLs together. Keep the old runtime for rollback.
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

## Downloads

- [Windows Player](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.5/seraphic-blue-player-windows-x86_64-v0.1.0-test.5.zip)
- [Deck Proton TEST Player](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.5/seraphic-blue-player-steamdeck-proton-TEST-v0.1.0-test.5.zip)
- [Complete corresponding Player source](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.5/seraphic-blue-player-source-v0.1.0-test.5.zip)
- [Unchanged EN patch](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-en-patch-v0.1.0-test.2.zip) / [unchanged JP patch](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-ja-patch-v0.1.0-test.2.zip)
- [Unchanged dependency sources](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-dependency-sources-v0.1.0-test.2.zip)
- [Native Ubuntu22.04 test.2 Player, without field clicking](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-player-ubuntu22.04-x86_64-v0.1.0-test.2.zip)

Read [INSTALL](INSTALL.html), [COMPATIBILITY](COMPATIBILITY.html), [Deck Proton guide](STEAM-DECK-PROTON-TEST.html), and [SOURCE-ACCESS](SOURCE-ACCESS.md). New installs apply the existing test.2 patch first, then enable this runtime.

## Retained test.2 battle controls

- Click a battle category to select and enter it. Move the pointer to highlight native categories and ability/item rows. A stationary pointer leaves keyboard selection alone.
- Disabled rows may highlight, but clicking does not confirm them. Empty and outside row clicks do nothing.
- Wheel up/down cycles main commands left/right and categories vertically; ability/item wheels change pages. During enemy selection it uses native Left/Right to cycle eligible living targets. Physical Up/Down retains the all-target toggle. Detailed data pages still use Decide/Back.
- Action-time labels show short actor/enemy names without hover. Only duplicates get numbers, ranked by occupied slots even while a marker is hidden. Native target opacity is retained.
- Left click advances text; right click is Back. Keyboard arrows/Enter/Escape remain available. Hold F/G for the built-in configurable 3x/10x fast-forward defaults.
- Main-menu mouse selection is described above; other picture submenus keep their existing selected-command behavior. Enemy sprite clicking is now supported as described above. MOD settings and optional cheats remain available.


## Steam Deck: full game for stock EasyRPG Flatpak

[Download the full English game with test.1 MOD data](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.2/seraphic-blue-fullgame-EN-test1-flatpak-TEST.zip) and read the [Flatpak setup guide](STEAM-DECK-FLATPAK-TEST.html). Extract it into a new folder on Deck, install EasyRPG Player from Discover and select the included game folder in its setup wizard. No Python, patching or Proton is needed. The event-based MOD menu remains available through keyboard/Steam Input controls. Custom pause skipping, battle mouse/wheel input, animation acceleration and test.2 timeline labels require our custom Player. Hardware and Flatpak runtime remain untested.

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

## Source and rights

See [SOURCE-ACCESS](SOURCE-ACCESS.md), [SOURCES](SOURCES.json), [LICENSES](LICENSES.md) and [CREDITS](CREDITS.md). MIT covers our authored scripts/docs only. Player, libraries, game, translation and derived art retain their own rights. No endorsement or new republication permission is implied.
