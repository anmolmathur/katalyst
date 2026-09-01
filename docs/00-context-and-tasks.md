# Nikhila / Katalyst — Claude Setup: Context and Task List

_Prepared 31 Aug 2026 from the two meetings of 29–30 Aug; revised 1 Sep after reading
katalystrm.com and the WhatsApp history from 22 Jul onward._

## The situation

Nikhila runs a luxury hospitality PR and marketing agency, and she is much further along
with Claude than the meeting notes alone suggest. She has written a full skills library,
built and deployed a named agent, and set up live tracker Sheets and fixed output formats —
all unaided. Her prompts and her groundwork are genuinely good. What is missing is a map of
which Claude surface does what, and beyond that the failures are mostly hard platform limits
rather than anything a better prompt would fix.

Five things are actually in the way: she can't tell the surfaces apart (chat, project, skill,
scheduled task, agent, Design), context gets thrown away by starting fresh chats, the model
tier is too low for her harder work, two data sources are inaccessible (SharePoint and Meta
analytics), and the coverage tracker was searching the model's own recall instead of the live
web. Only the last of those is a prompt problem.

People in play: Nikhila Palat (principal — also referred to as "Nikhil" in my notes; same
person), who does this work hands-on herself; Akanksha, who holds the SharePoint tenant; and
Pooja, who receives the daily coverage email. Gaurav made the introduction.

Their stack today: Claude Pro at the $20 tier; Canva and Google Drive connected and
working; SharePoint connector installed but the tenant is not shared; skills for
marketing, brand guidelines, internal comms and web artifacts builder; plugins for
marketing, design, product management, sales and PDF viewer, with the bio plugin
deliberately removed. That last decision is the right principle — every extra plugin
is noise the model has to filter.

---

## The business, from katalystrm.com

Katalyst Reputation Management is an eleven-year-old Mumbai agency working exclusively in
luxury hospitality and lifestyle — hotels, restaurants, and premium consumer brands. The
tagline is "Every brand has a spark. We're here to Katalyze it," and the founding principle
is that "a brand's reputation isn't managed, it's authored."

Critically for what we build: **this is not a PR shop.** They sell five integrated lines, and
any tool we hand over has to sit inside that reality.

| Line | What it covers |
|---|---|
| Reputation & PR | Media relations, brand storytelling, coverage |
| Design & Branding | Packaging, print, menus, merchandise |
| Digital & Social | Social strategy, community building |
| Marketing & Strategy | Calendars, campaigns, media planning |
| Recruitment & Training | Hiring and training the brand-facing staff |

Nikhila Palat founded it after seven years as Head of PR, Marketing & Communications at The
Taj Mahal Palace, Mumbai, with earlier roles at Taj Wellington Mews and Vivanta by Taj
President. Nearly two decades in luxury marketing, dual MBAs, diplomas from Harvard and
Glion, and a TED talk on influencer marketing. Her public position on the craft is worth
knowing before we write prompts in her voice: reputation takes years to build and a minute
to lose; tell a story rather than manage a narrative; learn from the unhappy customer; and
"the most important thing you are selling is not your food, but yourself." She argues from
real cases, never frameworks — so generated copy that reads as generic marketing language
will not pass her.

**Client roster (public):** Taj / IHCL family — The Taj Grand Palaces, Vivanta, IHCL
SeleQtions, Gateway Hotels. Independent restaurants — Masque, Masala Library, The Scarlett
House, Soraia, Fielia, Candy & Green, Sorena. International hotels — The St. Regis Goa
Resort, JW Marriott Kolkata, Sofitel. Coming up: RAGA by Gaggan Anand, Pali Bhavan, Paashh.
Historically also Gucci, Ulysse Nardin, Bell & Ross, Four Seasons, InterContinental, Conrad.
Best Design Agency at the Whisky India awards; 20+ brand launches in the last decade.

### What this changes about the build

The client roster is not 56 equal accounts. It is a small number of deep, high-stakes luxury
relationships — the IHCL family alone spans multiple properties — where a single off-brand
Instagram caption is a real reputational cost to a hotel that charges accordingly. That
should reshape three things:

**Per-brand voice is the whole game, not a nicety.** Masque and JW Marriott Kolkata cannot
share a content template. The per-client project structure (task 7) matters more than any
prompt we write, because it is what holds each brand's voice, guidelines and asset folder
apart from the others.

**Nothing should auto-publish.** Every generated post, caption and report needs a human
approval step before it reaches a client. Build queue-and-approve, never fire-and-forget.

**The design line means Canva output is a deliverable, not a convenience.** They won a design
award. Templates we generate get judged against that standard, so the reel and carousel work
(task 2) should lean on their existing brand kits in Canva rather than inventing layouts.

## What the WhatsApp history changes (22 Jul – 1 Sep)

The meeting notes undersold how far she already is. Reading the chat back, she is not a
beginner who needs prompts written for her — she has built a substantial Claude setup on her
own, and most of what is failing is hitting real platform ceilings, not bad prompting. That
changes what I should actually be building.

### What she has already built

