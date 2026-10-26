# Compatibility — v0.3.6

| Route | Included Player | Verification |
| --- | --- | --- |
| Windows x86-64 | 0.8.1.1-sb7, unchanged patched libraries | Focused arrival and Turku clerk/exit checks; English weapon/frame comparison. Final Windows DC Buy preserves native actor and full inventory state; unchanged earlier paths retain exact receipts. |
| Native Linux x86-64 | 0.8.1.1-sb7, bundled helper libraries | One controlled headless Altered shop comparison/Cancel replay on Debian 11. Final source differs only by two bound DC copy-range corrections verified on Windows; no second Linux replay claimed. |
| Steam / Proton | Included Windows Player | Earlier PortAudio crash fix retained; Proton not run here |
| Steam Deck native | Included Linux Player | Physical controls, display and audio unverified |

The native build uses Debian 11 and requires GLIBC_2.29, GLIBCXX_3.4.26, CXXABI_1.3.9, zlib and working system display/audio drivers. Symbol requirements do not prove universal distribution support. Keep **native-linux/lib** with Player.

Earlier v0.3.3 sb5 tests covered 36 replay cases on Debian 11/Arch/Ubuntu containers, 18 matching states, nine exact normal-speed images, 111 controlled images and 36 states. Those are earlier-build evidence, not another test pass for sb7. Unchanged libraries, launchers and individual game-file hashes retain their earlier receipts. The v0.3.6 game data includes the explicitly listed settings, comparison bindings, English title placement, font cards and minor wording change. No full playthrough or physical audio-device check is claimed.

Native MIDI uses FluidLite with an available soundfont, otherwise the included FM synthesizer. MIDI, MP3 and WAV remain supported; module-music playback remains disabled in this native build.

## Saves

Keep DC and Altered saves on their matching builds. Use a new extracted folder and copy your **saves** and **config** folders. [Installation and migration](INSTALL.md). No full playthrough or universal-save compatibility claim is made.

## Retained Japanese material

The English DC manual is mostly the 2016 English translation; four pages remain Japanese and two are mixed. Altered's manual and update history are Japanese. Some status labels keep an English word with a Japanese gloss; character reading captions, original artist-name credits and small background/sprite lettering remain as retained artwork. These exceptions are documented; this is not a claim that every image and manual page is English.

## Translation review scope

Application checks confirm that approved wording reached the game files. Meaning review checks the English against Japanese. The recorded additional review is still partial:

- **Altered-specific text:** 1,613 of 3,528 entries have matching review records: 982 independent, 623 earlier and 8 targeted mode checks. The other 1,915 have origin and application evidence.
- **Shared English text:** 11,328 transfers have separate origin and application checks. They are recorded separately from new meaning reviews.
- **DC text:** 22,137 entries lack matching records for the additional Japanese-meaning review pass. Earlier general retranslation and review work remains recorded separately.

The later basic screen is complete for all **24,052 requested text locations**: **22,942** had comparable source text and **1,110** were unassessable. A location is a saved message or entry and can contain more than one displayed line. The screen covered **21,090 distinct Japanese/English pairs** in 211 batches; repeated locations can share one pair. One confirmed minor Counter Attack wording issue was corrected; no major mistranslation was confirmed in this screen. Unassessable entries are not passes. This basic screen does not replace the separate additional meaning-review records above.

## Remaining source and artwork limits

The English editions replace 101 approved font cards each. Another 84 mixed-layout cards remain unchanged because their layout or artwork needs a separate decision. The completed geometry pass keeps all 108 bound location-title calls on screen without shortening their words.

Original DC and Altered both contain references to missing maps 550 and 824. The static scan found conditional routes but did not establish that players can reach them. No replacement maps have been invented. The separately reported Turku Inn missing-map problem was repaired in v0.3.5 and that repair is retained.

## JP resource-check scope

The existing JP data retains 246 unresolved static resource references (13 in the RTP name table, 233 outside it). The JP title tests had no missing-resource errors. We have not proved that every unresolved reference is unreachable, and do not claim complete resource coverage or a full playthrough.

## Earlier input checks

The test.6 Windows pass ran 15 focused input/movement tests (350 assertions), menu/target and equipment/save replays, plus seven enemy-hover/page regressions. Later versions added history, battle controls and text settings; their release notes identify the later checks. Those historical checks do not substitute for physical mouse, Deck or full-playthrough testing.

[Release notes](RELEASE-NOTES.md) · [Source and library replacement](SOURCE-ACCESS.md)
