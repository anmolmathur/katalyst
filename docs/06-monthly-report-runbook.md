# Monthly media coverage report — configuration runbook

_Task 5 from `00-context-and-tasks.md`. Written 9 Sep 2026. This is the sheet Anmol works
from to configure the report builder in Nikhila's Claude; the skill itself is written for
Claude to follow, and the two should not be confused._

## What was built

Four files, all inside the existing `katalyst` plugin, so this ships through the same install
Nikhila already has rather than as a second thing to set up:

    plugins/katalyst/skills/monthly-coverage-report/
      SKILL.md                          the skill Claude follows
      references/intake-checklist.md    the Stage 1 form she fills each month
      references/deck-spec.md           the 18-slide map and the theme table
      scripts/build_deck.py             the PPTX builder

Three decisions, taken 9 Sep against the alternatives in the task list:

**PR coverage and social in one report.** The earned coverage comes out of the workbook
automatically; the social numbers come from the intake because Meta sits behind her login.
That split is permanent by design, not a stopgap — the Meta Graph API is a later upgrade and
is not needed to ship this.

**One template with a per-client theme block, rather than a Taj-only deck.** Taj and the wider
IHCL family get gold, white and Trajan Pro; everything else gets a neutral house theme until
somebody adds a row with that client's real brand colours. Sofitel, JW Marriott and the
independent restaurants are more than half the roster and a Taj-styled deck is wrong for all
of them.

**PPTX out of Claude, which she finishes herself.** Closest to how she works now and it needs
no extra tooling. The deck is a draft; she reviews, edits and sends.

## The finding that needs her decision before first use

**Not one of the 44 rows in `ALL_COVERAGE` carries a numeric media value.** Thirty-eight of
the `MAV (Rs.)` cells hold explanatory text — `N/A - no public reach/rate data found` and
similar — and six are empty. The column cannot be summed and never could be.

The skill works around this by computing value from the `MAV_RATES` rate card instead: tier
base rate times placement multiplier, showing the arithmetic, excluding untiered rows from the
total and reporting how many were excluded. That produces a defensible number from data that
is actually present.

But it is still an estimate built on a rate card with no published source behind it, and the
workbook itself cites AMEC and PRSA holding that AVE multipliers are unsupported by research.
So the deck carries that caveat on the media-value slide, visibly.

**Ask her directly whether she wants a rupee figure in a client deck at all.** Some agencies
report media value; some have stopped precisely because of the AMEC position; some report it
only where a real rate card exists. It is her call as the principal, and it is better made
once now than negotiated every month. If she wants it out, the fix is to drop slide 12 and the
fourth figure on slide 4 — tell her it is a two-line change, not a rebuild.

## Installing it

**If the plugin marketplace is already wired up** — which is the plan in `repo.md`, though the
repo had not been pushed as of 1 Sep — this ships as an update. Commit, push, and she clicks
Update on the marketplace. Nothing else to do.

**If the repo still is not pushed**, push it first:

    gh repo create katalyst --private --source=. --remote=origin --push

Keep it private. The plugin will grow to hold per-brand guidelines, and the repo README already
records what must never be committed: the media list, any keys, and client contact details.

**If plugin installation proves awkward on her machine**, the fallback is to paste the four
files into a project's knowledge in her Claude account. It works, but she then has no update
path and every fix becomes a second handover — so try the marketplace route first. She is on
Windows; `gh auth login` and `gh auth setup-git` once during handover is what makes a private
marketplace authenticate.

## Fill these in before the first run

Two things in the shipped files are placeholders and should not stay that way.

**The Katalyst accent colour** in `THEMES` inside `build_deck.py` is `#A67C52`, a warm neutral
chosen to sit quietly beside a luxury client's own branding. Their real brand hex codes are not
on file. Get them from her and replace it. It is marked as a placeholder in both the script and
the deck spec so nobody later mistakes it for a brand standard.

**Per-client themes.** Only `taj-gold` and the house default exist. St. Regis, Sofitel, JW
Marriott and Sheraton all have brand guidelines she will have on hand. Add a row each, using
their real colours. Do not invent a palette — a neutral deck is a better failure than a
confidently off-brand one on a Marriott account.

Also worth confirming with her: **where the finished decks are filed**, and whether the report
month should follow the calendar month or her billing cycle. The skill assumes calendar.

## Testing it before she sees it

Run it against **Taj Krishna**, which is her own worked example, or against **St. Regis Goa
July 2026**, which is the fullest month in the workbook at sixteen placements.

It has already been dry-run here against the real deduplicated coverage data. St. Regis Goa
July 2026 produced a seventeen-slide deck: sixteen placements, thirteen publications, two
Tier 1, ₹7,25,000 computed, two placements correctly excluded for having no tier on file. A
one-placement month produced nine slides rather than padding to eighteen. Three layout bugs
were found and fixed in that pass — the contents slide ran into the footer past ten entries,
a long rupee figure wrapped into its own label, and the publications table silently dropped
five of thirteen outlets. Worth knowing they were found by rendering the deck and looking at
it, which is the check to repeat after any change to the builder.

What to look at in a test deck, in order:

1. **The media-value slide** — is the caveat there, is the arithmetic shown, does the excluded
   count match what the log shows as untiered.
2. **The coverage log** — every placement present, dates in the right month, no invented
   publication where the workbook says to-be-confirmed.
3. **The theme** — right palette for the client, and check whether Trajan Pro actually rendered
   on her Windows machine or silently substituted.
4. **The empty sections** — with no intake filled in they should read `Not reported this month`,
   not sit blank and not be quietly dropped without a note.

## What to tell her

Three things, and the first is the one that matters:

**The intake is the deal.** Ten minutes of typing a month buys the half of the report that no
automation can reach — the social numbers, what the agency actually did, and the context that
turns a count of placements into a report. Without it she gets a competent coverage summary and
nothing else. The form is deliberately blunt about leaving fields blank rather than guessing,
and that instinct is worth reinforcing: a repeated follower count reads as data and is worse
than an absence.

**The deck is a draft, every time.** It does not send, does not file itself, and is not marked
final. That matches how her own AlikhiN design already works — drafts to Gmail for review
rather than sending blind — so it should feel familiar rather than restrictive.

**A quiet month gets a short deck.** Twelve true slides beat eighteen with six hollow ones, and
a client on a retainer notices padding. The skill will offer the short form and ask before
building the long one anyway.

## Where this sits next to the other tasks

The daily coverage tracker feeds this. Every improvement there — a tier filled in, a publication
name resolved, a duplicate caught — shows up as a better report at month end, which is the
argument for keeping the tracker's data clean rather than treating it as a log nobody reads.

Two gaps carry straight through and she should know it: the Condé Nast India titles and
Travel + Leisure Asia cannot be reached by the tracker, and print-only coverage is invisible to
it. The intake has a section for exactly this so those placements still reach the report. Worth
saying out loud when handing it over, because a report that quietly omits a Vogue India feature
is the failure that costs trust.

A scheduled task on the 1st is tempting and probably premature. Better to run two months by
hand first, see where the intake actually snags, and only then automate the reminder — and even
then it should prepare a draft, never send.

## Not built, deliberately

**Meta Graph API access.** Manual intake ships now and matches how she already works. Revisit
only if the monthly typing becomes the bottleneck, which it may not.

**Charts as images.** The deck uses native PowerPoint charts so she can edit them. Images would
look marginally better and would be useless the moment she wants to change a label.

**Auto-filing to a client folder.** Deliberate. Nothing reaches a client without her.
