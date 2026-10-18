# Seraphic Blue MOD

[Download Windows Player](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-windows-x86_64-v0.1.0-test.6.zip) · [Steam Deck TEST](https://github.com/Nostramadeus/seraphic-blue-mod/releases/download/v0.1.0-test.6/seraphic-blue-player-steamdeck-proton-TEST-v0.1.0-test.6.zip) · [All downloads](https://github.com/Nostramadeus/seraphic-blue-mod/releases/tag/v0.1.0-test.6)

Optional mouse controls and convenience features for Seraphic Blue. **Test release: v0.1.0-test.6.**

## Start here — already playing this MOD?

```text
Close game → Back up saves → Update Player → Use your usual launcher
```

1. Close the game. Back up your actual save folder: the folder containing **Save*.lsd**. A launcher's **--save-path** tells you where it is.
2. Download the **Windows Player** above. Extract it into a **new runtime folder**; keep Player.exe and all 42 DLLs together.
3. Point your existing launcher at that new Player.exe. Keep its game, save and config paths unchanged. Launch and check that your saves appear.

**This update contains no game maps, database or saves.** Keep your game folder and EasyRPG.ini. If Player.exe already lives inside your game folder, you can instead replace **only Player.exe and its 42 DLLs** after backing up; leave everything else alone.

## First time installing?

```text
Your original game → Matching EN / JP game patch → Latest Player → Play
```

1. Start with the supported original English or Japanese Director's Cut game. This download is a MOD and Player, not the complete game.
2. Use the [first-install guide](INSTALL.md#fresh-game-installation-or-older-test1-game) to apply the matching game patch into a new folder.
3. Install the latest Windows Player using the steps above. [Steam Deck setup](STEAM-DECK-PROTON-TEST.md) is a separate TEST route.

## What's new? Try these four things

| You do this | You see this |
| --- | --- |
| Hover a menu row, enemy, or ally | Its highlight and information update immediately. Click to confirm. |
| Scroll while choosing battle magic/items | The next/previous page appears. **< 1/3 >** shows how many pages exist; its arrows also click. |
| Open Status, Gear, or Ability | Tabs at the top switch screens while keeping the same character. Page Up/Down works too. |
| Click the ground or an NPC's feet | Your character routes there. White marks the hovered tile; green marks an accepted destination until arrival. |

Deeper item, equipment, Supplement, Organize, Upgrade, shop and dictionary menus also gain mouse controls. Gear and battle screens show useful **Shift** hints. Shops show quantity buttons. Existing MOD settings remain available.

## Controls at a glance

| Action | Mouse | Keyboard |
| --- | --- | --- |
| Select / confirm | Hover / left click | Arrows / Enter |
| Back or cancel walking | Right click | Escape; arrows cancel walking |
| Change battle list page | Wheel or page arrows | Left / Right |
| Switch Status / Gear / Ability | Top tabs | Page Up / Page Down |
| Secondary action | Use the displayed hint | Shift |

In the game's **EasyRPG.ini**, keep these keys under its existing **[SB]** section. Change existing values; do not add duplicate sections.

```ini
[SB]
BattleUI=1
BattleMouse=1
MouseDecide=1
ClickWalk=1
```

Hover never spends an item, purchase, upgrade or attack. A stationary pointer leaves keyboard selection alone. Native number-entry and name-entry keep their existing controls. Reserve characters cannot use the Ability tab.

## Need more detail?

- [Install, save backup and rollback](INSTALL.md)
- [Full release notes](RELEASE-NOTES.md)
- [Steam Deck TEST setup](STEAM-DECK-PROTON-TEST.md) — hardware not verified; keyboard controls retained.
- [Test coverage and limits](COMPATIBILITY.md) — no full-playthrough claim; native Linux remains test.2.
- [Credits](CREDITS.md), [licenses](LICENSES.md) and [corresponding source](SOURCE-ACCESS.md).
