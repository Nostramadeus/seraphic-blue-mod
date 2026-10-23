"""Write the README keycap and mouse icons as small SVG files.

    python make_keys.py [OUT_ROOT]

Writes OUT_ROOT/docs/img/keys/<name>.svg (OUT_ROOT defaults to the repository
root, three folders up from docs/img/tools/). Standard library only. Every icon comes from the same few drawing
functions, so the style stays uniform: a rounded keycap with a light top face,
a darker side strip at the bottom (the 3D look), a white highlight line along
the top of the face and a 2 px dark edge.

The caps are opaque and light grey on purpose: they read the same on GitHub's
light and dark themes, with no transparency that could vanish on a dark page.
All icons are 22 px tall; the README shows them with height="22".
"""

from __future__ import annotations

import sys
from pathlib import Path

H = 22
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

EDGE = "#3d4450"       # 2 px outline
SIDE_TOP = "#c5cbd3"   # side of the cap (visible as the bottom strip)
SIDE_BOT = "#959eaa"
FACE_TOP = "#fbfcfd"   # top face
FACE_BOT = "#dfe4ea"
FACE_LINE = "#aeb6c0"  # thin line where face meets side
HILITE = "#ffffff"     # highlight along the top of the face
INK = "#1f2328"        # label colour
ACCENT_TOP = "#5aa7ff" # pressed mouse button / wheel
ACCENT_BOT = "#1f6feb"

# name -> (label, width). Width grows with the label so text never touches the edge.
KEYS = {
    "enter": ("Enter", 44),
    "escape": ("Esc", 31),
    "shift": ("Shift", 40),
    "space": ("Space", 64),
    "alt": ("Alt", 30),
    "x": ("X", 22),
    "z": ("Z", 22),
    "f": ("F", 22),
    "g": ("G", 22),
    "f11": ("F11", 32),
    "f12": ("F12", 32),
}
ARROWS = {"up": "Up", "down": "Down", "left": "Left", "right": "Right"}
MICE = {
    "mouse-left-click": "Left mouse button",
    "mouse-right-click": "Right mouse button",
    "mouse-wheel": "Mouse wheel",
}


def gradients() -> str:
    return (
        "<defs>"
        f'<linearGradient id="face" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{FACE_TOP}"/><stop offset="1" stop-color="{FACE_BOT}"/></linearGradient>'
        f'<linearGradient id="side" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{SIDE_TOP}"/><stop offset="1" stop-color="{SIDE_BOT}"/></linearGradient>'
        f'<linearGradient id="acc" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{ACCENT_TOP}"/><stop offset="1" stop-color="{ACCENT_BOT}"/></linearGradient>'
        "</defs>"
    )


def svg(width: float, label: str, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:g}" height="{H}" '
        f'viewBox="0 0 {width:g} {H}" role="img" aria-label="{label}">'
        f"<title>{label}</title>{gradients()}{body}</svg>\n"
    )


def cap(width: float) -> str:
    """The keycap without a label: edge + side, then the face on top."""
    w = width
    return (
        # Body: this is the side of the key. The 2 px stroke is the edge.
        f'<rect x="1" y="1" width="{w - 2:g}" height="20" rx="4.5" fill="url(#side)" '
        f'stroke="{EDGE}" stroke-width="2"/>'
        # Face: inset, sitting high, so a ~3.5 px side strip shows below it.
        f'<rect x="2.6" y="2.3" width="{w - 5.2:g}" height="14.4" rx="3.2" fill="url(#face)" '
        f'stroke="{FACE_LINE}" stroke-width="0.6"/>'
        # Highlight along the top of the face.
        f'<path d="M5 3.4H{w - 5:g}" stroke="{HILITE}" stroke-width="1.2" stroke-linecap="round"/>'
    )


def key_svg(label: str, width: float) -> str:
    text = (
        f'<text x="{width / 2:g}" y="13.7" text-anchor="middle" font-family="{FONT}" '
        f'font-size="12" font-weight="600" fill="{INK}">{label}</text>'
    )
    return svg(width, label, cap(width) + text)


