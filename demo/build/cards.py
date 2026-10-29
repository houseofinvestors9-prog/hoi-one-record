from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
HN = "/System/Library/Fonts/HelveticaNeue.ttc"
MN = "/System/Library/Fonts/Menlo.ttc"

INK = (20, 27, 45)
PAPER = (246, 244, 240)
ON_BAND = (242, 239, 233)
MUTED_D = (157, 152, 136)
MUTED_L = (103, 99, 106)
BRONZE = (138, 106, 60)
RULE_L = (223, 219, 211)

M = 150  # side margin


def f(size, idx=0):
    return ImageFont.truetype(HN, size, index=idx)


def mono(size, idx=1):
    return ImageFont.truetype(MN, size, index=idx)


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def base(dark=True):
    img = Image.new("RGB", (W, H), INK if dark else PAPER)
    d = ImageDraw.Draw(img)
    # house mark: short bronze rule top left
    d.rectangle([M, 96, M + 86, 101], fill=BRONZE)
    # footer
    fm = mono(21, 0)
    d.text((M, H - 92), "HOUSE OF INVESTORS   ·   ONE RECORD FOR ONE FAMILY",
           font=fm, fill=MUTED_D if dark else MUTED_L)
    return img, d


def label(d, text, dark=True, y=150):
    d.text((M, y), text.upper(), font=mono(24, 1), fill=BRONZE)


