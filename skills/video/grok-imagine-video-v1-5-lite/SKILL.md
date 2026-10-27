---
name: grok-imagine-video-1-5-lite-prompts
description: "Generate optimized prompts for xAI's Grok Imagine Video 1.5 Lite (grok-imagine-video-1.5-lite) — the lowest-price Grok video model, limited to text-to-video and single-first-frame image-to-video, 1–15 s clips at 480p/720p/1080p (1080p is upscaled from 720p), with native audio and lip-synced speech. Use whenever a user mentions Grok Imagine Video 1.5 Lite, Grok Video Lite, grok-imagine-video-1.5-lite, or the Lite model via the xAI API, Vercel AI Gateway, OpenRouter, Runware, fal or ComfyUI, or wants a cheap Grok clip with sound or spoken lines. Also use to decide when a request needs full Grok Imagine Video 1.5 instead (reference images, preset or uploaded voices, first/last frame, keyframes, native 1080p) or classic grok-imagine-video (edit, extend). Do not guess Lite syntax from general knowledge or copy full-1.5 fields (reference_images, reference_audios, last_frame, keyframes) into Lite requests."
---

# Grok Imagine Video 1.5 Lite — Prompt Generation Skill

Grok Imagine Video 1.5 Lite (`grok-imagine-video-1.5-lite`) is xAI's budget video model: **text-to-video
and image-to-video from one starting frame**, 1–15 s, with **native audio and lip-synced speech**. xAI's own
positioning: *"For simple videos, we recommend `grok-imagine-video-1.5-lite`, the lowest price per second."*

**This skill produces prompt text, not API calls.** Every result ships as two clearly separated pieces: the
**prompt** (prose in a code block) and a short **suggested settings** line. Never merge the two. When the
user's interface or API rejects or contradicts a value given here, **the interface wins** — adjust and say so.

## The Three Rules That Override Everything

1. **One shot-sized idea.** Lite is the "simple videos" model: one subject, one dominant action, one camera
   behavior, one sound bed. Several beats, cuts or a multi-character scene → split into separate clips, or
   route to full 1.5.
2. **Settings never go in the prose.** Duration, resolution, aspect ratio, model name and audio on/off are
   request fields. Don't write "8-second", "9:16 vertical" or "1080p" inside the prompt.
3. **Know what Lite cannot do — and route it.** No reference images, no voice references, no first+last
   frame, no keyframes, no editing, no extension, no native 1080p. Never invent a workaround syntax for these.

## Route Before You Write

| The user needs… | Model | Why |
|---|---|---|
| A simple imagined shot, cheap | **Lite**, text-to-video | Lowest price per second |
| A fixed opening image animated | **Lite**, image-to-video | One `image` = frame 1; prompt optional |
| Spoken lines with lip-sync, no specific voice | **Lite** | Lip-synced speech is native on Lite |
| A character/product/wardrobe bound from reference images | **Full 1.5** | Lite has no reference images (1.5: up to 14, 720p) |
| A specific preset or uploaded voice | **Full 1.5** | Voice references (up to 3) are 1.5-only |
| An exact end frame, or frames pinned mid-clip | **Full 1.5** | `last_frame` and up to 4 keyframes are 1.5-only |
| True native 1080p detail | **Full 1.5** | Lite's 1080p is a 720p render upscaled |
| Change part of an existing clip / continue a clip | **Classic `grok-imagine-video`** | Edit (source ≤ 8.7 s) and extend (+2–10 s) exist only there |

When routing away, say which model and why in one line, then write the prompt for that model (or hand off).

## Prompt Order

