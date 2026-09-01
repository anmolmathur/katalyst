# Migration Architecture — Build on Mine, Run on Hers

_1 Sep 2026. Success is defined as: everything working in the nikhilapalat@gmail.com Claude
account, not mine._

That definition is the right one, and it changes how the work should be sequenced — because
what actually crosses between two Claude accounts is narrower than it looks.

---

## What migrates, and what doesn't

| Component | Migrates? | How |
|---|---|---|
| **Skills** | Yes, cleanly | Files. Travel inside the plugin. |
| **Sub-agents, slash commands, hooks** | Yes | Same — part of the plugin package. |
| **Connector *declarations*** | Yes | The plugin declares which MCP connectors it needs. |
| **Connector *authentication*** | **No** | Each account signs in to its own Google, Canva, SharePoint. Hers must be authorised as her. |
| **Scheduled tasks** | **No** | Not a plugin component. Recreated by hand in her account — but if each one just invokes a plugin skill, that's a one-line recreation. |
| **Projects and project instructions** | **No** | Copy-paste. Text, so cheap, but manual. |
| **Artifacts / dashboards** | **No** | Published under whoever creates them. Must be republished from her account or she only ever gets a guest link to mine. |
| **Chat history** | No | Doesn't transfer, and doesn't need to. |
| **Personal memory** | Technically yes, via Settings → Memory export/import | **Don't.** Her memory should be built from her work, not seeded with mine. |

The pattern: **everything durable goes in the plugin; everything identity-bound gets set up
once in her account.**

---

## The vehicle: a private GitHub repo as a marketplace

Cowork accepts a Git repository as a plugin marketplace. Add the repo URL once under
Customize → Plugins → Add marketplace, install from it, and click **Update** to pull later
changes. That is the migration path — not a hand-off, a subscription.

I build and version the plugin in one repo. Both accounts install from that same repo. When I
fix a brand rule six months from now, she clicks Update.

**The repo must be private.** It will contain per-brand guidelines, banned-word lists and
property facts for Taj, IHCL and her F&B clients — client-confidential material that has no
business sitting in a public GitHub repo. Private marketplaces work, but they authenticate
through git credentials, which means a one-time setup on her Windows machine. Do that during
the handover session, while I'm already on her machine.

**Fallback if the git setup fights us:** Cowork also installs a plugin from an uploaded package
file. Zero friction, but updates become manual re-uploads. Fine as a starting point, worth
graduating off.

### Repo layout

```
katalyst-plugins/
├── .claude-plugin/
│   └── marketplace.json          # name, owner, plugins[]
└── plugins/
    └── katalyst/
        ├── .claude-plugin/
        │   └── plugin.json       # name, version, description
        ├── skills/
        │   ├── nikhila-voice/SKILL.md
        │   ├── brand-vocabulary-guard/SKILL.md
        │   ├── daily-coverage-tracker/SKILL.md
        │   ├── monthly-report-builder/SKILL.md
        │   └── ... one directory per skill
        ├── agents/
        └── .mcp.json             # connector declarations
```

She then adds the marketplace and installs `katalyst`. One step, everything arrives.

---

## The thing that breaks the "build on mine, then move" plan

**Most of this work cannot be meaningfully tested on my account.**

The coverage tracker reads *her* Gmail for Google Alerts, *her* two Sheets, and emails *her*
team. Run on my account, it reads my inbox and finds nothing — a green run that proves
absolutely nothing. The same is true of anything touching her Canva brand folders, her Drive,
or her plan tracker.

So the split has to be by *what the thing depends on*, not by phase:

**Author on my side** — anything that is just files. Skills, agent definitions, the plugin
manifest, prompt logic. Fast to iterate, costs her nothing, and the output is portable by
construction. This is most of the intellectual work.

**Wire and validate on her account** — connector authentication, scheduled tasks, projects, the
Artifact dashboards, and *every* end-to-end test. Since I already have access, there's no
reason to simulate what I can do for real.

The mistake to avoid is building a beautiful tracker against my inbox, migrating it, and
discovering on her account that half the assumptions were wrong.

---

## Three practical guardrails while working in her account

**Don't email Pooja during testing.** Her tracker's final step sends directly to
pooja.katalyst@gmail.com, CC'd to Nikhila — not a draft. Point that at my own address, or at
Nikhila only, until the run is genuinely stable. Sazia and Disha shouldn't get test mail
either.

**Every test run burns her usage, not mine.** She's on Pro. A few days of debugging a scheduled
task will eat into what she needs for actual client work. That's an argument for doing the Max
5x upgrade *before* the heavy testing phase rather than after — or keeping iteration on my side
and spending her quota only on real runs.

**Don't touch her live Sheets while testing.** The tracker writes rows into the coverage
workbook. Point test runs at a copy until the logic is proven, then switch the path. Her sheet
has 52 hard-won rows in it and no version history worth relying on.

---

## Revised sequence

1. **Set up the repo and plugin skeleton** — my side, no account needed.
2. **Audit and port her existing skills into it** — my side. This is where the bulk of the value
   is, and it's all files.
3. **Install on her account, authenticate her connectors** — her side, one sitting.
4. **Switch on the 30 Google Alerts** — her side, 25 minutes, and quite possibly the actual fix
   for the coverage tracker.
5. **Validate the tracker end to end against a copy of her sheet** — her side, email redirected.
6. **Recreate the scheduled tasks as one-line skill invocations** — her side, quick once the
   skills exist.
7. **Build the per-client projects and dashboards in her account** — her side, because Artifacts
   belong to whoever publishes them.
8. **Handover session** — teach her to edit a skill, commit, and click Update. That is the
   moment she becomes self-sustaining, and it's the real finish line.

Steps 1 and 2 don't need her account at all, so they can start immediately.
