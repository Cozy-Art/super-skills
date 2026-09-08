# Luma Uni-1.1 — Best Practices Guide

---

## The Architecture Shapes the Prompt

Uni-1.1 is a decoder-only autoregressive transformer. Unlike diffusion models that reduce noise iteratively, it **reasons before it generates** — decomposing the prompt, resolving visual constraints, and planning composition before producing any output tokens.

Practical implications:
- Natural-language, intent-driven prompts outperform keyword lists
- The model can handle multi-constraint prompts where diffusion models partially execute or blend them
- Specificity is rewarded — vague adjectives consume reasoning cycles without producing visual decisions
- Conflicting instructions confuse the reasoning pass — resolve them before submitting

---

## Prompt Length and Depth

Uni-1.1's reasoning architecture benefits from **natural-language specificity, not brevity**. More detail gives the reasoning pass more to work with.

| Weak | Strong |
|------|--------|
| `"cat in forest"` | `"A tabby cat sitting on a mossy log in an ancient forest at golden hour, soft dappled light filtering through oak leaves, painterly impressionist style, warm amber tones, peaceful and serene mood"` |
| `"beautiful cityscape"` | `"Rainy Tokyo street at 2am, neon reflections on wet asphalt, a single figure with an umbrella, cinematic anamorphic lens, 1970s Japanese cinema color grading"` |

**Target lengths:**
- Simple T2I: 80–150 words
- Reference-guided: 100–300 words
- Modify/edit: 30–100 words (surgical, not verbose)
- Multi-panel/storyboard: 150–300 words

---

## What to Emphasize

### Named Aesthetics (High Value)
Named aesthetics with visual specificity outperform generic style words:

✅ `"1970s Italian giallo film poster, high-contrast color blocking, typography-forward composition"`  
❌ `"stylized, artistic, edgy"`

Strong named aesthetic patterns:
- Era + medium: "1940s film noir, double-exposure photography"
- Cultural visual tradition: "ukiyo-e woodblock print, flat color planes, bold outline"
- Named movement: "German Expressionist cinema, harsh angular shadows"
- Platform-specific: "manga panel composition, screentone shading, dynamic action lines"

### Camera and Lens Language
Communicates composition precisely without over-describing:
- Focal length: "85mm lens, shallow depth of field"
- Movement: "slow-motion tracking shot feel, motion blur on periphery"
- Format: "anamorphic lens flare, cinematic widescreen"
- Perspective: "worm's eye view," "bird's-eye overhead," "Dutch angle"

### Cultural Visual Traditions
Uni-1.1 has deep knowledge of visual cultural traditions:
- Manga panels, screentone shading, ink outlines
- Ukiyo-e woodblock prints, flat planes, limited palette
- Film noir: hard shadows, venetian blind patterns, low-key lighting
- Arthouse cinema: wide frames, sparse staging, natural light
- Expressionism: distorted perspective, high contrast, psychological weight

### Text Rendering
For signs, labels, surfaces:
- Enclose exact text in quotes: `reading "OPEN 24 HRS"`
- Specify the medium: "neon sign," "painted wall lettering," "embossed metal"
- Specify environment: "rain-reflective surface at night"

### Lighting Specifics
All four dimensions have measurable effect:
- **Direction:** side-lit, backlit, overhead, rim light from camera-right
- **Quality:** soft diffused, harsh directional, dappled through canopy
- **Temperature:** warm amber, cool blue, neutral daylight, sodium vapor orange
- **Time of day:** golden hour, blue hour, midday overhead, 2am neon-lit

---

## What to Avoid

| Avoid | Why | Replace with |
|-------|-----|-------------|
| "beautiful," "amazing," "high quality," "masterpiece" | Unpredictable; often counterproductive — vague instructions create vague reasoning cycles | Specific visual description: "cinematic lighting," "realistic skin texture" |
| Negative prompting (`"no people"`, `"avoid blur"`) | Creates internal conflicts in the reasoning pass; Luma's official guidance explicitly warns against it | Convert to positive: "empty room," "sharp focus, deep depth of field" |
| Redundant phrasing ("beautiful, gorgeous, stunning, lovely") | Repeating the same concept dilutes rather than reinforces — the reasoning pass treats them as one weak signal | Say it once, specifically |
| Conflicting instructions ("photorealistic oil painting") | Model partially executes both, producing incoherent results | Resolve before submitting — pick one |
| Unlabeled references in Create mode | Model guesses reference role; guesses are unreliable | Always declare role: `"Use IMAGE1 as a STYLE reference"` |
| Lengthy Modify prompts | In `image_edit`, verbose prompts can cause structure drift | Keep Modify prompts surgical: 30–100 words |

