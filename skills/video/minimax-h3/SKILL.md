---
name: minimax-h3-prompts
description: Generate optimized prompts for MiniMax H3 (Hailuo 3.0) — a 33B omni-modal video model that jointly understands text, image, video and audio in one context and generates picture with native stereo sound in a single pass. Use this skill whenever a user mentions MiniMax H3, Hailuo 3, Hailuo 03, or wants a prompt for text-to-video, image-to-video, first/last-frame, or reference-to-video workflows on this model. Also trigger for requests involving typed reference tokens for character or location identity, multi-speaker dialogue with lip-sync in eleven languages, inline camera cues, shot markers and timestamps, or the structured six-section prompt format H3 uses in full-reference mode. Always use this skill instead of guessing at H3 prompt structure from general knowledge — its typed reference tokens, its separate speaker-attribution layer, and its structured section format are model-specific and easy to confuse with one another.
---

# MiniMax H3 Prompt Generator

Generate optimized prompts for MiniMax H3 — a 33B dense single-stream Transformer that takes text,
image, video and audio in one shared context and returns video with natively synchronized stereo
sound. Speech is lip-synced across eleven languages, and identity, motion and voice can each be
referenced independently from different source assets.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as clearly separated pieces: the **prompt**
and a short **suggested settings** line for the controls beside it. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Resolution, duration, aspect ratio, "2K", "vertical" —
none of it goes in the sentence. They are required API parameters with their own controls, and words
spent on them are words not spent on subject, action, camera, light and sound.

## Three Layers That Look Alike and Are Not

This is the thing to get right on H3, and the thing most likely to be conflated. The model has three
separate token systems that all look like "pointing at something."

| Layer | Tokens | What it binds |
|---|---|---|
| **Visual identity** | `<Subject 1>`, `<Picture 1>` | Who or what appears, and what it looks like |
| **Speech attribution** | `(S1)`, `(S2)` + `<d>…</d>` | Which character speaks which line |
| **Voice timbre** | `<Audio 1>` | What a voice sounds like |

MiniMax states the distinction directly: *"`<Subject N>` identifies the referenced subject, while
`(Sx)` identifies the actual speaker."*

They compose — one character can be all three at once — but they are not interchangeable, and a prompt
that uses `<Subject 1>` where it means `(S1)` will not route the dialogue correctly.

## Reference Tokens

Four typed tokens. **Angle brackets, capitalised type word, space, arabic numeral.** Numbering is
independent per category — `<Picture 1>` and `<Video 1>` are unrelated.

| Token | MiniMax's definition |
|---|---|
| `<Subject N>` | "Visible content abstracted from reference assets that can be reused or modified in the target video" |
| `<Picture N>` | "A reference image used as a concrete target frame or shot-planning anchor" |
| `<Video N>` | "A reference video that provides an editing source, continuation starting point, or whole-video temporal structure" |
| `<Audio N>` | "An audio signal that is copied or referenced" |

**Subjects are defined, then used.** Declare what a subject is by binding it to source assets, then
refer to it by token thereafter:

```
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue
cardigan, and a thin silver necklace.
```

A subject can draw different attributes from different sources — this is H3's most distinctive
capability:

```
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose
walking motion comes from <Video 1>.
```

### Retention markers

A fixed vocabulary describing how strongly a reference binds. Use the exact terms.

**Visual:** `fully_preserved` · `partially_preserved` · `attribute_transfer` · `weak_reference`
**Audio:** `fully_copy` · `partially_copy` · `reference` · `weak_reference`

`attribute_transfer` specifically means characteristics moved *to a different identifiable target
subject* — not "loosely inspired by." For a reference that only guides camera behaviour, `weak_reference`
on a `<Video N>` is the more accurate marker.

## Dialogue

Scripted speech uses a real tokenizer token. Two parts, both required:

```
<Subject 2> (S1) turns toward the woman and says, <d>[English] Last summer,
I went to my grandfather's house. He talked about you.</d>
```

