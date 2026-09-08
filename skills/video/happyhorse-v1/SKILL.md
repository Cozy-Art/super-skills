---
name: happyhorse-1-0-prompts
description: Generate optimized prompts for Alibaba's HappyHorse 1.0 video generation model — the #1 ranked model on Artificial Analysis Video Arena at launch (April 2026). Use this skill whenever a user mentions HappyHorse, Happy Horse, Alibaba video generation, or wants to generate video with native joint audio (dialogue, foley, ambient), multi-shot sequences (up to 5 shots per call), image-to-video animation, reference-to-video with up to 9 reference images, natural-language video editing, or 7-language lip-sync (English, Mandarin, Cantonese, Japanese, Korean, German, French). Also trigger for any prompt that involves T2V, I2V, R2V, or video-edit workflows on fal.ai, Runware, WaveSpeed, or Cloudflare AI targeting this model. Always use this skill — do not guess at HappyHorse prompt structure from general knowledge, as its token-economy rules and positional weighting are model-specific and counterintuitive.
---

# HappyHorse 1.0 Prompt Generator

Generate optimized prompts for Alibaba's HappyHorse 1.0 — a unified 15B-parameter single-stream Transformer that processes text, image, video, and audio tokens in one forward pass. This architecture directly shapes how prompts must be written.

## The One Rule That Overrides Everything

**Prompt economy wins.** Every word competes for the same finite token budget as motion and audio tokens. A tight 20-word prompt consistently outperforms a 60-word prompt. When prompts run too long, quality degrades in a predictable order: **face consistency fails first → hand geometry → natural gait.**

Do not add filler. Do not add vague quality boosters. Spend every token on motion, audio, or constraints.

## Prompt Structure: Positional Weighting

Position determines influence weight. Order elements accordingly:

| Position | What goes here | Why |
|----------|---------------|-----|
| **Start** | Subject + action | Anchors who/what renders first |
| **Middle** | Environment + lighting | Sets scene without competing with subject |
| **End** | Camera direction | Receives **highest weight** for motion behavior |

### Full Production Order (6 layers)

For complex or final-quality prompts, use this ordered structure — do not interleave:

1. **Scene and timing** — where, when, and duration ("a sunlit Tokyo café, late morning, 8 seconds")
2. **Subject** — who/what, scale, pose, gaze, body framing
3. **Action and motion** — what moves, how intensely
4. **Camera** — movement, angle, shot size (one or two cues max)
5. **Lighting and texture** — direction, quality, temperature
6. **Audio** — dialogue in quotes + language tag, foreground sound, foley, ambient bed

### Syntax Rules (Hard)

- ✅ Natural English prose sentences
- ✅ Dialogue in quotation marks with explicit language tag: `dialogue in French: "Bonjour"` 
- ✅ Reference images as `[Image 1]`, `[Image 2]` — square brackets, spaced, numbered by upload order
- ❌ NOT `@Image1` and NOT `@element_name` — those are a hosting wrapper's syntax, not the model's,
  and will not resolve against Model Studio
- ❌ Tag lists, booru tags, JSON syntax, weighted parentheses `(keyword:1.2)` — ignored or misinterpreted
- ❌ Vague boosters: "cinematic," "epic," "8K ultra-detailed," "masterpiece" — no effect, wasted tokens
- ❌ 3+ camera cues stacked — conflicts average into generic motion
- ❌ Describing the image in I2V mode — wastes tokens, creates text/image conflicts

## Quick-Start Templates

### T2V — Simple (20-word target)
```
[Subject + action]. [Environment]. [Camera cue — last].
```
**Example:**
```
A young woman in a red coat walks down a wet city street at night,
neon reflections on the pavement, slow tracking shot.
```

### T2V — Full Production (6 layers)
```
[Location, time of day, duration].
[Subject: scale, pose, gaze, framing].
[Action: what moves, intensity].
[Camera: one or two cues max].
[Lighting: direction, quality, temperature].
[Audio: dialogue in quotes + language / foley / ambient / music or no music].
```

### I2V — Motion Only (describe only what changes)
```
[Motion description]. [Camera cue]. [Audio].
```
Never redescribe the image — it's already the first frame.

### Dialogue / Lip-Sync
```
dialogue in [LANGUAGE]: "[exact line, EXACT verbatim, no extra characters]"
```
Always specify the language. Always use quotation marks. Add "EXACT, verbatim" for precision.

### Multi-Shot
```
Protagonist: [single description at top — not repeated per shot]

Shot 1 (0–Xs): [Camera]. [Action]. [Audio].
Shot 2 (X–Ys): [Camera]. [Action]. [Audio].
Shot 3 (Y–Zs): [Camera]. [Action]. [Audio].
```

### Video Edit (NL instruction)
```
Change only [X]. Keep [invariant A], [invariant B], [invariant C] exactly the same.
[Restate the preserve list a second time — doubles its weight in the model.]
Reference: [Image 1] [describe its role].
```

## Three-Layer Audio Structure

Always name all three layers explicitly — the model guesses if any are unspecified:

- **Foreground:** Primary sound (dialogue, solo instrument, key effect)
- **Midground:** Action-tied sounds (clinking cups, footsteps, equipment)
- **Background:** Ambient tone (street traffic, restaurant chatter, wind)

Add "no music" or "music: [description]" at the end to control the music layer.

## Endpoint Selection

| You want to... | Use this endpoint |
|----------------|-------------------|
| Generate from text only | `alibaba/happy-horse/text-to-video` |
| Animate a single image | `alibaba/happy-horse/image-to-video` |
| Generate with 1–9 reference images | `alibaba/happy-horse/reference-to-video` |
| Edit an existing video clip | `alibaba/happy-horse/video-edit` |
| Multi-shot sequence (up to 5 shots) | fal multi-shot endpoint |

## Ideation vs. Final Workflow

1. **Draft at 720p / Std / audio off** — fastest, cheapest, calibrate composition
2. **Run two generations at same seed** — confirm determinism before tweaking
3. **Refine with single-change NL edits** on the existing clip — do NOT regenerate from scratch
4. **Final at 1080p / Pro / audio on**

Regenerating from scratch on every iteration is the #1 source of character and scene drift.

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — All API parameters for T2V, I2V, R2V, video-edit, and Runware output format endpoints. Parameter tables, valid ranges, recommended combinations by use case, pricing, and output specs.

- **`best-practices.md`** — Detailed guidance on prompt economy, positional weighting, audio design, lip-sync, photorealism anti-clichés, East Asian scene writing, common mistakes table with fixes, and the iterative refinement workflow.

- **`continuity-and-references.md`** — How to use seed-based reproducibility, I2V keyframing, frameImages first/last frame control, Reference-to-Video with 9 images, @element compositing, multi-shot sequencing, and the NL video-edit endpoint in depth.

- **`examples.md`** — 7 annotated example prompts covering: simple T2V character shot, dialogue/lip-sync scene, environment/landscape, action sequence, camera movement focus, style/mood (3D cartoon), and multi-shot narrative. Each includes formula label and technique notes.
