# Dashboards and Chat, Without a Database

_1 Sep 2026. Sheets stay the system of record. The upgrade is in how they're **shaped** and
what reads them._

The reason her sheets feel unusable isn't that they're spreadsheets. It's that the coverage
workbook is **thirty sibling tabs that cannot be queried together**, and the media list is
twenty-one. Any question spanning clients requires opening thirty tabs by hand. That is a
structural problem, and it has a structural fix that costs nothing and needs no migration.

Three layers: reshape the sheets, put Artifacts on top, and give her two places to ask
questions.

---

## Layer 1 — Invert the coverage workbook

Today: one tab per client, rows appended to whichever tab matches. Thirty write targets, no way
to read across them.

**Flip it.** One flat table, `ALL_COVERAGE`, becomes the single write target:

```
Date | Client | Group | Publication | Tier | Reach | Topic | Link | Placement | MAV | Notes | LoggedOn
```

Every per-client tab becomes a one-line QUERY view of it:

```
=QUERY(ALL_COVERAGE!A:L, "select * where B = 'Masque' order by A desc", 1)
```

Nothing is lost — she still opens "Masque" and sees Masque's coverage — but now every
cross-client question is a single query, and the tracker skill appends one row instead of
choosing among thirty tabs. It also makes the automation simpler and less breakable, which is
its own win.

**Two columns worth adding while we're in there.** `Group` (Kalra / Dugar / Udeshi / Hotels /
Independent) turns the restaurateur clustering into something queryable — sixteen of thirty
brands roll up to three people, and she currently can't see that. And `LoggedOn` separates when
coverage *appeared* from when we *found* it, which is the difference between a reporting metric
and a debugging one.

### A CLIENTS reference tab

One row per client: name, group, status, and — critically — **the qualified search query**.
Those thirty queries already exist, fully worked out, in the Google Alerts tab. Moving them into
a proper reference tab means the tracker skill reads its search string from data instead of
constructing one from the client name, which is the bug that made half the roster unsearchable.

**This is the schema.** Written in Sheets rather than Postgres, maintainable by anyone who can
edit a spreadsheet, and if we ever do move to a database, the modelling work is already done and
already validated against real use.

### The media list gets the same treatment

`ALL_CONTACTS`, one flat table with a `Source` column (Master / Regional-Mumbai /
Bloggers-Chennai …), and the existing tabs become QUERY views. Then "who covers F&B in Goa and
is marked Active" is one query instead of a manual sweep across thirteen tabs.

---

## Layer 2 — Artifacts as the application

A published Artifact on claude.ai can call the viewer's own connectors and read her Sheets
**live**, and it can ask Claude questions of its own. That is genuinely most of what the app was
for — with nothing to deploy, nothing to patch, and no 9pm outage.

Because it reads through the *viewer's* credentials, the same page works for both of you: opened
by you it reads via your connector, opened by her via hers. Migration is just republishing it
from her account.

### Three pages

**Katalyst Command Centre** — internal, the morning view. Coverage this month by client and by
group; **which clients have had nothing in 30 days** (the number that actually matters, and
today invisible); tier mix; top publications; which monthly plans are filed versus missing. This
is the consolidated view the original meetings asked for, and it replaces the "morning dashboard
email" idea with something better — always current, no scheduled run to fail.

**Client review page** — one client or one group, coverage timeline, placements, tier
breakdown. What she opens before a client call.

**Media list health** — the Verify backlog by city and tier, stale mastheads, contacts with no
recent placement. This one earns its place: 150 unverified contacts is a standing liability, and
right now nobody can see the number.

### One constraint that shapes the design

A page granted connector access **cannot be publicly shared** — the grant is per-viewer and
consented. That rules out live client-facing portals on this route, and I think that's correct
rather than limiting: it makes it structurally impossible to leak the contact database to a
client link. Client-facing pages come later as **published snapshots** — coverage and analytics
baked into the page at generation time, no connector, no contact data. A monthly client report
is a snapshot anyway.

---

## Layer 3 — Two places to ask questions

**In Claude** — AlikhiN rehomed into a project with the plugin and the Drive connector. Full
power: reads the sheets, writes plans, drafts emails, builds reports. This is where real work
happens, and it's the fix for AlikhiN being stranded on a static page.

**In the dashboard** — the same pages can carry a chat box that asks Claude about what's on
screen. "Why has Masque had nothing this month?" or "summarise the Dugar group's quarter"
answered without leaving the page. It has no memory between questions, so it's for quick
interrogation of visible data, not for doing work — and that division is the right one to teach
her, because it's the same chat-versus-project distinction she struggles with everywhere else.

---

## What this actually gives up versus Postgres

Worth being straight about it. No enforced schema, so a typo in a client name creates a phantom
client. No history or audit trail. No real joins at scale. No concurrent-write safety beyond
what Sheets provides.

At her volume — 30 clients, ~730 contacts, roughly 50 coverage rows a month — none of those
bite. **The honest trigger for revisiting Postgres:** when coverage rows pass a few thousand,
when more than three or four people need to write at once, or when a client contractually wants
a live portal. Until then this is not a compromise, it's the correct amount of machinery. Revisit
it when one of those three things is true, not on a calendar.

---

## Order of work

1. Restructure the coverage workbook to `ALL_COVERAGE` + QUERY views, on a **copy** first.
2. Build the CLIENTS tab, moving the thirty qualified queries out of the Alerts tab.
3. Point the coverage tracker skill at the flat table and the qualified queries.
4. Build the Command Centre Artifact against the reshaped sheet.
5. Same treatment for the media list, then the health dashboard.
6. Client snapshot pages last.

Steps 1 and 2 are the highest-value hours in this whole plan. They're also the ones that make
everything downstream — tracker, dashboards, chat, and any future database — straightforward
rather than fiddly.
