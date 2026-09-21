# Task 7 — Per-client actionable dashboards

_9 Sep 2026. Built on Anmol's account, to be configured by hand in Nikhila's. Everything below
is a step you perform; nothing here runs on its own._

## What this is

The Coverage Desk answers "how are we doing" across the roster. This answers the other question,
the one she actually asked for after building the informational IHCL page: **what do I have to do
about this client today.**

It is one Artifact, not thirty. A group filter and a client rail across the top, then everything
below is about the selected client. Thirty separate pages would mean thirty publishes now and
thirty republishes every time a rule changes, and she would be maintaining them after you step
back — which is the opposite of the brief.

Every item on the page is **derived from the workbook on each load**. Nothing is ticked off and
nothing is stored. Log the coverage, or set the plan row, and the item disappears by itself.
That is the whole reason it needs no upkeep.

### What it shows, per client

The work order comes first — a numbered list of what is open, worst first, each with why it
matters and what to do about it. Under that: the month so far against last month, the plan
status for this month and next, the client's coverage feed, and a report-readiness table of every
row that would weaken a monthly report if it went in as it stands. At the bottom, an "ask about
this client" box scoped to that client's figures only.

The rules it applies:

| Signal | When it appears |
|---|---|
| Monthly plan never filed | Current month has no PLANS row, a blank status, or "Not started" |
| Plan waiting on approval | Marked sent 4+ days ago, or marked sent with no date |
| Next month's plan due | Not started and today is the 20th or later (the 14th–19th gives a softer warning) |
| Coverage gone quiet | 30 days warns, 60 days or never-logged is urgent |
| Alert not confirmed | `Alert Created?` on CLIENTS is not a yes |
| Not report-ready | Rows missing tier, valuation or link; dates flagged verify; duplicate rows |

A client with **no rows at all on the PLANS tab is not treated as a plan client** — the page says
so and makes no plan demands of it. That is the switch: add a PLANS row and plan chasing turns on
for that client; delete its rows and it turns off. No extra column to maintain on CLIENTS.

### One thing worth copying back into the Coverage Desk

This page **finds the workbook by name**, not by file id — it searches Drive for
`Katalyst_PR_Coverage`, prefers an exact title match, then reads it. File ids differ between
accounts, so the Coverage Desk's hardcoded id would have had to be edited before republishing
from her account. This one does not. Worth giving the Coverage Desk the same treatment next time
you touch it.

---

## Before you start

The workbook must be **a native Google Sheet in her Drive, named exactly
`Katalyst_PR_Coverage_WORKING`**. An uploaded .xlsx will not be read by the connector — that
gotcha is already in the project notes and it will bite here too. If she has renamed it, either
rename it back or change `WORKBOOK_TITLE` and `SEARCH_FRAGMENT` at the top of the page script.

---

## Step 1 — Add the PLANS tab

`data/PLANS_tab_scaffold.csv` in the repo has the header row and one row per client for September
and October 2026, sixty rows, all "Not started".

1. Open `Katalyst_PR_Coverage_WORKING`, add a tab, name it exactly **PLANS**.
2. Paste the CSV contents into A1. (File → Import → Insert new sheet also works and splits the
   columns for you; pasting straight in may need Data → Split text to columns.)
3. Select D2:D — Data → Data validation → Dropdown, with these five values, in this order:
   **Not started · Drafting · Sent for approval · Approved · Published**. The page matches on the
   first word, so close variants still work, but the dropdown stops typos creating a sixth state.
4. **Delete the rows for clients she does not do monthly social plans for.** Those clients then
   drop out of plan tracking entirely. This is the one judgement call in the setup and it is hers
   — ask her which of the thirty are PR-only before you delete anything, or leave all sixty in
   and let her delete them in the first session.

Column meanings, for the note you leave her: `Month` is `YYYY-MM` so it sorts; `Sent On` is the
date the deck went to the client, which is what the approval chase counts from; `Approved On`
closes it; `Deck Link` becomes an "Open deck" link on the page.

