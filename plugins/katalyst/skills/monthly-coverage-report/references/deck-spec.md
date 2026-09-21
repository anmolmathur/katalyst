# Deck specification

The eighteen slides, the theme table, and the layout rules. `scripts/build_deck.py` implements
this; read here to change what it produces.

## Themes

One row per client or client family. The builder matches `client` against `match` as a
case-insensitive substring and falls back to `katalyst-house` when nothing matches.

| Theme | Applies to | Accent | Deep | Heading font | Body font |
|---|---|---|---|---|---|
| `taj-gold` | Taj, IHCL, Vivanta, SeleQtions, Gateway, Taj Krishna, Taj Chandigarh | `#B08D57` | `#8A6D3B` | Trajan Pro | Georgia |
| `katalyst-house` | everything else — default | `#A67C52` | `#5C4632` | Georgia | Segoe UI |

Both run on a white ground with near-black text (`#1A1A1A`) and a grey for secondary type
(`#6B6B6B`). Luxury hospitality decks are white and quiet; the accent is used for rules,
figures and headings, never as a fill behind body text.

**Two honest notes on this table.**

*The Katalyst accent is a placeholder.* Their actual brand hex codes are not on file. It is a
warm neutral chosen to be inoffensive next to a luxury client's own branding, and it should be
replaced with the real values the first time anyone has them. It is marked here so that nobody
later mistakes a guess for a brand standard.

*Trajan Pro is a licensed Adobe font.* Naming it in the file does not embed it. On a machine
that has it — hers, since she already produces Taj decks — it renders correctly. Anywhere else
PowerPoint substitutes silently and the deck looks subtly wrong without saying why. If a deck
comes back looking off, this is the first thing to check.

**Adding a client:** add a row to `THEMES` in `build_deck.py` with the client's real brand
colours and fonts, taken from their brand guidelines. Do not invent them — an off-brand deck
sent to a luxury account is a worse outcome than a neutral one.

## The eighteen slides

| # | Slide | Source | When it is dropped |
|---|---|---|---|
| 1 | Cover — client, month, "Monthly Media Report", Katalyst credit | scope | never |
| 2 | Contents | fixed | never |
| 3 | Executive summary — narrative, four to six lines | computed + intake context | never |
| 4 | The month at a glance — four figures | computed | never |
| 5 | Coverage by tier — bar chart | computed | when fewer than 3 placements |
| 6 | Coverage by placement type — bar chart | computed | when fewer than 3 placements |
| 7 | Month on month — placements across recent months | computed | when only one month of data exists |
| 8 | Headline placements — up to three, Tier 1 first | computed | when nothing above Tier 3 |
| 9 | Coverage log, part 1 | computed | never |
| 10 | Coverage log, part 2 | computed | when everything fits on slide 9 |
| 11 | Where we landed — publications reached | computed | when fewer than 3 publications |
| 12 | Estimated media value — with the AVE caveat | computed | never |
| 13 | Social performance — headline metrics | intake | when intake absent |
| 14 | Top posts of the month | intake | when intake absent |
| 15 | Campaign and activity recap | intake | when intake absent |
| 16 | Observations — what worked | intake context | never |
| 17 | Next month — priorities | intake context | never |
| 18 | Closing — Katalyst contact | fixed | never |

Slides are dropped, never padded. A deck of twelve true slides is the right output for a quiet
month; eighteen slides with six hollow ones is not. The contents slide renumbers itself around
whatever was dropped.

## Layout rules

- **16:9**, 13.333 × 7.5 inches.
- **Margins**: 0.9" left and right, 0.75" top, 0.6" bottom. Nothing crosses them.
- **Slide title**: heading font, 28pt, deep accent colour, at the top margin, with a 2pt accent
  rule 0.12" beneath it running to a third of the slide width. That rule is the only decoration
  the deck uses; it is what makes the pages read as one set.
- **Body**: body font, 14pt, near-black, 1.35 line spacing.
- **Figures** (the four on slide 4): heading font, 40pt, accent colour, with a 11pt grey label
  beneath. Four equal columns.
- **Tables**: 10pt body font, header row in the deep accent with white type, banded rows in a
  2% grey. Column widths are fixed in the builder, not auto-fitted — auto-fit produces a
  different deck every month.
- **Charts**: native PowerPoint charts, not images, so she can edit them. Single series, accent
  colour, no gridlines, no legend on a single series, data labels on.
- **Never more than eight rows of coverage on one slide.** Nine is where a 10pt table starts to
  look cramped at the back of a room.
- **Every slide carries the client name and month** in 8pt grey at the bottom left, and the
  slide number bottom right. Decks get separated from their covers.

## Input contract

`build_deck.py` reads one JSON file. Shape:

```json
{
  "client": "The St. Regis Goa Resort",
  "month_label": "August 2026",
  "period": {"start": "2026-08-01", "end": "2026-08-31"},
  "summary": ["line one", "line two"],
  "metrics": {"placements": 7, "publications": 5, "tier1": 2, "media_value": 525000},
  "by_tier": {"Tier 1": 2, "Tier 2": 1, "Tier 3": 4},
  "by_type": {"Feature": 4, "Mention": 2, "Quote": 1},
  "by_month": {"2026-06": 3, "2026-07": 9, "2026-08": 7},
  "headlines": [{"publication": "...", "date": "2026-08-04", "topic": "...", "tier": "Tier 1"}],
  "coverage": [{"date": "...", "publication": "...", "tier": "...", "type": "...",
                "topic": "...", "value": 150000, "link": "..."}],
  "publications": [{"name": "BW Hotelier", "count": 2, "tier": "Tier 2"}],
  "value_note": "3 placements excluded — no tier on file",
  "social": {"instagram": {"Followers": "...", "Reach": "..."}, "facebook": {}},
  "top_posts": [{"post": "...", "format": "Reel", "reach": "...", "engagement": "...",
                 "why": "..."}],
  "activity": {"Releases": ["..."], "Events": ["..."], "Design": ["..."]},
  "observations": ["..."],
  "next_month": ["..."],
  "excluded_note": "…"
}
```

Every key is optional except `client` and `month_label`. A missing key drops its slide; an
empty value renders as `Not reported this month` rather than as a blank space, so that the
absence is visible to whoever reviews the deck.
