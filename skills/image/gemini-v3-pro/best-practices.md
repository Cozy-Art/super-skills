# Gemini 3 Pro Image - Best Practices Guide

> **⚠️ Output policy (2026-07-23, Skill v1.1):** Never write aspect ratio, resolution, or "2K/4K" into the prompt **prose**. Those are output settings the user controls — they belong only in the separate "Configuration notes" section, never inside the descriptive sentences. Any `N:N … orientation/aspect ratio` phrasing shown in the examples below is legacy and should **not** be copied into new prompt prose.

## Core Principles

### 1. Write Descriptive Sentences, Not Keyword Lists

**❌ WRONG: Keyword Approach**
```
coffee shop, wooden, warm, cozy, vintage, Edison bulbs, morning light
```

**✅ RIGHT: Sentence Approach**
```
A cozy vintage coffee shop with exposed wooden beams and warm Edison bulb lighting. 
Morning sunlight streams through large windows, creating soft shadows across weathered 
hardwood floors.
```

**Why:** Gemini's language model architecture interprets natural language far better than comma-separated keywords. Full sentences provide context, relationships, and hierarchy that keywords cannot.

---

## 2. The Six Essential Elements

Every strong prompt should include:

| Element | Purpose | Example |
|---------|---------|---------|
| **Subject** | Who/what with unique identifiers | "A confident businesswoman in her 40s with silver-streaked black hair" |
| **Action** | What subject is doing | "presenting to a boardroom, gesturing toward an unseen screen" |
| **Location** | Specific environment with atmosphere | "modern glass-walled office with city skyline visible through windows" |
| **Composition** | Shot type, camera, lens | "medium shot, 35mm lens, shallow depth of field" |
| **Lighting** | Quality, direction, color temperature | "soft diffused daylight mixed with warm interior lighting" |
| **Style** | Aesthetic, medium, mood | "photorealistic, professional and inspiring mood, 16:9 landscape" |

### Complete Example Applying All Six:
```
Create a photorealistic medium shot of a confident businesswoman in her 40s with 
silver-streaked black hair and warm brown eyes. She is presenting to a boardroom, 
gesturing toward an unseen screen. Set in a modern glass-walled office with city 
skyline visible through windows. Illuminated by soft diffused daylight mixed with 
warm interior lighting. Shot with 35mm lens, shallow depth of field. 16:9 landscape 
orientation. The mood is professional and inspiring.
```

---

## 3. Start with Action Verbs

Begin prompts with clear directives:

- **Create** - General image generation
- **Generate** - Systematic/technical imagery
- **Illustrate** - Conceptual or editorial
- **Transform** - Image-to-image modifications
- **Draw** - Artistic/stylized renders

**Example:**
```
Illustrate a cyberpunk street market at night with neon signs reflecting on wet pavement...
```

---

## 4. Be Specific with Descriptors (6+ Words Per Key Element)

**❌ VAGUE:**
```
A woman in a room
```

**✅ SPECIFIC:**
```
A young woman with curly red hair, freckles, and green eyes wearing a vintage 
denim jacket, sitting in a sunlit reading nook
```

**Rule of Thumb:** If an element is important to the composition, use at least 6 descriptive words for it.

---

## 5. Build Complexity Gradually (1-3 Changes Per Iteration)

When refining generations, make incremental changes rather than complete rewrites.

**First Generation:**
```
A cozy coffee shop interior with warm lighting
```

**Second Iteration (Add 2-3 details):**
```
A cozy coffee shop interior with warm Edison bulb lighting and exposed brick walls
```

**Third Iteration (Refine further):**
```
A cozy coffee shop interior with warm Edison bulb lighting, exposed brick walls, 
and vintage leather armchairs near a fireplace
```

**Why:** This helps you identify which changes improve results and maintains consistency across iterations.

---

