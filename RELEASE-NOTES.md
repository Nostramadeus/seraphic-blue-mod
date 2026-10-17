# Seraphic Blue MOD v0.1.0-test.2 — TEST

Direct category clicks, motion-only native highlights, enemy-target wheel selection and persistent short action-time names. Duplicate names use fixed-slot numbers. Matching test.1 updates now back up and migrate the explicitly selected save set into a new copy.

## Controls in test.2

- Click a battle category to select and enter it. Move the pointer to highlight native categories and ability/item rows. A stationary pointer leaves keyboard selection alone.
- Disabled rows may highlight, but clicking does not confirm them. Empty and outside row clicks do nothing.
- Wheel up/down cycles main commands left/right and category/ability lists vertically. During enemy selection it uses native Left/Right to cycle eligible living targets. Physical Up/Down retains the all-target toggle. Detailed data pages still use Decide/Back.
- Action-time labels show short actor/enemy names without hover. Only duplicates get numbers, ranked by occupied slots even while a marker is hidden. Native target opacity is retained.
- Left click advances text; right click is Back. Keyboard arrows/Enter/Escape remain available. Hold F/G for the built-in configurable 3x/10x fast-forward defaults.
- Other picture menus keep their existing selected-command behavior. Target-sprite clicking and click-to-walk are not included. MOD settings and optional cheats remain available.

## Update from matching test.1 and keep saves

Make an ordinary Memory Tree save and close the game. Extract the matching EN or JP test.2 patch separately. Keep your untouched pristine base, supported same-edition test.1 game and actual save folder. The --saves folder must match the old launcher's --save-path; if it used the default, use the old game folder. Do not guess a custom save location.

Windows, from the extracted patch directory:
```sh
py -3 update_game.py --base "PRISTINE-BASE" --current "OLD-TEST1-GAME" --saves "ACTUAL-OLD-SAVE-FOLDER" --out "NEW-GAME-FOLDER" --backup "NEW-SAVE-BACKUP"
```

Linux, from the extracted patch directory (first chmod +x tools/linux-x86_64/xdelta3decode):
```sh
python3 update_game.py --base "PRISTINE-BASE" --current "OLD-TEST1-GAME" --saves "ACTUAL-OLD-SAVE-FOLDER" --out "NEW-GAME-FOLDER" --backup "NEW-SAVE-BACKUP"
```

The updater prints the selected save files/count, creates a verified backup, builds a separate new game and checks copied save bytes. New output and backup paths must not exist. It supports the exact matching test.1 database only; no arbitrary-version, cross-edition or mid-event debug-save compatibility is claimed. A failed/interrupted .partial folder is unusable; keep it separate and retry with fresh paths after resolving the cause. Keep the old game and verified backup.

Launch the NEW game with its NEW save folder, not the old custom path:
```sh
Player.exe --project-path "NEW-GAME-FOLDER" --save-path "NEW-GAME-FOLDER"
./Player --project-path "NEW-GAME-FOLDER" --save-path "NEW-GAME-FOLDER"
```

# Compatibility and tested limits — test.2

Windows x86-64: Player SHA256 ae939308a7dbb08c1d70e4015e56df6ba0369cb796f6a22777abeddecca17d71, with the same 42 verified MSYS2 DLLs. New native replay checks: 53/53 EN input, 8/8 selected JP input, 9/9 EN timeline and 4/4 JP timeline. Both languages' native panel and label screenshots were visually reviewed. Timeline lifecycle checks cover hiding, erasure, revival, transformation, an initially empty slot becoming occupied, and ending art reusing a picture ID.

Retained test.1 evidence: 145 message-frame comparisons and prior MOD/field-save checks. Pause source is unchanged; no new pause sweep. The unchanged installer retains its 20-case adversarial result. The exact updater passed 18 independent real-xdelta cases, including changed sources and hard interruption. No real user saves were migrated in these tests.

Native Linux targets Ubuntu 22.04 x86-64, with only liblcf bundled. Player SHA256 a83eb60af4044b23f4210ff961de5804d1c74c4ccb6d04109734e258cb7bb800. Root built the accepted source and ran four headless replay/screenshot fixtures; relative liblcf loading was checked.

Steam Deck uses the identical Windows Player/DLLs through Proton in a hardware-unverified TEST package. No Deck hardware, Proton version or audio was tested. Ubuntu is not a universal Linux/Deck binary. Stock EasyRPG/Flatpak/EmuDeck lacks these custom changes.

Logical replays are not physical mouse proof. The owner's earlier Windy click was one positive physical case only. Full native item-Back, full playthrough and universal save compatibility remain unverified. Debug saves during a waiting battle-input prompt have an existing 8-bit variable limitation. No autosave, command palette or parked guide/font overhaul is included.

Issues and attachments are public. Share only sanitized minimal steps/screenshots; redact private paths, usernames, contact/location details. Keep raw logs private. Do not upload full games or arbitrary saves.

A separate full English game package for stock EasyRPG Flatpak is now available with older test.1 MOD data. Install EasyRPG from Discover, extract the package and choose its game folder. No Python, patching or Proton is needed for that package. Its event-based MOD menu is retained; custom engine pause/mouse/animation features and test.2 timeline labels are unavailable. Steam Deck hardware and Flatpak runtime are untested. Read STEAM-DECK-FLATPAK-TEST.html. Original game audio/manual/credits are included; separately added repair RTP sounds, user saves, original Windows executable and system fonts are excluded. The existing test.2 patch archives remain patch-only. Verify the addon ZIP against its separate .sha256 file; existing SHA256SUMS and release assets are unchanged.
