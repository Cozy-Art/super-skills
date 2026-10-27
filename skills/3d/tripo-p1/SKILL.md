---
name: tripo-p1-prompts
description: Generate optimized prompts and API payloads for Tripo Smart Mesh P1.0 (snapshot P1-20260311, alias tripo-p1), Tripo AI's low-poly 3D generation model with clean, structured topology and strict face-count control (50–20,000 faces). Use whenever a user mentions Tripo P1, Tripo Smart Mesh, P1-20260311, tripo-p1, Tripo3D low-poly, or wants text-to-3D, image-to-3D or multiview-to-3D game assets, mobile/WebGL/XR props, stylized characters, modular environment kits, or a downstream Tripo pipeline (retexture, segmentation, rig-check, auto-rig, animation retarget, format conversion). Also use when migrating Tripo v2 task payloads to v3 endpoints, or deciding between P1, P2 (quad output) and the high-poly H-series. Do not guess Tripo P1 field names, ranges or syntax from general knowledge or older Tripo versions — use the reference files.
---

# Tripo Smart Mesh P1 — Prompt Generation Skill

Tripo P1 (`P1-20260311`) generates a **static, low-poly, game-ready mesh** (GLB) from text, one image, or 2–4 views. It is a 3D asset model, not an image or video model: no aspect ratio, duration, camera or motion controls exist. Texturing, rigging, animation and format conversion are separate Tripo endpoints that consume the P1 result.

## The Three Rules That Override Everything

1. **One asset per generation, described as a 3D object.** Subject first, then silhouette, proportions and 2–4 structural parts. Scenes ("a knight on a horse by a castle") fuse or collapse — generate pieces separately and assemble in a DCC/engine.
2. **Numbers live in fields, not prose.** Face count, seeds, texture tier, PBR, scale and UVs are JSON parameters. "Exactly 5,000 triangles" in the prompt does nothing; `face_limit: 5000` does.
3. **Geometry first, texture second.** Iterate with `texture: false`, approve the mesh from all sides, then lock `model_seed` (and `image_seed`) and vary only `texture_seed` / material wording.

## Prompt Order (text-to-model)

| # | Layer | Example |
|---|---|---|
| 1 | Primary asset | "A compact medieval treasure chest" |
| 2 | Form + proportions | "broad rectangular body, curved lid about one third of total height" |
| 3 | 2–4 defining parts | "separate iron corner bands, oversized front lock" |
| 4 | Style | "stylized low-poly", "hand-painted", "hard-surface sci-fi" |
| 5 | Materials + dominant colours | "dark oak with blackened iron" |
| 6 | Use / topology intent | "mobile game prop", "neutral pose for rigging", "flat base" |

```
[ASSET], [SILHOUETTE + PROPORTIONS], [2–4 SEPARATE PARTS],
[STYLE], [MATERIALS + COLOURS], [INTENDED USE / TOPOLOGY INTENT].
```

Write it as one or two natural sentences. **Target 20–60 words** (practical, not official). Hard limits: `prompt` ≤ 1,024 chars, `negative_prompt` ≤ 255 chars. Plain natural language only — no weights, brackets, or flags.

**Negative prompt** = structural failures only: `floating parts, duplicate limbs, fused arms, thin fragile geometry, text, logo, background terrain`.

## Decide the Operation First

| User has / wants | Endpoint (`POST /v3/...`) | Where the "prompt" goes |
|---|---|---|
| Idea in words | `generation/text-to-model` | `prompt` + `negative_prompt` |
| One concept image | `generation/image-to-model` | **No text field.** Craft the reference image (clean bg, ¾ view) |
| Front + side/back views | `generation/multiview-to-model` | **No text field.** Consistent views, `front` mandatory, ≥2 images |
| Same mesh, new look | `models/texture` (input = task_id) | `texture_prompt.text` (+ optional `style_image`) |
| Parts for materials/rig | `mesh/segment` | none — then texture by `part_names` |
| Will it rig? | `animations/rig-check` | none — returns `riggable`, `rig_type` |
| Skeleton | `animations/rig` | none — `rig_type`, `spec`, `out_format` |
| Motion | `animations/retarget` | preset IDs, e.g. `preset:walk` |
| FBX / USDZ / OBJ / STL / 3MF | `models/convert` | none — final step, orientation + pivot here |

