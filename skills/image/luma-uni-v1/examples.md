# Luma Uni-1.1 — Example Prompts

All examples sourced from official Luma documentation. Each includes complete JSON, technique notes, and recommended parameters.

---

## Example 1 — Simple Cinematic Landscape (T2I)

**Formula:** Scene + atmosphere + one named aesthetic  
**Source:** Official Luma documentation  
**Model:** `uni-1`

```json
{
  "prompt": "A wide cinematic landscape during a violent storm. Rolling green hills, a lone tree in the foreground, chaotic lighting, dramatic clouds and atmosphere. Photorealistic.",
  "aspect_ratio": "16:9",
  "model": "uni-1"
}
```

**Technique notes:**
- Aspect ratio explicit — 16:9 is correct for cinematic landscape
- "Photorealistic" is used here as a rendering mode instruction, not a quality booster — acceptable when the alternative is illustrative
- "A lone tree in the foreground" is a specific compositional anchor, not a vague description
- "Chaotic lighting, dramatic clouds" — two observable visual properties, not mood language
- No references needed for a pure T2I with no identity requirements

---

## Example 2 — Character Portrait with Reference

**Formula:** CHARACTER role label + preserve instruction + new scene description  
**Source:** Official Luma character-reference pattern  
**Model:** `uni-1`

```json
{
  "prompt": "Use IMAGE1 (woman with short copper-red hair, freckles) as a CHARACTER reference. Preserve her features exactly. Generate a new scene: she is sitting in a softly lit café, morning light, warm tones, cinematic depth of field.",
  "aspect_ratio": "2:3",
  "model": "uni-1",
  "image_ref": [
    { "url": "https://your-cdn.com/character-reference.jpg" }
  ]
}
```

**Technique notes:**
- CHARACTER role declared immediately with brief description of distinguishing features
- "Preserve her features exactly" — explicit instruction to prevent creative drift
- New scene described separately from the character declaration
- Portrait aspect ratio (2:3) appropriate for character focus
- `uni-1` sufficient for single-reference character work; upgrade to `uni-1-max` for higher fidelity

---

## Example 3 — Multi-Reference Architecture (3 Roles)

**Formula:** Multi-role assignment + authority isolation clause + scene description  
**Source:** Official Luma multi-reference pattern  
**Model:** `uni-1-max` (recommended for multi-reference)

```json
{
  "prompt": "Use IMAGE1 as a COLOR PALETTE reference, IMAGE2 as LIGHTING, IMAGE3 as COMPOSITION. Create a lone figure walking through a rain-slicked street at night, 1940s film noir atmosphere, wet reflections on cobblestones. Treat each reference as having authority over its assigned layer only.",
  "aspect_ratio": "1:1",
  "model": "uni-1-max",
  "image_ref": [
    { "url": "https://your-cdn.com/palette-ref.jpg" },
    { "url": "https://your-cdn.com/lighting-ref.jpg" },
    { "url": "https://your-cdn.com/composition-ref.jpg" }
  ]
}
```

**Technique notes:**
- All three references labeled at the start, before the scene description
- "Authority over its assigned layer only" prevents bleed between references
- "1940s film noir atmosphere" is a named aesthetic — provides cultural visual context beyond what the references show
- `uni-1-max` recommended when using multiple references — better constraint resolution
- Square aspect ratio chosen here; adjust based on actual composition reference

---

## Example 4 — Manga Style Generation

**Formula:** Scene description + named aesthetic elements + manga-specific vocabulary  
**Model:** `uni-1`  
**⚠️ Manga requires portrait aspect ratio**

```json
{
  "prompt": "A young warrior stands at the edge of a cliff overlooking a vast ruined city at sunset, dramatic ink outlines, screentone shading on shadows, dynamic action pose, manga panel composition, high contrast black-and-white with selective red ink.",
  "aspect_ratio": "9:16",
  "style": "manga",
  "model": "uni-1"
}
```

**Technique notes:**
- `style: "manga"` activates the manga rendering mode — the prompt describes specific manga vocabulary to reinforce it
- "Screentone shading on shadows" — manga-specific visual technique the model understands
- "Selective red ink" — a specific stylistic choice that won't occur without explicit instruction
- `aspect_ratio: "9:16"` — portrait ratio required; landscape/square with `style: "manga"` returns HTTP 422
- "Dynamic action pose" — composition instruction, not a quality term

---

## Example 5 — Text Rendering (Sign / Label / Surface)

**Formula:** Object + exact quoted text + medium/surface + environment  
**Model:** `uni-1-max` (recommended for text precision)

```json
{
  "prompt": "A vintage neon diner sign reading \"OPEN 24 HRS\" mounted on a brick wall in the rain at night, neon light reflecting on wet pavement, photorealistic, 35mm film grain.",
  "aspect_ratio": "3:2",
  "model": "uni-1-max",
  "web_search": false,
  "output_format": "jpeg"
}
```

**Technique notes:**
- Exact text in quotes — this triggers the text rendering pathway
- The sign is described as a physical object ("neon sign mounted on brick wall"), not just text
- Environment supports the text: rain, night, reflections — provides context for the neon
- "Photorealistic, 35mm film grain" — specific rendering instructions, not vague praise
- `uni-1-max` for text precision
- `output_format: "jpeg"` acceptable here — photo content, not design with sharp text edges
- `web_search: false` — fictional diner, no real-world grounding needed

---

