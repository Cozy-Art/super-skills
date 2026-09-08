# Stable Diffusion 3.5 — Example Prompts

All examples sourced from official Stability AI documentation and community-validated patterns.

---

## Example 1 — Text Rendering (Sign / Typography)

**Formula:** Subject + object with quoted text + medium + setting  
**Variant:** Large or Medium  
**Parameters:** CFG 4.4–5.5 · Steps 25–30

```
A vintage coffee shop sign reading "BREW & BLOOM" in warm, hand-lettered typography,
surrounded by illustrated coffee beans and small flowers, on weathered wood background.
```

**Technique notes:**
- Text in **double quotation marks** — this is the trigger for SD3.5's text rendering pathway
- "Hand-lettered typography" describes the font style without requiring exact font specification
- No negative prompt needed — clean subject with simple composition
- "Weathered wood background" is a specific material rather than "rustic background"
- If text rendering is imprecise: increase steps to 30–35 and CFG to 5.0–5.5

---

## Example 2 — Environmental Portrait with Neon Text

**Formula:** Subject + environment + neon text in quotes + mood + color palette  
**Variant:** Large  
**Parameters:** CFG 4.4 · Steps 25 · No negative prompt

```
Beautiful pale woman, close up, drowning in an old tavern that has been flooded by sea water.
The waves are crashing against the walls.
The neon bar light reads "And So It Was" in red, its light reflects in the water.
Some playing cards and a martini glass are floating in the waves.
The scene is mostly white, bright, and faded, the mood is ominous, bleak and hauntingly beautiful.
```

**Negative prompt:** (none)

**Technique notes:**
- Natural language sentence structure handles complex spatial scene (woman, water, floating objects, neon sign) better than keyword list
- Text in quotes: `"And So It Was"`
- Mood language ("ominous, bleak and hauntingly beautiful") works because it's paired with specific visual anchors (pale woman, white/bright/faded palette, floating objects)
- No negative prompt — official Stability AI example; the positive description is specific enough
- "Its light reflects in the water" is a physical lighting interaction described in plain language

---

## Example 3 — Action / Dynamic Scene

**Formula:** Shot type + subject + action + environment  
**Variant:** Large or Turbo  
**Parameters (Large):** CFG 4.4 · Steps 20–25  
**Parameters (Turbo):** CFG 1.0 · Steps 4

```
Dynamic action shot of a cyberpunk flying car traveling over the grimy neon-lit streets
of a dystopian futuristic city below.
```

**Technique notes:**
- "Dynamic action shot" is both a mood instruction and a compositional cue — activates motion/energy composition
- "Grimy neon-lit" — specific material quality (grimy) + lighting type (neon)
- Works well on Turbo at this length — concise enough for Turbo's simpler prompt preference
- Can extend with: "Heavy rain, motion blur on the car, reflection of city lights on the vehicle's body"
- No negative prompt needed for this type of scene

---

## Example 4 — Illustration: Art Nouveau Style

**Formula:** Style first + subject description  
**Variant:** Large or Medium  
**Parameters:** CFG 4.4 · Steps 25

```
A tiny snail approaching a house built into a mushroom. Art Nouveau drawing in a Vienna Secession style.
```

**Negative prompt:** `deformed, ugly, photo, photorealism`

**Technique notes:**
- Style is **at the end** in this official example — note it still works because the scene is simple enough that the CLIP window captures both
- For more complex scenes, move style to front
- "Vienna Secession style" is a specific named aesthetic within Art Nouveau — more precise than "Art Nouveau" alone
- Negative prompt is minimal and strategic: only excludes photorealism to prevent style drift
- This is the appropriate length for Turbo — could be used directly at 4 steps

---

## Example 5 — Complex Fantasy Portrait

**Formula:** Medium/style indicator + multi-element subject description + material texture detail  
**Variant:** Large  
**Parameters:** CFG 4.4–5.0 · Steps 30–35  
**Negative prompt:** (none)

```
A highly detailed and vibrant digital artwork combining elements of realism and fantasy.
The composition features a portrait of a snake-human hybrid, with the subject's pale, smooth skin
subtly textured to resemble scales.
The snake-human's head is intricately detailed, facing the viewer with large, expressive eyes
that shimmer with vivid green irises.
Layers of iridescent and metallic textures contrast against darker, moody tones of black,
grey, and hints of gold.
The artwork merges hyper-realism with fantasy, rich in vivid colors and intricate details.
```

**Negative prompt:** (none)

**Technique notes:**
- Begins with a style/approach statement: "highly detailed and vibrant digital artwork"
- Each physical attribute described with texture language: "pale, smooth skin subtly textured to resemble scales"
- Color palette specified explicitly: "iridescent and metallic textures," "black, grey, and hints of gold"
- "Vivid green irises" is a specific detail — not just "green eyes"
- ~120 words — on the longer end; T5-XXL handles this; critical detail in first 77 tokens
- No negative prompt — the positive description is sufficiently specific

---

## Example 6 — Caricature / 3D Cartoon Style

