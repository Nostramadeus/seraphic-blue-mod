"""Draw the README battle-flow diagrams and the mode picker as SVG.

    python make_flow.py SOURCE.md [OUT_ROOT]

SOURCE.md is the battle-flow text (the README section "How a dungeon trip
feels", or the file it was written in). The script reads, from it:

  ### Original rules (...)   seven numbered steps -> flow-original.svg
  ### Arrange rules (...)    seven numbered steps -> flow-arrange.svg
  ### One line each          the Original / Arrange lines -> mode-picker.svg

A step is "N. **What happens.** more of what happens" followed by indented
"- ..." lines: a line in double quotes is what the player thinks (drawn as a
speech bubble), any other line is a note drawn inside the step's box. The text
is used exactly as written; nothing is reworded. Lines that are not steps
(an <img> tag, blank lines) are skipped, so the script also runs on the README
after the diagrams have been inserted into it.

Writes OUT_ROOT/docs/img/flow-original.svg, flow-arrange.svg, mode-picker.svg
(OUT_ROOT defaults to the repository root, three folders up from docs/img/tools/) and embeds the 64 px emoji from
OUT_ROOT/docs/img/emoji/ as data URIs (an SVG shown through <img> cannot load
other files). Standard library only.

Each SVG has its own background rectangle and two colour sets, picked by the
viewer's light/dark setting, so it reads on GitHub's light and dark themes.
Text width is estimated from Arial character widths plus a safety margin.
"""

from __future__ import annotations

import base64
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

W = 900
PAD = 24
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

# Which emoji goes in which step box (step number -> codepoints). Hourglass =
# the SUP pools, warning = an ailment or an ambush, shield = counters / guard,
# crossed swords = the boss, medal = the win after the boss.
ICONS = {
    "original": {1: ["23f3"], 2: ["23f3"], 3: ["26a0"], 4: ["26a0"], 5: ["23f3"], 6: ["2694"], 7: ["1f3c5"]},
    "arrange": {1: ["23f3"], 3: ["1f6e1"], 6: ["2694", "1f6e1"], 7: ["1f3c5"]},
}

# Mode picker text not in SOURCE.md, quoted from the README's "Which mode to pick".
PICKER = [
    {
        "name": "Original",
        "role": "The purist choice.",
        "setup": "The game as the author designed it (DC + the fixes below), NORMAL difficulty.",
        "line_from": "Original",  # the line comes from "One line each"
        "icon": "23f3",
        "accent": "orig",
    },
    {
        "name": "Extra content",
        "role": "",  # the badge says it: "First play (recommended)"
        "setup": "MANY on, BATTLE off, all five ARRANGE switches Off.",
        "line": "That is Altered's extra content (side maps, chatter, gear, shops) with the original battle rules.",
        "icon": "1f3ae",
        "accent": "rec",
        "recommended": True,
    },
    {
        "name": "Full Arrange",
        "role": "For a second run, if you want a smoother, modern-feeling run.",
        "setup": "BATTLE + MANY, switches On.",
        "line_from": "Arrange",
        "icon": "2694",
        "accent": "arr",
    },
]

# Arial advance widths (1/1000 em), regular. Bold text gets a wider factor.
_AW = dict(zip(
    " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
    [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
     556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
     1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
     667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
     333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
     556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584],
))


def text_w(s: str, size: float, bold: bool = False) -> float:
    k = 1.13 if bold else 1.07  # margin: Segoe UI / San Francisco run a little wider than Arial
    return sum(_AW.get(ch, 600) for ch in s) * size / 1000 * k


def wrap(s: str, width: float, size: float, bold: bool = False) -> list[str]:
    lines, cur = [], ""
    for word in s.split():
        trial = f"{cur} {word}" if cur else word
        if cur and text_w(trial, size, bold) > width:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


# --- parsing --------------------------------------------------------------------

STEP = re.compile(r"^(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)$")
SUB = re.compile(r"^\s{2,}[-*]\s+(.*)$")
ONE = re.compile(r"^[-*]\s+(Original|Arrange):\s+(.*)$")


