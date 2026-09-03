---
name: alert-keyword-research
description: Work out the best Google Alerts search terms for the Katalyst client roster — permanent brand terms plus time-bound terms derived from the press releases the team has actually pitched — and produce a paste-ready keyword sheet. Use when setting up alerts, refreshing them after new releases go out, or when the coverage tracker keeps missing stories.
---

# Alert keyword research

Works out what to search for, so the daily coverage tracker stops searching for the wrong thing.

## Why this exists

Nikhila finds coverage the tracker misses, and the reason is not that she searches harder. In
her words: *"I'm able to find it because I know what I'm searching for."* She knows a festival
launched at Oliveto last week, so she searches the festival. The tracker only knew the client
was called Oliveto, so it searched a brand name and got the restaurant's own website.

This was confirmed by testing. `"Raga Gaggan"` returns the restaurant's site, Wikipedia and
Instagram — the review published that morning appears nowhere. `Serious Slice Indiranagar third
outlet` returns the trade coverage immediately. **Same story, same day, same index. The
difference is entirely in the query.**

So the job here is to close that gap in advance: read what the team has actually pitched, and
write the queries a journalist's headline will match.

**What this skill does not do.** It does not write a PR strategy, summarise releases for their
own sake, log coverage, or build a report. The press releases are input for deriving search
terms and nothing else. Do not reproduce release bodies, client contact details or embargoed
material in the output — a keyword sheet needs names and campaign titles, which are published
anyway, and nothing more.

## Configuration

| Setting | Value |
|---|---|
| Keyword sheet | `Katalyst_PR_Coverage_WORKING` — tab `KEYWORDS` (create it if absent) |
| Client roster | Same workbook, tab `CLIENTS` |
| Release window | Last 90 days, weighted heavily to the last 30 |
| Cadence | Weekly, or on demand when a batch of releases goes out |
| Target volume | 150 excellent alerts, not 700 mediocre ones |

## Step 1 — Read the roster

Read `CLIENTS`. For each active client note the official name, the common media name, the city,
the group, and the existing query if there is one. That existing query is a starting point to
improve on, not something to preserve.

## Step 2 — Find what has actually been pitched

Search Gmail for the team's recent press activity. Search each of these separately rather than
as one giant query, because a single over-constrained search is how this step quietly returns
nothing:

- `from:pooja.katalyst@gmail.com newer_than:90d`
- Sender, recipient and cc searches for Disha and Sazia at their Katalyst addresses
- `from:me newer_than:90d (press OR media OR launch OR pitch)`
- Subject searches: `subject:(press release OR media release OR press note OR media note OR pitch OR launch)`

Look for press and media releases, story and media pitches, launch and festival announcements,
new menus, chef collaborations and residencies, appointments, events, awards, partnerships,
wellness and festive programmes, wedding announcements.

**Weight the newest most heavily.** Where a client has several releases, the current campaign
matters more than one from two months ago. Note the date of each release — you will need it for
the `Source` and `Expires` columns.

## Step 3 — Open the releases, do not skim subject lines

A subject line gives you the client. The body gives you the *hook* — and the hook is the whole
point of this exercise.

From each release, pull the distinctive named things a journalist would repeat: campaign or
festival name, visiting chef, resident chef, the restaurant and hotel, the collaboration title,
a named menu or package, an event title, a new appointment and the role, an award name, a
cuisine or concept, the destination.

Ignore adjectives. "Curated", "immersive", "elevated" and "bespoke" appear in every release ever
written and match nothing.

## Step 4 — Think like the headline, not like the brand

For each candidate term ask: **if this story runs, what words appear together in the headline,
the URL slug, or the first paragraph?** Then write the smallest combination that isolates it.

A festival called Mezzo at Oliveto in The St. Regis Goa Resort should not produce `Mezzo` —
that is a common word and will bury you. It should produce something like `"Mezzo" "Oliveto"`,
`"Mezzo Festival" Goa`, or `"<chef name>" "Oliveto"`.

The target is the sweet spot between specificity and discoverability. Too broad and the alert is
noise; too narrow and it matches only the press release's own wording, which is precisely what
journalists rewrite.

**Write variations where the wording is likely to shift.** A journalist may drop "Festival",
shorten "The St. Regis Goa Resort" to "St Regis Goa", or lead with the chef rather than the
venue. Two simple alerts that each catch a plausible phrasing beat one clever one that catches
neither.

## Step 5 — Two kinds of keyword, and the difference matters

**Evergreen** — permanent, tied to the brand: the property, the general manager, the executive
chef, an important spokesperson, a named restaurant or bar, a distinctive named spa or space.
Qualify anything generic: `"The Grill" "Vivanta Hyderabad"`, never `"The Grill"`. Skip generic
facilities — "the spa", "the ballroom", "Sunday brunch" — unless the name is genuinely
distinctive.

