# v0.3.6 — mouse interaction, equipment comparison and healing controls

All three full-game downloads include Windows and native Linux Player 0.8.1.1-sb7. English builds gain numerical shop comparison, corrected title placement and the approved font-card replacements.

- **Mouse interaction:** clicking visible characters uses their displayed artwork and native interaction rules, including counters. Blocked clicks immediately beside one native exit can select that exit. Pure speed adjustments no longer suppress an arrival transfer. These changes retain native event conditions and collision rules.
- **English shop comparison:** highlight a weapon or frame, then press **Tab** or click **[Tab] Compare**. Read **Now / After / Delta** for all 11 stats. Left/Right opens details, including sphere slots removed by a lower-capacity frame. Tab, Cancel or right-click closes. The panel does not purchase or equip anything; hidden item data stays hidden. Spheres retain their native shop behavior.
- **Altered settings:** Shift supports both native dash modes without canceling mouse movement. Hovering MOD updates its help. With free full-HP recovery Off, Supplement exposes HP reserve and HP Auto Fill controls. New Extra Content games start HP Auto Fill Off; loaded saves retain their settings. Manual FREE encounters give ordinary rewards. The separate Auto Fill Short Notice setting only changes messages.
- **English presentation:** 101 approved font cards per English edition use a consistent face; 84 mixed-layout cards remain unchanged. Location titles retain complete words within the screen. One minor Counter Attack wording correction is included. The two-map Turku Inn hotfix is retained.

**Update and keep your progress:** close the old game, extract the matching new full game into a new folder, and copy your **saves** and **config** folders. Keep the new **EasyRPG.ini**. DC saves stay on DC; Altered saves from v0.2.0 onward stay on Altered. Keep the old installation until your usual save loads.

