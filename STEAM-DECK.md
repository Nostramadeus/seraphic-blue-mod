# Steam Deck — latest MOD through Proton

## Install once

1. Switch to **Desktop Mode**. [Download the complete English game](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-fullgame-EN-v0.1.0-test.6.zip) and extract it into your home folder, such as Documents.
2. Open Steam → **Games → Add a Non-Steam Game → Browse**. Select **Player.exe** inside the extracted **SeraphicBlue** folder. Change the file filter to show all files if needed.
3. Open that shortcut's **Properties → Compatibility**. Enable **Force the use of a specific Steam Play compatibility tool** and select **Proton Experimental**.
4. In **Shortcut**, set **Start In** to the extracted **SeraphicBlue** folder and set **Launch Options** to the line below. Return to Gaming Mode and start the shortcut.

```text
--project-path . --save-path saves --config-path config --encoding 932 --window
```

Keep the quotes Steam uses around folder paths. Saves go in **SeraphicBlue/saves**. Keep the extracted folder in the same place after creating the shortcut.

## Suggested Steam Input controls

| Control | Bind to |
| --- | --- |
| D-pad | Keyboard arrow keys |
| A / B / X | Enter / Escape / Shift |
| Right trackpad / trackpad click | Mouse / left mouse button |
| Left trigger | Right mouse button |
| Optional LB / RB | Page Up / Page Down for character tabs |

These are suggested bindings. Physical Deck/Proton operation has not been tested here. The game keeps keyboard controls alongside mouse controls.

## Updating

Back up **saves**. For this runtime-only update, replace only Player.exe and its matching DLLs from the Windows Player update ZIP; keep the same folder, shortcut, game data and EasyRPG.ini.

## Other routes

The included [native Linux alternative](LINUX.md#native-linux-alternative) has older test.2 controls. The separate [stock Flatpak package](STEAM-DECK-FLATPAK-TEST.md) contains still older test.1 game data; it does not provide the latest custom mouse features. Use the Proton route above for the newest features.

[Return to the quick start and screenshots](README.md).
