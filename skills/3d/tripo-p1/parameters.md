# Tripo P1 — Parameters

Base URL: `https://openapi.tripo3d.ai/v3` · header `Authorization: Bearer <TRIPO_API_KEY>` · `Content-Type: application/json`.
All tasks are asynchronous: submit returns `{"code": 0, "data": {"task_id": "task_..."}}` → poll `GET /v3/tasks/{task_id}` or use a webhook.

*Verified against the Tripo Developers API reference (developers.tripo3d.ai: P-series text/image/multiview-to-model, texture, segment, rig-check, rig, retarget, convert, task query, changelog, P1 model page), October 2026.*

## Model Identity

| Item | Value |
|---|---|
| Product | Tripo Smart Mesh P1.0 |
| Snapshot (send this) | `P1-20260311` — the only P1 snapshot; stable |
| Guidance alias | `tripo-p1` (used in Tripo's models/versions guidance and CLI) |
| Successor | `P2-20260801` (marked Preview on endpoint pages) |
| Output | Low-poly triangle mesh, GLB (`output.model_url`) + preview (`output.rendered_image_url`) |
| Speed (model page) | ~10 s untextured, ~60 s textured — workload-dependent |
| Concurrency | 3 parallel P-series tasks by default (tier-dependent) |

## Text-to-Model — `POST /v3/generation/text-to-model`

| Field | Type | Req | Values | Default | Notes |
|---|---|---|---|---|---|
| `prompt` | string | ✅ | ≤ 1,024 chars | — | Shape, material, style, scale. Material/style hints improve PBR. |
| `negative_prompt` | string | — | ≤ 255 chars | none | Structural/visible exclusions. |
| `model` | string | ✅ | `P1-20260311` | — | No default on P-series endpoints. |
| `image_seed` | int | — | any | random | Seeds the internal text-to-image reference step. |
| `model_seed` | int | — | any | random | Same seed + same input → same mesh. |
| `face_limit` | int | — | **50–20,000** (P1) | adaptive | Start ≥150 (simple) / ≥250 (complex). |
| `texture` | bool | — | | `true` | `false` = bare geometry. |
| `pbr` | bool | — | | `true` | Base colour, metallic, roughness, normal. Forces `texture: true`. |
| `texture_seed` | int | — | any | random | Same seed → same texture. Vary with `model_seed` fixed. |
| `texture_quality` | string | — | `fast` `standard` `detailed` `extreme` | `standard` | See tiers below. |
| `texture_version` | string | — | `v3.5-20260815` `v3.0-20250812` `v2.5-20250123` | derived (`v3.0-20250812` for P-series) | Pins texture model independently of geometry. |
| `delight` | bool | — | | `true` | Strips baked lighting from the reference. Only read by `v3.5-20260815`. |
| `auto_size` | bool | — | | `false` | Real-world scale in metres. |
| `export_uv` | bool | — | | `true` | `false` = faster, smaller, but no UV unwrap. |
| `export_orientation` | string | — | `+x` `-x` `-y` `+y` | `+x` | Leave unset if post-processing; fix in `models/convert`. |

## Image-to-Model — `POST /v3/generation/image-to-model`

Same as text-to-model **minus** `prompt`, `negative_prompt`, `image_seed`. **There is no text field.** Adds:

| Field | Values | Default | Notes |
|---|---|---|---|
| `input` ✅ | file token (`file_...`), public URL, **or** task_id of a successful `text_to_image` / `image_to_image` task | — | Exactly one. PNG/JPEG/WebP, ≤ 20 MB, ≥ 256×256 recommended. |
| `enable_image_autofix` | bool | `false` | AI cleanup/completion of weak references. |
| `texture_alignment` | `original_image` `geometry` | `original_image` | Match source colours vs. follow generated shape. |
| `orientation` | `default` `align_image` | `default` | Align to reference viewpoint; only applies when texture on. |

## Multiview-to-Model — `POST /v3/generation/multiview-to-model`

Same fields as image-to-model, with `inputs` (plural) instead of `input`. Use **one** form:

| Form | Shape | Rules |
|---|---|---|
| View-key (recommended) | `[{"front": "<url\|file_token>"}, {"left": ...}, {"back": ...}, {"right": ...}]` | Any order (server reorders). Values may also be `{url}`, `{file_token}`, `{object:{bucket,key}}`. |
| Legacy positional | `["front", "left", "back", "right"]` — exactly 4 strings | `""` for a missing view. |
| Task chain | `[{"task_id": "<uuid>"}]` — single element | Source must be a successful `generate_multiview_image` / `edit_multiview_image` task. |

`front` mandatory · ≥ 2 images · same object, consistent lighting · PNG/JPEG/WebP · ≥ 256×256.

## Texture Tiers

| `texture_quality` | Behaviour | Use |
|---|---|---|
| `fast` | Same size + cost as standard, less detail. **Requires `v3.5-20260815`**, else `1004` (no fallback). | Quick look-dev |
| `standard` | Default balance | Iteration, most mobile/web assets |
| `detailed` | Higher fidelity, slower, more credits | Approved finals |
| `extreme` | 8K textures, extra credits | Hero/close-up finals only |

## Face-Budget Bands (production guidance, not Tripo presets)

| Asset class | `face_limit` |
|---|---|
| Blockout / icon / UGC filler | 150–800 |
| Web / UGC object | 500–3,000 |
| Mobile prop | 1,000–5,000 (Tripo quick-start uses 5,000) |
| Hero prop, vehicle, modular hero piece | 5,000–15,000 |
| Hero low-poly character / creature | 8,000–20,000 |

## Recommended Combinations

| Workflow | Settings |
|---|---|
| Silhouette exploration | `texture: false`, `pbr: false`, adaptive or target `face_limit` |
| Geometry-only base mesh | `texture: false`, `pbr: false`, `export_uv: false` |
| Mobile prop final | `face_limit` 1k–5k, `pbr: true`, `standard`, `auto_size: true` |
| Hero character | `face_limit` 8k–20k, `pbr: true`, `detailed`, UV on |
| Same shape, material variants | lock `image_seed` + `model_seed`; vary `texture_seed` |
| Fast look-dev | `texture_quality: fast` + `texture_version: v3.5-20260815` |
| Reference-faithful product | multiview 3–4 views, `texture_alignment: original_image` |
| AR / engine scale | `auto_size: true`; orientation only at convert |

## Downstream Endpoints (consume the P1 `task_id`)

**Texture — `POST /v3/models/texture`.** `input` (task_id / file_token / URL; GLB GLTF FBX OBJ STL ≤150 MB) · `model` (texture version, default `v3.0-20250812`; note: here it's `model`, not `texture_version`) · `texture_prompt` {exactly one of `text` | `image` | `images` (exactly 4: front, left, back, right); `style_image` only with `text`} · `pbr` (true) · `texture_seed` · `texture_alignment` · `texture_quality` · `part_names` (from segmentation; omit = all) · `compress: "geometry"` (meshopt) · `bake` (true) · `delight` (true, v3.5 only). Tripo recommends re-supplying the reference image when texturing from a task_id.

**Segmentation — `POST /v3/mesh/segment`.** `input` · `model` (`v1.0-20250506` default; `v2.0-20260430` Beta = semantic labelled parts) · v2 only: `segmentation_granularity` (`simple` `balanced` `detailed`, default balanced), `split_by_connectivity` (true), `ref_image`.

**Rig check — `POST /v3/animations/rig-check`.** `input` (GLB FBX OBJ STL ≤150 MB) → result `output.riggable` (bool), `output.rig_type`.

**Auto rig — `POST /v3/animations/rig`.** `input` · `model`: `v1.0-20240301` (default, biped only) · `v2.5-20260210` (non-humanoid creatures) · `v3.0-20260909` (better humanoid; adds `others`; request explicitly) · `rig_type`: `biped` (default) `quadruped` `hexapod` `octopod` `avian` `serpentine` `aquatic` `others` (v3.0 only) · `spec` (biped only): `tripo` (default) `mixamo` `actorcore` `unity` `unreal` `vrm` · `out_format`: `glb` (default) / `fbx`.

**Retarget — `POST /v3/animations/retarget`.** `input` = rigged task_id · `animation` (one) **or** `animations` (list) · `out_format` · `export_with_geometry` (true) · `animate_in_place` (false). `bake_animation` is deprecated/ignored.
- Rig v2.5 presets: `preset:idle` `walk` `run` `dive` `climb` `jump` `slash` `shoot` `hurt` `fall` `turn` · `preset:quadruped:walk` · `preset:hexapod:walk` · `preset:octopod:walk` · `preset:serpentine:march` · `preset:aquatic:march`.
- Rig v1.0: 90+ `preset:biped:*` (e.g. `idle`, `walk`, `run`, `jump`, `wave_goodbye_01`, `dance_01`, `sit`, `cast_a_spell`). Preset sets for rig v3.0 not documented — (unverified — confirm on your platform).

**Convert — `POST /v3/models/convert`.** `format` ✅ `GLTF` `FBX` `USDZ` `OBJ` `STL` `3MF` (STL/3MF geometry only; OBJ no animation) · `quad` (forces FBX; default 10k faces if no `face_limit`) · `force_symmetry` (quad only) · `face_limit` · `flatten_bottom` (+ `_threshold` 0.01) · `texture_size` (4096) · `texture_format` (`JPEG` default, PNG, WEBP…) · `bake` · `pack_uv` · `export_vertex_colors` (OBJ/GLTF) · `pivot_to_center_bottom` · `scale_factor` (1) · `with_animation` (true) · `animate_in_place` · `part_names` · `export_orientation` · `fbx_preset` (`blender` default, `3dsmax`, `mixamo`, `bake_scale`).

**Also in the v3 suite (Oct 2026 changelog):** retopology `POST /v3/mesh/decimate` (`model=v3.0` adds `smart_uv`), UV re-unwrap `POST /v3/mesh/uv`. Smart Segmentation and Mesh Complete exist in the docs sidebar; paths not verified here.

## Task Query

`GET /v3/tasks/{task_id}` → `status`: `queued` `running` `success` `failed` `cancelled` · `progress` 0–100 · `output.model_url`, `output.rendered_image_url` · `error_code` / `error_message` · `credits_consumed` (**decimal** — don't parse as int) · `created_at`, `completed_at`. Download outputs promptly into your own store; don't treat result URLs as permanent.

## Pricing (credits, per P1 model page)

| Task | No texture | Standard | Detailed |
|---|---|---|---|
| Text-to-3D | 30 | 40 | 50 |
| Image-to-3D | 40 | 50 | 60 |
| Multiview-to-3D | 40 | 50 | 60 |

`extreme` costs more than detailed; `fast` = standard. P2 for comparison: 100 / 110 / 120 / 130 (none/standard/detailed/extreme). Units on the P1 page are unlabelled — (unverified as credits — confirm on your plan).

## P1 vs P2 vs H-series

| | P1 `P1-20260311` | P2 `P2-20260801` | H-series (H3 / H3.1) |
|---|---|---|---|
| Purpose | Clean low-poly, real-time | Next-gen P-series | High-poly fidelity, print, marketing |
| Faces | 50–20,000 tri | 48–50,000 tri; 48–25,000 quad | High-poly |
| `quad` | ❌ (400) | ✅ | see H-series schema |
| Prompt grammar | plain language | unchanged — prompts migrate as-is | plain language |

Migrate P1→P2: change `model`, revisit `face_limit`, optionally add `quad: true`.

## Not Available on P1 (do not send)

`quad` · `smart_low_poly` · `generate_parts` · `geometry_quality` · aspect ratio / width / height / duration / fps / camera / motion fields · `prompt` on image/multiview endpoints.

## v2 → v3 Migration

| v2 habit | v3 |
|---|---|
| `POST /v2/openapi/task` + `type` | Dedicated routes, e.g. `/v3/generation/text-to-model` |
| `/v2/openapi/` base | `/v3/` |
| Mixed input fields | Unified `input` / `inputs` |
| `create_time`, `consumed_credit` | `created_at`, `credits_consumed` (decimal) |
