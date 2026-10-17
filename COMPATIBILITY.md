# Compatibility and tested limits — test.2

Windows x86-64: Player SHA256 ae939308a7dbb08c1d70e4015e56df6ba0369cb796f6a22777abeddecca17d71, with the same 42 verified MSYS2 DLLs. New native replay checks: 53/53 EN input, 8/8 selected JP input, 9/9 EN timeline and 4/4 JP timeline. Both languages' native panel and label screenshots were visually reviewed. Timeline lifecycle checks cover hiding, erasure, revival, transformation, an initially empty slot becoming occupied, and ending art reusing a picture ID.

Retained test.1 evidence: 145 message-frame comparisons and prior MOD/field-save checks. Pause source is unchanged; no new pause sweep. The unchanged installer retains its 20-case adversarial result. The exact updater passed 18 independent real-xdelta cases, including changed sources and hard interruption. No real user saves were migrated in these tests.

Native Linux targets Ubuntu 22.04 x86-64, with only liblcf bundled. Player SHA256 a83eb60af4044b23f4210ff961de5804d1c74c4ccb6d04109734e258cb7bb800. Root built the accepted source and ran four headless replay/screenshot fixtures; relative liblcf loading was checked.

Steam Deck uses the identical Windows Player/DLLs through Proton in a hardware-unverified TEST package. No Deck hardware, Proton version or audio was tested. Ubuntu is not a universal Linux/Deck binary. Stock EasyRPG/Flatpak/EmuDeck lacks these custom changes.

Logical replays are not physical mouse proof. The owner's earlier Windy click was one positive physical case only. Full native item-Back, full playthrough and universal save compatibility remain unverified. Debug saves during a waiting battle-input prompt have an existing 8-bit variable limitation. No autosave, command palette or parked guide/font overhaul is included.

Issues and attachments are public. Share only sanitized minimal steps/screenshots; redact private paths, usernames, contact/location details. Keep raw logs private. Do not upload full games or arbitrary saves.
