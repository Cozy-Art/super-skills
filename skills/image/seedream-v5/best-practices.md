# Seedream 5.0 — Best Practices Guide

## The Natural Language Philosophy

**Seedream's core strength is understanding creative intent from coherent sentences.**

Unlike keyword-driven models, Seedream 5.0 Lite uses Chain of Thought reasoning to parse your prompt, reason about spatial relationships, and make informed creative decisions. This means natural language consistently outperforms keyword stacking — the model reads your sentence like a creative brief, not a tag list.

### ✅ Good (Natural Language):
```
A girl in a lavish dress walking under a parasol along a tree-lined path, 
in the style of a Monet oil painting
```

### ❌ Bad (Keyword Soup):
```
girl, umbrella, tree-lined street, oil painting texture, beautiful, 
masterpiece, 8K, ultra detailed
```

**The first prompt produces dramatically better results because the model understands the relationship between elements, not just their presence.**

---

## The Five-Part Formula

The most reliable prompt structure, validated across 1,000+ test generations:

```
Subject > Setting > Style > Lighting > Technical
```

### Component Breakdown

**1. Subject** — Main focus, materials, textures, actions
- "A handmade red ceramic coffee mug with slightly uneven glaze"
- "A woman in her 30s with cropped silver hair, wearing a tailored charcoal coat"

**2. Setting** — Environment, time of day, background
- "on a weathered oak farmhouse table, morning kitchen"
- "standing at the edge of a fog-shrouded pier at dawn"

**3. Style** — Photography/art style, film reference, director reference
- "Food photography, shot on Fujifilm X-T5"
- "Sergio Leone style, anamorphic widescreen"
- "in the style of a Monet oil painting"

**4. Lighting** — Direction, quality, color temperature
- "warm morning light streaming through frosted window on the left"
- "harsh overhead fluorescent mixed with neon spill from a bar sign"

**5. Technical** — Camera specs, lens, depth of field, film stock
- "56mm f/1.2 lens, shallow depth of field, Kodak Portra tones"
- "ARRI Alexa Mini, 35mm, deep focus, slight grain"

### Progressive Detail Control

Not every prompt needs all five parts. Start simple and add detail where it matters:

**Level 1 (Simple):** "A red ceramic coffee mug on a wooden table."
→ Model fills all creative decisions. Good for exploration.

**Level 2 (Context):** "A red ceramic coffee mug with steam rising, on a weathered oak table, warm morning light through a frosted window."
→ Scene gets a story. Model handles style and technical.

**Level 3 (Full Control):** "A handmade red ceramic coffee mug with slightly uneven glaze, thin wisp of steam catching the light, on a weathered oak farmhouse table. Food photography, shot on Fujifilm X-T5. Warm morning light streaming through frosted window on the left, creating long shadows. 56mm f/1.2 lens, shallow depth of field, Kodak Portra tones."
→ Every pixel is intentional. Maximum control.

---

## What to Emphasize

### Materials and Surfaces
Specific material descriptions produce dramatically better results than generic adjectives.

- ✅ "Anodized aluminum with brushed steel accent" → model renders actual brushed metal
- ❌ "Shiny metallic" → model guesses which metal, which finish

More examples:
- "Weathered leather with visible grain and patina"
- "Hand-blown glass with tiny trapped air bubbles"
- "Rough-hewn granite with lichen patches"
- "Matte white ceramic with a hairline craze pattern"

### Camera and Lens References
Seedream knows what real cameras and lenses produce visually.

- "ARRI Alexa LF" → cinematic color science, natural skin tones
- "85mm f/1.4" → portrait compression, creamy bokeh
- "Canon 100mm macro" → extreme close-up detail, razor-thin DOF
- "Hasselblad X2D" → medium format rendering, exceptional resolution
- "28mm wide angle" → environmental context, slight barrel distortion

### Film Stock References
Film stocks shift color grading and grain authentically.

