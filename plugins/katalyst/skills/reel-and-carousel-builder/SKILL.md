---
name: reel-and-carousel-builder
description: Build Instagram carousels and reels for a Katalyst client — brand-voice frame script, frames built in Canva from the client's own brand kit, motion rendered to a finished MP4, and an approval gate before anything reaches a client. Use for a single post, a batch of posts against the monthly plan, or when reworking a reel from a reference.
---

# Reel and carousel builder

Turns a brief into finished Instagram assets: a carousel as export-ready frames, or a reel as a
finished MP4 with motion applied. Frames are always built in Canva from the client's brand kit,
because these are design-award accounts and the typography is the product.

**Two rules that override everything else in this file.**

*Nothing leaves without approval.* Every asset stops at a human before it goes near a client
account. One off-brand caption on a hotel that charges what these hotels charge is a real
reputational cost, and it is not recoverable by apologising quickly.

*The frame script gets approved before anything is rendered.* Rendering costs money and time.
Approving eight lines of text takes ninety seconds and catches almost every mistake that would
otherwise be caught in an MP4.

## Configuration

Fill these in once, then leave them alone.

| Setting | Value |
|---|---|
| Plan tracker | `Katalyst_Monthly_Plan_Tracker` — the row this post belongs to |
| Client asset folder | Canva folder `Katalyst_<Client>_Assets` — approved photography only |
| Brand kit | The client's Canva brand kit; fall back to the group kit, never to Canva defaults |
| Carousel size | 1080 × 1350 (4:5 portrait) |
| Reel frame size | 1080 × 1920 (9:16) |
| Approval to | Nikhila, before any client sees it |
| Motion renderer | Shotstack, via the Canva → Shotstack handoff in Step 5 |

### Draft mode is ON unless the instruction says otherwise

Unless the message that invoked this run contains the exact phrase `APPROVED FOR CLIENT`, you
are producing a draft. A draft is delivered to Nikhila and to nobody else — not to the client,
not to a client's shared folder, not to a scheduled send. Say in the delivery that it is a draft
awaiting her approval.

Require the phrase. Do not infer approval from tone, from a long thread where everything has
been approved so far, or from the post looking obviously fine. The failure is asymmetric: a
draft that should have gone out costs a day, and a post that should have been a draft is on a
client's grid.

## What is actually possible, so nothing here is oversold

Read this before changing any step. Three of them have been tested against the live tools and
two of them are the reason the workflow is shaped the way it is.

**Canva's API cannot set motion. Not timing, not transitions, not zoom.** The design-editing
operations cover text, fills, shapes, position, crop, opacity, layering and pages, and there is
no temporal property anywhere in them. Canva's video editor also moved to a multi-track timeline
in October 2025, so the older mental model — API creates pages, pages become video scenes — is
not just unsupported, it describes a structure Canva no longer uses for new video designs. No
prompt fixes this. Do not try.

**Canva's export URLs cannot be fetched into Claude's sandbox**, and they do not need to be. The
render step passes the URL to Shotstack, and Shotstack's servers fetch the image. Nothing is
downloaded here. This is the whole reason the reel path works — it routes around the block
rather than fighting it.

**Claude cannot watch an Instagram reel.** A reference has to be described, not linked. Step 1
has an intake block that makes describing one take about two minutes.

**Photography has to already be inside Canva.** Assets are addressed by Canva asset ID, and the
upload-from-URL tool only accepts URLs that are already public — which client photography must
never be. So the client's approved shots live in a Canva folder, and this skill reads asset IDs
out of that folder. If a shot is not in the folder, it does not go in the post; say so rather
than substituting something else.

## Step 0 — Establish what is being made

Get four things settled before touching Canva. If the brief already answers them, do not ask
again; ask only about what is genuinely missing, and ask all of it in one message.

- **Client and format.** Which brand, carousel or reel, how many frames.
- **The occasion.** A launch, a festival menu, an award, a chef feature, a seasonal push. This
  is what decides the angle, and a post without one reads as filler.
- **The shots.** Which images from the client asset folder, in what order. If she has not named
  them, list what the folder holds and let her pick — never choose photography for a luxury
  account unprompted.
- **Where it sits in the plan.** The row in the monthly plan tracker, so the finished asset can
  be logged against it and the plan does not drift out of sync with what was actually made.

