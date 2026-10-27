# Meshy 7.1 — Continuity & References

Meshy has no seed, no latent lock and no character-ID system. **Continuity is carried by task IDs (while retained) and by the files you keep.** Regenerating from the same prompt gives a new object every time; the downloaded GLB is the source of truth.

## 1. Housekeeping That Makes Continuity Possible

- API assets are deleted after **3 days** (non-Enterprise). Download every approved stage on `SUCCEEDED`.
- Never store signed URLs as references — they expire. Chain with `input_task_id` / `preview_task_id` inside the window; after it, upload your local copy as `model_url`.
- Keep a library per asset: `concept/`, `views/`, `mesh-master/` (un-remeshed GLB), `mesh-game/` (remeshed), `textures/vN/`, `rig/`, `anim/`, plus a `manifest.json` recording prompt, texture prompt, task IDs, `ai_model`, `geometry_resolution`, `texture_resolution`, polycount.
- Pin `ai_model: "meshy-7.1"` for an entire library. `latest` can move under you.

## 2. Task-ID Chains

| From | To | Field |
|---|---|---|
| Text to Image / Image to Image (API, one image) | Image to 3D | `input_task_id` |
| Text/Image to Image Multi-View (API) | Multi-Image to 3D | `input_task_id` |
| Text to 3D preview | Text to 3D refine | `preview_task_id` (omit `ai_model` to inherit) |
| Preview / refine / Image to 3D / Remesh | Retexture | `input_task_id` |
| Preview / refine / Image to 3D / Retexture | Remesh | `input_task_id` |
| Any textured humanoid task (≤300k faces) | Rigging | `input_task_id` |
| Rigging | Animation | `rig_task_id` |
| Text to Motion | Animation | `motion_task_id` (within 3 days) |

Texturing never regenerates the mesh — refine and retexture are the safe way to change a look without losing shape.

## 3. Canonical Asset Master Protocol

1. Explore shapes with Text to 3D preview at `standard` (or a 2D concept → Image to 3D).
2. Pick one. That GLB is **mesh master v1** — never remesh or overwrite it.
3. For anything that must be rebuilt or matched later, make a **reference sheet**: front, side, back (and three-quarter) at the same scale, pose and lighting, plain background.
4. Rebuild or upgrade from that sheet with Multi-Image to 3D (image 1 = front) at `2k`.
5. Texture once (refine or retexture), save as **texture v1**. Variants become texture v2, v3 on the same mesh.

## 4. Consistent Asset Libraries (props, kits, sets)

Generate each item as its own task, but lock everything that defines "the same set":

**Style lock block** — paste verbatim at the end of every geometry prompt in the set:
```
STYLE: chunky hand-sculpted stylized fantasy, soft bevelled edges, slightly
exaggerated proportions, single unified object, game-ready.
```

**Texture lock block** — verbatim in every texture/retexture prompt:
```
Hand-painted stylized texture, warm desaturated palette of #7A5C3E oak,
#3E4A52 slate iron and #C9A24B brass, soft painted edge highlights,
light grime in crevices, matte finish.
```

**Technical lock** — identical settings across the set:
- Same `ai_model`, `geometry_resolution`, `texture_resolution`, `enable_pbr`.
- Same topology route: all Smart Topology `meshy-t2.5`, or all Remesh with the same `topology` and a per-class polycount budget (e.g. small props 3k, medium 8k, hero 20k).
- Same scale convention: `auto_size: true` with `origin_at: "bottom"`, or resize every asset in the DCC to a measured reference. Mixed approaches give mismatched scale.
- Retexture with `enable_original_uv: true` so UVs (and texel density) stay stable across skins.

**Anchor piece:** generate and approve one hero item first; use its render as `image_style_url` (or its texture image as `texture_image_url`) for the rest of the set.

Only vary the subject phrase between prompts. If a set item drifts, fix the subject words — never the lock blocks.

## 5. Variants of One Asset

| Want | Do |
|---|---|
| Colourway / faction skin | Retexture master with new `text_style_prompt`, `enable_original_uv: true` |
| Damaged / worn version | Retexture with wear brief; for geometric damage, new preview from a damaged-concept image |
| LOD chain | Remesh the master at descending `target_polycount` (e.g. 20k / 8k / 2k) — same source each time, not chained |
| Print version | Repair Printability on the master; export `stl`/`3mf` |

## 6. Character Continuity Pipeline

1. **Character sheet** (2D): front, side, back; A-pose; neutral light; fixed costume and proportions.
2. **Mesh:** Multi-Image to 3D, `pose_mode: "a-pose"`, `2k`, textured.
3. **Lock:** save mesh + textures as character v1. Don't regenerate the character per shot.
4. **Optimize:** Remesh to ≤300k faces (game: much lower) — keep the pre-remesh GLB.
5. **Rig once:** Rigging with accurate `height_meters`; face +Z.
6. **Animate:** preset `action_ids` (≤10 per file) and/or Text to Motion clips via `motion_task_id`; `change_fps` to match your timeline (24/25/30/60).
7. **Wardrobe/skin variants:** retexture the same mesh before rigging, or keep rig and swap textures in the engine.

For a cast, apply the style lock block and identical settings to every character so they read as one world.

## 7. Multi-Shot / Film Use

Meshy produces assets, not shots. For a sequence: import the same mesh, rig, texture version and motion clips into every shot in Blender/Unreal/Unity/Maya; stage cameras, lenses, lights and timing there. Version explicitly — `char_ivy_mesh_v1 · tex_v3 · rig_v1 · motion_<task id> · shot_012`.

## 8. When Continuity Breaks

| Symptom | Cause | Fix |
|---|---|---|
| Re-running prompt gives a different object | No seed | Keep the GLB; chain task IDs |
| Set items look like different games | Style words differ | Verbatim lock blocks, one anchor `image_style_url` |
| Props at random scales | Mixed sizing | One scale convention for the set |
| Texture density varies | Different UVs per skin | `enable_original_uv: true` on retexture |
| Back of character invented differently each time | Single front image | Multi-view sheet |
| Refine changed the model family | `ai_model` set on refine | Omit it to inherit |
| Chain broke after a weekend | 3-day retention | Re-upload local copy as `model_url` |
| Multi-view result muddled | One inconsistent view | Drop it; 3 good views > 4 mixed |
