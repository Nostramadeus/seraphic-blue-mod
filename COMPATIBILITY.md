# Compatibility — test.4

## Updating an existing Windows installation safely

1. Close the game. Copy your actual save folder somewhere safe. Saves are Save*.lsd files; keep Save*.sav files too if present. If your shortcut or .cmd launcher includes --save-path, use that folder. Otherwise check the game folder. Do not guess from the Player download folder.
2. Download the Windows Player ZIP for test.4 and extract it into a NEW runtime folder. It contains Player.exe and its 42 DLLs; it contains no game database, maps or saves. Keep the old runtime for rollback.
3. Point your existing shortcut/launcher at the new Player.exe. Keep its --project-path, --save-path and --config-path values exactly as they were. If your installation keeps Player.exe inside the game folder, you may instead copy ONLY Player.exe and the 42 matching DLLs there after closing the game; leave every other file alone.
4. Keep your current EasyRPG.ini. Under its existing [SB] section, BattleUI=1, BattleMouse=1 and MouseDecide=1 enable these controls. Do not replace the whole INI or duplicate keys. Launch and check that your usual saves appear before continuing.

This runtime update does not overwrite or migrate saves. A backup still protects against selecting the wrong folder or later saving over a slot. Do not reapply the test.1-to-test.2 game updater to an already updated game. Future releases that change game data may need different instructions: read that release's install guide instead of copying every ZIP over the game.

## Enemy targets and battle list pages

Click a visible enemy sprite to select and confirm it for a single-target attack. Empty background, transparent sprite pixels, missing and defeated enemies do not confirm. Clicking an enemy switches an optional all-target selection back to that enemy; forced all-target abilities keep targeting everyone. Keyboard targeting and wheel target cycling remain available.

While choosing a battle ability or item, scroll down for the next page and up for the previous page. All magic categories and battle item lists use this same paging route. Move the pointer to highlight a row; click it to choose it. Multi-page lists show < current/total > above the list, with clickable previous/next arrows. Paging wraps at the ends, matching keyboard Left/Right. Single-page lists stay on their page. Other menus retain their existing controls.

Windows production build passed. Native replays passed 17 enemy-target/regression checks before paging integration; the final build passed 12 ability/item paging checks and 3 EN/JP targeting/paging rechecks. The prior test.3 enemy-click failure was reproduced on the same fixture. Page-counter screenshots were inspected. No full-playthrough or physical Steam Deck verification is claimed.

Player SHA256 fcefa37cefa9269b032ec395e49528d163db5233086293e89f3c63c6bbc36f5a.

Windows x86-64 tested with native input replays. Steam Deck/Proton hardware, full playthrough and universal save compatibility remain unverified. Native Linux stays at test.2; Flatpak addon stays on older test.1 game data with stock runtime.
