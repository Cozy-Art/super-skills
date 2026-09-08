# HappyHorse 1.0 — Best Practices Guide

---

## Prompt Economy: The Core Discipline

HappyHorse 1.0 processes text, image, video, and audio tokens in a single unified pass. Every word in your prompt directly competes for token budget with motion and audio tokens. This is fundamentally different from image-generation models.

**20 words is the target for single shots.**

When prompts exceed roughly 60 words, degradation follows a consistent pattern:
1. Face consistency fails first
2. Hand geometry distorts
3. Natural gait breaks down

The solution is never to write shorter descriptions of the wrong things — it's to write precise descriptions of the right things, then cut everything else.

---

## What to Emphasize

### Subject Specificity

Name scale, body framing, gaze direction, and object interactions explicitly.

✅ **Good:**
```
Full body visible, feet included, hands naturally gripping the handlebars
```

❌ **Bad:**
```
A person riding a bike
```

**High-value details to include:**
- Body framing: "full body," "waist up," "face only"
- Gaze direction: "looking directly at camera," "gaze left"
- Scale: "medium shot," "close-up on hands"
- Grip/contact: how subject physically interacts with objects

### Camera Language (Most Important Single Element)

HappyHorse 1.0 interprets standard cinematography terms reliably. The camera cue must go **at the end of the prompt** where it carries the highest weight.

**Camera moves that work well:**
- Slow dolly-in / slow push-in
- Tracking shot (specify direction: following left, panning right)
- Locked-off medium shot (best for dialogue)
- Handheld with slight shake
- Crane up / crane down
- Helicopter aerial sweeping [direction]

**One or two compatible cues maximum.** Stacking three or more averages into generic motion.

**Compatible pairs:**
- Slow dolly-in + slight tilt up ✅
- Tracking shot + crane up ✅

**Incompatible:**
- Dolly-in + dolly-out (cancels) ❌
- Pan left + pan right (cancels) ❌

### Audio Intent (Name All Three Layers)

The model generates audio by default and guesses if left unspecified. Always name all three layers:

**Three-Layer Structure:**
1. **Foreground** — Primary sound (dialogue, solo instrument, dominant effect)
2. **Midground** — Action-tied sounds (clinking cups, footsteps, cash register)
3. **Background** — Ambient tone filling the space (street traffic, café chatter, rain)

Then add explicit music direction: `no music` or `music: [description]`.

✅ **Complete audio direction:**
```
Foreground: espresso machine hissing; midground: ceramic cups clinking,
quiet conversation; background: muted street traffic. No music.
```

❌ **Underspecified:**
```
Ambient café sounds.
```

### Dialogue and Lip-Sync

The quoted literal triggers the lip-sync pathway. The language tag ensures phoneme alignment in that language.

**Format:**
```
dialogue in [LANGUAGE]: "[exact line]" — EXACT, verbatim, no extra characters
```

**Supported languages:** English, Mandarin, Cantonese, Japanese, Korean, German, French

**Examples:**
```
dialogue in French: "Tu as l'air fatigué ce matin, ça va?"
dialogue in Japanese: "おはようございます、今日もよろしくお願いします"
dialogue in English: "I know who did it." — EXACT, verbatim
```

**Rules:**
- Always use quotation marks
- Always specify the language — even for English
- Add "EXACT, verbatim, no extra characters" for precision-critical lines
- Keep lines short — one to two sentences per clip

### Lighting and Texture

Name direction, quality, and time of day specifically. Generic terms waste tokens.

✅ **Specific:**
```
Soft window light from camera-left, shallow depth of field, 50mm lens
```

❌ **Generic (no effect):**
```
Cinematic lighting
```

**High-value descriptors:**
- Direction: camera-left/right, overhead, backlit, side-lit, front-lit
- Quality: soft/diffused, hard/direct, dappled, fluorescent, practical
- Temperature: warm amber, cool blue, golden hour, blue hour
- Texture: available light, film grain, lens flare, shallow depth of field

---

## What to Avoid

| Avoid | What happens | Replace with |
|-------|-------------|--------------|
| Vague boosters: "cinematic," "epic," "8K ultra-detailed," "masterpiece" | Inherited from diffusion-model workflows — no meaningful effect on HappyHorse outputs | Specific techniques: "slow dolly-in," "warm amber backlight" |
| Booru-style tag lists | Model underperforms vs. the same content as a sentence | Rewrite tags as plain English prose |
| JSON or weighted parentheses `(keyword:1.2)` | Model ignores or misinterprets the structure | Write naturally |
| 3+ camera cues stacked | Cues conflict and average into generic motion | Pick one strong cue, two at most if compatible |
| Redescribing the image in I2V mode | Conflicts between image and text, wasted token budget | Describe only motion, sound, and lighting changes |
| No audio direction | Generic guessed audio bed | Name all three audio layers explicitly every time |
| Multi-region edits in one video-edit call | Three or more independent changes produce drift | Break into sequential single-change passes |
| Mixing prompt languages | Interpretation drift, especially on camera moves | Pick English or Mandarin and stay consistent throughout |