- "Kodak Portra 800" → warm skin tones, fine grain, pastel highlights
- "Fujifilm Velvia" → saturated landscapes, vivid greens and blues
- "Pushed Tri-X 400" → high-contrast black and white, visible grain
- "Expired Kodak Ektachrome" → color shifts, unpredictable warmth
- "CineStill 800T" → tungsten-balanced, halation around highlights

### Director and Artist References
- "Sergio Leone style" → wide shots, tension, extreme close-ups
- "Kubrick symmetry" → one-point perspective, obsessive framing
- "Annie Leibovitz lighting" → dramatic portraiture, sculptural light
- "Ridley Scott color palette" → desaturated teal and amber
- "Wes Anderson composition" → centered framing, pastel palette

### Spatial Keywords
Precise positioning eliminates ambiguity in multi-subject scenes.

- "On the left side" / "in the upper right corner"
- "In the foreground" / "in the background"
- "Lower right third" / "center frame"
- "Behind the subject" / "partially obscured by"

---

## What to Avoid

### Quality Spam
Remove these — the model doesn't need quality boosters:
- ❌ "8K, masterpiece, ultra detailed, best quality, award winning"
- ✅ Describe the actual scene with specificity instead

### Vague Adjectives
These convey zero visual information:
- ❌ "Beautiful," "amazing," "stunning," "incredible," "gorgeous"
- ✅ Replace with specific visual descriptors: material, lighting quality, composition

### Contradictory Styles
The model can't resolve impossible combinations:
- ❌ "Photorealistic watercolor anime"
- ❌ "Minimalist maximalist design"
- ✅ Pick one style direction and commit

### Overly Long Unstructured Prompts
Past ~200 words without JSON structure, internal contradictions become likely:
- ❌ 300-word paragraph describing 8 subjects with competing priorities
- ✅ Use JSON structured prompt for complex multi-subject scenes
- ✅ Or simplify to the essential elements

---

## Common Mistakes and Fixes

| Mistake | Fix |
|---------|-----|
| "Two people at a cafe table" (vague spatial) | "On the left side of a round marble cafe table, a man in a rust shirt. On the right, a woman in cream sweater" |
| "8K, masterpiece, ultra detailed" (quality spam) | Remove entirely — describe the scene instead |
| Neon sign: `A neon sign saying OPEN 24 HOURS` | `A neon sign reading "OPEN 24 HOURS"` |
| "Make it better" (vague edit) | "Replace the hat with a crown, keeping the pose and expression unchanged" |
| `guidance_scale > 10` (4.5 only) | Keep between 7–9; >10 causes oversaturation in ~40% of generations |
| Five subjects in plain text prompt | Switch to JSON structured prompt with position fields |
| "Color should be brand blue" | Use HEX: "color #0066CC brand blue" |

---

## Tips for Consistency Across Generations

### 1. Lock Character Descriptions
Copy-paste the **exact same** character description word-for-word between related prompts. Change only the scene, angle, and action.

**Character anchor (reuse verbatim):**
```
A woman in her early 30s with cropped silver hair, sharp cheekbones, 
wearing a tailored charcoal wool coat with brass buttons
```

**Prompt A:** "[character anchor], walking through a rain-soaked Tokyo alleyway at dusk, neon reflections on wet pavement..."

**Prompt B:** "[character anchor], sitting at a worn wooden bar, warm amber light from pendant lamps overhead..."

### 2. Use Multi-Image Generation
Ask for "a series" or "a set" to get consistent style and character continuity across images in a single generation. The `max_images` parameter maintains coherence.

### 3. Maintain Style Anchors
Reuse the same style reference across related generations:
- "Cinematic photography, ARRI Alexa LF, Kodak Vision3 250D"
- Keep this identical across all shots in a sequence

### 4. Use Seed for Reproducibility
The output includes a seed value. Resubmit with the same seed and prompt for near-identical results. Essential for iterative refinement.

