# Grok Imagine Video 1.5 — Continuity and References

Grok Imagine Video draws one distinction unusually cleanly: **who appears** and **what they sound
like** are separate token systems, and neither substitutes for the other.

---

## Two token systems

| Token | Binds | Supplied via | Max |
|---|---|---|---|
| `<IMAGE_N>` | **Visual identity** — person, wardrobe, object, set | Reference images (and a pinned first frame) | **14** |
| `<AUDIO_N>` | **Voice timbre** — how a speaker sounds | A preset `voice_id`, or an audio clip ≤ 15 s where enabled | **3** |

xAI's own example uses both:

```
The person from <IMAGE_0> presents the product from <IMAGE_1> on the set from
<IMAGE_2>, speaking with the voice from <AUDIO_0>. A second speaker with the
voice from <AUDIO_1> replies.
```

**`<AUDIO_N>` is not a reference token.** It carries no likeness and no visual information — it selects
a voice. Only `<IMAGE_N>` holds identity. The two lists are numbered independently, each from zero.

This is the same trap that `kling-v3` documents at length, resolved correctly by the vendor here rather
than needing to be untangled. Grok and `minimax-h3` both keep the two layers genuinely separate.

---

## Writing reference tokens

**Angle brackets, inline, beside what they govern.** xAI's showcase prompt:

```
the model from <IMAGE_0> walks in from the back of the shot … they wear the
shirt from <IMAGE_1> and black flared jeans
```

`<IMAGE_0>` scopes to the person; `<IMAGE_1>` scopes to the shirt. Placement is the scoping mechanism —
there is no separate role-declaration syntax.

> **The `@Image1` form does not exist on this model**, despite circulating widely. It appears nowhere in
> xAI's documentation.

### The index base — zero, shifted by a pinned first frame

xAI's reference-to-video page now states it outright: *"Refer to reference images in the prompt by
their position in the list, starting at `<IMAGE_0>` for the first image."* And: *"If you also set
`image` to pin the first frame, it takes `<IMAGE_0>` and your reference images start at `<IMAGE_1>`."*

Earlier versions of the docs mixed 1-based examples with zero-based instructions; the current page is
consistent. Off-by-one is still the most likely cause of "the wrong image governed the wrong thing" —
count against what is actually attached.

`<AUDIO_N>` is zero-based too: `<AUDIO_0>`, `<AUDIO_1>`, `<AUDIO_2>`.

### How many

**Up to 14 reference images** per request on 1.5; 7 on classic `grok-imagine-video`. xAI's own
showcase binds 14 at once — a model, a room and 12 catalog products — with a preset voice. Some hosted
routes cap lower (7 is common) and restrict references at 1080p or alongside a start frame; the
interface wins.

---

## The resolution trade-off

Unusual, and worth deciding deliberately.

| Mode | Max resolution |
|---|---|
| Text-to-video | **1080p** |
| Image-to-video | **1080p** |
| **Reference-to-video** (references, voices, last frame, keyframes) | **720p** |

**Binding a character from reference images costs you the top resolution tier.**

When identity is already well-described in prose and does not need to match a specific asset, a
text-to-video generation at 1080p may be the better shot than reference-to-video at 720p. When identity
must match across shots, reference mode wins regardless of resolution.

Cost favours reference mode slightly: 720p is $0.14/second against $0.25 at 1080p.

---

## Continuity without a seed

**There is no `seed` parameter on this model.** Seed-locked reproducibility, a standard technique
elsewhere, is unavailable.

That leaves reference images and pinned frames as the continuity mechanisms, and the usual discipline
applies:

1. **Fix the asset.** One approved image per identity, reused as the same `<IMAGE_N>` slot every time.
   A different photo of the same person is a different reference
2. **Keep the binding phrasing identical.** If `<IMAGE_1>` is "the model" in shot one, it is "the model"
   in shot four — not "the woman"
3. **Keep slot numbers stable** across a sequence. Costs nothing, makes prompts diffable
4. **Write the character description once and reuse it verbatim** alongside the token. The reference
   does the heavy lifting, but the prose should not contradict it

**Do not promise repeatable output from a fixed seed.** It does not exist here.

### What the folklore claims, and why it is not in this skill

Third-party guides state that a single reference "holds up for 5–10 clips before drift," and that clean
backgrounds produce "roughly 60% more consistent subject appearance." Neither figure has a stated
methodology or a first-party source. The 60% number in particular should not survive into production
guidance.

The underlying advice — that uncluttered reference images bind more reliably — is plausible and matches
general experience. Treat it as a working heuristic, not a measured effect.

---

## Pinned frames as continuity

1.5 can pin exact images: `image` (first frame), `last_frame`, and up to four `keyframes` inside the
clip. That gives shot-to-shot handoffs a pixel-exact join:

- **Cut-matched sequences** — pin shot two's first frame to shot one's final frame
- **Arrival on an approved composition** — pin `last_frame` to the approved still
- **Loops** — the same image as `image` and `last_frame`

Any pinned frame puts the request in reference-to-video, so it caps at 720p. And with a pinned first
frame, reference tokens start at `<IMAGE_1>`.

## Voice continuity

`<AUDIO_N>` selects a voice via a preset `voice_id` (or, where the account allows, an uploaded clip of
up to 15 s). Use the same `voice_id` for a character every time and voice continuity across shots is
straightforward.

**Constraints:**

- Maximum **3** voices per generation
- **Own-audio voice references are trusted-partner only** per xAI's guide — the schema field exists,
  access is the gate
- **The script goes in the prompt** — quoted lines attributed to a speaker, with lip-sync

A recurring character can now hold both voice and words across a production: same `voice_id`, lines
written verbatim in quotes beside the speaker they belong to. For more than three speaking characters
in one shot, or for line-reading control beyond prose delivery notes, a dedicated voice model laid
against the picture is still the fallback.

---

## Extension

Runs on **classic `grok-imagine-video`**, not 1.5 — a 1.5 clip can be the source. Continues **from the
last frame** of the source. There is no frame-selection option; claims that 1.5
added one are unsupported.

**`duration` is the portion added, not the total.** A 10-second source with `duration: 5` returns 15
seconds.

**The extension range is 2–10 seconds, default 6** — narrower than the 1–15 range for generation.

Extension is the strongest continuity link available here, because it is pixel-continuous at the join.
Its limit is the usual one: it constrains the *start* of the new segment, and drift resumes after that.

---

## Editing

**Runs on the non-1.5 `grok-imagine-video` model**, so 1.5's improvements do not apply to edits.

**Inherit-then-cap:**

- Duration retains the source's, **capped at 8.7 seconds**. A 4-second input yields 4 seconds out
- Resolution matches the source's, **capped at 720p**. A 1080p input is downsized

This means an edit cannot be used as a finishing pass on a 1080p generation — the edit itself reduces
resolution.

---

## When to route elsewhere

- **More than three voiced speakers in one shot.** Three voice references is the ceiling
- **Reproducible output from a seed.** No seed parameter here
- **Per-attribute reference control.** `minimax-h3` splits appearance and motion within one subject
  definition, with explicit retention markers. Grok scopes by token placement, which is looser
- **More than 14 reference images.** `seedance-v2-5` takes 30
- **1080p with reference binding.** Not available in combination — pick one
- **Anything past 15 seconds in one generation**, or past 25 with an extension

**Reach for Grok Imagine Video when** a shot needs characters, products or sets bound from references
*and* assigned voices speaking scripted lines, and 720p is acceptable. The clean identity/voice
separation is genuinely useful, and few models offer voice assignment at all.
