# Steam Deck Proton TEST guide

Hardware-unverified test release. No Steam Deck, Proton version, native controller layout or Deck audio was tested here. This package reuses the exact tested Windows Player and all 42 DLLs; it does not include Proton or the game. It is not Valve Verified.

## 1. Patch on Windows first

Download the EN or JP patch matching your exact original edition. Keep the original and a save backup. Extract the patch separately and run its Python 3.10+ installer with --base pointing to your game and --out pointing to a NEW folder. Existing source/save files stay untouched. Python is needed for patching, not normal play. Do not run the original RPG_RT.exe for this fork's features.

## 2. Transfer your own game

Copy your own patched game folder to Deck using your chosen file-transfer method. Extract the CONTENTS of this Player package beside RPG_RT.ldb in that folder: Player.exe, every DLL, licenses and guides stay together. Do not replace EasyRPG.ini supplied by the patch. This is not a replacement game download.

## 3. Add the Windows executable to Steam

In Desktop Mode, choose Steam > Add a Non-Steam Game > Browse and select Player.exe (show All Files if needed). In its properties, set Start In to the containing game directory. Set launch options to this exact line:

```sh
--project-path . --save-path .
```

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

## 5. Verify before relying on it

Start with backed-up saves. Check text advance, MOD tabs/settings, row 3 selection from row 1, page 2 selection, wheel direction, Back from an item menu, saving/reloading and sound at your chosen volume. Physical battle input and full native item-Back were not proven by the automated logical-replay tests. Do not make debug saves during a waiting battle-input prompt; that existing input-variable format has an 8-bit limitation.

## 6. Troubleshooting and rollback

Keep every DLL beside Player.exe. Confirm Start In and --project-path . --save-path . point to the patched game. Keep EasyRPG.ini from the patch. A stock EasyRPG/Flatpak/EmuDeck build does not automatically include this fork's mouse/pause/animation changes. The Ubuntu 22.04 native package is separate and is NOT a portable Deck package. Roll back to your untouched backup; do not overwrite the original while troubleshooting.

## 7. Report a problem safely

GitHub issues and attachments are PUBLIC. Include release version, EN/JP, platform, selected Proton version, exact steps, expected/actual behavior and relevant MOD settings. Sanitize minimal screenshots/log excerpts: redact private paths, usernames, contact details and location. Keep raw debug logs private. Do not upload full game folders or arbitrary saves; saves can contain personal names and story progress. A maintainer can request a sanitized minimal example if necessary.

## Official references

Valve explains Proton and Steam Deck support; those general references are not a test result for this fork.
https://partner.steamgames.com/doc/steamhardware/steamdeck/faq
https://partner.steamgames.com/doc/steamhardware/proton
https://github.com/ValveSoftware/Proton
Stock EasyRPG downloads (not this custom fork): https://easyrpg.org/player/downloads/
