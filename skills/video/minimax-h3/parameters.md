# MiniMax H3 — Parameters

Every value below is from MiniMax's published API reference, OpenAPI schema, official prompt-writing
guides, or the Hugging Face model card. Where MiniMax publishes nothing, this file says so.

**Model ID:** `MiniMax-H3` — sole enum value
**Architecture:** H3-Omni-Transformer, 33B dense single-stream
**Output:** 24 fps, 32 kHz stereo

---

## Required parameters — note there are no defaults

Three parameters are required and **none of them has a server-side default.** Omitting any of them
fails. This is a common source of error, because most video models default at least resolution.

| Parameter | Type | Enum / range | Notes |
|---|---|---|---|
| `resolution` | string | `768P` \| `2K` | **Required, no default.** See the two-stage path below. |
| `duration` | integer | 4–15 | **Required, no default.** Integers only. |
| `ratio` | string | see below | **Required and non-`adaptive` for text-to-video.** Forced to `adaptive` for image-to-video. Optional for reference-to-video, where it defaults to `adaptive`. |

### The 768P → 2K path

**768P is the base model's native output.** The model card is explicit: *"The shorter side is set to
768 pixels by default."* 2K is not a higher-quality setting on the same model — it is produced by a
**separate H3-Regenerate-2K module** applied to a completed 768P generation via `role=base_video`.

Practical consequence: **generate and iterate at 768P, regenerate the approved take at 2K.** This is
cheaper per second and it is how the model is designed to be used.

---

## Prompt length

**7,000 characters.** Stated first-party twice — once in the video generation guide (*"Prompt length
limit ≤ 7000 characters"*) and once in the API schema (*"Length is counted by characters, with a
maximum of 7000 characters per `text`"*).

That is a ceiling, not a target. MiniMax's own recommendation for the main description block is
**350–500 English words** on generation tasks — comfortably inside the cap. Writing to the cap
degrades output long before it hits the limit.

---

## Reference assets

| Category | Max | Per-asset limits |
|---|---|---|
| Images | 9 | 256–5760 px per side; aspect ratio between 2:5 and 5:2; ≤30 MB |
| Videos | 3 | 2–15 s each, **combined ≤15 s**; ≤50 MB |
| Audio | 3 | Same duration rules; ≤15 MB |

**Combined ceiling: 12 files** across all categories, regardless of the per-category maximums.
Request body ≤64 MB.

**Audio cannot be the sole input.** It must be paired with an image or a video.

---

## Input modes — five, and two are mutually exclusive

| Mode | Inputs |
|---|---|
| Text-to-video | Prompt only |
| Image-to-video | Prompt + 1 image, `role=first_frame` |
| Last-frame | Prompt + 1 image, `role=last_frame` |
| First-and-last-frame | Prompt + 2 images |
| Reference-to-video | Prompt + `reference_*` assets |

**`first_frame` / `last_frame` cannot be combined with any `reference_*` role.** Frame conditioning and
reference conditioning are exclusive. Mixing them returns 400.

The last-frame-only mode is easy to miss and genuinely useful — it fixes where a shot ends and lets the
model find the approach.

---

## H3-Context-IR

A separate endpoint that produces the structured six-section prompt from looser input. The typed token
syntax (`<Subject N>`, `<Picture N>`, and so on) is Context-IR's **intermediate representation** — the
canonical form fed to H3-Base.

At the raw `/v2/video_generation` endpoint MiniMax's own examples use plain prose instead: *"The
character performs street dance, following the motion in reference video 1; the character's appearance
follows reference images 1 and 2."*

**H3 accepts both.** This skill emits the token form because it is unambiguous, per-attribute, and what
the vendor's own canonical representation uses.

---

## Audio

Native, generated in the same pass. **There is no audio-disable parameter** — audio is always on.

- 32 kHz stereo
- Lip-synced speech in **eleven languages**: Arabic, Chinese, English, French, German, Italian,
  Japanese, Korean, Portuguese, Russian, Spanish

---

## Pricing

Per-second output pricing is only part of the cost; **input material is billed separately**, which
matters on reference-heavy jobs.

| Item | Cost |
|---|---|
| 2K output | $0.13 / second |
| 768P output | $0.08 / second |
| 2K regeneration | $0.05 / second |
| Input images | First 5 free, then $0.04 each |
| Input video | Billed by input duration at output resolution |
| Input audio | Free |
| H3-Context-IR | $0.90 / M tokens in, $3.60 / M tokens out |

---

## Open weights — narrower than it sounds

MiniMax H3 is described as open-weight, but the details constrain what that means:

- Released under the **MiniMax H3 Community License Agreement** (`license: other` — not Apache, not MIT)
- **A separate application is required for the USA, EU, UK and South Korea**
- **Only H3-Base is open.** H3-Context-IR and H3-Regenerate-2K are **not** open-sourced

Since Context-IR is what produces the structured prompt and Regenerate-2K is what produces 2K output,
self-hosting H3-Base gives you the generator without either the structured-prompt front end or the
resolution back end.

---

## What has no parameter

- **`negative_prompt`** — does not exist. And unlike FLUX 3, in-prompt negation is **not** documented
  first-party for H3. Prefer positive description; if you use negation, treat it as untested.
- **Audio disable** — does not exist.
- **An Extend endpoint** — does not exist. The API surface is create / context-IR / regeneration /
  query / list / delete. Claims that H3 output is "extendable to ~30 s via a separate Extend tool"
  circulate widely and are unsupported; the documented ceiling is 15 seconds per generation.

---

## Further reading

MiniMax publishes official prompting **skills** alongside the model at
`github.com/MiniMax-AI/MiniMax-H3/tree/main/skills`, plus two prompt-writing guides in the model repo
(`VIDEO_PROMPT_WRITING_GUIDE_base_en.md` and `VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`). These are the
authoritative sources for the token syntax and section format described in this skill.
