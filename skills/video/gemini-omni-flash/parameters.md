# Gemini Omni Flash — Parameters

All values from Google's own documentation — the Gemini API model page, the Omni Flash guide, the
pricing page, and the DeepMind model card.

**Model ID:** `gemini-omni-flash-preview` — in preview
**Surface:** Gemini API and Google AI Studio (both confirmed)

> **Two audiences.** A director generating in a UI needs the ceilings and behaviours. The parameter
> names and request-shape detail matter to **the integration layer**, which drives the API directly. Both are kept
> here; the constraints are the same either way.

---

## Output specification — narrow by design

| Item | Value |
|---|---|
| Duration | **3–10 seconds** |
| Resolution | **720p** — the only option |
| Frame rate | **24 fps** — fixed |
| Aspect ratio | **16:9** (default) or **9:16** — the only two |
| Audio | Native, synchronized, generated with the frames |
| Watermark | SynthID on all outputs, non-optional |

The output envelope is tight and entirely fixed. Nothing here is negotiable.

**Input data types:** Text, Image, Video (up to 10 s, for editing). **Output:** Video.

---

## Context window

**1,048,576 tokens**, stated verbatim on the model page.

That is the documented ceiling. Google publishes no separate prompt-length recommendation.

**It is a ceiling, not a target.** Google publishes no separate prompt-length recommendation, and a
video prompt anywhere near a million tokens is not a prompt. Working range is a few hundred words:
enough for a scene, its camera, its audio and two or three timecoded beats.

---

## Parameters

| Parameter | Where | Values | Notes |
|---|---|---|---|
| `task` | `generation_config.video_config` | `text_to_video`, `image_to_video`, `reference_to_video`, `edit` | **Inferred if omitted** |
| `aspect_ratio` | `response_format` | `16:9`, `9:16` | Default `16:9` |
| `delivery` | — | `uri` | **Required for outputs over 4 MB** |
| `previous_interaction_id` | — | id | Chains a stateful multi-turn edit |
| `background` / `store` / `stream` | — | boolean | See below |

### The retention trap

Setting `background=false`, `store=false` and `stream=false` gives a faster synchronous response — but
**`store=false` breaks later editing.** The clip cannot be referenced in a subsequent turn because it
was not retained.

This is a real footgun: the fastest configuration silently disables the model's best feature. If there
is any chance a result will be edited, it must be stored.

---

## Documented non-capabilities

Google lists these as unsupported. Several are surprising enough to plan around.

**Generation:**
- Video **extension** — no continuing a clip past its generated length
- **Interpolation** — no first-and-last-frame in-betweening
- **Multi-video referencing** — *"Referencing or reasoning across multiple videos is not supported"*
- **Video references in practice** — accepted by the API schema but *"not correctly processed by the
  model at this time."* The schema accepting them is not evidence they work
- **Audio reference uploads** — *"unsupported in the current version of the API"*
- **Voice editing**

**Inference controls:**
- System instructions
- `temperature`, `top_p`, stop sequences
- **Negative-prompt fields**
- Provisioned throughput
- YouTube sources

---

## Regional restrictions

Easy to trip over and absent from most write-ups:

- **Editing *uploaded* videos is unavailable in the EEA, Switzerland and the UK.** Editing
  model-generated videos is fine — the restriction is on user-supplied footage
- **Uploading or editing images containing minors is blocked** in the same regions
- **Only English has been evaluated**

---

## Pricing

| Item | Cost |
|---|---|
| Input | $1.50 / 1M tokens |
| Output video | $17.50 / 1M tokens |
| Effective rate | 5,792 tokens per second of 720p ≈ **$0.10 / second** |

**Paid tier only — there is no free tier.** A 10-second clip is about $1.

---

## Watermarking

**SynthID on all outputs** — invisible to viewers, programmatically detectable for provenance.

**C2PA is not documented.** Claims that Omni Flash embeds C2PA provenance metadata appear in
third-party write-ups but in neither the API docs nor the model card. Do not assert it.

---

## Known model limitations

From Google's own model card, worth carrying into expectations rather than discovering:

- **Consistency** across a generated sequence is a stated limitation
- **Text rendering** is a stated limitation — avoid designs depending on legible on-screen type

---

## Access surfaces

**Confirmed:** Gemini API, Google AI Studio, Gemini App, YouTube, Google Flow, Google Flow Music.

**Not confirmed:** "Gemini Enterprise Agent Platform" and "YouTube Shorts/Create" specifically appear
in third-party coverage but in neither the model page nor the model card.

**Consumer-surface resolution and duration tiers** (for example Google Flow offering 4-, 6-, 8- and
10-second options, or 1080p/4K) are third-party claims. Google's own model page states 3–10 s at 720p /
24 fps with no tiering. Treat consumer-app capability claims as describing the app, not the model.
