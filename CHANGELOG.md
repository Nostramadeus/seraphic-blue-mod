# Changelog

## v0.3.1

All three builds. New Windows Player 0.8.1.1-sb4 in all three ZIPs: Battle mouse on the Altered build: command grid, enemy targets with hover, ability and item rows with hover, page change by mouse wheel, category tabs, ally targets. MOD menu, SPEED page: new rows **Text speed** (1x / 2x / 4x / Instant) and **Text pauses** (1x / 2x / 4x; shortens the pauses inside messages, never removes them). Choice guard: for a third of a second a choice window ignores Enter that is held down or pressed repeatedly, so the Skip prompts are not skipped by accident. Cancel is unaffected. Save-slot placeholder name now reads "Blue-Hair Lady" (DC EN). English builds: Dictionary (Character Profiles and Glossary) re-sorted into English alphabetical tabs A-C ... Y-Z (182 entries). Empty tabs cannot be entered. Unlocks and saves are unchanged. 24 menu tile strips in English (272 words), including the party names of the Altered Ability menu. 14 menu words given more tiles or a ruled short form (10 by extra map tiles, 4 by a short form such as "Owned"); the 8 element labels of the Status menu now use two-letter codes (Fi Wa Wi Ea Li Da He Br). 27 pictures redrawn: place-name banners, world-map guides, ending-screen panels, shop and inn signs. Actor-name strings use the spelling Yancy. 108 story cards and labels redrawn (pulled cards corrected, Er and Sieg continuation text, dictionary labels, chapter titles, staff credits, Panorama menus). The new Player features need Player.exe: on Windows, or on Linux and Steam Deck through Proton. The native Linux Player (play-linux.sh) is unchanged from earlier releases (the older test.2 build) and has none of them. Known gaps: Three dictionary detail pages that no list row reaches (Gaia, Alma, Seraphic Blue Amplifier) stay as the Altered authors left them. Clicking an ally target in battle was tested with a one-member party only. The game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose. Saves: Altered saves from v0.2.0 to v0.3.0 load. DC saves load as before (no save-format change). DC saves do not move to the Altered build. Still open for the next release: 37 text pictures (12 explanation screens, the Panorama menus, the title-screen labels, a few art-background titles and message cards) and nine menu labels whose English needs more room than the layout gives (the three magic-level labels, Poison, Paralysis, four shop quantities).

## v0.3.0

All three builds. The DC builds (EN + MOD, JP + MOD) are rebuilt through the same release pipeline as the Altered build: full game folders verified file by file, **IMPORTANT README (MUST READ).txt** at the ZIP root, PLAY.cmd starts the Player by its full path. EN + MOD (DC) also gets the 23 retranslated opening quote cards (the same cards as Altered v0.2.3) and the newer text of Map0025, Map0026 and Map0140 (corrections from 2026-10-22 that the shipped game had but the source folder had lost); JP + MOD (DC) keeps its 141 standard RPG Maker asset files. English builds: redrawn text pictures (Altered 78 files, DC EN 73): 25 episode title cards (complete Japanese title; the English episode-number row and the German row unchanged), 15 Er explanation cards that were still Japanese in the Altered build, 18 report and diary cards, dictionary term labels (Altered 9, DC EN 17), 3 item description boxes and 1 item name, 1 place-name card (Revelstoke Mountains), the F12 menu label (now "Quit Game"), 1 party-member name label in DC EN; report cards and dictionary labels use the game's own 12 px pixel font instead of the 2016 smoothed font. Unchanged from v0.2.3: click-to-walk on in the Altered build, the Extra Content (Recommended) New Game choice. Saves load as before in both DC builds (no save-format change); DC saves still do not move to the Altered build. Known gaps: some text pictures still carry the 2016 wording or Japanese and come in the next release (party-name tiles of the Altered Ability menu, report-card continuation cards, several dictionary and place-name cards, chapter title cards 2 and 4, a few menu tile strips); the game's own manuals (Manual/, ManualAlt/ and the two Japanese history text files) ship in Japanese on purpose; one DC EN save-slot name still has the old spelling.

## v0.2.3

Altered build only. Click-to-walk is on (EasyRPG.ini: ClickWalk=1); it had been held back by a test-rig error, not by the game. The 23 opening character quote cards (Picture/Ep00_M*) are retranslated to the current script lines, same face as the opening poem cards; the DC builds get them with their next release. The New Game option now reads **Extra Content (Recommended)**. Game data: Map0004, 23 pictures, EasyRPG.ini; saves from the v0.2.0 to v0.2.2 Altered builds load.