**Formula:** Subject description + distinctive details + setting + expression + style  
**Variant:** Large or Medium  
**Parameters:** CFG 4.4 · Steps 25

```
A woman gardener with dirt and flowers in her hair, holding a cardboard box full of spring flowers,
wearing denim overalls, suburban wall background.
Piercing blue eyes and an exhausted expression.
Hilarious caricature in a 3D cartoon style.
```

**Negative prompt:** `deformed, ugly, photo, photography`

**Technique notes:**
- "Hilarious caricature in a 3D cartoon style" — combined style instruction at the end works here because the prompt is relatively short
- "Piercing blue eyes and an exhausted expression" — specific physical details plus emotion
- "Suburban wall background" — simple, uncluttered background instruction
- Negative prompt minimal: only excludes photorealism (appropriate when targeting cartoon style)
- "Cardboard box full of spring flowers" — specific prop rather than vague prop mention

---

## Example 7 — Product / Still Life Photography

**Formula:** Camera angle + surface + objects + action/detail + atmosphere  
**Variant:** Large  
**Parameters:** CFG 4.4–5.0 · Steps 25–30  
**Negative prompt:** (none)

```
Eye level shot of a rustic, hand-crafted wooden table covered with roasted coffee beans,
a burlap sack spilling beans in the foreground.
Hot streaming cup of espresso sits beside a sack of coffee beans,
with wisps of steam curling into the air.
```

**Technique notes:**
- "Eye level shot" — precise compositional instruction
- "Rustic, hand-crafted wooden table" — three descriptors creating a specific material quality
- "Burlap sack spilling beans" — physical action described (spilling) rather than just "burlap sack with beans"
- "Wisps of steam curling" — specific motion description for the steam
- No negative prompt — composition-focused still life with no distractors to exclude
- Can add: "Warm, diffused morning light from the left, shallow depth of field"

---

## Additional Templates

### Portrait / Character (Photorealistic)
```
[Gender/age] [distinctive physical features], [expression]. [Clothing description].
[Shot type: close-up/medium/full body]. [Lighting: direction, quality, source].
[Background: specific but uncluttered description]. Photorealistic [photography style].
```
*CFG: 4.4 · Steps: 25–30 · Negative: `deformed, ugly`*

### Landscape / Environment
```
[Primary landscape feature] at [time of day].
[Secondary environmental features in spatial order — mid-ground].
[Background element]. [Atmospheric conditions].
[Lighting: quality and color temperature]. [Camera: angle and lens].
[Style/medium if applicable].
```
*CFG: 4.4 · Steps: 25 · No negative*

### Art Nouveau / Decorative Illustration (Style-First)
```
Art Nouveau [specific sub-style, e.g., "Vienna Secession"] [medium, e.g., "drawing"].
[Subject with decorative details].
[Color palette: limited, jewel-toned, etc.].
[Border or compositional structure if applicable].
```
*CFG: 4.4 · Steps: 25 · Negative: `photo, photorealism, ugly`*

### Product / Commercial Photography
```
[Camera angle and shot type] of [product with exact material specification].
Placed on [surface with material detail]. [Lighting: direction, quality, source].
[Prop or context element if needed]. [Background: specific]. [Style signal].
```
*CFG: 4.4–5.0 · Steps: 25–30 · Negative: `text, watermark` if needed*

### Text Rendering Design
```
[Object type] [reading/showing/displaying] "[EXACT TEXT IN QUOTES]" [font description].
[Material: neon sign, painted wood, carved stone, etc.].
[Setting and environment]. [Lighting that enhances the text].
```
*CFG: 4.4–5.5 · Steps: 30–35 · No negative*

### Turbo Quick Generation
```
[Art style if relevant — 1–2 words] [subject] [key action] [brief environment]
```
*CFG: 1.0 · Steps: 4 · No negative · Keep under 15 words*

---

## Pre-Generation Checklist

**Prompt structure:**
- [ ] Is style/medium at the beginning (not buried at the end)?
- [ ] Is the primary subject in the first 77 tokens (~60 words)?
- [ ] Is spatial ordering logical (subject → near → mid-ground → background)?
- [ ] Are there conflicting style instructions? (resolve before submitting)

**Syntax:**
- [ ] Is desired text in **double quotation marks**?
- [ ] Have all `(keyword:weighting)` syntax been removed?
- [ ] Are artist names replaced with visual descriptions?

**Parameters:**
- [ ] Is CFG set to **4.4** (not SDXL's 7–9)?
- [ ] Is the step count appropriate? (20–25 Large; **4** Turbo; 20–30 Medium)
- [ ] Is variant appropriate? (Large=quality, Turbo=speed, Medium=LoRA/consumer)

**Negative prompt:**
- [ ] Is it minimal (5 words or fewer if used)?
- [ ] Is the SDXL standard negative removed?
- [ ] Are only specific observed issues listed?

**Consistency:**
- [ ] Is the seed recorded from any good result?
- [ ] Is the style description verbatim-identical across related generations?
- [ ] Are CFG and step count consistent across the series?
