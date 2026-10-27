# Recraft V4 — Continuity & References

Every generation request is independent — Recraft does not remember prior images. Continuity is carried by four tools: **identical text blocks, fixed request settings, style references / `style_id`, and image-to-image from an approved keeper.** There is no character-reference or face-ID parameter.

## 1. Housekeeping That Makes Continuity Possible

- Download keepers promptly — response URLs are temporary (~24 h). `multipart` or `b64_json` avoids the extra fetch.
- Store the **full request body** with each file: prompt, `model`, `size`, `random_seed`, `controls`, `style_id`, `style_match`, and source-image checksum + `strength` for image-to-image.
- Folders: `identity/`, `style/`, `palettes/`, `approved/`.

## 2. Seeds

`random_seed` reproduces an image only when model, size, prompt, controls and style are all identical. Changing any one — including moving from V4 to Pro, or 4:5 to 3:4 — can shift composition substantially. Use the seed for re-rolls and A/B wording tests, not as an identity lock.

## 3. Character Consistency Protocol

1. Approve one hero portrait on `recraftv4` (neutral light, clear face, signature wardrobe).
2. Write an **identity block** and paste it verbatim into every prompt:
   ```
   Mara: woman in her early 40s, oval face, warm brown skin, short tightly
   curled black hair, small scar through the left eyebrow, dark green eyes,
   brass crescent earring in the right ear, charcoal field jacket with a
   rust-orange collar.
   ```
   Keep age, facial geometry, hair, one distinctive mark and signature wardrobe stable. Scene action goes after the block.
3. For new shots, feed the hero into `/imageToImage` at `strength` 0.15–0.35 and describe only the change ("now standing beside the train window at dawn").
4. Keep model, ratio, palette controls and light direction fixed until a deliberate scene change.
5. Render close-up finals on `recraftv4_pro` only after continuity is stable.

## 4. Style Consistency

| Tool | When |
|---|---|
| `style_reference_urls` (1–10 images) | One-off series from references; response returns a reusable `style_id` (+$0.005) |
| `style_id` | Reuse a saved style across every request in a series |
| `POST /styles` | Create a named reusable style up front ($0.005) |
| `recraftv4_styles` (+ `_pro`) | Dedicated style-driven tier; always needs a style; cheaper vectors |
| Prose style block | Flash, image-to-image, or when no reference exists |

Rules:
- **One clean, high-resolution reference** usually gives the clearest signal; multiple refs only if they share one visual system.
- Reference controls line weight, colour logic, texture and rendering; **the prompt controls subject, scene, composition and pose.** Don't re-describe the style in prose when a reference supplies it.
- `style_match: "precise"` for strict rendering/lighting/texture match; `"flexible"` (default) for the same direction with variation.
- Never combine `style_id` with references (rejected). Styles don't run on Flash, and style fields on `/imageToImage` are V3-only.
- A style created for `recraftv4_styles` is bound to that model — test before mixing tiers.
- Style matching does not guarantee exact brand colour — add `controls.colors`.

**Style block** for when references can't be used:
```
STYLE: flat editorial illustration, bold geometric shapes, thick uniform
outlines, limited palette of deep navy, warm coral and off-white, subtle
paper grain, generous negative space.
```

## 5. Series Bible / Storyboard

Lock: `model`, `size`, identity block(s), wardrobe, palette controls, light direction, environment anchors, `style_id`, seed policy, reserved text/UI zones.
Change only the **shot block**: framing, action, viewpoint, expression, screen direction.

```
[SHOT: medium two-shot, eye-level, 50 mm look, subjects moving left-to-right].
[IDENTITY: Mara block]. [ACTION]. [ENVIRONMENT ANCHORS].
[LIGHT: soft overcast from camera-left]. [STYLE block or style_id].
```

- One moment per image; contact sheets only when asked.
- Use the previous approved frame as the image-to-image source when continuity beats novelty.
- Branch from the cleanest keeper — chained image-to-image passes accumulate drift.

## 6. Brand Systems

1. One reference (or a tight set) → one `style_id`.
2. `controls.colors` with weights + `background_color` locked in a shared payload template.
3. Prompt skeleton fixed; only subject and composition vary.
4. Vectors: same corner radius, stroke logic and colour count stated in every prompt; generate icons in one gridded request for internal consistency.
5. Validate typography and hex values outside the model before publishing.

## 7. Tier Handoff

- **Flash → V4:** Flash has no references; carry over only the rewritten prompt, size, seed and controls. Expect a new image — Flash is a screening tier, not a draft of the V4 image.
- **V4 → Pro:** a new render, not an upscale. To keep a 1K composition at 2K, use `/imageToImage` with `model: recraftv4_pro` and low `strength` (≈0.1–0.2) *(behaviour unverified — test)*, or the separate upscale/enhance tools.
- **Raster → SVG:** regenerate on a `_vector` model with geometry-led prompt, or use the vectorize tool on a flat raster keeper.

## 8. Handoff to Video

Recraft V4 outputs stills only. Approved frames make good first/last keyframes for any image-to-video model — generate them with the same identity block, style and screen direction so the video model inherits consistent anchors.
