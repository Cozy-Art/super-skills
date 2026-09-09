# Gemini Omni Flash — Example Prompts

Annotated examples across all four modes, drawn from the recurring example projects.

Note the durations: everything here is 3–10 seconds. That is the model's whole range.

---

## Example 1 — Single continuous take

**Project:** *Shadows of Ashford* · **Mode:** text-to-video

**Prompt:**
```
A single continuous take, no cuts.

Low-angle medium shot, slow push in. An elderly archivist in round wire
spectacles and a moth-eaten charcoal cardigan lifts a heavy ledger down from
a high shelf and turns it toward the window light. A long archive hall,
overcast north light through tall dusty glass, deep falloff into the stacks
behind him. Documentary realism, handheld with almost no movement.

Paper dragging against paper, a floorboard settling, low room tone. No
dialogue. No on-screen text.
```

**Settings:** 8s · 16:9 · 720p

**Technique notes:**
- **The first line is the most important one.** Without it, Omni Flash returns an edited sequence of
  several shots — its documented default. In 8 seconds that would be three cuts
- All six descriptive dimensions covered: framing, style, lighting, location, action, on-screen text
- **`No dialogue`** is deliberate. Native audio will otherwise fill silence with unscripted vocal
  performance, and there is no way to specify what it says
- One action. At 8 seconds there is room for one

---

## Example 2 — Timecoded mini-sequence

**Project:** *Shadows of Ashford* · **Mode:** text-to-video

**Prompt:**
```
[0-3s] Wide establishing shot of a disused railway platform at dusk, rain
blowing across it in sheets. Locked off.

[3-6s] Tight on the departure board as the split-flap letters roll over.
Slow push in.

[6-10s] The board settles on a single destination. The platform lights come
up, throwing long reflections on the wet concrete. Camera holds.

Documentary realism, flat grey light going to sodium orange. Rain on a tin
canopy, mechanical clatter of the letters, a distant announcement too
muffled to parse. No dialogue.
```

**Settings:** 10s · 16:9 · 720p

**Technique notes:**
- **Working with the default rather than against it.** A multi-shot result is what this model wants to
  produce; timecodes make the cut yours instead of its choice
- **Continuous ranges** — 0-3, 3-6, 6-10. A gap would leave the model improvising
- **Three beats in 10 seconds** is the comfortable ceiling. Four would rush
- One idea per beat. These shots are 3–4 seconds; they hold one thing each
- Style, light and audio stated once at the end, applying across all three shots

---

## Example 3 — First frame from an image

**Project:** *Aurelia* · **Mode:** image-to-video

**Prompt:**
```
<FIRST_FRAME> a single specular highlight travels slowly down the glass edge
and the amber liquid catches it. Almost imperceptible drift toward the label.

A single continuous take, no cuts. A crystalline chime, then a soft low room
tone settling behind it. No dialogue. No on-screen text.
```

**Settings:** 5s · 16:9 · 720p

**Technique notes:**
- **`<FIRST_FRAME>` tags the image inline**, at the point the description begins — the frame carries
  the product exactly, so the prompt never redescribes the bottle
- **Single-take instruction still required.** Supplying a first frame does not suppress the multi-shot
  default; a product shot cut three ways is not what anyone wants here
- Minimal, specific motion. Five seconds is enough for one highlight travel
- On-screen text suppressed deliberately — text rendering is a stated model limitation, so any label
  legibility should come from the supplied frame, not from generation

---

## Example 4 — Style and subject references

**Project:** *Neon Pulse* · **Mode:** reference-to-video

**References:** `@Image1` colour-grade plate, `@Image2` dancer portrait

**Prompt:**
```
[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]

In the style of <IMAGE_REF_0>, a dancer <IMAGE_REF_1> turns under a dead
neon sign on wet asphalt and stops mid-phrase as the light above her cuts
out. A single continuous take, handheld, low angle. The only remaining light
spills from an open doorway camera-right.

Rain on asphalt, a transformer buzz cutting to silence, a distant bassline
continuing through it. No dialogue.
```

