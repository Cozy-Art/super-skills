# Stable Diffusion 3.5 — Best Practices Guide

---

## Scene Description Ordering

The T5-XXL encoder parses sentence structure, and CLIP gives more weight to early tokens. Both reward logical spatial ordering.

**Move through the scene spatially:**
1. Art style/medium (front-loaded for strongest influence)
2. Primary subject + what they're doing
3. Immediate environment (what's near the subject)
4. Mid-ground and background
5. Lighting and atmosphere
6. Camera/composition language
7. Negative prompt (minimal)

**Official Stability AI example of correct ordering:**
```
A woman stands at the edge of a stormy ocean cliff, beneath a cherry blossom tree.
The tree drops countless pink petals into the sea below.
The petals float on the waves and sink into the sea.
In the background, dark gray clouds gather.
Oil painting, Expressionism.
```
The movement: woman → tree → petals falling → petals on water → background → style.

---

## Style Goes First

Placing art style/medium at the **beginning** produces stronger stylistic influence than appending at the end.

✅ **Correct (style first):**
```
Art Nouveau drawing of a beautiful redhead sitting at an outdoor bar
```

⚠️ **Weaker (style buried at end):**
```
A beautiful redhead sitting at an outdoor bar. In the Vienna Secession style, an Art Nouveau drawing.
```

This affects the CLIP encoders more than T5 — the 77-token window means early style tokens receive the full CLIP attention pass.

---

## What to Emphasize

### Specific Materials and Textures
Name observable, renderable surfaces:
- "Glazed ceramic," "brushed steel," "rough linen," "polished ebony"
- "Charcoal and colored pencils on light sepia drawing paper"
- "Ink wash on rice paper with visible paper texture"
- Fabric: "heavy wool tweed," "worn leather," "silk charmeuse"

### Lighting Descriptions
Direction, quality, and source all have measurable effect:
- Direction: "backlight," "side-lit from camera right," "overhead"
- Quality: "hard rim light," "soft diffused window light," "dappled"
- Source: "candlelight," "golden sunrise backlight," "neon wash"
- Contrast: "dynamic shadows," "deep chiaroscuro," "flat even light"

### Camera and Cinematic Language
SD3.5 responds reliably to cinematography terms:
- Shot type: "close-up," "extreme close-up," "wide-angle shot," "medium shot"
- Angle: "bird's eye view," "worm's eye view," "Dutch angle," "eye level"
- Lens: "fish-eye lens," "telephoto compression," "35mm feel"
- Movement implied: "crane shot," "handheld energy," "static composition"

### Mood and Atmosphere
These work when paired with specific visual anchors:
- "Ominous, haunting, and bleak"
- "Atmospheric and intimate"
- "Serene and otherworldly"
- "Tense, claustrophobic, suffocating"

Pair mood language with concrete visual details — "ominous" alone is weak; "ominous, dark clouds banking on the horizon, single pale light from a distant window" is actionable.

### Art Medium Over Artist Names

Artist names work **unpredictably** in SD3.5 — some influence style, others are ignored. Describe the visual look instead:

| Instead of (artist name) | Use (visual description) |
|--------------------------|--------------------------|
| "in the style of Ivan Bilibin" | "painted in ink wash and watercolor with fine line work and ornate border patterns" |
| "like Alphonse Mucha" | "Art Nouveau illustration, sinuous flowing lines, decorative floral border, jewel-toned palette" |
| "Caravaggio-style" | "dramatic chiaroscuro, single harsh light source from upper left, figures emerging from deep shadow" |
| "Ukiyo-e style" | "Japanese woodblock print, flat color planes, bold outline, limited palette, decorative wave patterns" |

---

## What to Avoid

### Prompt Weighting Syntax (Silently Ignored)

`(keyword:1.2)`, `[keyword]`, `((keyword))` — all silently ignored in SD3.5.

**Replace with:**
1. Move the element earlier in the prompt (positional emphasis)
2. Add more descriptive detail to the element
3. Repeat key attributes as natural language: "very detailed," "prominently featured," "dominant"

### Excessive Negative Prompts

The SDXL standard negative prompt actively hurts SD3.5 in many cases.

❌ **SDXL-style negative (often counterproductive in SD3.5):**
```
deformed, disfigured, ugly, blurry, worst quality, low quality, bad quality, mutation, extra limbs, watermark
```

✅ **SD3.5 approach:**
- Start with **no negative prompt**
- Generate and evaluate
- Add only the specific terms that address actual issues in the output
- Keep negative prompts to 5 words or fewer when used

**Minimal effective negatives (add only if needed):**
- For illustration: `deformed, ugly, photo, photorealism`
- For portraits: `deformed, ugly, blurry`
- For product shots: `text, watermark, logo`

### Quality Booster Keywords

"8K, masterpiece, ultra-detailed, photorealistic, best quality" — these add little to no value in SD3.5. The model doesn't respond to them the way SDXL does. Describe the actual visual instead.

### Conflicting Style Instructions

Some artistic styles conflict with subject matter because training data combinations are sparse:
- Comic book style + coral reef (few comic book coral reef images in training data)
- Watercolor + metallic surfaces (conflicting material expectations)
- Photo realism + cartoonish objects (mutually exclusive rendering modes)

Resolve contradictions before prompting.

### Long Prompts Without Spatial Logic

Piling up attributes without spatial organization ("woman, flower, cliff, storm, petals, ocean, sky, dark, beautiful, sad, expressive") forces the model to guess relationships. Use natural language sentences to establish spatial and narrative relationships.

---

## Common Mistakes and Fixes

| Mistake | Fix |
|---------|-----|
| Long SDXL negative prompt ("deformed, disfigured, ugly, blurry...") | Remove entirely or reduce to 1–3 specific terms |
| Style instruction at end of complex prompt | Move style to the **beginning** |
| Prompt weighting: `(fleur d'lis:1.4)` | Remove weighting; add descriptive detail instead |
| Relying on artist names for style | Replace with visual description of medium and technique |
| Too many inference steps (50+) | Use 20–25 for Large; exactly **4** for Turbo |
| CFG too high (>7) for SD3.5 | Start at **4.4**; values above 7 cause artifacts |
| Detailed/complex prompts on Turbo | Simplify — Turbo performs better with short prompts |
| Comma-separated keywords for spatial scenes | Write natural language sentences with spatial logic |
| Skipping seed documentation | Note every seed that produces good results — seeds are your consistency tool |
| No negative prompt producing specific unwanted elements | Add minimal specific terms: "no text" not "no text, no watermark, no logo, no writing, no letters" |

---

## Consistency Strategies

### The "Prune It Out" Rule

If an element in the prompt doesn't seem to affect the output, remove it. Excess text dilutes the signal of important elements. A focused 40-word prompt often outperforms a sprawling 120-word one.

**After each generation, ask:** "Which words in this prompt are actually affecting the output?" Remove ones that aren't.

### Seed Locking

Lock the seed after finding a good result. Then change **one element at a time** to see exactly what each change does.

Workflow:
1. Generate 3–5 images with random seeds
2. Pick the best result — copy the seed
3. Lock that seed in all subsequent runs
4. Make a single prompt change, re-generate
5. Evaluate what changed — keep or revert
6. Document seed + final prompt as your "recipe"

### Style Anchor Consistency

Reuse the exact same style description across related generations. Even minor phrasing changes shift the style output.

**Save style strings verbatim:**
```
Art Nouveau drawing in a Vienna Secession style
```
Copy-paste this exact string into every related prompt. Do not paraphrase.

### CFG and Step Consistency

Changing CFG or step count between generations introduces variation that can mask prompt changes. Use the same CFG and step count throughout a series.

---

## Prompt Length Strategy

| Prompt length | Model fit | Notes |
|--------------|-----------|-------|
| 5–15 words | **Turbo** | Turbo performs better with short prompts |
| 30–80 words | Large / Medium | Optimal — fits within 77-token CLIP window |
| 80–200 words | Large / Medium for complex scenes | Use spatial natural language ordering; critical info in first 77 tokens |
| 200+ words | Large only | T5-XXL handles it, but CLIP weight drops off significantly |

---

## Art Style Compatibility Notes

Some combinations work poorly because SD3.5's training data contains few examples:

| Style | Works well with | Potential conflicts |
|-------|----------------|---------------------|
| Oil painting / Expressionism | Portraits, landscapes, dramatic scenes | Highly technical/scientific diagrams |
| Manga / anime | Characters, action, fantasy | Photorealistic environments |
| Art Nouveau | Botanical, decorative, portrait | Industrial, gritty, dystopian |
| Comic book / graphic novel | Characters, urban scenes | Underwater, microscopic |
| Watercolor | Landscapes, soft portraits, botanical | Metallic objects, sharp industrial |
| Charcoal sketch | Portraits, architecture | Bright colorful scenes |
| Low-poly 3D | Abstract, geometric, isometric | Realistic skin, organic textures |

When targeting a specific combination, test first — some uncommon pairings produce surprising results; others fail consistently.
