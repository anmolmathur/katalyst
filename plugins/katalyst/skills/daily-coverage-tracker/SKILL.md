---
name: daily-coverage-tracker
description: Find, verify and log each day's new media coverage for the Katalyst PR client roster, then email the confirmed new finds to Pooja. Use for the daily coverage run, a catch-up run over several days, or a single-client coverage check.
---

# Daily coverage tracker

Finds new media coverage for the Katalyst client roster, verifies every hit by opening the
source, logs it to the coverage workbook, and emails the confirmed finds.

**The single most important rule: a completed run with partial coverage is success, not
failure.** An earlier version of this task tried to sweep 718 media contacts every run, never
finished, and sent nothing for weeks. Stopping early with three verified hits beats timing out
with none.

## Configuration

Fill these in once, then leave them alone.

| Setting | Value |
|---|---|
| Coverage workbook | `Katalyst_PR_Coverage_WORKING` — tab `ALL_COVERAGE` |
| Client roster | Same workbook, tab `CLIENTS` |
| Media list | `Katalyst_Master_Media_List 2026` |
| Email to | pooja.katalyst@gmail.com |
| Email CC | nikhilapalat@gmail.com |
| Time budget | 20 minutes of searching |

**Test mode.** While this is still being proven, set test mode on: write to a *copy* of the
workbook, and send the email to the operator only — never to Pooja. Say at the top of the email
that it is a test run. Turn test mode off only once three consecutive runs have produced correct
rows.

## Step 0 — Load the roster

Read the `CLIENTS` tab. Each row gives you a client name, its group, and — critically — a
**Google Alerts query** written to survive that client's name.

**Always search using the query in that column. Never search the bare client name.** A third of
this roster is unsearchable without its qualifier: "Masque" returns theatre and tech, "Swan",
"Paradox", "Circle 69", "Papaya", "Gigi" and "Raga" are all common words. Searching the bare
name is the single biggest reason past runs found nothing.

Also read the existing `ALL_COVERAGE` rows. You need the `Link` column to avoid logging the same
piece twice.

## Step 1 — Find coverage, inside 20 minutes

Track roughly how long you have spent. When you hit the cap, stop immediately — even mid-list —
and go to Step 2 with whatever is confirmed. Note internally which priority you reached.

