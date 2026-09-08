# GPT Image 2 — Best Practices Guide

---

## The Core Discipline: Visual Facts Over Vague Praise

GPT Image 2's reasoning layer can plan complex compositions — but only if the prompt gives it visual facts to work with, not emotional language.

**Replace vague praise with specific visual targets:**

| Weak | Strong replacement |
|------|-------------------|
| "stunning" | specific lighting: "overcast daylight, soft window fill" |
| "cinematic" | specific effect: "natural subject separation, soft depth falloff" |
| "epic" | specific composition: "low-angle wide shot, foreground silhouette" |
| "minimal/modern/premium" | visual specifics: "cream background, heavy black condensed sans serif, one hero object, generous negative space" |
| "masterpiece, ultra-detailed, 8K" | no equivalent needed — describe material instead: "brushed aluminum, worn canvas, wet concrete" |

**Note:** The word `"photorealistic"` is an exception — it **does** meaningfully activate the photorealistic rendering mode. Include it explicitly when you want a real-photo look.

---

## Anti-Slop Rules (7 Rules)

1. **Visual facts over vague praise** — Replace quality boosters with observable visual properties

2. **Style tags need visual targets** — Don't write `"minimalist brutalist editorial luxury"`; write `"cream background, heavy black condensed sans serif, asymmetrical type block, one hero object, generous negative space"`

3. **Say the real thing** — If the image must show a transit kiosk, write `transit kiosk`. If it must contain a readable boarding pass, write `boarding pass with legible text`

4. **Treat text like typography** — Wrap literal text in quotes or ALL CAPS, specify font style/size/color/placement, add `"no extra words"` and `"no duplicate text"` to Constraints

5. **One revision per turn** — Small iterative edits outperform one giant rewrite in a single prompt

6. **Include `"photorealistic"` explicitly** when you want a real-photo look — this word meaningfully activates the photorealistic rendering mode

7. **Avoid camera physics jargon** — Instead of `"85mm, f1.4, cinematic bokeh"`, describe the visual effect: `"natural subject separation, soft biological depth falloff, atmospheric perspective"`

---

## What to Emphasize by Element

### Lighting
- Direction: camera-left/right, overhead, backlit, side-lit, rim light
- Quality: hard/direct, soft/diffuse, dappled, incandescent, fluorescent, available light
- Temperature: warm amber, cool blue, golden hour, blue hour, north window
- Mixed sources: "incandescent work lamp spilling warm light against cool morning exterior"

### Material and Texture
Name specific surfaces — not "realistic texture":
- brushed aluminum, worn canvas, wet concrete, papery garlic skins, chipped porcelain
- fabric: linen, ribbed knit, heavy denim, satin, worn leather
- surface wear: scuffs, fingerprints, patina, rust, salt stains

### Composition
- Framing: close-up, medium, wide, extreme close-up
- Viewpoint: eye-level, low-angle, overhead, bird's eye, worm's eye
- Focal-length feel: "35mm feel," "50mm feel," "telephoto compression"
- Not: "85mm f1.4" (camera jargon) → use "soft background separation, natural perspective"

### People
Always specify:
- Scale and body framing: "full body visible, feet included" or "waist-up portrait"
- Gaze direction: "direct gaze at camera," "looking off-frame left"
- Hand position: "hands naturally gripping handlebars," "hands in pockets"
- Object interaction: what they're holding, touching, operating

### Text and Typography (Critical)
- Wrap text in quotes: `"OPEN 24 HOURS"`
- Or write in ALL CAPS: `OPEN 24 HOURS`
- Specify: font style, size relative to layout, color, placement, alignment
- Spell out hard-to-spell words letter-by-letter if critical
- Add to Constraints: `"no extra words, no duplicate text, no text artifacts"`
- Use `quality: "high"` + `thinking: "medium"` minimum for text-heavy layouts

### UI and Mockups
Specify explicitly:
- Screen type: mobile portrait, desktop wide, tablet landscape
- Exact copy in quotes (everything that must be readable)
- Hierarchy: H1, subheading, body, button label
- Widget state: button default/hover/pressed, toggle on/off, loading
- Spacing descriptor: "clean spacing, 24px gutters" or "generous negative space"

---

## Composition Techniques by Content Type

