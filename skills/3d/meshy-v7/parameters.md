# Meshy 7.1 — Parameters

Base URL `https://api.meshy.ai` · header `Authorization: Bearer <API key>` · `Content-Type: application/json`.
Every create call returns `{"result": "<task id>"}`. Poll `GET <endpoint>/:id`, list with `GET <endpoint>` (`page_num`, `page_size` ≤100, `sort_by: +created_at | -created_at`), or stream `GET <endpoint>/:id/stream` (SSE).

*Verified against the Meshy API docs (Text to 3D, Image to 3D, Multi-Image to 3D, Retexture, Remesh, Rigging, Animation, Text to Motion, Pricing, Asset Retention, Changelog), October 2026.*

## Model IDs

| `ai_model` | Status | Notes |
|---|---|---|
| `meshy-7.1` | Current | Pin it for reproducible pipelines. Only model that accepts `geometry_resolution` `2k`/`4k`. |
| `latest` | Default | Currently = `meshy-7.1` on Text/Image/Multi-Image to 3D. **On Retexture, `latest` = Meshy 7** (no 7.1 there yet). |
| `meshy-7` | Deprecated | Still works; migrate to `meshy-7.1`. |
| `meshy-6` | Supported | Only model that emits an emission map and honours `remove_lighting`. |
| `meshy-6-lite` | Supported | 5-credit fast mesh; no 4K/8K texture, no `image_enhancement`/`remove_lighting`. |
| `meshy-t2.5` / `meshy-t2` | Smart Topology only | Use with `model_type: "smart-topology"`. `t2.5` is the default (sharper game-asset detail); `t2` gives natively separated parts. Triangle output only. Not on Multi-Image. |

`meshy-5` was retired 10 Oct 2026 (returns 400).

## Text to 3D — Preview (geometry)

`POST /openapi/v2/text-to-3d`

| Field | Type | Default | Values / limits | Notes |
|---|---|---|---|---|
| `mode` | string | — (required) | `"preview"` | Mesh only, no texture. |
| `prompt` | string | — (required) | ≤ 800 chars | Geometry description. |
| `model_type` | string | `standard` | `standard`, `smart-topology`, `lowpoly` (deprecated, retires 30 Oct 2026) | Smart Topology ignores `should_remesh`/`decimation_mode`. |
| `ai_model` | string | `latest` | see table above | |
| `geometry_resolution` | string | `standard` | `standard`, `2k` (2048³), `4k` (4096³) | 7.1/`latest` only. +5 credits for either Ultra tier. |
| `should_remesh` | bool | `false` (Meshy 6/7) | | Keep `false` for max fidelity. |
| `topology` | string | `triangle` | `triangle`, `quad` | Applies when remeshing. `quad` + Smart Topology = error. |
| `target_polycount` | int | 30,000 (remesh) | Remesh 100–300,000 · `meshy-t2` 100–15,000 (def 4,000) · `meshy-t2.5` 100–30,000 (def 15,000) | Actual count may vary. |
| `decimation_mode` | int | — | `1` ultra · `2` high · `3` medium · `4` low (adaptive) | Overrides `target_polycount`. |
| `pose_mode` | string | `""` | `a-pose`, `t-pose`, `""` | Use for anything you'll rig. |
| `moderation` | bool | `false` | | Screens the prompt. |
| `target_formats` | string[] | all except `3mf` | `glb`, `obj`, `fbx`, `stl`, `usdz`, `3mf` | Fewer formats = faster completion. `3mf` only when requested. |
| `alpha_thumbnail` | bool | `false` | | Adds `alpha_thumbnail_url` (RGBA preview). |
| `auto_size` | bool | `false` | | AI estimates real-world height and rescales. |
| `origin_at` | string | `bottom` | `bottom`, `center` | Only with `auto_size: true`. |

## Text to 3D — Refine (texture)

Same endpoint, `mode: "refine"`. Textures the Preview mesh without regenerating it.

| Field | Type | Default | Values / limits | Notes |
|---|---|---|---|---|
| `preview_task_id` | string | — (required) | a `SUCCEEDED` preview | The continuity link. |
| `texture_prompt` | string | — | ≤ 800 chars | Surface only. |
| `texture_image_url` | string | — | jpg/jpeg/png/webp, ≤ 20 MB, URL or data URI | If sent with `texture_prompt`, the text wins. |
| `enable_pbr` | bool | `false` | | Adds metallic, roughness, normal. No emission on 7.1. |
| `texture_resolution` | string | `2k` | `2k`, `4k`, `8k` | 4K/8K need `meshy-6`, `meshy-7.1` or `latest`. |
| `ai_model` | string | inherited | | **Omit** to keep the preview's model. |
| `remove_lighting` | bool | `true` | | Only acts on `meshy-6`; 7.1 ignores it. |
| `moderation`, `target_formats`, `alpha_thumbnail`, `auto_size`, `origin_at` | | | | As in Preview. |

## Image to 3D (single image)

`POST /openapi/v1/image-to-3d`