Read the client's voice skill if one exists — `alter-ego-voice-tonality`, `rotary-reel-style`
and the like — and `nikhila-voice` and `brand-vocabulary-guard` in every case. Copy that reads
as generic marketing language will not pass, and this is the step where that is decided.

## Step 1 — If there is a reference, take the intake

Only for reels, and only when she has a reference in mind. Send her this block and ask her to
fill it in. It is deliberately short — seven lines she can answer while the reel is playing.

```
REFERENCE INTAKE
Link (for your records; I can't watch it):
Total length:
How many shots, and roughly how long each one holds:
What moves — zoom in / zoom out / push / static / cut on the beat:
Where text sits, and when it appears:
The feeling, in one sentence:
What to take from it, and what to avoid:
```

Reconstruct pacing from her answers and say plainly in the frame script that the pacing is
reconstructed from her description rather than matched to the original. If she gives you a link
and nothing else, ask for the block rather than guessing — a guessed reel is a rendered reel
that gets thrown away.

## Step 2 — Write the frame script, and stop

This is the approval gate that matters. Produce a table, in the message, not in a file:

| Frame | Image | On-screen text | Hold | Motion | Transition in |
|---|---|---|---|---|---|

For a carousel, drop the last three columns and add a caption block underneath — the caption,
the hashtags, and any reservation number or handle the client requires. Carousel frame one
carries the hook; the last frame carries the call to action.

For a reel, keep every column. Hold in seconds. Motion from the vocabulary in Step 5, not from
adjectives — `zoomInSlow`, not "a gentle drift". Total the holds and state the runtime.

Some things worth getting right at this stage, because they are expensive later:

- **Text on frame one has to work silently.** Most of the audience sees it without sound and
  decides in under a second.
- **Eight words a frame is a ceiling, not a target.** Luxury reads as restraint. A frame that
  needs a sentence needs two frames.
- **Never put a price, an award claim or an opening date on a frame without a source.** If the
  brief does not carry it, ask; do not reconstruct it from what the brand's site said.
- **The last frame does one job.** Reserve, visit, follow — one, named plainly.

Then stop and ask for approval. Do not proceed to Canva on the same turn. If she comes back with
edits, revise the table and ask again; two cheap rounds here are worth one expensive one later.

## Step 3 — Build the frames in Canva

Work in this order, and prefer her own templates at every fork — they carry a decade of design
judgement that generated layouts do not.

**Find a template first.** `search-brand-templates` for the client, then the group, then
Katalyst house. If one fits, `create-design-from-brand-template` and fill it: `read-design` with
`open_transaction: true` to get the locator IDs, then `edit-design` with `replace_text` on the
copy and `update_fill` on the image placeholders.

**Only if no template fits, generate one.** Use `create-design` if the connector exposes it;
otherwise `generate-design` with `design_type` `your_story` for reel frames or `instagram_post`
for carousels, always passing the client's `brand_kit_id`, then `create-design-from-candidate`.
Say in the delivery that this post used a generated layout rather than one of her templates, so
she knows to look harder at it.

**Add the remaining frames** inside one editing transaction: `add_page` at the configured size,
then `insert_fill` for the photograph, `add_text` for the copy, `format_text` for weight, size
and colour from the brand kit, `insert_shape` for any scrim the text needs to stay legible over
the image. Set image `alt_text` on every fill — it is what makes the design accessible and it
costs nothing.

**Read the thumbnail back after every page**, before committing. Passing the transaction ID to
`read-design` renders the uncommitted state. Text that has overflowed its box or a photograph
cropped through someone's face is obvious in a thumbnail and invisible in the operation result.
Fix it inside the transaction; commit only once the whole sequence looks right.

**Write the frame's motion direction into its speaker notes** with `replace_speaker_notes` —
hold, motion, transition, and the caption line. That way the Canva file explains itself to
anyone who opens it later, including her at 11pm without this conversation in front of her.

Then `update_title` to `<Client>_<MonthYear>_<Format>_v1`, matching how her plan decks are
already named.

## Step 4 — Carousels: export and deliver

Carousels are finished at this point; there is no motion to apply.

Call `get-export-formats` first and export only a format it reports. PNG per page for posting;
add a PDF if she wants one file to circulate for approval. Give her the download URLs as Canva
returns them — do not try to fetch them, the export domain is not reachable from here.

