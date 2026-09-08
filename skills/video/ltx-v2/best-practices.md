# LTX-2 — Best Practices Guide

---

## The Single Flowing Paragraph: Why It's Non-Negotiable

LTX-2's official documentation is unusually explicit: "Write your prompt as a single flowing paragraph."

This is not a style recommendation. The model's language understanding is optimized for narrative cohesion — it interprets how ideas connect, not just what ideas are present. A bulleted list tells the model what exists; a paragraph tells the model how everything relates, moves, and unfolds in time. The latter produces measurably better output.

**What a paragraph does that a list cannot:**
- Establishes causal relationships: "As the camera pulls back, the full market is revealed"
- Distributes motion across time: "Initially... after a moment... as the sequence continues..."
- Creates atmosphere through adjacency: "Rain streaks the window. Steam rises from her mug." — two images in proximity imply a warm/cold contrast the list equivalent misses
- Signals narrative intent that shapes generation quality

---

## Physical Cues Over Emotional Labels

LTX-2 cannot render internal states — only observable physical expressions. This is one of the most important modeling constraints to internalize.

### Conversion Table

| ❌ Abstract / Avoid | ✅ Physical / Use |
|--------------------|-----------------|
| "She is sad" | "Her eyes are downcast, lips pressed together, shoulders slightly hunched" |
| "He feels excited" | "His eyes are wide, leaning slightly forward, hands gesturing quickly" |
| "A mysterious woman" | "A woman in her 30s, dark hair pinned back, black coat, watching the door" |
| "Beautiful lighting" | "Side lighting from a single practical source, warm 3200K, deep shadow on one side" |
| "A tense atmosphere" | "Silence. Only the low hum of fluorescent lights. No movement." |
| "She looks happy" | "The corners of her eyes crinkle, a slight parting of the lips" |
| "Dramatic lighting" | "Hard overhead key light, deep shadow on the downstage side, rim light from behind" |

The test: can you photograph it? If yes, it's physical. If no, it's an emotional label — translate it.

---

## Camera Movement Vocabulary

LTX-2 responds to standard cinematographic terminology. Use these terms with motion intensity qualifiers.

### Movement Terms

| Term | Motion Type |
|------|------------|
| `dolly in / pull back` | Camera physically moves toward/away from subject |
| `track / tracking shot` | Camera moves laterally alongside subject |
| `pan left / right` | Camera rotates horizontally on fixed axis |
| `tilt up / down` | Camera rotates vertically on fixed axis |
| `orbit` / `circles around` | Camera moves in arc around subject |
| `crane up` | Camera moves vertically upward |
| `overhead view` | Top-down perspective |
| `handheld movement` | Organic, slightly unstable movement |
| `static frame` | No camera movement |
| `over-the-shoulder` | Behind subject perspective |
| `push in / pulls back` | Slow movement equivalent of zoom |

### Motion Intensity Qualifiers

Always pair a camera move with an intensity qualifier — the same "pan" can be gentle or whip-fast.

| Intensity level | Keywords |
|----------------|---------|
| Restrained | subtle, gentle, slight, imperceptible, barely perceptible |
| Moderate | steady, gradual, measured, smooth, controlled |
| Dynamic | dramatic, rapid, sweeping, vigorous, aggressive |

**Example:** `"The camera executes a slow, measured dolly in toward her face"` vs. `"The camera sweeps rapidly in a dramatic arc around the subject"` — the intensity qualifiers define the energy entirely.

---

## The Negative Space Rule

Static or empty frame regions — sky, water, plain backgrounds, walls — will **freeze** if the prompt doesn't explicitly animate them. This is one of the most common artifacts in LTX-2 output.

### The Problem

A prompt that says "A woman walks through a market" animates the woman and the camera. But the sky above the market stalls, the ground underfoot, and the cloth awnings remain motionless — visually obvious artifacts in an otherwise dynamic scene.

### The Fix

Add explicit motion to every region of the frame that matters:

| Region | Frozen without this | Add this to prompt |
|--------|--------------------|--------------------|
| Sky | Frozen blue plane | "clouds drift slowly overhead" |
| Water | Frozen mirror surface | "ripples spread across the still water surface" |
| Background foliage | Static leaves | "leaves rustle in a light breeze" |
| Curtains / fabric | Stiff, motionless | "curtains sway gently in a slight breeze" |
| Crowd/street (no focus) | Frozen figures | "background figures move through the market" |
| Smoke / steam | Static wisps | "steam rises steadily from the mug" |
| Dust / particles | Absent | "dust particles float visibly in the light beams" |

### Practical Check

Before finalizing any prompt: scan every region of the described frame. If a region isn't explicitly animated, either animate it or describe it as intentionally static: `"the still, glassy water surface reflects the sky"`.

---

## Temporal Distribution: The Most Important Technique

