# Install or update v0.3.8

## Fresh installation

1. Pick the full-game ZIP in the [download table](README.md#downloads). Use EN + MOD + Altered for a new Altered game, EN + MOD (DC) for existing Director's Cut saves, or JP + MOD (DC) for Japanese.
2. Extract the ZIP into a new folder. No original game, patch command or runtime download is needed.
3. On Windows open **PLAY.cmd** inside **SeraphicBlue** or **SeraphicBlue-Altered**. On Linux run **sh play-linux.sh** from that folder.

Keep Player.exe, its DLLs, **native-linux**, game data and launchers together. [Windows](WINDOWS.md) · [Linux](LINUX.md) · [Steam Deck](STEAM-DECK.md).

## GUI updater and optional startup checks

1. Close the game. Download the [Windows updater v1.1](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.7/seraphic-blue-updater-windows-v1.1.0.zip) or [Linux startup updater](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.7/seraphic-blue-updater-linux-v1.1.0.zip), then extract the complete folder.
2. On Windows, open **SeraphicBlue-Update.exe**, click **Choose...**, and select the old game folder containing **PLAY.cmd**. Click **Update to latest** when you want to update now.
3. For checks when starting the game, click **Enable startup checks**. On Linux, open **Startup-settings.desktop**, choose the game folder, and select **Enable**. Linux needs Python 3 and zenity or kdialog.
4. Start through **PLAY.cmd** on Windows or **play-linux.sh** on Linux. A newer matching stable release offers **Install update** or **Play current**. Checks are optional; the setup can disable them and restore the original launcher.

The updater checks free space before download and extraction. It creates a neighboring version folder, verifies downloaded files and copied saves/settings, and keeps the old copy plus a separate backup. It preserves the new **EasyRPG.ini**. Already current? It does not reinstall. Offline checks and check errors fall back to the current game.

Keep the complete extracted updater folder together. Direct **Player.exe** or **native-linux/Player** shortcuts bypass startup checks. Steam shortcuts are not rewritten automatically; point them to the desired version folder's launcher if you want startup checks. Native Linux helper checks passed; physical Steam Deck, Proton setup and real Linux desktop dialogs have not been verified. Existing working Proton shortcuts can stay as they are.

Supported: stable full-game releases with an intact **fullgame-manifest.json** and standard launcher paths. Historical patch-only copies, modified databases and custom save paths use the manual steps below. DC and Altered saves stay on their own editions. Use v1.1 instead of the older updater v1.0; v1.1 also corrects destination-folder handling. [Instructions and source](updater-v1.1/README.md).

## Update and keep saves

1. Close the game. Back up the old **saves** and **config** folders.
2. Extract the new full-game ZIP into a new folder.
3. Copy **saves** and **config** from the old installation to the new one. Keep the new release's **EasyRPG.ini**. If an older installation stored **SaveXX.lsd** directly in its game folder, copy those files into the new **saves** folder.
4. Start the new installation and load your usual save before removing the old one.

The old launcher's **--save-path** decides where its saves are stored. If it used a custom folder, copy from that folder. Do not guess from the game directory alone.

DC saves from previous MOD builds, the 2016 English patch and the Japanese original stay on a DC build. Altered saves from v0.2.0 onward stay on the Altered build. **DC saves do not move into Altered.** No general cross-edition or arbitrary mid-event debug-save guarantee is made. [Keep your saves](README.md#keep-your-saves).

## Existing patch installations

Older test.2 patch commands are historical. Use a new current full-game folder and copy your saves as above; do not apply that old patch over current game data. The [test.2 installation guide](https://github.com/Nostramadeus/seraphic-blue-mod/blob/v0.1.0-test.2/INSTALL.md) remains available for those archived downloads.

## Controls and limits

Arrows move and select. Enter confirms. Escape or right-click goes back. Hover highlights supported menu entries; left-click chooses. [Controls](README.md#controls).

The English DC manual is mostly the 2016 English translation; four pages remain Japanese and two are mixed. Altered's manual and update history are Japanese. Some status labels keep an English word with a Japanese gloss; character reading captions, original artist-name credits and small background/sprite lettering remain as retained artwork. These exceptions are documented; this is not a claim that every image and manual page is English.

[Compatibility and tested limits](COMPATIBILITY.md). Keep the old game and verified save backup for rollback.

Saved Auto commands: copy sb-repeat-a.json and sb-repeat-b.json too if they are beside Player.exe. The GUI updater v1.1 preserves them automatically. Files inside saves are included when you copy that folder.