## Example 6 — Web-Grounded Real Location

**Formula:** Real location + specific visual conditions + `web_search: true`  
**Model:** `uni-1-max`

```json
{
  "prompt": "The Shibuya crossing in Tokyo at rush hour during cherry blossom season, aerial view, dawn light, photorealistic, Canon 5D Mark IV quality.",
  "aspect_ratio": "16:9",
  "model": "uni-1-max",
  "web_search": true
}
```

**Technique notes:**
- `web_search: true` — model searches before generating for visual accuracy on the real location
- "Canon 5D Mark IV quality" is used here as a camera/optics reference, not an abstract quality booster — it communicates a specific photographic look
- Cherry blossom season is a specific visual condition, not a vague aesthetic
- Aerial view and dawn light are both specific compositional and lighting instructions
- Widescreen (16:9) appropriate for a city scene with horizontal extent

---

## Example 7 — Image Modification (Lighting Change)

**Formula:** Explicit change instruction + explicit preserve instruction  
**Source:** Official Luma Modify mode pattern  
**Model:** `uni-1`

```json
{
  "type": "image_edit",
  "prompt": "Change the time of day to golden hour. Update the sky, light direction, shadows, and color temperature to match late afternoon. Keep all subjects, composition, and foreground elements unchanged.",
  "model": "uni-1",
  "source": { "url": "https://your-cdn.com/original-photo.jpg" }
}
```

**Technique notes:**
- `type: "image_edit"` — this is Modify mode; structure of source image is preserved
- Change instruction is specific: lists exactly what should update (sky, light direction, shadows, color temperature)
- Preserve instruction is explicit and comprehensive: subjects, composition, foreground elements
- No `aspect_ratio` — inherits from source image
- No `image_ref` — this is a pure lighting modification from text; no style reference needed
- Keep Modify prompts surgical (30–100 words); verbose Modify prompts cause structure drift

---

## Additional Templates

### Standard T2I with Named Aesthetic
```json
{
  "prompt": "[Scene + subject + specific visual details]. [Named aesthetic or cultural tradition]. [Lighting: direction, quality, temperature]. [Camera/composition language].",
  "aspect_ratio": "[ratio]",
  "model": "uni-1"
}
```

### Character Series (Multiple Scenes)
```json
{
  "prompt": "Use IMAGE1 ([distinguishing features]) as a CHARACTER reference. Preserve [specific features] exactly. New scene: [environment and action]. [Camera, lighting, style].",
  "aspect_ratio": "[ratio]",
  "model": "uni-1",
  "image_ref": [{ "url": "[canonical reference URL]" }]
}
```
*Keep IMAGE1 declaration and character description identical across all scenes in the series.*

### Multi-Reference Production (4 Roles)
```json
{
  "prompt": "Use IMAGE1 as a CHARACTER reference, IMAGE2 as STYLE, IMAGE3 as LIGHTING, IMAGE4 as COLOR PALETTE. Treat each reference as having authority over its assigned layer only. [Scene description: environment, action, composition intent].",
  "aspect_ratio": "[ratio]",
  "model": "uni-1-max",
  "image_ref": [
    { "url": "[character ref]" },
    { "url": "[style ref]" },
    { "url": "[lighting ref]" },
    { "url": "[palette ref]" }
  ]
}
```

### Surgical Modify
```json
{
  "type": "image_edit",
  "prompt": "Change only [specific element]. Update [what changes with it]. Keep [comprehensive list of invariants] exactly unchanged.",
  "model": "uni-1",
  "source": { "url": "[source image URL]" }
}
```

### Web-Grounded Factual Subject
```json
{
  "prompt": "[Real-world location or subject with specific conditions]. [Specific time of day, season, or event]. [Camera/composition]. [Rendering style].",
  "aspect_ratio": "[ratio]",
  "model": "uni-1-max",
  "web_search": true
}
```

---

## Pre-Flight Checklist

Before submitting any Uni-1.1 generation:

**Mode selection:**
- [ ] Is this Create (`"image"`) or Modify (`"image_edit"`)?
- [ ] If Modify: is `source` present? Is `image_ref` excluded unless needed for style reference?

**Prompt quality:**
- [ ] Is the primary subject described specifically (not vaguely)?
- [ ] Are there any negative instructions? (Convert to positive if yes)
- [ ] Are there conflicting instructions? (Resolve before submitting)
- [ ] Is redundant phrasing removed?
- [ ] Are vague quality terms removed ("beautiful," "amazing," "masterpiece")?

**References:**
- [ ] Does every reference have an explicit role label?
- [ ] Is "Treat each reference as having authority over its assigned layer only" included (for multi-reference)?
- [ ] Are reference URLs publicly accessible and under 50 MB each?
- [ ] Is reference count ≤ 9 (Create) or ≤ 8 (Modify)?

**Parameters:**
- [ ] Is aspect ratio set (or intentionally left null)?
- [ ] If `style: "manga"` — is aspect ratio portrait (`2:3`, `9:16`, `1:2`, `1:3`)?
- [ ] Is model tier appropriate (`uni-1-max` for multi-reference, text, or detail-critical work)?
- [ ] Is `web_search: true` set for real-world factual subjects?
- [ ] Is `output_format: "png"` set for designs with text or sharp edges?

**Production:**
- [ ] Will output URL be downloaded promptly (expires in 1 hour)?
- [ ] Is seed recorded (or intentionally left random for exploration)?
