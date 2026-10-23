# Seraphic Blue MOD

**How does this translation compare to the 2016 patch?** [Side-by-side page: Japanese, 2016 English, this English, and why](https://nostramadeus.github.io/seraphic-blue-mod/) for several hundred dialogue boxes, plus a separate section on lines the 2016 patch softened. **Spoiler warning:** it quotes dialogue from the whole game. It is gated by story part, but skip it if you want to go in blind.

## In progress

The release already includes the Japanese-based dialogue retranslation and its review. Further translation, picture, content-dependency, optional combat and QoL checks support one combined release.

<details><summary>Current work</summary>

- **Additional translation checks:** The unchanged-English audit (test.11) and the crowded-box audit (test.12) are complete. Remaining: a few term rows in the translation bible.
- **Picture text and comparisons:** Reviewing remaining text images, large-font cards, source matching, and comparison pages that span several cards.
- **Easier use:** Planning simpler updates and clearer control illustrations. Quotation-mark display is also being checked.
- **DC Altered:** released in v0.2.0 as its own build ([Altered build](#altered-build-en--mod--altered)). Next: Arrange-rule switches (v0.2.1).
- **Optional combat and QoL:** Comparing Original/Arrange combat, difficulty, speed and animation skipping with this MOD. Defaults, save compatibility and safe settings are still under review.

</details>

## Downloads (v0.2.0)

| Build | What it is | Download |
| --- | --- | --- |
| **EN + MOD (DC)** | The English Director's Cut with the MOD. Same game data as test.13: your saves keep working. | **[seraphic-blue-fullgame-EN-v0.2.0.zip](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.2.0/seraphic-blue-fullgame-EN-v0.2.0.zip)** |
| **EN + MOD + Altered** | The English *DC Altered* Ver2.13 fan patch with the MOD. New game only. [What is Altered?](#altered-build-en--mod--altered) | **[seraphic-blue-fullgame-EN-Altered-v0.2.0.zip](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.2.0/seraphic-blue-fullgame-EN-Altered-v0.2.0.zip)** |
| **JP + MOD (DC)** | The Japanese Director's Cut with the MOD (Japanese MOD menu). | **[seraphic-blue-fullgame-JP-v0.2.0.zip](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.2.0/seraphic-blue-fullgame-JP-v0.2.0.zip)** |

[All downloads](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.2.0). Each ZIP includes its game, the Windows and older native Linux Players, and launchers.

**Setup:** [Windows](WINDOWS.md) · [Linux / Proton](LINUX.md) · [Steam Deck](STEAM-DECK.md). On Windows, double-click **PLAY.cmd**. Follow the linked Steam/Proton steps on Linux or Deck.

**Controls:** Enter confirms; Esc goes back. **Fast-forward:** hold **F** for 3x speed, hold **G** for 10x (EasyRPG Player feature; both speeds adjustable in Settings > Input, controller: right trigger).

**Save location:** the **saves** folder inside the extracted game folder, when launched with the included launcher or documented Steam options. Keep this folder when updating.

## Already playing? Keep your saves

1. Close the game.
2. [Download the new full game](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.2.0/seraphic-blue-fullgame-EN-v0.2.0.zip) (EN + MOD, DC) and extract it.
3. Copy the **saves** folder from your old game folder into the new one. Done.

Dropped the game years ago? Saves from the Japanese original or the 2016 English patch load here too: copy your **SaveXX.lsd** files into the **saves** folder.

<details><summary>Smaller download: update ZIPs instead (step by step)</summary>

1. Close the game. Keep a backup of your actual save folder.
2. On test.6 or older, first apply the [test.7 image update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.7/seraphic-blue-image-update-v0.1.0-test.7.zip) (extract beside **RPG_RT.ldb**, replace the Picture files).
3. On test.7 or older, [download the test.8 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.8/seraphic-blue-update-v0.1.0-test.8.zip). Extract it into your game folder, beside **RPG_RT.ldb**, and allow replacement of **Player.exe**, **RPG_RT.ldb**, **Map0003.lmu** and one **Picture** file. If your Player.exe lives in another folder (older patch installs), copy the new Player.exe there instead.
4. On test.8 or older, [download the test.9 picture update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.9/seraphic-blue-update-v0.1.0-test.9.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of the 55 **Picture** files.
5. On test.9 or older, [download the test.10 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.10/seraphic-blue-update-v0.1.0-test.10.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of **Map0507.lmu**.
6. On test.10 or older, [download the test.11 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.11/seraphic-blue-update-v0.1.0-test.11.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of **Player.exe** and the 43 **Map** files.
7. On test.11, [download the test.12 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.12/seraphic-blue-update-v0.1.0-test.12.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of the 45 **Map** files.
8. [Download the test.13 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.13/seraphic-blue-update-v0.1.0-test.13.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of the 22 **Map** files.
9. On test.13: nothing to update. The v0.2.0 EN + MOD (DC) build has the same game files.
10. Keep your **saves**, **config** and EasyRPG.ini. Saves from earlier tests load normally.

</details>

<details open><summary>Platform setup and limitations</summary>

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
| macOS (experimental) | Official Mac EasyRPG Player + this ZIP's game data. [Mac steps](#macos-experimental-keyboard-route) | Custom Player features unavailable; not Mac-tested |

</details>

<details open><summary>Altered build</summary>

## Altered build (EN + MOD + Altered)

**What it is.** *Seraphic Blue (DC Altered Version) Ver2.13* is an unofficial fan patch for the Director's Cut by **腐林檎** ("Rotten Apple") and **時空転移プリン** ("Space-Time Warp Pudding", ◆YuikkIDGis). Tempura (Sakaki), the original author, was not involved; the Altered authors ask players not to contact Sakaki or the Blue Field boards about it. Credits from the Altered manual: music by 氷石彩亜 (FREEDOM HOUSE 2nd), 星野春日 (Muzie), 煉獄小僧 (煉獄庭園) and Ciel (Le Ciel Bleu); sound effects by WEB WAVE LIB; backgrounds by aska (Silverry moon light); battle-animation graphics from Character Maker Pro (Enterbrain); help from the 2ch Blue Field threads and 風邪薬 ◆RohTo3cNBI. The Altered manual (Japanese) is included in the ZIP (**ManualAlt**, **改造版マニュアル.htm**).

**What this build adds:** the whole game in English (Altered's new text translated, its Japanese picture text redrawn in English), the MOD menu, the Original-mode choices below, and the standard RPG Maker files the game expects (so no separate runtime install is needed). EasyRPG Player is included and required: the database has 8,040 variables and picture ids up to 78, which the old RPG_RT.exe cannot run (it is not included).

**New game only.** Start a new game in this build. Keep old saves on the EN + MOD (DC) build: the test.13 download stays up, and the v0.2.0 DC download uses the same game data. The ZIP extracts to its own **SeraphicBlue-Altered** folder; read **IMPORTANT README (MUST READ).txt** first.

### Game modes (Altered build)

One dungeon trip, two designs:

| | Original | Full Arrange (BATTLE + MANY) |
| --- | --- | --- |
| Design | Attrition: the challenge lives between fights | Per-encounter: the challenge lives inside each boss fight |
| HP after a fight | Carries over to the next fight | Full HP after every fight |
| Refills | The SUP.HP / SUP.TP pools refill you and can run dry | Not needed between fights |
| Items | Your buffer, no per-battle limit | 5 of each item per fight |
| Escape | Can fail | Always works |
| Counterattacks | A dice roll | Always fire |
| Ailments on bosses | Bosses resist them | Ailments work on bosses |
| Turn order at the start | Fixed rules | Random opening turn order |
| Gear and shops | As designed | 50 new items, rebuilt shops |

- **First play: Original, NORMAL.** It keeps the game the author designed: the attrition loop.
- **Second play, or if you want a smoother, modern-feeling run: Full Arrange** (BATTLE + MANY).
- **MANY alone: not recommended.** It is a half-way state (Arrange rules without the rest of the Arrange battle system).
- Planned for v0.2.1: MOD switches to turn off the Arrange battle rules (full HP after battle, item limit, always-escape, always-counter, enemy stat changes) one by one, so you can play the extra content with the original battle rules.
- Inside Arrange, Altered's own Config can switch off the random turn order, the luck elements and the timing hits; full HP after battle, the item limit, always-escape and always-counter cannot be switched off in v0.2.0.
- New Game+ with bonus picks is available after clearing, in every mode.

### Original mode = DC + these fixes

- Opposite buffs and debuffs resolve sanely (for example a speed-up on a slowed unit cancels instead of failing).
- Enemy phase changes are measured as a share of max HP (a DC oversight where an enemy had extra HP).
- Overflow safety for extreme numbers (damage calculation order, caps of 300 on HIT / CRT / AVD / AGL / MOV).
- Reflex Guard halves damage once, as in DC (Altered halved it twice in Original mode).
- Sickness, five boss rewards and the key-item money bonus are back to their DC rules in Original mode (Arrange keeps Altered's).
- New games start with "skip battles with weak enemies", supplement auto-fill and the fewer-members EXP bonus OFF, and Config "default" resets match. All three stay in Config.
- Clever on a Forgetful unit still gives x1.3 as in DC (the Altered manual says x1.0; the game data says x1.3).

### MOD menu on the Altered build

| MOD row | On the Altered build |
| --- | --- |
| Walk speed, Hold Shift to run | Not in the MOD menu: use Config > Dash Movement (page 1) |
| Battle speed | Not in the MOD menu: use Config > Battle Speed (page 3; FAST2 also skips skippable effects) |
| Menu fade | Not in the MOD menu: use Config > Screen Speed of Menus (page 2) |
| Save anywhere (cheat) | Not in the MOD menu: use Config > Normal Save Method: MENU (page 1) |
| MOD button | Menu slot 9. With Save Method MENU, slot 9 asks Save / MOD / Break |
| Random-battle intro, Cutscene speed, Random battles 1/N, Rewards follow the rate, Escape always works, Retry lost battles, Full heal, Return to world map, +10,000 DEAR, Level up party, early MOD access | As on the DC build. Retry also gives back the items Arrange's per-fight limit held back. |

- **Steps Left** (Altered Config page 6) counts the MOD encounter rate: at 1/2 it shows twice the steps; with random battles Off it shows the last two digits of a very large number.
- **DC-only Player features:** the custom battle screen, the timeline names and click-to-walk stay off on the Altered build (Altered rebuilt its battle screens); mouse menus, message history and fast-forward work.
- **Database:** one party member's name now follows the translation bible's spelling (the 2016 data spelled it differently).

</details>

<details><summary>Release changes and translation comparison</summary>

**New in v0.2.0:**
- **Three builds:** EN + MOD (DC, same game data as test.13), EN + MOD + Altered (new), JP + MOD (DC, full game).
- **Altered build:** see [Altered build](#altered-build-en--mod--altered). New game only.
- No changes to the DC game files since test.13.

**New in test.13:**
- **22 dialogue boxes corrected** after an outside check: while the [comparison page](https://nostramadeus.github.io/seraphic-blue-mod/) was being built, its reviewers compared our lines with the Japanese and flagged the few where ours was weaker (a dropped qualifier, a Japanese idiom flattened into plain English, one word read in the wrong sense). Those are fixed. 4 boxes also had a pause moved to the line end (cosmetic).
- Changed files: 22 map files. No Player, picture or save changes.

**New in test.12:**
- **63 more dialogue boxes corrected to match the Japanese.** This completes the audit of all 3,013 "full" four-line boxes (the ones most likely to have been shortened to fit): 89 of them had lost a qualifier, a hedge, a clause or a Japanese idiom's image, and all are restored. 2 of the new corrections use two boxes instead of one shortened box.
- Changed files: 45 map files. No Player, picture or save changes.
- **Old saves work.** A save from the Japanese original, from the 2016 English patch or from any test release loads in this version: copy your SaveXX.lsd files into the **saves** folder.

**New in test.11:**
- **Message history (Windows Player):** scroll back through the last 100 message boxes you read, with the choice you picked. Open it with **mouse wheel up** or **Page Up** while a message is showing or while you walk on the field; scroll with the wheel or Up / Down, page with Page Up / Page Down, close with **Escape / B / right click**. It is cleared when you load or start a game and is never saved. The native Linux Player and the Mac Player do not have it.
- **67 dialogue boxes corrected to match the Japanese** (dropped qualifiers or hedges restored, Japanese idioms kept as their own image, 14 names and terms made consistent with the in-game dictionary). 7 of them now use two boxes instead of one shortened box. All 585 boxes whose English was identical to the 2016 patch were checked against the Japanese and found correct.
- Changed files: Player.exe and 43 map files. Saves, config and EasyRPG.ini are untouched; earlier saves load normally.

**New in test.10:**
- One opening dialogue line corrected to match the Japanese.

**New in test.9:**
- **55 picture cards retranslated from the Japanese:** 52 history timeline cards (names and terms now match the rest of the game; 10 cards had the wrong meaning), the two opening chant cards and the opening poem card.
- No Player, map or save changes.

**New in test.8:**
- **MOD settings from the very start:** while the story still locks the game menu (the opening chapters), Cancel / Esc / Deck B opens the MOD screen directly; Cancel returns to the same spot. After the menu unlocks, nothing changes.
- **Clicking to walk now works in the opening rooms** (it needed the unlocked game menu before).
- **Opening poem card:** the second card of the opening poem is retranslated to match the Japanese.
- Both need the included Windows Player (Windows, Proton, Steam Deck). The native Linux Player and the stock Mac Player keep the older behaviour.

**Already read the opening?** [Japanese / original English / corrected English](EARLY-GAME-CORRECTIONS.html). Opening and Episode 2 only; later sections stay hidden until selected.

</details>

<details open><summary>Original creators and credits</summary>

## Thank you to the original creators

Thank you to **eplipswich** for the tremendous work of translating Seraphic Blue into English and making its story accessible to more players.

Thank you to **Tempura (Sakaki)** for creating this work of art and sharing it freely with the world. This MOD exists because of that creativity and generosity.

Thank you to **腐林檎** and **時空転移プリン** for *Seraphic Blue (DC Altered Version)*, which the Altered build carries.

[See the full original credits](CREDITS.md).

</details>

<details><summary>macOS: experimental keyboard route</summary>

## macOS: experimental keyboard route

Use the latest game-data MOD with the **official Mac EasyRPG Player**. A custom Mac Player is not included.

1. [Download the full game](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.2.0/seraphic-blue-fullgame-EN-v0.2.0.zip) and extract it. Keep the **SeraphicBlue** folder together.
2. Install [Homebrew](https://brew.sh/) if needed. In Terminal, run:

```sh
brew install easyrpg-player
```

3. In Terminal, type `cd ` (including the space), drag the extracted **SeraphicBlue** folder into Terminal, and press Enter. Run:

```sh
mkdir -p saves config
easyrpg-player --project-path . --save-path saves --config-path config --encoding 932 --window
```

**Controls:** arrows select/move; Enter confirms; Escape goes back; Shift runs/opens secondary actions. Saves go in **SeraphicBlue/saves**.

**Limits:** script-based MOD options are expected to work. Custom hover/click targeting, click-to-walk, character tabs, enhanced text reveal and battle-animation acceleration need our modified Player and are unavailable here. **This Mac route is untested.** [Official Mac support](https://easyrpg.org/player/downloads/) · [Homebrew package](https://formulae.brew.sh/formula/easyrpg-player.html).

</details>

<details open><summary>Quick tutorials</summary>

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

</details>

<details open><summary>MOD menu tutorials</summary>

## MOD menu tutorials

**Open:** Escape / Deck B → select **MOD** → Enter / A. Before the story unlocks the game menu, Escape / Deck B opens the MOD screen directly (no CHEATS page yet). **Navigate:** Shift / X changes page; Up/Down selects a row; Left/Right changes its value. Enter / A confirms actions. Settings apply immediately and stay with your save. Choose **INFO** for the in-game explanations.

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

</details>

<details open><summary>Controls and menu shortcuts</summary>

## Controls

| Action | Mouse | Keyboard / suggested Steam Input |
| --- | --- | --- |
| Select / confirm | Hover / left click | Arrows / Enter; D-pad / A |
| Back / cancel walking | Right click | Escape / B; arrows cancel walking |
| Change battle list page | Wheel or page arrows | Left / Right |
| Switch character tabs | Top tabs | Page Up / Page Down; optional LB / RB |
| Secondary action | Follow the displayed hint | Shift / X |
| Message history (last 100 boxes) | Wheel up while a message shows or while walking; wheel scrolls; right click closes | Page Up opens; Up / Down scroll; Page Up / Down page; Escape / B closes |

Steam Input bindings are suggestions, not a verified Deck layout. Touch does not provide hover before contact.

## More menu shortcuts

| Try this | Mouse | Keyboard / suggested Deck buttons |
| --- | --- | --- |
| Secondary actions in Gear, shops or battle | Follow the visible hint; Shift still needs a key/button | Shift / X; opens the action shown on that screen |
| Buy or sell several items | Click -10 / -1 / +1 / +10, then Buy/Sell | Arrows adjust quantity; Enter / A confirms |
| Supplement or Upgrade amounts | Hover a digit/amount; wheel adjusts; click Apply/Upgrade | Arrows select/adjust; Enter / A confirms |
| Dictionary and history | Hover supported rows; wheel changes list pages or scrolls history | Arrows navigate; Enter / A chooses where applicable |

Native name-entry and number-entry keep their original keyboard controls.

</details>

<details><summary>Older install: optional engine upgrade</summary>

## Older install (test.1 to test.5)? Optional engine upgrade

Skip this if you installed the test.6 or test.7 full game: the test.8 update above already replaces Player.exe.

1. Close the game and back up the **saves** folder (or your existing custom save location).
2. Download the [test.6 Windows Player ZIP](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-windows-x86_64-v0.1.0-test.6.zip) for Windows or Proton (the newest Player ZIP with all DLLs). Extract it separately.
3. Copy **Player.exe and all .dll files from that same ZIP** into the folder containing your old Player.exe. Replace those files only. Keep saves, EasyRPG.ini and game data.
4. Then apply the test.7 image update and the test.8 update from the section above; the test.8 Player.exe replaces the test.6 one and uses the same DLLs.

Native Linux has no newer binary than test.2; use Proton for the latest engine features. Existing patch-based installations can continue using their current game/save paths.

</details>

<details><summary>More details and tested limits</summary>

## Details

- [Windows setup](WINDOWS.md), [Linux setup](LINUX.md), [Steam Deck setup](STEAM-DECK.md).
- [Full release notes](RELEASE-NOTES.md) and [tested limits](COMPATIBILITY.md).
- [Advanced patch installation / older-version migration](INSTALL.md).
- [Original credits](CREDITS.md), [licenses](LICENSES.md), and [corresponding source](SOURCE-ACCESS.md).

English game content and its original manual/credits are included. The JP + MOD full game (v0.2.0) and the separate Japanese patch are available for Japanese players. Native Linux remains the previously tested Ubuntu 22.04-compatible test.2 runtime. No full-playthrough or physical Deck verification is claimed.

</details>
