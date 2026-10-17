# Steam Deck Proton TEST guide

Hardware-unverified test release. No Steam Deck, Proton version, native controller layout or Deck audio was tested here. This package reuses the exact tested Windows Player and all 42 DLLs; it does not include Proton or the game. It is not Valve Verified.

## 1. Patch on Windows first

Download the EN or JP patch matching your exact original edition. Keep the original and a save backup. Extract the patch separately and run its Python 3.10+ installer with --base pointing to your game and --out pointing to a NEW folder. Existing source/save files stay untouched. Python is needed for patching, not normal play. Do not run the original RPG_RT.exe for this fork's features.

## 2. Transfer your own game

Copy your own patched game folder to Deck using your chosen file-transfer method. Extract the CONTENTS of this Player package beside RPG_RT.ldb in that folder: Player.exe, every DLL, licenses and guides stay together. Do not replace EasyRPG.ini supplied by the patch. This is not a replacement game download.

## 3. Add the Windows executable to Steam

In Desktop Mode, choose Steam > Add a Non-Steam Game > Browse and select Player.exe (show All Files if needed). In its properties, set Start In to the containing game directory. Set launch options to this exact line:

--project-path .

Under Compatibility, enable a Steam-supplied Proton version. Record the selected version in any test report; no particular version is certified here. No root/pacman/read-only-filesystem changes are needed by this guide.

## 4. Suggested Steam Input bindings

These are suggestions, not a tested native gamepad layout.

- D-pad or left stick: keyboard arrow keys.
- A: Enter (Decide).
- B: Escape (Back).
- X: Shift.
- Right trackpad: mouse; click sends left mouse button.
- Left trigger: right mouse button (Back).
- Optional right stick or two back buttons: mouse wheel up/down.

In battle, wheel up/down cycles MAIN commands left/right. In category and ability/item lists it moves vertically. Clicking a valid ability/item row selects that actual row before confirming. Empty, disabled and outside list clicks do nothing. Keyboard arrows/Enter/Escape remain available. Target-sprite clicking, other picture-menu hit tests and click-to-walk are not included.

## 5. Verify before relying on it

Start with backed-up saves. Check text advance, MOD tabs/settings, row 3 selection from row 1, page 2 selection, wheel direction, Back from an item menu, saving/reloading and sound at your chosen volume. Physical battle input and full native item-Back were not proven by the automated logical-replay tests. Do not make debug saves during a waiting battle-input prompt; that existing input-variable format has an 8-bit limitation.

## 6. Troubleshooting and rollback

Keep every DLL beside Player.exe. Confirm Start In and --project-path . point to the patched game. Keep EasyRPG.ini from the patch. A stock EasyRPG/Flatpak/EmuDeck build does not automatically include this fork's mouse/pause/animation changes. The Ubuntu 22.04 native package is separate and is NOT a portable Deck package. Roll back to your untouched backup; do not overwrite the original while troubleshooting.

## 7. Report a problem safely

GitHub issues and attachments are PUBLIC. Include release version, EN/JP, platform, selected Proton version, exact steps, expected/actual behavior and relevant MOD settings. Sanitize minimal screenshots/log excerpts: redact private paths, usernames, contact details and location. Keep raw debug logs private. Do not upload full game folders or arbitrary saves; saves can contain personal names and story progress. A maintainer can request a sanitized minimal example if necessary.

## Official references

Valve explains Proton and Steam Deck support; those general references are not a test result for this fork.
https://partner.steamgames.com/doc/steamhardware/steamdeck/faq
https://partner.steamgames.com/doc/steamhardware/proton
https://github.com/ValveSoftware/Proton
Stock EasyRPG downloads (not this custom fork): https://easyrpg.org/player/downloads/
