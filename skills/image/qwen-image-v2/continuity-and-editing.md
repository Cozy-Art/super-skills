# Qwen Image — Continuity and Editing Reference

---

## Seed-Based Reproducibility

Fixing `seed` is the **primary tool for reproducibility** in generation.

Same `seed` + same `prompt` + same model version = identical output.

### Workflow
1. Generate a set of images with **random seeds** — find the right direction
2. Identify the best result — note its seed from the output metadata
3. **Lock that seed** and refine the prompt incrementally
4. Change only **one variable at a time** to isolate what each change does
5. Set `enable_prompt_expansion: false` (2.0 API) to prevent auto-rewrites breaking reproducibility

### Important Limitation
Seed + same prompt = identical output *within the same model version*. Different API snapshots or model updates may produce different results even with the same seed.

---

## Image-to-Image (I2I) Reference

The **Qwen-Image-Edit** models (2509, 2511) and the unified 2.0 model accept reference images for identity or style anchoring.

### Single Reference Image

```
Edit the image, change the background to a snowy mountain scene.
Preserve the subject's face, clothing, and expression exactly.
```

### Multi-Image Reference: Positional Label Syntax

The model references images by position using explicit labels in the prompt.

**Critical syntax rules (community-validated):**
- ✅ Space between "image" and number: `image 1`, `image 2` (not `image1`)
- ✅ Always add preserve instruction: `"preserve [subject] unchanged"` or `"keep [element] identical"`
- ✅ Simplify prompts for multi-reference — structure over description detail
- ✅ Start with 2 images before attempting 3-image compositions
- ✅ Identity preservation is more reliable than full pose transfer

**Example (outfit swap, 2 images):**
```
Edit image 1, replace the woman's outfit with the red dress from image 2.
Keep her face, hair, and background unchanged.
```

**Example (3-image scene placement):**
```
Image 1: subject to place. Image 2: target background scene. Image 3: lighting style reference.
Place the subject from image 1 into the scene from image 2.
Match the lighting approach from image 3.
Preserve the subject's face, proportions, and expression exactly.
```

---

## Supported Reference Modes (Edit Models)

| Mode | Capability | Prompt Pattern |
|------|-----------|----------------|
| **Scene placement** | Insert person into new background | "Place the subject from image 1 into the scene from image 2" |
| **Outfit swap** | Change clothing using reference | "Replace the jacket with the coat from image 2. Preserve face." |
| **Pose transfer** | Apply pose from keypoint map | Use ControlNet pose node + "Match the pose from image 2" |
| **Style transfer** | Re-render in reference style | "Re-render this image in the painting style of image 2" |
| **Wedding composite** | Combine two people into scene | "Combine the man from image 1 and woman from image 2 in a wedding scene" |

### Community Tips for Multi-Image Editing

- Three-image compositions are challenging — build reliability with 2-image workflows first
- For outfit swaps: describe the garment in the prompt in addition to referencing the image — this doubles the model's constraint on the target clothing
- For face preservation: include the face description from your anchor prompt in addition to "preserve face" instruction
- Results are more reliable for global changes (background swap, style transfer) than for fine local edits (changing a specific accessory)

---

## LoRA: Character and Style Consistency

For v1/2512 (open-weights), LoRA is the primary tool for persistent character consistency across multiple generations.

### LoRA Parameter Recommendations

| LoRA Type | Recommended Scale | Notes |
|-----------|-----------------|-------|
| Style LoRA | 0.7–1.0 | Higher values may override composition |
| Character LoRA | 0.8–1.0 | For tight identity lock |
| Lightning LoRA | Distilled 8-step | ~4× faster; slightly lower quality |

**API syntax (fal.ai):**
```json
{
  "loras": [
    { "path": "https://your-lora-host/character.safetensors", "scale": 0.9 },
    { "path": "https://your-lora-host/style.safetensors", "scale": 0.75 }
  ]
}
```