**Priority 1 — Google Alerts (always, it's fast).**
Search Gmail for `from:googlealerts-noreply@google.com newer_than:1d`. Open and verify each hit.

If this returns nothing, **report that as an observation, not a diagnosis.** Say "no Google
Alerts mail found in the window" and stop there.

Specifically: **do not conclude from the `CLIENTS` tab's `Alert Created?` column that alerts
do or do not exist.** That column is a manual checklist for whoever sets the alerts up. Blank
means nobody has ticked it — it is not evidence about Google's state, and treating it as
evidence has already produced one confidently wrong conclusion.

When alert mail is missing but live search is finding coverage, the useful thing to report is
the discrepancy itself: *"found N pieces by search, none of which arrived as alert mail."*
That points at delivery — wrong address, digest frequency too coarse for the search window,
or a filter moving the mail — and lets a person check in a minute. Diagnosing it is not this
skill's job.

**Priority 2 — search the roster.**
For each client, run its query from `CLIENTS` with the web search tool. Spend no more than about
two minutes per client — breadth across the budget beats depth on one name. Prioritise clients
with recent activity or a known launch.

**Priority 3 — Tier 1 named contacts, only if time remains.**
Take Tier 1 names from the media list and pair each with a client or category term. Skip Tier
2 and 3 and skip LinkedIn crawling — that belongs to the weekly media-list task, not here.

### Verifying a hit

**Open the page. Never log from a search snippet.** Confirm three things: the date falls in the
window you are checking, the publication is who the snippet claimed, and the piece genuinely
concerns the client.

Exclude:

- Directory and aggregator listings — Zomato, Justdial, Tripadvisor, Magicpin, EazyDiner,
  booking and hotel-price sites.
- The client's own website and social posts. Earned coverage only.
- Anything already in `ALL_COVERAGE`. See the duplicate rules below — they matter more than they
  look.

### Duplicates: match on the normalised link, not the raw string

**Strip tracking parameters before comparing URLs.** `?igsh=`, `?img_index=`, `?utm_source=`,
`?utm_medium=`, `?utm_content=` and trailing slashes all vary between people logging the same
piece. An Instagram post logged once as `/p/Da0SOxaCFM1/` and once as
`/p/Da0SOxaCFM1/?img_index=12&igsh=…` is one placement, and a raw string comparison calls it two.

This is not hypothetical. The St. Regis Goa tab already carries roughly ten duplicate pairs from
two separate logging passes — the same Presidential Villa wire story held under both
`travelturtle.world/news/…` and the identical URL again, the same Grazia carousel under two
Instagram forms, the same BW Hotelier piece twice. Its 28 rows represent about 15 actual
placements.

**Also treat as a duplicate:** the same publication and the same story within about seven days,
even when the dates differ. Two passes over the same month routinely disagree by a few days —
one logs the verified dateline, the other the day it was noticed.

**But these are genuinely separate placements, so log both:** the same story picked up by two
different outlets (wire syndication is normal and each pickup counts), and two distinct articles
in one outlet with different URLs and different angles.

When you find a suspected duplicate of an existing row, do not silently skip it. Note it in the
email so someone can decide — a wrongly merged placement is as bad as a double-counted one.

**Watch for group-wide coverage.** Sixteen of the thirty clients belong to three restaurateur
groups (Kalra, Dugar, Udeshi). A single article naming three Dugar restaurants is three rows,
one per client, not one row.

## Step 2 — Log to ALL_COVERAGE

Append one row per confirmed find to the `ALL_COVERAGE` tab. One flat table — there is no
per-client tab to choose.

| Column | What goes in it |
|---|---|
| Date | When the coverage appeared, `YYYY-MM-DD`. Not when you found it. |
| Client | Exactly as spelled in `CLIENTS`. A typo creates a phantom client that every view then misses. |
| Group | From `CLIENTS`. |
| Publication / Account | Exact outlet name. |
| Tier | From the media list where the outlet is listed, else judge against `MAV_RATES` and note it. |
| Reach / Circulation | Real published figure if one exists, else `not disclosed`. Never invent one. |
| Topic / Coverage Focus | One line on what the piece was about. |
| Link | Direct URL. `N/A - print, no URL` for print-only. |
| Placement Type | Feature, Mention, Quote, Photo Credit, Blogger Post or LinkedIn Post. |
| MAV (Rs.) | Tier base rate × placement multiplier, from `MAV_RATES`. Show the arithmetic in Notes. |
| Notes | Anything needing her eye. Say plainly when reach or tier is estimated. |
| Date Note | Qualifiers only — `approx`, `print issue`, `exact date TBD`. Keep the Date cell clean. |
| Logged On | Today's date. |

**Never present MAV as fact.** These are estimated figures; only Free Press Journal has a real
rate card on file. AMEC and PRSA both consider AVE multipliers unsupported by research. If a
number is benchmarked from follower counts, say so in Notes.

**Use one MAV method, and it is the rate card in `MAV_RATES`.** The workbook currently holds two
incompatible systems in the same column: CPM-derived estimates built from Instagram follower
counts (ET Hospitality logged as no-data, LocalSamosa at Rs. 32,725) and rate-card figures
entered by hand (the same ET piece at ₹2,80,000, the same LocalSamosa at ₹1,02,500). They differ
by more than an order of magnitude. Summing that column today produces a number no one should
put in front of a client. Apply the rate card, and flag any row you find carrying the other
method rather than quietly leaving it.

Log nothing if nothing was confirmed — but still do Step 3.

### You cannot write into an existing Google Sheet

The Drive connector can create, copy and read files; it cannot set cells in a sheet that
already exists. So "append to ALL_COVERAGE" is not something you can do directly, and you
should not pretend otherwise or quietly skip the step.

What to do instead, in order of preference:

1. If a Sheets-capable tool is available in the session, use it and append properly.
2. Otherwise, produce the rows in the email as paste-ready lines — which is what the workflow
   was designed around — and say plainly in the email that they still need pasting into
   `ALL_COVERAGE`. Do not create a new spreadsheet per run: an accumulating pile of one-off
   sheets is worse than a paste step, because the desk reads one workbook and every stray file
   is coverage nobody can see.

## Step 3 — Email the finds

**This step always runs.** It is never skipped, and never replaced by a "run didn't finish"
message. That failure mode is what made the previous version useless.

- **To:** Pooja, **CC:** Nikhila (in test mode: operator only)
- **Subject:** `PR Coverage – New Finds – [Date]`
- One line of intro, then the list, then nothing. No commentary, no summary.
- Format each find as `Client | Publication | Date | Link | Placement Type`, ready to paste.
- Group by client where there is more than one.

Add a single closing line only when one of these is true:

- The time budget cut Step 1 short — say which priority you reached, so the gap reads as expected
  rather than as a bug.
- Priority 1 returned nothing and the `Alert Created?` column suggests alerts are missing — say
  that, because it is actionable and a quiet inbox is not.

If nothing was found, send a short note saying so. A quiet day is information; silence is not.

## When someone asks for something narrower

The same process, scoped:

- **One client** — that client's query only, no time cap, and go deeper: Tier 1 names, the
  listicle platforms, the group's other brands.
- **Catch-up over several days** — widen the Gmail window and the search dates, and expect more
  duplicates. Check links carefully.
- **A launch** — search the venue name, the chef, and the founder separately. Launch coverage
  often names the person rather than the property.