Front-loading all motion produces a common and severe artifact: all described events occur in the first 2–3 seconds, then the clip drifts or becomes static for the remainder of the duration.

**This is especially critical for 8–20 second clips.**

### Sequential Phase Language

Use temporal markers to distribute motion across the full duration:

```
"Initially, the camera holds on a wide shot of the market entrance.
After a moment, it begins a slow dolly forward.
As the dolly continues, the subject enters from the left.
By the final seconds, the camera reaches a medium close-up on her face."
```

### Temporal Marker Vocabulary

| Phase | Markers |
|-------|---------|
| Opening | "Initially," "At first," "The shot opens on..." |
| Transition | "After a beat," "After a moment," "Then," "Next," |
| Middle | "As the sequence continues," "During this," "Meanwhile," |
| Approaching end | "As the clip nears its end," "In the final seconds," |
| End state | "The camera comes to rest on..." "Final frame:" |

---

## Detail-to-Scale Matching

The level of descriptive specificity should match the shot scale.

**Close-up:** Requires microexpression cues, skin texture language, specific eye-direction
```
"Her left eye twitches slightly, brows drawing together. Skin texture visible in the harsh sidelight.
Her gaze tracks slowly from left to right."
```

**Medium shot:** Requires posture, gesture, costume interaction
```
"She shifts her weight from her left foot, one hand fidgeting with the strap of her bag."
```

**Wide/establishing shot:** Requires environmental and atmospheric description, fewer subject details
```
"The market stretches back into darkness, lanterns hanging at irregular intervals,
figures moving between stalls — individual faces indistinct."
```

Over-describing a wide shot wastes token budget on invisible detail. Under-describing a close-up leaves the model guessing.

---

## LTX-2 Strengths and Limitations

### What LTX-2 Handles Well

- Cinematic compositions with thoughtful lighting and natural motion
- Emotive single-subject moments — subtle gestures, facial nuance, restrained emotion through physical cues
- Atmosphere: fog, mist, golden-hour light, rain, smoke, reflections
- Clear camera language with explicit cinematographic terms
- Stylized aesthetics: painterly, noir, analog film, fashion editorial
- Voice: characters speaking and singing in multiple languages, synchronized via dialogue quotes
- Product and architecture walkthroughs with controlled camera paths

### Known Limitations

- **Text and logos:** Unreliable within video — add in post-production
- **Complex physics:** Explosions, large crowds with simultaneous actions introduce artifacts
- **Overloaded scenes:** Many characters + simultaneous actions = reduced clarity; simplify
- **Conflicting lighting:** Two contradictory light sources in the same scene confuse interpretation
- **Extreme close-ups on faces at high motion:** Risk of uncanny valley; use Pro mode and reduce motion intensity
- **Exaggerated expressions:** The model renders subtle physical cues well; exaggerated expressions often produce distortion

---

## Iteration Workflow (6 Steps)

1. **Start at 6 seconds, 1080p, 25 FPS** — minimum cost and time for baseline evaluation
2. **Use Fast mode for all drafts** — 2× faster, 1/10 the compute; find creative direction before committing
3. **Change one variable per iteration** in this order: motion description → camera work → environmental elements → style → audio
4. **Lock the seed** from any result you like — reuse the seed value from the API response to reproduce
5. **Batch generate** (`numberResults: 3–5`) with the same prompt to sample natural variation before changing the prompt
6. **Re-render in Pro** when the visual result is correct but final polish is needed for delivery

---

## Common Mistakes and Fixes

| Artifact | Root Cause | Fix |
|---------|-----------|-----|
| Frozen regions in frame | Empty areas lack motion prompts | Add explicit motion for all elements: "clouds drift," "water ripples," "curtains sway" |
| Jittery or conflicting motion | Multiple competing motion directions | Reduce to a single, clear motion vector |
| Subject distortion | Physics-violating prompt | Ground motion in realistic physical constraints |
| Inconsistent lighting across frames | Vague light description | Specify light source, color temperature, behavior |
| All motion front-loaded | Single-phase prompt | Use sequential phase language: "Initially... After a moment... As the sequence continues..." |
| Face flicker or drift | High motion + face emphasis | Tighten crop to face/upper torso; reduce motion intensity; avoid exaggerated expressions |
| Scene cuts abruptly mid-generation | Fast mode edge case | Use Pro for stable 6–10s clips; use sequential chaining for longer Fast clips |
| Running figure freezes initially | Fast mode latency | Use Pro for character animation; add explicit motion from frame 1: "immediately begins walking" |
| Audio out of sync with action | Temporal mismatch | Use phase-based prompt describing audio events at same pace as visual events |
| LoRA audio clicks in before video | Differential learning rate | Increase training steps; use longer clips in training data |
| Image quality degradation in I2V | Low input resolution | Use minimum 1080p source images; higher resolution improves I2V output significantly |
