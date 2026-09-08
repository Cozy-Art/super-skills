# LTX-2 — Example Prompts

All examples sourced from official LTX documentation, fal.ai dev guides, and official LTX blog posts. Each includes the full prompt, technique analysis, and recommended parameters.

---

## Example 1 — Simple Character Moment (T2V, Emotive)

**Formula:** Shot scale + lighting → subject + physical cues → action sequence → camera → environment → audio  
**Mode:** T2V · **Duration:** 6–8s · **FPS:** 25 · **Mode:** Pro (facial nuance)  
**Source:** fal.ai LTX-2 Pro I2V prompt guide (T2V version)

```
Medium close-up, natural indoor light from a nearby window. A woman in her late 30s
with auburn hair pulled back sits at a wooden kitchen table, hands wrapped around a coffee
mug. She exhales slowly, eyes lowering as she stares at the mug's surface. The camera
holds steady. Outside the window behind her, rain streaks against glass. Muted tones,
soft morning diffusion, slight film grain. Sound: gentle rain against glass, distant
hum of the house, the slight sound of breath.
```

**Technique notes:**
- Shot scale leads: `"Medium close-up"` — establishes framing before anything else
- Lighting specified before character: `"natural indoor light from a nearby window"` — physical source, not a quality adjective
- Emotion via physical cues: `"exhales slowly, eyes lowering"` — not "she looks sad"
- Negative space animated: `"rain streaks against glass"` — the window background is not frozen
- Camera explicitly static: `"The camera holds steady"` — prevents unwanted drift
- Audio as three distinct layers: rain (environment) → house hum (ambient) → breath (intimate)
- No unnecessary motion: the restraint is intentional and part of the mood

---

## Example 2 — Breaking News Live Broadcast (T2V, Narrative with Dialogue)

**Formula:** Scene header → environment + lighting → character + action → dialogue in quotes → camera → action escalation → dialogue  
**Mode:** T2V · **Duration:** 10–20s Fast · **Mode:** Fast (extended duration needed)  
**Source:** Official LTX documentation prompting guide

```
EXT. SMALL TOWN STREET – MORNING – LIVE NEWS BROADCAST. The shot opens on a news
reporter standing in front of cordoned-off cars, yellow caution tape fluttering behind him.
Light is warm early sun reflecting off the camera lens. The reporter, composed but
visibly excited, looks directly into the camera, microphone in hand.
Reporter (live): "Thank you, Sylvia. And yes — this morning, here in the quiet town of New Castle,
Vermont… black gold has been found!" He gestures toward the field behind him.
"If my cameraman can pan over, you'll see what all the excitement's about."
The camera pans right, slowly revealing a construction site. With a sudden roar, a geyser
of oil erupts from the ground, blasting upward. Workers cheer and scramble. The camera
shakes slightly. Reporter (shouting): "There it is, folks — the moment New Castle will
never forget!"
```

**Technique notes:**
- Screenplay-style header: `"EXT. SMALL TOWN STREET – MORNING"` — tells the model genre and context in a compact line
- Dialogue in quotes with speaker attribution and delivery note: `Reporter (live):` and `Reporter (shouting):` — triggers synchronized lip-sync and adjusts vocal performance
- Camera move inside the narrative flow: `"The camera pans right, slowly revealing"` — camera behavior motivated by story
- Sequential phase structure: reporter intro → dialogue → camera reveal → eruption → reaction — events distributed across the clip
- Negative space animated throughout: `"caution tape fluttering"`, `"geyser erupts"`, `"workers scramble"`, `"camera shakes slightly"`
- The `"camera shakes slightly"` is a handheld motion cue tied to the action climax — physically motivated

---

## Example 3 — Product Orbit (I2V, Commercial)

**Formula:** Camera movement → reflection behavior → depth of field → particle animation → camera endpoint → audio  
**Mode:** I2V · **Duration:** 6–8s · **Mode:** Pro (client deliverable)  
**Source:** fal.ai LTX-2 Pro I2V prompt guide