### 5. Example-Based Editing for Style Consistency (5.0 Only)
For complex style transfers (color grading, material changes, lighting shifts), provide a before/after pair showing the transformation, then apply to new images. More reliable than describing the style change in words.

---

## JSON Structured Prompts — When and How

### When to Use JSON Mode
- **Multi-subject scenes** with 3+ elements needing specific placement
- **Commercial art direction** with precise layout requirements
- **Brand work** requiring per-element HEX color control
- **Product flat lays** with defined spatial arrangement
- **UI mockups** and poster layouts with compositional precision

### When to Use Plain Text
- **Single-subject** scenes
- **Creatively open** prompts where model freedom is desired
- **Artistic/emotional** content where rigid positioning would harm the result
- **Simple scenes** that don't need positional control

### JSON Template

```json
{
  "scene": "Overall scene description and context",
  "subjects": [
    {
      "description": "Detailed description of subject 1",
      "position": "upper left",
      "color": "#FF006E"
    },
    {
      "description": "Detailed description of subject 2",
      "position": "center",
      "color": "#3A86FF"
    },
    {
      "description": "Detailed description of subject 3",
      "position": "lower right"
    }
  ],
  "style": "Photography or art style reference",
  "lighting": "Light direction, quality, color temperature",
  "camera": {
    "angle": "Camera angle description",
    "lens": "Focal length and aperture"
  }
}
```

### Position Values
- `"upper left"`, `"upper center"`, `"upper right"`
- `"center left"`, `"center"`, `"center right"`
- `"lower left"`, `"lower center"`, `"lower right"`
- `"foreground"`, `"midground"`, `"background"`
- `"left third"`, `"right third"`, `"lower right third"`

---

## Variant Selection Decision Tree

```
START: What does your shot need?
│
├─ Text rendering (posters, signs, branding)?
│  └─ → Seedream 5.0 Lite (superior typography)
│
├─ Multi-subject with precise placement?
│  └─ → Seedream 5.0 Lite + JSON mode
│
├─ Brand colors with HEX accuracy?
│  └─ → Seedream 5.0 Lite + HEX codes
│
├─ Need explicit negative prompts?
│  └─ → Seedream 4.5 (negative_prompt supported)
│
├─ Iterative refinement with guidance_scale?
│  └─ → Seedream 4.5 (1.0-12+ range)
│
├─ Example-based editing (material/style transfer)?
│  └─ → Seedream 5.0 Lite (before/after pairs)
│
├─ Visual marker editing (arrows, boxes on image)?
│  └─ → Seedream 4.5 (marker support)
│
├─ Simple single-subject scene?
│  ├─ Need max resolution? → 5.0 Lite (auto_2K default)
│  └─ Need fine parameter control? → 4.5 (scheduler, steps)
│
└─ Multi-image storyboard with consistency?
   └─ → Seedream 5.0 Lite (max_images + consistency)
```

---

## Migration Tips

### From Seedream 4.5 to 5.0 Lite

1. **Existing prompts generally improve without modification** — CoT reasoning understands intent better than instruction parsing
2. **Simplify keyword-heavy prompts** — Natural sentences outperform keyword stacking in 5.0
3. **Remove negative prompts** — Not supported in 5.0 Lite; describe desired end state more precisely instead
4. **Adopt JSON for complex scenes** — Replaces verbose spatial descriptions
5. **Use example-based editing** — For transformations that were hard to describe verbally (material swaps, color grading transfers)
6. **Trigger web search** — Include dates, product names, or trending terms for current references
7. **Resolution upgrade** — Default is now auto_2K (vs. 768×768 in 4.5); adjust downstream pipelines
8. **Guidance scale shift** — If using BytePlus API, default shifted from 7.0 (4.5) to 5.5 (5.0). Recommended range is now 3.0–7.0.

### From Other Models to Seedream