Text-to-video on Lite renders **a first frame from your prompt, then animates it** (xAI: *"text-to-video uses
text-to-image then image-to-video under the hood"*). So open with a clear picture, then the motion.

| # | Layer | What to write |
|---|---|---|
| 1 | Opening frame | Shot size, angle, subject placement, setting — what the first frame looks like |
| 2 | Subject anchors | Age range, build, hair, wardrobe, one signature detail; product geometry/materials |
| 3 | Primary action | One dominant, physically plausible action, told in order |
| 4 | Camera | One movement (or "locked off"), where it lands, lens feel, focus behavior |
| 5 | Light + look | Key source and direction, contrast, palette, medium/texture |
| 6 | Audio | Ambient bed, 1–2 synced effects, music or none, dialogue in quotes with speaker named |
| 7 | Stability | What must stay unchanged (logo, label text, decals, face) |

```
[OPENING FRAME: shot size, angle, subject in setting]. [SUBJECT ANCHORS]. [ONE ACTION, in order].
[CAMERA: one move + landing]. [LIGHT + PALETTE + TEXTURE].
[AUDIO: ambience, synced effects, music or none, Speaker: "short line"]. [WHAT STAYS THE SAME].
```

**Length:** xAI publishes no character limit (its error table only says a prompt can be "too long"). Prompts
pass through a documented prompt-rewriting **upsampler** LLM, so anything you leave out gets invented. Aim for
one specific paragraph, roughly 50–130 words. Specificity, not padding.

## Quick Syntax Reference

- **Dialogue:** name or describe the visible speaker, then the line in double quotes — xAI's own examples use
  `Sam: "I took the job in Berlin."` and `She says: "Welcome to my dream living room."` One short line per
  speaker per clip; two speakers is the practical ceiling.
- **Voice on Lite:** describe it in words ("low, gravelly voice", "bright, quick delivery"). No voice tokens.
- **Silence:** audio is on by default. Say "no dialogue" / "no music" when you mean it, or switch audio off in
  settings (SDK: `generate_audio=False`).
- **Camera:** plain film language — locked off, slow dolly in, lateral tracking, handheld, orbit, crane up.
  No camera-control parameter exists.
- **Image-to-video:** describe only what moves and changes, plus the 2–3 things that must hold. Don't
  re-describe the image.
- **No tokens of any kind.** `<IMAGE_1>`, `<AUDIO_0>` and `@Image1` do nothing on Lite.

## Output Format (always two parts)

1. **Prompt** — in a code block, prose only.
2. **Suggested settings** — one line, e.g.
   `model: grok-imagine-video-1.5-lite · mode: text-to-video · duration: 8 · resolution: 720p · aspect_ratio: 16:9 · audio: on`

Defaults and ranges: duration 1–15 s (xAI default 8; some wrappers default to 6 — set it explicitly) ·
resolution 480p (default) / 720p / 1080p (upscaled from 720p, and $0.14/s vs $0.03/s at 720p) · aspect ratio
1:1, 16:9 (default), 9:16, 4:3, 3:4, 3:2, 2:3, 21:9, 5:2 on the native API — wrappers may list fewer ·
image-to-video ignores aspect ratio and uses the source image's.

## Things That Will Break the Request

- **Full-1.5 fields on Lite:** `reference_images`, `reference_audios`, `last_frame`, `keyframes` — not
  supported on Lite. Remove them or switch model.
- **Edit/extend on Lite** — operation not available for the model (`failed_precondition`); use classic
  `grok-imagine-video`.
- **Duration outside 1–15**, or a prompt that is too long → `invalid_argument`.
- **Text-to-video without a prompt** — prompt is required unless an `image` is supplied.
- **Setting `aspect_ratio` on image-to-video** — ignored; crop/pad the source image instead.
- **Expecting a seed or negative prompt** — neither exists natively (a wrapper "seed" may only force a re-run).

## Iteration Workflow

1. Draft at **480p** for composition and motion; move to **720p** to judge audio, lip-sync and finish.
2. Change one layer per pass (action → camera → light → audio). The upsampler makes multi-change passes
   impossible to attribute.
3. Save every accepted prompt, source image and settings line — there is no seed to recreate a take.
4. Render **1080p only for chosen finals**, knowing it is an upscale of the 720p render.
5. If a take keeps failing for a reason in the routing table (identity drift, exact end frame, a specific
   voice), stop iterating on Lite and route.

## Reference Files

- **[best-practices.md](best-practices.md)** — writing for the upsampler and the first-frame pipeline, motion and camera language, audio and dialogue craft, image-to-video prompting, exclusions, resolution/cost tiers, mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — continuity without references or seed: canonical stills, identity anchors, last-frame handoff, audio and voice consistency, and when to move to full 1.5 or classic Grok Video.
- **[examples.md](examples.md)** — 10 annotated prompts: portrait, landscape, action, product, dialogue two-shot, single-speaker line, image-to-video portrait, image-to-video product, vertical social, routing-away note.
- **[parameters.md](parameters.md)** — model ID and wrapper IDs, every native field with values and defaults, Lite vs 1.5 vs classic capability matrix, pricing, async job flow, errors, what xAI does not publish.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
