# Linux — choose how to play

## Latest features through Steam / Proton

1. [Download the complete English game](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.2.0/seraphic-blue-fullgame-EN-v0.2.0.zip) and extract it into your home folder.
2. In Steam choose **Games → Add a Non-Steam Game → Browse**. Select **Player.exe** inside **SeraphicBlue**.
3. Open the shortcut's **Properties → Compatibility**. Enable **Force the use of a specific Steam Play compatibility tool** and choose **Proton Experimental**.
4. In **Shortcut**, set **Start In** to the extracted **SeraphicBlue** folder. Set **Launch Options** to the following. Press Play.

```text
--project-path . --save-path saves --config-path config --encoding 932 --window
```

Keep quotes around your actual folder path in Steam's Target / Start In fields if it contains spaces. The launch options above use the selected Start In folder; do not insert the Player.exe filename into those options. Saves go in **SeraphicBlue/saves**.

This uses the latest Windows Player through Proton. Proton/Linux execution was not tested on this machine.

## Native Linux alternative

The same ZIP includes the previously tested **Ubuntu 22.04-compatible x86-64 test.2 Player** and its bundled libraries. It needs a compatible Linux system; it is not a new universal Linux build.

1. Open a terminal in the extracted **SeraphicBlue** folder.
2. Run **sh play-linux.sh**.

This route uses older engine controls. New menu/target hover, character tabs and click-to-walk require the Proton route above. Keep backups before moving saves between runtimes; broad cross-runtime save compatibility is not claimed.

[Controls and screenshots](README.md#controls) · [Original native Linux build/source information](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.1.0-test.2).