---

## Positive Prompting: The Full Conversion Discipline

Luma's official guidance: **positive-only prompting produces the best results.** The model was trained and optimized for intent-driven positive language.

### Conversion Table

| Negative intent | Positive expression |
|-----------------|---------------------|
| "a room, do not add people" | "an empty, minimalist room with natural light" |
| "a landscape, no cars" | "a pristine, untouched natural landscape with dense forest and tranquil lake" |
| "don't make it blurry or ugly" | "a high-resolution, professional photograph with cinematic lighting" |
| "futuristic city, not too busy" | "a serene futuristic city with empty streets and glowing buildings at night" |
| "portrait, no distracting background" | "portrait against a clean, neutral-toned studio background, softly blurred" |
| "product on white, no shadows" | "product on pure white seamless background, shadowless studio lighting" |
| "no text in the image" | "a purely visual composition with no typography or signage" |

### Conversion Method

For any "don't" or "no" instruction:
1. Ask: what should the space contain instead?
2. Describe that positive state explicitly
3. Add specificity to prevent the model from filling the void with its defaults

---

## Seed Strategy

Luma's official "explore → lock → iterate" workflow:

1. **Explore** — leave `seed` unset, generate variations to find a direction
2. **Find a strong result** — note the seed from the UI or API response
3. **Lock the seed** — same seed + same prompt = same result
4. **Change one variable at a time** — adjust prompt OR parameters, not both
5. **Save prompt + seed together** — this is your reusable recipe

> Same seed + changed prompt = **controlled variation**, not the same image

This is identical in principle to other models but particularly important for Uni-1.1 because of multi-reference workflows — you want to isolate what each change contributes.

---

## Web Search Grounding

Enable `web_search: true` for prompts referencing real-world subjects where visual accuracy matters:

**Use for:**
- Specific real-world locations (Shibuya crossing, the Louvre, Machu Picchu)
- Brands and products with specific visual identities
- Cultural events with specific visual contexts
- Historical settings requiring factual accuracy

**Do not use for:**
- Purely fictional or imaginary content
- Speed-critical pipelines (adds minor latency)
- Abstract or atmospheric prompts with no factual anchor

The model searches the web before generating to improve visual accuracy. The cost delta is minimal compared to quality gain on factual subjects.

---

## Multi-Constraint Discipline

Uni-1.1's primary strength is handling multiple simultaneous constraints. To use this effectively:

1. **State all constraints explicitly** — the reasoning pass processes them together
2. **Separate spatial, stylistic, and referential constraints** — each in its own sentence or phrase
3. **Assign reference roles precisely** — prevents one reference dominating others
4. **Don't repeat the same constraint** — one clear statement is stronger than three restatements
5. **Resolve contradictions before submitting** — the model won't resolve them for you

**Example of well-structured multi-constraint prompt:**
```
A young woman (CHARACTER: IMAGE1) stands on a rain-slicked Tokyo street at 2am.
Camera: wide-angle anamorphic, slight upward tilt.
Lighting: sodium vapor street lamps creating warm orange pools against deep blue shadows.
Style: 1970s Japanese cinema color grading, slightly desaturated with warm highlight roll-off.
Composition: (COMPOSITION: IMAGE2) — rule of thirds, figure on left third.
```

Each constraint is in its own clause. Nothing conflicts. References are labeled.

---

## Create → Modify Workflow Chain

One of the most powerful production workflows:

1. Use `type: "image"` (Create) to explore compositions freely
2. Pick the best result
3. Use that image as `source` with `type: "image_edit"` (Modify)
4. Write targeted Modify prompts to refine specific elements while the model preserves overall structure

**Why this works:** Create mode lets you explore broadly without constraint. Modify mode lets you refine surgically. Trying to do both in one generation often compromises both.

**Example chain:**

Create prompt:
```
A quiet French village square at dusk, cobblestones, central fountain, warm café lights,
impressionist style, golden-hour atmosphere, 16:9.
```

Modify prompt (after selecting best result):
```
Change the time of day to early morning mist. Update sky, light direction,
and color temperature to cool blue-grey. Keep all architecture, fountain,
and cobblestone composition unchanged.
```
