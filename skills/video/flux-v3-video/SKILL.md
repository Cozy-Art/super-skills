---
name: flux-3-video-prompts
description: Generate optimized prompts for Black Forest Labs' FLUX 3 Video — a unified multimodal model that generates video with natively synchronized audio, including multilingual speech with lip-sync, sound effects, and ambience, in a single pass. Use this skill whenever a user mentions FLUX 3, FLUX 3 Video, BFL video generation, or wants a prompt for text-to-video, image-continuation, video-continuation, or draft-enhance workflows on this model. Also trigger for requests involving keyframe-timed generation, multi-shot sequences inside one generation, spoken dialogue in video, or the draft-then-enhance preview workflow. Always use this skill instead of guessing at FLUX 3 prompt structure from general knowledge — its keyframe semantics differ fundamentally from reference-image conventions on other models, its audio direction is written inline as a distinct prompt layer, and it endorses in-prompt negation despite having no negative-prompt parameter.
---

# FLUX 3 Video Prompt Generator

Generate optimized prompts for Black Forest Labs' FLUX 3 Video — a unified multimodal model that
produces video and synchronized sound together in one pass. Speech is multilingual and lip-synced,
effects and ambience are generated with the frames, and a single generation can carry multiple shots
across hard cuts while holding character, look and audio bed continuous.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are actually generating with. Every result ships as two clearly separated pieces:
the **prompt** (natural-language text, ready to paste into the prompt field) and a short **suggested
settings** line for the controls sitting next to that field. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Aspect ratio, resolution, duration, "4K", "vertical" —
none of it goes in the sentence. Those are controls, and words spent on them are words not spent on
subject, action, camera, light and sound. Every word in the prompt should describe what happens on
screen or on the soundtrack. Nothing else.

## Audio Is a Separate Layer, Written Inline

This is the thing FLUX 3 rewards most and the thing most prompts under-use. The model generates sound
with the picture, so the prompt has to direct both. Treat audio as its own pass over the scene rather
than a trailing clause.

Three layers, each worth naming explicitly:

| Layer | What it covers | Example fragment |
|---|---|---|
| **Speech** | Spoken lines, delivery, language | `A presenter speaks to the lens: "Storm season is here."` |
| **Effects** | Discrete, motivated sounds tied to on-screen events | `boots on wet gravel, a latch turning over` |
| **Ambience** | The continuous bed under everything | `low wind across open moorland, distant rooks` |

### Dialogue — hard rule

**Quote the line and the character says it.** This is BFL's documented trigger, verbatim: *"Quote the
line in your prompt and the character says it."*

```
A presenter speaks to the lens: "Storm season is here."
```

- Use straight double quotes around the exact words
- Name or describe the speaker immediately before the line so attribution is unambiguous
- Add a delivery note — it steers the performance, not just the transcript
- Keep lines short enough to land inside the clip; a 5-second shot holds one sentence, not three

## Prompt Shape

FLUX 3 takes one free-text string. Write it as flowing prose in this order — it front-loads what the
model anchors on first:

```
[Subject + action] → [Setting + light] → [Camera] → [Audio: speech, effects, ambience] → [Constraints]
```

Shot vocabulary beats thematic vocabulary. "Handheld medium shot, slight lag on the pan" gives the
model something to execute; "cinematic and dramatic" does not.

## Mode Selection

| Mode | Alias | Use when | Needs |
|---|---|---|---|
| `t2v` | `text-to-video` | Fully imagined scene, no existing asset | Prompt only |
| `i2v` | `image-continuation` | You have frames to hit — an opening image, an opening and closing pair, or a set of beats | Prompt + `keyframes` |
| `v2v` | `video-continuation` | Continuing an existing clip | Prompt + `start_video` |
| `draft_enhance` | `draft-enhance` | Re-rendering an approved draft at full quality | The draft's cache bundle |

### Keyframes are frames, not references

