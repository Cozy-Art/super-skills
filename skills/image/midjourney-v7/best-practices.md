# Midjourney v7 - Best Practices Guide

> **⚠️ Output policy (2026-07-23, Skill v1.1):** Generated prompts are **pure descriptive prose with NO trailing `--` parameters** (no `--ar`, `--s`, `--q`, `--c`, `--sref`, `--oref`). The director controls aspect ratio and all Midjourney settings in their own environment. The parameter examples below are retained for reference/manual use only — do **not** reintroduce parameter appending into `SKILL.md`.

## Core Principle: Less is More

Midjourney v7's enhanced natural language understanding means **20-60 words is optimal**. Beyond 60 words, the model's attention to details drops significantly. Quality over quantity.

---

## The 20-60 Word Rule

### ✅ GOOD: 32 words
```
A weathered lighthouse keeper in his 60s stands at the edge of a rocky cliff 
at sunset, warm golden light, oil painting style, melancholic mood --ar 3:4 --s 250
```

### ❌ TOO LONG: 85 words
```
A very old and weathered lighthouse keeper who has spent his entire life at 
sea, approximately 60-65 years old with gray hair and a thick beard, wearing 
a traditional navy blue keeper's uniform with brass buttons, standing at the 
very edge of a dramatic rocky cliff with crashing waves below during a beautiful 
sunset with orange and pink clouds, painted in a classical oil painting style 
with visible brushstrokes, feeling melancholic and contemplative --ar 3:4 --s 250
```
**Problem:** Model will likely ignore or blend many details. Diminishing returns after 60 words.

---

## Essential Best Practices

### 1. Start with the Most Important Element

Word order matters. Midjourney gives more weight to concepts at the beginning.

**✅ Character Focus:**
```
A cyberpunk samurai in neon-lit Tokyo streets, rain-slicked pavement, moody lighting --ar 16:9
```

**✅ Environment Focus:**
```
A neon-lit Tokyo street at night with rain, cyberpunk aesthetic, samurai figure in distance --ar 16:9
```

### 2. Use Complete Sentences with Proper Grammar

V7 understands natural language. Write like you're describing to a person.

**✅ Natural:**
```
An ancient oak tree stands in a misty meadow at dawn, soft golden light filtering through branches
```

**❌ Keyword Soup:**
```
ancient oak tree, misty, meadow, dawn, golden light, soft, branches, atmospheric, beautiful
```

### 3. Be Specific About Visual Elements

Concrete descriptors > abstract concepts

**✅ Specific:**
```
A red brick Victorian house with white trim, bay windows, wrap-around porch --ar 4:3
```

**❌ Vague:**
```
A nice old house with character and charm --ar 4:3
```

### 4. Avoid Filler Keywords

V7 doesn't need quality descriptors—they're wasted tokens.

**DON'T USE:**
- "high resolution," "4K," "8K," "highly detailed"
- "photorealistic," "ultra realistic" (unless specifically needed for style)
- "beautiful," "stunning," "amazing," "incredible"
- "trending on artstation"
- "award-winning"

**These add no value and waste your limited word count.**

### 5. No Conversational Language

**❌ Don't:**
```
Please make me an image of a cat sitting on a windowsill, I want it to look cozy
```

**✅ Do:**
```
A tabby cat sitting on a sunlit windowsill, cozy interior, soft afternoon light --ar 3:4
```

---

## Parameter Strategy

### Stylize (`--s`) Guidelines

| Value | Effect | When to Use |
|-------|--------|-------------|
| `--s 0` | Completely literal | Technical diagrams, infographics |
| `--s 50` | Very subtle styling | Product photography, realistic portraits |
| `--s 100` | Default balance | General use, starting point |
| `--s 250` | Enhanced artistic | Concept art, illustrations |
| `--s 500` | Highly artistic | Fantasy art, stylized work |
| `--s 750` | Very stylized | Experimental, abstract |
| `--s 1000` | Maximum artistic | Wild interpretations, art experiments |

**Recommendation:** Start at `--s 100` (default), adjust by increments of 50-100.

### Chaos (`--c`) Guidelines

| Value | Effect | When to Use |
|-------|--------|-------------|
| `--c 0` | Very consistent | Final renders, need exact variations |
| `--c 10-20` | Slight variation | Exploring small differences |
| `--c 30-50` | Moderate variety | General exploration |
| `--c 60-80` | High diversity | Brainstorming, discovery |
| `--c 90-100` | Maximum chaos | Creative experiments, unexpected results |

**Note:** Chaos affects variety *between* the 4 generated images, not within each image.

### Quality (`--q`) Strategy