---

## Common Mistakes and Fixes

| Mistake | What happens | Fix |
|---------|-------------|-----|
| Prompt over 60 words | Faces drift, motion flattens, hands lose geometry | Cut to ~20 words; use multi-shot with timecodes for complex scenes |
| Booru tag lists | Model underperforms vs. prose | Rewrite tags as plain English prose |
| JSON or weighted parentheses | Ignored or misinterpreted | Remove all syntax, write naturally |
| "Cinematic," "epic," "masterpiece" | No meaningful effect | Replace with specific technique |
| Stacking 3+ camera cues | Cues conflict → generic motion | Pick one strong cue, two at most |
| Redescribing image in I2V | Text/image conflict, wasted tokens | Describe only motion, sound, and lighting changes |
| Forgetting dialogue quotes | Model paraphrases, lip-sync degrades | Always quote dialogue; add "EXACT, verbatim" |
| No audio direction | Generic guessed audio | Name all three audio layers explicitly every time |
| Multi-region edits in one call | Three or more independent changes produce drift | Break into sequential single-change passes |
| Mixing prompt languages | Interpretation drift on camera moves | Pick English or Mandarin and stay consistent |

---

## Photorealism: Anti-Clichés

For photorealistic output, name specific imperfections and add explicit anti-cues:

**Add:**
- Pores, fine lines, fabric wear
- Available light (not studio lighting)
- Slight motion blur
- Natural skin texture

**Add anti-cues:**
```
no glamorization, no heavy retouching, no smooth AI skin, no studio lighting
```

This pushes away from the generic AI portrait aesthetic toward naturalistic results.

---

## East Asian Scenes

HappyHorse 1.0 has strong world knowledge for East Asian settings:
- Beijing hutong courtyards
- Cantonese street markets
- Japanese izakaya interiors
- Korean bookshops

**Write these scenes in their native language** (Chinese, Japanese, Korean) for more physically accurate architectural and cultural detail than translated equivalents. The model's internal representation of these spaces is richer in the original language.

---

## I2V Mode Specifics

The uploaded image is the literal first frame. Do not describe it — describe only what changes.

**What to include in I2V prompts:**
- Motion type and intensity
- Camera movement
- Audio direction
- Lighting changes (if any)

**Camera motion guidance:**
- Best with small, named motion: "slow push-in, no more than 5%"
- Large camera moves on a still image break the source composition
- Avoid: "zoom out dramatically," "wide pan revealing scene" — these conflict with the fixed first frame

**Character consistency across I2V clips:**
Use the same reference image across every generation for the same character. The image anchors identity more reliably than text descriptions.

---

## Iterative Refinement Workflow

Starting from scratch on every iteration is the **single biggest source of character and scene drift**.

**Recommended pattern:**

1. Ship a clean base prompt at 720p/Std with audio off
2. Run two generations at the same seed to calibrate
3. Confirm the composition and character read correctly
4. Refine using single-change natural-language video-edit instructions on the existing clip
5. Change at most one or two elements per edit pass
6. Restate the invariants explicitly in every edit pass
7. Final pass: 1080p/Pro with audio on

**Video edit phrase-of-record:**
```
Change only [X]. Keep [A], [B], [C] exactly the same. [Restate: A, B, C remain unchanged.]
```
Restating the preserve list twice doubles its weight in the model.

---

## Duration Strategy

| Duration | Best for |
|----------|---------|
| 3–5s | Single action beats, product close-ups, reaction shots |
| 5–8s | Dialogue scenes, character introductions, most B-roll |
| 8–12s | Environmental reveals, action sequences, multi-beat moments |
| 12–15s | Full multi-shot scenes, narrative sequences |

**Character consistency note:** Temporal consistency degrades on clips longer than ~5 seconds for character identity. Multi-shot mode mitigates this by treating each beat as a semi-independent generation.

---

## Multi-Shot Audio Continuity

In multi-shot mode, maintain audio environment continuity across shots unless a deliberate cut is intended:

**Shot 1:**
```
ambient: café chatter, espresso machine. No music.
```

**Shot 2:**
```
same café ambient bed continues. Foreground: ceramic cups clinking.
```

**Shot 3 (deliberate audio cut):**
```
audio cuts to exterior: street traffic, wind, distant traffic. No music.
```

Naming the audio environment per shot prevents the model from generating inconsistent soundscapes across a sequence.
