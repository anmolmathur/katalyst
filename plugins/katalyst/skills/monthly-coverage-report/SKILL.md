---
name: monthly-coverage-report
description: Build the monthly media report for one Katalyst client — earned PR coverage pulled from the coverage workbook, plus social performance and campaign activity supplied by hand — as an 18-slide PPTX in the client's house style. Use for the month-end client report, a quarterly roll-up, or a one-off report for a launch period.
---

# Monthly coverage report

Builds one client's monthly media report end to end: pulls the earned coverage from the
workbook, takes the numbers that live behind a login from a filled-in intake, and produces an
18-slide PPTX in that client's house style.

**This report goes to a paying luxury client under Nikhila's name. Nothing here auto-sends.**
The run produces a deck and a summary of what is thin or estimated in it; she reviews, edits
and sends. That gate is not negotiable and is not a placeholder for a later automation.

## The two rules that matter most

**One: never sum the `MAV (Rs.)` column.** As of the September 2026 audit, *zero* of the 44
rows in `ALL_COVERAGE` carry a numeric MAV. Thirty-eight hold explanatory text like
`N/A - no public reach/rate data found`, and six are blank. A spreadsheet sum of that column
returns nothing, and a model that skims it and reports "₹0" or invents a plausible total has
put a fabricated number in front of a hotel client. Compute media value from `MAV_RATES`
instead — tier base rate × placement multiplier — as Step 4 sets out, and show the arithmetic.

**Two: an estimated number must be labelled estimated on the slide itself, not in the notes.**
The rate card is a directional benchmark with no published source behind it, and both AMEC and
PRSA hold that AVE multipliers are unsupported by research. The workbook says so; the deck has
to say so too, on the media-value slide, in type the client will actually read. A client who
later learns the ₹ figure was benchmarked from Instagram follower counts and was not flagged
is a reputation problem for the agency — which is the one thing this agency sells.

## Configuration

| Setting | Value |
|---|---|
| Coverage workbook | `Katalyst_PR_Coverage_WORKING` — tab `ALL_COVERAGE` |
| Client roster | Same workbook, tab `CLIENTS` |
| Rate card | Same workbook, tab `MAV_RATES` |
| Intake form | `references/intake-checklist.md` in this skill |
| Deck specification | `references/deck-spec.md` in this skill |
| Builder script | `scripts/build_deck.py` in this skill |
| Output name | `<Client>_<MONTH><YEAR>_MediaReport_v1.pptx` |
| Cadence | Monthly, first week of the following month |

Her existing file naming is `TajChandigarh_AUGUST2026_SocialMediaPlan_v2.pptx`. Match that
shape — no spaces, month in caps, explicit version — so the report files sort alongside the
plan files in the same folder.

## Step 0 — Establish scope before touching data

Confirm three things, and ask if any is unclear rather than guessing:

- **Which client.** One client per deck. A combined deck across a group (Kalra, Dugar, Udeshi)
  is a different deliverable — see the variants at the end.
- **Which month.** Calendar month unless told otherwise. "August" means 2026-08-01 to
  2026-08-31 inclusive.
- **Whether the intake is filled in.** If `references/intake-checklist.md` has not been
  completed for this client and month, say so and offer to build the PR half only. Do not
  invent social numbers, and do not carry forward last month's — a repeated follower count is
  worse than an absent one, because it looks like data.

Read the `CLIENTS` row for the client too. It carries the group, the key people, and the
setup notes naming the venues that belong to the property — Miri, Oliveto, Riverside and
Susegado for St. Regis Goa; Pondichéry Café, Jyran, Tuskers and Artisan Bar for Sofitel
Mumbai BKC. Coverage of a venue is coverage of the client, and the report should name the
venue where the article did.

## Step 1 — Pull the month's coverage

Read `ALL_COVERAGE` and filter to the client and the month. Match `Client` exactly as spelled
in `CLIENTS`; a near-miss spelling silently drops rows.

**Dates are not all clean, and the mess is load-bearing.** The column holds three shapes:

| Shape | Example | How to treat it |
|---|---|---|
| Full date | `2026-07-06` | Normal. |
| Month only | `2026-07` | Belongs to that month. Include it, and flag it in the run summary as undated. |
| Full date with a `Date Note` | `2026-07-06` + `approx` | Include it. If it sits within three days of a month boundary, list it for her to confirm rather than deciding yourself. |

A row assigned to the wrong month is coverage the client never sees, or coverage counted twice
across two reports. When a boundary case is genuinely ambiguous, put it in the deck and say so
in the run summary — visible and flagged beats silently dropped.

**Separate earned social from owned social.** `ALL_COVERAGE` contains rows like
`Grazia India (Instagram)`, `LocalSamosa (Instagram)`, `Soul of Hospitality (Instagram)` and
`LinkedIn (Travel Turtle repost)`. Those are *earned* placements on somebody else's account
and belong in the PR count. They are not the client's own channel performance, which comes
from the intake in Step 3. Never merge the two — doing so double-counts reach and inflates
both halves of the report.

**Normalise publication names for counting, but not for display.** `Hotelier India` and
`Hotelier India (print)` are one publication with two placements; `LocalSamosa` and
`LocalSamosa (Instagram)` likewise. Count them as one outlet in "publications reached", and
show each placement on its own row in the log with its name as written.