def parse(md: str) -> dict:
    out: dict = {"original": None, "arrange": None, "oneline": {}}
    key = None
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("#"):
            head = line.lstrip("#").strip()
            if head.startswith("Original rules"):
                key = "original"
            elif head.startswith("Arrange rules"):
                key = "arrange"
            elif head.startswith("One line each"):
                key = "oneline"
                continue
            else:
                key = None
                continue
            m = re.match(r"^(.*?)\s*\((.*)\)\s*$", head)
            title, sub = (m.group(1), m.group(2)) if m else (head, "")
            out[key] = {"title": title, "subtitle": sub, "steps": []}
            continue
        if key in ("original", "arrange"):
            m = STEP.match(line)
            if m:
                out[key]["steps"].append({
                    "n": int(m.group(1)), "title": m.group(2).strip(), "body": m.group(3).strip(),
                    "thoughts": [], "notes": [],
                })
                continue
            m = SUB.match(line)
            if m and out[key]["steps"]:
                t = m.group(1).strip()
                st = out[key]["steps"][-1]
                if len(t) >= 2 and t[0] == '"' and t[-1] == '"':
                    st["thoughts"].append(t[1:-1])
                else:
                    st["notes"].append(t)
        elif key == "oneline":
            m = ONE.match(line)
            if m:
                out["oneline"][m.group(1)] = m.group(2).strip()
    for k in ("original", "arrange"):
        if not out[k] or len(out[k]["steps"]) != 7:
            n = len(out[k]["steps"]) if out[k] else 0
            raise SystemExit(f"{k}: expected 7 steps, found {n}")
    for k in ("Original", "Arrange"):
        if k not in out["oneline"]:
            raise SystemExit(f"'One line each' has no {k} line")
    return out


# --- drawing helpers ----------------------------------------------------------------

STYLE = """
.bg{fill:#f6f8fa;stroke:#d0d7de}
.box{fill:#ffffff;stroke:#afb8c1}
.t{fill:#1f2328}
.m{fill:#59636e}
.bub{fill:#fff8c5;stroke:#c69026}
.ln{stroke:#8c959f;fill:none}
.lnh{fill:#8c959f}
.orig{fill:#8250df}.origs{stroke:#8250df}.origt{fill:#6639ba}.orign{fill:#f6f1ff}
.arr{fill:#0969da}.arrs{stroke:#0969da}.arrt{fill:#0550ae}.arrn{fill:#eef6ff}
.rec{fill:#1a7f37}.recs{stroke:#1a7f37}.rect{fill:#116329}.recn{fill:#effaf2}
.on{fill:#ffffff}
@media (prefers-color-scheme: dark){
.bg{fill:#161b22;stroke:#3d444d}
.box{fill:#0d1117;stroke:#4d5562}
.t{fill:#e6edf3}
.m{fill:#9198a1}
.bub{fill:#2e2614;stroke:#bb8009}
.ln{stroke:#7d8590}
.lnh{fill:#7d8590}
.orig{fill:#a37ef5}.origs{stroke:#a37ef5}.origt{fill:#c4a9fb}.orign{fill:#211a33}
.arr{fill:#4493f8}.arrs{stroke:#4493f8}.arrt{fill:#79b8ff}.arrn{fill:#0f2034}
.rec{fill:#3fb950}.recs{stroke:#3fb950}.rect{fill:#56d364}.recn{fill:#0f2a17}
.on{fill:#0d1117}
}
"""


def t(x: float, y: float, s: str, size: float, cls: str = "t", bold: bool = False,
      italic: bool = False, anchor: str = "start") -> str:
    attrs = f'x="{x:.1f}" y="{y:.1f}" font-size="{size:g}" class="{cls}"'
    if bold:
        attrs += ' font-weight="700"'
    if italic:
        attrs += ' font-style="italic"'
    if anchor != "start":
        attrs += f' text-anchor="{anchor}"'
    return f"<text {attrs}>{escape(s)}</text>"


def lines_at(x: float, top: float, lines: list[str], size: float, lh: float, **kw) -> tuple[str, float]:
    """Draw wrapped lines from `top`; return (svg, new top)."""
    out = []
    for ln in lines:
        out.append(t(x, top + lh * 0.5 + size * 0.36, ln, size, **kw))
        top += lh
    return "".join(out), top


