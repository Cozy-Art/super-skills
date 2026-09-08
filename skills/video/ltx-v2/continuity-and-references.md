# LTX-2 — Continuity and Reference Features

---

## Image-to-Video (I2V): The Primary Consistency Tool

I2V is LTX-2's most reliable mechanism for visual consistency. Supplying a reference image locks the starting visual identity — composition, subject appearance, lighting, and color palette — so the prompt can focus entirely on temporal evolution.

### How It Works

- The reference image becomes the literal first frame
- The model generates all subsequent frames from that visual anchor
- The prompt handles only: motion, camera behavior, light changes, audio

### I2V Specifications by Mode

| Mode | Max Duration | Max Resolution |
|------|-------------|---------------|
| LTX-2 Pro I2V | 10 seconds | 2160p (4K) |
| LTX-2.3 Fast I2V | 20 seconds | 4K |

### Supported Image Formats

PNG, JPEG, WebP, AVIF, HEIF

Images must be a publicly accessible URL or base64 data URI for API use.

### Resolution Impact on I2V Quality

Source image resolution directly affects I2V output quality. Use minimum 1080p source images — higher resolution improves output quality significantly. Low-resolution inputs amplify artifacts in the generated frames.

### The I2V Prompt Rule

**Describe only what changes.** The image already contains everything static:

❌ **Wrong (wastes token budget):**
```
"A red Ferrari parked on a cobblestone street in Paris. It is raining.
The car is shiny and well-maintained. The camera pans left."
```

✅ **Correct (motion only):**
```
"The camera pans slowly left across the car's profile as rain streaks
down the windshield and reflections shift across the polished hood.
Sound: rain on stone, water on metal."
```

Everything described in the wrong example is already in the image. The second example describes only what changes and happens over time.

---

## First/Last Frame Interpolation (LTX-2.3 Fast Only)

Supply two keyframe images — the model generates all frames in between.

### How It Works

1. Provide an **opening keyframe** (first frame image)
2. Provide a **closing keyframe** (last frame image)
3. Write a prompt describing the motion and transition between them
4. The model fills all intermediate frames with appropriate motion

### Best Use Cases

- Controlled scene transitions (morning → evening)
- Before/after product reveals (closed box → open box)
- Narrative cutaways with defined start and end states
- Character entering and exiting frame with defined positions
- Lighting transitions (overcast → golden hour)

### Availability

- **LTX-2.3 Fast:** Full support
- **LTX-2.0 Pro:** Not available — Fast mode exclusive

---

## Video Chaining for Sequences Beyond Maximum Duration

For projects requiring more than 10s (Pro) or 20s (Fast) of continuous footage:

### Workflow

1. Generate the initial clip with the opening scene
2. Extract the **final frame** from the generated clip
3. Use that frame as the I2V input for the next generation
4. Write a new prompt describing only what changes next — do not re-establish the full scene
5. Repeat as needed
6. Stitch all clips in post-production

### Chaining Prompt Strategy

Each continuation prompt should:
- Describe the motion that begins immediately (no "initial hold" needed — the clip starts already in motion)
- Continue any camera path that was in progress
- Advance the narrative forward
- Use the same seed from the previous clip (see Seed Locking) to maintain visual style

### Maintaining Continuity Across Chains

- Use consistent style language in every prompt in the chain (same lighting descriptors, same aesthetic vocabulary)
- Keep camera terminology consistent (don't switch from "dolly" to "push in" for the same move across clips)
- Note seeds from each clip — the chain should use consistent seeds when style continuity matters

---

## Seed Locking for Visual Continuity

The `seed` parameter is the primary tool for cross-shot style consistency within a project.

### What Seed Locking Maintains

When the same seed is used with prompts in the same scene family:
- Lighting quality and color grade remain consistent
- Visual treatment and film aesthetic stay stable
- Minor variations from prompt changes are predictable and controlled

### Workflow

1. Generate a batch of clips (`numberResults: 3–5`) to explore variation
2. Identify the strongest result
3. Note the seed value from the API response metadata
4. Apply that seed to all subsequent related generations
5. Document seed + prompt + parameters as a reusable recipe

### What Seed Locking Does NOT Do

- Does not lock character appearance (use I2V references for that)
- Does not guarantee frame-for-frame identical motion (that varies with prompt changes)
- Does not transfer across model versions (seeds are version-specific)

---

## LoRA Fine-Tuning for Character Consistency

For projects requiring a specific recurring character — the highest-fidelity consistency method available.

### Recommended Training Configuration

| Setting | Value | Notes |
|---------|-------|-------|
| LoRA size | 16 | Higher = more identity capture; higher risk of overfitting |
| Learning rate | 0.0002 | Validated community configuration |
| Training resolution | 960×576 at 24 FPS | Optimal balance of quality and training speed |
| Training data type | **Video preferred over images** | Images train appearance; video trains motion, expression, vocal patterns |
| Minimum training clips | ~6 | Functional result; 12–20 for stable identity |

### Training Data Requirements

- Caption each clip accurately — the model learns visual-text pairs
- Mix angles, expressions, and actions — narrow training data = narrow generation range
- Include video at various focal lengths (close-up, medium, wide)
- Consistent lighting is not required but helps early training convergence

### Audio-Video Training Note

Audio and video learn at different rates during fine-tuning:
- Audio identity may appear before visual identity is fully trained
- If video is still generic but audio sounds correct → increase training steps
- Longer clips in training data improve audio-video synchronization

### Inference with LoRA

Load the trained LoRA at inference and reference the character via the same captions used in training. The character's appearance transfers through the LoRA weights without needing an I2V reference image.

---

## The Grid Method (Character Consistency Without LoRA)

For multi-shot character consistency without the training investment:

### Workflow

1. Use a text-to-image model (Qwen, Flux, or similar) to generate a **character grid** — multiple poses, expressions, and angles — in a single image
2. Crop individual panels from the grid into separate high-quality frames
3. Upscale each crop using an unblur LoRA for sharpness
4. Use each cropped frame as the I2V reference for its corresponding shot
5. All shots share identical visual DNA because they originated from the same grid generation

### Why It Works

The grid generation ensures all poses and angles are consistent with a single character identity — the same lighting interpretation, same underlying facial structure, same color palette. When individual frames are extracted and used as I2V anchors, the consistency carries through.

### Grid Method vs. LoRA

| Factor | Grid Method | LoRA Fine-Tuning |
|--------|-------------|-----------------|
| Setup time | 15–30 minutes | Hours of training |
| Identity stability | Good — consistent per clip | Excellent — stable across varied contexts |
| Generalization | Limited to grid variations | Can generate novel poses/contexts |
| Cost | No training compute | GPU training compute required |
| Best for | Short projects, one-off characters | Recurring characters, long-form productions |
