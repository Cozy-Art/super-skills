# Tripo P1 — Continuity & References

In 3D, continuity means an **asset library that looks like it came from one studio**: shared shape language, materials, face-budget classes, scale, orientation and topology — plus the ability to regenerate or extend any asset exactly. P1 gives you three tools for this: **pinned snapshots, layered seeds, and task-ID chaining**.

## 1. Housekeeping That Makes Continuity Possible

- Pin `model: "P1-20260311"` and, when texturing, `texture_version` (e.g. `v3.0-20250812` or `v3.5-20260815`). Geometry and texture versions are versioned separately — pin both.
- Download every approved GLB and preview into your own store; treat Tripo URLs as temporary.
- Keep a library: `style-bible/`, `refs/<asset>/front|left|back|right.png`, `meshes/`, `textured/`, `rigged/`, `exports/`.
- Per asset, archive a manifest:

```json
{
  "asset": "crate_wood_small",
  "task_id": "task_...",
  "model": "P1-20260311",
  "prompt": "...", "negative_prompt": "...",
  "image_seed": 41277, "model_seed": 731902, "texture_seed": 91824,
  "face_limit": 1200, "texture_version": "v3.0-20250812",
  "texture_quality": "standard", "pbr": true, "auto_size": true,
  "refs": ["sha256:..."], "downstream": {"rig": "task_...", "convert": "task_..."}
}
```

## 2. Seed Layering

| Seed | Controls | Exists on |
|---|---|---|
| `image_seed` | Hidden text-to-image reference that drives the mesh | text-to-model only |
| `model_seed` | Geometry | all three generation endpoints |
| `texture_seed` | Texture | generation endpoints + `models/texture` |

Same input + same `model_seed` → same mesh (per Tripo). For text-to-model, also hold `image_seed`, since it shapes the reference the mesh is built from.

| Goal | Hold | Vary |
|---|---|---|
| Exact regeneration | prompt, all seeds, snapshot, all params | nothing |
| Same mesh, new materials | prompt, `image_seed`, `model_seed`, `face_limit` | `texture_seed`, material words — or use `models/texture` |
| Same design, different budget | prompt, seeds | `face_limit` (expect shape drift — re-inspect) |
| New silhouette candidates | prompt | `model_seed` (and `image_seed`) |

Changing the prompt text changes the input, so seeds stop guaranteeing identity. For material variants on an approved mesh, prefer **`models/texture` on the task_id** over regenerating — geometry is then untouched by definition.

## 3. The Style Bible (style lock block)

Write it once; paste it **verbatim** at the end of every prompt in the set.

```
STYLE BLOCK — "Ember Coast" kit:
stylized low-poly PBR game asset, rounded bevelled edges, broad readable shapes,
matte hand-painted surfaces, warm sandstone and driftwood palette with teal accents
```

Alongside it, fix per kit:

| Lock | Example |
|---|---|
| Shape language | rounded bevels, chunky proportions, no sharp spikes |
| Material vocabulary | "weathered driftwood", "sun-bleached sandstone", "verdigris copper" — reuse exact phrases |
| Detail density | 2–3 parts per prop; no micro-detail |
| Face-budget class | small prop 800–1.5k · large prop 3–5k · hero 8–12k · character 12–18k |
| Texture | same `texture_version`, same `texture_quality` tier for finals |
| Scale | `auto_size: true` for every asset, or none — never mixed |
| Orientation | unset at generation; one `export_orientation` + `pivot_to_center_bottom` at convert |

Keep the **asset description** the only part that changes between prompts.

## 4. Building a Modular Kit

1. Generate a **hero piece** first; iterate until the style block reads correctly. Its prompt becomes the template.
2. Derive siblings by swapping only the asset clause: wall module → corner → gate → pillar → stairs.
3. For tiling pieces, prompt "flat connection faces on both sides", "flat base aligned to the ground", and keep proportions stated in the same units ("about twice as wide as tall").
4. Snap in the engine; fix tiling seams there — P1 has no grid or snapping parameters.
5. Convert everything with identical `models/convert` settings (format, `scale_factor`, `pivot_to_center_bottom`, `texture_size`, `export_orientation`, `fbx_preset`).

## 5. Recurring Characters & Products

Prose alone is weak for identity. For anything that must match across many assets (a mascot, a product SKU, a character with outfit variants):

1. Produce a **turnaround**: front, left, back, right at the same scale, same height, flat even light, neutral A-pose, plain background. Tripo's multiview image tasks can be chained directly as `inputs: [{"task_id": "..."}]`.
2. Generate with multiview-to-model; keep `model_seed` fixed for reruns.
3. Outfit / colour variants: keep geometry, retexture with `models/texture` using `texture_prompt.text` (+ `style_image`) or `texture_prompt.images` (exactly 4 views) of the new colourway.
4. Geometry variants (armour on/off): new turnaround per variant, same style block, same budget class.

Single-image path: chain the approved concept with image-to-model `input: "<text_to_image task_id>"` so the exact image (not a re-description) drives the mesh.

## 6. Pipeline Continuity (generation → finished asset)

```
generate (P1, texture off) ─► approve ─► generate textured / models/texture
     │                                      │
     └──► mesh/segment ─► texture part_names (per-part materials)
                                            │
animations/rig-check ─► animations/rig ─► animations/retarget ─► models/convert (last)
```

- Each step takes the previous **task_id** as `input` — don't download and re-upload unless you edited the file externally.
- Run `rig-check` and use its `rig_type`; pass the same `rig_type`, rig `model` version and `spec` (e.g. `mixamo`, `unity`, `unreal`) for every character in a project so skeletons are interchangeable.
- Retarget all characters from the same preset set (v2.5 short presets vs v1.0 `preset:biped:*`) for consistent motion style; use `animate_in_place: true` for engine-driven locomotion.
- Orientation and pivot are decided **once**, at convert.

## 7. P1 ↔ Other Tripo Models

- **P2 migration** keeps prompts unchanged. Changing snapshot changes outputs even with identical seeds — regenerate the whole kit, don't mix P1 and P2 meshes in one set unless reviewed.
- **High-poly hero + low-poly set:** if a hero must come from H-series, bring it into the kit via retopology (`/v3/mesh/decimate`) to a matching face class and retexture with the kit's texture version.

## 8. Continuity Checklist

- [ ] Snapshot and texture version pinned
- [ ] Style block identical across all prompts
- [ ] Face-budget class assigned per asset type
- [ ] Seeds + manifest archived for every keeper
- [ ] Recurring characters/products built from multiview turnarounds
- [ ] Scale policy uniform (`auto_size` all-or-none)
- [ ] Same rig model/type/spec across characters
- [ ] Identical convert settings; orientation set only there