```
The camera orbits 180 degrees around the product in a smooth, controlled arc.
Studio lights create evolving highlights and reflections across the surface as
the perspective shifts. A subtle depth-of-field effect keeps the product sharp
while the background gently blurs through the rotation. Dust particles float
visibly in the light beams throughout the arc. The orbit ends with the front
face of the product centered. Sound: ambient studio hum, faint mechanical click.
```

**Technique notes:**
- Zero subject description — the image already provides it; all 100% of the prompt describes motion and camera behavior
- Camera move specified with arc degree: `"180 degrees"` — not vague "orbits around"
- Intensity qualifier: `"smooth, controlled"` — restraint is appropriate for commercial product work
- Negative space animated: `"dust particles float visibly in the light beams throughout the arc"` — prevents frozen air
- Camera endpoint defined: `"ends with the front face of the product centered"` — final frame compositional target
- DOF behavior described dynamically: `"background gently blurs through the rotation"` — changes during the move
- Audio matched to scene reality: `"ambient studio hum, faint mechanical click"` — not invented sounds

---

## Example 4 — Atmospheric Walkthrough (T2V, Environment/Architecture)

**Formula:** Interior + time of day → camera path → lighting behavior → particle animation → endpoint → background vista → style → audio  
**Mode:** T2V · **Duration:** 8–10s · **Mode:** Pro or Fast  
**Source:** Official LTX blog and fal.ai guide

```
Interior of a Scandinavian wooden cabin at dawn. The camera glides forward in a
steady dolly from the doorway through the main room toward a floor-to-ceiling window.
Morning light streams through the glass, casting long golden shadows across worn oak
floorboards. Dust particles float visibly in the light beams. Steam rises from a
ceramic mug on the windowsill. Outside the glass, snow-covered pine trees are framed
against a pale blue sky with slowly drifting low clouds. The camera comes to rest
close to the window. Muted warm palette, slight vignette, analog film texture.
Sound: silence broken only by faint wind outside, soft wood creak underfoot.
```

**Technique notes:**
- Four distinct negative space animations: long shadows → dust particles → steam → drifting clouds — comprehensive coverage
- Camera path is a complete journey: `"from the doorway through the main room toward the window"` — start, middle, and endpoint defined
- Camera endpoint: `"comes to rest close to the window"` — final frame target
- Sequential phases implied by the dolly path: composition changes continuously as camera moves
- Style anchor at the end: `"muted warm palette, slight vignette, analog film texture"` — three reinforcing descriptors
- Audio as deliberate absence: `"silence broken only by..."` — the quietness is part of the atmosphere
- `"worn oak floorboards"` — material specificity (worn, not generic)

---

## Example 5 — Multi-Phase Action (T2V, Complex 20-Second Fast Mode)

**Formula:** Phase markers distributing motion across full 20-second duration  
**Mode:** T2V · **Duration:** 20s · **Mode:** Fast (only mode supporting 20s)  
**Source:** Official LTX "How to Generate 20 Second AI Videos" blog

```
Cinematic sequence, wide to tight. Initially, a wide establishing shot of a rooftop
garden in a futuristic city at dusk. The camera holds steady for a moment, taking in
rows of plants lit by warm amber grow lights against the cool blue of the skyline below.
After a beat, the camera begins a slow dolly toward a young man in his mid-20s tending
to the plants, wearing worn work clothes, focused expression. As the camera reaches
medium range, the man pauses, straightens, and turns toward the horizon where city
lights are beginning to flicker on across the skyline. Camera continues its slow dolly
to a tight close-up on his face — warm light from below, cool blue light from above,
a slight exhale visible in the cool air. Final frame: his eyes scan the horizon.
Cinematic realism. Sound: ambient city hum from far below, gentle wind, fabric movement,
distant traffic. No dialogue.
```