If a row reads `Publication TBD (per your image - possibly Grazia)` or similar, do not put a
guess in a client deck. Show it as `Publication to be confirmed` and list it in the run summary
for her to resolve.

## Step 2 — Work out what the month actually looks like

Before building anything, compute and hold these:

- Total placements, and how many distinct publications they represent.
- The split by tier, and by placement type.
- Tier 1 placements listed individually — these are the ones she leads with.
- Which of the client's venues or people were named.
- The same figures for the previous month, for a direction-of-travel line.

**Then judge whether there is a report here at all.** Some clients have one placement in a
month; Paashh, Pali Bhavan and Serious Slice each have exactly one row in the whole workbook.
An 18-slide deck built on one placement is padding, and padding is obvious to a client paying
a retainer. When a client has fewer than three placements in the month, say so plainly and
offer the short form — cover, summary, the coverage itself, activity, next month — six slides
that respect the reader. Ask before building the long form anyway.

The reverse case matters too: a month that looks like a spike is often one wire release picked
up widely. Four PTI pickups of one Sofitel release is four genuine placements and should be
counted as four, but the summary line should say "one release, four pickups" rather than
letting the number stand alone and read as four separate stories.

## Step 3 — Take in the numbers that live behind a login

Meta Business Suite, Instagram and Facebook analytics sit behind her login and are not
reachable from here. That is settled — do not attempt to log in, and do not offer to. Stage 1
is manual by design, and it matches how she already works.

Read the filled-in `references/intake-checklist.md`. It supplies the follower and engagement
figures, the top posts, the campaign activity, and anything client-specific she wants said.

**Use only what she wrote.** Where a field is blank, the corresponding slide says
`Not reported this month` and the run summary lists it. An empty field is a fact about the
month; a filled-in guess is a lie in a client deck. This is the single most likely place for
this skill to go wrong, because the pressure to produce a complete-looking deck is real.

## Step 4 — Compute media value, and caveat it on the slide

Read `MAV_RATES`. As of September 2026 it holds:

| Tier | Base per feature |
|---|---|
| Tier 1 | ₹150,000 |
| Tier 2 | ₹75,000 |
| Tier 3 | ₹25,000 |

Multipliers: Feature 1.0, Mention 0.5, Quote 0.4, Photo Credit 0.25.

Read the live tab rather than trusting these figures — the card is hers to change, and a
hardcoded rate silently goes stale.

For each placement: `base rate for its Tier × multiplier for its Placement Type`. Sum those.
Rows missing a tier or a placement type are excluded from the total and reported as excluded,
with a count — never assumed into a middle tier to make the sum look complete.

The media-value slide carries this sentence, visibly, not in a footnote a reader skips:

> Estimated media value, calculated on an internal rate-card benchmark. AMEC and PRSA both
> consider advertising-value equivalents unsupported by research; treat this as directional,
> not as a valuation.

If she asks to drop that line, that is her call as the agency principal — but it comes out
because she decided, not because the deck quietly omitted it.

## Step 5 — Build the deck

Follow `references/deck-spec.md`. It carries the eighteen-slide map, the per-client theme
table, and the layout rules. Run `scripts/build_deck.py` with the assembled data — the script
exists so that a report built in March looks identical to one built in September, which is
what a client notices.

Pick the theme by matching the client against the `THEMES` table in the deck spec. Taj and the
wider IHCL family take the gold-and-white treatment with Trajan Pro headings; everything else
takes the Katalyst house theme until somebody adds a row for it. **Do not invent a palette for
a client that has no row.** An off-brand deck reaching a Marriott or Accor property is exactly
the reputational cost the agency exists to prevent, and inventing colours for a luxury account
is a worse failure than using a neutral house style.

If the script cannot run in the session, build the deck with whatever PPTX tooling is
available, following the same spec — but say in the run summary that it was built by hand, so
that a formatting drift has an explanation.

## Step 6 — Hand it over with an honest run summary

Deliver the file, then a short summary covering:

- Placements found, publications reached, tier split, computed media value.
- **Every soft edge:** rows with month-only dates, rows near a month boundary, placements
  excluded from the value calculation and why, publications listed as to-be-confirmed,
  intake fields left blank.
- Anything the coverage tracker flagged as found-but-unverified for this client in the period.
- What would make next month's report better — usually a tier for an untiered outlet, or a
  reach figure.

**Then stop.** The deck is a draft for her review. Do not email it, do not file it in a client
folder, do not mark it final. Her approval is the last step and it belongs to her.

## Variants

- **Quarterly roll-up** — same process across three months. Lead with the trend across months
  rather than the placement list, and keep the full log as an appendix.
- **Group report** (Kalra, Dugar, Udeshi) — one deck, a section per brand, and a group-level
  summary at the front. Watch the duplicate case: one article naming three Dugar restaurants
  is three client rows but one article, and the group summary should say so.
- **Launch report** — the window is the campaign, not the month. Take the dates from her.
- **Coverage-only** — drop slides 13 to 15 when the intake is not filled in. Twelve slides that
  are all true beats eighteen with three that are hollow.
