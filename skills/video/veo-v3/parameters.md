# Veo 3.1 — Parameters

Every value below comes from Google's Vertex AI / Gemini API documentation for Veo 3.1. Where Google
publishes nothing, this file says so rather than filling the gap.

**Model IDs:** `veo-3.1-generate-preview` (standard) · `veo-3.1-fast-generate-preview` (faster, lower cost)
**Platform:** Google Cloud Vertex AI, Gemini API
**Output:** MP4, 24 fps, native audio, SynthID watermark on every result

---

## The constraint that shapes everything else

**Resolution and duration are coupled.** This is the single most useful thing to internalise about
Veo's parameters, because it decides the shape of a shoot before a word of prompt is written.

| Resolution | Allowed durations | Extension | Typical use |
|---|---|---|---|
| `720p` | 4s, 6s, 8s | ✅ supported | Iteration, and anything that will be extended |
| `1080p` | **8s only** | ❌ | Client review, finished single shots |
| `4k` | **8s only** | ❌ | Final deliverables |

Two consequences worth planning around:

- **Anything longer than 8 seconds has to be built at 720p.** Extension is 720p-only, so a 40-second
  sequence is a 720p sequence. There is no path to a 4K minute.
- **Reference images force 8 seconds** regardless of resolution. A 4-second shot cannot use them.

**Work at 720p, finish at the target resolution.** Iterate cheaply, then regenerate the approved take.

---

## Core generation parameters

| Parameter | Type | Enum / range | Default | Notes |
|---|---|---|---|---|
| `aspectRatio` | string | `16:9` \| `9:16` | `16:9` | Only two. No square, no 21:9. |
| `resolution` | string | `720p` \| `1080p` \| `4k` | `720p` | 1080p and 4k are Veo 3.1 only — Veo 3 was 720p-only. |
| `durationSeconds` | integer | 4, 6, 8 | 8 | See the coupling table above. |
| `seed` | uint32 | any integer | random | For reproducibility across related generations. |
| `numberOfVideos` | integer | 1–4 | 1 | Variations per request. |
| `generateAudio` | boolean | `true` \| `false` | `true` | Leave it on — see below. |
| `personGeneration` | string | `allow_all` \| `allow_adult` | `allow_adult` | Content restriction. |
| `negativePrompt` | string | free text | none | Exclusion-only. See the caveat below. |

### `generateAudio` — the parameter you should not touch

Native synchronized audio is Veo 3.1's headline capability and the reason to choose it over most of the
catalogue. Disabling it gives you a silent video from a model priced for one that talks. If silent
output is genuinely wanted, a cheaper model is the better answer.

### `negativePrompt` — real, but Google discourages leaning on it

The parameter exists and accepts a comma-separated exclusion list
(`"wall, frame, urban background, man-made structures"`). Google's own guidance is to prefer positive
phrasing in the prompt over exclusion here, and never to write `no` or `don't` into either field —
Veo tends to render the named thing rather than omit it.

---

## Reference and input parameters

| Parameter | Type | Limit | Purpose |
|---|---|---|---|
| `image` | Image object | 1 | First frame for image-to-video. **Forces 8s duration.** |
| `lastFrame` | Image object | 1 | End frame; interpolates between two stills. |
| `referenceImages` | array | **3** | Character / style consistency. **Veo 3.1 only.** |
| `video` | Video object | 1 | Source for extension. Veo-generated, 720p, ≤141s. |

### `referenceImages` and `referenceType`

Each reference carries a `referenceType`:

- **`character`** — people and creatures, where identity must hold
- **`asset`** — objects, props, environments

⚠️ **The role assignment lives in this API field, not in the prompt.** Veo has no in-prompt reference
token of any kind — see `continuity-and-references.md`, which is the single most important thing to get
right on this model.

Google's guidance for the images themselves: 1–3 high-resolution stills, front-facing for characters,
and the *same* references reused across related shots.

---

## Video extension

| | |
|---|---|
| Length added per extension | **7 seconds** |
| Maximum extensions | **20** |
| Maximum total length | **~148 seconds** |
| Resolution | **720p only** |
| Source | Veo-generated video only |
| Source length cap | ≤141 seconds |
| Storage window | **2 days**, and the timer resets each time the video is referenced |

The two-day storage window is easy to lose a sequence to. An extension chain left over a weekend is
gone; re-generate from the beginning or keep the intermediate downloads.

---

## Prompt length

| | |
|---|---|
| Token limit | 1,024 |
| Approximate characters | ~7,500 |
| **Sweet spot** | **100–180 words, 3–6 sentences** |

The cap is a ceiling, not a target. Google's guidance is explicit that longer prompts confuse the
model, and the sweet spot is well under a fifth of the limit. No length ceiling is asserted for this
skill, because the useful number is the sweet spot, and the sweet spot is prose guidance, not a cap.

---

## Timestamp prompting

Multi-shot sequencing *inside* a single 8-second generation:

```
[00:00-00:02] Medium shot. Detective at desk, examining evidence.
[00:02-00:04] Footsteps echo on wooden floor.
[00:04-00:06] Close-up on the detective's face, realization dawning.
```

⚠️ **These brackets are TIMESTAMPS, not reference tokens.** Veo, Hailuo 2.3 and MiniMax H3 all use
square brackets in prompts and all three mean something different — timestamps, camera commands and
shot markers respectively. Nothing bracketed in a Veo prompt points at an attached image.

---

## Audio syntax

Three layers, each with its own convention. All three go in the prompt text.

| Layer | Form | Example |
|---|---|---|
| Dialogue | Speaker + verb + `"quoted text"` | `A detective murmurs, "This must be it."` |
| Sound effects | `SFX: description` | `SFX: thunder cracks in the distance` |
| Ambient | `Ambient noise: description` | `Ambient noise: the quiet hum of a starship bridge` |

Dialogue budget is **1–2 short lines per 8-second clip**, and the shot needs to frame the mouth clearly
for lip-sync to read.

---

## Veo 3 → 3.1, what actually changed

| | Veo 3 | Veo 3.1 |
|---|---|---|
| Resolution | 720p only | 720p / 1080p / 4k |
| Reference images | basic | 3, typed `character` / `asset` |
| Audio quality | good | richer, more natural |
| Lip-sync | decent | improved |
| Character consistency | limited | improved across shots |
| Motion physics | good | smoother |

---

## What Google does not publish

Recorded so nobody re-derives it from a third-party page:

- **No per-second or per-generation pricing** in the model documentation — it is on the Vertex AI
  pricing page and changes independently of the model.
- **No published cap on total reference-image file size**, only the count of 3.
- **No structured/JSON prompt format.** The "Veo 3 JSON prompting" templates circulating online are
  community inventions. Google documents a prose formula and timestamp prompting, both plain text.
  This is why no structured output format is defined.

---

## Further reading

- `best-practices.md` — the five-part formula, cinematography vocabulary, and the mistakes table
- `continuity-and-references.md` — how identity actually binds on this model, and why no token exists
- `examples.md` — annotated prompts across the modes
