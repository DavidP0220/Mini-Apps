"""Badge de SUBSCRIBE para videos largos (1920x1080), adaptado del badge de
Shorts (mismo sistema visual: navy/amarillo/rojo). Se coloca en la esquina
superior derecha para no tapar nunca los subtitulos del tercio inferior."""
from PIL import Image, ImageDraw

from _paths import VE_OUTPUTS, bold_font

NAVY = (13, 27, 42, 255)
YELLOW = (255, 212, 0, 255)
RED = (230, 57, 70, 255)

W, H = 620, 150
OUT = VE_OUTPUTS / "subscribe_badge_long.png"


def rounded(draw, box, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def main():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    rounded(d, (6, 8, W - 2, H - 4), 22, fill=(0, 0, 0, 170))
    rounded(d, (0, 0, W - 8, H - 12), 22, fill=NAVY, outline=YELLOW, width=5)

    f_big = bold_font(52)
    f_small = bold_font(22)

    bx, by = 62, 66
    d.pieslice((bx - 26, by - 34, bx + 26, by + 18), 180, 360, fill=YELLOW)
    d.rectangle((bx - 26, by - 8, bx + 26, by + 16), fill=YELLOW)
    d.rectangle((bx - 34, by + 16, bx + 34, by + 25), fill=YELLOW)
    d.ellipse((bx - 8, by + 25, bx + 8, by + 40), fill=YELLOW)
    d.ellipse((bx - 6, by - 43, bx + 6, by - 31), fill=YELLOW)
    d.ellipse((bx + 15, by - 40, bx + 37, by - 19), fill=RED)

    tx = 108
    d.text((tx + 3, 27), "SUBSCRIBE", font=f_big, fill=(0, 0, 0, 255))
    d.text((tx, 24), "SUBSCRIBE", font=f_big, fill=YELLOW)

    d.line([(tx + 2, 90), (tx + 130, 86), (tx + 260, 91), (tx + 370, 87)],
           fill=RED, width=8, joint="curve")

    d.text((tx + 2, 100), "for more evolutionary psychology", font=f_small, fill=(230, 230, 230, 255))

    img.save(OUT)
    print(f"Badge guardado: {OUT}")


if __name__ == "__main__":
    main()