def arrow_svg(direction: str, label: str) -> str:
    w = 22
    cx, cy = w / 2, 9.5
    # A filled triangle plus a short shaft, drawn as a path (no font needed).
    pts = {
        "up": [(cx, cy - 4.6), (cx + 4.4, cy + 0.4), (cx - 4.4, cy + 0.4)],
        "down": [(cx, cy + 4.6), (cx + 4.4, cy - 0.4), (cx - 4.4, cy - 0.4)],
        "left": [(cx - 4.6, cy), (cx + 0.4, cy - 4.4), (cx + 0.4, cy + 4.4)],
        "right": [(cx + 4.6, cy), (cx - 0.4, cy - 4.4), (cx - 0.4, cy + 4.4)],
    }[direction]
    shaft = {
        "up": f"M{cx:g} {cy:g}V{cy + 4.4:g}",
        "down": f"M{cx:g} {cy:g}V{cy - 4.4:g}",
        "left": f"M{cx:g} {cy:g}H{cx + 4.4:g}",
        "right": f"M{cx:g} {cy:g}H{cx - 4.4:g}",
    }[direction]
    tri = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts) + "Z"
    body = (
        cap(w)
        + f'<path d="{tri}" fill="{INK}" stroke="{INK}" stroke-width="0.8" stroke-linejoin="round"/>'
        + f'<path d="{shaft}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>'
    )
    return svg(w, label, body)


def mouse_svg(which: str, label: str) -> str:
    """A mouse seen from above, same edge / side / face / highlight as the keys."""
    w = 16
    split_y = 9.2  # where the two buttons end
    left = f'<rect x="2.4" y="2.2" width="5.6" height="{split_y - 2.2:g}" fill="url(#acc)"/>'
    right = f'<rect x="8" y="2.2" width="5.6" height="{split_y - 2.2:g}" fill="url(#acc)"/>'
    pressed = {"mouse-left-click": left, "mouse-right-click": right, "mouse-wheel": ""}[which]
    if which == "mouse-wheel":
        wheel = (
            f'<rect x="6.4" y="3.0" width="3.2" height="5.6" rx="1.6" fill="url(#acc)" '
            f'stroke="{EDGE}" stroke-width="0.9"/>'
        )
    else:
        wheel = f'<rect x="7" y="3.6" width="2" height="4" rx="1" fill="{EDGE}"/>'
    body = (
        '<defs><clipPath id="faceclip"><rect x="2.4" y="2.2" width="11.2" height="15.6" rx="5.6"/>'
        "</clipPath></defs>"
        f'<rect x="1" y="1" width="14" height="20" rx="7" fill="url(#side)" stroke="{EDGE}" stroke-width="2"/>'
        f'<rect x="2.4" y="2.2" width="11.2" height="15.6" rx="5.6" fill="url(#face)" '
        f'stroke="{FACE_LINE}" stroke-width="0.6"/>'
        f'<g clip-path="url(#faceclip)">{pressed}</g>'
        f'<path d="M8 2.2V{split_y:g}M2.4 {split_y:g}H13.6" stroke="{EDGE}" stroke-width="0.9"/>'
        f'<path d="M5 3.6Q8 2.6 11 3.6" stroke="{HILITE}" stroke-width="1" fill="none" '
        f'stroke-linecap="round"/>'
        + wheel
    )
    return svg(w, label, body)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3]
    out = root / "docs" / "img" / "keys"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for name, (label, width) in KEYS.items():
        (out / f"{name}.svg").write_text(key_svg(label, width), encoding="utf-8", newline="\n")
        n += 1
    for name, label in ARROWS.items():
        (out / f"{name}.svg").write_text(arrow_svg(name, label), encoding="utf-8", newline="\n")
        n += 1
    for name, label in MICE.items():
        (out / f"{name}.svg").write_text(mouse_svg(name, label), encoding="utf-8", newline="\n")
        n += 1
    print(f"wrote {n} icons to {out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
