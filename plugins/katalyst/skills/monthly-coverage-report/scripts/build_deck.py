#!/usr/bin/env python3
"""Build a Katalyst monthly media report deck from an assembled JSON payload.

    python3 build_deck.py report.json output.pptx

Implements references/deck-spec.md. Slides are dropped when their data is absent;
nothing is padded and no figure is invented here. See the skill for the rules on
media value and on what must be labelled as estimated.
"""

import json
import sys

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

# --- themes -----------------------------------------------------------------
# Add a client by adding a row, using their real brand colours and fonts.
# Do not invent a palette for a luxury account; leave it on katalyst-house.

THEMES = {
    "taj-gold": {
        "match": ["taj", "ihcl", "vivanta", "seleqtions", "gateway"],
        "accent": "B08D57",
        "deep": "8A6D3B",
        "heading": "Trajan Pro",   # licensed Adobe font; substitutes silently if absent
        "body": "Georgia",
    },
    "katalyst-house": {
        "match": [],               # default
        "accent": "A67C52",        # PLACEHOLDER — replace with Katalyst's real brand hex
        "deep": "5C4632",
        "heading": "Georgia",
        "body": "Segoe UI",
    },
}

TEXT = "1A1A1A"
MUTED = "6B6B6B"
BAND = "F5F5F5"
WHITE = "FFFFFF"

W, H = Inches(13.333), Inches(7.5)
L, R = Inches(0.9), Inches(0.9)
TOP, BOT = Inches(0.75), Inches(0.6)
CONTENT_W = W - L - R

MAX_ROWS_PER_LOG_SLIDE = 8


def rgb(h):
    return RGBColor.from_string(h)


def pick_theme(client):
    low = (client or "").lower()
    for name, t in THEMES.items():
        if any(m in low for m in t["match"]):
            return t
    return THEMES["katalyst-house"]


def money(n):
    """Indian grouping: 5,25,000 rather than 525,000."""
    try:
        n = int(round(float(n)))
    except (TypeError, ValueError):
        return str(n)
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return ("-" if n < 0 else "") + s