**From Midjourney:** Remove `--ar`, `--stylize`, `--chaos` parameters. Convert to natural language. Seedream doesn't use parameter flags.

**From Stable Diffusion / Flux:** Remove `steps:`, `cfg:`, `sampler:` parameters from prompt text. Seedream handles these internally (5.0) or via dedicated API parameters (4.5).

**From DALL-E:** Prompts generally transfer well since both prefer natural language. Add camera/lens references for photorealism boost.

---

## Advanced Techniques

### Multi-Language Scene Authenticity
Prompt in the native language of the scene for culturally authentic results:
- French prompt for Parisian bakery → authentic architecture, signage, lighting
- Japanese prompt for Tokyo street scene → accurate kanji, store layouts, atmosphere
- Arabic prompt for Moroccan market → authentic geometric patterns, color palette

### Film Stock as Color Grading
Instead of describing color grading, reference the film stock that produces it:
- Warm, desaturated nostalgia → "shot on expired Kodak Portra 400"
- High-contrast noir → "pushed Tri-X 400, 3200 ISO"
- Vivid saturated landscape → "Fujifilm Velvia 50"
- Tungsten-balanced urban night → "CineStill 800T with halation"

### Storyboard Grid Technique
For multi-panel storyboards, describe the grid layout explicitly:
```
A cinematic 2x2 storyboard grid. 
Panel 1: [description]. 
Panel 2: [description]. 
Panel 3: [description]. 
Panel 4: [description]. 
Consistent character design, [style reference].
```

### Progressive Refinement Workflow (4.5)
1. Generate with `guidance_scale: 7.0` and `steps: 30`
2. If too literal → lower guidance_scale to 5.0
3. If too loose → raise guidance_scale to 9.0
4. If artifacts → add specific items to negative prompt
5. Lock seed once composition is right → iterate on details

### Example-Based Editing Workflow (5.0)
1. Create or find a before/after pair showing your desired transformation
2. Upload as Image 1 (before) and Image 2 (after)
3. Upload your target image as Image 3
4. Prompt: "Reference the change from Image 1 to Image 2, apply the same operation to Image 3"
5. Supported transformations: material swaps, day→night, style transfers, color grading

---

## Troubleshooting

### Text Rendering Issues
**Problem:** Text appears garbled or doesn't render
- Verify double quotation marks around all literal text
- Keep text strings reasonable length (1-8 words per string work best)
- Specify font style in prompt: "bold condensed sans-serif," "elegant script"
- For multi-line text, describe the layout hierarchy explicitly

### Color Accuracy Issues
**Problem:** Colors don't match specification
- Use HEX codes: `color #FF006E hot pink` (always pair with descriptive name)
- For gradients, describe start and end colors with HEX: "gradient from #FF006E hot pink at the base to #3A86FF electric blue at the top"
- Verify HEX code is correct (common typo source)

### Composition Issues
**Problem:** Elements placed incorrectly in complex scenes
- Switch from plain text to JSON structured prompt
- Be explicit about position: "upper left," "lower right third"
- Reduce number of subjects if composition is still confused
- Add camera angle to JSON: `"angle": "directly overhead"` for flat lays

### Consistency Issues
**Problem:** Character appearance changes between shots
- Lock character description verbatim across prompts
- Use multi-image generation (max_images) for batch consistency
- Use same seed when possible
- Maintain identical style anchors (camera, film stock, lighting style)

### 4.5-Specific Issues
**Problem:** Oversaturation
- Lower guidance_scale to 5.0-7.0 range
- Check negative prompt for conflicting terms

**Problem:** Soft or blurry output
- Increase num_inference_steps to 40-50
- Try "DPM++ 2M Karras" scheduler
- Add sharpness-implying terms: "crisp detail," "sharp focus"

---

## Version Information

- **Guide Version:** 1.0
- **Covers:** Seedream 5.0 Lite, Seedream 4.5
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
