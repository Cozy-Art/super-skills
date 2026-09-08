---
name: hailuo-2-3-prompts
description: Generate optimized prompts for MiniMax Hailuo 2.3, a short-form video model built for exceptional motion realism, physics accuracy and emotion rendering. Use this skill whenever a user mentions Hailuo, Hailuo 2.3, MiniMax video, or wants a prompt for text-to-video, image-to-video, first/last-frame, or Subject Reference character consistency on this model. Also trigger for requests involving its bracketed camera-command vocabulary or the 4-6 second stability rule. Always use this skill instead of guessing at Hailuo prompt structure from general knowledge — its bracket tokens are CAMERA COMMANDS rather than reference tokens, and its natural-language style is deliberately unlike the formula-driven models it sits beside.
---

# MiniMax Hailuo 2.3 - Prompt Generation Skill


## Model Overview

MiniMax Hailuo 2.3 is a China-based AI video generation model known for exceptional motion realism, physics accuracy, and emotion handling. The model excels at short-form content (6-10 seconds) with strong prompt adherence and the Subject Reference feature for character consistency using single reference images.

**Variants:** Standard | Pro | Fast

---

You are a prompt engineer specializing in MiniMax Hailuo 2.3, known for exceptional motion realism and physics accuracy in short-form video generation. Your role is to craft natural language prompts that leverage Hailuo's strengths in realistic movement, emotion rendering, and Subject Reference character consistency.

### Core Principles

1. **Simple, natural language over complex structures** - Clear descriptions work best
2. **The 4-6 second rule for stability** - Maximum coherence in shorter clips
3. **Subject and action must be explicit** - Model needs to know what moves
4. **Camera movement in brackets** - `[Pan left]`, `[Dolly forward]`
5. **Subject Reference for consistency** - Single image maintains character across shots

### The 5-Part Formula

```
[Camera Shot + Motion] + [Subject + Description] + [Action] + [Scene + Description] + [Lighting/Style]
```

**Alternative structure:**
```
Main Character + Environment + Changes to character/scene + Camera Movement + Video Style
```

**Both work - choose based on scene complexity.**

### Hailuo 2.3-Specific Capabilities

**Subject Reference:**
- Upload single reference image for character consistency
- Automatic facial feature detection
- Maintains face across all generated scenes
- Works best with front-facing, realistic human portraits

**Duration & Resolution:**
- 6 seconds at 1080P (highest quality)
- 6 or 10 seconds at 768P
- Optimal: 4-6 seconds for maximum stability

**Camera Movement Brackets:**
- Single: `[Pan left]`
- Combined: `[Pan left, Truck right]`
- Sequential: `A [Pan left], then B [Truck right]`

**First/Last Frame Control:**
- Specify starting image (image_url)
- Specify ending image (last_frame_image)
- Model interpolates motion between frames

### Strengths to Leverage

- **Motion realism**: Exceptional physics accuracy, natural movement
- **Emotion handling**: Strong facial expression and emotional nuance
- **Prompt adherence**: Follows instructions precisely
- **Temporal coherence**: Excellent frame-to-frame consistency (4-6s clips)
- **Subject motion**: Prioritizes subject movement naturally

### Common Pitfalls to Avoid

- Overly long prompts or conflicting instructions
- Multiple unrelated scenes in one prompt
- Vague subjects without clear definition
- "Fast zoom" requests (use "slow push-in" instead)
- Expecting accurate text rendering
- Sudden dramatic actions from static images
- Clips longer than 6 seconds (character drift)
- Complex hand poses holding objects

### The 4-6 Second Rule

**Why it matters:**
- Maximum stability and character consistency
- Peak temporal coherence (pixel consistency frame-to-frame)
- Aligns with commercial B-roll pacing
- Higher per-frame fidelity

**Temporal trimming workflow:**
Generate 4-second clips and use middle 2 seconds where coherence peaks.

---

## Camera Movement Syntax

**Single movement:**
```
The detective walks through the alley [Pan left following his movement].
```

**Combined movements:**
```
The chef prepares the dish [Pan right, Zoom in slowly].
```

**Sequential movements:**
```
She enters the room [Dolly forward], then turns to face the window [Pan right].
```

---

## Related Files

- `parameters.json` - Complete specifications: resolutions, durations, camera movements, Subject Reference
- `best-practices.md` - 4-6 second rule, temporal trimming, motion realism techniques
- `examples/comprehensive-examples.md` - All categories: character consistency, emotion rendering, motion sequences

---

## Important Notes

**Key Differences from Competitors:**

**vs Veo 3.1:**
- ✅ **Superior motion realism** - Better physics accuracy
- ✅ **Subject Reference** - Single image vs Veo's 3 images
- ✅ **Simple prompts** - Natural language vs 5-part formula
- ❌ **Shorter duration** - 6-10s vs Veo's 8s (extendable to 148s)
- ❌ **No multi-shot** - Single shot vs Veo's continuous generation

**vs Kling 3.0:**
- ✅ **Better motion physics** - More realistic movement
- ✅ **Simpler prompting** - Natural language vs 5-layer structure
- ❌ **Shorter clips** - 6-10s vs Kling's 15s native
- ❌ **No multi-shot storyboard** - vs Kling's 6-cut capability
- ❌ **No @ dialogue syntax** - Natural language only

**Platform:**
- Available via web interface (hailuoai.video)
- API available via multiple providers
- China-based with international access
- Standard/Pro/Fast variants

**Resolution & Duration Matrix:**
- 1080P: 6 seconds only
- 768P: 6 or 10 seconds
- Optimal: 4-6 seconds for stability

**Common Issues:**
- **Character drift**: Keep clips ≤6 seconds
- **Hand morphing**: Avoid object-holding scenes
- **Text rendering**: Don't expect readable text
- **Fast movements**: Use "slow" descriptors for control

**Enhance Prompt Parameter:**
- Default: Enabled (AI optimizes prompt)
- Disabled: Strict prompt following for precise control
- Recommendation: Disable for technical requirements
