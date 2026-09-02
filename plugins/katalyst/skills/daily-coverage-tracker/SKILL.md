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
| Time budget | 40 minutes — feeds, inbox, all 30 clients, Bing for the big names, then verify |

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

## Step 0 — Load the roster and the keywords

Read the `CLIENTS` tab. Each row gives you a client name, its group, and — critically — a
**Google Alerts query** written to survive that client's name.

**Always search using the query in that column. Never search the bare client name.** A third of
this roster is unsearchable without its qualifier: "Masque" returns theatre and tech, "Swan",
"Paradox", "Circle 69", "Papaya", "Gigi" and "Raga" are all common words. Searching the bare
name is the single biggest reason past runs found nothing.

**Then read the `KEYWORDS` tab if it exists**, produced by the `alert-keyword-research` skill.
It carries better queries than `CLIENTS` does, and in particular it carries **campaign
keywords** — terms taken from the press releases the team has actually pitched.

This matters more than it looks. Nikhila finds coverage this task misses because she knows a
festival launched last week, so she searches the festival; the task knew only that the client
was called Oliveto, so it searched a brand name and got the restaurant's own website. The
`KEYWORDS` tab is how that knowledge reaches the run.

Use it like this:

- **Unexpired campaign rows first**, for the clients that have them. A client with a live
  campaign is where this week's coverage actually is, so search those terms before the
  brand terms.
- **Evergreen rows** replace the single static `CLIENTS` query for that client. Where both
  exist, prefer `KEYWORDS`.
- **Skip any campaign row whose `Expires` date has passed** — a September festival is noise in
  December. Do not search it, and mention in the email that expired keywords were skipped so
  somebody knows the tab needs a refresh.
- Where `KEYWORDS` has no row for a client, fall back to the `CLIENTS` query.

If the tab does not exist yet, carry on with `CLIENTS` alone and say so in one line of the
email — it is a gap worth closing, not a reason to stop.

Also read the existing `ALL_COVERAGE` rows. You need the `Link` column to avoid logging the same
piece twice.

## Step 1 — Find coverage, inside 40 minutes

Three channels, in this order. **Channel A is the one that catches same-day coverage.** Read the
next paragraph before changing anything in this section, because the ordering is not arbitrary.

### Why the order matters — read this before touching it

Web search is ranked by *relevance*, not recency. Search "Raga Gaggan" and you get the
restaurant's own site, Wikipedia, Instagram and the big launch pieces from a fortnight ago. The
review that a trade title published three hours ago is on page four, if it is indexed at all.
This is not a bad query — it is what a relevance-ranked index is built to do, and no amount of
rewording changes it. A run that relies only on per-client search will keep reporting "quiet
day" on days when Nikhila can find four placements by hand in ninety seconds. That has already
happened, and it is the reason this section was rebuilt.

What she does by hand is different in kind: she searches Google with the **past-24-hours filter**
on, which throws away everything canonical and leaves only what is new. There is no such filter
here. So the run has to get recency a different way — by reading publications' own feeds, which
are ordered newest-first by construction.

The inversion is the whole trick. Do not ask *"is there news about client X?"* thirty times.
Ask *"here is everything this beat published today — which of it is ours?"* once. That is how a
human clipping service works, and it is why it does not miss things.

### Channel A — sweep the trade feeds (primary, always, first)

Fetch each feed below and read every item published inside the window from Step 1's date rules.
Ten fetches, recency-ordered, no ranking to fight. This channel is cheap and must always
complete.

| Publication | Feed |
|---|---|
| Elle Gourmet India | `https://ellegourmet.in/rss` |
| HospiBuz | `https://hospibuz.com/rss` |
| BW Travel | `https://www.bwtravel.com/rss` |
| Local Samosa | `https://www.localsamosa.com/rss` |
| MediaBrief | `https://mediabrief.com/feed/` |
| Business of Food | `https://www.businessoffood.in/feed/` |
| The Nod Mag | `https://thenodmag.com/feed/` |
| Finely Chopped | `https://finelychopped.net/feed/` |
| Restaurant India (Operations) | `https://www.restaurantindia.in/rss/operations` |
| Indian Food Freak | `https://indianfoodfreak.com/feed/` |

To add a publication, add a row. To drop one that has gone quiet or started 403ing, delete its
row and say so in the email. A feed that fails is worth one line in the email — "HospiBuz feed
returned 403" — and nothing more; do not spend budget retrying it.