This is the most common way to get FLUX 3 wrong. `keyframes` accepts up to 10 images, which looks like
a reference-image array on other models. It is not. BFL: *"Your images become frames of the video…
one starts the video, two start and end it, with more the first starts it, the last ends it, and the
rest fall evenly in between."*

Consequences for how you write the prompt:

- **Never write "the character from the first reference image."** There is no reference slot to point
  at. That phrasing is borrowed from image-editing models and will not bind.
- **Describe the motion between the frames**, not the frames themselves. The images already supply
  their own content; the prompt supplies what happens in the gaps.
- Frames can be placed on the timeline explicitly rather than spaced evenly, which is how you control
  pacing: `[[0, "..."], [3.5, "..."]]`.

### No cross-generation identity mechanism — yet

FLUX 3 holds character and look **within** a single generation, including across hard cuts. It has no
documented way to carry an identity **between** generations — no reference token, no attachment slot.
BFL states Omni Reference for images and video is coming but not shipped.

Until it does, continuity across shots comes from disciplined description: write the character's
description once, reuse it verbatim in every prompt, and prefer one longer multi-shot generation over
several short ones whenever the shots need to match. See `continuity-and-references.md`.

## Multi-Shot Inside One Generation

FLUX 3 can carry several shots in a single generation, with continuity holding across the cut and one
audio bed running underneath. Write the cut into the prose:

```
SHOT ONE — [description]. HARD CUT. SHOT TWO — [description].
```

Keep each shot to one clear beat. This is the strongest continuity tool the model has, precisely
because there is no cross-generation reference mechanism.

## Negation — the exception worth knowing

FLUX 3 has **no negative-prompt parameter**, and BFL's general guidance is that most FLUX models don't
support negative prompts. But BFL's own FLUX 3 Video examples use in-prompt negation heavily and
deliberately, and list it as the fix in their troubleshooting table:

```
No on-screen text, no subtitles.
No announcer delivery, no sales voice.
No music, no second voice.
```

So: **positive description first, targeted negation second** — and reach for negation specifically when
the model keeps adding something you don't want. This is the opposite of the advice for most models in
the catalogue, and it is vendor-endorsed here.

## Suggested Settings

Pair every prompt with a short settings line. See `parameters.md` for the full table.

- **Mode:** `t2v` · `i2v` · `v2v` · `draft_enhance`
- **Duration:** `auto` (default) or 5–20 seconds
- **Resolution:** `hd` (default) or `fhd`
- **Aspect ratio:** `auto` (default), 21:9, 2:1, 16:9, 4:3, 1:1, 3:4, 9:16
- **Audio:** on by default — leave it on unless a silent draft is specifically wanted
- **Draft:** on for exploration, then re-render the approved take through `draft_enhance`

### Use the draft workflow

`draft` generates a fast, low-cost preview. When one is approved, `draft_enhance` re-renders it at full
quality from a cache bundle that pins the mode, prompt, seed and conditioning media — so the enhanced
version is the same take, not a re-roll. Recommend this whenever a director is exploring rather than
finishing: it is much cheaper to find the shot in draft and enhance once.

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Full settings reference: every documented parameter with its real enum and
  default, keyframe timing syntax, the draft/enhance bundle, safety tolerance, and what BFL does *not*
  publish (there is no stated prompt-length cap).

- **`best-practices.md`** — Prose shape and ordering, shot vocabulary that works versus thematic
  vocabulary that doesn't, the three audio layers in depth, dialogue and lip-sync mechanics, the
  in-prompt negation pattern, and a mistakes/fixes table.

- **`continuity-and-references.md`** — Why `keyframes` are not references, how to hold a character
  across shots without a reference mechanism, multi-shot single-generation technique, and the
  workarounds to use until Omni Reference ships.

- **`examples.md`** — Annotated example prompts across all four modes, including a dialogue scene, a
  keyframe-timed sequence, a multi-shot single generation, and a draft-to-enhance workflow.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
