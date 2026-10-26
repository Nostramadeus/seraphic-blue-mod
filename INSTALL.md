# Install or update v0.3.7

## Fresh installation

1. Pick the full-game ZIP in the [download table](README.md#downloads). Use EN + MOD + Altered for a new Altered game, EN + MOD (DC) for existing Director's Cut saves, or JP + MOD (DC) for Japanese.
2. Extract the ZIP into a new folder. No original game, patch command or runtime download is needed.
3. On Windows open **PLAY.cmd** inside **SeraphicBlue** or **SeraphicBlue-Altered**. On Linux run **sh play-linux.sh** from that folder.

Keep Player.exe, its DLLs, **native-linux**, game data and launchers together. [Windows](WINDOWS.md) · [Linux](LINUX.md) · [Steam Deck](STEAM-DECK.md).

## Windows GUI updater

1. Close the game. [Download the updater](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.3.7/seraphic-blue-updater-windows-v1.0.0.zip) and extract it into its own folder.
2. Open **SeraphicBlue-Update.exe**. Click **Choose...** and select the old game folder containing **PLAY.cmd**.
3. Click **Update to latest**. After the checksum, extracted files and copied saves/settings are verified, click **Play updated copy**.

The old game stays in place. The updater keeps a separate verified save/settings backup, creates a new same-edition folder and preserves its new **EasyRPG.ini**. Keep **Update.ps1** beside the updater program. No Python installation is needed. Already on the latest version? It says so without reinstalling.

This supports stable full-game releases with an intact **fullgame-manifest.json** and the standard launcher paths. Historical patch-only copies, modified databases, custom save locations, Linux and Steam Deck use the manual steps below. [Updater details and source](updater/README.md).

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