## Common Mistakes and Fixes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Keyword lists** | Generic, random results | Write full descriptive sentences |
| **Too many changes at once** | Inconsistent outputs, can't identify what worked | Make 1-3 step-by-step edits per iteration |
| **Vague subject descriptions** | AI interpretation varies wildly | Add 6+ specific characteristics |
| **No style specification** | Default aesthetic applied arbitrarily | Specify art style, photography type, mood |
| **Static prompts without verbs** | Lifeless, posed compositions | Include actions and implied movement |
| **Negative phrasing ("no cars")** | Often ignored by model | Describe positively ("empty street", "pedestrian-only zone") |
| **Missing lighting details** | Flat, inconsistent illumination | Describe light source, quality, direction, color temp |
| **Aspect ratio changes unexpectedly** | Crops important elements | Add "Do not change the input aspect ratio" when editing |
| **Text spelling errors** | Garbled text in image | Keep text under 25 characters, specify font clearly |
| **Small faces rendering poorly** | Blurry or distorted features | Use close-up compositions, specify "portrait" shot type |

---

## Advanced Techniques

### Character Consistency Across Multiple Generations

#### Method 1: Multi-Turn Conversation (Most Reliable)

Use Gemini's 1-million-token context window:

```
TURN 1:
Create a character: A young woman with curly red hair, freckles, and green eyes 
wearing a vintage denim jacket. Photorealistic portrait, soft natural lighting.

TURN 2:
Show the same character from the previous image, now sitting at a café reading 
a book. Keep identical facial features and outfit. Medium shot, warm café lighting.

TURN 3:
Same character walking through a park in autumn, leaves falling around her. 
Maintain exact same facial features, hair, and denim jacket. Golden hour lighting.
```

**Pro Tip:** Use preservation commands:
- "Keep the exact same composition"
- "Maintain identical facial features"
- "Preserve all original colors"
- "Keep this person's likeness"

#### Method 2: Reference Image Input (Up to 14 Images)

Upload reference images and describe relationships:

```
Using Image 1 as the character reference and Image 2 as the style reference, 
create a portrait of this person in the artistic style shown. The character 
should maintain their exact facial features, hair color, and eye color from 
Image 1 while adopting the painterly aesthetic of Image 2.
```

**Reference Image Best Practices:**
- Use high-resolution, well-lit images
- Front-facing photos work best for facial consistency
- Realistic human images > stylized/anime for character work
- Combine up to 5 human references and 6 object references

---

### Style Consistency Techniques

#### Style DNA Extraction
```
Analyze the visual style of these three reference images (Image 1, Image 2, Image 3) 
and describe the common aesthetic elements: color palette, lighting approach, 
composition style, and artistic technique.
```

Then use extracted description:
```
Create a new image using the style DNA: [paste extracted description here]. 
Subject: [your new subject]
```

#### Multi-Pass Refinement
1. Generate base image
2. Identify preferred elements ("I like the lighting in this version")
3. Regenerate emphasizing those elements
4. Combine best aspects for final version

---

### Text Rendering Best Practices

**For logos, signage, typography:**

```
Create a modern coffee shop logo with the text "Brewed Awakening" in a bold 
sans-serif font. The design should feature a minimalist coffee cup icon above 
the text. Clean lines, earthy brown and cream color palette, professional branding.
```

**Rules:**
1. Always put exact text in quotation marks
2. Specify font style (serif, sans-serif, script, bold, etc.)
3. Keep text under 25 characters for accuracy
4. Provide context for text placement
5. Test complex spellings - regenerate if errors occur

---

### Google Search Grounding (Gemini 3 Pro Exclusive)

For real-time information visualization:

```
Visualize the current weather forecast for the next 5 days in San Francisco 
as a clean, modern weather chart. Include high/low temperatures, conditions 
(sunny/cloudy/rainy), and visual recommendations for what to wear each day. 
Infographic style, blue and white color scheme.
```

**Use Cases:**
- Current events visualization
- Real-time data charts
- Product information that changes frequently
- Trending topic illustrations

**Configuration Required:** Enable `tools=[{"google_search": {}}]` in API config

---

## Optimization for Different Use Cases

### Portrait Photography
```
[Action verb] a [photorealistic/stylized] [close-up/medium/full-body] portrait 
of [subject with 8+ specific characteristics]. [Subject action or expression]. 
Set in [specific location]. Illuminated by [detailed lighting]. Shot with 
[camera/lens]. [Aspect ratio]. Mood: [emotional tone].
```