def emoji_defs(root: Path, cps: set[str], size: int) -> str:
    out = []
    for cp in sorted(cps):
        b64 = base64.b64encode((root / "docs" / "img" / "emoji" / f"{cp}.png").read_bytes()).decode()
        out.append(
            f'<image id="e{cp}" width="{size}" height="{size}" '
            f'href="data:image/png;base64,{b64}"/>'
        )
    return "".join(out)


def svg_doc(height: float, title: str, desc: str, defs: str, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{W}" height="{height:.0f}" viewBox="0 0 {W} {height:.0f}" role="img" '
        f'aria-label="{escape(title)}">'
        f"<title>{escape(title)}</title><desc>{escape(desc)}</desc>"
        f"<style>{STYLE}</style><defs>{defs}</defs>"
        f'<g font-family="{escape(FONT)}">'
        f'<rect class="bg" x="0.5" y="0.5" width="{W - 1}" height="{height - 1:.0f}" rx="12" stroke-width="1"/>'
        f"{body}</g></svg>\n"
    )


# --- flow diagrams --------------------------------------------------------------------

NUM_CX = PAD + 17
BOX_X = 74
BOX_W = 452
BUB_X = 566
BUB_W = W - PAD - BUB_X
IN = 16          # inner padding
ICON = 30
LH = 21          # body line height
GAP = 34         # space between boxes (holds the arrow)


def bubble_path(x: float, y: float, w: float, h: float, r: float, tip_x: float, tail_y: float) -> str:
    """Rounded rectangle with a tail on its left side pointing at (tip_x, tail_y)."""
    ty0, ty1 = tail_y - 7, tail_y + 7
    return (
        f"M{x + r:.1f} {y:.1f}H{x + w - r:.1f}"
        f"A{r} {r} 0 0 1 {x + w:.1f} {y + r:.1f}V{y + h - r:.1f}"
        f"A{r} {r} 0 0 1 {x + w - r:.1f} {y + h:.1f}H{x + r:.1f}"
        f"A{r} {r} 0 0 1 {x:.1f} {y + h - r:.1f}V{ty1:.1f}"
        f"L{tip_x:.1f} {tail_y + 2:.1f}L{x:.1f} {ty0:.1f}V{y + r:.1f}"
        f"A{r} {r} 0 0 1 {x + r:.1f} {y:.1f}Z"
    )


