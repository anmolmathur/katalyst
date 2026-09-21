# Reels and carousels — decision record and install runbook

_Task 4. Written 9 Sep 2026, after re-testing the live Canva connector rather than trusting the
August diagnosis. Read the first half once; work from the second half when configuring her
account._

## What changed since August

The August write-up put two options to her: build frames in Canva and set the motion by hand, or
build frames and assemble the MP4 outside Canva. Anmol's instruction on 9 Sep was that this
should be fully automated, and that the alternatives should be researched properly rather than
assumed away.

They were, and the picture is better than August suggested — but not in the direction the
earlier note pointed.

**The no-motion finding holds, and is worse than described.** Nothing in Canva's API surface —
Connect, the design-editing operations, autofill, Bulk Create — exposes duration, transitions,
animation or zoom. Checking the live connector's own operation list confirms it: text, fills,
shapes, position, crop, opacity, layering, pages, speaker notes, and no temporal property
anywhere. Worse, Canva moved new video designs to a multi-track timeline in October 2025, so
"generate pages, she sets the motion on them" describes a structure Canva no longer uses. The
manual-handoff option from August was already stale when it was written.

**But the export block turns out not to bind.** August recorded that Canva's export domain is
unreachable from Claude's sandbox, and concluded that frames therefore have to be downloaded and
re-uploaded by hand. That conclusion only follows if Claude has to be the one holding the file.
It does not. A render service fetches the frames from Canva's URLs on its own servers, and Claude
only ever passes URLs around. Nothing is downloaded, so nothing is blocked.

That is the whole unlock, and it is why full automation is achievable now when it was not in
August.

## The options, and why Shotstack

| Option | Automated end to end | Cost | Verdict |
|---|---|---|---|
| Canva frames, motion by hand | No — that is the manual step | Free | The August plan. Rejected: it is the thing we were asked to remove, and the page-based model it assumed is obsolete. |
| Canva video brand template + autofill | Yes, but motion is fixed per template | Free | Genuinely attractive and worth probing — see below. Blocked on whether the connector can edit a timeline-based video design at all, which cannot be tested without one of her templates. |
| ffmpeg in Claude's own container | No | Free | Needs the frames inside the container, which is the one thing the export block prevents. Only works if she attaches PNGs by hand — the manual step again, wearing a different hat. |
| Frames rendered by Claude instead of Canva | Yes | Free | Rejected on quality. These are design-award accounts; Pillow-rendered typography is not going on a Taj grid. |
| **Canva frames → Shotstack motion** | **Yes** | **~13c a reel** | **Recommended.** |
| Creatomate | Yes | $29/mo, credits do not roll over | Cheaper only at high volume, no hosted connector, needs a card either way. |
| Remotion | Yes | $100/mo licence minimum above 3 staff | Templates are React components. This is a software project, not a design workflow. |
| Plainly | Yes | $69/mo | An After Effects render farm. Templates must be authored in After Effects, which she cannot do. |
| Sora, Veo, Runway, Pika, Kling | Yes | Varies | **Never.** They synthesise footage. Asked to animate a photograph of a real suite, they invent architecture that does not exist — which on a hotel account is a factual-accuracy and client-liability problem, not a stylistic one. |

Shotstack wins on three specific things rather than on being generally good. It publishes a
**hosted MCP server** at `https://mcp.shotstack.io/`, so it goes into Claude as a custom
connector with an OAuth click and no terminal — decisive for someone on Windows who should not
be installing npm packages. Its Ken Burns motion is a **named vocabulary** (`zoomInSlow`,
`slideLeftSlow`) rather than a hand-tuned scale animation, so there is very little for Claude to
get subtly wrong. And pay-as-you-go credits are valid a year, so a quiet month costs nothing.

At roughly 25 seconds a reel, a render is about 0.4 of a minute at $0.30 a minute — **call it 13
cents a reel, or under $5 a month at thirty reels.** That is not the number that decides this;
the setup effort is. But it is worth being able to say plainly.

**Carousels need none of this.** No motion, so Canva alone finishes them, and that half of the
skill works the day it is installed regardless of what she decides about Shotstack.

### The free option still worth probing

If she has, or is willing to hand-build, a **Canva video brand template with the motion already
baked in**, then swapping the images and text into a copy of it and exporting MP4 would be fully
automated at zero marginal cost, with motion that is hers rather than a render service's. That is
strictly better if it works.

It is not in the skill because it could not be verified: it depends on whether
`create-design-from-brand-template` preserves a video design's timeline and whether `edit-design`
can touch a timeline-based design at all, and there is no Canva video template available here to
test against. **Twenty minutes in her account settles it** — Step 6 of the checklist below is that
test. If it passes, that path is worth building as the default for her three or four recurring
reel formats, with Shotstack kept for bespoke pacing.

## What is installed

One skill: `plugins/katalyst/skills/reel-and-carousel-builder/SKILL.md`.

Reels and carousels share the intake, the voice work, the frame script and the approval gate, and
diverge only at the last step, so they are one skill rather than two. That also keeps the skill
count down, which matters — she has fifteen already and will not remember them all.

