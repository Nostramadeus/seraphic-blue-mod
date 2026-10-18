# Compatibility — test.5

## Enemy hover selection

With BattleUI=1, BattleMouse=1 and MouseDecide=1 in the existing [SB] section of EasyRPG.ini, move the pointer over a visible enemy sprite to select it. The enemy name, target icon and cursor follow the selected enemy. Hover selects only; click to confirm the action once.

Moving over empty background, transparent sprite pixels, hidden, missing or defeated enemies leaves the choice alone. A stationary pointer leaves keyboard and wheel selection alone, and held direction keys take priority. Hover preserves optional and forced all-target selection; an explicit enemy click can return optional all-target selection to one enemy.

This is a runtime-only update. Close the game, back up your actual save folder, and extract the Windows Player ZIP into a NEW runtime folder. Keep Player.exe and all 42 DLLs together. Point your existing launcher to the new Player.exe while retaining its --project-path, --save-path and --config-path values. Preserve EasyRPG.ini, game data and saves. The detailed safe-update instructions below still apply.

Windows production incremental build passed. Native input replay checks passed14 EN cases plus3 focused JP cases. Real native target name, icon transparency and coordinates were checked from save records; original-asset EN/JP screenshots were inspected. Prior test.4 missing-hover behavior was reproduced on the same fixture. Motion selects without attacking, stationary pointers and held navigation preserve manual choices, optional/forced all-target choices remain intact, ineligible sprites are ignored, and held click confirms once. No physical mouse, full-playthrough or Steam Deck hardware verification is claimed.

Player SHA256 abcc5acdf083c379d35013fb3aed5e5c9f3ecad0aca742c17c70ba01e8271ee2.

Windows x86-64 native input replays are the acceptance checks. Physical mouse, Steam Deck/Proton hardware, full playthrough and universal save compatibility remain unverified. Native Linux stays at test.2; Flatpak addon stays on older test.1 game data with stock runtime.
