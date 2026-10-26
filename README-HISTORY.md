<a name="history"></a>
# Seraphic Blue — README history

[Back to current setup](README.md#downloads) · [Full release notes](RELEASE-NOTES.md) · [Changelog](CHANGELOG.md)

These entries describe the release named in each heading. An old limitation or pending item is **not** a statement about the current game. Use the current [player guide](PLAYER-GUIDE.md) and [compatibility notes](COMPATIBILITY.md) for present behavior.

<a name="release-history"></a>
## Release history

<details><summary>v0.3.8 — saved commands and English corrections</summary>

saved manual encounter commands in English DC/Altered with explicit R or optional Auto-button start and stop on Windows/native Linux; the idle button defaults Off under F1 > Engine; Stop remains visible during replay; four approved English wording corrections (three matching Altered passages), and one directly translated DC picture card. Existing saves, battle rules and the separate experimental UI are unchanged.

</details>

<details><summary>v0.3.7 — picture text and optional song titles</summary>

English DC received 83 additional clearer-font cards; Altered received the 75 matching cards. Eight were widened by 1–20 pixels, with complete wording and original heights retained. One source card remained unresolved **at that release**; v0.3.8 translates it directly in DC. Eight Altered absences/revisions remained untouched.

The optional **F1 → Engine → Song title banner** starts Off. It shows the music filename after a track change, uses multiple pages for long names, and pauses while dialogue, menus, battle or transitions hide it. Fast-forward does not shorten its four-second display. It is an engine preference, separate from game saves. [Full v0.3.7 entry](RELEASE-NOTES.md#v037--clearer-picture-text-and-optional-song-titles).

</details>

<details><summary>v0.3.6 — mouse interaction, comparison and healing</summary>

The following features shipped in v0.3.6. An earlier README placed them under v0.3.7; the [release notes](RELEASE-NOTES.md) record their correct version.


- Mouse selection follows visible character artwork, native counter interaction and a unique adjacent exit. Arrival handling retains touch transfers during a pure speed adjustment.
- English shops add **Tab Compare** for weapons and frames, using native calculations without purchases or equipment changes.
- Altered: Shift dash preserves mouse movement; MOD hover updates its hint; HP Supplement controls appear with free healing Off; new Extra Content HP Auto Fill starts Off; manual FREE rewards stay ordinary.
- English: 101 approved font cards per edition use a consistent face; 108 title calls keep their complete names inside the screen; one minor Counter Attack wording correction. 84 mixed-layout cards remain unchanged.

</details>

<details><summary>v0.3.5 (Altered only)</summary>

- Restores missing Map0022 (Turku Inn upstairs) and Map0088. Existing saves work; Player, Linux runtime and the DC builds are unchanged. This urgent map-only hotfix received file-integrity checks, without a new gameplay test.

</details>

<details><summary>v0.3.4 (all three builds)</summary>

- Consistent menu hover, native keyboard handoff and click confirmation. No game text, pictures, event data or save-format changes. Same sb6 source for Windows/native Linux; focused current-release tests. [Matching Player source](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.4/seraphic-blue-player-source-v0.3.4.zip).

</details>

<details><summary>v0.3.3 (all three builds)</summary>

- **Proton title-screen crash:** bundled PortAudio library patched using AryaNetwork's diagnosis and verified fix ([issue #1](https://github.com/Nostramadeus/seraphic-blue-mod/issues/1)); Windows regression checked, Proton and physical Deck hardware not tested here.
- **Current native Linux Player:** the same 0.8.1.1-sb5 source and custom features as Windows. [Setup and exact test limits](LINUX.md).
- **Credits and source:** Altered now shows the 2016 translator/proofreader cards; [current Player source](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.3/seraphic-blue-player-source-v0.3.3.zip) accompanies the release.
- **English content and battle labels:** Eight dictionary captions corrected, full Poison label and the full Blue-Haired Woman save name. DC restores its native battle controls; Altered gains full timeline names. The DC English build restores 132 dialogue corrections missed by earlier packages, with 11 extra message boxes to retain the full wording. Altered also fixes three lines that used outdated translation inputs. Both English builds translate six remaining Daisy, Gerard and Owen portrait captions.
- **Retained Japanese material:** The English DC manual is mostly the 2016 English translation; four pages remain Japanese and two are mixed. Altered's manual and update history are Japanese. Some status labels keep an English word with a Japanese gloss; character reading captions, original artist-name credits and small background/sprite lettering remain as retained artwork. These exceptions are documented; this is not a claim that every image and manual page is English.

</details>

<details><summary>v0.3.2 (all three builds)</summary>

- **Menu labels (English builds):** 12 menu labels that were still Japanese in v0.3.1 are now in English (Altered; 6 of them in DC EN too): the three magic types of the Ability menu, Qty to Make, Discount, Qty to Sell, Paralysis, Ailment Trigger Rate / Defense Rate and the three magic-level labels of the Status menu, and Poison as **PSN**. Labels that did not fit in the game font use a narrower font, not a shortened word. DC EN Status screen: the movement stat reads **MOV** (the 2016 label said "DEX"), and "Field Mutation Element" replaces the 2016 label "Element Physical Cast". Both English ZIPs carry **MENU-LABEL-NOTES.txt** with the list.
- **Story pictures and credits (English builds):** All remaining story pictures redrawn in English (Altered 32 files, DC EN 43): 12 explanation screens, episode title cards, battle chant pictures, the Panorama menus (temporary save, organize, EXT bonus, shop line-up), the title-screen labels (DC EN), one battle background, unused leftover pictures, two dictionary titles and end-credits cards. End credits: the music credits card follows the Japanese list (both English builds); a DC EN credits card now carries the Japanese music credit together with the 2016 team; the 2016 translator credits card now also shows in the DC EN credits sequence that lacked it. One glossary term is written out in its full form in 2 boxes (both English builds).
- **New text file (Altered ZIP):** The Altered ZIP adds **HIDDEN-DICTIONARY-ENTRIES (SPOILERS).txt**: 3 unreachable dictionary entries written for an unfinished sequel, in a spoiler-marked text file. The game itself is unchanged; the entries stay unreachable in game.
- **Other:** JP + MOD (DC): no content changes; it carries the new version number so the three builds stay in step. Player: unchanged from v0.3.1 (Windows Player 0.8.1.1-sb4; native Linux Player = the older test.2 build). Clicking an ally target in battle is now tested with a two-member party (passed).
- **Known gaps:** The native Linux Player (**play-linux.sh**) is unchanged and has none of the v0.3.1 Player features (use Player.exe on Windows, or Proton on Linux and Steam Deck). The Altered build's credits do not show the 2016 translator card. The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose.
- **Saves:** Altered saves from v0.2.0 to v0.3.1 load. DC saves load as before (no save-format change). DC saves do not move to the Altered build.

</details>

<a name="v031"></a>
<details><summary>v0.3.1 (all three builds)</summary>

- **New Windows Player 0.8.1.1-sb4** in all three ZIPs. Battle mouse on the Altered build: command grid, enemy targets with hover, ability and item rows with hover, page change by mouse wheel, category tabs, ally targets. MOD menu, SPEED page: new rows **Text speed** (1x / 2x / 4x / Instant) and **Text pauses** (1x / 2x / 4x; shortens the pauses inside messages, never removes them). Choice guard: for a third of a second a choice window ignores Enter that is held down or pressed repeatedly, so the Skip prompts are not skipped by accident. Cancel is unaffected. Save-slot placeholder name now reads "Blue-Hair Lady" (DC EN).
- **English builds:** Dictionary (Character Profiles and Glossary) re-sorted into English alphabetical tabs A-C ... Y-Z (182 entries). Empty tabs cannot be entered. Unlocks and saves are unchanged. 24 menu tile strips in English (272 words), including the party names of the Altered Ability menu. 14 menu words given more tiles or a ruled short form (10 by extra map tiles, 4 by a short form such as "Owned"); the 8 element labels of the Status menu now use two-letter codes (Fi Wa Wi Ea Li Da He Br). 27 pictures redrawn: place-name banners, world-map guides, ending-screen panels, shop and inn signs. Actor-name strings use the spelling Yancy. 108 story cards and labels redrawn (pulled cards corrected, Er and Sieg continuation text, dictionary labels, chapter titles, staff credits, Panorama menus).
- **Linux:** The new Player features need **Player.exe**: on Windows, or on Linux and Steam Deck through Proton. The native Linux Player (**play-linux.sh**) is unchanged from earlier releases (the older test.2 build) and has none of them.
- 37 text pictures still carry the 2016 wording or Japanese and come in the next release: 12 explanation screens, the Panorama menus (temporary save, organize, status, EXT bonus and shop line-up), the title-screen labels, a few art-background titles and message cards. In the menus, nine labels stay Japanese for now (the three magic-level labels of the Ability menu, Poison, Paralysis and four shop quantity labels: their English needs more room than the screen layout gives).
- **Known gaps:** Three dictionary detail pages that no list row reaches (Gaia, Alma, Seraphic Blue Amplifier) stay as the Altered authors left them. Clicking an ally target in battle was tested with a one-member party only. The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose.
- **Saves:** Altered saves from v0.2.0 to v0.3.0 load. DC saves load as before (no save-format change). DC saves do not move to the Altered build.

</details>

<details><summary>v0.3.0 (all three builds)</summary>

- **DC builds rebuilt** (EN + MOD and JP + MOD) through the same release pipeline as the Altered build: full game folders verified file by file, the text file **IMPORTANT README (MUST READ).txt** at the ZIP root, and PLAY.cmd starts the Player by its full path. Saves load as before in both DC builds; DC saves still do not move to the Altered build.
- **EN + MOD (DC)** also gets the 23 retranslated opening quote cards (the same cards as Altered v0.2.3) and the newer text of three maps (Map0025, Map0026, Map0140: corrections from 2026-10-22 that the shipped game had but the source folder had lost). JP + MOD (DC) keeps its 141 standard RPG Maker asset files.
- **Redrawn text pictures in the English builds** (Altered 78 files, EN + MOD DC 73 files): 25 episode title cards (titles now carry the complete Japanese title; the English episode-number row and the German row are unchanged), 15 Er explanation cards that were still Japanese in the Altered build, 18 report and diary cards, dictionary term labels (Altered 9, DC 17), 3 item description boxes and 1 item name, 1 place-name card (Revelstoke Mountains), the F12 menu label (now "Quit Game"), 1 party-member name label in the DC build. Report cards and dictionary labels use the game's own 12 px pixel font instead of the 2016 smoothed font.
- **Known gaps:** some text pictures still carry the 2016 wording or Japanese and come in the next release (the party-name tiles of the Altered Ability menu, the report-card continuation cards, several dictionary and place-name cards, the chapter title cards 2 and 4, a few menu tile strips). The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose. One EN + MOD (DC) save-slot name still has the old spelling.
- Unchanged from v0.2.3: click-to-walk is on in the Altered build; the New Game choice **Extra Content (Recommended)**.

</details>

<details><summary>v0.2.1 (Altered build only)</summary>

- **ARRANGE page** in the MOD menu: five switches that turn single Arrange battle rules back to the original rules (see [Altered build](PLAYER-GUIDE.md#altered)).
- **First-play recommendation:** MANY on, BATTLE off, all five switches Off.
- **+ marker** on the name pictures of gear that exists only in Altered's extra content.
- Saves from the v0.2.0 Altered build carry over. The EN + MOD (DC) and JP + MOD (DC) builds are unchanged (v0.2.0).

</details>

<details><summary>v0.2.0</summary>

- **Three builds:** EN + MOD (DC, same game data as test.13), EN + MOD + Altered (new), JP + MOD (DC, full game).
- **Altered build:** see [Altered build](PLAYER-GUIDE.md#altered). New game only.
- No changes to the DC game files since test.13.

</details>

<details><summary>test.13</summary>

- **22 dialogue boxes corrected** after an outside check: while the [comparison page](https://nostramadeus.github.io/seraphic-blue-mod/) was being built, its reviewers compared our lines with the Japanese and flagged the few where ours was weaker (a dropped qualifier, a Japanese idiom flattened into plain English, one word read in the wrong sense). Those are fixed. 4 boxes also had a pause moved to the line end (cosmetic).
- Changed files: 22 map files. No Player, picture or save changes.

</details>

<details><summary>test.12</summary>

- **63 more dialogue boxes corrected to match the Japanese.** This completes the audit of all 3,013 "full" four-line boxes (the ones most likely to have been shortened to fit): 89 of them had lost a qualifier, a hedge, a clause or a Japanese idiom's image, and all are restored. 2 of the new corrections use two boxes instead of one shortened box.
- Changed files: 45 map files. No Player, picture or save changes.
- **Old saves work.** A save from the Japanese original, from the 2016 English patch or from any test release loads in this version: copy your SaveXX.lsd files into the **saves** folder.

</details>

<details><summary>test.11</summary>

- **Message history (Windows Player):** scroll back through the last 100 message boxes you read, with the choice you picked. Open it with <img src="docs/img/keys/mouse-wheel.svg" height="22" alt="Mouse wheel"> **up** or **Page Up** while a message is showing or while you walk on the field; scroll with the <img src="docs/img/keys/mouse-wheel.svg" height="22" alt="Mouse wheel"> wheel or <img src="docs/img/keys/up.svg" height="22" alt="Up"> / <img src="docs/img/keys/down.svg" height="22" alt="Down">, page with Page Up / Page Down, close with **<img src="docs/img/keys/escape.svg" height="22" alt="Escape"> / B / <img src="docs/img/keys/mouse-right-click.svg" height="22" alt="Right click">**. It is cleared when you load or start a game and is never saved. The native Linux Player and the Mac Player do not have it.
- **67 dialogue boxes corrected to match the Japanese** (dropped qualifiers or hedges restored, Japanese idioms kept as their own image, 14 names and terms made consistent with the in-game dictionary). 7 of them now use two boxes instead of one shortened box. All 585 boxes whose English was identical to the 2016 patch were checked against the Japanese and found correct.
- Changed files: Player.exe and 43 map files. Saves, config and EasyRPG.ini are untouched; earlier saves load normally.

</details>

<details><summary>test.10</summary>

- One opening dialogue line corrected to match the Japanese.

</details>

<details><summary>test.9</summary>

- **55 picture cards retranslated from the Japanese:** 52 history timeline cards (names and terms now match the rest of the game; 10 cards had the wrong meaning), the two opening chant cards and the opening poem card.
- No Player, map or save changes.

</details>

<details><summary>test.8</summary>

- **MOD settings from the very start:** while the story still locks the game menu (the opening chapters), Cancel / <img src="docs/img/keys/escape.svg" height="22" alt="Esc"> / Deck B opens the MOD screen directly; Cancel returns to the same spot. After the menu unlocks, nothing changes. This early window exists on the DC builds; the Altered build unlocks the menu right after the opening, so Cancel there opens the normal menu.
- **Clicking to walk now works in the opening rooms** (it needed the unlocked game menu before).
- **Opening poem card:** the second card of the opening poem is retranslated to match the Japanese.
- Both need the included Windows Player (Windows, Proton, Steam Deck). The native Linux Player and the stock Mac Player keep the older behaviour.

[Full release notes](RELEASE-NOTES.md) · [Changelog](CHANGELOG.md)

</details>

<a name="old-updates"></a>
## Archived update procedures

**For archived test releases only.** For a current installation, use the [four-step full-game update](README.md#keep-your-saves). These old patch links and file lists are retained for reference.

<details><summary>Test-release patch ZIPs — original sequence</summary>

1. Close the game. Keep a backup of your actual save folder.
2. On test.6 or older, first apply the [test.7 image update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.7/seraphic-blue-image-update-v0.1.0-test.7.zip) (extract beside **RPG_RT.ldb**, replace the Picture files).
3. On test.7 or older, [download the test.8 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.8/seraphic-blue-update-v0.1.0-test.8.zip). Extract it into your game folder, beside **RPG_RT.ldb**, and allow replacement of **Player.exe**, **RPG_RT.ldb**, **Map0003.lmu** and one **Picture** file. If your Player.exe lives in another folder (older patch installs), copy the new Player.exe there instead.
4. On test.8 or older, [download the test.9 picture update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.9/seraphic-blue-update-v0.1.0-test.9.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of the 55 **Picture** files.
5. On test.9 or older, [download the test.10 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.10/seraphic-blue-update-v0.1.0-test.10.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of **Map0507.lmu**.
### Later test releases

6. On test.10 or older, [download the test.11 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.11/seraphic-blue-update-v0.1.0-test.11.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of **Player.exe** and the 43 **Map** files.
7. On test.11, [download the test.12 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.12/seraphic-blue-update-v0.1.0-test.12.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of the 45 **Map** files.
8. [Download the test.13 update](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.13/seraphic-blue-update-v0.1.0-test.13.zip). Extract it into the same folder, beside **RPG_RT.ldb**, and allow replacement of the 22 **Map** files.
9. On test.13, v0.2.0, v0.3.0 or v0.3.1 (DC): download the v0.3.8 EN + MOD (DC) build, extract it to a new folder and copy your **saves** and **config** folders into it. Keep the new **EasyRPG.ini**.
10. Copy your **saves** and **config** folders. Keep the new release's **EasyRPG.ini** so its current controls and label tables remain enabled. Saves from earlier tests load normally.

</details>

<details><summary>test.1–test.5 — optional historical engine upgrade</summary>

Skip this if you installed the test.6 or test.7 full game: the test.8 update above already replaces Player.exe.

1. Close the game and back up the **saves** folder (or your existing custom save location).
2. Download the [test.6 Windows Player ZIP](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-windows-x86_64-v0.1.0-test.6.zip) for Windows or Proton (the newest Player ZIP with all DLLs). Extract it separately.
3. Copy **Player.exe and all .dll files from that same ZIP** into the folder containing your old Player.exe. Replace those files only. Keep saves, EasyRPG.ini and game data.
4. Then apply the test.7 image update and the test.8 update from the section above; the test.8 Player.exe replaces the test.6 one and uses the same DLLs.

Native Linux now uses the same Player source as Windows; see [Linux setup and tested limits](LINUX.md). Existing patch-based installations can continue using their current game/save paths.

</details>
