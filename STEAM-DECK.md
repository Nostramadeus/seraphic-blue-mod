# Steam Deck — two launch options

The ZIP includes native Linux and Windows Players from the same **0.8.1.1-sb7** source, with consistent menu hover and the existing custom controls. One controlled headless Debian 11 shop comparison/Cancel replay passed, including numerical values and unchanged native state. The final native build retains that path across two source-bound DC copy-range corrections verified on Windows; no second Linux replay is claimed. Physical Steam Deck hardware and Proton were not tested here.

Earlier v0.3.3 sb5 container tests covered Debian 11, Arch and Ubuntu 24.04: 36 cases and 18 matching save states, nine exact normal-speed images, plus 111 controlled timeline/save-name images and 36 states. Earlier MIDI and launcher checks are retained for their unchanged components; they are not another test pass for sb7. No physical display/audio-device verification is claimed.

## Native Linux

1. Switch to **Desktop Mode**. [Download the complete English game](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.6/seraphic-blue-fullgame-EN-v0.3.6.zip) and extract it.
2. Open a terminal in **SeraphicBlue** (or **SeraphicBlue-Altered** for the Altered ZIP). Run **sh play-linux.sh**.
3. To launch through Steam, make **play-linux.sh** and **native-linux/Player** executable: **chmod +x play-linux.sh native-linux/Player**.
4. In Steam choose **Games → Add a Non-Steam Game → Browse**, show all files, and select **play-linux.sh**. Set **Start In** to the game folder. Leave forced Proton compatibility off for this native shortcut.

Keep the extracted files together. Native MIDI uses an available soundfont or the included FM synthesizer; the FM instruments may sound different. [Linux requirements and test limits](LINUX.md#native-linux-player).

## Windows Player through Proton

1. Add **Player.exe** from the same game folder as a Non-Steam Game.
2. Open **Properties → Compatibility**, enable the forced compatibility tool, and select **Proton Experimental**.
3. In **Shortcut**, set **Start In** to the game folder and **Launch Options** to:

```text
--project-path . --save-path saves --config-path config --encoding 932 --window
```

v0.3.3 includes AryaNetwork's PortAudio library fix for the title-screen MIDI crash ([issue #1](https://github.com/Nostramadeus/seraphic-blue-mod/issues/1)). Windows regression tests passed; we did not run the patched build on physical Deck hardware or Proton.

## Suggested Steam Input controls

| Control | Bind to |
| --- | --- |
| D-pad | Keyboard arrow keys |
| A / B / X | Enter / Escape / Shift |
| Right trackpad / trackpad click | Mouse / left mouse button |
| Left trigger | Right mouse button |
| Optional LB / RB | Page Up / Page Down for character tabs |

These are suggested bindings. The game keeps keyboard controls alongside mouse controls.

## Updating

Close the game. Back up **saves** and **config**. Extract the new ZIP into a new folder and copy those folders from the old installation. Point the Steam shortcut at the new launcher or Player.exe. Keep DC and Altered saves on their matching builds. [Keep your saves](README.md#keep-your-saves).

The separate [stock Flatpak package](STEAM-DECK-FLATPAK-TEST.md) contains older test.1 game data and does not supply the current custom Player. [Quick start](README.md).