def flow_svg(key: str, sec: dict, root: Path) -> str:
    acc = "orig" if key == "original" else "arr"
    icons = ICONS[key]
    body: list[str] = []

    # Header.
    y = PAD
    body.append(t(PAD, y + 22, sec["title"], 24, bold=True))
    y += 34
    if sec["subtitle"]:
        s, y = lines_at(PAD, y, wrap(sec["subtitle"], W - 2 * PAD, 15), 15, 21, cls="m")
        body.append(s)
    y += 10
    # Legend: a small box and a small bubble with their meaning.
    body.append(f'<rect class="box" x="{PAD}" y="{y:.1f}" width="26" height="18" rx="4" stroke-width="1.5"/>')
    body.append(t(PAD + 34, y + 14, "What the game does", 14, cls="m"))
    lx = PAD + 34 + text_w("What the game does", 14) + 28
    body.append(f'<path class="bub" stroke-width="1.5" d="{bubble_path(lx + 8, y, 26, 18, 4, lx, y + 9)}"/>')
    body.append(t(lx + 42, y + 14, "What the player is thinking", 14, cls="m"))
    y += 18 + 22

    prev_bottom = None
    for st in sec["steps"]:
        n = st["n"]
        cps = icons.get(n, [])
        icon_room = len(cps) * (ICON + 6)
        title_lines = wrap(st["title"], BOX_W - 2 * IN - icon_room, 16, bold=True)
        body_lines = wrap(st["body"], BOX_W - 2 * IN, 14.5)
        note_blocks = [wrap(nt, BOX_W - 2 * IN - 20, 14.5, bold=True) for nt in st["notes"]]
        box_h = IN + len(title_lines) * 23 + 4 + len(body_lines) * LH + IN - 2
        for nb in note_blocks:
            box_h += 10 + len(nb) * LH + 12
        if cps:
            box_h = max(box_h, IN + ICON + IN)

        thought_blocks = [wrap(f"“{th}”", BUB_W - 2 * IN, 14.5) for th in st["thoughts"]]
        bub_hs = [IN - 3 + len(b) * LH + IN - 3 for b in thought_blocks]
        bub_top = y + 10
        bub_total = sum(bub_hs) + 12 * max(0, len(bub_hs) - 1)
        row_h = max(box_h, 10 + bub_total)

        # Arrow from the previous box.
        if prev_bottom is not None:
            ax = BOX_X + BOX_W / 2
            body.append(f'<path class="ln" stroke-width="2.5" d="M{ax:.1f} {prev_bottom + 4:.1f}V{y - 10:.1f}"/>')
            body.append(f'<path class="lnh" d="M{ax - 7:.1f} {y - 12:.1f}L{ax + 7:.1f} {y - 12:.1f}L{ax:.1f} {y - 3:.1f}Z"/>')

        # Step number.
        cy = y + 25
        body.append(f'<circle class="{acc}" cx="{NUM_CX}" cy="{cy:.1f}" r="16"/>')
        body.append(t(NUM_CX, cy + 6, str(n), 17, cls="on", bold=True, anchor="middle"))

        # Box: what happens.
        body.append(f'<rect class="box" x="{BOX_X}" y="{y:.1f}" width="{BOX_W}" height="{box_h:.1f}" rx="10" stroke-width="1.5"/>')
        for i, cp in enumerate(cps):
            ix = BOX_X + BOX_W - IN - ICON - i * (ICON + 6) + 4
            body.append(f'<use href="#e{cp}" xlink:href="#e{cp}" x="{ix:.1f}" y="{y + 10:.1f}"/>')
        top = y + IN - 4
        s, top = lines_at(BOX_X + IN, top, title_lines, 16, 23, cls=f"{acc}t", bold=True)
        body.append(s)
        top += 4
        s, top = lines_at(BOX_X + IN, top, body_lines, 14.5, LH)
        body.append(s)
        for nb in note_blocks:
            top += 10
            nh = len(nb) * LH + 8
            body.append(f'<rect class="{acc}n" x="{BOX_X + IN:.1f}" y="{top - 4:.1f}" width="{BOX_W - 2 * IN}" height="{nh:.1f}" rx="5"/>')
            body.append(f'<rect class="{acc}" x="{BOX_X + IN:.1f}" y="{top - 4:.1f}" width="4" height="{nh:.1f}"/>')
            s, top = lines_at(BOX_X + IN + 14, top, nb, 14.5, LH, bold=True)
            body.append(s)
            top += 4

        # Speech bubble(s): what the player thinks.
        by = bub_top
        for blk, bh in zip(thought_blocks, bub_hs):
            tail_y = by + min(24, bh / 2)
            body.append(f'<path class="bub" stroke-width="1.5" d="{bubble_path(BUB_X, by, BUB_W, bh, 12, BOX_X + BOX_W + 8, tail_y)}"/>')
            s, _ = lines_at(BUB_X + IN, by + IN - 3, blk, 14.5, LH, italic=True)
            body.append(s)
            by += bh + 12

        prev_bottom = y + box_h
        y += row_h + GAP

    height = y - GAP + PAD
    used = {cp for v in icons.values() for cp in v}
    desc = (f"{sec['title']}: seven steps of one dungeon trip. Each box is what the game does; "
            "each speech bubble is what the player is thinking. The same text is in the README.")
    return svg_doc(height, sec["title"], desc, emoji_defs(root, used, ICON), "".join(body))


# --- mode picker --------------------------------------------------------------------

