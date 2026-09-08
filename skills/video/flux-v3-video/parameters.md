# FLUX 3 Video — Parameters

Every value below is from Black Forest Labs' published OpenAPI schema and docs. Where BFL publishes
nothing, this file says so rather than supplying a number.

**Endpoint:** `POST https://api.bfl.ai/v1/flux-3-video`
**Auth:** `x-key` header
**Pattern:** async — submit, receive a `polling_url`, poll until `status: "Ready"`
**Output:** `result.sample` is a signed `.mp4` URL

---

## Modes

`mode` is the discriminator. Four values, each with an alias:

| Value | Alias | Conditioning input |
|---|---|---|
| `t2v` | `text-to-video` | none |
| `i2v` | `image-continuation` | `keyframes` |
| `v2v` | `video-continuation` | `start_video` |
| `draft_enhance` | `draft-enhance` | `draft_cache` |

---

## Core parameters

| Parameter | Type | Range / enum | Default | Notes |
|---|---|---|---|---|
| `prompt` | string | — | required | Single free-text field. Carries scene, camera, audio and constraints together. |
| `duration` | integer or `"auto"` | 5–20 | `"auto"` | **Minimum is 5**, not 4. There is no numeric default — `auto` lets the model choose. |
| `resolution` | string | `hd` \| `fhd` | `hd` | **Not** a 480p/720p/1080p enum. `fhd` = 1920×1088 at 16:9, 24 fps. |
| `aspect_ratio` | string | `auto`, `21:9`, `2:1`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` | `auto` | `2:3` and `3:2` **do not exist** on this model. `2:1` does. |
| `generate_audio` | boolean | — | `true` | Audio is on unless explicitly disabled. |
| `safety_tolerance` | integer | 0–4 | `2` | |
| `draft` | boolean | — | `false` | Fast, cheap preview render. |
| `draft_cache` | bundle | — | — | Encrypted bundle from a draft; pins mode, prompt, seed and conditioning media for `draft_enhance`. |
| `version` | string | `latest` | `latest` | |

## Conditioning inputs

| Parameter | Type | Limits | Notes |
|---|---|---|---|
| `keyframes` | array | 1–10 images | **Frames on the timeline, not identity references.** See below. |
| `start_video` | mp4 URL or base64 | — | `v2v` only. |

### Keyframe placement

Default behaviour, in BFL's own words: *"Your images become frames of the video… one starts the video,
two start and end it, with more the first starts it, the last ends it, and the rest fall evenly in
between."*

For explicit placement, use the timed form — a list of `[seconds, image]` pairs:

```
[[0, "..."], [3.5, "..."], [9, "..."]]
```

This is how you control pacing rather than accepting even spacing.

---

## What has no parameter

- **`negative_prompt`** — does not exist. In-prompt negation is documented and endorsed instead; see
  `best-practices.md`.
- **Cross-generation reference / identity binding** — does not exist. BFL: *"Video editing and Omni
  Reference with images and videos will be available soon."*
- **A FLUX 3 image endpoint** — does not exist. Only `/v1/flux-3-video` is published. FLUX 3 image is
  a separate, unshipped thing; FLUX.2 remains the current BFL image model and has its own skill.

---

## What BFL does not publish

**Prompt length.** There is no character or token cap stated anywhere in BFL's docs, schema, or
prompting guides for FLUX 3. A 512-token figure circulates in third-party write-ups; it is a FLUX.1
Kontext fact carried across by analogy and should not be presented as a FLUX 3 limit.

No length ceiling is asserted here for that reason. Write to the
scene, not to a budget — but note that BFL's own examples are compact, and long adjective-stacked
prompts underperform tight ones here as they do everywhere.

---

## Audio

Native, generated in the same pass as the frames. Covers multilingual speech with lip-sync, discrete
effects, and continuous ambience. Directed inline in the prompt — there is no separate audio field.

Disabling audio via `generate_audio: false` produces a silent clip; there is no documented cost saving
in doing so, so leave it on unless a silent draft is specifically wanted.

---

## Deprecations

BFL has documented deprecations effective 31 October 2025 covering `flux-pro-1.0`, `flux-pro-1.0-depth`,
`flux-pro-1.0-canny` and the entire Finetuning API. None affect FLUX 3, but any claim that BFL has
never deprecated anything is false.
