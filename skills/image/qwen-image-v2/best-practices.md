# Qwen Image — Best Practices Guide

---

## Front-Loading: The Most Important Rule

Qwen Image uses a **language model text encoder (Qwen2.5-VL)**. Earlier tokens receive more weight — this is not a diffusion model with keyword attention. The primary subject and action must come first.

| ❌ Weak (buried subject) | ✅ Strong (front-loaded) |
|--------------------------|------------------------|
| "A nice landscape photo featuring somewhere a red sports car" | "Red sports car on mountain road, aerial drone shot, golden hour lighting, cinematic wide angle" |
| "Beautiful image, high quality, detailed" | "A hyper-realistic close-up of a Golden Retriever outdoors in soft daylight. Every strand of fur is distinct." |
| "In a quiet forest, there is a woman standing" | "A woman standing in a quiet forest, morning mist, soft diffused light, editorial photography" |

**Rule:** The first 5–10 words define what the model renders. Everything after refines it.

---

## What to Emphasize

### Specific Visual Attributes
Name observable, renderable details — not abstract qualities:

- **Material:** "brushed aluminum," "matte black ceramic," "worn canvas," "polished oak"
- **Texture:** "every strand of fur is distinct," "visible skin pores," "papery garlic skins"
- **Hair:** "natural curly hair," "tightly coiled," "straight black hair with front bangs" — Qwen-Image-2.0 renders individual strands natively
- **Fabric:** "linen," "ribbed knit," "heavyweight denim," "satin"

### Camera and Composition Language
Qwen Image responds well to standard photography/cinematography terms:

- Shot type: "close-up portrait," "wide establishing shot," "aerial drone shot," "macro"
- Angle: "low angle," "overhead," "eye level," "bird's eye," "worm's eye"
- Lens feel: "35mm lens shallow depth of field," "rule of thirds composition," "telephoto compression"
- Framing: "full body visible," "waist-up," "tight face crop"

### Style Anchors — One Per Prompt
Pick **one** clear style direction and commit to it. Conflicting styles produce muddled outputs.

✅ **Single clear style:**
- "editorial photography style"
- "watercolor illustration"
- "low-poly 3D render"
- "Studio Ghibli-inspired cel-shading"
- "vintage grain film photograph"

❌ **Contradictory style:**
- "photorealistic oil painting" (mutually exclusive)
- "minimalist maximalist" (self-defeating)
- "4K photorealistic watercolor illustration" (medium conflict)

### Lighting and Atmosphere
- Direction: "soft window light from camera-left," "rim light from behind," "overhead fluorescent"
- Quality: "soft diffused," "harsh directional," "dappled through canopy," "overcast flat light"
- Temperature: "warm golden hour," "cool blue hour," "neutral daylight"
- Mood: "golden hour warmth," "neon-lit rain-slicked street," "cool overcast diffuse light"

### In-Image Text
See the dedicated text rendering section below.

---

## Anti-Patterns Table

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| `"photorealistic, 8K, ultra HD, masterpiece"` | Quality boosters are meaningless to the LLM encoder; can distract | Describe the actual visual: "soft focus bokeh background, studio lighting, realistic skin texture" |
| `(keyword:1.3)` weight syntax | Not parsed; may produce artifacts | Use natural language emphasis: "very detailed fur, exquisitely rendered" |
| Booru/Danbooru comma tag lists | LM text encoder expects sentences, not tag syntax | Write full prose sentences |
| Conflicting style anchors ("photorealistic oil painting") | Model averages contradictions | Pick one style |
| Vague scale words ("beautiful," "amazing," "stunning") | Non-specific; model cannot render a feeling | Replace with visual specifics |
| `acceleration: "high"` for text images | Degrades text legibility | Use `none` or `regular` for any image with readable text |
| `enable_prompt_expansion: true` during testing | Auto-rewrites your prompt; results non-reproducible | Set to `false` when iterating exact phrasing |
| CFG above 5 (local/v1) | Contrast artifacts appear | Keep guidance_scale at 2.5–5 |
| JPEG output for text-heavy designs | Compression artifacts damage text edges | Always use PNG for text designs |
| Burying the subject mid-prompt | LM encoder underweights it | Move subject and action to the very first sentence |

---

## Text Rendering Workflow (Qwen's Core Differentiator)

Qwen Image outperforms GPT Image, Gemini, and FLUX on multilingual text rendering — but requires correct syntax.

### Step-by-Step

1. **Quote exact strings:** `The sign reads "GRAND OPENING" in bold red letters`
2. **Describe font style:** serif / sans-serif / condensed / italic / script
3. **Specify color explicitly:** "cream white," "deep navy," "gold," "black"
4. **Give spatial context:** "top-center," "bottom third," "centered below the illustration," "lower-left corner"
5. **State relative size:** "large," "small," "same size as the headline"
6. **Use `output_format: "png"`** — lossless, preserves sharp letter edges
7. **Avoid `acceleration: "high"`** — degrades text legibility on v1/2512
8. **Chinese text:** Write characters directly in the prompt (e.g., `中文文字`), not romanized — the model's Chinese knowledge activates best with native characters

