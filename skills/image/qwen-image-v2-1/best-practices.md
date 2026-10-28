# Qwen-Image-2.1 — Best Practices

## 1. Text-to-Image Grammar: Describe the Frame as an Observer

Qwen's official T2I rewriter writes **present tense, third person, declarative** prose — no "create", "make sure", "you", "the AI should". Copy that voice.

1. **Opening sentence** (~20 words): medium, style, subject, background/palette.
2. **Spatial walk**: background → top band → body left-to-right → bottom band. For a single subject: background → pose → face → body → held objects → frame edges. Roughly a third of sentences can open with a positional phrase ("In the lower-left corner…", "Along the right edge…").
3. **One lighting sentence**: source, direction, hardness, colour, shadows.
4. **One closing sentence**: "The overall composition…" — balance, palette, style, mood. Only one.

| Weak | Better |
|---|---|
| `cinematic` | `A wide horizontal film still from a low camera, hard cyan backlight and warm amber practicals` |
| `highly detailed` | `Rain beads on the waxed canvas; individual threads of the frayed cuff are visible` |
| `beautiful woman` | `A woman in her forties with silver-streaked short hair and a calm, analytical gaze` |
| `vintage` | `Faded 1970s colour-negative film, visible grain, cool green shadows` |
| `masterpiece, 8K, best quality` | *(delete — the official rewriter bans quality boosters)* |

Add detail only when it resolves a visual decision. Contradictions ("orthographic fisheye", "flat vector photorealism", sunrise + overhead noon) compete with the scene.

## 2. Positive Language

`negative_prompt` does nothing at the default CFG 1.0. Qwen's edit enhancer also says "state requirements affirmatively."

| Instead of | Write |
|---|---|
| no people | a deserted platform, every bench empty |
| no text | clean unmarked surfaces |
| no clutter | a plain seamless warm-grey backdrop |
| no extra fingers | both hands relaxed, five fingers each, naturally posed |
| not blurry | crisp focus on the eyes, fine skin texture |

## 3. Edit Grammar: Imperative and Surgical

```
[Replace / Remove / Add / Change] [precise target + location] [with/to observable result].
Preserve [identity, pose, composition, camera, lighting, medium, and all untargeted content].
```

- Lead with the operation. Name the target by type, position and role ("the ceramic mug on the left edge of the desk").
- Describe **the change** in concrete detail; describe everything else with **one broad preservation clause**. Restating the whole preserved scene invites regeneration and drift.
- Edit too weak? Make the requested attribute stronger and more visible — preservation applies to everything *else*.
- One operation per pass. Stage hard multi-part edits.
- Single image: "the image". Never invent tags for one image.
- Ratio: leave it out of prose; for single-image edits the output follows the source unless you pass new `width`/`height`.

## 4. Multi-Image Roles

Tags are 1-based and follow list order: `image=[a, b, c]` → `<image1>`, `<image2>`, `<image3>`. Qwen's edit enhancer calls this format "mandatory and non-negotiable".

Every image gets exactly one job: **canvas · identity source · pose source · garment · product · background · style reference**.

```
Use <image3> as the canvas and preserve its composition, perspective and lighting.
Place the person from <image1> on the right side of the crosswalk, preserving their
exact facial identity and body proportions. Dress them in the complete outfit from
<image2>. Match <image3>'s rainy light and reflections.
```

- Name the canvas explicitly — it anchors composition.
- Earlier images are attended by later ones; put the strongest anchor (identity or canvas) where you want it read first, and keep that order across a project.
- Ten unlabelled references are worse than three with roles. Drop any image without a job.
- Style refs: say *only* palette / lighting / texture / line treatment transfers, and that content and layout come from the canvas.

## 5. Typography, Layouts, Infographics

