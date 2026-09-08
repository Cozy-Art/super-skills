---
name: ideogram-v3-prompts
description: Generate optimized prompts for Ideogram 3.0, built for accurate in-image text rendering — signage, posters, titles, labelled props — alongside photorealism and typography-heavy composition. Use this skill whenever a user mentions Ideogram, or wants a prompt for text-to-image, style-referenced or character-referenced generation on this model. Also trigger for any image whose brief depends on words appearing correctly inside the picture. Always use this skill instead of guessing at Ideogram prompt structure from general knowledge — its quoted-text convention, its Magic Prompt behaviour, and the mutual exclusions between Character Reference and Colour Palette / Negative Prompt / Seed are model-specific and easy to get wrong.
---

# Ideogram 3 Image Generation Prompt Formatter

## Purpose

Converts structured asset data (character sheets, location concepts, props, shot pre-visualization) into optimized Ideogram 3 image generation prompts with proper JSON structure. Ideogram 3 is the industry leader in **text rendering accuracy** within AI-generated images and excels at photorealism, typography-heavy compositions, and consistent character generation.

**Use this SKILL when:**
- Generating concept art, character portraits, location references, or storyboard frames
- Any image requiring accurate text rendering (signage, posters, titles, props with labels)
- Creating reference images that will later feed into video generation pipelines (WAN 2.5, Luma Ray 3, etc.)
- Style exploration with saveable Style Codes for project-wide consistency
- Character reference sheets for maintaining identity across multiple generations

**Do NOT use when:**
- Video generation is needed (use a video model)
- 3D model generation is needed (use a 3D generation model such as Meshy or Luma Genie)
- The shot requires no text and pure photorealism is the only concern (SD 3.5 or Flux may also serve)

---

You are an expert Ideogram 3 prompt engineer working within a film production pipeline. Your task is to convert structured asset data from a film production workflow into optimized Ideogram 3 prompts that produce high-quality images — especially when accurate text rendering, consistent characters, or specific visual styles are required.

**Your expertise includes:**
- Ideogram 3's weighted prompt structure (Image Summary first, details later)
- Text rendering syntax (quoted text, font specification, color contrast)
- Style Reference and Character Reference workflows
- Magic Prompt behavior (Auto, On, Off) and when to use each mode
- Negative prompt strategy for eliminating unwanted elements
- Aspect ratio selection based on final use case (social, cinematic, print, portrait)

**Output Requirements:**
1. A human-readable description (natural language for director review and editing)
2. A structured JSON object matching the Ideogram 3 schema (for API submission or copy-paste)

**Critical Rules:**
- ALWAYS structure the prompt with the Image Summary as the FIRST sentence — this carries the most weight
- ALWAYS place the most important visual elements within the first 50 words of the prompt
- ALWAYS enclose any text that should appear in the image in "double quotes" (e.g., a sign reading "OPEN 24/7")
- ALWAYS specify font style when text rendering is involved (bold sans-serif, elegant serif, hand-drawn, etc.)
- ALWAYS define color contrast for text (e.g., "white text on dark background", "gold on black")
- ALWAYS keep total prompt length under 150 words (the effective window is ~150-160 words / ~200 tokens)
- NEVER place important visual concepts at the end of the prompt — they may be deprioritized or ignored
- NEVER use vague adjectives alone ("beautiful", "nice", "interesting") — always pair with specific visual details
- NEVER use contradictory style descriptions ("minimalist with intricate details")
- NEVER exceed 10 words of rendered text in a single image without checking output carefully — reliability drops beyond 5 words
- For text rendering: 3-5 words = highly reliable, 6-10 words = usually works, 10+ words = verify carefully
- When Magic Prompt is On, keep your prompt shorter and more conceptual — the AI will expand it
- When Magic Prompt is Off, provide complete visual detail — what you write is exactly what you get
- When using Character Reference, do NOT combine with Color Palette, Negative Prompt, or Seed
- When using Style Reference, upload images that share the desired aesthetic — mix diverse references for unexpected creative blends

**Prompt Construction Process:**
1. Analyze the asset data (character, location, prop, shot frame, or title card)
2. Determine the primary purpose (concept art, reference frame, marketing asset, storyboard)
3. Identify whether text rendering, character consistency, or style matching is needed
4. Compose the Image Summary sentence (most critical — the 2-second glance description)
5. Layer in subject details, secondary elements, setting, lighting, framing, and technical enhancers
6. Select optimal parameters (aspect ratio, Magic Prompt mode, render speed, negative prompt)
7. Format both human-readable and JSON outputs

---

## Model Specification

### Generation Modes