class Deck:
    def __init__(self, client, month_label, theme):
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = W, H
        self.client = client
        self.month = month_label
        self.t = theme
        self.n = 0

    # -- primitives ---------------------------------------------------------
    def _blank(self):
        s = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        bg = s.background.fill
        bg.solid()
        bg.fore_color.rgb = rgb(WHITE)
        return s

    def _text(self, s, x, y, w, h, txt, size, color, font, bold=False,
              align=PP_ALIGN.LEFT, spacing=1.35, anchor=MSO_ANCHOR.TOP):
        box = s.shapes.add_textbox(x, y, w, h)
        tf = box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        lines = txt if isinstance(txt, (list, tuple)) else [txt]
        for i, line in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            p.line_spacing = spacing
            if i:
                p.space_before = Pt(6)
            r = p.add_run()
            r.text = str(line)
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.name = font
            r.font.color.rgb = rgb(color)
        return box

    def _rule(self, s, x, y, w, color, pt=2):
        bar = s.shapes.add_shape(1, x, y, w, Pt(pt))  # 1 = rectangle
        bar.fill.solid()
        bar.fill.fore_color.rgb = rgb(color)
        bar.line.fill.background()
        bar.shadow.inherit = False
        return bar

    def _footer(self, s):
        self.n += 1
        self._text(s, L, H - BOT, Inches(7), Inches(0.3),
                   f"{self.client}  ·  {self.month}", 8, MUTED, self.t["body"])
        self._text(s, W - R - Inches(1), H - BOT, Inches(1), Inches(0.3),
                   str(self.n), 8, MUTED, self.t["body"], align=PP_ALIGN.RIGHT)

    def slide(self, title):
        s = self._blank()
        self._text(s, L, TOP, CONTENT_W, Inches(0.6), title, 28,
                   self.t["deep"], self.t["heading"])
        self._rule(s, L, TOP + Inches(0.62), CONTENT_W // 3, self.t["accent"])
        self._footer(s)
        return s, TOP + Inches(1.05)

    # -- slides -------------------------------------------------------------
    def cover(self):
        s = self._blank()
        self._rule(s, L, Inches(2.55), Inches(1.6), self.t["accent"], pt=3)
        self._text(s, L, Inches(2.9), CONTENT_W, Inches(1.2), self.client, 42,
                   self.t["deep"], self.t["heading"])
        self._text(s, L, Inches(4.15), CONTENT_W, Inches(0.5),
                   "Monthly Media Report", 20, TEXT, self.t["body"])
        self._text(s, L, Inches(4.7), CONTENT_W, Inches(0.4), self.month, 16,
                   MUTED, self.t["body"])
        self._text(s, L, H - Inches(1.1), CONTENT_W, Inches(0.4),
                   "Prepared by Katalyst Reputation Management", 11, MUTED,
                   self.t["body"])
        self.n += 1

    def contents(self, items):
        """Two columns past nine entries. A single column of eleven runs into the
        footer, which is how a contents slide silently loses its last section."""
        s, y = self.slide("Contents")
        y += Inches(0.15)
        avail = H - BOT - y - Inches(0.2)
        if len(items) <= 9:
            lines = [f"{i:02d}      {t}" for i, t in enumerate(items, start=1)]
            self._text(s, L, y, CONTENT_W, avail, lines, 13, TEXT,
                       self.t["body"], spacing=1.85)
            return
        half = -(-len(items) // 2)
        colw = CONTENT_W // 2
        for c, chunk in enumerate((items[:half], items[half:])):
            start = 1 if c == 0 else half + 1
            lines = [f"{i:02d}      {t}" for i, t in enumerate(chunk, start=start)]
            self._text(s, L + colw * c, y, colw - Inches(0.4), avail, lines, 13,
                       TEXT, self.t["body"], spacing=1.85)

    def prose(self, title, lines, lead=None):
        s, y = self.slide(title)
        if lead:
            self._text(s, L, y, CONTENT_W, Inches(0.6), lead, 16,
                       self.t["deep"], self.t["body"])
            y += Inches(0.75)
        self._text(s, L, y, CONTENT_W, Inches(4.2),
                   lines or ["Not reported this month."], 14, TEXT,
                   self.t["body"], spacing=1.5)

    def figures(self, title, pairs):
        """Four columns. The figure size steps down with its length: "Rs. 7,25,000"
        at 40pt wraps onto a second line and collides with the label beneath it,
        so a big media-value month would otherwise break this slide."""
        s, y = self.slide(title)
        n = max(len(pairs), 1)
        colw = CONTENT_W // n
        sizes = [len(str(v)) for v, _ in pairs]
        longest = max(sizes) if sizes else 0
        size = 40 if longest <= 7 else 32 if longest <= 10 else 26 if longest <= 14 else 21
        for i, (value, label) in enumerate(pairs):
            x = L + colw * i
            self._text(s, x, y + Inches(0.55), colw - Inches(0.25), Inches(1.1),
                       str(value), size, self.t["accent"], self.t["heading"],
                       anchor=MSO_ANCHOR.BOTTOM)
            self._text(s, x, y + Inches(1.78), colw - Inches(0.25), Inches(0.8),
                       label, 11, MUTED, self.t["body"], spacing=1.2)

    def chart(self, title, mapping, note=None):
        s, y = self.slide(title)
        data = CategoryChartData()
        data.categories = list(mapping.keys())
        data.add_series("Placements", tuple(mapping.values()))
        gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, L, y,
                                CONTENT_W, Inches(3.9), data)
        ch = gf.chart
        ch.has_legend = False
        ch.has_title = False
        plot = ch.plots[0]
        plot.gap_width = 90
        plot.has_data_labels = True
        dl = plot.data_labels
        dl.font.size = Pt(11)
        dl.font.name = self.t["body"]
        dl.font.color.rgb = rgb(TEXT)
        ser = plot.series[0]
        ser.format.fill.solid()
        ser.format.fill.fore_color.rgb = rgb(self.t["accent"])
        va = ch.value_axis
        va.has_major_gridlines = False
        va.visible = False
        ca = ch.category_axis
        ca.has_major_gridlines = False
        ca.tick_labels.font.size = Pt(11)
        ca.tick_labels.font.name = self.t["body"]
        ca.tick_labels.font.color.rgb = rgb(TEXT)
        if note:
            self._text(s, L, y + Inches(4.0), CONTENT_W, Inches(0.5), note, 10,
                       MUTED, self.t["body"])

    def table(self, title, headers, rows, widths, note=None):
        s, y = self.slide(title)
        shape = s.shapes.add_table(len(rows) + 1, len(headers), L, y,
                                   CONTENT_W, Inches(0.42) * (len(rows) + 1))
        tbl = shape.table
        tbl.first_row = True
        total = sum(widths)
        for i, frac in enumerate(widths):
            tbl.columns[i].width = Emu(int(CONTENT_W * frac / total))
        for c, head in enumerate(headers):
            cell = tbl.cell(0, c)
            cell.text = head
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(self.t["deep"])
            p = cell.text_frame.paragraphs[0]
            p.runs[0].font.size = Pt(10)
            p.runs[0].font.bold = True
            p.runs[0].font.name = self.t["body"]
            p.runs[0].font.color.rgb = rgb(WHITE)
        for r, row in enumerate(rows, start=1):
            for c, val in enumerate(row):
                cell = tbl.cell(r, c)
                cell.text = "" if val is None else str(val)
                cell.fill.solid()
                cell.fill.fore_color.rgb = rgb(BAND if r % 2 == 0 else WHITE)
                p = cell.text_frame.paragraphs[0]
                if not p.runs:
                    p.add_run().text = ""
                p.runs[0].font.size = Pt(10)
                p.runs[0].font.name = self.t["body"]
                p.runs[0].font.color.rgb = rgb(TEXT)
        if note:
            self._text(s, L, y + Inches(0.42) * (len(rows) + 1) + Inches(0.2),
                       CONTENT_W, Inches(0.6), note, 10, MUTED, self.t["body"])

    def value(self, total, breakdown, note):
        s, y = self.slide("Estimated media value")
        self._text(s, L, y, CONTENT_W, Inches(1.0), f"Rs. {money(total)}", 48,
                   self.t["accent"], self.t["heading"])
        rows = [(k, str(v)) for k, v in breakdown.items()]
        lines = [f"{k}    —    {v}" for k, v in rows]
        self._text(s, L, y + Inches(1.15), CONTENT_W, Inches(1.8), lines, 13,
                   TEXT, self.t["body"], spacing=1.6)
        caveat = ("Estimated media value, calculated on an internal rate-card benchmark. "
                  "AMEC and PRSA both consider advertising-value equivalents unsupported "
                  "by research; treat this as directional, not as a valuation.")
        cy = H - BOT - Inches(1.25)
        self._rule(s, L, cy - Inches(0.14), CONTENT_W, self.t["accent"], pt=1)
        self._text(s, L, cy, CONTENT_W, Inches(0.9), caveat, 11, MUTED,
                   self.t["body"], spacing=1.35)
        if note:
            self._text(s, L, cy - Inches(0.55), CONTENT_W, Inches(0.4), note, 10,
                       MUTED, self.t["body"])

    def closing(self):
        s = self._blank()
        self._rule(s, L, Inches(3.1), Inches(1.6), self.t["accent"], pt=3)
        self._text(s, L, Inches(3.45), CONTENT_W, Inches(0.9), "Thank you", 36,
                   self.t["deep"], self.t["heading"])
        self._text(s, L, Inches(4.5), CONTENT_W, Inches(1.0),
                   ["Katalyst Reputation Management",
                    "nikhila@katalystrm.com  ·  katalystrm.com"],
                   13, MUTED, self.t["body"], spacing=1.5)
        self.n += 1

    def save(self, path):
        self.prs.save(path)


def truncate(s, n):
    s = "" if s is None else str(s)
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def build(d, out):
    client = d["client"]
    month = d["month_label"]
    deck = Deck(client, month, pick_theme(client))

    m = d.get("metrics", {})
    coverage = d.get("coverage", []) or []
    social = d.get("social", {}) or {}
    has_social = any(v for v in social.values())

    # Work out the contents list from what will actually be built.
    toc = ["Executive summary", "The month at a glance"]
    if len(coverage) >= 3:
        toc += ["Coverage by tier", "Coverage by placement type"]
    if len(d.get("by_month", {})) > 1:
        toc.append("Month on month")
    if d.get("headlines"):
        toc.append("Headline placements")
    if coverage:
        toc.append("Coverage log")
    if len(d.get("publications", [])) >= 3:
        toc.append("Where we landed")
    toc.append("Estimated media value")
    if has_social:
        toc.append("Social performance")
    if d.get("top_posts"):
        toc.append("Top posts of the month")
    if d.get("activity"):
        toc.append("Campaign and activity")
    toc += ["Observations", "Next month"]

    deck.cover()
    deck.contents(toc)
    deck.prose("Executive summary", d.get("summary"))

    deck.figures("The month at a glance", [
        (m.get("placements", 0), "Placements"),
        (m.get("publications", 0), "Publications reached"),
        (m.get("tier1", 0), "Tier 1 placements"),
        ("Rs. " + money(m.get("media_value", 0)), "Estimated media value"),
    ])

    if len(coverage) >= 3:
        if d.get("by_tier"):
            deck.chart("Coverage by tier", d["by_tier"])
        if d.get("by_type"):
            deck.chart("Coverage by placement type", d["by_type"])

    if len(d.get("by_month", {})) > 1:
        deck.chart("Month on month", d["by_month"],
                   note="Placements logged per month. Earlier months may be incomplete "
                        "where the tracker was not yet running.")

    if d.get("headlines"):
        rows = [[h.get("date", ""), truncate(h.get("publication"), 30),
                 h.get("tier", ""), truncate(h.get("topic"), 70)]
                for h in d["headlines"][:3]]
        deck.table("Headline placements", ["Date", "Publication", "Tier", "Story"],
                   rows, [0.13, 0.24, 0.11, 0.52])

    for i in range(0, len(coverage), MAX_ROWS_PER_LOG_SLIDE):
        chunk = coverage[i:i + MAX_ROWS_PER_LOG_SLIDE]
        part = ""
        if len(coverage) > MAX_ROWS_PER_LOG_SLIDE:
            part = f" ({i // MAX_ROWS_PER_LOG_SLIDE + 1} of " \
                   f"{-(-len(coverage) // MAX_ROWS_PER_LOG_SLIDE)})"
        rows = [[c.get("date", ""), truncate(c.get("publication"), 26),
                 c.get("tier", ""), c.get("type", ""),
                 truncate(c.get("topic"), 58),
                 money(c["value"]) if c.get("value") else ""] for c in chunk]
        deck.table("Coverage log" + part,
                   ["Date", "Publication", "Tier", "Type", "Story", "Value (Rs.)"],
                   rows, [0.12, 0.20, 0.09, 0.10, 0.37, 0.12])

    pubs = d.get("publications", [])
    if len(pubs) >= 3:
        # Paginate. Truncating here drops publications the client was told about
        # in the log two slides earlier, which reads as an error rather than a cap.
        rows = [[truncate(p.get("name"), 46), p.get("tier", ""), p.get("count", "")]
                for p in pubs]
        pages = -(-len(rows) // MAX_ROWS_PER_LOG_SLIDE)
        for i in range(0, len(rows), MAX_ROWS_PER_LOG_SLIDE):
            part = f" ({i // MAX_ROWS_PER_LOG_SLIDE + 1} of {pages})" if pages > 1 else ""
            deck.table("Where we landed" + part,
                       ["Publication", "Tier", "Placements"],
                       rows[i:i + MAX_ROWS_PER_LOG_SLIDE], [0.62, 0.20, 0.18])

    deck.value(m.get("media_value", 0), d.get("value_breakdown", {}),
               d.get("value_note"))

    if has_social:
        lines = []
        for channel, stats in social.items():
            if not stats:
                continue
            lines.append(channel.title())
            lines += [f"    {k}    —    {v}" for k, v in stats.items()]
        deck.prose("Social performance", lines)

    if d.get("top_posts"):
        rows = [[truncate(p.get("post"), 44), p.get("format", ""),
                 p.get("reach", ""), p.get("engagement", ""),
                 truncate(p.get("why"), 34)] for p in d["top_posts"][:3]]
        deck.table("Top posts of the month",
                   ["Post", "Format", "Reach", "Engagement", "Why it worked"],
                   rows, [0.34, 0.12, 0.13, 0.15, 0.26])

    if d.get("activity"):
        lines = []
        for head, items in d["activity"].items():
            if not items:
                continue
            lines.append(head)
            lines += [f"    {i}" for i in items]
        deck.prose("Campaign and activity", lines)

    deck.prose("Observations", d.get("observations"))
    deck.prose("Next month", d.get("next_month"))
    deck.closing()
    deck.save(out)
    return deck.n


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: build_deck.py <report.json> <output.pptx>")
    with open(sys.argv[1]) as fh:
        payload = json.load(fh)
    count = build(payload, sys.argv[2])
    print(f"{sys.argv[2]} — {count} slides")