- Every visible string in **straight double quotes**, copied character-for-character, in its own script. Quoted strings should be monolingual.
- Give each string: position, hierarchy, size, weight/character, colour. `Across the upper third, a large condensed off-white headline reads "MEMORY HAS MASS" on two lines, strict left alignment.`
- Line breaks: say "on two lines" / "a second line reads…", not a newline.
- Charts and data: axes, tick labels, legend entries, series names and cell values are text — spell them out.
- Small illegible marks: call them "small blurred fine print" rather than inventing body copy.
- Walk layouts in reading order: background → top band → left/centre/right body → bottom band.
- Validate at the 2K preset; dense text may follow better at `true_cfg_scale` 2.0 (watch for over-sharpened edges).

## 6. Transparency (RGBA)

Use the official wrapper verbatim around the subject:

```
This is an RGBA image with transparency. <subject description>. The image has alpha channel and the background is transparent.
```

- Describe only the object; keep shadows inside the silhouette ("no cast shadow beyond its silhouette" — or better, "contact shadow contained within the base").
- Save as PNG/WebP with alpha. JPEG discards it.
- In ComfyUI, split alpha before any 3-channel node (`SplitImageWithAlpha`), rejoin after.
- Check semitransparent edges (hair, glass, smoke) at full size.

## 7. Local Edits: Circles, Paint, Masks

The model supports edits indicated by **circles, painted annotations, or separate masks**.

```
Replace only the object inside the red circle with a closed black notebook aligned to
the same surface perspective. Remove the red annotation in the result. Preserve every
element outside the marked region.
```

- Name the mark's colour and shape. Keep the mark inside the target.
- Say "remove the annotation" — painted strokes are part of the input pixels.
- If the mark colour could plausibly appear in the result, state the colour you want ("the new jacket is navy").
- Validate edges and semitransparent detail around the region.

## 8. Action and Camera Language for Stills

No temporal controls exist. Describe a **decisive instant** and the photographic evidence of movement:

- Body mechanics, gaze, limb direction, airborne debris, directional fabric, where motion blur is and isn't.
- Camera intent as a single viewpoint: "viewed from twenty centimetres above wet pavement, tracking parallel to the rider" → panning-photo look.
- Lens character: "wide 28 mm perspective", "85 mm portrait compression", "deep focus", "shallow depth of field on the eyes".
- One medium, one era, one supporting effect.

Composition order: ratio from deliverable → hero + beat → placement (thirds / symmetry / edge tension / negative space) → depth layers → camera height/angle → lens → one motivated key light → palette and mood.

Match prompt geometry to the frame: give both sides of a 16:9 something to hold; stack depth vertically for 9:16.

## 9. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Subject-only prompt | Flat, generic frame | Medium, placement, light, palette, mood |
| Subject appears late | Ignored or demoted | Hero subject + action in first sentence |
| Quality tags | Nothing useful | Visible material/camera evidence |
| "no X" with CFG 1.0 | X persists | Describe what fills the space |
| Omitting `width`/`height` | ~1 MP at source ratio | Pass a 2K preset |
| Ratio written in prompt | Wrong aspect | `width`/`height` arguments |
| Unquoted text / too much copy | Misspelling, pseudo-text | Quote exact strings, fewer of them, position + style |
| Redescribing a face instead of pointing to ref | Identity drift | "the person from <image1>" + preserve |
| Restating the whole scene in an edit | Composition drift | Lead with the local operation + one preserve clause |
| References without roles | Identity/style bleed | One role per `<imageN>`, name the canvas |
| Many edits in one pass | Leakage | One operation per pass |
| Painted mark not mentioned | Mark stays / wrong region | Name colour + "remove the annotation" |
| Same seed, different result | `use_kv_cache`, size, order or precision changed | Lock the full recipe |
| Old recipes (CFG 4, 50 steps) | Over-cooked output | 40 steps, CFG 1.0 |
| RGBA saved as JPEG | Alpha lost | PNG |
| 4K target size | Weaker adherence | Generate at 2K, upscale downstream |
| Hosted prompt extension left on | Wording rewritten, non-reproducible | `promptExtend: false` for exact control |
