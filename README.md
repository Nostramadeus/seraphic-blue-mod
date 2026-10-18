# Seraphic Blue MOD

## Download the complete English game

**[Download the full game + MOD + Players](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-fullgame-EN-v0.1.0-test.6.zip)** · [All downloads](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.1.0-test.6)

One ZIP includes the English game, latest Windows Player, an older native Linux Player, and launchers. No separate original-game download, patching, Python or DLL selection is needed.

```text
Download → Extract All → Choose your platform below → Play
```

| Your platform | Start here | Newest mouse features? |
| --- | --- | --- |
| Windows | Double-click **PLAY.cmd**. [Windows steps](WINDOWS.md) | Yes |
| Linux through Steam / Proton | Add **Player.exe** to Steam; enable Proton. [Linux steps](LINUX.md) | Yes; compatibility not verified here |
| Steam Deck | Desktop Mode: add **Player.exe** to Steam; enable Proton. [Deck steps](STEAM-DECK.md) | Yes; hardware not verified here |
| Native Linux alternative | Run **sh play-linux.sh**. [Requirements](LINUX.md#native-linux-alternative) | Older test.2 controls; new hover/tabs/walking are unavailable |

**Save location:** the **saves** folder inside the extracted game folder, when launched with the included launcher or documented Steam options. Keep this folder when updating.

## Four things to try

| You do this | You see this |
| --- | --- |
| Hover a menu row or enemy/ally | Its highlight and information update. Click to confirm. Hover spends nothing. |
| Scroll while choosing battle magic/items | The page changes. **< 1/3 >** and clickable arrows show more pages. |
| Open Status, Gear or Ability | Top tabs switch screens while keeping the same character. Page Up/Down works too. |
| Click ground or an NPC's feet | Your character routes there. White marks hover; green marks an accepted destination. |

## Feature demos

### Hover an enemy to select it

Move over a visible enemy. Its name and target indicators update before you click. A stationary mouse leaves keyboard selection alone.

<img src="docs/images/battle-hover.png" width="640" alt="Enemy hover selection with the selected enemy name and battle menu">

### See and change list pages

The **< 2/3 >** indicator means page two of three. Scroll or click an arrow to change pages. Hover selects an entry within the page.

<img src="docs/images/spell-pages.png" width="640" alt="Battle list showing clickable arrows and page two of three">

### Switch character screens without backing out

Click **Status / Gear / Ability** at the top. Reserve characters keep their identity; their Ability tab is unavailable.

<img src="docs/images/character-tabs.png" width="640" alt="Status screen with Status Gear and Ability quick tabs">

### See where click-to-walk is going

The green square marks the accepted destination. It clears when you arrive or cancel. Arrow keys or right-click cancel walking.

<img src="docs/images/walking-destination.png" width="640" alt="Green destination square on the field after a click-to-walk command">

## Controls

| Action | Mouse | Keyboard / suggested Steam Input |
| --- | --- | --- |
| Select / confirm | Hover / left click | Arrows / Enter; D-pad / A |
| Back / cancel walking | Right click | Escape / B; arrows cancel walking |
| Change battle list page | Wheel or page arrows | Left / Right |
| Switch character tabs | Top tabs | Page Up / Page Down; optional LB / RB |
| Secondary action | Follow the displayed hint | Shift / X |

Native number-entry and name-entry keep their existing controls. Steam Input bindings are suggestions, not a verified Deck layout.

## Already playing? Update without replacing saves

1. Close the game and back up the **saves** folder (or your existing custom save location).
2. Download the smaller [Windows Player update ZIP](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-windows-x86_64-v0.1.0-test.6.zip) for Windows or Proton. Extract it separately.
3. Copy **Player.exe and all .dll files from that same ZIP** into the folder containing your old Player.exe. Replace those files only. Keep saves, EasyRPG.ini and game data.

This test.6 Player update does not change game data. Native Linux has no new test.6 binary; use Proton for the latest engine features. Existing patch-based installations can continue using their current game/save paths.

## Details

- [Windows setup](WINDOWS.md), [Linux setup](LINUX.md), [Steam Deck setup](STEAM-DECK.md).
- [Full release notes](RELEASE-NOTES.md) and [tested limits](COMPATIBILITY.md).
- [Advanced patch installation / older-version migration](INSTALL.md).
- [Original credits](CREDITS.md), [licenses](LICENSES.md), and [corresponding source](SOURCE-ACCESS.md).

English game content and its original manual/credits are included. The separate Japanese patch remains available for existing supported Japanese installations. Native Linux remains the previously tested Ubuntu 22.04-compatible test.2 runtime. No full-playthrough or physical Deck verification is claimed.
