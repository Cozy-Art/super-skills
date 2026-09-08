# Seedance 2.5 — Example Prompts

Annotated examples across the major task types, following ByteDance's documented structure. Drawn from
the recurring example projects.

Note the length: ByteDance's own published examples run 400–700 words with full shot lists. Long and
structured is the house style for this model.

---

## Example 1 — Text-to-video with timestamps

**Project:** *Shadows of Ashford* · **Unlocked**

**Prompt:**
```
Realistic period drama style, natural window light. In a county archive on
a grey winter afternoon, an elderly archivist retrieves a ledger and finds
something he was not looking for. Slow push-in throughout.

The archivist is in his sixties, close-cropped grey beard, round wire
spectacles, a moth-eaten charcoal cardigan buttoned wrong at the collar. The
room is a long archive hall with tall dusty windows on one side and floor-
to-ceiling shelves on the other. Dust hangs in the light. The camera is at
chest height, slight handheld feel, framing stable.

0-4s: The archivist walks between two shelves, scanning spines with one
hand raised. He stops, tilts his head, and pulls a heavy ledger down with
both hands. Dust lifts off the top edge.

4-9s: He carries the ledger to the window sill and sets it down. Sunlight
through the glass falls across the cover. He opens it about a third of the
way in, flattening the page with his palm.

9-14s: His scanning slows. He leans closer, lowers his spectacles slightly,
and stops moving entirely. Then he looks up and away from the book, toward
the door at the far end of the hall.

Chest-height camera, slight handheld feel, pushing in slowly across the
whole video. Natural depth of field: foreground shelving slightly blurred,
the archivist sharp. Environmental audio only — paper dragging, a floorboard
settling, distant traffic through glass. No BGM. No subtitles.
```

**Settings:** `duration: 14` · `ratio: 16:9` · 480p · `generate_audio: true`

**Technique notes:**
- **The four-part structure**: one-sentence summary, then subject and setting, then timestamped plot,
  then consistent-throughout notes
- **Continuous timeline** — 0-4, 4-9, 9-14. No gaps
- **Load balanced** — one clear beat per range, roughly 5 seconds each
- **Negative control inside the documented guarantee** — `No BGM` and `No subtitles` are exactly the
  two categories ByteDance documents as supported
- Camera stated in the summary and again in the closing notes, which is ByteDance's own pattern

---

## Example 2 — Multi-subject reference mapping

**Project:** *Iron Crown* · **Unlocked** · 6 images, 2 audio

**Prompt:**
```
Image 1 is the great hall and sets the environment, lighting and colour.
Image 2 is Queen Alisa and corresponds to Audio 1 for voice timbre.
Image 3 is General Varek and corresponds to Audio 2 for voice timbre.
Images 4-6 are the assembled court.

Cinematic historical drama, candlelit interior, slow push-in from the rear
of the hall.

0-4s: [Wide shot, locked-off] The herald strikes the floor with his staff
and the hall falls silent. Courtiers turn toward the head of the room.

4-9s: [Medium shot] Queen Alisa rises from the map table.
Dialogue (Alisa): "Then we hold the bridge until spring."

9-14s: [Medium close-up, over the shoulder] General Varek does not move.
Dialogue (Varek): "Spring is four months away, your grace."

14-18s: [Close-up] Alisa holds his gaze and says nothing. The camera settles.

Torchlight from sconces along both walls, the far end of the hall in
shadow. Fire crackle, cloth shifting, the hollow quiet of a large cold
room. No BGM.
```

**Settings:** `duration: 18` · `ratio: 21:9` · 480p · `generate_audio: true`

**Technique notes:**
- **Mapping stated in the prompt, never inside the assets.** Writing names onto the character images
  and referring to them by name causes confusion or duplication
- **Image-to-audio correspondence made explicit** — this is ByteDance's documented pattern for pairing
  a face with a voice
- **Group range** `Images 4-6` for the court, rather than three separate clauses
- Bracketed shot descriptors are ByteDance's own convention
- Dialogue in double quotes behind a speaker label

---

## Example 3 — 3D clay-model reference

**Project:** *Stellar Drift* · **Unlocked** · 1 clay video, 2 images

