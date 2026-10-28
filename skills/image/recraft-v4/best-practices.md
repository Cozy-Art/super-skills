# Recraft V4 — Best Practices

## 1. Detail Level: Match Prompt Length to Intent

| Situation | Approach |
|---|---|
| Exploring a direction | 3–15 words; let V4 / V4.1 decide composition and styling |
| More than one subject, strict placement, exact text, brand palette | Short labelled sentences, one job each |
| Reproducible art direction / series | Fixed skeleton: identity block + style block + variable shot block |

Structure buys **intentionality and repeatability**, not automatic beauty. Add constraints only where the output drifts.

Concrete visual facts beat adjective piles:

| Weak | Better |
|---|---|
| `epic, cinematic, stunning` | `single hard light from upper left, black background, silver reflections` |
| `high quality product shot` | `slightly top-down 35-degree view, centered hero object, controlled specular highlights, seamless background` |
| `beautiful landscape` | `24 mm wide-angle look, low viewpoint, basalt foreground, river leading line, ridges layered into haze` |
| `modern logo` | `bold geometric monogram, two flat fills, consistent corner radius, reads at 24 px` |
| `vintage` | `faded 1970s colour-negative look, visible grain, cool green shadows` |

## 2. What to Emphasize

- **Count:** "exactly three bottles", "one cyclist".
- **Spatial relationships:** "bottle centered; sliced lime in the lower-left foreground".
- **Framing:** "chest-up", "full body", "90-degree top-down", "subject in the right third".
- **Light behaviour:** direction, softness, colour temperature, contrast, reflections.
- **Material behaviour:** matte ceramic, brushed aluminium, translucent acrylic, coarse wool.
- **Palette:** 2–4 named colours; reinforce with `controls.colors` when exactness matters.
- **Typography:** quoted copy, largest vs secondary, alignment, crop, overlap, readability.

Put the decisive noun and medium first: `editorial photograph`, `flat vector icon set`, `3D product render`, `large-format poster`.

## 3. Exclusions Without a Negative Prompt

V4 has no `negative_prompt`. Describe what fills the space first; add one short exclusion clause at the end only for what genuinely matters.

| Instead of | Write |
|---|---|
| long "no…" list | positive target + "No text or logos." |
| no crowds | an empty platform, one distant figure |
| no clutter | plain seamless warm-gray backdrop |
| no gradients (vector) | flat solid fills only |

A long exclusion list competes with the target and can pull excluded concepts in.

## 4. Composition and Camera Language for Stills

Recraft has no camera parameters; write the **visual consequence**, not the camera verb.

| Weak | Better |
|---|---|
| `camera pans with cyclist` | `side-on panning-shot aesthetic; face and torso sharp, wheels and background streaked horizontally` |
| `dolly in` | `intimate close framing, strong perspective, shallow depth, foreground edges out of focus` |
| `orbit around product` | `three-quarter product view, curved highlight travelling across the metal body` |

Shot recipes:
- **Portrait:** `eye-level medium close-up, 85 mm portrait look, shallow depth, subject on right third, clean negative space left`.
- **Environment:** `24 mm wide-angle look, low viewpoint, foreground anchor, leading line, layered haze`.
- **Action:** direction of travel + decisive instant + where blur is and isn't.
- **Wide ratios (`2:1`, `16:9`):** give both sides of frame a job. **Tall (`1:2`, `9:16`):** stack depth vertically.

Format-specific orders:

| Use case | Order |
|---|---|
| Character / photo | medium → identity → pose → environment → framing → light → lens/depth → mood |
| Landscape | environment + scale → fg/mg/bg → weather → light → viewpoint → palette |
| Poster / cover | format → background → image layer → headline hierarchy → exact text → placement → overlap → finish |
| Logo / vector | graphic type → silhouette logic → palette → fill/stroke rules → grid/spacing → scalability → exclusions |
| Product / 3D | render type → geometry → materials → placement → light → camera → background → colour system |

## 5. Typography

- Quote every visible string: `headline reads "FORM / LIGHT"`.
- State hierarchy (largest / secondary / tertiary), position ("spans the top edge, slightly cropped", "vertical along the right edge"), type character ("condensed uppercase", "geometric sans"), colour.
- Describe interaction: "the sculpture overlaps the lower edge of the headline without obscuring readability".
- Keep generated copy to a headline + one or two short lines; add body or legal copy in a design tool.
- There is no `text_layout` on V4 — placement is prose only. Use Pro for cleaner letter edges at print size.

## 6. Vector Discipline (`_vector` models)

- Lead with graphic type: "flat vector icon", "monoline badge", "geometric monogram".
- Control with **geometry**: silhouette, corner radius, stroke logic ("uniform stroke weight"), grid, spacing, negative space.
- Fix the colour count ("strict two-colour system: deep navy and warm coral on white") and back it with `controls.colors`.
- State scalability: "remains recognizable at 24 pixels".
- Drop raster vocabulary as primary control — lens, bokeh, film grain, subsurface skin.
- Exact counts and grids ("exactly six icons in a 3 × 2 grid") work better than "a set of icons".

## 7. Brand Colour

- Named colours in prose + `controls.colors` RGB with weights (dominant colour highest).
- `controls.background_color` for flat backdrops.
- Treat both as strong preferences; style references do not guarantee exact colour. Validate hex values in output before approval.

## 8. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| No `model` set | Runs on V4.1 (or V4 Styles) | Set `model` every request |
| Sending `negative_prompt` / `text_layout` | Error or silently ignored | Positive prompt + prose layout |
| Important object buried late | Missing object | First sentence, with count + placement |
| Vague relationships | Composition drift | Thirds, fg/mg/bg, gaze, overlap, negative space |
| Unquoted or long copy | Misspelling | Quote short text, state size + location |
| Adjective stack | Generic "AI" look | Medium + material + light logic |
| Conflicting media | Incoherent render | One medium; assign any second treatment to a layer |
| Pronouns with two subjects | Traits swap | Repeat names / descriptors |
| Raster texture in vector prompt | Messy SVG | Geometry, fills, stroke rules |
| Style fields on Flash | Request fails | Text-to-image only |
| `style_id` + references together | Rejected | Pick one |
| Style fields on `/imageToImage` | V3-only | Drop them; describe style in prompt |
| Seed reused with other changes | Different image | Seed only holds when everything else matches |
| Paying Pro for exploration | 6× cost | Explore on Flash/V4, finish on Pro |