**AlikhiN** — her named AI assistant, deployed as a static chat page at
`alikhin-katalyst.netlify.app`. It knows brand guidelines for the whole IHCL roster, writes
captions and reel scripts in brand voice, audits Canva plans, drafts team emails, reads the
live plan-tracker Sheet, and fires reminder emails on the 20th and 1st. She started it in
mid-August and, in her words, "just started her — want her to take over planning and coverage
tracking."

**A full skills library**, already written and in use:

| Area | Skills |
|---|---|
| Voice | nikhila-voice, humanize-writing, art-prompting |
| Katalyst core | katalyst-design-training-manual, brand-vocabulary-guard, katalyst-monthly-plan, social-content-builder, monthly-report-builder |
| Client-specific | sheraton-chennai-seo-blogs, alter-ego-voice-tonality (Krish Shah's restaurant), rotary-reel-style (Rotary Club of Bombay) |
| Business dev | client-onboarding-package, pr-pitch-press-release-generator, customer-voices, competitor-voices |

That reveals three clients the website doesn't name: **Sheraton Grand Chennai Resort & Spa,
The Alter Ego, and Rotary Club of Bombay.**

**Live working files** — a Master Media List Sheet (718 media contacts), a PR Coverage Tracker
workbook (one worksheet per client, with MAV columns), a monthly plan-tracker Sheet, and an
Instagram reference Sheet she works from by line number.

**Established output formats** — monthly social plans are Canva decks named like
`TajChandigarh_AUGUST2026_SocialMediaPlan_v2.pptx`, one page per post carrying title, caption,
timings, reservation numbers and hashtags. Monthly reports are 18-slide PPTX in Taj house
style: gold and white, Trajan Pro headings. Taj Krishna was the worked example.

**Other team member:** Pooja (pooja.katalyst@gmail.com) receives the daily coverage email.
Her working Gmail for all this is her personal account, not the katalystrm.com address.

### Her actual problem, in her own words

> "i cant tell the diff between what to schedule, what to use claude work for and what to use
> design for" … "i didnt really understand what an agent is supposed to do" … "i want them all
> to integrate"

That is a mental-model gap, not a prompt gap. She is building sophisticated things without a
map of which surface does what, so effort lands in the wrong place — the clearest example
being AlikhiN, where she put a genuinely good agent onto a static Netlify page that by
definition has no memory, no connectors and no scheduled runs, and then wondered why it
answered so thinly. **Teaching the map is worth more than any single prompt I hand over.**

### The three blockers are platform limits, not prompt quality

Her own Claude sessions already diagnosed these correctly, and I should not spend time trying
to out-prompt them:

**Canva's API cannot set transitions, timing or zoom.** This was confirmed with Canva's own
help service — the functionality is not exposed to any integration, so no connector and no
custom MCP can reach it. Anything we generate is a sequence of static frames; the motion has
to be set by hand in Canva's Reel timeline, or the video assembled outside Canva from
exported PNGs. This materially changes what "generate a reel template" can mean.

**Canva's export domain is network-blocked from Claude's sandbox.** Exported PNGs cannot be
fetched back, so rendering a video means she downloads the frames and attaches them manually.

**Meta Business Suite, Instagram, Facebook and X analytics are behind her login.** Claude
declined to log into her authenticated business accounts, correctly. Either set up proper
Meta Graph API access with tokens, or accept that Stage 1 of the report is manual collection —
which is how her workflow was already designed anyway.

**Instagram reels can't be played by Claude**, so reference pacing gets reconstructed from her
description rather than matched frame-by-frame.

### The coverage tracker has already been through three versions

Worth knowing before I "fix" it again. V1 tried to sweep all 718 media contacts across three
platforms every run and never finished, so Pooja only ever got a "run hadn't finished"
message. V2 added a hard 20-minute time budget with a three-tier priority order (Google Alerts
first, then client roster, then Tier 1 names only if time remains) and an instruction that a
partial run is a success, not a failure. I restructured that into the GOAL / WORKFLOW /
GUARDRAILS format on 18 Aug. V3 added the search API key on 30 Aug.

So the remaining gap really is just live search — the scoping problem is already solved, and
her V2 logic should be preserved rather than rewritten.

### Security note

The search API key was pasted in plaintext into WhatsApp on 30 Aug. **It should be rotated**,
and future keys handed over through something that isn't a chat backup. Worth mentioning
gently — it is a normal mistake, and she has no reason to know better yet.

### New task the meetings didn't cover: hosting

katalystrm.com is a single HTML file she built in Claude, sitting on a Squarespace domain.
AlikhiN is on Netlify. She is paying Squarespace for what is effectively just a domain. Worth
consolidating — Netlify or Vercel for both, Squarespace kept as registrar only — and it is a
quick win that visibly saves her money. **Note: she is on Windows** (her paths are `F:\Users\
Admin\...`), so nothing I set up should assume a Mac.

## Tasks Anmol owns

Reordered after reading the WhatsApp history. Item 1 is new and, I think, the highest-value
thing on the list.

### 1. Teach her the map — one working session
Chat vs project vs skill vs scheduled task vs agent vs Claude Design, and which surface has
memory, connectors and the ability to run unattended. She said outright she can't tell these
apart, and every misplaced effort so far traces back to that. AlikhiN on a static page is the
worked example to walk through: same agent, wrong surface. One hour here saves months of her
building good things in places they can't work.

### 2. Rehome AlikhiN
Her agent's brand knowledge and content writing are solid; the Netlify chat page is the wrong
container for it, because it has no memory, no connectors and no scheduled runs. Move that
capability into a Claude project with her skills attached, and keep the Netlify page only if
she wants a public-facing demo. Follows directly from item 1 and makes it concrete.

### 3. Daily PR coverage tracker — finish the last mile
**Preserve her V2 logic.** The 20-minute budget and the three-tier priority order are the fix
to the original failure and should not be rewritten. The only remaining gap is that searches
need to hit a live search API rather than the model's own recall. Wire that in, run it a few
days, and confirm Pooja gets a real email each morning.

Rotate the API key first — see the security note above.

### 4. Reel and carousel generation — rescope honestly
Canva's API cannot set transitions, timing or zoom, so "generate a finished reel" is not
achievable through the connector no matter how the prompt is written. Two honest options to
put to her:

- Generate the frame sequence in Canva as editable full-bleed fills, and she sets the motion
  by hand in the Reel timeline. Closest to how she works today.
- Generate frames, export them, and assemble the MP4 outside Canva with the timing applied
  programmatically. More automated, but it leaves her Canva workflow.

Either way the reference reel has to be described rather than linked, since Claude can't play
Instagram. Worth building a short intake format so describing a reference is quick.

### 5. Monthly media coverage report builder
Her format is fixed and known: 18-slide PPTX, Taj house style, gold and white, Trajan Pro
headings, Taj Krishna as the worked example. The generator is the easy half. The real decision
is the data: set up proper Meta Graph API access with tokens, or keep Stage 1 as manual
collection through an intake checklist. Manual is faster to ship and matches how she already
works — propose that first, and treat the API as a later upgrade.

### 6. Publish the prompt converter
Get the prompt-maker tool onto a URL she can reach. Highest leverage of the build items,
because it lets her keep improving her own prompts — and given the quality of what she has
already written unaided, that compounds fast.

### 7. Per-client actionable dashboards
She already built an informational IHCL dashboard as an Artifact and asked the right follow-up:
"so we can build an actionable one?" Yes. One Artifact per client pulling from her live Sheets
— plan filed or missing, coverage this month, what needs chasing. This is the consolidated view
the meetings asked for, and it is a better shape than a morning email digest.

### 8. Hosting consolidation
katalystrm.com is a single HTML file on a Squarespace domain; AlikhiN is on Netlify. Put both
on one host, keep Squarespace as registrar only, and tell her what she saves. Quick, visible
win. She is on Windows — don't hand her Mac instructions.

### 9. Plan recommendation
Which Claude plan, with the actual cost. Her harder work was failing on Sonnet, working on
Opus, then running out of credits mid-task. Give her the numbers and let her decide.

---

## Tasks for Nikhila's side

### 10. Restructure projects by client, not by platform
Today the projects are organised as "PR" and "social media". They should be one project per
brand, each holding its own instructions, memory and Drive or SharePoint links. With a luxury
roster this is the fix that protects per-brand voice — Masque and JW Marriott Kolkata cannot
share a template.

### 11. Stop starting fresh chats
Either continue the working chat, or start new chats inside the right project so context
persists at project level. Demonstrate once rather than explain twice.

### 12. Akanksha to share the Katalyst SharePoint folder
Claude cannot reach another tenant without a direct share. Edit rights if Claude is to write
anything back.

### 13. Rotate the search API key
It went over WhatsApp in plaintext on 30 Aug.

---

## Two things to correct rather than build

**The five-minute batch job will not work as described.** Scheduled tasks fire hourly at the
fastest, and generating daily content for 56 brands is far beyond what a $20 Pro plan will
sustain. The realistic version is a weekly scheduled run producing a batch of posts per brand,
queued for approval.

**Nothing should auto-publish.** These are high-stakes luxury accounts where one off-brand
caption is a real reputational cost to a hotel charging accordingly. Build queue-and-approve,
never fire-and-forget. Her own AlikhiN design already does this correctly — it drafts emails
to Gmail drafts for review rather than sending blind — so the instinct is already there and
just needs to hold as things get more automated.

---

## Open questions

1. Which item does she want first? I would lead with the map session (item 1), because
   everything else lands better afterwards — but if she wants a visible win first, the coverage
   tracker is closest to done.
2. Is the agency on Claude Team or individual Pro accounts? Changes the plan recommendation and
   whether projects can be shared with Akanksha and Pooja at all.
3. What does "56 brands" actually count? The website names roughly 15–20 clients and the skills
   library reveals a few more. The 56 is probably every individual outlet and property across
   the roster, which is a very different automation problem from 56 contracts.
4. Does she want the Meta Graph API set up properly, or is manual monthly data collection
   acceptable? Decides how much work item 5 actually is.
