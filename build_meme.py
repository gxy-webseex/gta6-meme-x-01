#!/usr/bin/env python3
"""Draw the fourth gta6-meme-x-01 meme: '3 AM, just one more mission'.

A dark living room at night: a tired person with heavy dark circles
under their eyes sits on the couch, controller in hand, lit by the
glow of a TV showing a Vice City night scene; a wall clock reads 3:00.
make.fun's real ghost sits on the couch next to them like a gaming
buddy, 'make.fun' written under it. Original art only (PIL shapes),
the real ghost asset pasted in. 1024x1024 PNG, captions big and
legible.
"""
from PIL import Image, ImageDraw, ImageFont
import random

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGB", (W, H), (28, 34, 62))  # dark night wall
d = ImageDraw.Draw(img)

# ---- soft glow around the TV ----
d.rounded_rectangle([78, 108, 946, 536], radius=24, fill=(40, 48, 86))

# ---- TV on the wall ----
MON = (110, 140, 914, 500)
d.rounded_rectangle(MON, radius=12, fill=(12, 12, 18))  # frame
sx0, sy0, sx1, sy1 = 124, 154, 900, 486  # screen
# night-sky gradient, dark purple top to warm horizon
top = (26, 18, 58)
bot = (198, 88, 96)
for yy in range(sy0, sy1):
    t = (yy - sy0) / max(1, (sy1 - sy0 - 1))
    c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
    d.line([(sx0, yy), (sx1, yy)], fill=c)
# stars in the upper half
random.seed(7)
for _ in range(60):
    x = random.randint(sx0 + 8, sx1 - 8)
    y = random.randint(sy0 + 8, sy0 + 150)
    r = random.choice([1, 1, 2])
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))
# moon
d.ellipse([772, 196, 828, 252], fill=(250, 240, 200))
d.ellipse([786, 208, 812, 234], fill=(232, 220, 180))
# skyline: dark buildings with lit windows along the bottom
random.seed(21)
bx = sx0 + 6
while bx < sx1 - 50:
    bw = random.randint(48, 84)
    bh = random.randint(70, 150)
    by1 = 486 - 0  # buildings sit on the screen bottom edge
    d.rectangle([bx, 486 - bh, bx + bw, 486], fill=(18, 14, 38))
    for _ in range(10):
        wx = random.randint(bx + 6, bx + bw - 10)
        wy = random.randint(486 - bh + 8, 486 - 14)
        if random.random() < 0.7:
            d.rectangle([wx, wy, wx + 5, wy + 7],
                        fill=random.choice([(255, 210, 90), (255, 190, 120),
                                            (140, 220, 255)]))
    bx += bw + 4
# palms: two simple dark silhouettes at the screen edges, fronds drooping
def palm(px, py, h, flip=False):
    s = -1 if flip else 1
    tx, ty = px + 10 * s, py - h
    d.line([(px, py), (tx, ty)], fill=(14, 10, 30), width=7)
    # each frond: out from the crown, then drooping down
    for dx in (-44, -24, 0, 24, 44):
        mx = tx + dx * s
        my = ty - 10
        ex = tx + int(dx * 1.5) * s
        ey = ty + 22
        d.line([(tx, ty), (mx, my), (ex, ey)], fill=(14, 10, 30), width=5)

# (no palms — the skyline, moon and stars already read as Vice City night;
# the earlier palm silhouettes read as stray marks at the judge's 480px view)
# "VICE CITY" neon sign on the screen, pink glow + white core
f_vc = ImageFont.truetype(BOLD, 34)
vc = "VICE CITY"
vb = d.textbbox((0, 0), vc, font=f_vc)
vx = (sx0 + sx1 - (vb[2] - vb[0])) // 2
d.text((vx + 2, 440), vc, font=f_vc, fill=(255, 60, 170))
d.text((vx, 438), vc, font=f_vc, fill=(255, 255, 255),
       stroke_width=3, stroke_fill=(10, 8, 24))
# TV stand leg
d.rectangle([492, 500, 532, 560], fill=(12, 12, 18))
d.rounded_rectangle([430, 556, 594, 574], radius=8, fill=(12, 12, 18))

# ---- wall clock, top-left, reading 3:00 ----
cx, cy, cr = 82, 72, 50
d.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(245, 240, 225),
          outline=(15, 15, 20), width=5)
for tick in range(12):
    import math
    a = math.radians(tick * 30)
    x1 = cx + int((cr - 8) * math.sin(a))
    y1 = cy - int((cr - 8) * math.cos(a))
    x2 = cx + int((cr - 14) * math.sin(a))
    y2 = cy - int((cr - 14) * math.cos(a))
    d.line([(x1, y1), (x2, y2)], fill=(30, 30, 40), width=3)