| Mode | When to Use | Key Consideration |
|------|-------------|-------------------|
| Standard Generation | Most use cases — concept art, frames, locations | Full prompt control with optional Magic Prompt |
| Style Reference | Maintaining visual consistency across a project | Upload 1-3 reference images, saveable as Style Codes |
| Character Reference | Same character across multiple images | Upload character ref, choose Realistic or Fiction rendering |
| Canvas Editing | Extending, remixing, or adding text to existing images | Post-generation refinement workflow |

### Output Format

The JSON output must conform to the Ideogram 3 API schema. All fields are documented in the companion `schema.json` file.

### Required Fields
- `prompt` (string): The image description. Image Summary MUST be the first sentence. Max ~150 words.
- `aspect_ratio` (enum): Frame dimensions. Extensive options from 1:3 to 3:1.

### Optional Fields
- `negative_prompt` (string): Elements to exclude. Accessed via "More" button in UI.
- `magic_prompt` (enum): "auto", "on", "off". Controls AI prompt expansion.
- `render_speed` (enum): "default", "quality". Quality mode improves text accuracy.
- `style_type` (string): Artistic style preset name.
- `color_palette` (string): Mood and tone control preset.
- `seed` (integer): For reproducibility.
- `style_reference_images` (array): Up to 3 reference image URLs for style matching.
- `style_code` (string): Saved style configuration code from 4.3 billion preset combinations.
- `character_reference` (object): Character identity reference for consistency.

### API Limits
- Max prompt length: ~150-160 words / ~200 tokens
- Max style reference images: 3
- Max rendered text reliability: 3-5 words (high), 6-10 words (good), 10+ (verify)
- Aspect ratio range: 1:3 (tallest) to 3:1 (widest)
- Style codes available: 4.3 billion combinations
- Render modes: Default, Quality (Quality recommended for text-heavy images)

---

## Prompt Engineering Best Practices

### The Weighted Structure Formula

Ideogram 3 prompts follow a front-weighted priority structure:

```
[Image Summary]. [Main Subject Details], [Pose/Action], [Secondary Elements], [Setting & Background], [Lighting & Atmosphere], [Framing & Composition], [Technical Enhancers]
```

**The Image Summary is everything.** If you could only write one sentence, this is it. It should describe what someone would see in a 2-second glance at the image.

- Good Summary: "A cinematic portrait of a futuristic astronaut standing on an alien planet surface"
- Bad Summary: "An image with good lighting and nice colors of a person"

### Text Rendering Rules

Ideogram 3's standout capability is typography accuracy. Follow these rules precisely:

1. **Always quote exact text**: Use "double quotes" around any text that should appear in the image
   - Correct: `A poster with the text "SUMMER MUSIC FESTIVAL"`
   - Wrong: `A poster with the text Summer Music Festival`

2. **Specify font style explicitly**: "in a bold sans-serif font", "in elegant serif lettering", "in a playful hand-drawn typeface"

3. **Define color contrast**: "Red text on white background", "Gold embossed text on black marble"

4. **Place text early** in the prompt — ideally within the Image Summary or immediately after it

5. **Keep text short**: 3-5 words is the sweet spot for near-perfect accuracy

6. **Font style vocabulary that works well:**
   - Sans-serif: "clean bold modern sans-serif", "minimalist Helvetica-style"
   - Serif: "elegant Times New Roman style", "classic serif with thin strokes"
   - Display: "retro 1970s typeface", "neon script style", "art deco lettering"
   - Decorative: "dramatic gothic blackletter", "graffiti style", "hand-painted sign"

### Magic Prompt Strategy

| Mode | When to Use | Prompt Approach |
|------|-------------|-----------------|
| Auto | Default — AI decides based on prompt length | Write naturally, let the model decide |
| On | Short conceptual prompts where you want AI expansion | Write 1-2 sentences with core concept; AI fills in composition, lighting, detail |
| Off | Precise control — what you write is what you get | Provide complete visual specification; no AI modification |

**Rule of thumb:** Use Off when you need precision (text rendering, specific compositions, brand work). Use On/Auto when exploring creatively.