**Known blind spots, and be honest about how bad they are.** Two different failures get
confused here, and only one of them Channel C can rescue.

*No feed, but findable by search:* Hospemag, Hotelier India, Hospitality Biz India, Express
Hospitality, Esquire India. The feed sweep misses these; a Channel C query can still surface
them. Search by name when a client has something live.

*Neither fetchable nor indexed:* **Condé Nast India's stable — Vogue India, GQ India,
Architectural Digest India, Condé Nast Traveller India — and Travel + Leisure Asia.** The
search index available here is US-weighted, and these titles barely appear in it at all; a
direct query naming the publication and the client returns Wikipedia, Tripadvisor and booking
sites instead. **Channel C does not reach them. Nothing in Channels A or C does.** These are
Tier 1 for a luxury hospitality roster, so this is the real gap in the task, not a footnote.

The only automated channel that sees them is **Channel B, the inbox** — Google's index is
global and does carry them, so a working Google Alert on a client name will surface a Vogue
India piece that no search here can find. That is the strongest argument for getting alert mail
delivery fixed, and for subscribing the tracker inbox to those titles' own newsletters.

**Never report a quiet day for a client whose likely coverage sits in one of those titles
without saying so.** If a client had a launch or event and the run found nothing, add one line:
"nothing found, but the Condé Nast titles are not reachable from here — worth a manual check."
A wrong quiet day is the specific failure this task exists to prevent.

One partial consolation: a single event usually appears across several titles in a week, so a
blocked publication often still reaches you through one that isn't. The Oliveto residency ran
on both Hospemag (no feed) and BW Travel (feed) on the same day. This does not cover an
exclusive feature, which is exactly the coverage that matters most.

**Match each item against the roster three ways**, because trade press often names the parent,
not the outlet:

1. The client name and its qualifier, from `CLIENTS`.
2. The **group** — Kalra, Dugar, Udeshi, the hotel brand, the parent company. A piece headlined
   about a group launch is coverage for the client inside it.
3. **People** — the chef, GM or founder attached to that client in the `CLIENTS` notes. "Chef
   Jacopo Avigo at Oliveto" is St. Regis Goa coverage; a query for "Oliveto" alone may not
   rank it.

An item that matches goes straight to the candidate list. You already have its title, date and
canonical link from the feed, so verification is usually one page-open to confirm the piece is
genuinely about the client.

Some titles that matter will not name a client at all — a roundup like "new restaurant openings
this week" can carry a client in the body. Open a roundup if its subject overlaps the roster's
beat; do not open every general-interest item.

### Channel B — the inbox: Google Alerts, and publisher newsletters

This is the only channel that reaches the publications Channels A and C cannot see, because it
rides on Google's index rather than the one available here. Treat it as load-bearing, not as a
nice-to-have that happens to be empty.

Search Gmail for `from:googlealerts-noreply@google.com` over a window that covers everything
since the last run — **not a fixed one day.**

Also read any publisher newsletters that have been subscribed to the tracker inbox — Condé Nast
Traveller India, Vogue India, Travel + Leisure Asia and the like. Newsletters are curated and
will miss short items, so they are a top-up on the blind spots rather than full coverage of
them. Match their contents against the roster the same three ways as Channel A.

If the task runs on weekdays only, Monday must look back to Friday morning, or Friday evening
and the whole weekend are never seen by any run. Indian lifestyle and F&B press publishes
heavily at weekends. Use `newer_than:1d` on Tuesday to Friday and `newer_than:4d` on Monday, or
simply `newer_than:4d` every day and rely on the duplicate rules to drop what you have already
logged — that is the safer default, since duplicates are cheap and missed coverage is not.

Apply the same window to the date filter you use when judging Channel C search results.

If this returns nothing, **report that as an observation, not a diagnosis.** Say "no Google
Alerts mail found in the window" and stop there.

Specifically: **do not conclude from the `CLIENTS` tab's `Alert Created?` column that alerts
do or do not exist.** That column is a manual checklist for whoever sets the alerts up. Blank
means nobody has ticked it — it is not evidence about Google's state, and treating it as
evidence has already produced one confidently wrong conclusion.

When alert mail is missing but Channel A or C is finding coverage, the useful thing to report is
the discrepancy itself: *"found N pieces by feed and search, none of which arrived as alert
mail."* That points at delivery — wrong address, delivery set to RSS rather than email, digest
frequency too coarse for the window, or a filter moving the mail — and lets a person check in a
minute. Diagnosing it is not this skill's job.

