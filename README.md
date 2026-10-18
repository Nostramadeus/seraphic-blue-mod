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

## Thank you to the original creators

Thank you to **eplipswich** for the tremendous work of translating Seraphic Blue into English and making its story accessible to more players.

Thank you to **Tempura (Sakaki)** for creating this work of art and sharing it freely with the world. This MOD exists because of that creativity and generosity.

[See the full original credits](CREDITS.md).

## Quick tutorials

**Deck buttons below need the [suggested Steam Input bindings](STEAM-DECK.md#suggested-steam-input-controls).** They are not a bundled controller preset. New controls require the latest Windows Player, including through Proton.

### Select menus, spells and targets

- **Mouse:** hover to preview; left-click to choose. Works on supported menu rows, enemies and allies.
- **Keyboard / Deck:** arrows / D-pad select; Enter / A confirms; Escape / B backs out.
- **Result:** highlight and information update. Hover spends nothing. A stationary mouse leaves keyboard selection alone.

<img src="docs/images/battle-hover.png" width="640" alt="Enemy hover selection with the selected enemy name and battle menu">

### Find the next spell or item page

- **Mouse:** wheel or click the page arrows; hover an entry to select it.
- **Keyboard / Deck:** Left/Right / D-pad left/right changes pages; Up/Down selects a row.
- **Result:** **< 2/3 >** means page two of three. Applies to paged battle magic/items and supported menu lists.

<img src="docs/images/spell-pages.png" width="640" alt="Battle list showing clickable arrows and page two of three">

### Switch Status / Gear / Ability without backing out

- **Mouse:** click a top tab. **Keyboard:** Page Up / Page Down. **Deck:** bind LB / RB to those keys.
- **Result:** switch screens while keeping the same character. Left/Right still changes characters.
- Tabs work at the top level; back out of an unfinished selection first. Reserve characters cannot open Ability.

<img src="docs/images/character-tabs.png" width="640" alt="Status screen with Status Gear and Ability quick tabs">

### Click or tap to walk

- **Mouse:** click ground to route there; click an NPC's feet to approach and interact once.
- **See:** white square = hovered tile; green square = accepted destination. No green square means no route was accepted. It clears on arrival or cancellation.
- **Cancel / walk manually:** arrows / Deck D-pad. Escape / B or right-click also cancels routing. No separate keyboard destination picker.
- **Deck touchscreen:** tapping ground is expected to work through Proton because [Deck taps normally act as mouse clicks](https://partner.steamgames.com/doc/steamhardware/steamdeck/faq#Input). **Not tested on Deck hardware.** If tapping fails, try the right trackpad as Mouse + left-click. Hover preview needs a trackpad/mouse.

<img src="docs/images/walking-destination.png" width="640" alt="Green destination square on the field after a click-to-walk command">

### Advance dialogue and story pauses

- **Mouse:** left-click. **Keyboard / Deck:** Enter / A with the suggested binding.
- Press while text appears to reveal it faster; press again at a dialogue pause to continue. Use separate presses, not a held click.
- **Not every pause is skippable:** timed scene waits, movement and animations can continue. Use **MOD → SPEED → Cutscene speed** to shorten scripted waits; confirm is not a universal scene-skip button.

## MOD menu tutorials

**Open:** Escape / Deck B → select **MOD** → Enter / A. **Navigate:** Shift / X changes page; Up/Down selects a row; Left/Right changes its value. Enter / A confirms actions. Settings apply immediately and stay with your save. Choose **INFO** for the in-game explanations.

### SPEED — spend less time waiting

| Setting | Try / result |
| --- | --- |
| Walk speed / Hold Shift to run | Choose 2x for faster walking. Enable running; hold Shift / X to run. Scripted movement stays unchanged. |
| Battle speed | Choose 2x–10x for shorter waits/animations; Instant skips animation waits. |
| Random-battle intro | Off skips the random-battle flash; story intros stay. |
| Menu fade | Choose 0.1 s or None for quicker menu transitions. |
| Cutscene speed | Choose 2x/5x/Instant to shorten scripted waits. This changes scene pacing. |

### BATTLE — choose how often you fight

| Setting | Try / result |
| --- | --- |
| Random battles | Choose 1/2–1/10 for fewer fights, or Off for none. |
| Rewards follow the rate | On scales EXP, DEAR and SUP.EXP to compensate for fewer random fights. |
| Escape always works | On guarantees escape from random battles; story battles stay unchanged. |
| Retry lost battles | On offers a retry after defeat. **Items spent in the lost fight stay spent.** |

### CHEATS — optional, confirmed actions

Enable the CHEATS page when asked. Select an action and confirm. **Save first before teleporting or saving during an event.**

| Action | Result |
| --- | --- |
| Full heal | Restores party HP and TP. |
| Return to world map | Returns to your known world-map position; can skip events. Visit the world map first. |
| Save anywhere | Opens saving here; unusual save locations can interrupt events. |
| +10,000 DEAR | Adds 10,000 currency. |
| Level up party | Raises every party member by one level. |

## Controls

| Action | Mouse | Keyboard / suggested Steam Input |
| --- | --- | --- |
| Select / confirm | Hover / left click | Arrows / Enter; D-pad / A |
| Back / cancel walking | Right click | Escape / B; arrows cancel walking |
| Change battle list page | Wheel or page arrows | Left / Right |
| Switch character tabs | Top tabs | Page Up / Page Down; optional LB / RB |
| Secondary action | Follow the displayed hint | Shift / X |

Steam Input bindings are suggestions, not a verified Deck layout. Touch does not provide hover before contact.

## More menu shortcuts

| Try this | Mouse | Keyboard / suggested Deck buttons |
| --- | --- | --- |
| Secondary actions in Gear, shops or battle | Follow the visible hint; Shift still needs a key/button | Shift / X; opens the action shown on that screen |
| Buy or sell several items | Click -10 / -1 / +1 / +10, then Buy/Sell | Arrows adjust quantity; Enter / A confirms |
| Supplement or Upgrade amounts | Hover a digit/amount; wheel adjusts; click Apply/Upgrade | Arrows select/adjust; Enter / A confirms |
| Dictionary and history | Hover supported rows; wheel changes list pages or scrolls history | Arrows navigate; Enter / A chooses where applicable |

Native name-entry and number-entry keep their original keyboard controls.

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