Read the refurbished [README](https://github.com/Nostramadeus/seraphic-blue-mod#readme) for mode selection, healing controls, illustrated battle labels and comparison controls. Matching source and dependency information accompany the release.

Focused Windows checks covered the arrival-race reproduction, actual Turku clerk/exit, and numerical shop comparison in both English editions. Exact earlier receipts are retained for unchanged paths; the final Windows binary passed DC Buy with the full inventory and native actor values unchanged. One controlled headless Debian 11 shop comparison/Cancel replay passed, including numerical values and unchanged native state. The final native build retains that path across two source-bound DC copy-range corrections verified on Windows; no second Linux replay is claimed. No full playthrough, physical Steam Deck or Proton test is claimed. [Recorded scope and limits](COMPATIBILITY.md).


## Earlier release — v0.3.4

# v0.3.4 — consistent menu hover

Menus now respond consistently to pointer movement in the English Altered build and both DC builds. Native lists, title/save screens and number/sign editors give keyboard and gamepad input priority. Custom battle, field, shop, dictionary, MOD and configuration menus keep their own native selection, help and permission rules.

Move the pointer to highlight a menu choice or inspect its help. Hover does not confirm, buy, equip, apply a setting or move the player. Click or press Enter to choose. Keyboard/gamepad navigation takes control until the pointer moves again. Unavailable choices keep their native restrictions.

All three full-game ZIPs include Windows and native Linux Player **0.8.1.1-sb6**, built from the same source **eb421f5**. Focused Windows checks covered native selection, keyboard handoff, click confirmation, MOD tabs and the native nine-row bonus menu. One controlled headless Linux hover/click/keyboard replay passed on Debian 11. This is not physical Steam Deck, Proton or full-playthrough verification.

Game text, pictures, event data and save formats are unchanged from v0.3.3. Extract into a new folder and copy your **saves** and **config** folders. Keep DC saves with DC and Altered saves with Altered. Preserve the new release's **EasyRPG.ini**.

The matching [Player source](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.4/seraphic-blue-player-source-v0.3.4.zip) includes build recipes and dependency source information. Earlier releases and their exact matching source assets remain available. [Setup and limits](COMPATIBILITY.md).

Recorded additional Japanese-meaning review remains partial: 1,915 Altered-specific entries have origin/application evidence without matching review records; 22,137 DC entries lack matching records for the additional review pass. The 11,328 shared-English transfers remain separate. This hover release makes no new translation changes or whole-script review claim.

## Earlier release — v0.3.3


## Builds and saves

- **seraphic-blue-fullgame-EN-Altered-v0.3.3.zip** — EN + MOD + Altered. New game or an Altered save from v0.2.0 onward.
- **seraphic-blue-fullgame-EN-v0.3.3.zip** — EN + MOD (DC). Earlier DC saves load as before.
- **seraphic-blue-fullgame-JP-v0.3.3.zip** — JP + MOD (DC). Earlier DC saves load as before.

DC saves do not move into Altered. Back up **saves** and **config** before updating.

## Proton title-screen crash

The bundled PortAudio library includes [AryaNetwork's fix for issue #1](https://github.com/Nostramadeus/seraphic-blue-mod/issues/1). FluidSynth was starting PortAudio to enumerate devices; that device listing crashed under Wine. The patch makes **Pa_Initialize** report that PortAudio is unavailable. Player audio uses SDL, so it does not need PortAudio. The final Windows Player passed title-screen MIDI startup with audio enabled through an inaudible SDL dummy device. We did not run Proton or physical Steam Deck hardware.

## Native Linux and source

The native Linux Player now uses the same **0.8.1.1-sb5** source as Windows, including mouse controls, click-to-walk, history, Text speed and Text pauses. Run **sh play-linux.sh**. Helper libraries and notices are in **native-linux**. Headless tests passed 36 replay cases on Debian 11, Arch and Ubuntu 24.04 containers. All 18 generated save states matched Windows. A separate normal-speed replay matched Windows on all three systems (nine images). Timeline and save-name checks also matched all 111 images and 36 generated save states. MIDI produced nonzero audio through a virtual disk driver. Launcher paths with spaces and save/config storage passed. Physical Steam Deck, Proton and desktop display/audio drivers remain untested.

MIDI uses an available soundfont through FluidLite or the included FM synthesizer. No soundfont download is required to play; FM instruments sound different. [Requirements and setup](LINUX.md).

The [Player source asset](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.3/seraphic-blue-player-source-v0.3.3.zip) exports current Player **0cb855f**, a separate historical sb4 **a13da25** tree, and native liblcf **92c4450**, with build recipes, timeline asset generators and exact dependency-source information. Git history is not included.

## Credits and English content

Both DC builds restore mouse controls, the native battle panel and timeline name tables/assets. Altered gains full timeline names, including DRIVE/red markers and conditional Er names. English save slots retain the full “Blue-Haired Woman” name beside all four faces.

Altered now shows the two 2016 English-team cards already present in DC: Special Thanks, translator **eplipswich**, and proofreader **kumada**. Thanks also to kumada for the original proofreading.

Both English builds have eight dictionary captions corrected to the ruled names and roles, with the complete wording retained. Cilia is listed under A-C and Person under P-R; unlock switches and target pages are unchanged. The Status menu now spells out Poison instead of PSN, including at 100% trigger and defense rates. Altered choice-guard checks passed for held Enter, repeated presses and Cancel, with unguarded controls checked too.

The DC English build restores 132 dialogue corrections missed by earlier packages, with 11 extra message boxes to retain the full wording. Altered also fixes three lines that used outdated translation inputs. Both English builds translate six remaining Daisy, Gerard and Owen portrait captions.

## Known limits

The English DC manual is mostly the 2016 English translation; four pages remain Japanese and two are mixed. Altered's manual and update history are Japanese. Some status labels keep an English word with a Japanese gloss; character reading captions, original artist-name credits and small background/sprite lettering remain as retained artwork. These exceptions are documented; this is not a claim that every image and manual page is English.

Application checks confirm that approved wording reached the game files. The additional review of English against Japanese remains incomplete. [Review scope and counts](COMPATIBILITY.md#translation-review-scope).

No full-playthrough, physical Steam Deck or Proton verification is claimed. Windows and Linux replays check specific paths and saved states. [Compatibility](COMPATIBILITY.md).

# Release notes — v0.3.2

## Build

- **seraphic-blue-fullgame-EN-Altered-v0.3.2.zip** — EN + MOD + Altered. New game, or a save from the v0.2.0 to v0.3.1 Altered builds.
- **seraphic-blue-fullgame-EN-v0.3.2.zip** — EN + MOD (DC). Saves from the earlier EN + MOD (DC) builds load as before (no save-format change).
- **seraphic-blue-fullgame-JP-v0.3.2.zip** — JP + MOD (DC). Saves from the earlier JP + MOD (DC) builds load as before (no save-format change).
- DC saves still do not move to the Altered build.

## Menu labels (English builds)

- 12 menu labels that were still Japanese in v0.3.1 are now in English (Altered; 6 of them in DC EN too): the three magic types of the Ability menu, Qty to Make, Discount, Qty to Sell, Paralysis, Ailment Trigger Rate / Defense Rate and the three magic-level labels of the Status menu, and Poison as **PSN**. Labels that did not fit in the game font use a narrower font, not a shortened word. DC EN Status screen: the movement stat reads **MOV** (the 2016 label said "DEX"), and "Field Mutation Element" replaces the 2016 label "Element Physical Cast". Both English ZIPs carry **MENU-LABEL-NOTES.txt** with the list.

## Story pictures and credits (English builds)

- All remaining story pictures redrawn in English (Altered 32 files, DC EN 43): 12 explanation screens, episode title cards, battle chant pictures, the Panorama menus (temporary save, organize, EXT bonus, shop line-up), the title-screen labels (DC EN), one battle background, unused leftover pictures, two dictionary titles and end-credits cards.
- End credits: the music credits card follows the Japanese list (both English builds); a DC EN credits card now carries the Japanese music credit together with the 2016 team; the 2016 translator credits card now also shows in the DC EN credits sequence that lacked it.
- One glossary term is written out in its full form in 2 boxes (both English builds).

## New text file (Altered ZIP)

- The Altered ZIP adds **HIDDEN-DICTIONARY-ENTRIES (SPOILERS).txt**: 3 unreachable dictionary entries written for an unfinished sequel, in a spoiler-marked text file. The game itself is unchanged; the entries stay unreachable in game.

## Other

- JP + MOD (DC): no content changes; it carries the new version number so the three builds stay in step.
- Player: unchanged from v0.3.1 (Windows Player 0.8.1.1-sb4; native Linux Player = the older test.2 build).
- Clicking an ally target in battle is now tested with a two-member party (passed).

## Known gaps

- The native Linux Player (**play-linux.sh**) is unchanged and has none of the v0.3.1 Player features (use Player.exe on Windows, or Proton on Linux and Steam Deck). The Altered build's credits do not show the 2016 translator card. The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose.

## Saves

- Altered saves from v0.2.0 to v0.3.1 load. DC saves load as before (no save-format change). DC saves do not move to the Altered build.

# Release notes — v0.3.1

## Build

- **seraphic-blue-fullgame-EN-Altered-v0.3.1.zip** — EN + MOD + Altered. New game, or a save from the v0.2.0 to v0.3.0 Altered builds.
- **seraphic-blue-fullgame-EN-v0.3.1.zip** — EN + MOD (DC). Saves from the earlier EN + MOD (DC) builds load as before (no save-format change).
- **seraphic-blue-fullgame-JP-v0.3.1.zip** — JP + MOD (DC). Saves from the earlier JP + MOD (DC) builds load as before (no save-format change).
- DC saves still do not move to the Altered build.

## New Windows Player 0.8.1.1-sb4 (all three ZIPs)

- Battle mouse on the Altered build: command grid, enemy targets with hover, ability and item rows with hover, page change by mouse wheel, category tabs, ally targets.
- MOD menu, SPEED page: new rows **Text speed** (1x / 2x / 4x / Instant) and **Text pauses** (1x / 2x / 4x; shortens the pauses inside messages, never removes them).
- Choice guard: for a third of a second a choice window ignores Enter that is held down or pressed repeatedly, so the Skip prompts are not skipped by accident. Cancel is unaffected.
- Save-slot placeholder name now reads "Blue-Hair Lady" (DC EN).

## English builds

- Dictionary (Character Profiles and Glossary) re-sorted into English alphabetical tabs A-C ... Y-Z (182 entries). Empty tabs cannot be entered. Unlocks and saves are unchanged.
- 24 menu tile strips in English (272 words), including the party names of the Altered Ability menu. 14 menu words given more tiles or a ruled short form (10 by extra map tiles, 4 by a short form such as "Owned"); the 8 element labels of the Status menu now use two-letter codes (Fi Wa Wi Ea Li Da He Br).
- 27 pictures redrawn: place-name banners, world-map guides, ending-screen panels, shop and inn signs.
- Actor-name strings use the spelling Yancy.
- 108 story cards and labels redrawn (pulled cards corrected, Er and Sieg continuation text, dictionary labels, chapter titles, staff credits, Panorama menus).

## Linux

- The new Player features need **Player.exe**: on Windows, or on Linux and Steam Deck through Proton. The native Linux Player (**play-linux.sh**) is unchanged from earlier releases (the older test.2 build) and has none of them.

## Known gaps

- The native Linux Player is unchanged (see Linux above); the new Player features are Windows and Proton only unless a native Linux build follows.
- 37 text pictures still carry the 2016 wording or Japanese and come in the next release: 12 explanation screens, the Panorama menus (temporary save, organize, status, EXT bonus and shop line-up), the title-screen labels, a few art-background titles and message cards. In the menus, nine labels stay Japanese for now (the three magic-level labels of the Ability menu, Poison, Paralysis and four shop quantity labels: their English needs more room than the screen layout gives).
- Three dictionary detail pages that no list row reaches (Gaia, Alma, Seraphic Blue Amplifier) stay as the Altered authors left them.
- Clicking an ally target in battle was tested with a one-member party only.
- The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose.

## Saves

- Altered saves from v0.2.0 to v0.3.0 load. DC saves load as before (no save-format change). DC saves do not move to the Altered build.

# Release notes — v0.3.0

## Build

- **seraphic-blue-fullgame-EN-Altered-v0.3.0.zip** — EN + MOD + Altered. New game, or a save from the v0.2.0 to v0.2.3 Altered builds.
- **seraphic-blue-fullgame-EN-v0.3.0.zip** — EN + MOD (DC). Saves from the earlier EN + MOD (DC) builds load as before (no save-format change).
- **seraphic-blue-fullgame-JP-v0.3.0.zip** — JP + MOD (DC). Saves from the earlier JP + MOD (DC) builds load as before (no save-format change).
- DC saves still do not move to the Altered build.

## DC builds

- Both DC builds are rebuilt through the same release pipeline as the Altered build: full game folders verified file by file, the text file **IMPORTANT README (MUST READ).txt** at the ZIP root, and PLAY.cmd starts the Player by its full path (the v0.2.2 fix).
- EN + MOD (DC) also gets the 23 retranslated opening quote cards (the same cards as Altered v0.2.3) and the newer text of three maps (Map0025, Map0026, Map0140): corrections from 2026-10-22 that the shipped game had but the source folder had lost.
- JP + MOD (DC) keeps its 141 standard RPG Maker asset files.

## Pictures

- Redrawn text pictures in the English builds: Altered 78 files, DC EN 73 files. The same picture ships under both builds' names where both have it.
- 25 episode title cards: the titles now carry the complete Japanese title. The English episode-number row and the German row are kept pixel for pixel.
- 15 Er explanation cards that were still Japanese in the Altered build.
- 18 report and diary cards.
- Dictionary term labels (Altered 9, DC EN 17).
- 3 item description boxes and 1 item name.
- 1 place-name card (Revelstoke Mountains).
- The F12 menu label, now "Quit Game".
- 1 party-member name label in DC EN.
- Report cards and dictionary labels use the game's own 12 px pixel font (the Japanese cards' font) instead of the 2016 smoothed font.

## Known gaps

- Some text pictures still carry the 2016 wording or Japanese and come in the next release: the party-name tiles of the Altered Ability menu (katakana), the report-card continuation cards, several dictionary cards and place-name cards, the chapter title cards 2 and 4, a few menu tile strips.
- The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose.
- One DC EN save-slot name still has the old spelling.

## Unchanged

- From v0.2.3: click-to-walk is on in the Altered build, and the New Game choice reads **Extra Content (Recommended)**.

# Release notes — v0.2.3

## Build

- **seraphic-blue-fullgame-EN-Altered-v0.2.3.zip** — EN + MOD + Altered. New game, or a save from the v0.2.0 to v0.2.2 Altered builds.
- The EN + MOD (DC) and JP + MOD (DC) builds are unchanged: download them from [v0.2.0](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.2.0).

## Click-to-walk (Altered build)

- Click-to-walk is now on in the Altered build (EasyRPG.ini: ClickWalk=1). Left-click ground to route there, click an NPC's feet to approach it, right-click or a direction key to stop; the green destination square shows the target (README, Quick tutorials). Battle-screen mouse rows and the timeline names stay off on Altered.
- It had been held back by a test-rig error: the rig replayed a click as Enter plus click on one frame, which Altered's dash routine reads as an Enter press. A real click never does that. Nothing in the game data was changed for it.

## Opening quote cards (Altered build)

- The 23 character quote cards of the opening (Picture/Ep00_M*) were still the 2016 patch's pictures with its loose wording. They are redrawn with the current script lines (each card = the same sentence as its message box in this translation), in the same condensed italic face as the opening poem cards. One card (Vene) has no message-box source in the script and carries a new translation of its Japanese.
- The DC builds (EN + MOD, JP + MOD) get the same cards with their next release.

## Label

- The New Game option now reads **Extra Content (Recommended)**, so a first-time player sees the recommendation on the screen itself. Map0004 only.

## Game data

- Changed against v0.2.2: Map0004, the 23 Ep00_M* pictures, EasyRPG.ini. Saves from the v0.2.0 to v0.2.2 Altered builds load. Everything else as v0.2.2 (below).

# Release notes — v0.2.2

## Build

- **seraphic-blue-fullgame-EN-Altered-v0.2.2.zip** — EN + MOD + Altered. New game, or a save from the v0.2.0 / v0.2.1 Altered build.
- The EN + MOD (DC) and JP + MOD (DC) builds are unchanged: download them from [v0.2.0](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.2.0).

## New: the Extra Content choice (Altered build)

- New Game now offers four options: About Game Modes, Original Mode, **Extra Content**, Arrange Mode.
- **Extra Content** is the first-play setup in one choice: MANY on, BATTLE off, the five ARRANGE switches Off (Original), Skip Battles with Weak Enemies OFF, Character EXP Gain ON1, HP Auto Fill on, TP Auto Fill off. It equals the six manual steps the v0.2.1 README described, verified by a full switch-and-variable comparison of the two saves (0 differences).
- Original Mode and Arrange Mode are unchanged (0 differences against v0.2.1).
- About Game Modes has a new page 3/6 for Extra Content. The "Game Mode Selection" title now shows on its own before the four choices (one extra key press).
- Game data changed: Map0004 only. Saves from the v0.2.0 and v0.2.1 Altered builds load.

## ZIP

- PLAY.cmd starts the Player by its full path. Before, with the Windows setting NoDefaultCurrentDirectoryInExePath on, the game did not start (exit 9009).
- The root text file (IMPORTANT README) names the Extra Content choice.

## Docs

- The early MOD screen (Cancel while the story locks the menu) is a feature of the DC builds' opening; the Altered build unlocks the menu right after its opening.
- Rewards are capped at 999,999 per fight by the engine; at 1/10 in the late game a scaled reward can be trimmed.
- In Arrange mode, Full heal does not revive KO members (Altered's own heal rule, kept on purpose).

# Release notes — v0.2.1

## Build

- **seraphic-blue-fullgame-EN-Altered-v0.2.1.zip** — EN + MOD + Altered. New game, or a save from the v0.2.0 Altered build.
- The EN + MOD (DC) and JP + MOD (DC) builds are unchanged: download them from [v0.2.0](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.2.0) (**seraphic-blue-fullgame-EN-v0.2.0.zip**, **seraphic-blue-fullgame-JP-v0.2.0.zip**).

## New: ARRANGE switches (Altered build)

- New MOD menu page **ARRANGE** (pages: SPEED, BATTLE, ARRANGE, CHEATS, INFO) with five rows. Each is On (Altered) or Off (Original); the default is On.
  - Full HP after battle. Off: HP refills from the SUP.HP pool, as in the original game.
  - Item limit per battle. Off: no per-battle item limit.
  - Escape always succeeds. Off: the original escape roll.
  - Counterattack always fires. Off: the original counter chance.
  - Enemy stats and resistances. Off: the original enemy data (enemies that are new in Altered keep theirs).
- Used only in Arrange mode. With BATTLE on, the Escape and Enemy rows follow BATTLE's own rules.
- Not switchable (always Altered in Arrange mode): critical hits, Charge, guard, pre-emptive odds, low-difficulty areas, Quick/Slow and Clever/Forgetful checks, value caps, HP/TP display, level-learned abilities, sphere duplicate bonus, stat coefficients, battle result multipliers, full-heal bottles, revive heals survivors, single-target hit roll, village patterns.
- New first-play recommendation: MANY on, BATTLE off, all five switches Off (Altered's extra content with the original battle rules). Original stays the purist choice; Full Arrange (BATTLE + MANY) is for a second run. Setup steps: README, "Which mode to pick".
- **+ marks gear that exists only in Altered's extra content** (on its name picture).
- Saves from v0.2.0 (Altered build) load. The switches appear (all On) after the next map change or battle; other settings are kept.
- The MOD INFO page explains each switch.
- README: a step-by-step dungeon trip under both rule sets, with the player's reasoning at each step.
- MOD: new games start with Escape always works Off; existing saves keep their setting. (The EN + MOD and JP + MOD builds get this with the next DC release.)
- Checked by scripted runs: battles with the rows Off and On under MANY only and in Original mode (item counts, held-back items, how HP is refilled), the retry cycle, escapes with the Escape row Off (a failed escape seen), a v0.2.0 save, enemy data with the Enemy row Off and On, the ARRANGE page on screen. The Counterattack row was checked in the game data; its Off chance was not measured in play. Not a full playthrough.

## Known items and issues

- v0.2.0 listed a DC retry issue after story battles; it could not be reproduced from normal play. Please report it with a save if you see it.
- Other known items: unchanged from v0.2.0 (below).

# Earlier: release notes — v0.2.0

## Builds

- **seraphic-blue-fullgame-EN-v0.2.0.zip** — EN + MOD (DC). Same game files as test.13 (re-tagged; only the documents and checksums inside the ZIP are new). Old saves keep working.
- **seraphic-blue-fullgame-EN-Altered-v0.2.0.zip** — EN + MOD + Altered (DC Altered Ver2.13 fan patch, translated). **New game only.**
- **seraphic-blue-fullgame-JP-v0.2.0.zip** — JP + MOD (DC), full Japanese game with the Japanese MOD menu.

## Altered build

- All Altered text in English; its Japanese picture text redrawn in English; the MOD menu adapted (rows Altered already has are left to its Config; see the README).
- Original mode = DC + bug fixes; first play: Original, NORMAL. Full Arrange (BATTLE + MANY) for a second play; MANY alone not recommended. (Superseded by the v0.2.1 recommendation above.)
- Standard RPG Maker files (sound effects, battle animations and a few others) are included under the names the game uses, so no runtime install is needed.
- EasyRPG Player only (8,040 variables, picture ids up to 78); RPG_RT.exe is not included.
- Checked by scripted runs: new game to the first map, the MOD screen, losing and retrying battles many times and then winning (Original and Arrange; items, money and MOD settings unchanged, Arrange item-limit items given back), the return-to-world-map cheat. Not a full playthrough.

## Known items to check (play test)

- The text-input door on Map0746.
- The scene on Map0524 with the added second box.
- Pictures 187, 327, 531, 532, 533, 542, 558, 559.
- Pictures drawn with tighter letter spacing: 342, 343, 510, 516, 518, 523, 527, 532, 533, 536, 538, 540, 542, 567, 568, 569, 570, 571, 572, 573, 576, 600, 601, 620, 622, 681, 682, 683, 687, 750, 758, 774, 780, 844, 865.

## Known issues

- EN + MOD (DC) build: after losing a story or boss battle, **Retry** may not respond; choose Accept defeat or load a save. Random-battle Retry works. (Shipped since test.10.) Update: this could not be reproduced from normal play (see v0.2.1 above); report it with a save if you see it.

## Next

- Planned for v0.2.1: MOD switches to turn off the Arrange battle rules (full HP after battle, item limit, always-escape, always-counter, enemy stat changes) one by one, so you can play the extra content with the original battle rules.
- Next DC text release: the derived review data for three Map0746 boxes is shifted by one box (the shipped game text is correct).

# Earlier: release notes — v0.1.0-test.13

## Translation corrections from the comparison review

- **22 dialogue boxes corrected** after an outside check: while the [comparison page](https://nostramadeus.github.io/seraphic-blue-mod/) was being built, its reviewers compared our lines with the Japanese and flagged the few where ours was weaker (a dropped qualifier, a Japanese idiom flattened into plain English, one word read in the wrong sense). Those are fixed. 4 boxes also had a pause moved to the line end (cosmetic).
- Changed files: 22 map files. No Player, picture or save changes.

## Update safely

1. Close the game and back up the actual save folder used by your launcher.
2. Easiest: download **seraphic-blue-fullgame-EN-v0.1.0-test.13.zip**, extract it, and copy your old **saves** folder into it.
3. Or, on test.11 or test.12: extract **seraphic-blue-update-v0.1.0-test.13.zip** into the game folder containing **RPG_RT.ldb** and replace the 22 map files. On test.10 or older, apply the test.11 update first (it carries the Player).
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