| Setting | Cost | When to Use |
|---------|------|-------------|
| `--q 1` | 1x | Standard work, most uses, default |
| `--q 2` | 2x | Important renders, more detail needed |
| `--q 4` | 4x | Final hero images, maximum fidelity |

**Workflow:** Draft → Q1 → Q2 for finals → Q4 only for absolute best shots

### Draft Mode (`--draft`) Strategy

**Use Draft Mode for:**
- ✅ Initial concept exploration
- ✅ Testing compositions quickly
- ✅ Comparing multiple ideas
- ✅ Budget-conscious iteration
- ✅ Generating reference thumbnails

**Don't Use Draft Mode for:**
- ❌ Final deliverables
- ❌ Text rendering (will be poor quality)
- ❌ Fine detail requirements
- ❌ High-resolution needs

**Workflow:**
```
1. Draft Mode (--draft): Generate 10-20 concepts quickly
2. Standard Mode: Refine top 3-5 concepts
3. Quality 2 (--q 2): Polish final selections
4. Quality 4 (--q 4): Ultimate hero images only
```

---

## Common Mistakes and Fixes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Prompts >60 words** | Details get ignored/blended | Trim to 20-60 words, prioritize |
| **Keyword lists** | Generic, unpredictable results | Write natural sentences |
| **"Make it detailed"** | Wastes tokens, adds no value | Remove filler, be specific instead |
| **Contradictions** | "Minimalist with lots of detail" | Choose one direction |
| **Abstract concepts** | "Make it emotional" hard to visualize | Use concrete visual descriptors |
| **Parameters mid-prompt** | Breaks prompt parsing | Always put parameters at END |
| **Spaces in parameters** | `-- ar` or `- - ar` | Use `--ar` (no spaces) |
| **Too many concepts** | Muddy, unfocused results | Focus on 2-3 main elements |

---

## Omni Reference (`--oref`) Best Practices

Omni Reference is V7's new feature for character/object consistency.

### When to Use
- Character consistency across multiple scenes
- Maintaining specific vehicle/object appearance
- Brand mascot or creature continuity

### How to Use
```
/imagine [your scene description] --oref [URL] --ow 100-400
```

### Omni Weight (`--ow`) Guidelines

| Value | Effect | When to Use |
|-------|--------|-------------|
| `--ow 100` | Subtle reference | Inspiration, not exact copy |
| `--ow 200` | Moderate adherence | Balanced character similarity |
| `--ow 300` | Strong adherence | High consistency needed |
| `--ow 400` | Maximum (recommended limit) | Exact character replication |

**IMPORTANT:** Keep `--ow` below 400. Higher values can cause artifacts.

### Example Workflow
```
# First image - establish character
/imagine A cyberpunk detective with silver hair and leather coat --ar 3:4

# Save URL of best result, then use in subsequent scenes:
/imagine The silver-haired detective examines evidence in a neon-lit alley --oref [URL] --ow 250 --ar 16:9

/imagine Same detective in pursuit on a rain-slicked street --oref [URL] --ow 250 --ar 16:9
```

---

## Style Reference (`--sref`) Best Practices

### Style Reference Codes
Midjourney has a library of style reference codes (e.g., `--sref 1234567890`).

```
/imagine A mountain landscape --sref 1234567890 --sw 200
```

### Style Reference Images
Use your own images for style control:

```
/imagine A portrait --sref [URL of style image] --sw 300
```

### Style Weight (`--sw`) Guidelines

| Value | Effect |
|-------|--------|
| `--sw 0` | No style influence |
| `--sw 100` | Default balance |
| `--sw 300` | Strong style influence |
| `--sw 500` | Very strong style |
| `--sw 1000` | Maximum style dominance |

### Style Version (`--sv`)

**New in V7:** Control which style reference behavior to use.

- `--sv 6` (default): V7 native behavior, use with new srefs
- `--sv 4`: Legacy behavior for old V4/V6 sref codes

**Example:**
```
# Old sref code from V6
/imagine A forest scene --sref 9876543210 --sv 4
```

---

## Multi-Prompt Syntax (Advanced)

Use `::` to control concept weights:

### Equal Weight
```
forest:: mountains
```
Both concepts weighted equally.

### Weighted Concepts
```
ancient temple::2 futuristic city
```
Temple has 2x the weight of city.

### Negative Weight
```
portrait:: busy background::-0.5
```
Reduces background emphasis.

### Complex Example
```
cyberpunk samurai::2 neon cityscape:: rain::-0.3 --ar 16:9 --s 300
```
- Samurai emphasized (2x)
- Cityscape normal weight
- Rain de-emphasized (-0.3)

---

## Aspect Ratio Strategy

