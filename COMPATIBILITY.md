# Compatibility — test.3

Windows x86-64 custom Player; opt-in field clicking and direct main-menu selection. Steam Deck uses the identical Windows binary through Proton and remains hardware-unverified. The native Ubuntu22.04 download remains test.2 without field clicking or the new main-menu selection. Fullgame Flatpak retains stock-runtime limits.

## Field clicking

With ClickWalk=1 and MouseDecide=1, click the ground to follow a four-direction route around current blockers. Click an NPC/event's ground tile to approach a cardinal adjacent tile and interact once. A new click replaces the route. Keyboard arrows or right-click cancel it.

Field clicking is restricted to ordinary free movement. Dialogue, battles, menus, forced movement and scripted transitions suspend it. Event sprites can extend above their actual ground tile; click their feet. It does not choose dialogue options or repeat interaction automatically.

## Main menu mouse selection

With BattleUI=1 and MouseDecide=1 in the existing [SB] section of EasyRPG.ini, move the pointer over ITEM, ABILITY, STATUS, ARM, SUPPLEMENT, DICTIONARY, ORGANIZE, EXTEND or MOD to highlight that button immediately. Click to select and open the button under the pointer. In the ABILITY/STATUS/ARM party picker, hover or click an occupied party portrait. A stationary pointer leaves keyboard selection alone. Disabled ORGANIZE and outside/empty clicks do not confirm.

Battle categories and ability/item rows retain the test.2 hover and direct-click behavior with BattleUI=1 and BattleMouse=1. Other picture submenus keep their existing selected-command behavior.

Windows build passed. Focused engine tests: 15 cases and 345 assertions, including obstacle routing, unreachable targets, moving NPC approach once, cancellation, context gates and mouse mapping. Actual native field replay reached the clicked tile and preserved source save/map bytes; full native menu Ability hover visually accepted. Four battle category and ability hover/click regressions passed. Separate native main-menu checks passed 31 cases. Automated replay and engine fixtures do not claim physical mouse or Steam Deck/Linux runtime testing. NPC targeting uses the event feet tile.

Player SHA256 f94387c12b7247c1a8ed04a1316a15e0eb89b2bda58ef13223e0715074298814. Existing battle/MOD checks belong to test.2 and are not a new complete gameplay pass. Full playthrough, universal save compatibility and physical Deck input remain unverified.