Two gates are built into it deliberately, and both should survive any future edit. **The frame
script is approved before anything is built**, because approving eight lines of text costs ninety
seconds and catches nearly everything. **Nothing publishes**, ever, under any phrasing — the skill
produces assets and hands them over. Her own AlikhiN design already drafts to Gmail drafts rather
than sending blind; this is the same instinct held as the automation grows.

## Configuring her instance

Her side is Windows and Claude Pro. Nothing below needs a terminal.

### 1 — Install the skill

Update the plugin from the marketplace, or upload the skill folder directly if she has not got
the marketplace wired up yet. Confirm it appears in her skills list.

### 2 — Canva asset folders, one per client

This is the only genuinely new habit the workflow asks of her, and it is the step most likely to
be skipped.

Claude addresses photography by Canva asset ID, and it can only read IDs out of a Canva folder.
The upload-from-URL route is not usable here: it only accepts URLs that are already public, and
client photography must never be that.

So in Canva, one folder per active client, named `Katalyst_<Client>_Assets`, holding only shots
approved for use. Start with the four or five clients that post most. A shot that is not in the
folder does not go in the post — the skill is written to say so rather than substitute something.

### 3 — Brand kits

Confirm each of those clients has a Canva brand kit with the real fonts and colours. The skill
passes `brand_kit_id` on every generated layout, and falls back to the group kit — never to Canva
defaults. If a client has no kit, generated layouts for that client will be off-brand and she
will rightly reject them, so it is worth checking before the first run rather than after.

### 4 — Reel and carousel brand templates

Not required, but it is what makes the output look like hers. The skill searches her brand
templates before it generates anything, and says in the delivery when it had to generate. If she
has story or reel templates already, make sure they are published as **brand templates** rather
than sitting as ordinary designs — `search-brand-templates` cannot see ordinary designs.

### 5 — Shotstack, if she wants the reel half

1. Sign up at shotstack.io and get a **production** key. Sandbox keys are rejected by the MCP
   server — this catches people out.
2. Buy a small pay-as-you-go credit pack. Credits last a year.
3. In Claude: **Settings → Connectors → Add custom connector**, endpoint
   `https://mcp.shotstack.io/`, then complete the OAuth with the Shotstack account.
4. Confirm the connector's tools appear — `render_video` and `get_render_status` are the two the
   skill uses.

Custom connectors on the Pro tier should be verified at this point rather than assumed; if they
are not available on her plan, that becomes an input to the plan recommendation in task 9.

### 6 — The video brand template probe

Twenty minutes, and it decides whether she needs Shotstack at all. In her account, take one
existing reel she is happy with, publish it as a brand template, and ask Claude to create a
design from it and replace one text element and one image. Then check three things: does the copy
still have the motion on it, did the edit apply, and does `get-export-formats` offer `mp4`. All
three yes means the free path works for her recurring formats and is worth building next.

## Verification, first run

Do this on one real post before telling her it works. The chain has one link that has never been
exercised, and it is the third item.

1. **Carousel end to end.** Pick a client with a brand kit and an asset folder. Frame script,
   approval, build, export. Look at the PNGs. This half has no external dependency and should
   simply work.
2. **Frame script gate.** Ask for a reel and check that Claude stops after the table and waits.
   If it builds straight through, the gate is not holding and the skill needs a fix, not a
   workaround.
3. **The Canva → Shotstack handoff.** The one unverified link: whether Shotstack's servers can
   fetch a Canva export URL. Export two frames, render a five-second test, and watch for a fetch
   error. If it fails, the fix is likely a signed-URL expiry rather than anything structural —
   re-export immediately before rendering. Establish this before building anything else on top.
4. **Motion quality.** Render one real reel and watch it. `Slow` variants, alternating direction,
   clips overlapped by a quarter-second for the crossfade. If it reads as a slideshow rather than
   as film, the pacing is in the frame script and that is where to fix it.
5. **Draft mode.** Confirm a run without `APPROVED FOR CLIENT` says it is a draft and goes nowhere
   near a client.
6. **Plan tracker.** Confirm the finished post is logged against its row.

## What is deliberately not built

**Publishing.** Not to Instagram, not through any connector. The skill produces assets and stops.

**Trending audio.** Instagram's trending tracks are licensed inside Instagram; pulling a copy in
at render time is a rights problem on a client account. Reels render silent and she picks the
audio in the Instagram composer, or the client's own licensed track is used. Worth telling her
explicitly, because it will otherwise look like a missing feature.

**Frames rendered outside Canva.** Quality, not capability. The typography is the deliverable.

**A second render vendor.** One is enough until the first one is a problem.

## Open questions for her

1. Shotstack, or hand-build three or four Canva video templates and use the free path? The probe
   in step 6 above decides whether that is even a choice.
2. Which four clients get asset folders and brand kits first?
3. Does she want the batch mode — a whole month's posts scripted in one pass, approved together,
   then built — or one post at a time to start?
