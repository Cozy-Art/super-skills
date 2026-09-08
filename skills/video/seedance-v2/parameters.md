# Seedance 2.0 — Settings Reference

This model is reached through several different tools, and their documentation doesn't fully agree with itself — sometimes not even page-to-page within the same provider. This file gives a baseline you can trust, plus what varies and where.

Because this skill produces prompt text for a person to paste elsewhere (not API calls this app makes directly), field *names* matter less than knowing what the control does and what range is realistic to suggest. Treat everything below as "what to tell the director to set," not a request body.

---

## Baseline (fal.ai — the most consistently documented surface)

fal.ai is ByteDance's most visible integration partner for Seedance 2.0 and has the cleanest, most internally-consistent documentation of the providers checked, so it's the baseline this skill defaults to.

| Setting | Values | Default | Notes |
|---|---|---|---|
| Resolution | `480p`, `720p` | `720p` | Hard cap per fal.ai's own reference docs — see "Where sources disagree" below |
| Duration | `auto`, or `4`–`15` (seconds) | `auto` | `auto` lets the model pick a length based on the prompt content |
| Aspect ratio | `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` | `auto` | See adaptive behavior below |
| Audio | on / off (boolean) | on | Generating audio does not cost extra on fal.ai — no reason to turn it off except for a genuinely silent draft |
| Seed | integer | random | For reproducibility. fal.ai's own docs note results can vary slightly even at a fixed seed — treat as a strong nudge, not a guarantee |

### Two speed tiers

| Tier | Priority | Rough cost (10s, 720p, audio on) |
|---|---|---|
| Standard | Maximum quality | ~$3.03 |
| Fast | Lower latency and cost | ~$2.42 |

Some resellers (see below) additionally expose a third, cheaper **Mini** tier for quick drafts. If the director's tool has one, it's a reasonable place to test a prompt before committing to a Standard/Fast render.

### `auto` aspect ratio resolution logic

- **Text-to-Video:** infers the best ratio from the prompt content
- **Image-to-Video:** adapts to the input (first-frame) image's aspect ratio
- **Reference-to-Video:** priority order is video ratio > image ratio > prompt inference

### Resolution × aspect ratio → pixel dimensions

| Aspect | 480p | 720p |
|---|---|---|
| 21:9 | 992×432 | 1470×630 |
| 16:9 | 864×496 | 1280×720 |
| 4:3 | 752×560 | 1112×834 |
| 1:1 | 640×640 | 960×960 |
| 3:4 | 560×752 | 834×1112 |
| 9:16 | 496×864 | 720×1280 |

---

## Where sources disagree

Documentation for Seedance 2.0 is moving fast and providers don't agree with each other — or, in a couple of cases, with themselves. Worth knowing about so a director isn't surprised:

| Point of disagreement | fal.ai says | Other sources say |
|---|---|---|
| Max resolution | 480p / 720p, stated as a hard limit | 1080p available on "standard" tier (Volcano/BytePlus-style resellers); one provider claims native 4K as of June 2026; oddly, one fal.ai example call itself uses `"resolution": "1080p"` despite the documented cap |
| Max duration | 4–15 seconds, or `auto` | Some resellers advertise up to 20 seconds |
| Tier count | 2 (Standard, Fast) | Some resellers offer 3 (Standard, Fast, Mini) |
| Reference token syntax | `@Image1` / `@Video1` / `@Audio1` (API reference and the official GitHub repo) | `[Image1]` / `[Video1]` / `[Audio1]` appears in fal.ai's own marketing copy and some reseller docs |
| Extra controls | Not present on fal.ai's schema | Some resellers add `content_filter` (safety strictness), `web_search` (real-world grounding for T2V), and `callback_url` (webhook) |

**Practical takeaway:** write the prompt the same way regardless of which of these turns out to be true for the director's tool. None of it changes the six-block formula or the syntax rules — it only changes what number goes in the settings line. If a tool offers a higher resolution or longer duration than the fal.ai baseline, take it; nothing about the prompt needs to change to use it.

---

## Endpoint names (for context, not for calling)

Useful if the director is trying to identify the right dropdown or model picker in their tool:

| Capability | fal.ai endpoint ID |
|---|---|
| Text to Video | `bytedance/seedance-2.0/text-to-video` |
| Text to Video (Fast) | `bytedance/seedance-2.0/fast/text-to-video` |
| Image to Video | `bytedance/seedance-2.0/image-to-video` |
| Image to Video (Fast) | `bytedance/seedance-2.0/fast/image-to-video` |
| Reference to Video | `bytedance/seedance-2.0/reference-to-video` |
| Reference to Video (Fast) | `bytedance/seedance-2.0/fast/reference-to-video` |

Reseller naming varies — one common alternate pattern is `seedance-t2v` / `seedance-i2v` style short IDs, sometimes split further into `-standard` / `-fast` / `-mini` suffixes.

---

## Reference file requirements (Image-to-Video / Reference-to-Video)

If the director is uploading their own reference material rather than typing text alone:

| Input | Formats | Limits |
|---|---|---|
| Start-frame image (I2V) | JPEG, PNG, WebP | Max 30 MB |
| End-frame image (I2V, optional) | JPEG, PNG, WebP | Max 30 MB — when present, the video transitions from start frame to end frame |
| Reference images (R2V) | JPEG, PNG, WebP | Up to 9, max 30 MB each |
| Reference videos (R2V) | MP4, MOV | Up to 3; combined duration 2–15s; roughly 480p–720p source resolution; total under 50 MB |
| Reference audio (R2V) | MP3, WAV | Up to 3; combined duration ≤ 15s; max 15 MB each; requires at least one image or video also present — audio can't be the only reference |

Total reference files across all types: 12 maximum per Reference-to-Video generation.

---

## Practical prompt-length guidance

No provider publishes a hard, universally-agreed character limit, but the pattern across sources is consistent: **2–3 sentences is the sweet spot**, well short of any technical ceiling. One reseller documents an absolute cap around 10,000 tokens (roughly 500 Chinese characters or 1,000 English words) — you will not get near this writing a proper six-block prompt, and hitting anywhere close to it is itself a sign the prompt needs to be split into a scene-cut or a separate shot rather than lengthened further.
