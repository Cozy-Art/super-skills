# World Labs Atlas — Input Modes and Continuity

In Atlas, continuity is **scene state**: posed views, depth, cameras in one world frame, a fixed prompt and seed. A long "keep everything consistent" paragraph is the weakest tool you have.

## 1. Two ways to pose images

| Mode | When | Rules |
|---|---|---|
| **Reconstruct together** | Several photos of one real place | One `images2PosedRGBD` call with all frames. "Use sharp images of a mostly static scene, with similar exposure and lighting." Overlap and translation, not only rotation. `refinePoses: true` when small pose errors cause blur. |
| **Pose separately, place yourself** | Creative images from different sources (concept art, generated stills) | Pose each alone, then put them into one shared scene frame. Their camera views **must not overlap** — Atlas invents the connecting space between them. |

Never mix unrelated places in one reconstruction request.

## 2. Building and curating context

1. Pose anchors; inspect depth and camera registration before generating anything.
2. Generate a conservative first set of targets.
3. "Inspect the result, add useful returned RGBD views to your context, and choose the next cameras."
4. Reject any view with smeared geometry, wrong scale or appearance drift — errors carry into later requests.
5. Keep a **compact** set of strong, complementary keyframes near where future shots will look. Don't recursively keep every output.

"The more it sees, the less it imagines." More good views reduce invention; more weak views add conflict.

## 3. Prompt and seed lock

For every later view of the same scene:
- pass the earlier response's `promptUsed` as `prompt`,
- set `enhancePrompt: false` (skips recaptioning, lowers latency),
- keep the seed fixed,
- change one thing at a time.

Store per operation: request body, cameras, seed, `promptUsed`, operation ID and output assets. Operation records last 30 days.

**Scene bible (kept outside the prompt):** canonical appearance prompt, coordinate convention (`rub`/`rdf`), world origin and unit, intrinsics policy, seed policy, accepted keyframe asset IDs, shot → camera mapping.

## 4. Characters and props

Humans and articulated motion are the weakest targets. For a recurring character or prop:
- Use sharp full- or medium-body views, not face crops.
- Supply front, three-quarter, profile and rear evidence when those sides will be seen.
- Keep costume, lighting, focal length, exposure and pose compatible across references.
- Reconstruct overlapping photos of one real setup together; place independently posed references in non-overlapping views.
- Repeat only short canonical attributes in text ("white crackle-glaze ceramic robot, blue shoulder markings"); let the images carry identity.
- Keep figures small in frame as scale/story anchors when the world is the subject.

## 5. Lighting, weather and set-dressing changes

A change of time, weather or dressing is a **state transition**, not a prompt tweak inside a continuing path:
1. Finish and store the "before" state.
2. Write the new state as a new appearance prompt (or edit an anchor and propagate with `atlasMasked`).
3. Build new anchors for the "after" state; don't mix before/after views in one context.

## 6. Multiview object edits (`atlasMasked`, if your account has it)

1. Pick a strong anchor view and edit it in an image editor.
2. Send it as `contextFrames[0]` with an **all-white** mask, paired with `targetCameras[0]`.
3. Add 1–16 overlapping views of the same scene, each with a mask whose **black** region fully covers the object plus a small margin.
4. Pair every frame with the target camera at the same index.
5. Prompt with enhancement on: "Replace the yellow utility cart beside the west arch with a low oxidized-bronze fountain." The enhancer does not see masks, so locate the edit by visible landmarks. State removals explicitly.
6. After the edit, update every affected stored view before continuing — stale views reintroduce the old object.

## 7. Blockout to environment (`atlasChisel`)

Structure from depth, appearance from text and photos:
- Render one 1280 × 720 depth raster per target camera from your blockout (or skip depth and generate from the prompt alone).
- `voxelSize` 0.05–0.15 to quantize a rough blockout; omit for faithful depth. `world` grid for axis-aligned architecture.
- Add posed `sourceFrames` (any size) to carry real materials, colour and light. Budget: context + source + targets ≤ 64.
- The prompt is required and should carry style, materials and light — layout is already decided by depth.

The same blockout with different prompts gives different worlds; keep the cameras and depth fixed and vary only the text to compare looks.

## 8. Multi-shot workflow

1. Fix one coordinate system, scene scale, master appearance prompt and seed policy.
2. Pose anchors; check registration.
3. Generate a conservative establishing path with depth.
4. Reject flawed outputs.
5. Save strong RGBD keyframes near future shot regions.
6. Generate each shot from nearby anchors + unchanged `promptUsed`.
7. Treat lighting/weather/dressing changes as state transitions (§5).
8. After edits, update all affected views.
9. Export only after camera and geometry validation.

Never request a shot list as one collage prompt — each shot is its own set of target cameras inside the maintained scene.

## 9. Video: what is and isn't available

- **Early access only:** the Atlas partner system generates camera-controlled video "from one to six input images with manually designed camera paths", "up to 1 minute of video at 1440p." No public duration, FPS, codec, aspect-ratio or motion-intensity fields are documented. If you have partner access, its interface defines those controls — follow it.
- **Public beta:** build sequences as many `atlasGenerate` targets along a designed path (one frame per target, 1280 × 720) and assemble them downstream. Smoothness comes from target density; length from path length.
- From a single image: `images2PosedRGBD` → `atlasGenerate`. Each extra real view reduces invention (the launch post shows video reframing from "as few as three cameras"); one image means the model imagines everything it can't see.