### Documentary / Editorial Photography
- Name the lens feel: "35mm feel," "50mm feel"
- Name the light source: "incandescent work lamp," "north window light," "overcast daylight"
- Name surface wear: "worn wooden table," "chipped porcelain bowl"
- Name believable imperfections: "realistic skin texture," "every wrinkle visible"
- Avoid: commercial styling, heavy retouching, stock-photo poses

### Product Photography
- Inventory every physical object that appears
- Material accuracy: name the exact material ("matte ceramic," "brushed stainless")
- Lighting consistency: where is the key light, is there a fill, is there a rim?
- Label fidelity: if the label text matters, quote it explicitly
- The "use case" slot tells the model the finish level: `"product mockup"` vs. `"commercial product ad"`

### UI / App Mockups
- Specify screen type first
- Write exact copy in quotes for every readable element
- Specify hierarchy (what's H1, what's a button)
- Specify widget state (button active/inactive, checkbox checked)
- Add: `"clean spacing"`, `"exact readable copy"`, `"no placeholder text"`
- Use `thinking: "medium"` minimum

### People in Scenes
- Always specify gaze direction
- Always specify full-body visibility intent or crop level
- Always specify hand/object interactions
- Prevents: proportion errors, alignment artifacts, hands floating away from objects

---

## Common Mistakes and Fixes

| Mistake | Fix |
|---------|-----|
| Garbled small text in output | Switch to `quality: "high"`; use `thinking: "medium"` or higher |
| Character/scene drift across iterations | Use "change only X" + "keep everything else the same" + repeat the preserve list each turn |
| Extra unwanted text in image | Add "no extra words, no duplicate text, no watermark" to Constraints |
| Living artist name blocks generation | Replace with style description: use "Ghibli" style, not "Hayao Miyazaki" |
| Noise artifacts in complex sessions | Restart the session (reload the page) — artifact amplification is a known bug tied to session image data reuse |
| Transparent background not working | `gpt-image-2` does not support `background: "transparent"` — generate on opaque background and apply background removal as post-processing |
| Identical images appearing in same session | Restart session — images in the same session share style/seed context |
| Response URL expired | Copy to own S3/CDN immediately — URLs expire in 1 hour |
| Using `standard` quality for UI/text work | Always use `quality: "high"` for any prompt with labels, icons, or UI copy |
| Overloaded prompt (500+ words) | Split into Six-Element structure; use `thinking` to handle complex constraints instead of cramming into prompt |
| "Same style as before" in edit | Describe the visual language explicitly: name the color palette, brushwork, line weight, palette |
| Camera physics jargon (85mm f1.4) | Describe the visual effect instead: "soft background separation, natural perspective" |
| Mood language burying the brief | Replace "a feeling of solitude" with "a person sitting alone on a bench, back to camera, empty park behind them" |

---

## Syntax Rules

- **Prompt length:** Hard max 32,000 characters; practical recommended under 500 words / a few hundred tokens
- **Past a few hundred tokens**, the model may deprioritize earlier instructions. Solution: `thinking` parameter, not a longer prompt
- **Line breaks** between sections improve readability and parsing for complex prompts
- **Repeat key constraints** — repeating a constraint strengthens adherence
- **In ChatGPT** (not API), use `(don't change the prompt, send it as it is.)` to suppress automatic prompt enhancement when testing exact prompts
- **Label reference images by role** when using the edit endpoint: `Image 1: base scene. Image 2: jacket reference.`

---

## Known Limitations

| Limitation | Status | Workaround |
|-----------|--------|------------|
| No transparent background | Confirmed — not supported | Post-process with background removal |
| Noise pattern amplification in sessions | Known bug, no prompt fix | Restart session / reload page |
| Identical images in same session | Related to above | Restart session between generations |
| Knowledge cutoff: December 2025 | Hard limit | Provide reference images for post-cutoff subjects (logos, products, events) |
| Living artist name triggers moderation | Known behavior | Use style descriptions instead of artist names |
| 4K output variable quality | Experimental above 2K | Use 2K as reliable ceiling; upscale externally |
| `input_fidelity` parameter unsupported | By design | Parameter is disabled; always processes at high fidelity |
| Web search for current visuals | Available but not always triggered | Mention the subject explicitly as a real-world reference |
