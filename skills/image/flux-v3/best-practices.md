# FLUX 3 Image — Best Practices

## 1. Detail Level: Visible Evidence Over Adjectives

Start with one sentence. Add detail only when it describes something the camera would see.

| Weak | Better |
|---|---|
| `cinematic` | `A low-angle 35mm film still with hard cyan backlight and deep amber practical lights` |
| `highly detailed` | `Individual rain droplets catch the storefront light; wet wool fibers remain visible` |
| `beautiful landscape` | `Layered volcanic ridges fade from charcoal to pale blue through morning haze` |
| `professional photo` | `Editorial portrait, 85mm lens, eye-level framing, shallow depth of field` |
| `vintage` | `Faded mid-1970s color-negative film with visible grain and cool green shadows` |
| `scary` | `A single bare bulb throws hard shadows up the stairwell; the top landing is lost in black` |

Describe **relationships**: who faces whom, who is foreground, where the light lands, what is in focus.

## 2. Positive Language

No negative prompt exists. Replace every "no X" with what occupies that space.

| Instead of | Write |
|---|---|
| no crowds | an empty promenade, a single distant figure |
| no text | clean unmarked surfaces |
| no background clutter | a plain seamless warm-gray backdrop |
| not blurry | crisp focus on the eyes, fine skin texture visible |
| no people | a deserted platform, benches empty |

An occasional exclusion inside the prompt can help for typography or asset hygiene ("the label carries no other text"), but positive description should do the work.

## 3. Composition by Shot Type

- **Portraits:** shot size + identity first, environment after.
- **Landscapes:** name foreground, midground, background; give the eye a path (road, river, light beam, repeating form).
- **Action:** the precise peak instant — body geometry, direction of travel, debris, fabric, where motion blur is and isn't.
- **Wide ratios (21:9, 2:1):** give both sides of frame something meaningful or you get dead space.
- **Vertical (9:16, 1:2):** describe stacked depth, height, up/down movement.
- **Multiple subjects:** separate each by clothing, position, pose and appearance; state how they relate.
- **Complex layouts:** plain positional language first ("in the lower left…"); upgrade to bounding boxes when positions must be exact or reproducible.

Match prompt geometry to the ratio — a "towering lighthouse" in 21:9 fights the frame.

## 4. Camera Language for Stills

No camera parameters exist; write intent into the prompt. Movement words produce the **look** of motion, not motion.

```
eye-level close-up · low-angle hero shot · overhead bird's-eye view
35mm wide-angle · 50mm natural · 85mm portrait · 200mm compressed telephoto
shallow depth of field · deep focus · rack-focus aesthetic · foreground occlusion
dutch angle · split-level underwater shot · over-the-shoulder
long-exposure light trails · panning motion blur · tracking-shot aesthetic
```

Example: "a low tracking shot with lateral background streaking and the rider sharply frozen" = panning-photo look.

**One medium, one era, one supporting effect.** Stacking "oil painting, anime, 1970s Polaroid, Unreal render" yields incoherent materials.

## 5. Typography

- Quote every visible string exactly: `reads "THE TIDE ABOVE"`.
- Front-load important text instructions.
- Keep copy short; one headline + one line beats a paragraph.
- State placement ("across the upper third"), type character ("tall weathered navy serif", "condensed sans"), hierarchy, colour (hex allowed: `#1F2A44 navy`).
- For exact positions of text blocks, put each in its own bounding box (e.g. `<title_1>`, `<En_Text_1>`).
- Validate typography at the delivery resolution (`2k`+).

## 6. Bounding-Box Layouts (new images)

Write a caption with inline `<id>` tags, then a JSON array.

```
Minimalist screen-printed poster featuring a running figure <runner_1>
centered on a chartreuse paper background <background_1>.
[
  {"id": "background_1", "bbox": [0, 0, 1000, 1000], "desc": "A flat chartreuse field with porous paper grain."},
  {"id": "runner_1", "bbox": [150, 150, 850, 850], "desc": "A black stippled silhouette running toward the left."}
]
```

Rules:
- `bbox` = `[top, left, bottom, right]`, integers **0–1000**, origin top-left. A full-width top letterbox bar is `[0, 0, 80, 1000]`.
- The grid stretches to the aspect ratio — a square box in 16:9 renders as a wide rectangle.
- IDs follow `name_N` (`character_1`, `planet_1`). Use the same ID in caption and JSON.
- Boxes **guide** composition; they don't clip. Shadows and reflections may spill.
- Very small boxes may fail to render an element — enlarge or simplify.
- Layout examples in BFL docs also use a `"hidden": [ids]` list; its behaviour is undocumented, so avoid relying on it.

## 7. Edit Rows (changing an existing image)

Reference the source as `<ref_image_0>` (0-based) in the instruction, then one row per element.

```json
{
  "id": "knight_1",
  "kind": "move",
  "from": "ref_image_0",
  "src_bbox": [500, 150, 850, 350],
  "tgt_bbox": [194, 55, 544, 255],
  "desc": "The same small armored figure, identity and armor unchanged."
}
```

| Operation | `kind` | `from` | `src_bbox` | `tgt_bbox` |
|---|---|---|---|---|
| Keep unchanged | `anchor` | `"ref_image_0"` | existing | same |
| Move / resize | `move` | `"ref_image_0"` | existing | new |
| Add / replace / recolor | `new` | `null` | `null` | target |
| Remove | — | `"ref_image_0"` | existing | `null` |

`kind` appears in BFL's current examples; include it. The removal row shape comes from BFL's prompting guide — pair it with an instruction such as "Remove <cat_1> and fill the space with the continuing floorboards."

Prompt pattern:
```
In <ref_image_0>, move <knight_1> to the upper-left cliff edge. Keep <castle_1>
exactly where it is. Keep the rest of the image completely unchanged.
[ ...rows... ]
```

Anchor the elements you care about — unanchored neighbours can drift. Local light, shadow and reflections may still update; that's expected.

## 8. Natural-Language Edits (no boxes)

```
Change only [X]. Preserve [identity / layout / lighting / palette] exactly.
```
- One conceptual change per request.
- Name the preserve list explicitly; repeat the most critical item.
- Pass the image being edited as image 1 with `aspect_ratio: "auto"`.

## 9. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Keyword soup | Weak relationships, conflicting cues | Ordered sentences |
| Subject appears late | Subject loses priority | Subject, action, framing first |
| Many unrelated styles | Incoherent materials | One medium + era + effect |
| Quality tags | Nothing | Visible camera/material evidence |
| "no X" phrasing | X persists | Describe what fills the space |
| Unquoted text | Misspelling / pseudo-text | Quote + placement + type style |
| Ratio vs composition conflict | Crowding or dead space | Match geometry to ratio |
| Ambiguous reference roles | Identity/style bleed | Explicit role per image |
| Many changes in one edit | Continuity drift | One change per request |
| Tiny boxes | Element vanishes | Bigger box or simpler element |
| Upscaling by changing tier | Composition shifts | Approved draft as image 1 |
| Expecting seeds | Can't reproduce a draft | Save the file, reuse as reference |
| Sending FLUX.2 fields | 422 error | Strip to native fields |
| Leaving grounding on for fiction | Off-model real-world details | `grounding: false` |
