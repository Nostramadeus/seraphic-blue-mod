# PITFALLS — what broke when two mods met, and how we found it

For future sessions, contributors and forks. Read before touching tools/mod_build.py, the Altered base, or any common event the two mods share. Each entry: what broke, why, how it was found, the fix, and the test that now guards it. Dates are 2026-10-23 unless noted. Evidence folders are under work/.

## The shape of the problem

Seraphic Blue is not "a 2000 JRPG". It is about 1,400 event programs in RPG Maker 2000's event language: no types, no scopes, global numbered switches and variables, pointer-style indirect access (write to variable number X where X is itself a variable). Altered (fan patch, 2012) rewrote the battle engine, the enemy database and the menu maps in that language. Our MOD (2026) was written against the DC original. Every bug below sits at the seam between the two; none was in the base game.

## Catalogue

### 1. Retry a lost battle froze the game (Altered build)
- **Symptom:** after "Retry this battle" the screen stays on the battle, hero at 0 HP, no input.
- **Cause:** our retry block jumps back into the battle map from inside the battle-end routine (CE71). On DC nothing runs after that jump. Altered added cleanup after the same spot (switches S1-S380 off, battle variables cleared), so the retried battle had no setup.
- **Found by:** scripted challenger (work/release-v0.2.0-20261023/challenger_retry.py): lose, retry, compare saves.
- **Fix:** End Event Processing (12310) right after the jump, Altered profile only.
- **Lesson:** an insertion that is safe because "nothing runs after it" is a hidden dependency on the code that follows. On a rewritten base, re-read the rest of the routine.

### 2. MOD settings placed on top of Altered's pointer range
- **Symptom:** one won Arrange-mode battle: 4 of 9 items vanished, 21 phantom item types appeared with counts equal to our settings, settings reset to 0.
- **Cause:** the ruling put the MOD variables at V5001-V5040 because "no Altered command names an id above 5000". Altered's per-battle item limit parks counts at V[5000 + item id] through pointer writes, which a literal-id search cannot see.
- **Found by:** the same challenger, item x9 through a won battle.
- **Fix:** static pointer-base scan (build/scripts/s09c_pointer_scan.py: bases 5001, 5061, 5101, 5201, 6001, 6002; max reachable 6,952), MOD block moved to V8001+ (array extended to 8040), EasyRPG.ini keys follow.
- **Lesson:** free-id proofs must include pointer bases + maximum index, and still cannot bound 3,568 indirect writes statically; the runtime test is the real proof.

### 3. Retry lost held-back items (Altered build, Arrange mode)
- **Symptom:** item 12 x9 -> 5 after a retried battle was finally won.
- **Cause:** fix 1 ends the routine before Altered's give-back step (CE71 2124-2168 returns V[5000+k] to item k). The retried battle's start (CE77) capped the already-capped inventory and overwrote the stored 4 with 0.
- **Fix:** a verified copy of the give-back block runs in the retry branch before the jump.
- **Lesson:** every fix that skips code must list what that code did (here: a restore paired with a hold-back at battle start). Pairs must flip together.

### 4. Missing standard files (RTP)
- **Symptom:** "Image not found: Battle/打撃" during an Altered battle; muted smoke runs cannot hear missing sounds.
- **Cause:** Japanese data references RPG Maker's standard runtime files by Japanese names and expects them installed. The English 1.94 base shipped them under English names.
- **Fix:** build/scripts/s13_rtp.py maps names through EasyRPG's rtp_table and copies the files under the Japanese names (171 for Altered, 141 for JP).
- **Lesson:** grep every Player log for "not found" after every smoke; audio misses are silent in headless runs.

### 5. One page rewritten by both mods (the password door, Map0746 ev8 p1)
- **Symptom:** the English answer could never match: the comparison string and the name-input mode were Japanese.
- **Cause:** the English 1.94 base restructured the page (two name inputs, actor 13 holds the second half) and Altered also changed it (mode branches, name reset). Neither a string swap nor a whole-page copy was right.
- **Fix:** surgical port (build/scripts/s04c_map0746.py): Latin input mode in both branches, the 1.94 two-password block with test.13 strings replacing the DC-identical comparison block, Altered's CE75 call kept.
- **Lesson:** when a derived file (data/current.json) and the shipped game disagree, trust the game bytes; the review TSV for this map had rows shifted by one box.

