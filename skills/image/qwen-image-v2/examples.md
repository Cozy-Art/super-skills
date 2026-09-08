# Qwen Image — Example Prompts

All examples sourced and annotated from official Qwen Image documentation and community validation. Each includes version routing, recommended parameters, and technique notes.

---

## Version Routing Guide

| Example | Works on v1/2512? | Requires 2.0? |
|---------|------------------|---------------|
| 1. Simple Portrait | ✅ | No |
| 2. Environment / Landscape | ✅ | No |
| 3. Poster with Text | ⚠️ Basic only | ✅ Full element-by-element layout |
| 4. Product / E-Commerce | ✅ | No |
| 5. Infographic / Slide | ❌ | ✅ 1,000-token budget required |
| 6. Character Scene (Artistic) | ✅ | No |
| 7. Multi-Character Composite | ✅ | No |

---

## Example 1 — Simple Photorealistic Portrait

**Formula:** Subject + physical description → lighting → style → composition  
**Works on:** v1/2512 and 2.0  
**Parameters:** `image_size: "portrait_4_3"` · `output_format: "png"` · `guidance_scale: 3.0` (v1 only)

```
A 28-year-old East Asian woman with natural curly hair,
wearing a white linen shirt, standing in soft window light indoors.
Candid, unposed expression. Editorial photography style.
Shallow depth of field. Clean white background, slightly blurred.
```

**Technique notes:**
- No "photorealistic" booster — the visual description activates realism instead
- Age and ethnicity are specific, renderable facts
- "Natural curly hair" is specific material description
- "Candid, unposed" prevents stock-photo pose defaults
- "Editorial photography style" is one clear style anchor
- "Clean white background, slightly blurred" handles the background without overspecifying

---

## Example 2 — Environment / Landscape

**Formula:** Primary landscape feature → detail accumulation → light → time of day → negative composition  
**Works on:** v1/2512 and 2.0  
**Source:** Official Qwen-Image-Max example  
**Parameters:** `image_size: "landscape_16_9"` · `output_format: "jpeg"`

```
A turquoise river winds through a lush canyon. Thick moss and dense ferns cover the rock walls.
Multiple waterfalls cascade from high above, shrouded in mist.
At noon, sunlight filters through the dense canopy, casting dappled shimmering spots on the river surface.
The air feels moist and fresh, full of primitive jungle vitality.
No people, no text, no artificial objects in the scene.
```

**Technique notes:**
- Front-loaded with the primary feature: "turquoise river"
- Negative composition (`"No people, no text..."`) written as part of the positive prompt — this works well in Qwen and avoids the negative prompt field for compositional exclusions
- Atmospheric language ("moist and fresh," "primitive jungle vitality") is unusually effective here — the LM encoder handles emotion when paired with specific visual anchors
- Time of day specified explicitly: "At noon"

---

## Example 3 — Poster with In-Image Text

**Formula:** Background → center illustration → text elements top-to-bottom → style/finish  
**Works on:** Basic on v1/2512; full element-by-element control requires 2.0  
**Parameters:** `image_size: {width: 1080, height: 1920}` · `output_format: "png"` · (2.0) `enable_prompt_expansion: false`

```
A vertical event poster. Background: deep navy blue with subtle star-field grain texture.
Center: a geometric illustration of a mountain range rendered in gold line art.
Top third: the text "ALTITUDE FESTIVAL" in large bold condensed sans-serif, white, all caps.
Below the title: "June 20–22 | Telluride, Colorado" in smaller weight, gold color.
Bottom: "altitudefestival.com" in minimal small caps, white.
Balanced whitespace. Modern editorial design. Print-ready at 2K resolution.
```

**Technique notes:**
- Background described before foreground — establishes the canvas
- Each text element described in its own sentence with: string in quotes → font style → color → position
- "All caps" is an explicit instruction that prevents the model from guessing capitalization
- "Balanced whitespace" and "Print-ready" activate design-finishing behavior
- This prompt is ~85 words — within v1/2512 effective range, but 2.0 handles it more reliably
- Use `output_format: "png"` always for text designs