| Field | Type | Default | Values / limits | Notes |
|---|---|---|---|---|
| `image_url` | string | — | jpg/jpeg/png/webp, ≤ 20 MB, URL or data URI | One of this or `input_task_id`. |
| `input_task_id` | string | — | `SUCCEEDED` API Text to Image / Image to Image task with exactly one image | Wins if both sent. |
| `model_type` | string | `standard` | `standard`, `smart-topology`, `lowpoly` (deprecated) | |
| `ai_model` | string | `latest` | | |
| `geometry_resolution` | string | `standard` | `standard`, `2k`, `4k` | 4K supported here. |
| `should_texture` | bool | `true` | | `false` = mesh-only iteration. |
| `enable_pbr` | bool | `false` | | Needs `should_texture: true`. |
| `texture_resolution` | string | `2k` | `2k`, `4k`, `8k` | |
| `texture_prompt` / `texture_image_url` | string | — | ≤ 800 chars / image as above | Send one; text wins. |
| `image_enhancement` | bool | `true` | | `false` keeps the input's exact look (clean renders). Error on `meshy-6-lite`/Smart Topology. |
| `remove_lighting` | bool | `true` | | Acts on `meshy-6` only; 7.1 accepts and ignores. |
| `should_remesh`, `topology`, `target_polycount`, `decimation_mode` | | | as Text to 3D | |
| `save_pre_remeshed_model` | bool | `false` | | Extra `pre_remeshed_glb` when `should_remesh: true`. |
| `pose_mode` | string | `""` | `a-pose`, `t-pose`, `""` | |
| `multi_view_thumbnails` | bool | `false` | | Front/right/back/left previews (~+3 s). **Documented as applying only when `auto_size: true`.** |
| `target_formats`, `auto_size`, `origin_at`, `alpha_thumbnail`, `moderation` | | | as Text to 3D | |

## Multi-Image to 3D (1–4 views)

`POST /openapi/v1/multi-image-to-3d` — no `model_type` field (no Smart Topology).

| Field | Type | Default | Values / limits | Notes |
|---|---|---|---|---|
| `image_urls` | string[] | — | 1–4 images, jpg/jpeg/png/webp, ≤ 20 MB each | Same object, same pose. For 7.1, **image 1 = front**; order of the rest doesn't matter. |
| `input_task_id` | string | — | API Text/Image to Image (incl. Multi-View) task | Wins if both sent. |
| `geometry_resolution` | string | `standard` | `standard`, `2k` | **No `4k`.** |
| `texture_image_urls` | string[] | — | 1–4 images, front first | 7.1/`latest` only; can't combine with `texture_prompt` or `texture_image_url`. |
| `texture_prompt` / `texture_image_url` | | — | as Image to 3D | |
| `image_enhancement` | bool | `true` | | |
| `remove_lighting` | bool | `true` | | Listed as supported for 7.1 on this endpoint (unlike single Image to 3D) — verify visually. |
| all other fields | | | as Image to 3D | `target_polycount` default 30,000. |

## Retexture

`POST /openapi/v1/retexture`

| Field | Type | Default | Values / limits | Notes |
|---|---|---|---|---|
| `input_task_id` | string | — | `SUCCEEDED` Text to 3D preview/refine, Image to 3D or Remesh task | Wins over `model_url`. |
| `model_url` | string | — | glb/gltf/obj/fbx/stl; URL ≤ 400 MB, data URI ≤ 100 MB | >100 MB: ≤10M tris, no Draco, binary FBX 7.1+. |
| `text_style_prompt` | string | — | ≤ 800 chars | One style input required. |
| `image_style_url` | string | — | jpg/jpeg/png/webp ≤ 20 MB | Overrides text if both sent. |
| `multiview_image_urls` | string[] | — | 1–4, front first | Exclusive; requires `ai_model: "meshy-7"`. |
| `ai_model` | string | `latest` (= Meshy 7) | `meshy-6-lite`, `meshy-6`, `meshy-7`, `latest` | |
| `enable_original_uv` | bool | `false` | | `true` keeps existing UVs — use it for Meshy meshes and for texel-consistent libraries. |
| `enable_pbr`, `texture_resolution`, `remove_lighting`, `target_formats`, `alpha_thumbnail` | | | as above | |

## Remesh

`POST /openapi/v1/remesh` — input `input_task_id` (Text to 3D, Image to 3D, Retexture) or `model_url` (glb/gltf/obj/fbx/stl, limits as Retexture).

| Field | Default | Values | Notes |
|---|---|---|---|
| `topology` | `triangle` | `triangle`, `quad` | `quad` = quad-dominant. |
| `target_polycount` | 30,000 | 100–300,000 | Ignored if `decimation_mode` set. |
| `decimation_mode` | — | `1`–`4` | Adaptive. |
| `target_formats` | `["glb"]` | `glb`, `fbx`, `obj`, `usdz`, `blend`, `stl`, `3mf` | Only endpoint that outputs `.blend`. |
| `resize_height`, `resize_longest_side`, `auto_size`, `origin_at`, `convert_format_only` | | | Deprecated — prefer the dedicated Resize / Convert APIs. |

## Rigging · Animation · Text to Motion