def statement(path, text, lab=None, size=92, sub=None):
    img, d = base()
    y = 150
    if lab:
        label(d, lab, y=y)
        y += 60
    fo = f(size, 1)
    lines = wrap(d, text, fo, W - 2 * M - 120)
    lh = int(size * 1.22)
    block = len(lines) * lh
    y = max(y + 70, (H - block) // 2 - 20)
    for ln in lines:
        d.text((M, y), ln, font=fo, fill=ON_BAND)
        y += lh
    if sub:
        y += 34
        fs = f(40, 0)
        for ln in wrap(d, sub, fs, W - 2 * M - 120):
            d.text((M, y), ln, font=fs, fill=MUTED_D)
            y += 54
    img.save(path)


def lines_card(path, head, items, lab=None):
    img, d = base()
    y = 150
    if lab:
        label(d, lab, y=y)
        y += 66
    fh = f(72, 1)
    for ln in wrap(d, head, fh, W - 2 * M - 120):
        d.text((M, y), ln, font=fh, fill=ON_BAND)
        y += 86
    y += 46
    fi = f(44, 0)
    for it in items:
        d.rectangle([M, y + 22, M + 34, y + 25], fill=BRONZE)
        for k, ln in enumerate(wrap(d, it, fi, W - 2 * M - 200)):
            d.text((M + 68, y), ln, font=fi, fill=ON_BAND)
            y += 58
        y += 20
    img.save(path)


def number(path, num, lab, note=None):
    img, d = base()
    label(d, lab, y=150)
    fn = ImageFont.truetype(HN, 300, index=9)  # Condensed Black
    bb = d.textbbox((0, 0), num, font=fn)
    y = (H - (bb[3] - bb[1])) // 2 - 70
    d.text((M, y), num, font=fn, fill=ON_BAND)
    yy = y + (bb[3] - bb[1]) + 80
    d.rectangle([M, yy, M + 120, yy + 4], fill=BRONZE)
    if note:
        d.text((M, yy + 44), note, font=f(38, 0), fill=MUTED_D)
    img.save(path)


def slate(path, n, title, items, dur):
    img, d = base(dark=False)
    d.text((M, 150), f"SCREEN CAPTURE {n} OF 3   ·   HOLD {dur}",
           font=mono(24, 1), fill=BRONZE)
    fh = f(76, 1)
    y = 236
    for ln in wrap(d, title, fh, W - 2 * M - 120):
        d.text((M, y), ln, font=fh, fill=INK)
        y += 92
    y += 40
    fi = f(42, 0)
    for it in items:
        d.rectangle([M, y + 20, M + 30, y + 23], fill=BRONZE)
        for k, ln in enumerate(wrap(d, it, fi, W - 2 * M - 200)):
            d.text((M + 62, y), ln, font=fi, fill=INK)
            y += 56
        y += 16
    d.rectangle([M, H - 206, W - M, H - 203], fill=RULE_L)
    d.text((M, H - 180), "BLUR OR REPLACE EVERY REAL NAME AND PHONE NUMBER BEFORE RECORDING.",
           font=mono(23, 1), fill=BRONZE)
    img.save(path)


def endcard(path):
    img, d = base()
    fo = f(100, 1)
    y = 400
    d.text((M, y), "One record for one family.", font=fo, fill=ON_BAND)
    d.text((M, y + 128), "So nobody asks the same", font=fo, fill=BRONZE)
    d.text((M, y + 128 + 118), "question twice.", font=fo, fill=BRONZE)
    img.save(path)


def stack(path, lines, accent_from=None, size=110):
    img, d = base()
    fo = f(size, 1)
    lh = int(size * 1.26)
    y = (H - len(lines) * lh) // 2 - 20
    for i, ln in enumerate(lines):
        hot = accent_from is not None and i >= accent_from
        d.text((M, y), ln, font=fo, fill=BRONZE if hot else ON_BAND)
        y += lh
    img.save(path)


C = "cards/"

stack(C + "c0a.png", ["Two firms.", "The same buyer.", "One commission."], size=124)

stack(C + "c0b.png",
      ["That fight used to happen", "on WhatsApp.", "Nobody wrote down who won."],
      accent_from=2, size=94)

statement(C + "c1a.png",
          "A family in Hyderabad decides to buy a flat.",
          sub="Two or three partner firms. A sales executive at every project. "
              "A site executive at the flat. Someone from the builder's office. "
              "Every one of them keeps a list of their own.")

lines_card(C + "c1b.png", "By the third call, nobody is winning.", [
    "The family has stopped answering properly.",
    "The builder, who pays for the ads and owns the flats, asks somebody for a sheet to find out how his own project sold this week.",
])

statement(C + "c2a.png",
          "There is no common record of that family anywhere.",
          sub="Most of these people already have a CRM and use it properly. "
              "There is just nothing for the work to add up against.")

statement(C + "c2b.png", "So we gave the family one.", size=110)

slate(C + "s3.png", 1, "One family record in the Lead Engine", [
    "Open a single record and scroll it slowly.",
    "Hold on client_id. It is the hero of the shot.",
    "Show: source and ad creative, calls, site visit, stated budget vs revealed, cheque, booking.",
    "End on project_history, the second property eighteen months later.",
], "25.6s")

slate(C + "s4.png", 2, "Attribution: duplicate, contested, audit log", [
    "A lead marked duplicate. Show attribution_status and attribution_until.",
    "A lead marked contested, then its AuditLog entry.",
    "Show that AuditLog has no edit and no delete control, for any role.",
], "25.8s")

slate(C + "s5.png", 3, "hyderabad.properties and the review desk", [
    "Search a project. Open its report.",
    "Show the source list and the document dates.",
    "Then the review desk with a verdict waiting for a person to approve.",
], "26.5s")

number(C + "n1.png", "9,100", "families on one record", "Lead.client_id, issued once, never reused")
number(C + "n2.png", "6,415", "pulled out of spreadsheets", "One backfill, 6 October 2026")
number(C + "n3.png", "30,000", "contacts logged against them", "to 40,000. Counted by offset probe, not estimated")
number(C + "n4.png", "27", "people using it every working day", "Attendance punches, last 23 days")
number(C + "n5.png", "74", "bookings closed on it", "Booking records with a cheque attached")

statement(C + "c7a.png",
          "Not measured yet: the minutes this saves per family.",
          sub="I know the method. It takes an afternoon. It is the next thing I do.")

lines_card(C + "c7b.png", "What I can show today.", [
    "6,415 families who used to be rows in a spreadsheet now have one record each.",
    "234 firms that compete with each other work against it.",
    "The commission fight that used to happen on WhatsApp is now a decision with a log.",
])

endcard(C + "end.png")
print("cards written")