### Channel C — per-client search, as a backstop

Every client is searched every run. No rotation, no blocks. The point of this task is that
nobody has to wonder whether a client was looked at. But understand what this channel is for:
it catches the publications not in the feed table — nationals, wires, foreign titles — and it
is weak on anything published in the last few hours. Channel A is what catches those.

Run each client's query from `CLIENTS`, in roster order, all thirty. Read titles and dates only;
do not open pages yet. Never search the bare client name — a third of this roster is
unsearchable without its qualifier ("Masque" returns theatre and tech; "Swan", "Paradox",
"Circle 69", "Papaya", "Gigi" and "Raga" are all common words).

**Where the `CLIENTS` notes flag a launch, opening, residency, appointment or award inside the
last fortnight, run a second query that describes the event rather than naming the client** —
"Serious Slice Indiranagar third outlet", "Chef Jacopo Avigo Oliveto St Regis Goa". Descriptive
queries reach the trade coverage that brand-name queries bury, because they match how the piece
is actually headlined. This is worth roughly one extra query for the two or three clients with
something live, not for all thirty.

### Channel D — Bing News, for the national press and wire pickup

Google News RSS cannot be used. It is blocked by robots policy, as are Google Alerts' own RSS
feeds and the free news APIs built on Google's index. Do not spend budget rediscovering this.

Bing News does work, and it reaches something the other channels miss entirely: **Indian
national dailies and wire pickup** — Indian Express, NDTV, Telegraph India, Mid-Day, Free Press
Journal, The Tribune, The Wire, ANI, MSN. Channel A is trade press only and Channel C's index is
US-weighted, so without this a national story about a client can pass unnoticed.

One query per client, of this exact shape:

`https://www.bing.com/news/search?q=%22<quoted client name>%22&format=RSS&cc=IN`

Rules learned by testing, so do not improvise here:

- **Quote the client name.** Unquoted terms return noise.
- **Never use `OR`** in the query — it returns an empty feed.
- **Never add `sortby=Date`** — it returns an HTML page instead of a feed.
- Expect zero items for small independents. "Serious Slice" returns nothing; "Sofitel Mumbai
  BKC" returns five. This channel is for clients with national reach, not for the whole roster.

**Do not run this for all thirty.** Run it for the hotel and group clients, the named chefs, and
any client with a launch or event live — roughly a dozen. Each query is a fetch, and the budget
is better spent on Channel A, which is what actually catches same-day coverage. **If the run is
short of time, Channel D is the first thing to cut.**

Two cautions on what comes back. It is **not reliably same-day** — a story the trade feeds
carried this morning may not appear here for a day or two, so a Bing hit is a safety net, not a
freshness check. And **wire releases arrive many times over**: one Sofitel PTI release came back
four times, as Tribune, The Wire, ANI and Webindia123. Those are four genuine placements by the
duplicate rules below and should be logged as four, but say so in the email — a day that looks
like a spike is often one release picked up widely, and Nikhila should see it described that way
rather than counted silently.

### Then verify the candidates

Now open pages and confirm, spending the remaining budget. Work in this order:

1. Anything that appeared in Google Alerts mail.
2. Anything from Channel A — it is dated by the feed, so it is fast to confirm.
3. Clients with a launch or event inside the next fortnight.
4. Channel D hits, checking the date carefully — Bing's index lags, so an item can be months old.
5. Everything else, Tier 1 publications before Tier 3.

If the budget runs out with candidates still unverified, **list them in the email as "found,
not yet verified", with client, publication and link.** Do not log them — an unverified hit
never enters the sheet. But do not discard them silently either: a person can check three
links in a minute, and next run will pick them up again.

**Report all thirty as searched, and report the feed sweep separately.** Say plainly that every
feed was read and every client was swept, then which had candidates, which were verified, and
which are carrying over. That is the sentence that lets Nikhila stop wondering — and it is only
true because Channels A and C both always finish.

**A quiet day is only credible if Channel A ran.** If the feeds could not be fetched, say the
day was unverified rather than quiet. The difference matters: she checks by hand when we say
quiet and we are wrong, and that is the whole trust problem this task exists to solve.

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

Three or four lines, covering: how many trade feeds were read and whether any failed, that all
thirty clients were swept, which clients you did not reach verification on, and whether Google
Alerts mail appeared. This is what stops a client that was never searched being read as a
client with no coverage — and what stops a failed feed sweep being read as a quiet day.

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