| Endpoint | Fields | Rules |
|---|---|---|
| `POST /openapi/v1/rigging` | `input_task_id` or `model_url` (GLB only) · `height_meters` (default 1.7) · `texture_image_url` (PNG) | Textured humanoid biped, clear limbs, ≤300k faces (Remesh first), face toward **+Z**. Returns rigged FBX/GLB + basic walk/run clips. 422 = pose estimation failed. |
| `POST /openapi/v1/animations` | `rig_task_id` + exactly one of `action_id` · `action_ids` (1–10 unique) · `motion_task_id` · optional `post_process` | `post_process.operation_type`: `change_fps` (`fps` 24/25/30/60, default 30), `fbx2usdz`, `extract_armature`. `action_ids` merge into one file in array order. `motion_task_id` needs a biped rig. |
| `GET /openapi/v1/animations/library` | `search`, `category`, `sub_category`, `action_ids` | Free. Categories: `WalkAndRun`, `BodyMovements`, `DailyActions`, `Fighting`, `Dancing`. IDs are not contiguous — look them up. |
| `POST /openapi/v1/text-to-motion` | `prompt` (≤400, required) · `duration` (2–10 s, 0.5 steps, required) · `mode` (`prime` default / `swift`) | `prime` → FBX, `swift` → BVH. Standalone clip; apply via `motion_task_id` within 3 days. 403 = moderation. |

## Credits (API)

| Item | Credits |
|---|---|
| Text to 3D preview, `meshy-7.1` / `meshy-6` | 20 |
| Preview `meshy-6-lite` / `meshy-t2` / `meshy-t2.5` | 5 |
| Ultra geometry (`2k` or `4k`), 7.1 only | +5 |
| Refine or Retexture, 2K/4K texture | 10 |
| Refine or Retexture, 8K texture | 15 |
| Image to 3D / Multi-Image 7.1: mesh only · 2K/4K tex · 8K tex | 20 · 30 · 35 |
| Remesh · Rigging · UV Unwrap | 5 each |
| Animation | 3 per action |
| Text to Motion `prime` / `swift` | 10 / 3 |
| Convert · Resize | 1 |
| Analyze Printability · Repair Printability | free · 10 |

Failed tasks refund. Deleting a `PENDING` task refunds; `IN_PROGRESS` returns 409. Web-app pricing and subscription gating (Ultra tiers and 7.1 downloads need a subscription in the workspace) differ from API credits.

## Outputs & Retention

- Task object: `status` (`PENDING`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `CANCELED`), `progress`, `model_urls`, `texture_urls` (`base_color`, + `metallic`/`roughness`/`normal` with PBR), `thumbnail_url`, `consumed_credits`, `task_error`.
- **API assets are kept 3 days (non-Enterprise), then deleted.** Signed URLs stop at `expires_at`. Download on `SUCCEEDED`; chain by task ID while retained.
- USDZ exports are in metres (since 12 Oct 2026).

## Format Choice

| Format | Use |
|---|---|
| GLB | Default review/web/interchange, keeps PBR |
| FBX | Rigging, animation, Unity/Unreal/Maya |
| OBJ (+MTL) | Static interchange |
| STL / 3MF | Printing (3MF opt-in) |
| USDZ | Apple AR |
| BLEND | Remesh output only |

## Recommended Combinations

| Workflow | Endpoint | Key settings |
|---|---|---|
| Shape exploration | Text to 3D preview | `meshy-7.1`, `standard`, no remesh, `["glb"]` |
| Hero prop / close-up | Text or single Image | `geometry_resolution: 4k`, no remesh → refine `4k`/`8k`, `enable_pbr` |
| Accurate asymmetric object | Multi-Image | 3–4 consistent views, `2k`, `image_enhancement: false` for clean renders |
| Rig-ready humanoid | Text/Image/Multi | `pose_mode: a-pose`, textured, then Remesh ≤300k → Rigging |
| Real-time game asset | Smart Topology or Remesh | `meshy-t2.5` 5k–15k, or Remesh `quad`/`triangle` to budget |
| Variant skins of one mesh | Retexture | `input_task_id` of master, `enable_original_uv: true` |
| 3D print | Text/Image → Repair Printability | prompt "solid, watertight", `["stl","3mf"]` |

## Meshy 7 → 7.1 Migration

| Old | 7.1 |
|---|---|
| `ai_model: "meshy-7"` | `"meshy-7.1"` (pin; don't rely on `latest`) |
| `ultra_mode: true` | `geometry_resolution: "2k"`; `"4k"` for text/single image |
| `hd_texture: true` | `texture_resolution: "4k"` |
| `is_a_t_pose` | `pose_mode` |
| `art_style`, `symmetry_mode`, `surface_mode`, `negative_prompt` | No effect — style goes in the prompt |
| `model_type: "lowpoly"` | `smart-topology` + `meshy-t2.5` before 30 Oct 2026 |
| `/v2/text-to-3d` | `/openapi/v2/text-to-3d` |

Prompts transfer unchanged, but 7.1 renders more micro-detail as real geometry — regression-test polycount, decimation and printability.