- Up to **3 LoRAs** simultaneously on fal.ai (merged at inference)
- Qwen-Image-2512 is the best open-source base for LoRA training — community confirms very high character consistency from trained LoRAs

### ComfyUI Node Chain with LoRA

```
GGUF Loader → CLIPLoader (Qwen2.5-VL) → VAE → LoRA Loader → KSampler
```

---

## Lightning LoRA (Speed Mode)

For rapid iteration on v1/2512:
- Forces 8-step generation
- ~4× faster than 40-step standard
- Quality slightly lower — acceptable for drafts, not for final production
- Recommended steps: 8
- CFG: ~1.2 (bundled in Lightning LoRA behavior)

---

## Next-Scene / Cinematic Transition

A specialized endpoint for shot progressions using LoRA-augmented Qwen Edit:

**Endpoint:** `fal-ai/qwen-image-edit-2509-lora-gallery/next-scene`

**Prompt convention:** Start with `"Next Scene:"` then describe camera/scene changes

**LoRA strength:** 0.7–0.8 recommended

**Supported transitions:**
- Dolly shots
- Push-ins and pull-backs
- Framing evolution (wide → medium → close)
- Lighting transitions (day → dusk → night)

**Example:**
```
Next Scene: The camera slowly pulls back from the close-up on her face to reveal
the full café interior behind her, warm afternoon light now visible through the
windows, ambient café chatter building in the audio bed.
```

---

## ControlNet Support (Edit-2509+ Models)

The Qwen-Image-Edit-2509 and later models support native ControlNet for structural guidance.

| Control Type | Capability | Use When |
|-------------|-----------|---------|
| **Depth maps** | Spatial structure control | Precise spatial arrangement |
| **Edge maps (Canny)** | Outline/linework guidance | Architectural accuracy, product shapes |
| **Pose keypoints** | OpenPose-style body control | Specific character poses |
| **Sketch guidance** | Convert rough sketch to polished render | Concept-to-image workflow |

**Task type for sketch guidance:** Set `task_type: "sketch_guidance"` in the edit API.

---

## Unified 2.0 Editing Workflow

Qwen-Image-2.0 consolidates generation and editing into a single model.

### For Generation
Use the standard text-to-image endpoint with the five-element framework.

### For Editing
Use the image-to-image / inpainting task modes with reference image positional labels.

### Edit Endpoint Best Practices

1. **Describe only what changes** — don't redescribe the entire image
2. **State explicitly what to preserve** — "Preserve the subject's face, clothing, and expression"
3. **Use positional labels** — `image 1`, `image 2` with a space
4. **Single change per pass** — multiple simultaneous edits produce less reliable results
5. **Restate invariants** — repeat the preserve list for stronger adherence

### Inpainting

Requires:
- Source image
- Mask image (white = areas to regenerate, black = areas to preserve)
- Prompt describing only what should appear in the masked region

```
task_type: "inpainting"
prompt: "A vintage red bicycle leaning against the brick wall"
[source image] + [mask covering the wall area where the bicycle should appear]
```

### Outpainting (Canvas Expansion)

Extends the canvas beyond the original image borders:

```
task_type: "outpainting"
prompt: "Continue the forest path to the left, same lighting, same time of day, same visual style"
[direction: expand left by 50%]
```

---

## Character Consistency Without LoRA (API Workflow)

For Qwen-Image-2.0 (no LoRA support on closed API):

1. **Generate anchor image** — detailed character description, face close-up preferred
2. **Lock the seed** from the best output
3. **Use as reference image** in subsequent I2I calls with `image 1` positional label
4. **Repeat character description explicitly** in each continuation prompt — do not rely on model memory
5. **State what stays the same:** "Preserve the face, hair, and clothing from image 1"

For series work, prepend a consistent character description block at the start of each prompt:

```
Character: [name], [age], [build], [hair], [eyes], [distinguishing features], [clothing]

Scene: [new scene description]
Preserve character appearance from image 1 exactly.
```
