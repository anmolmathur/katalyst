# Build Plan — Katalyst on Claude

_Decisions taken 1 Sep 2026, after Nikhila cleared access to her Netlify and Claude accounts._

## The three decisions

**Architecture: native, packaged as a plugin.** Everything is built as skills, projects and
scheduled tasks inside her own Claude account, then bundled into one installable **Katalyst
Cowork plugin**. Nothing important lives on infrastructure only I can maintain.

**Plan: Max 5x (~$100/mo).** Pro already includes Cowork, projects, Claude Code, Design and
Opus — her ceiling was never access, it was usage. Max 5x is what stops a report build dying
halfway through. Team seats are the later conversation, once the per-client projects exist and
Akanksha and Pooja actually need in.

**Data layer: free first.** Google News RSS costs nothing and needs no key. Brave Search is the
paid fallback ($5/mo of free credits, ~1,000 queries, card required). We only spend money if
free genuinely fails.

---

## Why "packaged as a plugin" is the whole answer

The brief is that she should sustain herself after I step back. That rules out anything where
the intelligence sits in a prompt she has to remember to paste, or a server she can't restart.

A Cowork plugin bundles skills, connectors and sub-agents into one installable unit. Everything
we build goes in it. That gives her four things she does not have today:

**One install instead of fifteen setup steps.** Akanksha and Pooja install the plugin and have
the same brand guardrails, the same voice, the same report format she does.

**Versioning.** When a brand's hashtag rules change, the skill changes once and everyone gets
it. Right now her guidelines live in skills she edits individually and in her own head.

**Portability.** If she moves to Team seats later, the plugin moves with her. Nothing has to be
rebuilt.

**A place for things to belong.** Her current problem is that she can't tell which surface to
put something on. A plugin gives a single correct answer to "where does this go?" — which is
the mental-model fix from the other document, made structural instead of taught.

---

## What goes in the plugin

### Her existing skills — audit, don't rebuild

She wrote these herself and they are good. The work is review and consolidation, not
replacement.

| Keep as-is | Needs work |
|---|---|
| nikhila-voice, humanize-writing | katalyst-design-training-manual — split per brand family so Vivanta rules can't bleed into Taj Palace |
| brand-vocabulary-guard | katalyst-monthly-plan — pin to the actual Canva deck format she ships |
| customer-voices, competitor-voices | monthly-report-builder — pin to 18-slide Taj format, add the data-intake step |
| pr-pitch-press-release-generator, client-onboarding-package | social-content-builder — reconcile with the reel constraints below |
| Client-specific: sheraton-chennai-seo-blogs, alter-ego-voice-tonality, rotary-reel-style | |

### One finding worth acting on immediately

**Her `art-prompting` skill already does what my prompt converter does.** It turns rough
one-line asks into structured Act as / Request / Terms prompts. Publishing my prompt-maker for
her would be building a second version of something she already owns and uses.

**Drop that task.** Sharpen her skill instead — feed it the GOAL / DELIVERABLES / WORKFLOW /
GUARDRAILS structure I've been writing by hand, so her own tool produces what I produce. That
is strictly better for self-sufficiency and it costs an hour instead of a hosting setup.

### New skills to write

- **`daily-coverage-tracker`** — her V2 logic, with Google News RSS as the search layer.
- **`reel-template-builder`** — frames only, with the motion handoff made explicit.
- **`client-dashboard`** — generates the per-client Artifact from her live Sheets.
- **`katalyst-router`** — a front door that answers "which of my skills do I want right now?",
  because fifteen skills is past the point where she'll remember them all.

---

## Build order

### Step 1 — The map session, and rotate the key
An hour, live. Chat vs project vs skill vs scheduled task vs plugin vs Design, and which has
memory, connectors and unattended runs. AlikhiN is the worked example: right agent, wrong
container. Rotate the search API key in the same session so it's done.

Nothing else lands properly until she has this map, and it costs almost nothing.

### Step 2 — Coverage tracker, end to end
The closest thing to done and the most visible daily win. Preserve her 20-minute budget and
three-tier priority order — that logic is hers and it works. Replace the search step with
Google News RSS queries per client, keep the verification rule that every hit gets opened
before it's logged, keep the Pooja email exactly as specified.

Run it three days on her account before calling it done.

### Step 3 — Plugin skeleton and one pilot client
Scaffold the plugin, move the audited skills in, and take **Vivanta Hyderabad** end to end:
its own project, its own instructions, its Drive and Canva folders wired in, a monthly plan
generated, and an actionable dashboard Artifact on top. One client done properly is the
template for the rest — and it's the proof she needs before restructuring 50-odd projects.

### Step 4 — Reels, rescoped honestly
Frames in Canva as editable full-bleed fills; motion set by hand in the Reel timeline. Build
the reference-intake format so describing a reel takes her two minutes. If she wants true
automation later, the fallback is assembling the MP4 outside Canva from exported frames — but
that leaves her workflow, so it's her call, not mine.

### Step 5 — Monthly report
Data intake first, generator second. Manual Stage 1 through a checklist, matching how she
already works. Meta Graph API is a later upgrade, not a prerequisite.

### Step 6 — Hosting, and handover
Move katalystrm.com and AlikhiN onto her Netlify. Squarespace stays as registrar only. Then a
second session walking her through editing the plugin herself — the actual finish line.

---

## What I am deliberately not building

**Anything on a server I maintain.** If it can't live in her Claude account, it needs a very
good reason.

**A replacement for her prompt library.** She writes good prompts. The gap was never quality.

**Fully autonomous publishing.** Queue and approve, always. Her own AlikhiN design already
drafts to Gmail drafts rather than sending blind — that instinct is right and it should hold
as the automation grows.

**A custom Canva MCP.** Her session already established that Canva's API doesn't expose
transitions or timing to anyone. A custom server can't call an endpoint that doesn't exist.
