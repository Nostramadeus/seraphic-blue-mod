"""Draw the README section banners as PNG, in the game's chapter-card style.

    python make_banners.py [OUT_ROOT]

Writes OUT_ROOT/docs/img/banners/<slug>.png (OUT_ROOT defaults to the
repository root, three folders up from docs/img/tools/). One banner per row of
BANNERS below: a hero banner (1800 x 320) and section banners (1800 x 150),
all drawn at 2x so the README can show them with width="900".

Needs Pillow. This is the only docs tool that does; the others are standard
library only. Install it with "python -m pip install Pillow".

Fonts: Garamond Italic (C:/Windows/Fonts/GARAIT.TTF) for titles and Georgia
Italic (C:/Windows/Fonts/georgiai.ttf) for subtitles, both Microsoft Windows
system fonts. The text is rasterized into the PNG; no font file is
distributed. If a font is missing the script stops instead of substituting.

Layers, bottom to top:
  1. vertical gradient #000307 (top) to #001628 (bottom)
  2. azure glow #0E92F8 from the bottom-left corner, alpha 0.55 there,
     falling linearly to 0 at 0.55 x width
  3. seven blurred bokeh circles #9BDCFF (alpha 0.06-0.14, radius 40-130,
     blur 18), placed by random.Random(slug) inside the right 55 percent
  4. window-skin frame, square corners: 4 px #88CAFA, 4 px #018CF7,
     4 px #052367 (the 2/2/2 px rim of the game's extsys.png at 2x)
  5. cyan rule, 2 px #0ED5D6 at alpha 0.8, 56 px in from each side
  6. title, Garamond Italic #F0F0F0, 3 px #3080D0 stroke, #0E92F8 glow
     (blur 14, alpha 0.7) under it; ink left edge at x=60; vertically, the
     box of the probe string "Hpg" at the title size (stroke included) is
     centred between the frame and the rule, so all titles share a baseline
  7. subtitle, Georgia Italic #C0C0C0: section banners right-aligned to
     width - 70 and centred like the title with its own "Hpg" box (40 px;
     32 px if the title is wider than width - 70 - subtitle - 80; dropped if
     it still is); hero: under the title, ink left edge at x=64, the two
     "Hpg" boxes plus a 16 px gap centred between the frame and the rule as
     one block

The images are opaque RGB, so they look the same on GitHub's light and dark
themes. Every run gives the same pixels.
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W = 1800
H_SECTION = 150
H_HERO = 320

FONT_TITLE = Path("C:/Windows/Fonts/GARAIT.TTF")
FONT_SUB = Path("C:/Windows/Fonts/georgiai.ttf")

GRAD_TOP = "#000307"
GRAD_BOT = "#001628"
GLOW = "#0E92F8"
BOKEH = "#9BDCFF"
FRAME = ("#88CAFA", "#018CF7", "#052367")  # outside in, 4 px each
FRAME_W = 4
RULE = "#0ED5D6"
TITLE = "#F0F0F0"
TITLE_STROKE = "#3080D0"
MOD_COLOUR = "#BBDEFC"
SUB = "#C0C0C0"

TITLE_X = 60
STROKE = 3
SUB_RIGHT = 70           # section subtitle: ink right edge at W - 70
SUB_GAP = 80             # overlap when title width > W - 70 - subtitle width - 80
HERO_SUB_X = 64
HERO_GAP = 16            # hero: px between the title's and the subtitle's probe boxes
PROBE = "Hpg"            # vertical centring uses this string's box, so every banner shares one baseline

BANNERS = [
    ("hero", "Seraphic Blue MOD", "English retranslation \u00b7 MOD menu \u00b7 DC Altered build"),
    ("mode", "Which mode to pick", "Three ways to play"),
    ("trip-original", "A dungeon trip: Original rules", "The journey is the challenge"),
    ("trip-arrange", "A dungeon trip: Arrange rules", "Each boss is the challenge"),
    ("downloads", "Downloads", "Three builds, one ZIP each"),
    ("saves", "Keep your saves", "Old saves load here"),
    ("altered", "The Altered build", "A fan patch, in English, with the MOD"),
    ("tutorials", "Quick tutorials", "Mouse, keyboard, Steam Deck"),
    ("modmenu", "MOD menu", "Speed \u00b7 Battles \u00b7 Cheats"),
    ("controls", "Controls", "Every key and button"),
    ("releases", "Release notes", "What changed, version by version"),
    ("credits", "Credits", "The people who made this possible"),
]


def rgb(colour: str) -> tuple[int, int, int]:
    return tuple(int(colour[i:i + 2], 16) for i in (1, 3, 5))


def paint(img: Image.Image, colour: str, mask: Image.Image) -> None:
    """Blend a flat colour over img through an L mask (0 = none, 255 = full)."""
    img.paste(Image.new("RGB", img.size, rgb(colour)), (0, 0), mask)


def gradient(w: int, h: int) -> Image.Image:
    top, bot = rgb(GRAD_TOP), rgb(GRAD_BOT)
    col = Image.new("RGB", (1, h))
    col.putdata([tuple(round(a + (b - a) * y / (h - 1)) for a, b in zip(top, bot)) for y in range(h)])
    return col.resize((w, h), Image.NEAREST)


def glow_mask(w: int, h: int) -> Image.Image:
    radius = 0.55 * w
    data = []
    for y in range(h):
        dy = h - (y + 0.5)
        for x in range(w):
            d = math.hypot(x + 0.5, dy)
            data.append(round(255 * 0.55 * max(0.0, 1.0 - d / radius)))
    mask = Image.new("L", (w, h))
    mask.putdata(data)
    return mask


def bokeh(img: Image.Image, slug: str) -> None:
    w, h = img.size
    rng = random.Random(slug)
    left = 0.45 * w  # whole circle inside the right 55 percent of the canvas
    for _ in range(7):
        r = rng.uniform(40, 130)
        cx = rng.uniform(left + r, w)
        cy = rng.uniform(0, h)
        alpha = rng.uniform(0.06, 0.14)
        mask = Image.new("L", (w, h), 0)
        ImageDraw.Draw(mask).ellipse([cx - r, cy - r, cx + r, cy + r], fill=round(255 * alpha))
        paint(img, BOKEH, mask.filter(ImageFilter.GaussianBlur(18)))


def frame(img: Image.Image) -> None:
    w, h = img.size
    draw = ImageDraw.Draw(img)
    for i, colour in enumerate(FRAME):
        o = i * FRAME_W
        draw.rectangle([o, o, w - 1 - o, h - 1 - o], outline=rgb(colour), width=FRAME_W)


def rule(img: Image.Image, y: int) -> None:
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rectangle([56, y, w - 57, y + 1], fill=round(255 * 0.8))
    paint(img, RULE, mask)


def ink(parts) -> tuple[int, int, int, int]:
    """Ink box of title parts [(text, font, colour, x_offset)] relative to the baseline origin."""
    boxes = []
    for text, font, _colour, dx in parts:
        l, t, r, b = font.getbbox(text, anchor="ls", stroke_width=STROKE)
        boxes.append((l + dx, t, r + dx, b))
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))


def draw_title(img: Image.Image, parts, x: int, y: int) -> None:
    """Draw parts with their baseline origin at (x, y): blurred glow layer first, then stroked text."""
    mask = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(mask)
    for text, font, _colour, dx in parts:
        md.text((x + dx, y), text, font=font, fill=255, anchor="ls")
    mask = mask.filter(ImageFilter.GaussianBlur(14)).point(lambda v: round(v * 0.7))
    paint(img, GLOW, mask)
    draw = ImageDraw.Draw(img)
    for text, font, colour, dx in parts:
        draw.text((x + dx, y), text, font=font, fill=rgb(colour), anchor="ls",
                  stroke_width=STROKE, stroke_fill=rgb(TITLE_STROKE))


def make(slug: str, title: str, subtitle: str, notes: list[str]) -> Image.Image:
    hero = slug == "hero"
    w, h = W, (H_HERO if hero else H_SECTION)
    img = gradient(w, h)
    paint(img, GLOW, glow_mask(w, h))
    bokeh(img, slug)
    frame(img)
    rule_y = h - (40 if hero else 30)
    rule(img, rule_y)
    top = len(FRAME) * FRAME_W          # inner edge of the frame
    centre = (top + rule_y) / 2

    if hero:
        big = ImageFont.truetype(str(FONT_TITLE), 170)
        small = ImageFont.truetype(str(FONT_TITLE), 90)
        head = "Seraphic Blue"
        assert title == head + " MOD"
        parts = [(head, big, TITLE, 0), (" MOD", small, MOD_COLOUR, round(big.getlength(head)))]
        sub_font = ImageFont.truetype(str(FONT_SUB), 56)
        tl = ink(parts)[0]
        _, tt, _, tb = big.getbbox(PROBE, anchor="ls", stroke_width=STROKE)
        sl = sub_font.getbbox(subtitle, anchor="ls")[0]
        _, st, _, sb = sub_font.getbbox(PROBE, anchor="ls")
        block = (tb - tt) + HERO_GAP + (sb - st)
        title_top = round(centre - block / 2)
        draw_title(img, parts, TITLE_X - tl, title_top - tt)
        sy = title_top + (tb - tt) + HERO_GAP - st
        ImageDraw.Draw(img).text((HERO_SUB_X - sl, sy), subtitle, font=sub_font, fill=rgb(SUB), anchor="ls")
        return img

    font = ImageFont.truetype(str(FONT_TITLE), 76)
    parts = [(title, font, TITLE, 0)]
    tl, _, tr, _ = ink(parts)
    _, tt, _, tb = font.getbbox(PROBE, anchor="ls", stroke_width=STROKE)
    draw_title(img, parts, TITLE_X - tl, round(centre - (tt + tb) / 2))
    title_w = tr - tl
    for size in (40, 32):
        sub_font = ImageFont.truetype(str(FONT_SUB), size)
        sl, _, sr, _ = sub_font.getbbox(subtitle, anchor="ls")
        _, st, _, sb = sub_font.getbbox(PROBE, anchor="ls")
        if title_w <= w - SUB_RIGHT - (sr - sl) - SUB_GAP:
            if size != 40:
                notes.append(f"{slug}: subtitle shrunk to {size} px")
            ImageDraw.Draw(img).text((w - SUB_RIGHT - sr, round(centre - (st + sb) / 2)), subtitle,
                                     font=sub_font, fill=rgb(SUB), anchor="ls")
            break
    else:
        notes.append(f"{slug}: subtitle dropped (title too wide)")
    return img


def main() -> int:
    for f in (FONT_TITLE, FONT_SUB):
        if not f.is_file():
            print(f"missing font {f.as_posix()}; stopping (no substitute)", file=sys.stderr)
            return 1
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3]
    out = root / "docs" / "img" / "banners"
    out.mkdir(parents=True, exist_ok=True)
    notes: list[str] = []
    for slug, title, subtitle in BANNERS:
        make(slug, title, subtitle, notes).save(out / f"{slug}.png", optimize=True)
    for n in notes:
        print(n)
    print(f"wrote {len(BANNERS)} banners to {out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
