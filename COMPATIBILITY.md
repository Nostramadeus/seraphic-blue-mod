# Compatibility and tested limits

## Tested builds

Windows x86-64: exact custom Player SHA256 810c2fab79c135248c0c49045dd6977b97a2132bbb67f46c2f0cbe2a6ce27716, with 42 matching MSYS2 DLLs. Automated checks include 41 logical input replays, 145 message-frame comparisons and MOD structural checks. Japanese smoke adds 4 input cases, pause controls, settings save/reload and visually checked Japanese MOD text.

Native Linux: dynamically linked Ubuntu 22.04 x86-64 build, Player SHA256 9d6f96860abb71ed06d0101e68d070712c86ab51116c1c738c986cd41a8bd8b0, only liblcf bundled. Headless input/animation smoke and independent relative-library lookup passed. System-library requirements include fmt 8, ICU 70 and the SDL/audio libraries listed in its dependency file. Desktop/audio/Steam Deck and full Linux message-frame parity were not tested.

## Steam Deck and other platforms

The Steam Deck Proton TEST package contains the same Windows Player/DLLs plus setup suggestions. No hardware or Proton version was tested. It is not Valve Verified and is not a native controller-support claim. Stock Flatpak/EmuDeck lacks these custom additions. No custom Android, ARM or macOS build is provided.

## Known limits

Physical battle clicking and the full native item-Back path still need real-device testing. Logical replay tests are not physical-input proof. Hit testing covers ability/item list rows, not target sprites or every picture menu. Ordinary field save persistence passed; debug-saving during a waiting battle-input prompt has an existing 8-bit variable serialization limitation. No full-game playthrough, universal save compatibility, autosave, new palette or completed walkthrough/font overhaul is claimed.

## Report privacy

Issues and attachments are public. Report release/language/platform/Player or Proton version, steps, expected/actual result and MOD settings. Share only sanitized minimal excerpts; redact private paths, usernames, contact/location details. Keep raw logs private. Never upload the full game or arbitrary saves by default.
