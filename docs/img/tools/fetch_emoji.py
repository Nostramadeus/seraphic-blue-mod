"""Fetch the README's 3D emoji (Microsoft Fluent UI Emoji, MIT) and save them at 64 px.

    python fetch_emoji.py DOWNLOAD_DIR [OUT_ROOT]

Same source and naming as the Magic Writer icon library: the 3D render from
github.com/microsoft/fluentui-emoji (assets/<Name>/3D/*.png), named by the
codepoint in that folder's metadata.json. Instead of cloning the whole 416 MB
repository, only the ten files needed are downloaded, one by one, into
DOWNLOAD_DIR (kept apart from this script). Each 256 px render is scaled down
to 64 px with a 4x4 box filter on premultiplied alpha, so edges stay clean.

Writes OUT_ROOT/docs/img/emoji/<codepoint>.png (OUT_ROOT defaults to the
repository root, three folders up from docs/img/tools/). The variation selector fe0f is dropped from the file name.
Standard library only: the PNG reading and writing below is a minimal
decoder/encoder for 8-bit non-interlaced PNGs.
"""

from __future__ import annotations

import json
import struct
import sys
import urllib.parse
import urllib.request
import zlib
from pathlib import Path

RAW = "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/"
API = "https://api.github.com/repos/microsoft/fluentui-emoji/contents/assets/"

# codepoint -> Fluent folder name (the CLDR name).
EMOJI = {
    "2328": "Keyboard",
    "1f5b1": "Computer mouse",
    "1f579": "Joystick",
    "1f3ae": "Video game",
    "1f6e1": "Shield",
    "2694": "Crossed swords",
    "23f3": "Hourglass not done",
    "1f3c5": "Sports medal",
    "1f4ca": "Bar chart",
    "26a0": "Warning",
}
SIZE = 64


def fetch(url: str, dest: Path) -> bytes:
    if dest.exists():
        return dest.read_bytes()
    req = urllib.request.Request(url, headers={"User-Agent": "fetch_emoji.py"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    dest.write_bytes(data)
    return data


# --- minimal PNG decode / encode ------------------------------------------------

def _paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    return b if pb <= pc else c


def png_decode(data: bytes) -> tuple[int, int, list[bytearray]]:
    """Return (width, height, rows of RGBA bytes)."""
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    pos, idat, plte, trns = 8, b"", b"", b""
    width = height = depth = ctype = interlace = 0
    while pos < len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        chunk = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, depth, ctype, _, _, interlace = struct.unpack(">IIBBBBB", chunk)
        elif kind == b"PLTE":
            plte = chunk
        elif kind == b"tRNS":
            trns = chunk
        elif kind == b"IDAT":
            idat += chunk
        elif kind == b"IEND":
            break
    if depth != 8 or interlace != 0 or ctype not in (2, 3, 6):
        raise ValueError(f"unsupported PNG (depth {depth}, type {ctype}, interlace {interlace})")
    bpp = {2: 3, 3: 1, 6: 4}[ctype]
    raw = zlib.decompress(idat)
    stride = width * bpp
    rows: list[bytearray] = []
    prev = bytearray(stride)
    i = 0
    for _ in range(height):
        f = raw[i]
        line = bytearray(raw[i + 1:i + 1 + stride])
        i += 1 + stride
        for x in range(stride):
            a = line[x - bpp] if x >= bpp else 0
            b = prev[x]
            c = prev[x - bpp] if x >= bpp else 0
            if f == 1:
                line[x] = (line[x] + a) & 255
            elif f == 2:
                line[x] = (line[x] + b) & 255
            elif f == 3:
                line[x] = (line[x] + ((a + b) >> 1)) & 255
            elif f == 4:
                line[x] = (line[x] + _paeth(a, b, c)) & 255
        prev = line
        if ctype == 6:
            rows.append(line)
        elif ctype == 2:
            out = bytearray()
            for x in range(width):
                out += line[x * 3:x * 3 + 3] + b"\xff"
            rows.append(out)
        else:
            out = bytearray()
            for x in range(width):
                k = line[x]
                out += plte[k * 3:k * 3 + 3] + bytes([trns[k] if k < len(trns) else 255])
            rows.append(out)
    return width, height, rows


def png_encode(width: int, height: int, rows: list[bytearray]) -> bytes:
    def chunk(kind: bytes, body: bytes) -> bytes:
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body))

    raw = bytearray()
    prev = bytearray(width * 4)
    for line in rows:
        # Pick the cheaper of filter 0 (none), 1 (sub) and 2 (up) per row.
        sub = bytearray((line[x] - (line[x - 4] if x >= 4 else 0)) & 255 for x in range(len(line)))
        up = bytearray((line[x] - prev[x]) & 255 for x in range(len(line)))
        cands = [(0, line), (1, sub), (2, up)]
        f, best = min(cands, key=lambda t: sum(v if v < 128 else 256 - v for v in t[1]))
        raw += bytes([f]) + best
        prev = line
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + chunk(b"IEND", b"")
    )


def downscale(width: int, height: int, rows: list[bytearray], size: int) -> list[bytearray]:
    """Box filter on premultiplied alpha. Needs width and height divisible by size."""
    if width % size or height % size:
        raise ValueError(f"{width}x{height} is not a multiple of {size}")
    fx, fy = width // size, height // size
    n = fx * fy
    out = []
    for oy in range(size):
        line = bytearray()
        for ox in range(size):
            r = g = b = a = 0
            for yy in range(oy * fy, oy * fy + fy):
                row = rows[yy]
                for xx in range(ox * fx, ox * fx + fx):
                    p = xx * 4
                    al = row[p + 3]
                    r += row[p] * al
                    g += row[p + 1] * al
                    b += row[p + 2] * al
                    a += al
            if a == 0:
                line += b"\x00\x00\x00\x00"
            else:
                line += bytes((
                    min(255, round(r / a)),
                    min(255, round(g / a)),
                    min(255, round(b / a)),
                    min(255, round(a / n)),
                ))
        out.append(line)
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    dl = Path(sys.argv[1])
    root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parents[3]
    dl.mkdir(parents=True, exist_ok=True)
    out = root / "docs" / "img" / "emoji"
    out.mkdir(parents=True, exist_ok=True)
    for cp, name in EMOJI.items():
        q = urllib.parse.quote(name)
        meta = json.loads(fetch(RAW + q + "/metadata.json", dl / f"{cp}.metadata.json"))
        got = (meta.get("unicode") or "").lower().replace(" fe0f", "").strip()
        if got != cp:
            raise SystemExit(f"{name}: metadata says {got!r}, expected {cp}")
        listing = json.loads(fetch(API + q + "/3D", dl / f"{cp}.3d-listing.json"))
        pngs = [e["name"] for e in listing if e.get("name", "").endswith(".png")]
        if len(pngs) != 1:
            raise SystemExit(f"{name}: expected one 3D png, found {pngs}")
        data = fetch(RAW + q + "/3D/" + urllib.parse.quote(pngs[0]), dl / f"{cp}.3d.png")
        w, h, rows = png_decode(data)
        small = downscale(w, h, rows, SIZE)
        (out / f"{cp}.png").write_bytes(png_encode(SIZE, SIZE, small))
        print(f"{cp}.png  <- {name}/3D/{pngs[0]} ({w}x{h})")
    print(f"wrote {len(EMOJI)} emoji to {out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