---

## Example 4 — Product / E-Commerce Photography

**Formula:** Subject + material → surface → lighting → composition → negative  
**Works on:** v1/2512 and 2.0  
**Parameters:** `image_size: "square_hd"` · `output_format: "png"` · `guidance_scale: 3.5` (v1 only)

```
A clean product photography shot of a matte black ceramic pour-over coffee dripper.
Placed on a white marble surface with faint veining.
Soft diffused studio lighting from the left.
A small card next to it reads "SINGLE ORIGIN" in minimal serif type.
Minimal composition, slight downward angle, professional product catalog aesthetic.
No background objects, no shadows except a gentle ground shadow directly beneath.
```

**Technique notes:**
- "Matte black ceramic" is a precise material callout — not "black object"
- "White marble with faint veining" — surface detail prevents generic white background
- "Soft diffused studio lighting from the left" — direction + quality specified
- Text element included in the scene description: `reads "SINGLE ORIGIN"` — Qwen handles this well inline
- Negative composition inline: "No background objects, no shadows except..." — more reliable than negative prompt field for precise spatial exclusions
- "Professional product catalog aesthetic" as use case signal

---

## Example 5 — Infographic / Slide (Qwen-Image-2.0 Required)

**Formula:** Background → title → columns/sections (element-by-element) → caption → style signal  
**Requires:** Qwen-Image-2.0 (1,000-token budget)  
**Parameters:** `image_size: {width: 1920, height: 1080}` · `output_format: "png"` · `enable_prompt_expansion: false`

```
A single-slide infographic explaining the evolution of Qwen-Image AI.
White background. Title at top: "Qwen Image: From 20B to 7B" in bold dark blue sans-serif.
Three columns below the title, each with a labeled icon:
Left: clock icon, label "Qwen-Image v1 (Aug 2025) — 20B Parameters"
Center: upward arrow icon, label "Qwen-Image-2512 (Dec 2025) — Enhanced Textures"
Right: star icon, label "Qwen-Image-2.0 (Feb 2026) — 7B Unified Model"
Bottom caption: "Source: Alibaba Tongyi Lab" in small gray italic.
Clean tech brand style, consistent icon line weight, ample padding.
```

**Technique notes:**
- Background stated first: "White background."
- Hierarchical structure described top-to-bottom: title → columns → caption
- Each labeled text element quoted exactly
- Icon descriptions are abstract ("clock icon") — the model infers standard icon representations
- "Consistent icon line weight" and "ample padding" signal design finishing quality
- This requires ~120 words / ~200 tokens — within 2.0's budget but would truncate on v1/2512
- `enable_prompt_expansion: false` is critical here — any auto-rewrite would damage the layout spec

---

## Example 6 — Character Scene (Artistic Style)

**Formula:** Character + clothing → action → setting → atmosphere → style anchor → mood  
**Works on:** v1/2512 and 2.0  
**Parameters:** `image_size: "portrait_4_3"` · `output_format: "jpeg"` · `guidance_scale: 3.0` (v1 only)

```
A young woman in a flowing red kimono with crane patterns stands on a traditional wooden bridge
over a koi pond in autumn. Maple leaves fall around her.
She looks contemplatively into the water.
Soft overcast light, muted earth tones, Studio Ghibli-inspired illustration style.
Painterly texture, warm sepia shadows, high emotional atmosphere.
```

**Technique notes:**
- "Studio Ghibli-inspired" — this style descriptor is effective because it's a well-represented aesthetic in training data; use "inspired" rather than direct name attribution
- Single clear style anchor: illustration (not "photorealistic" — that would conflict)
- "Contemplatively" is mood language that works here because it's paired with a specific visual action ("looks into the water")
- "Muted earth tones" as color direction — specific enough to act on
- "Painterly texture, warm sepia shadows" are renderable style modifiers, not vague praise