### Product Visualization
```
Generate a professional product photograph of [detailed product description] 
on a [background type]. Studio lighting setup with [key light position], 
[fill light], and [rim light]. Shot with [lens specs] for [desired effect]. 
[Aspect ratio]. Clean, commercial aesthetic.
```

### Editorial Illustration
```
Illustrate [concept/scene] in a [art style] style. [Detailed scene description]. 
The composition should emphasize [focal point]. Color palette: [specific colors]. 
Mood: [emotional tone]. [Aspect ratio]. Reference artists: [optional].
```

### Sticker/Icon Design
```
Create a [style] sticker of [subject], featuring [key characteristics] and 
a [color palette]. The design should have [line style] and [shading approach]. 
White background. Clean vector aesthetic.
```

---

## Resolution Strategy

| Use Case | Recommended Resolution | Reasoning |
|----------|----------------------|-----------|
| Rapid prototyping | 1K | Fast iteration, concept validation |
| Client review | 2K | Balance quality/speed, good detail |
| Social media | 2K | Sufficient for web display |
| Print materials | 4K | Maximum quality, print-ready |
| Final assets | 4K | Highest fidelity, future-proof |

**Pro Tip:** Start at 1K for exploration, move to 2K for refinement, generate 4K only for final approved concepts.

---

## Troubleshooting Guide

### Issue: Character Features Drift After Multiple Edits

**Solutions:**
1. Reset with original reference image
2. Consolidate all edits into single comprehensive prompt
3. Use multi-turn conversation mode instead of single generations
4. Add preservation commands explicitly

### Issue: Poor Quality Results

**Solutions:**
1. Increase resolution (try 2K or 4K)
2. Use high-resolution reference images if providing
3. Add more specific lighting description
4. Specify camera/lens details for depth control

### Issue: Text Rendering Errors

**Solutions:**
1. Reduce text length (under 25 characters)
2. Simplify spelling/avoid unusual words
3. Specify font family more clearly
4. Use quotation marks around exact text
5. Generate multiple times if errors persist

### Issue: Composition Doesn't Match Intent

**Solutions:**
1. Be more specific about shot type (close-up, medium, wide)
2. Add camera angle (eye-level, low-angle, high-angle, bird's-eye)
3. Specify what should be in focus vs background
4. Use framing language (centered, rule of thirds, off-center)

---

## Quick Reference Checklist

Before submitting a prompt, verify:

- [ ] Starts with action verb (Create, Generate, Illustrate, etc.)
- [ ] Subject has 6+ descriptive characteristics
- [ ] Action/pose is clearly specified
- [ ] Location includes atmospheric details
- [ ] Lighting is described (quality, direction, color)
- [ ] Style/mood is explicitly stated
- [ ] Composition details included (shot type, camera, lens)
- [ ] Any text is in quotation marks
- [ ] Written as full sentences, not keyword lists
- [ ] Only 1-3 changes from previous iteration (if refining)

---

## Templates for Common Scenarios

### Character Introduction (First Generation)
```
Create a [style] [shot type] portrait of [detailed character description including: 
age, ethnicity, distinctive features, clothing, personality traits]. [Character is 
doing action]. Set in [environment]. [Lighting details]. [Camera specs]. 
[Aspect ratio]. Mood: [tone].
```

### Character in New Scene (Subsequent Generations)
```
Show the same character from the previous image, now [new action/location]. 
Keep identical facial features, [specific details to preserve]. [New environment 
description]. [New lighting]. [New composition]. Maintain character consistency.
```

### Image Editing - Add Element
```
Using the provided image, add [specific element] to [location in image]. 
The addition should [integration requirements]. Match the existing lighting, 
style, and quality. Keep all other elements unchanged.
```

### Image Editing - Remove Element
```
Remove [specific element] from the provided image. Fill the area naturally to 
maintain scene continuity, lighting, and details. Keep all other elements exactly 
the same. [Style matching].
```

### Image Editing - Style Transfer
```
Transform the provided image into [target style], while maintaining the exact 
composition, subject position, and scene structure. Adapt lighting and textures 
to match [style description]. Preserve all key elements.
```

---

**Remember:** Gemini 3 Pro excels when given clear, detailed, sentence-based prompts with comprehensive context. The model's thinking mode means it can handle complex requests—don't oversimplify, but do organize your instructions clearly.
