# Qwen-Image-2.1 — Continuity & References

The open pipeline has no generation IDs, sessions or threads. **Continuity is carried by the images you pass back in and by a locked recipe.** Seeds help only when every other variable is also fixed.

## 1. Housekeeping

- Save every keeper as **PNG** (alpha, lossless text, clean re-edits).
- Library folders: `identity/`, `wardrobe/`, `products/`, `locations/`, `style/`, `approved-shots/`.
- Store with each keeper: prompt, rewritten prompt (if a PE model ran), seed, `width`×`height`, steps, `true_cfg_scale`, precision, backend, reference list in order, `use_kv_cache`.

## 2. Lock the Recipe

A same-seed rerun only matches when all of these match:

| Locked | Why |
|---|---|
| seed (`generator`) | noise basis |
| `width` / `height` | different size = different sample |
| `num_inference_steps` / `sigmas` | schedule |
| `true_cfg_scale` (+ negative) | guidance path |
| dtype (bf16 etc.) and backend (Diffusers / ComfyUI / hosted) | numerics |
| reference images **and their order** | attention reads in list order |
| `use_kv_cache` | toggling changes the bf16 sample visibly |
| prompt enhancer on/off | rewrites change everything |

Hosted `qwen-image-2.1-pro`: set `promptExtend: false` and a fixed seed when reproducibility matters.

## 3. Reference Ordering and Roles

`image=[identity, outfit, scene]` → `<image1>` identity, `<image2>` outfit, `<image3>` canvas. Keep the **same slot for the same role** across the whole project.

| Slot (suggested) | Role |
|---|---|
| `<image1>` | Identity master **or** the canvas being edited (ComfyUI treats `image_1` as the edited image) |
| `<image2>`–`<image3>` | Wardrobe, full-body proportions, product |
| `<image4>`–`<image5>` | Location / set canvas |
| `<image6>` | Style frame — palette, light, texture only |
| `<image7>`+ | Props, secondary characters (max 10 total) |

Every image gets a role sentence. Drop any reference without one.

## 4. Character Consistency Protocol

1. **Identity pack:** clean close-up, three-quarter portrait, full body — consistent hair, costume, age, proportions; neutral even light, plain backdrop, 3:4 or 1:1 at 2K.
2. Keep the hero identity image in the **same slot** every shot.
3. **Point, don't redescribe.** "The person from <image1>, preserving exact facial identity, hairstyle, skin tone and body proportions." Qwen's edit guidance: identity should be anchored to a reference, not rebuilt in words — verbal faces drift.
4. A short costume line is fine where no wardrobe ref exists ("charcoal flight jacket, orange shoulder patch").
5. State what may change (pose, expression, camera, action) and what holds (face, hair, proportions, markings).
6. One major variable per request.
7. For a small change (expression, eyeline, prop state) **edit the approved frame** instead of regenerating the shot.

## 5. Product / Logo Consistency

- Product ref as its own slot: "Preserve the exact shape, label layout, logo, colours and material of the bottle from <image2>."
- Quote any label copy that must remain legible.
- Place into a canvas: "Match <image3>'s perspective, contact shadows and colour temperature."

## 6. Style Lock

Reusable block pasted verbatim into every prompt (put it in the closing sentence):

```
The overall composition reads as desaturated near-future realism: practical sets,
cool cyan interiors, amber hazard lights, natural skin texture, subtle 35 mm grain,
matte surfaces.
```

Stronger: add one approved style frame and restrict it — "Take only the palette, contrast and lighting quality from <image4>; preserve the layout and identity from <image1>."

## 7. Shot Manifest (multi-shot / storyboard)

Qwen-Image-2.1 does not enforce temporal or camera continuity — you do.

| Locked field | Example |
|---|---|
| Character source | `mara_identity_v4.png` first in every list |
| Costume | charcoal flight jacket, orange shoulder patch, black utility trousers |
| World style | style-lock block above |
| Frame | 2752×1536 (16:9) |
| Inference | 40 steps, CFG 1.0, KV cache on, bf16, same backend |
| Lens language | 35 mm wides, 50 mm mediums, 85 mm close-ups |
| Screen direction | left-to-right until the continuity cut |
| Colour script | cyan interiors, amber exterior hazards |

**Shot template:**
```
A wide horizontal film still, [shot size, camera height, lens]. The person from <image1>,
preserving exact facial identity and hairstyle, [action + screen direction] inside the
[location] from <image2>. [Lighting sentence matching <image2>]. [Style-lock sentence].
```

Branch each new shot from the cleanest master. Use the previous approved frame as the canvas only when the shot is a direct continuation.

## 8. Edit Chains

- Edit from the saved approved PNG; pass explicit `width`/`height` equal to the source (or let it follow the source ratio at a known `output_resolution`).
- One operation per pass; one broad preserve clause.
- After 3–4 chained edits, regenerate from the master with all accumulated changes stated once — chains accumulate softness and drift.
- For region-bound changes, mark the region (circle/paint/mask) instead of describing location in words.

## 9. Outpainting / Reframing

Pass the source and the new target `width`/`height`; describe what appears in the new area and preserve the original subject, light and perspective. In ComfyUI with `custom_size` on, keep the canvas close to the resized `image_1` size or the edit may shift.

## 10. Handoff to Video

Qwen-Image-2.1 outputs stills only. Use it for identity masters, style frames and **first/last keyframes**; describe the midpoint or end pose of a move as a single frame. Put duration, FPS, camera travel and motion intensity into the image-to-video model's prompt and parameters, never into the Qwen call. Generate all keyframes with the same identity ref, style lock, lens language and screen direction so the video model inherits consistent anchors.