Need quads or >20k faces → P2 (`P2-20260801`). Need high-poly hero/print fidelity → H-series. See [parameters.md](parameters.md).

## Quick Syntax Reference

- **Model:** always `"model": "P1-20260311"` (required — no default on P-series endpoints).
- **Face budget:** `face_limit` 50–20,000; omit for adaptive. Don't go below 150 (simple) / 250 (complex).
- **Seeds:** `image_seed` (text-to-model only; hidden reference image) · `model_seed` (geometry) · `texture_seed` (appearance).
- **Texture:** `texture` / `pbr` default `true`; `pbr: true` forces texture on. `texture_quality`: `fast` | `standard` | `detailed` | `extreme` (8K).
- **`fast` and `delight`** need `texture_version: "v3.5-20260815"`; `fast` on any other version → error `1004`.
- **Multiview inputs:** `[{"front": url}, {"left": url}, {"back": url}, {"right": url}]` — never mix with positional or task_id forms.
- **Chaining:** image-to-model `input` can be a prior Tripo `text_to_image`/`image_to_image` task_id; downstream endpoints take the P1 `task_id`.

## Output Format (always two parts)

1. **Prompt** — in a code block, prompt text only. If useful, a second code block labelled **Negative prompt**. Never put face count, seeds, texture tier or format inside the prompt.
2. **Suggested settings** — one line, e.g. `model: P1-20260311 · face_limit: 3000 · texture: false (geometry pass) · auto_size: true · export_uv: true`

For image/multiview requests, the "prompt" is the **reference-image brief** (for whatever image model makes the views) plus settings. If the user is building an API call, also give the JSON body with only valid fields.

## Things That Will Break the Request

- `quad`, `smart_low_poly`, `generate_parts`, `geometry_quality` on P1 → rejected (`quad=true` returns 400). Quad = P2 or `models/convert` with `quad: true`.
- `face_limit` outside 50–20,000.
- `texture_quality: "fast"` without `texture_version: "v3.5-20260815"` → `1004`.
- Missing `model`. Sending `prompt` to image/multiview endpoints (no such field).
- Mixing multiview input forms; omitting `front`; fewer than 2 views.
- v2 habits: `POST /v2/openapi/task` with `type: "text_to_model"`, `model_version`, `create_time` parsing.
- Setting `export_orientation` at generation when you'll texture/rig/convert later — may silently mis-orient. Orient in `models/convert`.
- Emoji / unusual Unicode in prompts (legacy P1 docs warn against them).

## Iteration Workflow

1. **Blockout:** `texture: false`, adaptive or target `face_limit`. ~10 s per mesh. Try 2–3 `model_seed`s.
2. **Inspect all sides** — back, underside, thin parts, limb gaps. Fix wrong silhouette by *simplifying* the prompt, not adding adjectives. Wrong hidden side → switch to multiview.
3. **Lock** prompt, `image_seed`, `model_seed`, `face_limit`, snapshot.
4. **Texture:** re-run with texture on (same seeds) or call `models/texture` on the task_id; vary `texture_seed` for variants. `standard` while exploring, `detailed`/`extreme` for finals.
5. **Downstream:** segment → rig-check → rig → retarget → convert (last). Download every output into your asset store.
6. **Archive** prompt, negative, all seeds, model + texture versions, settings, reference hashes, task IDs.

## Reference Files

- **[parameters.md](parameters.md)** — every field for the three generation endpoints plus texture, segment, rig-check, rig, retarget, convert, task query; face-budget bands; pricing; P1 vs P2 vs H; v2→v3 migration.
- **[best-practices.md](best-practices.md)** — thinking in 3D, silhouette-first, ratios, part separation, face-budget matching, reference-image craft, composition for characters/props/environments, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — seed layering, style bibles, asset-kit consistency, recurring characters via multiview, retexture/rig pipelines, library archiving.
- **[examples.md](examples.md)** — annotated prompts: prop, character, creature, vehicle, modular kit, style variants, multiview product, retexture, rig + animation chain, P2 migration.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