- `(S1)`, `(S2)` — speaker IDs, assigned per speaking character and kept stable across the prompt
- `<d>[Language] … </d>` — the line itself, language named in square brackets

Two further tags exist for edge cases:

- `<scenetrans>` — dialogue continuing across a cut
- `<cutoff>` — speech truncated by the end of the video

**Eleven languages:** Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese,
Russian, Spanish.

**Dialogue lives only inside `<d>` within the main description.** Do not repeat lines in the soundscape
or music sections — that produces doubled audio.

## Inline Camera and Timing

H3 reads camera cues placed **directly after the description they apply to**, not collected at the end:

```
[pan]   [zoom]   [static]
```

Shot markers and timestamps are also read inline:

```
[Shot 1] … [Shot 2] …
At 00:04.000, …
```

## Structured Output

In full-reference mode H3 uses six named prose sections **in this fixed order**. This is the structure
[schema.json](schema.json) describes.

| # | Section | Carries |
|---|---|---|
| 1 | `subject_definitions` | Each `<Subject N>` bound to its source assets, with retention markers |
| 2 | `summary` | One or two sentences — what the shot is |
| 3 | `retention_analysis` | What must be preserved from each reference, and what may change |
| 4 | `detailed_description` | The main prose block: action, camera, setting, light, dialogue |
| 5 | `overall_soundscape` | Diegetic sound — effects and ambience |
| 6 | `non_diegetic_music` | Score, if any |

In text-to-video, image-to-video and first/last-frame modes the main block is named
`integrated_multimodal_description` instead, and sections 1 and 3 are omitted.

**Recommended length for the main description block: 350–500 English words** on generation tasks.

### Authoritative fields

H3 exposes six prose fields, and the main one changes name by mode, so **nothing is auto-synced**
between them. The `spec` sections are authoritative for the API call and the prose block is their
human rendering. If you revise one, revise all.

## Mode Selection

| Mode | Use when | Inputs |
|---|---|---|
| **Text-to-video** | Fully imagined scene | Prompt only |
| **Image-to-video** | Opening frame is fixed | Prompt + 1 image as `first_frame` |
| **Last-frame** | Ending is fixed, approach is open | Prompt + 1 image as `last_frame` |
| **First-and-last-frame** | Both ends fixed | Prompt + 2 images |
| **Reference-to-video** | Identity, motion or voice carried from assets | Prompt + reference assets |

**Image-to-video and reference-to-video are mutually exclusive.** `first_frame` and `last_frame` cannot
be combined with any `reference_*` role. Mixing them fails.

## Suggested Settings

Pair every prompt with a settings line. See [parameters.md](parameters.md) for the full table.

- **Resolution:** `768P` or `2K` — **required, no default.** 768P is the base model's native output; 2K
  comes from a separate regeneration pass
- **Duration:** 4–15 seconds, integer — **required, no default**
- **Ratio:** `adaptive` (default) or an explicit ratio. Must be explicit and non-adaptive for
  text-to-video; forced to `adaptive` for image-to-video; optional for reference-to-video
- **Audio:** always on — there is no disable parameter

## Reference Files

- **[parameters.md](parameters.md)** — Every documented parameter with its real enum and default, reference-asset
  limits and file caps, the two-stage 768P→2K path, pricing including per-asset input billing, and
  what MiniMax does not publish.

- **[best-practices.md](best-practices.md)** — Section-by-section guidance on the six-part structure, camera and timing
  cue placement, dialogue mechanics across multiple speakers, retention-marker selection, and a
  mistakes/fixes table.

- **[continuity-and-references.md](continuity-and-references.md)** — Subject definition in depth, drawing appearance and motion from
  different sources, holding identity across generations, and the three-layer distinction applied to
  real production cases.

- **[examples.md](examples.md)** — Annotated examples across all five modes, including multi-speaker dialogue, a
  split-source subject, and a full six-section structured output.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