---

## Example 7 — Multi-Character Composite

**Formula:** Setting → Character A description → Character B description → interaction → lighting  
**Works on:** v1/2512 and 2.0  
**Parameters:** `image_size: "landscape_4_3"` · `output_format: "jpeg"` · `guidance_scale: 3.0` (v1 only)

```
Two women are seated on a white linen sofa in a bright minimalist living room.
Woman on the left has natural coily hair, wearing a mustard yellow blazer, relaxed smile.
Woman on the right has straight black hair, wearing a slate blue turtleneck, laughing.
They are holding mugs and turned slightly toward each other in conversation.
Natural midday daylight through large windows. Warm, candid lifestyle photography mood.
```

**Technique notes:**
- Setting established first to ground the composition
- Each character described separately with full physical detail
- Clothing is specific: "mustard yellow blazer," "slate blue turtleneck" — not "yellow top," "blue shirt"
- Interaction described explicitly: "turned slightly toward each other," "holding mugs"
- Shared lighting applied after both characters: "Natural midday daylight through large windows"
- "Warm, candid lifestyle photography mood" as style anchor — one clear direction

---

## Additional Templates

### Bilingual Poster (Chinese + English)
```
一张竖版海报，推广[活动名称]。
背景：[颜色描述]。
中央：[主视觉元素描述]。
顶部文字："[中文标题]" — 粗体，[字体风格]，[颜色]。
英文副标题："[English subtitle]" — 较小字重，[颜色]，位于中文标题下方。
底部："[网址或联系方式]" — 小字，[颜色]。
[整体风格描述]。
```
*Write Chinese text elements directly in Chinese characters for best rendering.*

### Simple Product Shot
```
[Product name + material + color]. Placed on [surface with detail].
[Lighting direction and quality]. [Minimal composition signal].
[Use case signal: "product catalog," "e-commerce listing"].
No [unwanted elements].
```

### Character Consistency Anchor
```
[Character name]: [age]-year-old [ethnicity/description], [hair], [eyes], [distinguishing features].
Wearing: [specific clothing items with colors].
Expression: [specific expression].
[Photography/illustration style]. [Lighting].
```
*Lock seed on this generation. Use as image 1 in subsequent I2I calls.*

### Next-Scene Cinematic Transition
```
Next Scene: [Camera movement description — dolly, pull-back, push-in].
[What changes in the frame as the camera moves].
[What remains consistent — subject, lighting style, time of day].
[Audio/mood evolution if applicable].
```
*Use endpoint: `fal-ai/qwen-image-edit-2509-lora-gallery/next-scene` · LoRA scale 0.7–0.8*

---

## Quick Diagnostic: Is My Prompt Correct?

- [ ] Is the primary subject in the first 5–10 words?
- [ ] Is there exactly one clear style anchor?
- [ ] Are all in-image text strings in quotation marks?
- [ ] Is font style, color, and position specified for each text element?
- [ ] Is `output_format: "png"` set for text-heavy designs?
- [ ] Is `acceleration` set to `none` or `regular` (not `high`) for text images?
- [ ] Is `enable_prompt_expansion: false` during iterative testing? (2.0 only)
- [ ] Is the negative prompt written in NLP sentences (not keyword lists)?
- [ ] Is the negative prompt under 500 characters? (2.0 only)
- [ ] For multi-image edits: is there a space between "image" and the number? (`image 1` not `image1`)
- [ ] For multi-image edits: is there a preserve instruction?
- [ ] For Chinese text: are Chinese characters written directly (not romanized)?
- [ ] For complex layouts: am I using Qwen-Image-2.0 (not v1/2512)?
- [ ] Is `guidance_scale` at 2.5–5 maximum? (v1/2512 only — above 5 causes artifacts)
- [ ] For blurry/washed out local output: is `shift` raised to 12–13?
