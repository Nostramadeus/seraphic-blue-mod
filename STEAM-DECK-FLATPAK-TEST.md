# Steam Deck stock Flatpak alternative — full EN game / test.1 MOD TEST

This download includes the English game with the published test.1 MOD data already applied, the original manual/credits and a launcher. Install EasyRPG Player separately from Discover. No patching, Python, original Windows executable or Proton is needed. Steam Deck hardware, Flatpak runtime, gamepad and audio are untested here.

## 1. Extract the game

Extract the entire ZIP into a new folder inside your Deck home folder, for example under Documents. Keep launch-flatpak.sh beside the included game folder. Leave existing game folders and saves alone. SD cards need separate Flatpak filesystem access; these steps use home storage. This is a fresh separate install, with no save migration. Do not copy test.2 saves backward into this older database.

## 2. Install EasyRPG Player

Enter Desktop Mode. Open Discover, search EasyRPG Player and install the Flathub app org.easyrpg.player.

## 3. Add EasyRPG to Steam

In Desktop Steam choose Games > Add a Non-Steam Game and select EasyRPG Player. Open that shortcut's Properties. Preserve all existing Launch Options and append a space followed by --first-start for the first launch. Do not replace the existing Flatpak arguments. Start the shortcut, then use EasyRPG's setup wizard to select the extracted game folder containing RPG_RT.ldb. After setup remove only the --first-start argument you added. Return to Gaming Mode and start EasyRPG Player, then select the game if shown. Do not enable Proton for this Linux Flatpak.

To bypass the game browser, preserve Steam's existing Flatpak Launch Options and append --project-path "FULL-PATH-TO-GAME" --save-path "FULL-PATH-TO-GAME". Replace both placeholders with the actual extracted game folder and keep the quotes.

Optional Desktop launch from Konsole, inside the extracted addon folder:

```sh
sh launch-flatpak.sh
```

The script also accepts a game folder as its first argument. It explicitly saves beside RPG_RT.ldb. The official Flatpak manifest currently permits home-folder access.

## 4. Controls and MOD options

Suggested Steam Input bindings: D-pad to keyboard arrows, A to Enter, B to Escape and X to Shift. This is not a verified Deck layout. Open the ordinary field menu with Escape and choose MOD. Use arrows, Enter and Escape inside MOD. Existing event-based movement, encounters/rewards, scripted waits, HP/TP refill and optional cheats remain in the test.1 data. Defaults keep the original behavior.

Stock EasyRPG does not include our custom text-pause skipping, battle mouse/wheel input, animation-speed hook or test.2 timeline labels. The Animation setting may still appear in MOD but its custom engine effect is unavailable. Use keyboard bindings for menus. Stock EasyRPG's own fast-forward depends on your Player settings.

## 5. Saves, limits and credits

This package uses test.1 game data; the test.2 custom Player route is separate. No new runtime/Deck test was run. Keep backups and verify an ordinary Memory Tree save/reload before relying on it. Original game content is by Tempura (Sakaki), English translation by eplipswich, proofreading by kumada. Original manual and credits are retained under game. Game, translation and derived materials retain their rights; MIT covers only our authored launcher/docs. No endorsement or blanket new redistribution permission is implied. Separately sourced repair RTP sounds, system fonts, original Windows executable and user saves/config/logs are excluded. Audio originally present in the supported game is retained.

## Official setup references

- [EasyRPG Flatpak announcement and first-start wizard](https://blog.easyrpg.org/2024/12/easyrpg-player-flatpak-available/)
- [Official Flathub manifest and filesystem permissions](https://github.com/flathub/org.easyrpg.player/blob/master/org.easyrpg.player.yml)
- [EasyRPG Player on Flathub](https://flathub.org/apps/org.easyrpg.player)
