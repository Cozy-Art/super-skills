# Midjourney V8 — Annotated Examples

Every example is two-part: **prompt** (with Midjourney's required inline parameters at the end) + **settings** line summarising them and anything set outside the string.

---

## 1. Character Portrait (identity master)

```
a retired Japanese watchmaker, late seventies, silver buzz cut, round tortoiseshell glasses, navy work apron, calm direct gaze, seated at a scarred wooden bench, medium close-up, soft north-window light from frame left, muted indigo and warm brass palette, documentary photograph, 85mm lens, shallow depth of field --ar 4:5 --raw --s 100 --c 3 --v 8.2
```
**Settings:** `V8.2 · 4:5 · Raw · stylize 100 · chaos 3 · SD draft → --hd final · personalization off`

**Technique:** identity traits first and specific enough to repeat; one light source with a direction; palette as two named families; Raw + default stylize keeps it documentary.

---

## 2. Cinematic Storyboard Keyframe

```
a 32-year-old Afro-Latina starship engineer, heart-shaped face, close-cropped black curls, small scar through her right eyebrow, cobalt pressure suit with an orange triangular shoulder patch, kneeling beside an open reactor panel, three-quarter medium shot from her left, blue diagnostic light from below and warm emergency light behind, tense jaw and focused hands, grounded science-fiction production still --ar 16:9 --raw --s 75 --c 0 --v 8.2
```
**Settings:** `V8.2 · 16:9 · Raw · stylize 75 · chaos 0 · weird 0 · attach identity master via Edit for later shots`

**Technique:** the identity clause is written once here and pasted verbatim into every following shot (see example 10). Chaos 0 for production; no seed reliance.

---

## 3. Environment / Panoramic Establishing

```
a basalt monastery built into a sea cliff above a stormy northern ocean, tiny amber windows, switchback stairs carved into black rock on the left, waves exploding against the lower arches at centre, distant snow peaks under layered slate clouds on the right, ultra-wide elevated establishing view, deep focus, cold cyan-gray palette with restrained warm practicals, atmospheric perspective, large-format landscape photograph --ar 21:9 --s 180 --c 8 --v 8.2
```
**Settings:** `V8.2 · 21:9 (within HD's 4:1 cap) · stylize 180 · chaos 8 · validate at 16:9 first`

**Technique:** left / centre / right each assigned so the wide frame has no dead space; warm practicals give the eye a scale cue.

---

## 4. Frozen Action

```
a female parkour athlete in a white windbreaker clears the gap between two rain-soaked rooftops, captured at the apex with knees tucked and one hand reaching forward, camera low on the landing roof, 24mm lens, diagonal composition from lower left to upper right, gravel kicked toward the lens, city lights streaked by panning blur while her face stays sharp, midnight blue and red neon, cinematic action photograph --ar 16:9 --raw --s 125 --c 8 --v 8.2
```
**Settings:** `V8.2 · 16:9 · Raw · stylize 125 · chaos 8`

**Technique:** "captured at the apex" names the peak instant; blur is assigned to the background only; one lens, one diagonal.

---

## 5. Product Fidelity (with exclusions + HD)

```
a single brushed titanium field watch standing upright on dark volcanic stone, exact circular case geometry, black dial with simple luminous markers, three-quarter product angle, narrow white strip light defining the bezel, cool gray background fading to black, faint water beads on the stone, crisp microtexture, luxury studio photography, clean negative space on the left for copy --ar 4:3 --raw --s 40 --c 0 --no hands wrists extra watches text logos --hd --v 8.2
```
**Settings:** `V8.2 · 4:3 · Raw · stylize 40 · chaos 0 · HD 2K (≈1.3 GPU-min) · --no list`

**Technique:** low stylize + Raw for geometry. The research's `--q 4` was removed — Quality is incompatible with V8.1/8.2; `--hd` gives native 2K instead. Draft this in SD, add `--hd` only on the approved prompt.

---

## 6. Poster Typography

```
a screen-printed science-fiction film poster showing a tiny radio telescope beneath an enormous red eclipse, flat geometric shapes, rough ink edges, black, cream and vermilion palette, strong centred hierarchy, the title "SIGNAL ZERO" in condensed uppercase lettering across the top, the line "ONE NIGHT ONLY" small at the bottom --ar 2:3 --raw --s 250 --c 4 --no extra text --v 8.2
```
**Settings:** `V8.2 · 2:3 · Raw · stylize 250 · chaos 4 · check type at --hd before delivery`

**Technique:** exact copy in double quotes with placement and type character; two strings only. `--no extra text` replaces "no other writing" prose. Fix stray glyphs with Edit inpaint.

---

## 7. Seamless Tile

```
hand-painted gouache pattern of lemons, glossy dark leaves and small white blossoms, evenly scattered at mixed angles, flat cobalt blue ground, visible brush texture, vintage Mediterranean ceramic feel --tile --ar 1:1 --s 200 --v 8.2
```
**Settings:** `V8.2 · 1:1 · tile · stylize 200`

**Technique:** describe a motif and a ground, not a scene with a horizon or focal subject — those break the repeat. Tile blending was improved for V8.1/8.2.

---

## 8. Style Exploration With srefs

```
a lighthouse keeper's cottage on a windswept headland at dusk, a single lit window, laundry snapping on a line --ar 3:2 --sref random --s 400 --c 20 --v 8.2
```
then, once a code is liked:
```
a lighthouse keeper's cottage on a windswept headland at dusk, a single lit window, laundry snapping on a line --ar 3:2 --sref 1234567890 --sw 150 --s 250 --c 5 --v 8.2
```
**Settings:** `V8.2 · 3:2 · sref random → locked code · style weight 150 · personalization off (one style system only)`

**Technique:** keep the content prompt short so the sref carries look. `random` is replaced by the real code after submission — copy it into the log. Replace `1234567890` with the returned code.

---

## 9. Edit — Local Change (V8.2 Edit model)

```
Change: replace the paper cup in her right hand with a clear glass of iced tea.
Keep: her face, hairstyle, camel coat, pose, framing and the window light exactly.
Look: photoreal condensation, pale amber tea, reflections consistent with the window.
```
**Settings:** `V8.2 Edit · source image attached (web: Edit in lightbox; Discord: --edit <URL>) · inpaint region over the cup · no other references`

**Technique:** Change / Keep / Look, one conceptual change. Selecting only the cup region means only those pixels change, so further edits won't degrade the face.

---

## 10. Continuity Shot (identity carried by Edit references)

```
close-up, eye level, 50mm lens, the woman from the first reference — a 32-year-old Afro-Latina starship engineer, heart-shaped face, close-cropped black curls, small scar through her right eyebrow, cobalt pressure suit with an orange triangular shoulder patch — looks frame left toward a flickering console, wiping sweat from her brow, same reactor bay as the second reference, blue diagnostic underlight and warm emergency backlight, grounded science-fiction production still --ar 16:9 --raw --s 75 --c 0 --v 8.2
```
**Settings:** `V8.2 Edit · refs: 1 = identity master (face/hair), 2 = approved reactor-bay shot (location/light) · 16:9 · Raw · stylize 75 · chaos 0`

**Technique:** identity clause pasted verbatim from example 2; roles named per reference; screen direction stated; one change from the previous shot (shot size). Replaces V7's `--oref`/`--cref`, which don't run on V8.

---

## 11. Image-to-Video From an Approved Keyframe

```
she gently brushes ash from the glowing petals as dust drifts through her headlamp beam; the camera slowly pulls back and rises, revealing the full cavern --motion low --raw --bs 1
```
**Settings:** `Video · start frame: approved V8.2 cave keyframe (16:9) · motion low · Raw · batch 1 · SD 480p for tests (2 GPU-min), HD 720p on Standard+ in Fast · extend +4 s if needed`

**Technique:** describes only what changes — subject action, environment, one camera move. No sref or still-image params (they're stripped). For a loop, swap the camera move for cyclical motion and add `--loop`; to land on the next shot, add `--end <public URL>`.