**Prompt:**
```
Refer to the camera movement, motion, shot rhythm and blocking in [Video 1]
as the only reference for the camera. Do not reference its visual content.
Map the grey model in [Video 1] to the flight engineer from [Image 1]. Use
[Image 2] as the corridor environment.

Near-future science fiction, practical lighting, realistic texture.

The flight engineer is in her mid-thirties, shaved head, a healed burn scar
across the left jaw, a scuffed orange pressure suit with a hand-stencilled
callsign on the chest plate. The corridor is narrow, lit by recessed strips
at knee height, everything beyond ten metres falling into dark.

0-6s: She pulls herself hand-over-hand along the service corridor, moving
away from camera, boots never touching the deck.

6-11s: She reaches a junction and catches a strut to stop herself, turning
back the way she came.

11-16s: An amber warning light begins to cycle above her, throwing her
shadow long down the corridor and pulling it back again.

Character appearance must strictly reference [Image 1] and remain consistent
throughout. Suit fans running, gloves catching on metal, a distant
structural knock through the hull. No BGM; environmental and action sounds
only.
```

**Settings:** `duration: 16` · `ratio: 21:9` · 480p · `generate_audio: true`

**Technique notes:**
- **Scope the clay reference explicitly.** "Do not reference its visual content" prevents the previz
  look bleeding into the render
- **Map models to references by name** — grey model → engineer, exactly as ByteDance's examples do
- **Still describe the target in full.** A clay reference does not replace description; the prompt
  carries appearance, environment and light
- Coarse-grained clay works better than fine-grained for motion reference

---

## Example 4 — Keyframe reference, strict alignment

**Project:** *Forgotten Waters* · **Unlocked** · 5 images

**Prompt:**
```
Use Images 1 to 5 in order as keyframes. A ship's mate crosses a storm-lit
deck at dawn, reaches the rail, and looks out at empty water. Realistic
maritime drama, flat grey dawn light, long tracking move at deck height.

The mate wears a soaked oilskin and carries a lantern in his right hand.
Between keyframes his stride stays continuous and the lantern stays in the
same hand throughout. Spray comes over the rail intermittently.

Hull working against the sea, rigging ticking, boots on wet planking, gulls
thinning out into the distance. No BGM. No subtitles.
```

**Settings:** `duration: 20` · `ratio: 21:9` · 480p · `generate_audio: true`

**Technique notes:**
- **Opening line is the documented trigger** for keyframe mode: `Use Images 1 to 5 in order as
  keyframes`
- **Keyframes align strictly; storyboards do not.** If a multi-panel board had been supplied instead,
  the visuals would be a loose plot reference only
- **Invariants named across the keyframes** — same stride, lantern in the same hand. This prevents the
  most common long-clip artefact
- The prompt fills in everything the keyframes don't show: motion between them, audio, light

---

## Example 5 — First-and-last frame (LOCKED)

**Project:** *Aurelia* · **Locked**

**Inputs:** hero bottle still as `first_frame`, lit beauty still as `last_frame` — **matching aspect
ratios**

**Prompt:**
```
A single specular highlight travels slowly down the glass edge as the
lighting builds from a near-silhouette to a full beauty exposure. Almost
imperceptible drift toward the label throughout. A crystalline chime, then a
soft low room tone settling behind it. No subtitles.
```

