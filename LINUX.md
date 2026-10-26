# Linux — download and play

## Native Linux Player

1. [Download the complete English game](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.7/seraphic-blue-fullgame-EN-v0.3.7.zip) and extract it.
2. Open a terminal in the extracted **SeraphicBlue** folder.
3. Run **sh play-linux.sh**.

The Altered ZIP uses **SeraphicBlue-Altered** instead. The launcher selects its own game folder even when the path contains spaces. Saves go in **saves** and Player settings in **config**, inside that folder. If extraction removed executable permissions, run **chmod +x native-linux/Player** and try again.

The native x86-64 Player is **0.8.1.1-sb7**, from the same Player source as Windows. It includes the custom mouse controls, click-to-walk, message history, Text speed and Text pauses. Its helper libraries are in **native-linux/lib**; keep that folder with Player.

Built on Debian 11. Required symbol versions include **GLIBC_2.29**, **GLIBCXX_3.4.26** and **CXXABI_1.3.9**, plus the system's display/audio drivers and zlib. These requirements alone do not prove compatibility with every Linux distribution. The earlier sb6 build passed one controlled headless hover/click/keyboard replay on Debian 11. One controlled headless Debian 11 shop comparison/Cancel replay passed, including numerical values and unchanged native state. The final native build retains that path across two source-bound DC copy-range corrections verified on Windows; no second Linux replay is claimed. Earlier v0.3.3 sb5 tests passed 36 replay cases on Debian 11, Arch and Ubuntu 24.04 containers. All 18 generated save states matched Windows. A separate normal-speed replay matched Windows on all three systems (nine images). Timeline and save-name checks also matched all 111 images and 36 generated save states. MIDI produced nonzero audio through a virtual disk driver. Launcher paths with spaces and save/config storage passed. Physical Steam Deck, Proton and desktop display/audio drivers remain untested.

MIDI uses FluidLite when a compatible soundfont is available, otherwise the included FM synthesizer. No soundfont download is required to start playing. The two synthesizers sound different. Physical desktop audio and Steam Deck hardware were not tested here.

## Steam / Proton alternative

1. In Steam choose **Games → Add a Non-Steam Game → Browse**. Select **Player.exe** in the extracted game folder.
2. Open **Properties → Compatibility**. Enable **Force the use of a specific Steam Play compatibility tool** and choose **Proton Experimental**.
3. In **Shortcut**, set **Start In** to that game folder. Leave **Launch Options** blank, then press Play.

The earlier custom launch options could prevent a fresh copy from starting because **--save-path saves** requires that folder to exist. A direct **Player.exe** shortcut skips the launcher that creates it. Default saves may be **SaveNN.lsd** files beside **Player.exe**. Keep an existing working shortcut unchanged; adding a custom save path can hide saves in the old location.

Keep quotes around folder paths in Steam's Target / Start In fields if they contain spaces. The v0.3.3 Windows libraries include AryaNetwork's fix for the title-screen MIDI crash reported in [issue #1](https://github.com/Nostramadeus/seraphic-blue-mod/issues/1). The patched library was checked on Windows; our tests did not run Proton.

## Updating

[Download the Linux startup updater](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.7/seraphic-blue-updater-linux-v1.1.0.zip) and extract the complete folder. Open **Startup-settings.desktop**, choose the game folder, and select **Enable**. Python 3 and zenity or kdialog are required. If your desktop asks whether to trust or allow this local launcher, inspect its source first. Start the game with **sh play-linux.sh**; a newer matching release offers **Install update** or **Play current**. Run the setup again to disable checks. [Instructions and source](updater-v1.1/README.md).

The updater checks free space and installs into a neighboring version folder. The old game and a verified save/settings backup stay in place. Direct Player shortcuts bypass checks; Steam shortcuts are not rewritten. Physical Steam Deck, Proton and real Linux desktop dialogs remain unverified.

For a manual update, close the game. Back up **saves**, **config**, and any root **SaveNN.lsd** files. Extract the new ZIP into a new folder, then copy your personal files from the old installation. Keep DC saves on a DC build and Altered saves on an Altered build. [Keep your saves](README.md#keep-your-saves).

[Controls](README.md#controls) · [Steam Deck setup](STEAM-DECK.md) · [Source and libraries](SOURCE-ACCESS.md)