## v0.2.2

Altered build only. Fourth New Game choice **Extra Content**: MANY on, BATTLE off, the five ARRANGE switches Off, Skip Battles with Weak Enemies OFF, Character EXP Gain ON1, HP Auto Fill on, TP Auto Fill off. It replaces the six-step manual setup for a first play; About Game Modes gets a page for it (3/6). The "Game Mode Selection" title now shows on its own before the four choices. Game data: Map0004 only; saves from the v0.2.0 and v0.2.1 Altered builds load. ZIP: PLAY.cmd starts the Player by its full path (fixes exit 9009 when Windows' NoDefaultCurrentDirectoryInExePath is set); root text updated. Docs: the early MOD screen via Cancel is a DC-opening feature; rewards are capped at 999,999 per fight by the engine; Full heal in Arrange mode does not revive (Altered's rule). Full heal was NOT changed.

## v0.2.1

Altered build only: MOD menu page ARRANGE with five switches that turn single Arrange battle rules back to the original rules (full HP after battle, item limit per battle, escape always succeeds, counterattack always fires, enemy stats and resistances); new first-play recommendation (MANY on, BATTLE off, switches Off); + marker on gear that exists only in Altered's extra content; v0.2.0 Altered saves carry over; new games start with the MOD row Escape always works Off (existing saves keep their setting). EN + MOD (DC) and JP + MOD (DC) unchanged (v0.2.0).

## v0.2.0

Three builds: EN + MOD (DC, same game data as test.13), EN + MOD + Altered (new, new game only), JP + MOD (DC). Altered: all text in English, picture text redrawn, MOD menu adapted, Original mode = DC + bug fixes, standard RPG Maker files included. Known issue: Retry after a lost story battle on the DC build may not respond. (Later not reproduced from normal play; see v0.2.1.)

## v0.1.0-test.13

22 dialogue boxes corrected after the comparison-page review (plus 4 cosmetic pause moves). Map-only update; saves unchanged. New: the public comparison page https://nostramadeus.github.io/seraphic-blue-mod/

## v0.1.0-test.12

63 more dialogue boxes corrected against the Japanese; the audit of all 3,013 full four-line boxes is complete. Map-only update; saves unchanged. Old saves from any version load.

## v0.1.0-test.11

Message history viewer in the Windows Player (wheel up / Page Up). 67 dialogue boxes corrected against the Japanese; the 585 boxes identical to the 2016 English were audited and kept. Player and map data update; saves unchanged.

## v0.1.0-test.10

One opening dialogue line corrected to match the Japanese. Map-only update.

## v0.1.0-test.9

55 picture cards retranslated from the Japanese (history timeline, opening chant and poem cards). Picture-only update.

## v0.1.0-test.8

MOD settings reachable from the start: while the story locks the game menu, Cancel / Esc / Deck B opens the MOD screen directly. Click-to-walk works in the opening rooms. Opening poem card retranslated. Windows Player and game data update; saves unchanged.

## v0.1.0-test.7

178 corrected or realigned image files, including opening narration and six battle labels/help images. Image-only update.

## v0.1.0-test.6

Ally targets, scripted and native menu pointer support, character quick tabs, contextual hints and field tile/destination feedback. Runtime-only update.

## v0.1.0-test.5

Mouse motion selects a visible enemy and refreshes the native name, target icon and cursor without attacking. Keyboard priority and all-target choices are preserved. Runtime-only update.

## v0.1.0-test.4

Direct enemy sprite targeting; battle ability/item wheel paging and clickable page counter. Runtime-only update, saves and game data retained.

## v0.1.0-test.3

Opt-in ground click walking, cardinal NPC approach and interaction once, and keyboard/right-click cancellation. Windows/Proton runtime-only update; existing test.2 patches retained.

## v0.1.0-test.2

Direct category clicks, motion-only native highlights, scoped target wheel, short timeline names with duplicate-only suffixes, and a verified-backup updater from matching test.1. Existing translation/help/HP-TP fixes retained.

## v0.1.0-test.1

First public TEST: English translation/redraw plus MOD patch; Japanese MOD-only patch; tested custom Player mouse/pause/animation improvements. Separate Windows and Ubuntu 22.04 packages, hardware-unverified Proton TEST guide/package, exact fork/dependency source access and notices. No stable/full-playthrough/Deck verification claim.
