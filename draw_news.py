#!/usr/bin/env python3
"""Draw the front page for 'The World in One Day' - 24 November 2026.

A newspaper front page: masthead, one lead feature, then five stories in
two columns. Drawn with PIL only, no network, deterministic output.
Run:  python3 draw_news.py   ->  writes news.png (1024x1024) next to it.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 46
INK = (18, 24, 38)          # deep navy ink
RED = (178, 34, 28)         # accent red
PAPER = (248, 244, 234)     # warm paper
TINT = (236, 230, 214)      # lead feature tint
GREY = (92, 96, 104)
RULE = (150, 146, 132)

FONT_DIR = "/usr/share/fonts/truetype/noto/"
SERIF_BLACK = FONT_DIR + "NotoSerifDisplay-Black.ttf"
SERIF_BOLD = FONT_DIR + "NotoSerif-Bold.ttf"
SERIF = FONT_DIR + "NotoSerif-Regular.ttf"
SERIF_IT = FONT_DIR + "NotoSerif-Italic.ttf"
SANS = FONT_DIR + "NotoSans-Regular.ttf"
SANS_BOLD = FONT_DIR + "NotoSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width` pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def story_card(draw, x, y, width, kicker, headline, summary,
               head_size=26, head_lead=31, body_size=18, body_lead=23,
               head_max=2, body_max=3):
    """One story: red kicker, serif headline, sans summary. Returns bottom y."""
    f_kick = font(SANS_BOLD, 15)
    f_head = font(SERIF_BOLD, head_size)
    f_body = font(SANS, body_size)
    draw.text((x, y), kicker, font=f_kick, fill=RED)
    y += 22
    head_lines = wrap(draw, headline, f_head, width)[:head_max]
    y = text_block(draw, x, y, head_lines, f_head, INK, head_lead)
    y += 5
    body_lines = wrap(draw, summary, f_body, width)[:body_max]
    y = text_block(draw, x, y, body_lines, f_body, (58, 62, 72), body_lead)
    return y


STORIES = [
    # kicker, headline, summary
    ("EUROPE  ·  SECURITY",
     "NATO sends early-warning jets to Poland",
     "NATO will deploy an AWACS surveillance aircraft to Poland after three "
     "Russian Kh-101 missiles landed there on Friday. A Russian drone also "
     "briefly crossed Polish airspace."),
    ("WAR  ·  LIBYA",
     "Ukraine sinks Russian warship off Libya",
     "Ukrainian drones sink the Russian corvette Merkury in Benghazi port, "
     "Kyiv says — a day after a strike on a Russian-linked cargo ship in "
     "the Gulf of Finland."),
    ("ASIA  ·  SECURITY",
     "Russian jet triggers evacuation alert in South Korea",
     "South Korea briefly orders residents of Ulleung island to evacuate "
     "after a Russian aircraft enters its airspace. The warning is lifted "
     "three minutes later."),
    ("TECH  ·  UNITED STATES",
     "Huang returns as Nvidia chief",
     "Jensen Huang walks back into Nvidia headquarters to applause after the "
     "board reinstates him as CEO. Shares jumped more than 31% in a day."),
    ("AMERICAS  ·  ENERGY",
     "US details $12bn in Venezuelan oil revenue",
     "The State Department publishes a 53-page report on more than $12bn in "
     "revenue from Venezuelan oil and minerals, nearly a year after US "
     "forces captured Nicolas Maduro."),
]

LEAD = ("CLIMATE  ·  ANTALYA, TURKEY",
        "Climate talks collapse with no deal",
        "UN climate talks in Turkey end without any agreement — the first COP "
        "to fail since Copenhagen in 2009 — after the EU rejects a final text "
        "with no mention of fossil fuels. Pacific island nations call the "
        "outcome despair, and the blame game begins.")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    y = 34
    f_title = font(SERIF_BLACK, 66)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, y), title, font=f_title, fill=INK)
    y += 84
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=3)
    y += 8
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=1)
    y += 12
    f_date = font(SANS_BOLD, 21)
    f_tag = font(SERIF_IT, 20)
    d.text((MARGIN, y), "TUESDAY, 24 NOVEMBER 2026", font=f_date, fill=INK)
    tag = "Six stories that defined the day"
    d.text((W - MARGIN - d.textlength(tag, font=f_tag), y), tag,
           font=f_tag, fill=GREY)
    y += 34
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=1)
    y += 14

    # ---- lead feature ----
    lead_top = y
    lead_h = 196
    d.rectangle([MARGIN, lead_top, W - MARGIN, lead_top + lead_h], fill=TINT)
    lx = MARGIN + 22
    lw = W - 2 * MARGIN - 44
    ly = lead_top + 14
    f_kick = font(SANS_BOLD, 16)
    d.text((lx, ly), LEAD[0], font=f_kick, fill=RED)
    ly += 26
    f_head = font(SERIF_BLACK, 42)
    head_lines = wrap(d, LEAD[1], f_head, lw)[:2]
    ly = text_block(d, lx, ly, head_lines, f_head, INK, 48)
    ly += 6
    f_body = font(SANS, 20)
    body_lines = wrap(d, LEAD[2], f_body, lw)[:3]
    ly = text_block(d, lx, ly, body_lines, f_body, (58, 62, 72), 26)
    y = lead_top + lead_h + 16
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=2)
    y += 14

    # ---- five stories, two columns: 3 left, 2 right ----
    col_w = (W - 2 * MARGIN - 36) // 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 36
    col_top = y

    # left column: stories 0,1,2
    ly = col_top
    for i in (0, 1, 2):
        k, h, s = STORIES[i]
        ly = story_card(d, left_x, ly, col_w, k, h, s)
        if i < 2:
            ly += 8
            d.line([(left_x, ly), (left_x + col_w, ly)], fill=RULE, width=1)
            ly += 12
    left_bottom = ly

    # right column: stories 3,4 (taller cards, roomier summaries)
    ry = col_top
    for i in (3, 4):
        k, h, s = STORIES[i]
        ry = story_card(d, right_x, ry, col_w, k, h, s,
                        head_size=27, head_lead=32, body_max=4)
        if i == 3:
            ry += 8
            d.line([(right_x, ry), (right_x + col_w, ry)], fill=RULE, width=1)
            ry += 12
    right_bottom = ry

    bottom = max(left_bottom, right_bottom)
    assert bottom < 928, f"stories overflow: bottom={bottom}"

    # ---- footer ----
    fy = 936
    d.line([(MARGIN, fy), (W - MARGIN, fy)], fill=INK, width=2)
    fy += 12
    f_foot = font(SANS, 15)
    foot1 = ("Sources: Reuters, 24 Nov 2026  ·  Times of India, 24 Nov 2026  ·  "
             "The Paris Eye, 24 Nov 2026")
    d.text((MARGIN, fy), foot1, font=f_foot, fill=GREY)
    fy += 22
    foot2 = ("Every event happened, or was first reported, on 24 November 2026  ·  "
             "make.fun bounty news-image-20261124")
    d.text((MARGIN, fy), foot2, font=f_foot, fill=GREY)

    out = "news.png"
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out}: {img.size}, bottom={bottom}")


if __name__ == "__main__":
    main()
