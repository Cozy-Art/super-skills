# Magnific One — Best Practices

## 1. Start With the Medium

The medium sets the world the art director works in. Name it first, then the subject.

```
photo · editorial photograph · film photography · documentary sports photograph
gouache illustration · risograph · linocut · watercolor
3D render · claymation · diorama · knitted 3D miniature world
poster · minimal bold poster · typography · magazine cover · campaign key visual
```

Pick **one** primary medium. One deliberate hybrid at most ("claymation figures in a real photographed kitchen").

## 2. The Control Dial

Magnific's own progression. Each step trades the model's art direction for your control.

| Level | Prompt | Use |
|---|---|---|
| One word | `gossip` | Pure exploration — let the art director choose everything |
| Subject | `two grandmothers gossiping on a bench` | Lock *what*, leave *how* open |
| Story | `…in matching lilac tracksuits, one hiding a croissant behind her back` | Lock the narrative detail |
| Full direction | `…park bench in Madrid. Side view at bench height, both in profile. Late afternoon sun through plane trees. Soft pastel palette, lilac against warm terracotta.` | Lock viewpoint, light, palette |

Default habit: explore at Subject/Story in Draft, move to Full direction in Final.

## 3. Describe Causes, Not Effects

Adjectives that name a feeling give the model nothing to render. Name what *produces* the feeling.

| Weak | Stronger |
|---|---|
| premium product shot | brushed aluminum bottle on a dark slate plinth, one soft window reflection, restrained black-and-silver palette |
| cinematic | a candid mid-scene moment, practical light from the table lamp, deep background falloff, foreground occlusion |
| dynamic | runner crossing above a glass floor, worn sole close to camera, directional motion blur, colored light leaks |
| cozy | coarse wool blanket, low amber firelight, condensation on the window, cool rain outside |
| epic landscape | low basalt rocks in the foreground, a small red hut in the middle distance, snow ridges fading into cloud |

## 4. Say Each Thing Once

Repetition with synonyms makes Magnific One **drop details**. Not "cinematic, dramatic, movie-like film still" — pick one phrase. One light setup, one composition statement, one mood word. Use short sentences, one visual function each.

## 5. One Sharp Idea

For photography, subject + decisive moment beats a lens-spec inventory. "A pit mechanic carrying a tire through smoke" directs more than "85mm f/1.4, ISO 400, shallow DOF". Add camera language only when a specific viewpoint matters.

What to add, only when it matters:
- **Identity:** age range, face geometry, hair, one distinctive feature, signature wardrobe.
- **Action:** one observable instant — stills can't show a timeline.
- **Environment:** only details that serve story or composition.
- **Composition:** viewpoint, placement (thirds), fore/mid/background, negative space.
- **Light:** a source already in the scene, direction, softness, time, temperature.
- **Material:** brushed, knitted, glazed, translucent, oxidized.
- **Palette:** 2–4 colours and where they live ("lilac against warm terracotta").

## 6. Corrective Lines

Magnific's guide supplies compact repair lines, each changing one property while leaving the rest alone. Append **one** per iteration to the prompt that produced the near-miss.

| Problem | Line |
|---|---|
| Yellow whites | `Finish it under natural light (white balance around 5500K), with no yellowish tint or color cast.` |
| Wrong / extra text | `Reproduce the text exactly as written. No other logos or text.` |
| Too centered | `Subject off-center on the right third, foreground elements out of focus.` |
| Looks posed | `Make it feel like a still from a film: a moment caught mid-scene, with the light coming from what's already in the room.` |
| Unwanted people/clutter | `No people, no vehicles, no text.` |
| New light only | `Keep everything in the image exactly as it is. Change only the light: early morning, low sun from the left, long soft shadows.` |
| Rework without moving anything | `Keep the exact camera angle, crop, horizon and the position, scale and silhouette of every object. Do not move, add or remove anything.` |
| Too HDR | `Soft, natural contrast, no harsh outlines, real-world texture.` |

The "keep everything" lines assume you're reworking an existing image in the app. The API has no source-image field (`reference_images` are style only), so via API they act as reinforcement of a restated prompt, not a true edit.

## 7. Composition by Subject Type

- **Character:** stable identity block first, then pose, shot size, placement, eyeline.
- **Landscape:** name foreground anchor, middle-distance subject, background — plus where the negative space is.
- **Action:** describe the evidence of motion — what's sharp, what's blurred, what's frozen mid-air.
- **Wide ratios (`21:9`, `3:1`, `2:1`):** give both sides of frame a job, or leave deliberate negative space for copy.
- **Vertical (`9:16`, `2:3`):** stacked depth, height, upward/downward movement.
- **Multiple subjects:** separate each by position, clothing and pose; state how they relate.

## 8. Implied Camera Motion

Output is a still. Motion words only produce the *look* of motion — write the visual evidence.

| Camera idea | Still-image phrasing |
|---|---|
| Push-in | intimate close framing, strong perspective, shallow foreground falloff |
| Pan / tracking | subject sharp, background streaked horizontally, side-on movement |
| Orbit | three-quarter hero view, curved highlights revealing form |
| Handheld | slightly off-level, foreground occlusion, candid mid-scene timing |
| Locked-off | symmetrical frame, fixed horizon, no motion blur |
| Crane reveal | high oblique viewpoint, foreground roofline opening onto the scene |

## 9. Typography

- Quote every visible string: `headline "OPEN LATE" painted across the awning`.
- State placement and hierarchy ("smaller line bottom-left").
- Keep copy short — one headline, one supporting line.
- Add `Reproduce the text exactly as written. No other logos or text.`
- Generated type can still drift. For client-ready copy, keep the image and set type in Auto Layers or Designer. Brand Kit also does not guarantee exact typography or exact colour values.

## 10. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Writing a thesis before exploring | Kills the built-in art direction | Medium + subject + moment in Draft |
| Synonym stacking | Details dropped | Say it once |
| Quality / feeling adjectives | Nothing visible to render | Name materials, light, framing, palette |
| Several unrelated media | Muddled treatment | One medium, one hybrid max |
| A sequence of events | Unclear still | The decisive instant |
| `tiles: 8` at `16:9`/`21:9`/`9:16` | Ratio approximated | `tiles: 16` |
| Setting `quality`/`resolution` in Draft | Silently ignored | Draft is medium / 2K |
| Expecting Brand Kit in Draft | Not applied | Explore free, apply kit in Final |
| Normal references used as a look (app) | Read as content | Use the Style tab |
| Re-describing the reference look in the prompt | Redundant, fights the reference | Spend words on scene, action, composition |
| Stacking all corrective lines | New conflicts | One per iteration |
| Rerolling for a typo | Lost composition, wasted credits | Auto Layers / Designer |
| `mode: "final"`, `quality: "max"`, `negative_prompt`, `seed` | Request rejected | Valid fields only |
| Video controls (duration, camera path) | Not supported | Animate in a video model |
