# Katalyst

Working repository for Katalyst Reputation Management's Claude setup — the installable
plugin, the planning documents behind it, and snapshots of the working data.

Maintained by Anmol Mathur for Nikhila Palat. Private.

## What's here

| Path | What it is |
|---|---|
| `plugins/katalyst/` | The installable Cowork plugin — skills Claude loads |
| `.claude-plugin/marketplace.json` | Makes this repo installable as a plugin marketplace |
| `artifacts/coverage-desk.html` | Source of the Coverage Desk dashboard |
| `docs/` | The reasoning: audit findings, architecture decisions, build plan |
| `data/` | Point-in-time snapshots — **not** the live source |

## Installing the plugin

In Claude (Cowork), open **Customize → Plugins → Add marketplace** and enter this
repository. Then install **katalyst** from the list. Click **Update** on the marketplace
later to pull changes — that is how fixes reach everyone without a re-handover.

This repo is private, so git credentials are needed the first time. On a machine with the
GitHub CLI:

```
gh auth login
gh auth setup-git
```

If that proves awkward, the plugin can also be installed from an uploaded package file
instead — same contents, but updates become manual.

## The live sources are elsewhere

Nothing in `data/` is authoritative. The live workbook is a **Google Sheet** — the coverage
tracker writes to it and the Coverage Desk reads from it. The CSVs here are a snapshot from
1 Sep 2026, kept so the deduplication work is reviewable, and they go stale the moment a new
placement is logged.

**The workbook must stay a native Google Sheet.** Uploaded `.xlsx` files come back from the
Drive connector as unparseable flattened text rather than clean tables, and the dashboard
cannot read them. See `docs/02-sheets-audit.md`.

## What must never be committed here

- **The media list.** It holds journalists' personal mobile numbers and home addresses.
  It stays in Drive, behind normal access control, and never enters a git repository.
- **API keys or tokens.** The coverage tracker uses Claude's built-in web search and needs
  no key at all. If one is ever added, it belongs in the connector settings, not in a file.
- **Client contact details** of any kind.

Coverage data — publications, links, dates, MAV — is fine. Contacts are not.
