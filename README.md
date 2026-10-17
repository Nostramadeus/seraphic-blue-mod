# Seraphic Blue MOD — v0.1.0-test.1

Unofficial TEST patches plus a custom EasyRPG Player. Bring your own supported game. No full game is distributed.

## Features and quick controls

| Control | What it does now |
| --- | --- |
| Mouse wheel in battle | Cycles main commands left/right; moves through magic categories and ability/item lists vertically. |
| Click an ability/item row | Selects the actual clicked row before confirming, instead of confirming the previously selected row. |
| Left click / right click | Advances text / goes back. Picture menus without direct hit testing still confirm their current selection. |
| Keyboard arrows / Enter / Escape | Navigate / confirm / go back; keyboard controls remain available. |
| Hold F / G | Built-in EasyRPG fast-forward: 3x / 10x by default, configurable in Player settings. This speeds up the whole game. |

The in-game MOD menu provides separate speed, battle and optional cheat settings. EN includes translation/art corrections; JP keeps Japanese text and adds the MOD features.

Not included yet: category direct-clicking, hover-to-highlight, wheel selection of enemy targets/data, or named action-time markers. Do not assume every picture-based menu supports direct clicking. See [tested limits](COMPATIBILITY.md).

## Downloads

Release and SHA256SUMS: https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.1.0-test.1

- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-en-patch-v0.1.0-test.1.zip
- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-ja-patch-v0.1.0-test.1.zip
- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-player-windows-x86_64-v0.1.0-test.1.zip
- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-player-ubuntu22.04-x86_64-v0.1.0-test.1.zip
- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-player-steamdeck-proton-TEST-v0.1.0-test.1.zip
- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-player-source-v0.1.0-test.1.zip
- https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.1/seraphic-blue-dependency-sources-v0.1.0-test.1.zip

## Start here

Read [INSTALL](INSTALL.md) (or [HTML guide](INSTALL.html)), then [COMPATIBILITY](COMPATIBILITY.md). Deck users: [Steam Deck Proton TEST guide](STEAM-DECK-PROTON-TEST.html). Choose the correct EN/JP patch and a separate Player package. Patch into a new copy; preserve originals/saves.

## Tested and untested

Windows logical-replay/message tests and Ubuntu headless smoke passed. Physical mouse/full native item-Back, full playthrough, hardware/Proton/audio on Deck remain unverified. Native Ubuntu is not portable Deck support. Stock EasyRPG/Flatpak/EmuDeck does not automatically include this fork.

## Source, licenses and credits

[SOURCE-ACCESS](SOURCE-ACCESS.md) and [SOURCES manifest](SOURCES.json) link matching release source archives/recipes/hashes. [LICENSES](LICENSES.md) scopes MIT to our new scripts/docs only; Player and all third-party/game material keep their own licenses/rights. Read [CREDITS](CREDITS.md), [original EN credits](CREDITS-EN.html) and [original JP credits](CREDITS-JA.html). No new permission or endorsement from game/translation owners is implied.

## Bugs and updates

Use the bug template with release/platform/reproduction/expected/actual. Issues and attachments are PUBLIC: sanitize private paths, usernames, contact/location details; keep raw logs private. Do not upload game folders or arbitrary saves. Maintainer process: [UPDATE-CHECKLIST](UPDATE-CHECKLIST.md). No automated publication/CI.
