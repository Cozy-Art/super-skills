# Seedance 2.0 — Best Practices Guide

---

## The Six-Block Formula, In Depth

Seedance 2.0's own prompt guidance converges on six blocks, written as 2–3 sentences rather than a long single paragraph. Order matters less strictly here than the *presence* of each block — but the natural grouping (subject + action + camera as sentence one, setting + lighting + style as sentence two, audio as sentence three) reads most predictably.

### 1. Subject

Name age, clothing, and distinguishing features explicitly — and then **reuse that exact wording** on every subsequent prompt for the same character or product. Consistency comes from repeating the description word-for-word, not from a "character lock" feature.

✅ **Good:**
```
A woman in her thirties with short black hair and a grey wool coat
```

❌ **Vague:**
```
A woman
```

### 2. Action / Motion

One primary action per clip. If the scene needs several beats, either split them into separate prompts or connect them with a native scene cut (see below) — don't chain them in one clause.

✅ **Good:**
```
walks toward the camera and smiles
```

❌ **Overloaded:**
```
walks in, sits down, opens a laptop, and starts typing
```

### 3. Camera

**The single biggest quality lever in a Seedance prompt.** State both movement and framing every time — clips read as flat and generic when the camera is left unspecified.

**Camera moves that work well:**
- Slow dolly-in / push-in
- Orbit (specify direction: "smooth 180-degree orbit")
- Tracking / follow shot (specify what it follows and from where)
- Handheld follow
- Crane up / crane down
- Locked-off / static — good default for dialogue, where camera motion competes with lip-sync clarity

**Framing terms:** medium shot, close-up, wide shot, tight vertical close-up, two-shot

Even a minimal instruction ("static locked shot") outperforms no instruction at all.

### 4. Setting & Lighting

Use real photography and location language, not mood words.

✅ **Specific:**
```
soft overcast daylight on a city sidewalk
golden hour backlight with long shadows
warm interior lamplight with soft reflections on the metal
```

❌ **Generic:**
```
cinematic lighting
```

### 5. Style

Pick **one** visual treatment and hold it. Stacking multiple, sometimes-conflicting style words is a common failure mode.

✅ **Good:** "clean documentary style," "premium commercial product style," "gritty handheld UGC style"

❌ **Stacked:** "cinematic, epic, hyperrealistic, anime-influenced, painterly"

### 6. Audio

Seedance 2.0 generates audio natively and in sync with the picture — describe what you want to hear as deliberately as what you want to see. Cover ambient bed, effects, music direction, and dialogue where relevant.

✅ **Good:**
```
quiet street ambience with footsteps and distant traffic
upbeat background music with a crisp pop on the reveal
ambient river noise and the soft whirr of the bicycle wheels
```

---

## Dialogue and Lip-Sync

Quoted text triggers the lip-sync pathway — the model generates matching mouth movement and a voice performance for the line.

**Format:**
```
[Subject] says, "[exact line]," [delivery description]
```

**Example:**
```
She leans forward and says, "You're going to want to see this,"
calm and confident.
```

**Rules:**
- Always use double quotes around the spoken line
- Add a short delivery note (tone, pace, emotional color) — it steers the voice, not just the transcript
- Keep lines short: one to two sentences per clip
- Pair with a locked-off or minimal-motion camera — a moving camera competes with lip-sync legibility

---

## Native Multi-Shot (Scene Cuts)

Seedance 2.0 can render more than one shot inside a single generation — there's no separate "multi-shot mode" parameter. The cut lives directly in the prose:

```
[Shot 1: subject, action, camera, setting]. Cut scene to [shot 2:
what changes, new camera/setting as needed].
```

**Example (from ByteDance's own reference material):**
```
An octopus finds a football in the ocean and excitedly calls its
octopus friends to come and play. Cut scene to an octopus football
game under the sea.
```

Keep each shot to one clear beat. Two to three shots is a realistic ceiling within the duration cap — pushing further tends to compress each beat until none of them land.

---

## What to Avoid

| Avoid | What happens | Replace with |
|---|---|---|
| Format words in the prompt ("16:9," "1080p," "10 seconds," "4K") | Wastes words that should describe the scene; doesn't reliably override the actual setting | Leave format entirely to the settings line |
| Adjective soup ("epic," "hyperrealistic," "8K," "masterpiece") | Called out explicitly in Seedance's own guide as weaker than concrete detail | Specific camera, light, or setting language |
| Chained actions in one clip | Beats compress and blur together | One primary action, or split into a scene-cut |
| Long negation lists ("no blur, no distortion, no extra fingers") | Tends to backfire per official guidance | Describe the positive outcome you want instead |
| Omitting the camera | Clips read flat and generic | At minimum, name a framing and whether the camera moves |
| Mixed, conflicting style words | Style becomes muddy or generic | Pick one label and hold it |
| Redescribing the source image in I2V | Wastes words on something already fixed; can create text/image conflicts | Describe only what changes: motion, camera, light shift, audio |

---

## Consistency Across Generations

- **Reuse exact subject and style wording** verbatim across every prompt for the same character, product, or brand series — this is the actual mechanism behind consistency, not a hidden model feature
- **Generate 2–3 variants** of the same prompt and pick the best — Seedance, like all diffusion/generation systems, is probabilistic; expecting one perfect render from a single call is the wrong mental model
- **Change one block at a time** when refining. If motion is weak, rewrite the camera/action clause. If the mood is wrong, rewrite lighting/setting. If the subject looks off, strengthen the subject description. Changing several blocks per iteration makes it impossible to tell what caused what
- **Keep a swipe file.** Once a prompt formula reliably produces the right character or product look, save it and reuse the wording rather than reconstructing it from scratch each time

---

## Iterative Refinement Workflow

1. **Draft short.** Start with a 4–5 second generation to check composition, subject read, and style before committing to a longer or higher-resolution render
2. **Generate 2–3 variants** at the draft settings and pick the strongest
3. **Refine one block at a time** on the chosen variant — camera, then lighting, then subject, as needed — rather than rewriting the whole prompt
4. **Move to Reference-to-Video** once you have a version you like, using it as `@Video1` to lock camera/motion or `@Image1` to lock a character look, so later prompts only need to describe what's new
5. **Final pass** at full duration and resolution once the formula is proven

---

## Photorealism Notes

For photorealistic output, name specific texture and imperfection details rather than relying on quality boosters:

**Include:** natural skin texture, fabric detail, available-light quality, shallow depth of field, subtle motion blur

**Avoid relying on:** "photorealistic," "8K," "ultra-detailed" as standalone descriptors — they add little on their own without concrete detail behind them
