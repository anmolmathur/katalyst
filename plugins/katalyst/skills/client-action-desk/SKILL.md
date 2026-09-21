---
name: client-action-desk
description: Work out what a Katalyst client needs right now — plan filed or missing, coverage gone quiet, monitoring not set up, rows that would weaken the monthly report — and draft the chase. Use for a single client before a call, for a weekly sweep across the roster, or when asked what to chase today.
---

# Client action desk

Turns the coverage workbook into a list of things to do about one client, or about the whole
roster. It is the chat half of the Client Desk dashboard: same data, same rules, but it can
draft the email, write the pitch angle and look things up that the page cannot.

**This skill reads and advises. It does not write to the workbook.** The Google Drive connector
cannot put cells into an existing sheet — see `daily-coverage-tracker` for the Apps Script that
closes that gap for coverage rows. When something here needs recording, hand back the row to
paste and say where it goes.

## Configuration

| Setting | Value |
|---|---|
| Workbook | `Katalyst_PR_Coverage_WORKING` (a native Google Sheet, not an .xlsx upload) |
| Tabs read | `ALL_COVERAGE`, `CLIENTS`, `PLANS` |
| Dashboard | Artifact **Katalyst Client Desk** — same rules, live, in the artifacts gallery |

Find the workbook by name rather than by file id. The id differs between accounts and copies.

## Step 1 — Read the three tabs

Read the whole workbook in one call. It comes back as markdown tables; take the table whose
header row matches, not the one in a particular position.

- `ALL_COVERAGE` — Date, Client, Group, Publication, Tier, Reach, Topic, Link, Placement Type,
  MAV, Notes, Date Note, Logged On.
- `CLIENTS` — Client, Group, Google Alerts Query, Key People, Setup Notes, Alert Created?, Status.
- `PLANS` — Client, Group, Month (`YYYY-MM`), Status, Sent On, Approved On, Deck Link, Notes.

If `PLANS` is missing, say so once and carry on without the plan checks. Do not invent plan
status from anything else.

A client with rows in `ALL_COVERAGE` but no row on `CLIENTS` is still a client — report it, and
flag that it is off the roster.

## Step 2 — Work out what is open

Apply these rules exactly. They are the same ones the dashboard uses, so the two never disagree.

### Monthly plan — only for clients that have any row on `PLANS`

A client with no `PLANS` rows at all is not a plan client. Make no plan demands of it.

| Condition | Severity | The action |
|---|---|---|
| Current month has no row, a blank status, or "Not started" | Do today | Find out whether the deck exists. If it does, the row needs updating; if not, the month is running unplanned |
| Current month is "Drafting" or similar | This week | Finish and send it |
| Current month is "Sent for approval" and `Sent On` is 4+ days ago, or `Sent On` is blank | This week | Chase the approval |
| Next month not started and today is the 20th or later | Do today | The plan should be with the client before the month turns |
| Next month not started and today is the 14th–19th | This week | Start the deck |
| Current month "Approved" or "Published" | — | Nothing open |

The 20th is the marker because that is the day her existing reminders fire.

### Coverage silence

| Condition | Severity |
|---|---|
| No coverage ever logged | Do today |
| 60+ days since the last placement | Do today |
| 30–59 days | This week |

**Always read zero coverage as a monitoring failure first.** On this roster it almost never
means nothing was written — it means nobody was looking. Say that plainly rather than implying
the client had a quiet month.

### Monitoring

If `Alert Created?` is not a yes, that client is invisible to the daily tracker every morning.
Quote the exact query from `CLIENTS` so it can be pasted into Google Alerts. **Never suggest
searching the bare client name** — a third of this roster (Masque, Swan, Paradox, Circle 69,
Papaya, Gigi, Botie, Raga, Alter Ego, Ikai) is unsearchable without its qualifier.

### Rows that are not report-ready

Count, per client: rows with no Tier; rows with no usable MAV; rows with no link that are not
print; rows whose Date Note says verify or TBD; rows that duplicate another row on the same
normalised link, or the same publication on the same date.

Report these as one item — "N placements not ready for a report" — and list the specifics only
when asked, or when a monthly report is actually being built.

If both rupee-symbol figures and "Rs." figures appear against one client, say so: those are two
different valuation methods (Katalyst's own rate card, and a CPM estimate from follower counts)
and totalling them produces a number that cannot be explained if the client asks.

## Step 3 — Answer

**For one client**, lead with the single most urgent thing in one sentence, then the rest in
priority order. Name dates, publications and day counts. End with what you can do next — draft
the chase, sketch three pitch angles, build the alert query.

**For a weekly sweep**, rank the whole roster and report only what is open. Group by severity,
not by client, so the reader sees the shape of the week. Fifteen quiet clients is a finding —
say it in a line rather than listing them.

## Drafting

When asked to draft a chase or a pitch:

- Plain, warm, unfussy English. No marketing language, no exclamation marks, no "excited to".
  These are luxury hotels and restaurants and the writing is judged accordingly.
- Reference the actual thing — the plan's month, the date it was sent, the property, the named
  chef or GM from `Key People`.
- Never claim coverage, a date or a figure that is not in the workbook.
- Draft only. Nothing goes to a client or a colleague without Nikhila reading it first.

## Guardrails

- **Never invent a placement, publication, date or MAV.** If the workbook does not have it, say
  so. A fabricated line in a coverage conversation is worse than a gap.
- **Every MAV is an estimate.** AMEC and PRSA both hold that advertising-value multipliers are
  unsupported by research; only Free Press Journal has a real rate card on file. If a figure is
  going anywhere near a client, carry the caveat with it.
- **Do not write to the workbook**, and do not offer to. Hand back rows to paste.
- **Do not email anyone.** This skill produces drafts.
- Client names, contacts and coverage are confidential. They stay in the session.