def picker_svg(oneline: dict, root: Path) -> str:
    gap = 16
    col_w = (W - 2 * PAD - 2 * gap) / 3
    inner = col_w - 2 * IN
    body: list[str] = []
    y = PAD
    body.append(t(PAD, y + 22, "Which mode to pick", 24, bold=True))
    y += 34 + 26  # room for the badge above the middle card
    cards = []
    for col in PICKER:
        line = col.get("line") or oneline[col["line_from"]]
        line = line[0].upper() + line[1:]
        name_lines = wrap(col["name"], inner - 46, 17, bold=True)
        role_lines = wrap(col["role"], inner, 14, bold=True) if col["role"] else []
        setup_lines = wrap(col["setup"], inner, 14)
        line_lines = wrap(line, inner, 14.5)
        h = IN + max(40, len(name_lines) * 22) + 10 + len(role_lines) * 20 + (10 if role_lines else 0) \
            + len(setup_lines) * 20 + 18 + len(line_lines) * LH + IN
        cards.append((col, name_lines, role_lines, setup_lines, line_lines, h))
    card_h = max(c[-1] for c in cards)
    for i, (col, name_lines, role_lines, setup_lines, line_lines, _) in enumerate(cards):
        x = PAD + i * (col_w + gap)
        a = col["accent"]
        rec = col.get("recommended", False)
        sw = 3 if rec else 1.5
        body.append(f'<rect class="box {a}s" x="{x:.1f}" y="{y:.1f}" width="{col_w:.1f}" height="{card_h:.1f}" rx="12" stroke-width="{sw}"/>')
        body.append(f'<rect class="{a}" x="{x + 1.5:.1f}" y="{y + 1.5:.1f}" width="{col_w - 3:.1f}" height="6" rx="3"/>')
        if rec:
            label = "First play (recommended)"
            bw = text_w(label, 13, bold=True) + 34
            bx = x + (col_w - bw) / 2
            body.append(f'<rect class="{a}" x="{bx:.1f}" y="{y - 15:.1f}" width="{bw:.1f}" height="28" rx="14"/>')
            body.append(f'<path class="on" d="{star(bx + 17, y - 1, 6.5)}"/>')
            body.append(t(bx + 28, y + 3.5, label, 13, cls="on", bold=True))
        top = y + IN + 4
        body.append(f'<use href="#e{col["icon"]}" xlink:href="#e{col["icon"]}" x="{x + IN:.1f}" y="{top:.1f}"/>')
        name_h = max(40, len(name_lines) * 22)
        s, _ = lines_at(x + IN + 46, top + (name_h - len(name_lines) * 22) / 2, name_lines, 17, 22, bold=True)
        body.append(s)
        top += name_h + 10
        if role_lines:
            s, top = lines_at(x + IN, top, role_lines, 14, 20, cls=f"{a}t", bold=True)
            body.append(s)
            top += 10
        s, top = lines_at(x + IN, top, setup_lines, 14, 20, cls="m")
        body.append(s)
        top += 9
        body.append(f'<path class="ln" stroke-width="1" d="M{x + IN:.1f} {top:.1f}H{x + col_w - IN:.1f}"/>')
        top += 9
        s, top = lines_at(x + IN, top, line_lines, 14.5, LH)
        body.append(s)
    height = y + card_h + PAD
    desc = ("Three ways to play: Original, extra content with the five ARRANGE switches Off "
            "(recommended first play), and Full Arrange. The same text is in the README.")
    used = {c["icon"] for c in PICKER}
    return svg_doc(height, "Which mode to pick", desc, emoji_defs(root, used, 40), "".join(body))


def star(cx: float, cy: float, r: float) -> str:
    import math
    pts = []
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.45
        ang = -math.pi / 2 + k * math.pi / 5
        pts.append(f"{cx + rr * math.cos(ang):.2f} {cy + rr * math.sin(ang):.2f}")
    return "M" + "L".join(pts) + "Z"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1])
    root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parents[3]
    data = parse(src.read_text(encoding="utf-8"))
    out = root / "docs" / "img"
    out.mkdir(parents=True, exist_ok=True)
    files = {
        "flow-original.svg": flow_svg("original", data["original"], root),
        "flow-arrange.svg": flow_svg("arrange", data["arrange"], root),
        "mode-picker.svg": picker_svg(data["oneline"], root),
    }
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8", newline="\n")
        print(f"{name}: {len(text.encode()) // 1024} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
