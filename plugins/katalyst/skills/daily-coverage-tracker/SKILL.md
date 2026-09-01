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

### Test mode is ON unless the instruction says otherwise

**Default to test mode.** Unless the message that invoked this run contains the exact phrase
`TEST MODE OFF`, you are in test mode:

- Write to a *copy* of the workbook, never the live one.
- Send the email to the operator who set the task up — **never to Pooja, never to Nikhila.**
- Open the email with a line saying it is a test run.

This defaults on deliberately. A scheduled task's instruction can be shortened or rewritten by
whoever edits it, and the failure mode is not symmetrical: a test run that should have been live
costs one day, while a live run that should have been a test puts an unreviewed automated email
in a colleague's inbox under Nikhila's name. Do not infer from tone, from how polished the setup
looks, or from "this has been working for a while" that you should go live. Require the phrase.

When you do see `TEST MODE OFF`, use the live workbook and the addresses in the configuration
table above.

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
Search Gmail for `from:googlealerts-noreply@google.com`, over a window that covers everything
since the last run — **not a fixed one day.**

If the task runs on weekdays only, Monday must look back to Friday morning, or Friday evening
and the whole weekend are never seen by any run. Indian lifestyle and F&B press publishes
heavily at weekends. Use `newer_than:1d` on Tuesday to Friday and `newer_than:4d` on Monday, or
simply `newer_than:4d` every day and rely on the duplicate rules to drop what you have already
logged — that is the safer default, since duplicates are cheap and missed coverage is not.

Apply the same window to the date filter you use when judging Priority 2 search results.

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
two minutes per client — breadth across the budget beats depth on one name.

**Rotate through the roster on a fixed three-day cycle.** The budget covers roughly ten of the
thirty clients per run, so a run that always starts at the top means the bottom twenty are never
searched at all.

Take the `CLIENTS` tab in its own row order and split it into three blocks of ten. Pick the
block by the day of the month:

| Day of month | Block |
|---|---|
| 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31 | rows 1–10 |
| 2, 5, 8, 11, 14, 17, 20, 23, 26, 29 | rows 11–20 |
| 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 | rows 21–30 |

This needs no memory of previous runs, which matters because each scheduled run starts fresh
with none. Every client is searched at least every third day, and which clients a given run
covered is reproducible after the fact.

**Do not rotate by "least recently logged".** A client that is searched but has no coverage
never gets a `Logged On` stamp, so it would look permanently unsearched and monopolise the
rotation while genuinely active clients starve.

Two exceptions jump the queue regardless of block: a client with a launch or event inside the
next fortnight (the `CLIENTS` setup notes flag these), and any client that appeared in Priority
1 alert mail. Search those first, then work the day's block.

Name in the email which block you covered and which clients you did not reach. Without that,
nobody can tell a genuinely quiet client from one that simply was not searched — and the
dashboard's silence ledger will read the second as the first.

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

### Record the canonical URL, never a wrapper

**Unwrap Google redirect links before logging anything.** Links copied out of Gmail arrive as
`https://www.google.com/url?q=<the real url>&source=gmail&ust=...` — take the `q=` parameter
and log that. Strip `/amp/` from AMP links too, so the same article has one form.

This is not cosmetic. The duplicate rule below strips query strings, so every wrapped link
normalises to `google.com/url` — meaning a run that logs wrappers marks all its own finds as
duplicates of each other, and no real URL ever matches them again. It has already happened
once.

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
| MAV (Rs.) | Tier base rate × placement multiplier, from `MAV_RATES`. **A plain number — `150000`, not `Rs. 150,000`** — so the column can be summed. Show the arithmetic in Notes. Leave empty when there is no figure. |
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
2. Otherwise, put the rows in the email in the formats Step 3 specifies, and say plainly there
   that they still need pasting into `ALL_COVERAGE`. Do not create a new spreadsheet per run:
   an accumulating pile of one-off sheets is worse than a paste step, because the dashboard
   reads one workbook and every stray file is coverage nobody can see.

Either way the row carries **all fourteen columns in sheet order**. A row without `Group` is
invisible to the dashboard's group rollup, one without `Tier` cannot be valued, and a short row
silently shifts every column after it. Leave a cell empty rather than dropping it.

