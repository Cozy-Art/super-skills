---
name: seedance-2-5-prompts
description: Generate optimized prompts for ByteDance's Seedance 2.5 — a multimodal video model that generates up to 30 seconds in a single pass with native synchronized audio in 10+ languages, accepts up to 50 reference assets, and supports 3D clay-model camera control, storyboard and keyframe reference, timestamp-scoped editing, and forward or backward extension. Use this skill whenever a user mentions Seedance 2.5, Dreamina, Jimeng, or wants a prompt for reference-to-video, storyboard-driven generation, video editing, video extension, or seamless video transition on this model. Also trigger for many simultaneous character references, previz blocking from a clay render, or integer-second timestamp control. Always use this skill instead of guessing at Seedance 2.5 prompt structure — its tasks split into locked and unlocked categories that constrain aspect ratio and duration, several task types require literal trigger words in the prompt text, and its negative-control support is narrowly scoped in non-obvious ways.
---

# Seedance 2.5 Prompt Generator

Generate optimized prompts for ByteDance's Seedance 2.5 — a multimodal video model built for
production workflows rather than single impressive clips. Up to **30 seconds in a single pass**, up to
**50 reference assets** per request, native audio in 10+ languages, and editing and extension controls
that hold audio-visual continuity across joins.

Its distinctive capabilities are **reference breadth** (many subjects bound at once, from images,
video and audio) and **previz control** (a 3D clay-model pass can supply an entire camera performance).

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as two clearly separated pieces: the
**prompt** and a short **suggested settings** line. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Aspect ratio, resolution and duration are API
parameters with their own controls. ByteDance's guidance is explicit: do not restate settings already
selected in the UI.

One deliberate exception: writing something like "vertical phone video" to evoke an *aesthetic* is
legitimate. Writing "9:16" to set the canvas is not.

## Locked vs Unlocked — decide this first

Seedance 2.5 splits tasks into two categories, and the category determines **whether the shape of the
output is yours to choose at all.** This distinction does not exist in Seedance 2.0.

| | Locked | Unlocked |
|---|---|---|
| **Tasks** | Editing · First/last frame · Extension | Reference · Storyboard · Keyframe |
| **Aspect ratio** | **Inherited from the input asset** | Yours to choose |
| **Duration** | Editing: **inherited from the source clip.** First-frame and extension: yours | Yours to choose |
| **Why** | The input asset sits on the output timeline as a real segment | The input asset is only a semantic reference |

**Locked tasks adapt to their input.** An edit comes back the same shape and length as the clip it
edited. A first-frame generation comes back the shape of that first image. This is behaviour, not a
setting — there is nothing to override, and asking for a different shape in the prompt will not change
it.

Two consequences worth planning around:

- **Match your first and last frames.** If the last frame's aspect ratio differs from the first's, it
  gets stretched.
- **Edit at the shape you want to deliver.** An edit cannot reframe; if the source is 16:9, the result
  is 16:9.

*(Driving this through the API rather than a UI: locked tasks require `ratio: adaptive`, and editing
additionally requires `duration: -1`. See [parameters.md](parameters.md).)*

## Trigger Words — required, and easy to miss

**Editing and extension are selected by literal words in the prompt text**, not by a parameter alone.
Omitting the trigger means the model does not know which task it is performing.

| Task | Include at least one of |
|---|---|
| **Editing** | `edit video` · `add` · `insert` · `remove` · `delete` · `modify` · `replace` · `change to` |
| **Extension** | `extend forward` · `extend backward` · `continue` · `continue from` · `extend the story` |

Where multiple videos are supplied, **the model decides which one to act on from the prompt** — so name
the target explicitly.

## Reference Binding

**Number references by upload order and bind each one explicitly in the text.** That is the whole rule.

> ByteDance: *"The numbering should correspond to the upload order of the assets, such as Image 1 /
> Video 1 / Audio 1, and each asset should be explicitly bound in the text prompt."*

**The delimiter is not load-bearing.** ByteDance's own documentation uses `@Image1`, `@Image 1`,
`@video1`, `[Video 1]`, `<video1>` and bare `Image 1:` interchangeably across first-party examples.
Pick one and stay consistent within a prompt. This skill uses `@Image 1`.

### Bind the mapping in text, never only in the asset

> Avoid writing "John" on the protagonist's image and then just saying "John is at school." That causes
> character confusion or duplication.

Instead, state the mapping:

```
Image 1 depicts the protagonist John and uses the voice timbre from Audio 1.
Images 1-2 are Character 1 and correspond to Audio 1; Images 3-4 are
Character 2 and correspond to Audio 2.
```

### Say what each asset is a reference *for*

Partial references are supported and should be scoped explicitly:

```
Refer to the action of casting the spell in Video 1 and the wrap-around
camera movement in Video 2.
Refer to Image 1 for lighting and filters.
```

**When an asset is already accurate, just point at it.** Do not re-describe what it shows:

```
Strictly refer to the actions and camera movements in Video 1, and keep the
sequence consistent with the video.
```

## Prompt Structure

ByteDance's recommended shape, in order:

1. **Asset referencing** — each asset, its number, its job
2. **One-sentence summary** — Subject + Location + Event + Genre/Style + Camera movement
3. **Detailed plot description** — timestamps or `Shot N`, each segment's visuals, camera, action,
   dialogue and sound