## Step 2 — Tick the alerts column

The `Alert Created?` column on CLIENTS is blank for all thirty, so every client will show
"Google Alert not confirmed" until it is filled. The alerts do exist — that was checked in her
account — so this is a data-entry gap, not a real one, and leaving it blank makes the desk cry
wolf on all thirty clients at once.

Put `Yes` against each client whose alert you can confirm. Twenty-five minutes, and it is the
same tick the Coverage Desk's readiness meter reads.

## Step 3 — Add the skill

`plugins/katalyst/skills/client-action-desk/SKILL.md` goes into the plugin alongside
`daily-coverage-tracker`. It applies exactly the same rules in chat, so the two never disagree,
and it can do what the page cannot — draft the chase email, sketch pitch angles, sweep the whole
roster for the week.

Push the repo, then in her account: Customize → Plugins → the Katalyst marketplace → **Update**.
If the plugin is not installed there yet, that install is part of the earlier handover, not this
task.

She invokes it as "what does Masque need?" or "what should I be chasing this week?".

## Step 4 — Publish the artifact from her account

Artifacts belong to whoever publishes them, and a page that reads a connector reads through the
*viewer's* connection. Published from your account she cannot open it. It has to be republished
from hers, which is the last step and the only one that touches her Claude directly.

1. Sign in to her Claude account and confirm **Google Drive is connected** under Settings →
   Connectors.
2. Start a new Cowork session and attach `artifacts/client-desk.html` from the repo.
3. Give it this instruction, near enough verbatim:

   > Publish the attached `client-desk.html` as an artifact, exactly as written — do not rewrite,
   > reformat or "improve" the file. Title: Katalyst Client Desk. Favicon: 🗂️. Declare these
   > capabilities: `{"mcp": {"servers": [{"server": "Google Drive", "tools": ["search_files",
   > "read_file_content"]}]}, "sample": {}}`

   The "do not rewrite" line matters. Without it the model may decide to restructure a 700-line
   page it did not write, and the version she ends up with will not be the one that was tested.

4. Open the published link **from the artifact card or the gallery**, and approve Google Drive
   when asked.
5. Pin the URL somewhere she will find it. The gallery at claude.ai/code/artifacts lists it.

## Step 5 — Check it landed

Open it and confirm, in this order:

- The stamp top-right shows a client count and a placement count rather than "not connected".
  Thirty clients and fifty-five placements is the current shape of the workbook.
- The rail headline names a number of clients needing something today, and the dots are not all
  the same colour.
- Click three clients — one with coverage (St. Regis Goa), one with none (Masque), one with a
  plan row — and check the work order changes and reads sensibly.
- The report-readiness table on St. Regis Goa flags around ten possible duplicates. That is real:
  the ₹-valued rows duplicate the "Rs."-valued ones from an earlier pass. Worth raising with her
  separately — it double-counts both the placement and its MAV.
- The "ask about this client" panel appears. If it does not, the `sample` capability was not
  declared and step 4 needs redoing.

---

## Constraints to keep in mind

**It only works inside Claude.** The page holds no data of its own. Downloaded and opened from a
Downloads folder it will say so rather than spin, but tell her anyway: open it from the artifact
link, never from a saved file.

**It cannot be shared publicly.** A page granted connector access cannot be given a public link —
the grant is per-viewer and consented. That is correct rather than limiting here: it makes
leaking the roster through a shared link structurally impossible. Anyone at Katalyst who needs
it opens it in their own Claude with their own Drive connected, which also means they see it
through their own permissions.

**Client-facing versions are a different build.** A page for a client is a published snapshot
with the figures baked in at generation time — no connector, no contact data, no other clients.
Not this page with a filter on it.

**Everything red is not a bug.** On today's data most clients show critical, because the alerts
column is blank and no plans are recorded. That is an honest reading of the workbook, and it
resolves as steps 1 and 2 get done. If it still reads red after that, the finding is real.
