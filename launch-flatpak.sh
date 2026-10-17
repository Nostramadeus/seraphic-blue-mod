#!/bin/sh
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
game=${1:-"$here/game"}
if [ ! -f "$game/RPG_RT.ldb" ]; then
    printf '%s
' 'Patched game not found. Read STEAM-DECK-FLATPAK-TEST.html first.' >&2
    exit 1
fi
exec flatpak run org.easyrpg.player --project-path "$game" --save-path "$game"