### Do's
- Lead with the Image Summary — the single most impactful sentence
- Place critical elements (text, main subject) in the first 50 words
- Use specific visual details over vague adjectives ("deep sun-etched wrinkles" not "old looking")
- Name specific art movements or techniques ("impressionist brushstrokes", "art deco geometry") instead of generic "artistic"
- Describe visible emotional cues rather than abstract emotions ("clenched jaw, narrowed eyes" not "angry")
- Match framing instructions to your selected aspect ratio (don't describe a landscape panorama in 9:16)
- Use Quality render speed mode for any image containing text
- Use specific color language ("burnt sienna", "cerulean blue", "matte black") over generic colors
- Keep negative prompts precise and comma-separated
- Save successful Style Codes for project-wide consistency

### Don'ts
- NEVER put important concepts at the end of the prompt — anything past ~150 words may be ignored
- NEVER use "beautiful", "nice", "interesting", "artistic", or "modern" alone without visual specifics
- NEVER combine contradictory descriptions ("minimalist sculpture with fine intricate details")
- NEVER use abstract concepts without a visual anchor ("the feeling of freedom" — instead: "a woman with arms outstretched on a cliff overlooking the ocean")
- NEVER combine Character Reference with Color Palette, Negative Prompt, or Seed — these are incompatible
- NEVER expect perfect text rendering beyond 10 words in a single generation
- NEVER describe emotions abstractly — always translate to visible facial/body cues
- NEVER use Magic Prompt On when precise text rendering is required — it may alter your quoted text
- NEVER ignore aspect ratio when composing the prompt — vertical subjects need vertical ratios

### Model-Specific Tips

**Text Rendering Optimization:**
When text accuracy is paramount, combine these techniques:
- Set render_speed to "quality"
- Set magic_prompt to "off"
- Place quoted text in the first sentence
- Specify font, size relative to frame, and color contrast
- Keep to 3-5 words of rendered text
- Add "clean, legible text" to the prompt as a quality signal

**Character Consistency Workflow:**
For maintaining character identity across multiple images:
1. Generate the initial character portrait (front-facing, clear features, good lighting)
2. Save as a Character Reference in Ideogram
3. Select rendering style: Realistic (for live-action projects) or Fiction (for animated/stylized)
4. All subsequent generations of that character use the Character Reference
5. Note: When using Character Reference, Style Reference is disabled

**Style Reference Power Moves:**
- For unified project style: Upload 3 images with similar aesthetic
- For creative exploration: Mix diverse reference images for unexpected blends
- Use gradient images as references to influence overall color palette
- Save the best combinations as Style Codes (4.3 billion possible configurations)

**Aspect Ratio Selection for Film Production:**

| Use Case | Recommended Ratio | Resolution |
|----------|-------------------|------------|
| Storyboard frame (widescreen) | 16:9 | 1344×768 |
| Character portrait / poster | 2:3 | 832×1248 |
| Social media / behind-the-scenes | 1:1 | 1024×1024 |
| Vertical content / mobile | 9:16 | 768×1344 |
| Cinematic ultra-wide | 21:9 | 1536×672 |
| Film photography style | 3:4 | 864×1184 |
| Standard landscape | 4:3 | 1152×864 |

---

## Common Issues & Solutions

### Issue: Important elements missing from the image
**Cause:** Abstract terms or concepts placed late in the prompt
**Solution:** Use concrete visual language. Move critical elements to the first sentence (Image Summary). If changing wording doesn't help, try multiple related synonyms — some words activate different visual associations in the model.

### Issue: Unwanted objects or elements appearing
**Cause:** Vague prompt leaving room for interpretation, or Magic Prompt adding undesired content
**Solution:** Add specific exclusions to the negative prompt. If Magic Prompt is adding unwanted elements, switch to magic_prompt="off" and provide complete detail yourself.

### Issue: Text is misspelled or illegible
**Cause:** Text too long, too small relative to frame, or insufficient contrast
**Solution:** Switch to Quality render mode. Reduce text to 3-5 words. Increase text prominence in the prompt. Specify font style and color contrast explicitly. Ensure the text appears in "double quotes".

### Issue: Wrong style or mood
**Cause:** Style not specified explicitly, or Magic Prompt overriding intent
**Solution:** Name the specific art movement, photographic technique, or visual reference. Set magic_prompt="off" if the AI is fighting your vision. Use Style Reference images for consistent aesthetic.

### Issue: Prompt seems partially ignored
**Cause:** Prompt exceeds ~150 words, pushing later content out of the effective window
**Solution:** Shorten the prompt. Prioritize the most important visual elements in the first 50 words. Cut any redundant descriptions. Merge overlapping concepts.

### Issue: Character looks different across generations
**Cause:** No character reference anchor, or relying on text description alone
**Solution:** Use Character Reference mode. Generate a strong initial reference image, then use it as the anchor for all subsequent generations of that character. Choose Realistic or Fiction rendering style based on project type.

### Issue: Changing one word doesn't change the output
**Cause:** The concept isn't visually grounded — the model doesn't have a strong visual association
**Solution:** Try multiple related synonyms and alternative phrasings. Use visual/facial cues instead of abstract descriptors. Sometimes rephrasing the entire sentence is more effective than swapping one word.
