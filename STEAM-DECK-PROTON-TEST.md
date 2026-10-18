# Steam Deck Proton — TEST

Use the Windows binary from the Proton TEST package. Hardware has not been tested. Keep the existing game/save folders and their shortcut arguments.

## Update safely

1. Close the game and back up your actual save folder. Saves are Save*.lsd files. If your launcher includes --save-path, that folder is authoritative; otherwise locate your existing saves in the game folder.
2. Extract the test.6 Windows Player ZIP into a NEW runtime folder. Keep Player.exe and its 42 DLLs together. Keep the previous runtime for rollback.
3. Point your existing launcher at the new Player.exe. Retain its --project-path, --save-path and --config-path arguments. Keep your existing game data and EasyRPG.ini. If Player lives inside the game folder, replace only Player.exe and its matching DLLs after closing it; leave every other file alone.
4. Under the existing [SB] section of EasyRPG.ini, retain BattleUI=1, BattleMouse=1, MouseDecide=1 and ClickWalk=1. Change existing keys instead of duplicating them. Launch and check your usual saves before continuing.

This release updates the runtime only. It contains no game database, maps or saves and does not migrate save data. Do not reapply a game-data updater to an already matching test.2 game. Future releases may have different update instructions.

## Suggested Steam Input bindings

D-pad: arrow keys. A: Enter/Decide. B: Escape/Back. Right trackpad: mouse, click: left mouse. Left trigger: right mouse. X: Shift for secondary actions. Optional bumpers: Page Up/Page Down for character tabs. These are suggested keyboard/mouse mappings, not a verified hardware layout. Every screen retains its native keyboard route.

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

## Tested limits

Focused native replay/build evidence is listed in [COMPATIBILITY](COMPATIBILITY.html). No physical Steam Deck/Proton, full-playthrough or universal-save compatibility claim is made.