### 6. Pre-existing DC bug: Retry after a lost fixed battle ignores input (DC English build)
- **Symptom:** the retry question appears but no Decision press is accepted; random-battle retry works.
- **Outcome (2026-10-23):** NOT REPRODUCED. 8 hidden runs on the shipped DC files (fixed battle entered through its map event, random battle, parties of 4 and of 1) all accepted Decision and restarted the battle; the decoded saves show only CE110/CE71 on the stack at the question. The two failing runs used a hand-edited test save and a debug teleport the game never performs. Treated as a test-setup artifact. work/bugfix-dc-retry-20261024/ROOTCAUSE.md; challenger_dc_retry.py is now a release gate for the DC builds.
- **Lesson:** a failure seen only from a hand-edited save is not a bug until it reproduces from a game-made state; record every save edit in the evidence folder.

### 7. Translation records that did not exist as a type
- **Symptom:** 513 Japanese strings remained after all message boxes were English: party names reset at runtime to katakana, UI fragments spliced into boxes through actor names, and comparisons against Japanese names.
- **Cause:** Altered uses "Change Actor Name" (10610) as a string table; no translation pipeline covered it.
- **Fix:** c2/actor-names.json + build/scripts/s04b_actor_names.py; the 4 name comparisons changed in the same step.
- **Lesson:** inventory every command type that carries text (10110/20110 boxes, 10140 choices, 10610 names, 12010 string compares, database fields, pictures) before declaring a build "all English".

### 8. Choice strings with "/" inside an option
- **Symptom:** the loader splits choice text on "/", so a page counter "x/y" inside an option produced one surplus piece.
- **Fix:** convention: real options first in branch order, one empty surplus record, counter written "x of y"; the verifier reads the option strings the Player shows, not the header.

### 9. Picture text has no room (info boxes)
- **Symptom:** 33 translated info pictures needed a 5th row; the list below the box starts at the next pixel row.
- **Fix:** measured in-game screenshots first (pictures/measure/evidence), then exact rewording (never cut meaning), then tracking -1 px on rows that still did not fit (pictures/RENDER-REPORT.md "play-test: tracking -1").
- **Lesson:** measure the real window before growing a picture; the owner rule is "add space or reword exactly, never shorten".

### 10. Two mods, one menu slot
- **Symptom:** both mods want the BREAK slot of the game menu (our MOD button, Altered's save-from-menu).
- **Fix:** slot 9 opens the MOD screen when Altered's save method is TREE, and a Save / MOD / Break choice when it is MENU. MOD pictures moved to ids 51-78 because Altered uses 1-50; MOD dialogs carry their own backdrop copy (78); Cancel waits for key release because Altered's menu loop reacts to held keys.

## How to add a feature safely (the order that worked)

1. Write the exact anchor (command code + parameters) for every insertion; the build must refuse on a mismatch, never guess.
2. For every id you allocate: literal search, pointer-base scan, then a runtime test that exercises the code that owns neighbouring ids.
3. For every block you skip or end early: list what it did; restore pairs.
4. Rebuild from the original files with the script chain (build/RUN.md), never by hand-editing the output.
5. Headless challenger before every upload: lose/retry/win in each mode, item counts and settings compared across saves, logs grepped for "not found".
6. Keep the owner's play-test list in CANDIDATE.md for what scripts cannot judge (feel, balance, scenes).

## Pointers

- Build chain and logs: work/altered-incorporation-20261023/build/ (RUN.md, CANDIDATE.md, scripts/, data/).
- MOD id tables per base: tools/mod_build.py PROFILE; anchors: build/data/mod-anchors-altered.json.
- Release tooling and challengers: work/release-v0.2.0-20261023/, work/release-v0.2.1-20261023/.
- Verdicts: work/altered-incorporation-20261023/AUDIT-VERDICT.html, many/MANY-VERDICT.html.
