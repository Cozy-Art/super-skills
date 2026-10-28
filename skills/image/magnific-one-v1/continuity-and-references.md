# Magnific One — Continuity & References

Magnific One has no seed, no identity/face reference parameter, no Draft-tile ID and (in the API) no source-image field. **Continuity is carried by four things you hold constant:** the prompt skeleton, the style references, the Brand Kit (app), and the aspect ratio.

## 1. Housekeeping

- Download every keeper as soon as the task completes (URL lifetime is not documented).
- Keep a project library: `style-refs/`, `brand/`, `identity/`, `approved/`.
- Save the exact prompt, settings line and reference URL list with each approved image. Host style references at stable public URLs — the API fetches them.

## 2. Draft → Final Handoff

Draft explores; it does not hand a tile to Final. There's no public "promote tile" parameter.

1. Draft at the **final aspect ratio**, 16 tiles if shape matters.
2. Choose one tile. Write down what makes it work: subject placement, viewpoint, crop, light direction, palette, negative space.
3. Final prompt = the Draft prompt **+ those traits stated explicitly**, same `reference_images`, same ratio.
4. Optionally add the chosen tile to `reference_images` — but note the API treats references as **style**, so it carries look and palette more reliably than exact layout.

```
Draft:  Poster concepts for a jazz festival by the sea.
Final:  Minimal bold poster for a jazz festival by the sea. A lone upright bass
        silhouetted on a pier at the lower left, a huge low moon filling the
        upper right, wide band of empty navy sky between them. Cobalt, cream and
        brass palette, screen-printed texture.
```

## 3. Style References

| Surface | How | Count |
|---|---|---|
| App | **Style** tab (or pick a built-in Magnific style). Images added as normal references are read as **content**, not a look | 1–5 |
| API | `reference_images` — described as style guidance, both modes | 1–10 URLs |
| App + Brand Kit | Reference images alongside the kit | up to 5; ~2 usually best |

- Choose a **coherent** set: shared palette, texture or technique. Mixed references send a mixed signal.
- Keep the same set, **in the same order**, for a whole series.
- Once the style is carried by references, write the prompt around the **scene** — who, doing what, where. Don't restate the look in words.
- Styles carry through both Draft and Final.

## 4. Brand Kit (app)

- Built once in Library → References → Brand Kit from a website URL, PDFs/images/ZIP, and/or a written description. Magnific proposes palette, imagery style, tone and typography rules; you review test images and mark on/off-brand.
- **Applies only in Final** with Magnific One. Draft explores freely.
- Marking an image off-brand becomes a permanent rule. Kits can include channel templates (aspect ratio + safe zones) and are shared per project or team member.
- Strongest at direction (colour, mood, style, composition). **Not** a guarantee of exact typography, exact colour values or pixel-precise placement — finish those in Auto Layers / Designer.
- Not a documented API field. For API series, approximate it with a fixed style-reference set plus a palette sentence.

Division of labour: **Brand Kit = brand identity · Style refs = rendering look · Prompt = scene content.** Don't duplicate one in another.

## 5. Character Consistency

No identity parameter exists. Use this hierarchy:

1. A **verbatim identity block** — the same sentence in every prompt:
   ```
   Mara, a woman in her early forties with an oval face, warm brown skin, short
   tightly curled black hair, a small scar through the left eyebrow, and a brass
   crescent earring.
   ```
2. Same style references and Brand Kit.
3. Same medium, palette, lighting logic and aspect ratio.
4. Change only the **shot / action / environment** block.
5. In the app, an approved character image can be attached as a content reference (normal reference, not Style).
6. Iterate one change at a time; small single-variable edits are the most predictable.

Expect some drift — this is prompt-and-reference continuity, not locked identity.

## 6. Series Bible

Keep it outside the prompt; paste the fixed parts verbatim, append only the variable parts.

```
MEDIUM:      editorial film photography
CHARACTER:   [identity block, verbatim]
WARDROBE:    charcoal field jacket, rust-orange collar
PALETTE:     charcoal, rust, cold blue-gray
LIGHT:       soft source from camera-left; warm practical behind
STYLE REFS:  [same ordered URL list]
BRAND KIT:   [same project kit, Final only]
RATIO:       3:4
TEXT RULE:   No other logos or text.
---- per image ----
SHOT / ACTION / ENVIRONMENT
```

Rewriting the whole prompt each time causes gradual style and identity drift.

## 7. Multi-Image Sets (campaigns, carousels)

- Draft the **hero** first; derive the rest from its Final prompt.
- Lock ratio per placement (e.g. `3:4` feed, `9:16` story, `3:1` banner) and Draft each placement at 16 tiles — recomposition across ratios is a new composition, not a crop.
- Keep screen direction and light direction consistent across the set.
- For wide placements, leave explicit negative space for copy, then set copy in Designer.

## 8. Still → Video Handoff

Magnific One has no image-to-video mode. Use the approved still as the **start frame** (optionally a second still as the end frame) in Magnific's Video Generator or any image-to-video model. Available frame options depend on the chosen video model.

Prompt only what moves — the still already carries look, identity and composition:

```
The woman takes one slow breath and turns her eyes toward the arriving train.
Her body remains nearly still. A subtle handheld camera drifts forward a few
centimeters. Coat fabric moves lightly in the platform breeze. Preserve her
face, wardrobe, lighting and background architecture. No cut.
```

For two-frame handoffs, generate both stills from the same series bible so the video model interpolates between consistent anchors.