**Technique notes:**
- Phase markers distributing motion: `"Initially"` → `"After a beat"` → `"As the camera reaches medium range"` → `"Final frame"` — four distinct temporal markers preventing front-loading
- Camera path narrated as a complete journey: wide → medium → close-up
- Character entry delayed: man isn't introduced until the camera reaches him — mirrors real dolly cinematography
- Dual light sources: `"warm light from below, cool blue light from above"` — color contrast creating depth
- `"a slight exhale visible in the cool air"` — physical detail dependent on specific lighting and atmosphere conditions being met
- `"No dialogue"` explicitly stated — prevents the audio model from guessing
- Audio as three-layer description: city hum (far ambient) → wind (immediate ambient) → fabric movement (subject SFX) → distant traffic (depth)
- Total prompt: approximately 8 sentences — appropriate for 20-second complex sequence

---

## Quick-Start Templates by Use Case

### T2V: Intimate Character Moment
```
[Shot scale], [light source and quality]. [Character: age, hair, clothing, physical position].
[Physical action sequence]. The camera [movement or static statement].
[Background element with motion]. [Style keywords — one direction].
Sound: [ambient layer], [intimate sound], [optional: dialogue in "quotes"].
```

### T2V: Environment/Architecture Walkthrough
```
[Interior/exterior] of [specific space] at [time of day].
The camera [dolly/glide/track] from [start point] through [path] toward [endpoint].
[Light behavior: source + effect on surfaces].
[Particle or atmospheric animation in light beams].
[Background vista through window/opening with animated sky/landscape].
The camera [endpoint behavior]. [Style anchor].
Sound: [ambient layer], [material sound from camera path].
```

### T2V: Extended Multi-Phase (8–20s)
```
[Genre/style label]. Initially, [opening composition and camera state].
After a beat/moment, [camera begins movement toward subject].
As the camera reaches [distance marker], [subject action and response].
[Camera continues to endpoint]. Final frame: [final composition description].
[Style]. Sound: [ambient layers in descending intimacy]. [Dialogue or "No dialogue"].
```

### I2V: Motion from Still Image
```
The camera [movement + intensity qualifier] [around/toward/along] [subject/environment element].
[Surface or material response to camera movement: reflections, light shifts].
[Depth-of-field behavior if applicable].
[Particle or atmospheric animation throughout].
[Camera endpoint if applicable].
Sound: [ambient layer], [action-tied sound].
```

### I2V: Scene Extension / Chain
```
[Continuation of action from previous clip — begin mid-motion, no re-establishment].
[Camera path continues or transitions to: movement description].
[New beat or development in this clip].
[Negative space animation].
Sound: [consistent ambient from previous clip], [new audio element if scene changes].
```

---

## Pre-Generation Checklist

**Format:**
- [ ] Is the prompt a single flowing paragraph (not a list or bullet points)?
- [ ] Are all verbs in present tense?
- [ ] Is the prompt 4–8 sentences (or more for extended sequences)?

**Content:**
- [ ] Are emotions described as physical cues (not emotional labels)?
- [ ] Is every static region of the frame explicitly animated?
- [ ] Is motion distributed across the full duration with phase markers (for 8s+ clips)?
- [ ] Are lighting sources named specifically (not vaguely)?

**Mode-specific:**
- [ ] T2V: Are all 6 elements present (shot, scene, action, character, camera, audio)?
- [ ] I2V: Is the prompt describing only motion and changes (not re-describing the image)?

**Parameters:**
- [ ] Is Fast or Pro selected appropriately for the use case?
- [ ] Is duration matched to the described action complexity?
- [ ] Is `generate_audio` explicitly set (platform defaults differ)?
- [ ] Is seed noted from any strong result for reproducibility?

**Audio:**
- [ ] Is audio described in at least 2 layers (ambient + action-tied)?
- [ ] Is dialogue in quotation marks with speaker attribution if needed?
- [ ] Is "No dialogue" stated explicitly if audio should be ambient only?
