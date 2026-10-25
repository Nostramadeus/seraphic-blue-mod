# Compatibility — v0.3.3

| Route | Included Player | Verification |
| --- | --- | --- |
| Windows x86-64 | 0.8.1.1-sb5, v0.3.3 PortAudio patch | Final MOD/menu/save/retry replays; title MIDI startup with audio enabled through an inaudible SDL dummy device |
| Native Linux x86-64 | 0.8.1.1-sb5, bundled helper libraries | Headless tests passed 36 replay cases on Debian 11, Arch and Ubuntu 24.04 containers. All 18 generated save states matched Windows. A separate normal-speed replay matched Windows on all three systems (nine images). Timeline and save-name checks also matched all 111 images and 36 generated save states. MIDI produced nonzero audio through a virtual disk driver. Launcher paths with spaces and save/config storage passed. Physical Steam Deck, Proton and desktop display/audio drivers remain untested. |
| Steam / Proton | Included Windows Player | AryaNetwork supplied the verified crash fix; our tests did not run Proton |
| Steam Deck native | Included Linux Player | Container tests only; physical Deck controls, display and audio unverified |

The native build was compiled on Debian 11. It requires GLIBC_2.29, GLIBCXX_3.4.26, CXXABI_1.3.9, zlib and working system display/audio drivers. A version number alone does not prove every distribution works. Keep **native-linux/lib** together with its Player.

Turbo screenshots sometimes differed during transition frames; the exact image comparisons above used normal speed.

Native MIDI uses FluidLite with an available soundfont, otherwise the built-in FM synthesizer. The shipped game uses MIDI, MP3 and WAV; module-music playback is not enabled in this native build. No physical audio-device check is claimed.

## Saves

Keep DC and Altered saves on their matching builds. Use a new extracted folder and copy your **saves** and **config** folders. [Installation and migration](INSTALL.md). No full playthrough or universal-save compatibility claim is made.

## Retained Japanese material

The English DC manual is mostly the 2016 English translation; four pages remain Japanese and two are mixed. Altered's manual and update history are Japanese. Some status labels keep an English word with a Japanese gloss; character reading captions, original artist-name credits and small background/sprite lettering remain as retained artwork. These exceptions are documented; this is not a claim that every image and manual page is English.

## Translation review scope

Application checks confirm that approved wording reached the game files. Meaning review checks the English against Japanese. The recorded additional review is still partial:

- **Altered-specific text:** 1,613 of 3,528 entries have matching review records: 982 independent, 623 earlier and 8 targeted mode checks. The other 1,915 have origin and application evidence.
- **Shared English text:** 11,328 transfers have separate origin and application checks. They are recorded separately from new meaning reviews.
- **DC text:** 22,137 entries lack matching records for the additional Japanese-meaning review pass. Earlier general retranslation and review work remains recorded separately.

## JP resource-check scope

The existing JP data retains 246 unresolved static resource references (13 in the RTP name table, 233 outside it). The JP title tests had no missing-resource errors. We have not proved that every unresolved reference is unreachable, and do not claim complete resource coverage or a full playthrough.

## Earlier input checks

The test.6 Windows pass ran 15 focused input/movement tests (350 assertions), menu/target and equipment/save replays, plus seven enemy-hover/page regressions. Later versions added history, battle controls and text settings; their release notes identify the later checks. Those historical checks do not substitute for physical mouse, Deck or full-playthrough testing.

[Release notes](RELEASE-NOTES.md) · [Source and library replacement](SOURCE-ACCESS.md)