| Ratio | Dimensions | Best For |
|-------|------------|----------|
| `--ar 1:1` | Square | Social posts, profile images |
| `--ar 3:4` | Portrait | Portraits, vertical art |
| `--ar 4:3` | Landscape | Photos, horizontal art |
| `--ar 16:9` | Widescreen | Cinematic, YouTube, web |
| `--ar 21:9` | Ultrawide | Epic cinematic shots |
| `--ar 2:3` | Tall | Magazine covers, posters |
| `--ar 9:16` | Vertical | Mobile, Instagram stories |

---

## Lighting Keywords That Work

Instead of vague "good lighting," be specific:

**Natural Light:**
- "golden hour sunlight"
- "overcast diffused light"
- "harsh midday sun"
- "soft dawn light"
- "blue hour twilight"

**Artificial Light:**
- "neon lighting"
- "studio key light"
- "candlelight"
- "street lamps"
- "spotlight dramatic"

**Quality:**
- "rim lighting"
- "backlighting"
- "side lighting"
- "soft diffused"
- "hard shadows"

---

## Style/Medium Keywords

Be specific about artistic style:

**Photography Styles:**
- "shot on 35mm film"
- "DSLR photograph"
- "vintage Polaroid"
- "professional studio photography"

**Art Styles:**
- "oil painting"
- "watercolor illustration"
- "digital art"
- "pencil sketch"
- "ink drawing"

**Specific Movements:**
- "art nouveau"
- "impressionist"
- "minimalist"
- "baroque"
- "surrealist"

---

## Camera Angle Keywords

**Position:**
- eye level
- low angle
- high angle
- bird's eye view
- worm's eye view

**Shot Types:**
- extreme close-up
- close-up
- medium shot
- full body shot
- wide shot
- establishing shot

**Depth:**
- shallow depth of field
- deep focus
- bokeh background
- selective focus

---

## Mood Keywords

**Emotional Tone:**
- serene, peaceful, calm
- dramatic, intense, powerful
- mysterious, enigmatic
- melancholic, nostalgic
- joyful, energetic, vibrant
- eerie, unsettling, haunting

---

## The `--no` Parameter

Exclude unwanted elements:

```
A beach scene --no people, buildings, boats --ar 16:9
```

**When to use:**
- Midjourney keeps adding unwanted elements
- Need to explicitly exclude common additions
- Want empty/minimal scenes

**Format:** `--no item1, item2, item3`

---

## Raw Mode (`--raw`)

Use `--raw` to reduce Midjourney's automatic artistic interpretation:

**Without --raw:**
```
A red ball
```
Result: Artistically rendered, stylized, beautified ball

**With --raw:**
```
A red ball --raw
```
Result: More literal, straightforward red ball

**When to use:**
- Technical illustrations
- Product photography
- When artistic interpretation is unwanted
- Need literal prompt interpretation

---

## Iteration Strategy

### Phase 1: Exploration (Draft Mode)
```
[base prompt] --draft --c 50
```
Generate many concepts quickly, explore variations.

### Phase 2: Refinement
```
[refined prompt based on winners] --s 200
```
Develop promising concepts at standard quality.

### Phase 3: Variations
```
[winning prompt] --c 20
```
Generate controlled variations of best concept.

### Phase 4: Final Polish
```
[final prompt] --q 2 --s 300
```
High quality render of approved concept.

### Phase 5: Hero Images (optional)
```
[hero prompt] --q 4 --s 350
```
Maximum quality for absolute best shots only.

---

## Troubleshooting

### Issue: Results Don't Match Prompt

**Solutions:**
1. Reduce prompt length (aim for 20-30 words)
2. Lower `--s` value for more literal results
3. Try `--raw` mode
4. Use `--no` to exclude unwanted elements
5. Increase specificity of key elements

### Issue: Inconsistent Results

**Solutions:**
1. Use `--seed` to lock in specific noise pattern
2. Reduce `--c` chaos value
3. Be more specific about composition
4. Use Omni Reference for character consistency

### Issue: Wrong Style

**Solutions:**
1. Be explicit about medium/style
2. Use `--sref` for style reference
3. Adjust `--s` stylize value
4. Add `--raw` if too artistic

### Issue: Poor Quality

**Solutions:**
1. Remove `--draft` if using it
2. Increase to `--q 2` or `--q 4`
3. Upscale the image
4. Be more specific about details

---

## Quick Reference Template

```
[Subject] + [Action/State] + [Environment] + [Lighting] + [Style] + [Mood] + [Parameters]

Example:
A steampunk airship captain at the helm, brass and leather details, storm clouds 
gathering, dramatic side lighting, digital art style, adventurous mood --ar 16:9 --s 300 --q 2
```

---

**Remember:** Midjourney v7's strength is understanding natural language. Write clear, concise descriptions in 20-60 words, and let the model's intelligence handle the interpretation.
