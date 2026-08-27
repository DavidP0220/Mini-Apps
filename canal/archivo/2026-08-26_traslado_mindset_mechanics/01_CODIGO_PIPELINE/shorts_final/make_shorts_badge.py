"""
Compact SUBSCRIBE badge for vertical Shorts (1080x1920).

Why this exists: as of 2026-08-22 the channel's Shorts had pulled 95 views and
0 subscribers, while long-form pulled 146 views and all 4 subscribers. The best
Short holds 83.8% average retention, so viewers DO reach the end - there was just
nothing there asking them to subscribe. This badge is that ask.

Sizing/placement notes:
- Drawn onto the blurred padding band BELOW the video content (the 1080x1920
  composition centers a 1080x607 video at y=656..1263), so it never covers the
  burned-in captions.
- Kept clear of the Shorts UI: action buttons live on the right edge and the
  title/handle sits in the bottom ~250px.
- ffmpeg's drawtext filter segfaults on this machine (Fontconfig crash), so all
  text is rasterised here with Pillow instead.
"""
from PIL import Image, ImageDraw, ImageFont

NAVY = (13, 27, 42, 255)
YELLOW = (255, 212, 0, 255)
RED = (230, 57, 70, 255)
WHITE = (255, 255, 255, 255)

W, H = 660, 172           # badge canvas
OUT = "subscribe_badge_shorts.png"


def rounded(draw, box, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def main():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # card: black drop shadow, navy body, yellow border
    rounded(d, (6, 10, W - 2, H - 4), 26, fill=(0, 0, 0, 170))
    rounded(d, (0, 0, W - 10, H - 14), 26, fill=NAVY, outline=YELLOW, width=6)

    f_big = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 62)
    f_small = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 26)

    # bell glyph, drawn by hand (no emoji font dependency)
    bx, by = 68, 74
    d.pieslice((bx - 30, by - 40, bx + 30, by + 20), 180, 360, fill=YELLOW)
    d.rectangle((bx - 30, by - 10, bx + 30, by + 18), fill=YELLOW)
    d.rectangle((bx - 40, by + 18, bx + 40, by + 28), fill=YELLOW)
    d.ellipse((bx - 9, by + 28, bx + 9, by + 46), fill=YELLOW)
    d.ellipse((bx - 7, by - 50, bx + 7, by - 36), fill=YELLOW)
    d.ellipse((bx + 18, by - 46, bx + 42, by - 22), fill=RED)  # notification dot

    # wordmark
    tx = 124
    d.text((tx + 3, 31), "SUBSCRIBE", font=f_big, fill=(0, 0, 0, 255))
    d.text((tx, 28), "SUBSCRIBE", font=f_big, fill=YELLOW)

    # hand-drawn red underline accent (matches the thumbnail brand system)
    d.line([(tx + 2, 104), (tx + 150, 99), (tx + 300, 106), (tx + 430, 100)],
           fill=RED, width=9, joint="curve")

    d.text((tx + 2, 116), "MINDSET MECHANICS", font=f_small, fill=WHITE)

    img.save(OUT)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