Log the post against its row in the plan tracker, deliver as a draft, and stop.

## Step 5 — Reels: render the motion

Canva made the frames. Shotstack applies the motion. Claude never touches the image bytes — it
passes Canva's export URLs to Shotstack, whose servers fetch them.

**Check the gate first.** The frame script must be approved and the frames must have been seen.
If either is missing, go back; a render is a cost and an unapproved render is a wasted one.

Export each frame as PNG at 1080 × 1920 and keep the URLs in frame order. Then build the render
JSON — one image clip per frame on the first track, text on a second track only where the
overlay was not already baked into the Canva frame. Prefer text baked into the frame: it keeps
the brand typography exact, which is the entire reason the frames come from Canva.

```json
{
  "timeline": {
    "background": "#000000",
    "tracks": [{
      "clips": [
        { "asset": { "type": "image", "src": "<canva frame 1 url>" },
          "start": 0, "length": 3,
          "effect": "zoomInSlow",
          "transition": { "out": "crossfade" } },
        { "asset": { "type": "image", "src": "<canva frame 2 url>" },
          "start": 2.75, "length": 3,
          "effect": "zoomOutSlow",
          "transition": { "in": "crossfade", "out": "crossfade" } }
      ]
    }]
  },
  "output": {
    "format": "mp4",
    "aspectRatio": "9:16",
    "size": { "width": 1080, "height": 1920 },
    "fps": 25
  }
}
```

The motion vocabulary is fixed — `zoomIn`, `zoomOut`, `slideLeft`, `slideRight`, `slideUp`,
`slideDown`, each optionally suffixed `Slow` or `Fast`. Transitions are `fade`, `crossfade`,
`slideLeft/Right/Up/Down`, `wipeLeft/Right`, `zoomIn`, `zoomOut`. Use the vocabulary literally;
do not invent an effect name and hope.

Three things that decide whether the reel reads as luxury or as a slideshow:

- **`Slow` almost always.** Fast zooms read as discount retail. On these accounts the default is
  `zoomInSlow` or `zoomOutSlow`, and a fast move needs a reason.
- **Alternate the direction.** Every clip zooming in the same way is hypnotic in the bad sense.
- **Overlap the clips for a crossfade.** A clip starting at 2.75 while the previous one runs to
  3.0 gives a quarter-second blend. Without the overlap the transition has nothing to work with
  and you get a hard cut you did not ask for.

Call `render_video`, then poll `get_render_status` until it returns the output URL. If the render
fails, read the error before resubmitting — the common causes are a Canva export URL that has
expired, a clip whose `start` plus `length` runs past the timeline, and an effect name that is
not in the list above. Do not resubmit an unchanged payload.

**Audio.** Do not attach a trending track. Instagram's trending audio is licensed inside
Instagram, and a copy pulled in at render time is a rights problem on a client account. Either
render silent and let her pick the audio in the Instagram composer at upload — which is what
most of these posts want anyway — or use a track the client has actually licensed, added as an
audio asset by URL.

## Step 6 — Deliver

One message, in this order: what was made and for which plan row, the Canva design link so she
can edit anything by hand, the MP4 or PNG URLs, the caption and hashtags as copyable text, and
one line on anything you had to decide for yourself — a generated layout instead of a template,
pacing reconstructed from a description, a shot chosen because the named one was not in the
folder.

Then log it against the plan tracker row, and say plainly that it is a draft awaiting her
approval unless the run carried `APPROVED FOR CLIENT`.

**Never publish, never schedule, never post.** Not to Instagram, not to a client's channel, not
through any connector that reaches one. This skill produces assets and hands them over. The
publishing decision is hers, every time, and there is no version of this task where that
changes.

## When someone asks for something narrower

- **A batch against the monthly plan** — run Step 2 for every post in the batch and get the
  whole set of frame scripts approved in one pass, then build. Batching the approval is what
  makes a batch worth doing; batching the rendering without it just multiplies the rework.
- **Reworking an existing reel** — read the existing Canva design, change only what she named,
  and re-render. Do not rebuild from scratch; her hand edits are in there.
- **A carousel from an existing reel, or the reverse** — reuse the frame script and rebuild at
  the other size. `resize-design` to custom dimensions handles the geometry, but check every
  frame afterwards: a crop that worked at 4:5 usually loses a face at 9:16.