**Settings:** 8s · 9:16 · 720p

**Technique notes:**
- **Zero-indexed references.** `<IMAGE_REF_0>` is the *first* reference image. Numbered references
  elsewhere start at 1 — this one starts at 0
- **The declaration block mixes bases**, and that is Google's own convention: `@Image1` counts uploads
  from 1, `<IMAGE_REF_0>` counts references from 0. Both in one line
- **Tag placement carries meaning** — `in the style of <IMAGE_REF_0>` binds that image to style,
  `a dancer <IMAGE_REF_1>` binds the other to the subject. Collecting the tags at the front would lose
  that
- Vertical delivery chosen in settings, never written into the prompt

---

## Example 5 — Conversational edit chain

**Project:** *Neon Pulse* · **Mode:** edit · Four turns on Example 4's result

**Turn 1:**
```
Make it night.
```

**Turn 2:**
```
Slow the camera move down. Keep everything else the same.
```

**Turn 3:**
```
Remove the reflection in the puddle. Keep everything else the same.
```

**Turn 4:**
```
Warmer light from the doorway. Keep everything else the same.
```

**Technique notes:**
- **This is the model's real strength**, and the prompts are shorter than people expect. Google's
  guidance is explicit that simple edit instructions outperform verbose ones
- **One change per turn.** Three changes in one turn produces three interpretations at once, and you
  lose the ability to attribute the result to any of them
- **`Keep everything else the same`** is Google's own documented preserve instruction. Worth using by
  default on anything but the most trivial edit
- **Continuity is free here** — the subject persists because it is the same clip, not because it was
  re-described. That is a different continuity model from re-describing the subject every time
- ⚠️ **Requires the original to have been retained.** The fastest generation configuration silently
  disables editing — see `parameters.md`
- Budget: each turn regenerates the clip at roughly $0.10/second. Four turns on an 8-second piece is
  about $3.20

---

## Example 6 — Sequence that will not fit

**Project:** *Stellar Drift* · **Scenario:** a 25-second corridor sequence

**Notes field:**
```
Omni Flash cannot produce this in one piece. Its ceiling is 10 seconds, and
it supports neither video extension nor first-and-last-frame interpolation —
both are documented as unsupported. There is no way to chain past the limit
within the model.

Two options:

1. Route to seedance-v2-5 (30s single-pass, extends twice) or minimax-h3
   (15s). Either handles this in one or two generations.

2. If Omni Flash's look is specifically wanted, generate three separate
   clips and assemble in an edit — but note that consistency across separate
   generations is a stated limitation on Google's own model card, and there
   is no persistent reference mechanism to hold the engineer's appearance
   between them. Expect visible drift.

Recommend option 1.
```

**Technique notes:**
- Following the D5 precedent — `notes` is where honesty lives, including recommending a different model
  when this one is the wrong choice
- The 10-second ceiling combined with no extension and no interpolation is the hardest constraint on
  this model, and the one most likely to be discovered too late

---

## Quick reference

| Situation | Approach |
|---|---|
| One continuous shot | `A single continuous take, no cuts.` — **required**, the default is multi-shot |
| A short cut sequence | Timecode blocks, continuous ranges, three beats max |
| Fixed opening frame | `<FIRST_FRAME>` inline |
| Style or subject reference | `<IMAGE_REF_0>`, `<IMAGE_REF_1>` — **zero-indexed** |
| Refining a result | Edit turns, one change each, `Keep everything else the same.` |
| Specific spoken lines | **Route elsewhere** — no documented way to script dialogue |
| Longer than 10 seconds | **Route elsewhere** — no extension, no interpolation |
| Legible on-screen text | **Route elsewhere** — stated model limitation |
| Video or audio as a reference | **Not available** — schema accepts video refs, model does not process them |