**Campaign** — derived from a current release, and **time-bound**. This is the highest-yield
category and the one nobody has been using.

### Never write an unannounced deal into the sheet

**If the story is not public yet, it does not go in the sheet at all** — not as a row, not as
OPTIONAL, not with a note saying it is unconfirmed. Leave it out entirely and mention in the
chat reply that a keyword is being held back until the announcement, without naming the partner.

The `KEYWORDS` tab is a shared Google Sheet. It has been link-shared with edit access, other
people at Katalyst open it, and it is not a confidential document. A row reading
`"<celebrity name>" "<hotel>"` with a source note saying *commercials sent, not yet confirmed*
is a leak of a live negotiation sitting in a shared file — and the explanatory note makes it
worse, because it documents the deal rather than merely hinting at it.

This is not hypothetical. A run proposed rows for two unannounced St. Regis Goa collaborations
taken from internal threads — one with commercials still under negotiation, one an unconfirmed
influencer booking. Both named real public figures. Neither appears anywhere in the press;
checked. For a reputation agency, that sheet leaking is a client-losing event, and the
keyword sheet is not worth that risk.

The test is simple: **has this been announced, or has coverage already run?** If yes, it is fair
game. If it is a pitch, a proposal, an approval thread, a commercial under negotiation, or a
booking still being confirmed, hold it. Add the keyword the day it goes public — that is soon
enough, because coverage cannot precede the announcement anyway.

Being right about a keyword is worth nothing if the sheet costs Nikhila a client.

### Campaign keywords must expire

This is the part not to skip. A festival alert is gold for three weeks and pure noise by
December, and an alert list nobody prunes becomes an inbox people stop reading — which is how
the last monitoring setup died.

Give every campaign keyword an **`Expires`** date: the event end date plus three weeks, or the
release date plus 60 days where there is no event. Nothing gets a campaign keyword without one.
On each run, list expired rows under **RETIRE THESE** so they can be deleted from Google Alerts,
and do not re-propose them.

## Step 5b — Verify every person's name against the press

**A quoted name that isn't how the press writes it is a permanently dead alert**, and it fails
silently — it never matches, and nobody ever finds out.

This is not hypothetical. A first run proposed `"Anita Gomes" "St. Regis Goa"` for the St. Regis
Goa marcom director. Her name in every published piece — BW Hotelier, HospiBuz, Travel And Tour
World — is **Anita Dacosta E Gomes**. A quoted phrase requires exact adjacency, so
`"Anita Gomes"` matches none of them. The alert would have run for years finding nothing.

So for every `EVERGREEN - PERSON` row, before writing the query:

1. **Search the name once** and look at how publications actually render it — middle names,
   double-barrelled surnames, initials, honorifics, common misspellings.
2. **Quote the full published form**, not the short form you saw in an email signature or a
   client's own shorthand.
3. Where the press is genuinely inconsistent, write two rows rather than one clever query.
4. If you cannot confirm the spelling, mark the row `OPTIONAL` and say plainly in
   `What It Tracks` that the spelling is unverified. Do not quote a guess.

**Mine the source you already opened.** When one name checks out in a piece, read the rest of
that piece before marking anyone else unverified — trade coverage of a launch usually names the
whole founding team, the chef and the parent company in the same three paragraphs. A run
verified one Serious Slice co-founder against a Business of Food article and marked the other
two `OPTIONAL` as unverified; all three were named, correctly spelled, in that same article.
One extra read promotes two rows.

**Correct the name; don't drop the person.** When a search turns up the published form, use it —
`"Anita Dacosta E Gomes" "St Regis Goa"` rather than deleting the row. A marcom director, GM or
executive chef is one of the most productive evergreen alerts there is, because appointments,
interviews and quotes all carry the name. Dropping the row silently loses that coverage, and is
the wrong response to a spelling you have just successfully verified.

The same care applies to restaurant and campaign names taken from internal notes — the client's
internal working title is often not the name in the release.

## Step 6 — Keep the queries simple

Google Alerts is not a search engine with a query planner behind it. Prefer `"Campaign" "Hotel"`
over a Boolean construction. Use quotation marks for distinctive phrases. Use `OR` only where it
genuinely earns its place. **If two simple alerts are more reliable than one complicated one,
recommend two** — the goal is coverage found, not elegance.

Note for whoever sets these up: unquoted words in a Google Alert are ANDed together, so a
flattened query that lost its quotation marks will match almost nothing. Several of this
roster's existing alerts failed exactly that way. Quotation marks are load-bearing.

### Two rules the dual purpose imposes