## Step 3 — The email

The email has three parts, in this order. They serve different readers and must not be merged.

### Part 1 — the readable summary

A one-line intro, then the finds grouped by client, one per line:

`Client | Publication | Date | Placement Type`

For scanning on a phone. No links here — they make it unreadable.

### Part 2 — the paste table

**An HTML table. Not tab-separated text.**

This is the part Nikhila actually uses, and it is where the previous format failed: tabs do
not survive Gmail's HTML rendering, so a tab-separated block pastes into a single column and
has to be unpicked by hand. A real `<table>` pastes into Google Sheets as proper cells, because
Sheets reads the HTML clipboard format. She selects the table, copies, clicks the first empty
row of `ALL_COVERAGE`, pastes — and it lands in fourteen columns.

Build it exactly like this:

- One `<table>` with a header row carrying the fourteen column names, so she can see at a glance
  that the columns line up before she pastes. Tell her in one line to select from the first data
  row down, so the header does not get pasted in.
- One `<tr>` per find, fourteen `<td>` in sheet order, **every cell present** even when empty.
  A missing `<td>` shifts every column after it.
- Column order: Date, Client, Group, Publication / Account, Tier, Reach / Circulation,
  Topic / Coverage Focus, Link, Placement Type, MAV (Rs.), Notes, Date Note, Logged On,
  MAV Method.
- Links as bare URL text — do not wrap them in an anchor with different display text, or the
  cell will hold a label instead of the URL, and both the deduplication and the dashboard read
  that cell as the link.
- **MAV as a plain number: `150000`, not `Rs. 150,000`.** A currency prefix makes the cell text,
  and a text column cannot be summed — which defeats the point of tracking MAV at all. The sheet
  formats the column; the row supplies the number. Leave it empty when there is no figure rather
  than writing "N/A".
- Dates as `YYYY-MM-DD` so they sort. Qualifiers go in `Date Note`, never in `Date`.
- Commas inside Topic and Notes are fine — an HTML table has no delimiter to break.

### Part 3 — the machine-readable block

After the table, the same rows once more, tab-separated, between these markers:

```
---KATALYST-ROWS-START---
2026-08-27<TAB>RAGA<TAB>Kalra<TAB>Esquire India<TAB>Tier 1<TAB>…
---KATALYST-ROWS-END---
```

This one is not for a person. A Google Apps Script bound to the workbook reads the email's
plain-text part — where tabs *do* survive — and appends the rows automatically, which is what
removes the paste step entirely once it is switched on. Until then it is harmless.

- Fourteen fields on every line, even where several are empty.
- No markdown, no bullets, no bold inside the block.
- Strip tabs and newlines out of any field value first.
- Omit the markers entirely when there is nothing to log. An empty block is fine; a malformed
  one is not.

The script deduplicates on the `Link` column, so a re-run or a double trigger cannot double-log.
That safety depends on the link being the canonical URL — another reason to unwrap Google
redirect wrappers before this point.

### Part 4 — the coverage note

Close with which block of the roster you searched, which clients you did not reach, and whether
Google Alerts mail appeared. Two or three lines. This is what stops a client that was never
searched being read as a client with no coverage.

### Sending it

**This step always runs.** It is never skipped, and never replaced by a "run didn't finish"
message. That failure mode is what made the previous version useless.

- **To:** Pooja, **CC:** Nikhila — in test mode, the operator only.
- **Subject:** `PR Coverage – New Finds – [Date]`
- Send as HTML, or the paste table arrives as unformatted text and the whole point is lost.

If nothing was found, send the summary and the coverage note and omit the table and the marker
block entirely. A quiet day is information; silence is not.

## When someone asks for something narrower

The same process, scoped:

- **One client** — that client's query only, no time cap, and go deeper: Tier 1 names, the
  listicle platforms, the group's other brands.
- **Catch-up over several days** — widen the Gmail window and the search dates, and expect more
  duplicates. Check links carefully.
- **A launch** — search the venue name, the chef, and the founder separately. Launch coverage
  often names the person rather than the property.