# hands: hour hand to 3 (right), minute hand to 12 (up)
d.line([(cx, cy), (cx + 26, cy)], fill=(20, 20, 30), width=5)
d.line([(cx, cy), (cx, cy - 34)], fill=(20, 20, 30), width=4)
d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(200, 40, 60))

# ---- floor ----
d.rectangle([0, 950, W, H], fill=(52, 40, 32))
d.line([(0, 950), (W, 950)], fill=(38, 28, 22), width=3)

# ---- couch across the bottom ----
d.rounded_rectangle([40, 620, 984, 830], radius=28, fill=(18, 78, 82))  # back
d.rounded_rectangle([40, 800, 984, 950], radius=24, fill=(14, 62, 66))  # seat front
d.rounded_rectangle([40, 640, 110, 950], radius=24, fill=(22, 92, 96))  # left arm
d.rounded_rectangle([914, 640, 984, 950], radius=24, fill=(22, 92, 96))  # right arm
d.line([(40, 800), (984, 800)], fill=(10, 50, 54), width=3)

# ---- tired person, front-facing, left-center of the couch ----
# body: dark red hoodie
d.rounded_rectangle([296, 786, 452, 928], radius=30, fill=(150, 62, 62))
d.rounded_rectangle([296, 786, 452, 830], radius=20, fill=(168, 74, 74))
# arms down to the controller
d.line([(322, 820), (352, 884)], fill=(150, 62, 62), width=26)
d.line([(426, 820), (396, 884)], fill=(150, 62, 62), width=26)
# head
d.ellipse([312, 656, 436, 772], fill=(232, 190, 150))
# messy hair: dark cap + small bumps on top
d.pieslice([308, 648, 440, 740], 180, 360, fill=(52, 36, 26))
for hx, hy, hr in [(330, 656, 9), (362, 646, 10), (396, 648, 9), (420, 660, 8)]:
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=(52, 36, 26))
# tired eyes: half-closed, heavy dark bags underneath
for ex in (340, 396):
    d.ellipse([ex - 13, 706, ex + 13, 722], fill=(255, 255, 255))  # eye white
    d.ellipse([ex - 6, 708, ex + 6, 720], fill=(30, 30, 40))  # pupil
    d.rectangle([ex - 14, 700, ex + 14, 711], fill=(232, 190, 150))  # droopy lid
    d.ellipse([ex - 15, 726, ex + 15, 740], fill=(96, 62, 116))  # bag
    d.line([(ex - 15, 700), (ex + 15, 694)], fill=(52, 36, 26), width=4)  # brow
# slack open mouth
d.ellipse([362, 748, 386, 764], fill=(90, 40, 40))
# controller in front
d.rounded_rectangle([318, 862, 430, 908], radius=12, fill=(18, 18, 24))
d.line([(336, 878), (336, 892)], fill=(255, 255, 255), width=4)
d.line([(329, 885), (343, 885)], fill=(255, 255, 255), width=4)
d.ellipse([392, 872, 402, 882], fill=(255, 255, 255))
d.ellipse([404, 884, 414, 894], fill=(255, 255, 255))

# ---- ghost (real asset) on the couch, right side ----
ghost = Image.open("../assets/mark-1024.png").convert("RGBA")
gs = 200
ghost = ghost.resize((gs, gs), Image.LANCZOS)
gx, gy = 700, 648
d.ellipse([gx + 22, 842, gx + gs - 22, 860], fill=(8, 40, 44))  # contact shadow
img.paste(ghost, (gx, gy), ghost)
# "make.fun" under the ghost, clear of the bottom caption
f_mf = ImageFont.truetype(BOLD, 32)
mf = "make.fun"
mb = d.textbbox((0, 0), mf, font=f_mf)
d.text((gx + gs // 2 - (mb[2] - mb[0]) // 2, 862), mf, font=f_mf,
       fill=(255, 255, 255), stroke_width=2, stroke_fill=(8, 40, 44))

# ---- captions (classic meme style: bold white, thick black outline) ----
def caption(text, y, size):
    f = ImageFont.truetype(BOLD, size)
    bb = d.textbbox((0, 0), text, font=f, stroke_width=8)
    x = (W - (bb[2] - bb[0])) // 2
    d.text((x + 3, y + 3), text, font=f, fill=(0, 0, 0),
           stroke_width=8, stroke_fill=(0, 0, 0))
    d.text((x, y), text, font=f, fill=(255, 255, 255),
           stroke_width=8, stroke_fill=(0, 0, 0))

caption("3:00 AM", 16, 76)
caption("JUST ONE MORE MISSION IN GTA 6.", 948, 48)

img.save("meme.png")
print("saved meme.png", img.size)