### Multi-Text Element Layout (2.0 Only)

With Qwen-Image-2.0's 1,000-token budget, describe element by element:

```
Title: "ALTITUDE FESTIVAL" — large, bold condensed sans-serif, white, all caps, top third
Subtitle: "June 20–22 | Telluride, Colorado" — smaller weight, gold, directly below title
Footer: "altitudefestival.com" — minimal small caps, white, bottom
```

### Text Troubleshooting

| Problem | Fix |
|---------|-----|
| Text garbled or wrong characters | Quote the exact string; avoid `acceleration: "high"` |
| Chinese characters incorrect | Write Chinese directly in prompt, not transliterated |
| Text too small to read | Specify size: "large," "prominent," "filling the top third" |
| Extra unwanted text appearing | Add to negative prompt: "no text artifacts, no duplicate text, no watermark" |
| Text at wrong position | Be more explicit: "top-center," "lower-right corner," "centered in the bottom 20% of the frame" |

---

## Negative Prompt Strategy

**Write NLP sentences, not keyword dumps.** The Qwen2.5-VL text encoder processes negatives the same way it processes positives — as language, not as a token blacklist.

✅ **Good (NLP style):**
```
No watermarks, no distorted faces, no blurry backgrounds, avoid artificial plastic skin texture
```

❌ **Bad (keyword dump):**
```
blurry, bad anatomy, ugly, deformed, watermark, low quality, extra limbs
```

### All-Purpose Negative Prompt
```
No distortion, no watermarks, no text artifacts, no duplicate subjects, no overexposed highlights
```

### For Portraits (Add)
```
No artificial skin smoothing, no plastic texture, no heavy retouching
```

### For Text Designs (Add)
```
No text artifacts, no duplicate text, no blurry letters, no misaligned characters
```

### For Product Photography (Add)
```
No background objects, no unwanted reflections, no studio equipment visible
```

### 2.0 API Constraint
Negative prompt is capped at **500 characters** on Qwen-Image-2.0. Keep it concise.

---

## Composition Techniques by Content Type

### Photorealistic Portrait
- Front-load: specific ethnicity/age/hair/clothing at the start
- Name the light source explicitly: "soft north window light," "golden hour side light"
- Specify gaze: "direct gaze at camera," "looking slightly off-frame right"
- Name skin texture cue: "realistic skin texture, visible pores" (2.0 renders this by default)
- Avoid: "beautiful face," "perfect skin" — describe observable properties instead

### Landscape / Environment
- Front-load: primary landscape feature first ("Turquoise river winds through a lush canyon")
- Describe motion: "wind sweeps through tall grass," "waterfalls cascade"
- Include negative composition: "No people, no text, no artificial objects" — works as part of positive prompt
- Specify light quality and time of day: "noon sunlight filtering through canopy," "dappled spots on river surface"

### Poster / Event Design
- Use the element-by-element layout approach (2.0 only for complex layouts)
- State background before foreground elements
- Quote all text strings
- End with: "Balanced whitespace. Print-ready layout." — activates design finishing behavior

### Product Photography
- Name the material precisely: "matte black ceramic," "brushed stainless"
- Specify surface: "white marble with faint veining," "oak wood grain"
- Name lighting exactly: "soft diffused studio lighting from the left"
- Use negative composition inline: "No background objects, no shadows except ground shadow directly beneath"
- Include "The use case" signal: "professional product catalog aesthetic," "e-commerce product shot"

### Infographic / Slide (2.0 Only)
- Describe the background first: "White background."
- Title and hierarchy: "Title at top: [text] in [font style and color]"
- Columns/sections: "Three columns below the title, each with a labeled icon:"
- Per-element descriptions: "Left: [icon], label [text]; Center: [icon], label [text]"
- Caption / footer last
- End with style signal: "Clean tech brand style, consistent icon line weight, ample padding"

### Character Scene / Illustration
- State style anchor early: "Studio Ghibli-inspired illustration style"
- Describe character clothing and expression specifically
- Include atmospheric language: "Soft overcast light, muted earth tones"
- End with mood: "Painterly texture, warm sepia shadows, high emotional atmosphere"

### Multi-Character Composite
- Describe each character separately with full detail
- Name their position: "Woman on the left... Woman on the right..."
- Describe interaction: "turned slightly toward each other," "holding mugs"
- Specify shared lighting and setting: "Natural midday daylight through large windows"

---

## Consistency Across Generations

- **Lock `seed`:** Same seed + same prompt + same version = identical output
- **Change one variable at a time:** Isolate what changed between generations
- **Save exact prompt strings:** The LM encoder is sensitive to word order — document what worked
- **Disable `enable_prompt_expansion`** when comparing prompt versions (2.0 only)
- **Blurry/washed out output (local):** Raise `shift` to 12–13 — resolves most local deployment issues
