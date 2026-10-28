# Tripo P1 — Best Practices

## 1. Think in Volumes, Not Pictures

P1 builds a mesh. Describe what a modeller would block out — volume, silhouette, thickness, part relationships — not a beauty shot.

| Weak | Better |
|---|---|
| `a breathtaking cinematic robot` | `a squat cylindrical service robot, body twice as wide as its head, three-wheel base` |
| `cool sword` | `a broad single-edged sword, blade tapering to a clipped point, thick square crossguard, wrapped grip` |
| `cute house` | `a tall narrow timber cottage, steep gable roof overhanging the walls, one round chimney, recessed door` |
| `epic tree` | `a stylized oak with a thick twisting trunk and three rounded canopy clumps, exposed roots forming a flat base` |
| `dramatic lighting, 35mm lens` | *(delete — render language, not mesh language)* |

Primitive vocabulary steers geometry: **cylindrical, boxy, spherical, tapered, flared, beveled, recessed, stepped, chamfered, domed, faceted, segmented**.

## 2. Silhouette First, Detail Last

At low face counts, silhouette and big part boundaries are everything. Order:

1. Primary object → 2. broad proportions → 3. major components → 4. signature shape feature → 5. style + materials → 6. intended use.

Start with **2–4 defining details**. If the shape is wrong, **remove** words and regenerate — adding adjectives rarely rescues a bad silhouette. Scratches, wood grain, fabric weave, rivets and grime are texture concerns; overemphasising them can bake noise into geometry.

## 3. Use Ratios, Not Intensifiers

| Instead of | Write |
|---|---|
| very long legs | legs about 1.5× torso length |
| huge wheels | four wheels reaching halfway up the body |
| big head | head roughly one third of total height (chibi proportions) |
| tall tower | tower about four times taller than its base width |

Ratios aren't hard constraints, but they cut ambiguity and make seed comparisons meaningful.

## 4. Name Separations Explicitly

Segmentation, material zones, rigging and assembly all benefit from clear part boundaries:

`separate shoulder armour` · `detached backpack mounted close to the torso` · `distinct wheel housings` · `clean gap between grip and guard` · `lid as a separate slab`

But avoid *floating* pieces unless the design needs them. High-risk at low budgets: straps, wires, antennae, thin blades, fingers, horns, chains, hair strands. Thicken ("thick rounded horns"), merge ("hair as one solid sculpted mass"), or drop them.

## 5. Match the Prompt to the Face Budget

| `face_limit` | What the prompt can carry |
|---|---|
| 150–800 | 3–4 big forms. Pure blockout language. |
| 1k–5k | Primary form + 2–3 parts + one signature feature |
| 5k–12k | Add secondary panels, costume layers, modest bevels |
| 12k–20k | Full character with separated armour/clothing; still no micro-detail |

Below 150 (simple) / 250 (complex) Tripo warns quality drops. Need more than 20k → P2 or H-series, not a longer prompt.

## 6. Negative Prompt Hygiene

≤ 255 chars. List **visible or structural** failures only:

```
floating parts, duplicate limbs, fused arms, crossed legs, thin fragile geometry,
text, logo, base plate, background terrain, open lid
```

Don't put style words ("ugly, bad quality") or parameters there. If you need a closed lid, also say "closed lid" positively in the prompt.

## 7. Image & Multiview: The Prompt Is the Reference

Image- and multiview-to-model have **no text field** — prompt craft moves into the reference images.

Reference brief checklist (for whatever image model makes the views, including Tripo's own image task you chain by `task_id`):
- one isolated object, centred, fully in frame, nothing cropped
- plain light-grey or white background, no cast-shadow floor
- even, soft, shadowless studio light (or rely on `delight` with texture v3.5)
- ¾ view for single image (exposes more volume than strict front)
- neutral A-pose / T-pose for characters, limbs clear of the body
- orthographic-feeling views for multiview: same scale, same height, same light across front/left/back/right
- no text overlays, watermarks, motion blur or depth-of-field

Weak or low-res reference → `enable_image_autofix: true`. Texture follows your colours → `texture_alignment: original_image`; texture should follow reconstructed form → `geometry`.

## 8. Composition for 3D

**Characters.** Neutral symmetrical stance, arms slightly away from torso (A-pose), legs apart, simplified hands, clear neck/shoulder gaps. Avoid crouches, crossed limbs, weapons fused into both hands, long coats hiding legs, capes touching the ground. Action happens later via rig + retarget.

**Creatures.** Name leg count and state "clearly separated legs"; tail thick and held away from the body; neutral standing pose. Pick the matching `rig_type` later.

**Props.** One strong central volume; attachments described relative to it; stable flat base; sensible wall thickness; clear material zones (wood body / iron bands).

**Vehicles.** State wheel count and placement, chassis shape, open vs. enclosed cabin, "no driver". Symmetric by default — say so.

**Environments.** Never a whole scene. One modular piece with clear boundaries: `straight wall module`, `corner section`, `arch gateway`, `market stall`, `cliff chunk`, `floor tile`. Add "flat connection faces on both sides", "flat base aligned to the ground", "no surrounding terrain".

**Camera words.** No camera exists. `orbit`, `dolly`, `35mm`, `depth of field`, `golden hour` are wasted characters. View words (front, left, back, right) matter only for references and orientation.

## 9. Geometry / Texture Separation

1. `texture: false` → judge shape.
2. Lock `model_seed` (+ `image_seed` for text) and `face_limit`.
3. Texture: same request with texture on, or `models/texture` on the task_id.
4. Vary `texture_seed` and material wording for variants; `texture_prompt.text` + `style_image` for a targeted restyle.

Material/style words still belong in the original text prompt — they inform the hidden reference image and PBR results — but keep them short.

## 10. Inspect Before Approving

Rotate fully: collapsed backs, fused limbs, holes underneath, asymmetric part placement, thin geometry, internal faces. A front preview (`rendered_image_url`) hides most failures. Wrong far side → multiview, not more prose.

## Common Mistakes

| Problem | Cause | Fix |
|---|---|---|
| Generic blob | Prompt is just "robot" / "chair" | Add silhouette, proportions, 2 parts, material, style |
| Mangled multi-object result | Scene in one prompt | One asset per task; assemble externally |
| Noisy, lumpy surfaces | Wear/grime/scratches in geometry prompt | Simplify; handle surface detail in texture |
| Broken thin parts | Budget too low / parts too slender | Thicken, simplify, or raise `face_limit` |
| Can't reproduce a mesh | Seeds not stored | Archive `image_seed`, `model_seed`, `texture_seed` + prompt + snapshot |
| Texture changes every run | `texture_seed` not locked | Fix `texture_seed` once approved |
| Back of model invented badly | Single front image | Multiview with front + side/back |
| Mis-oriented after rig/convert | `export_orientation` set at generation | Leave unset; orient in `models/convert` |
| `quad=true` → 400 | Quad is P2 only | Drop it, use P2, or `models/convert` `quad: true` |
| Error `1004` | `fast` without texture v3.5 | Add `texture_version: v3.5-20260815` |
| Slow, expensive exploration | `extreme` texture on every draft | Untextured until approved |
| "80,000 faces" request | P1 caps at 20,000 | P2 (50k tri) or H-series |
| Prompt sent to image-to-model | Field doesn't exist | Encode intent in the reference image |
| Rig fails / odd weights | Posed or fused character | Neutral A-pose, separated limbs; run rig-check first |