4. **Additional notes** — what stays consistent throughout: camera angle, environment, atmosphere,
   recurring elements

For long or multi-subject prompts, bracketed section headers are ByteDance's own organising
convention: `[Subject settings]`, `[Overall style]`, `[Shot list]`, `[Strictly exclude]`.

## Timestamps

**Seedance 2.5 responds to integer-second timestamps. Seedance 2.0 does not** — 2.0 reads only shot
numbers. This is one of the headline upgrades.

Three supported forms:

- **Intervals** — `0-3 seconds… 3-7 seconds… 7-15 seconds` or `[1s-4s]… [4s-8s]`
- **Time points** — `Quick left sideways transition at the 5-second mark.`
- **Relative** — `After 3 seconds, everyone around him shakes their head.`

Rules:

- **No gaps in the timeline.** `0-3s… 5-6s…` leaves a hole the model fills unpredictably
- **Balance the load.** Too little plot in a range and the model improvises; too much and you get
  excessive cuts or dropped beats
- **Not for high-frequency action.** "Shake your head three times per second" will not work

## Dialogue

Native, lip-synced, 10+ languages. Put the line in **double quotes**, behind a speaker label:

```
Dialogue (elderly woman): "Fly safe, my child. Come back to me."
```

For sung or multilingual content, label each line:

```
English: "Hello"  Chinese: "你好"  Japanese: "こんにちは"
```

> **Bracket conventions circulating online are not real.** Claims that music takes parentheses, sound
> effects take angle brackets, dialogue takes braces `{ }` and subtitles take `【 】` appear in no
> ByteDance source and are contradicted by their own examples. Double quotes are what work.

## Negative Control — narrowly scoped, and that scope matters

ByteDance: *"Use positive descriptions whenever possible. Negative constraints are supported for
subtitles and audio control."*

**Documented as supported:**

- Subtitles — `No subtitles.` · `Do not add subtitles.`
- Audio, at fine granularity — `No BGM; generate only environmental sounds and action sounds.` ·
  `No audio.` Covers sound effects, background music and dialogue separately

**Beyond that scope**, ByteDance's own examples do use broader exclusions — `no text overlays, no
dissolve transitions, no duplicated people, only hard cuts`, and a `[Strictly exclude]` block listing
unwanted styles. These work in practice but sit outside the documented guarantee. Use them; prefer
positive description first.

## Mode Selection

| Mode | Use when | Locked? |
|---|---|---|
| **Text-to-video** | Fully imagined scene | No |
| **Reference-to-video** | Subject, motion, style, audio or scene carried from assets | No |
| **Storyboard reference** | A multi-panel board sets the plot at a high level | No |
| **Keyframe reference** | Visuals must align closely to supplied images, in order | No |
| **First / first-and-last frame** | Exact opening, optionally exact ending | **Yes** |
| **Video editing** | Add, remove or modify visuals or audio in an existing clip | **Yes** |
| **Video extension** | Continue a clip forward or backward | **Yes** |
| **One-click video creation** | Assemble a short video from several source assets | No |
| **Seamless transition** | Generate the missing in-between segment joining two clips | No |

**Storyboard vs keyframe — the distinction that matters:** a storyboard is a *high-level plot
reference* and will not be followed frame-for-frame. If visuals must align strictly, supply the panels
as independent keyframe images instead and open with `Use Images 1 to 7 in order as keyframes.`

## Suggested Settings

Whatever surface the director is generating on, these are the controls beside the prompt field — never
words inside it.

- **Duration:** **4–30 seconds**, or let the model choose within that range. Editing inherits the
  source clip's length
- **Resolution:** **480p or 720p only.** Seedance 2.5 does **not** offer 1080p or 4K — Seedance 2.0
  does. If a finishing-grade master is the requirement, that is a routing decision, not a settings one
- **Aspect ratio:** `21:9` · `16:9` · `4:3` · `1:1` · `3:4` · `9:16`, or adaptive. Under adaptive, 2.5
  can land on **any ratio between 0.4 and 2.5** by inheriting from the input assets — that flexibility
  comes from the assets, not from the control. Locked tasks are always adaptive
- **Audio:** on — native and synchronized
- **Output format:** `mp4` or `mov`. **Use `mov` for editing and extension** — better colour,
  brightness and audio-visual continuity across joins. 2.5 is the only Seedance that offers `mov`
- **Extension:** forward or backward from the source clip
- **No draft mode.** Unlike some models there is no cheap preview tier; iterate at 480p instead

## Reference Files

- **[parameters.md](parameters.md)** — Model ID, endpoint shape, the locked/unlocked parameter rules, `content.role`
  values, the full asset-count recommendations, and what ByteDance does not publish.

- **[best-practices.md](best-practices.md)** — Structure, timestamp discipline, camera language, action and expression
  description, storyboard and clay-model technique, negative control, and a mistakes/fixes table.

- **[continuity-and-references.md](continuity-and-references.md)** — Reference binding in depth, multi-subject mapping, subject
  count and viewpoint guidance, 3D clay-model rendering, and editing and extension continuity.

- **[examples.md](examples.md)** — Annotated examples across all major task types, based on ByteDance's own
  documented patterns.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
