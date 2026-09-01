# Audit — The Two Live Sheets

_Read 1 Sep 2026. Both sheets opened in full via the Drive connector: all 30 tabs of the
tracker and all 21 tables of the media list were parsed programmatically. Individual contact
rows were sampled rather than read one by one — the counts and distributions below are
computed across every row._

Owner of both: nikhilapalat@gmail.com. Anmol's Drive connector can already read them, so
there is no access problem for the build.

---

## Katalyst_PR_Coverage_Tracker — the headline finding

**30 client tabs. Six have any data. Twenty-four are completely empty.**

| Client | Rows logged |
|---|---|
| The St. Regis Goa Resort | 28 |
| Sheraton Grand Chennai Resort & Spa | 9 |
| Sofitel Mumbai BKC | 5 |
| JW Marriott Kolkata | 5 |
| Sorena | 4 |
| Pali Bhavan | 1 |
| **24 other clients** | **0** |

Fifty-two rows total, and the README says most of those came from a seeded July backfill
rather than the daily run. This is not a tracker that is working badly — it is a tracker that
has essentially never run.

### The client roster is 30, not 56

That settles the open question. And the shape of it matters more than the count: the roster
clusters under a handful of restaurateur groups.

| Group | Brands on the roster |
|---|---|
| Zorawar Kalra | Masala Library, Swan, Botie, Louis Burger, Papaya, Mamma Killa, plus Raga with Gaggan Anand |
| Aditi Dugar | Masque, Sage & Saffron, TwentySeven BakeHouse, Paradox, Circle 69 |
| Dhaval Udeshi | Gigi, Sweeney, Soraia, Fielia, The Scarlett House |
| Hotels | Sofitel Mumbai BKC, Sheraton Grand Chennai, St. Regis Goa, JW Marriott Kolkata, Soulinaire Alibaug |
| Independent | Pali Bhavan, Paashh, Serious Slice, Ikai, Sorena, Alter Ego, Chicnutrix, Rotary Club of Bombay |

Sixteen of thirty brands sit under three people. That changes the automation: one relationship
covers many brands, and a single piece of coverage often names several of them at once.

---

## The likely root cause of the empty tracker

Her daily tracker prompt makes **Google Alerts its Priority 1** — search Gmail for
`from:googlealerts-noreply@google.com newer_than:1d`, verify each hit, log it.

The tracker workbook contains a fully built **"How to Set Up Google Alerts" tab**: thirty
ready-to-paste alert queries, one per client, each with the key people named and the exact
qualifier syntax worked out. The tab's own instructions say it takes 20–25 minutes to set them
all up.

**If those alerts were never created, Priority 1 returns nothing every single morning** — and
the run falls through to a live search that then times out on the 718-contact sweep. That
matches the failure exactly: not a bad prompt, an unfired prerequisite.

**Check this before building anything.** Twenty-five minutes at google.com/alerts may fix more
than any prompt rewrite would.

## The second cause: generic client names

A third of the roster has names that collide badly in search — Swan, Paradox, Circle 69,
Papaya, Gigi, Botie, Masque, Raga, Alter Ego, Ikai. The sheet already documents the required
qualifier for each one ("Masque" alone is too generic — theatre, tech term; "Raga" collides
with music; "Swan" is hopeless unqualified).

Her V2 prompt says *"for each client/brand name, do one Google News search."* For half the
roster that instruction produces noise, not coverage.

**The fix is free and immediate:** the tracker skill should read the qualified query from the
Google Alerts tab rather than constructing one from the client name. She already did this
work; nothing is using it.

---

## Katalyst_Master_Media_List v6 — roughly 730 contacts across 21 tabs

| Section | Rows |
|---|---|
| Master Media List | 176 |
| Regional tabs (Mumbai, Delhi, Goa, Kolkata, Bengaluru, Chennai) | 300 |
| Blogger tabs, six cities | 256 |
| Gifting / courier logistics | 56 |
| Listicle & Discovery Platforms | 29 |
| Top Priority | 14 |
| Avoid / Verify | 10 |

Across the media rows: **Tier 1 — 212, Tier 2 — 130, Tier 3 — 29.** About 63% carry an email
address.

### The data-quality number that matters

**Status is `Verify` on roughly 31% of contacts** — 150 of the ~481 rows scanned, against 217
`Active`. Nearly a third of the list cannot safely be pitched by name without confirming the
masthead first.

The Avoid/Verify tab is the proof of why that matters: it flags a critic who **died in 2008**
and still circulates on scraped lists, plus six editors whose mastheads have changed
(Lifestyle Asia → Esquire, Grazia → The Word, T+L India's EIC superseded in Jan 2026).

**This is a better automation candidate than more scraping.** A weekly verification pass over
the `Verify` rows — confirm masthead, update or retire — compounds in value and protects her
from pitching a dead critic to a Taj client. Nothing in the current plan does this.

---

## Two risks worth raising with her

**There may be two master lists in circulation.** The sheet's own README says v6 could not be
written into the existing sheet, so it was uploaded as a *new* file, with instructions to do
File → Import → Replace into `…1mhhktHrD2aT…` — the URL that **Pooja, Sazia and Disha** have
bookmarked. That import may never have happened. I cannot open that other sheet at all, so I
can't tell which one the team is actually editing. **Ask her directly** — if the team is adding
contacts to one file while automation reads another, the tracker will drift permanently.

Also note two new team names: **Sazia and Disha**, alongside Pooja.

**MAV is flagged as unscientific in her own sheet, correctly.** Only Free Press Journal has a
real published rate card; everything else is estimated from Instagram follower counts as a
reach floor. The sheet itself cites AMEC and PRSA calling AVE multipliers unsupported by
peer-reviewed research. Any client-facing report we generate must carry that caveat — presenting
these as rupee values of earned coverage would be indefensible if a client pushed back.

---

## What this changes in the build plan

**Step 2 gets cheaper and more likely to work.** Before rewriting the coverage tracker: switch
on the 30 Google Alerts, and point the skill at the qualified queries already in the sheet.
Then see what the existing logic produces. There is a real chance the tracker mostly works once
its prerequisite exists.

**Add a weekly media-list verification pass** as a scheduled task. 150 unverified contacts is a
standing liability in a business whose product is knowing who to call.

**Group the client projects by restaurateur, not one per brand.** Sixteen brands under three
people means one Aditi Dugar project covering Masque, Sage & Saffron, TwentySeven BakeHouse,
Paradox and Circle 69 is closer to how the work actually happens than five separate projects
that each need the same relationship context.

**Resolve the two-list question before automating anything that reads the media list.**
