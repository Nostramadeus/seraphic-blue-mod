#!/bin/sh
set -u
cd -- "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)" || exit 1
if [ "$#" -eq 0 ] && [ -f .sb-startup-updates/startup_update.py ] && command -v python3 >/dev/null 2>&1; then
    code=0
    python3 .sb-startup-updates/startup_update.py --game-folder "$PWD" || code=$?
    [ "$code" -ne 10 ] || exit 0
fi
exec sh "$PWD/play-linux.pre-startup.sh" "$@"