The `KEYWORDS` tab is read by two different things — Google Alerts, and the coverage tracker,
which runs the same strings against web search and Bing News. They do not tolerate the same
syntax, so:

**Avoid `OR`.** Google Alerts accepts it; **Bing News returns an empty feed for any query
containing `OR`** — tested and confirmed. A row like `"St. Regis Goa" OR "St Regis Goa"` works in
one channel and silently returns nothing in the other. Write the single best form, or two rows.
In that example one row is enough anyway: search engines ignore the full stop, so
`"St. Regis Goa"` already catches `St Regis Goa`.

**Don't AND a category word onto an already-distinctive phrase.** Every unquoted word is an AND
that can only lose coverage. `"Serious Slice" pizza` misses any piece about Serious Slice that
doesn't use the word *pizza*; `"Anirudh Kheny" restaurant` misses a profile that calls him a
founder. The quoted name was already specific — the extra word buys nothing and costs matches.
Qualify generic names (`"Miri" "St. Regis Goa"` is right, because *Miri* alone is a common word);
leave distinctive ones alone.

## Step 7 — Cut duplicates, then prioritise

Drop alerts that do the same work. If `"Rambagh Palace"` reliably catches what
`"Rambagh Palace Jaipur"` catches, keep one. Keep both only where the qualifier materially
improves precision.

Then classify every surviving alert:

- **ESSENTIAL** — high likelihood of finding real coverage. Add it.
- **RECOMMENDED** — useful additional monitoring.
- **OPTIONAL** — plausible, but likely to generate noise. Do not add by default.

Be hard about this. A hundred and fifty alerts that get read beat seven hundred that do not.

## Step 8 — The output

Three parts, in this order.

### Part 1 — the keyword sheet

Grouped by client, and within each client, **ALWAYS-ON ALERTS** then **CURRENT PR RELEASE
ALERTS**. Columns:

`Client | Property / Brand | Google Alert Search Term | Keyword Type | What It Tracks | Source | Priority | Expires`

`Keyword Type` is one of: `EVERGREEN - BRAND`, `EVERGREEN - PERSON`, `EVERGREEN - RESTAURANT`,
`EVERGREEN - OTHER`, `CURRENT PR RELEASE`.

`Source` is `BRAND RESEARCH` for evergreen rows, and the release name and date for campaign rows
— `Press Release - Mezzo Festival - 28 Aug 2026`.

`Expires` is blank for evergreen rows and a date for every campaign row.

**Render this as an HTML `<table>`, not tab-separated text.** Tabs do not survive rendering and
paste into a single column; an HTML table pastes into Google Sheets as real cells. This was
learned the hard way on the coverage tracker.

### Part 2 — the counts

Total clients analysed; total always-on keywords; total campaign keywords; totals for ESSENTIAL,
RECOMMENDED and OPTIONAL; and how many existing keywords are being retired.

### Part 3 — GOOGLE ALERTS TO ADD NOW

Only the ESSENTIAL and RECOMMENDED queries, one per line, nothing else on the line — no numbering,
no commentary, no priority label. This block is for copying straight into Google Alerts.

Follow it with **RETIRE THESE**: expired campaign queries, one per line.

## Setting the alerts up

**Do not create Google Alerts automatically, and never inside a scheduled run.** Alerts are
standing configuration in Nikhila's Google account; a hundred and fifty of them created
unattended, with no one watching for a misfired query, is a mess that takes longer to unpick
than it saved. The paste-ready block exists so a person can add them deliberately.

If she wants help doing it, that is a separate, watched session with a browser — in batches, with
her present, confirming as it goes. Not this skill, and not a scheduled task.

**Sequencing matters more than volume.** As of 2 September 2026 no mail from
`googlealerts-noreply@google.com` has ever arrived in the tracker inbox, though thirty alerts
demonstrably exist. Adding a hundred and fifty more before that is diagnosed multiplies a broken
thing. Fix delivery on the existing alerts first — check that each one's "Deliver to" is an
email address and not an RSS feed, and that the address is the inbox the tracker reads — then
confirm mail arrives, then add.

Recommended alert settings, unless there is a reason otherwise: **at most once a day**, sources
**Automatic**, language **English**, region **India** (or **Any Region** for brands and people
with genuine international press), how many **All results** — not "only the best results", which
silently discards trade coverage. Do not change her account or the delivery address.

## How this feeds the coverage tracker

The `KEYWORDS` tab is what the `daily-coverage-tracker` skill should search from. Evergreen
rows replace the single static query per client; unexpired campaign rows are the high-yield
additions, and should be searched for the clients that have them **before** the evergreen terms,
because a live campaign is where the week's coverage actually is.

That is the whole loop: research the keywords, set the alerts, and let the tracker search what
the press is actually being told about rather than guessing from a brand name.