**Settings:** `ratio: adaptive` **(forced)** · `duration: 8` (director's choice) · 720p

**Technique notes:**
- **Locked task.** `ratio` must be `adaptive` and inherits the first frame's aspect ratio exactly
- **Matching ratios on both frames** — if the last frame differs, it gets stretched
- The frames carry the product exactly, so the prompt **never redescribes the bottle**
- Duration remains the director's choice on first/last-frame tasks, unlike editing

---

## Example 6 — Video editing (LOCKED)

**Project:** *Aurelia* · **Locked** · 1 video, 1 image

**Prompt:**
```
Editing task: replace the black marble surface in @Video 1 with brushed
brass from @Image 1, from 0-8 seconds. Change the reflection on the surface
from a hard specular line to a soft diffuse sheen. Keep the bottle, the
label, the highlight travel and the camera movement exactly unchanged.
```

**Settings:** `ratio: adaptive` **(forced)** · `duration: -1` **(forced)** · `output_format: mov`

**Technique notes:**
- **Trigger word present** — `replace` and `Editing task:`. Without one, the model does not know this
  is an edit
- **Change described as A → B**, which ByteDance recommends over "make it brass"
- **Timestamp scopes the edit** to 0-8 seconds
- **Invariants named explicitly** — this is what keeps an edit from becoming a re-generation
- `duration: -1` and `ratio: adaptive` are both forced. Output may differ by ~0.3 s — or not at all,
  since this source was itself Seedance 2.5 output
- `mov` for colour and audio-visual continuity

---

## Example 7 — Audio-only edit (LOCKED)

**Project:** *Neon Pulse* · **Locked**

**Prompt:**
```
Only edit the audio in @Video 1: remove the background music entirely and
keep the environmental sound and footsteps unchanged. Translate the spoken
line into Spanish and precisely adjust the lip movements to match the
translated speech. No subtitles. Leave all other content unchanged.
```

**Settings:** `ratio: adaptive` · `duration: -1` · `output_format: mov`

**Technique notes:**
- **Audio is independently editable** — vocals, music and sound effects can each be added, modified or
  removed without touching the picture
- **Lip re-sync on translation** is a documented capability, not a hopeful request
- Scoping with "Only edit the audio" and "Leave all other content unchanged" is the pattern that keeps
  an edit narrow

---

## Example 8 — Extension (LOCKED ratio)

**Project:** *Stellar Drift* · **Locked ratio, free duration**

**Prompt:**
```
Extend @Video 1 backward by 8 seconds. Before the corridor sequence begins,
the engineer pushes off from a hatch at the far end and begins moving toward
camera. The camera holds where it is. The system hum is already present and
steady, rising slightly as she approaches.
```

**Settings:** `ratio: adaptive` **(forced)** · `duration: 8` · `output_format: mov`

**Technique notes:**
- **Backward extension** — 2.5 extends in either direction, which is easy to overlook
- **Trigger word present**: `Extend … backward`
- Short and continuation-focused; the source supplies everything else
- "The camera holds where it is" prevents a new move at the join
- `mov` on both input and output for the cleanest join. Volume differences are smallest when the source
  was itself Seedance 2.5

---

## Example 9 — Routing away

**Project:** *Aurelia* · **Scenario:** finishing-grade master needed for broadcast

**Notes field:**
```
Seedance 2.5 is the right tool for this campaign's reference work — the
bottle, the set and the talent bind cleanly across shots, and the editing
and extension controls hold audio-visual continuity.

But 2.5 tops out at 720p. It does NOT offer 1080p or 4K; Seedance 2.0 does.
This is counter-intuitive, and consumer-surface marketing advertising 4K for
2.5 does not describe the API model's output specification.

For a finishing-grade master, either route to a model with a higher output
ceiling, or treat Seedance 2.5 output as an offline/previz pass and conform
at finishing resolution elsewhere. Do not plan a 4K delivery around this
model.
```

**Technique notes:**
- Following the D5 precedent — `notes` is where honesty lives, including recommending a different
  model where this one is the wrong choice
- The resolution ceiling is the most likely reason to route away from this model and the least obvious

---

## Quick reference

| Situation | Task | Locked? |
|---|---|---|
| Imagined scene | Text-to-video | No |
| Many identities in one frame | Reference-to-video with explicit mapping | No |
| Shot has been previz'd | Reference-to-video with clay-model video | No |
| Plot from a board, framing flexible | Storyboard reference | No |
| Framing must match supplied images | Keyframe reference | No |
| Exact opening, optionally exact ending | First / first-and-last frame | **Yes — ratio** |
| One thing in an approved clip is wrong | Video editing + trigger word | **Yes — ratio + duration** |
| Continue a clip either direction | Video extension + trigger word | **Yes — ratio** |
| Need 1080p or 4K | **Route elsewhere** — 720p ceiling | — |
| Appearance and motion from different assets | **Route to `minimax-h3`** | — |
