# PixVerse V6 — Example Prompts

All examples sourced from official PixVerse V6 documentation, PixVerse blog, and validated benchmark tests.

---

## Example 1 — Corporate Headshot / Walk (Character Focus, Commercial)

**Formula:** Subject → action + pace → environment → camera → style + negative  
**Mode:** T2V or I2V · **Aspect:** 16:9 · **Duration:** 5–8s · **Resolution:** 1080p  
**Source:** PixVerse V6 official prompt guide

```
Professional woman in her early 40s, black blazer and white shirt, confident expression.
Walking steadily through a modern glass-and-marble office lobby toward the camera.
Medium tracking shot from chest height, slight upward tilt.
Corporate commercial aesthetic, cool neutral tones, sharp focus, shallow depth of field.

Negative: blurry, extra fingers, morphing, inconsistent lighting, duplicate limbs.
```

**Technique notes:**
- Subject leads: physical description before any action or environment
- Pace qualifier: `"steadily"` — prevents ambiguous speed interpretation
- Camera: 2 moves (`"tracking"` + `"upward tilt"`) — within the safe limit
- Style: `"corporate commercial aesthetic"` is a validated high-signal style anchor for V6
- `"shallow depth of field"` describes a lens behavior, not a vague quality term
- Negative prompt targets the most common character generation artifacts

---

## Example 2 — Action / Destruction (Motion Focus, High Energy)

**Formula:** Camera angle + tracking → subject + physical details → environmental chaos → motion cues → quality  
**Mode:** T2V · **Aspect:** 16:9 · **Duration:** 5–10s · **Resolution:** 720p/1080p  
**Source:** PixVerse V6 benchmark test (official blog)

```
A low-angle fast tracking shot of a giant armored ape monster running through a city.
Buildings falling. Smoke and broken stone in the air. Blue cold lighting.
Handheld camera shake. Sparks from the metal joints. Glowing orange eyes, open mouth.
The monster stays centered as debris reacts to its footsteps.
Professional movie quality, cinematic color grade, sharp subject focus amid particle chaos.

Negative: subject blur, subject lost in background, unnatural physics, visual noise.
```

**Technique notes:**
- Camera leads for action content: `"low-angle fast tracking shot"` — angle + speed + movement type all in one clause
- Physical chaos described literally: `"buildings falling," "smoke and broken stone in the air"` — not "epic destruction"
- `"Handheld camera shake"` explicitly chosen for action — appropriate for this genre
- `"Sparks from the metal joints"` — hyper-specific physical detail, not a vague quality term
- `"The monster stays centered as debris reacts"` — spatial relationship instruction preventing subject drift into background
- Negative prompt targets subject-specific artifacts (blur, background absorption, physics)

---

## Example 3 — Product Commercial (Detail Focus, Commercial)

**Formula:** Shot scale + subject + surface → environmental motion → camera + focus behavior → style → audio + negative  
**Mode:** I2V or T2V · **Aspect:** 9:16 (social) · **Duration:** 5–8s · **Resolution:** 1080p  
**Source:** PixVerse V6 benchmark test

```
Extreme macro close-up of a luxury matte-black ceramic mug on a natural wood surface.
Steam rises slowly from the surface. Soft warm window light from the left.
Camera: locked-off, gentle rack focus from rim to surface, no motion.
Style: premium product photography aesthetic, warm neutral tones, high material detail,
shallow depth of field with bokeh background.
Sound: quiet ambient room tone, faint ceramic-on-wood contact sound.

Negative: warping, extra objects, logo distortion, overexposed highlights.
```

**Technique notes:**
- Shot scale leads: `"Extreme macro close-up"` — sets the spatial relationship before anything else
- `"Matte-black ceramic"` — material is named specifically (not "black mug")
- Environmental motion to prevent frozen frame: `"Steam rises slowly"` — the only motion in a locked-off shot
- `"Locked-off"` explicitly stated — critical for product work to prevent unwanted camera drift
- Rack focus described as a physical camera behavior: `"from rim to surface"` — not "focus on the details"
- Style block uses `"premium product photography aesthetic"` — a genre anchor
- Audio appropriate to the scene: ambient room tone (light) + specific material contact sound
- Negative targets product-specific issues (warping, extra objects, logo problems)

---

## Example 4 — Anime Character with Japanese Dialogue and LipSync

**Formula:** Subject (physical specifics) → action → environment → camera → style + dialogue in quotes + negative  
**Mode:** T2V with TTS lip-sync · **Aspect:** 16:9 · **Duration:** 8–10s  
**Source:** PixVerse V6 official benchmark (multilingual lip-sync test)

```
A male fox demon with fox ears and tail. Gentle eyes. Wearing dark traditional clothing.
He turns toward a young woman and smiles softly. His tail moves slowly behind him.
Soft warm garden setting at dusk, lanterns in background.
Camera: medium two-shot, slow dolly-in during dialogue.
Style: anime cinematic, soft light, warm amber tones, fluid character animation.
Maintain character features consistently across the full clip.

Japanese dialogue — Male (Gentle): 'お疲れ様、夜の古街は危ないですよ.'
Female (Surprised): 'あ、あなたは…妖ですか？'

Negative: identity drift, face morph, ear shape change, tail disappear, stiff movement.
```

**Technique notes:**
- Character identity anchors: `"fox ears and tail"` + `"dark traditional clothing"` + `"gentle eyes"` — distinguishing features the model can maintain
- Physical action (not emotion): `"smiles softly"` + `"tail moves slowly behind him"` — observable, renderable
- `"Maintain character features consistently across the full clip"` — explicit consistency instruction
- Dialogue with speaker + emotional tone: `"Male (Gentle):"` and `"Female (Surprised):"` — tone guidance for TTS vocal performance
- Negative targets character-specific anime drift artifacts: ear shape, tail disappearance, face morphing
- Camera: `"slow dolly-in during dialogue"` — single camera move timed to the audio action

---

## Example 5 — Multi-Shot Brand Narrative (Full Production)

**Formula:** Multi-shot structure with consistent vocabulary + environment anchor + audio transition  
**Mode:** T2V with multi-shot engine · **Aspect:** 16:9 · **Duration:** 10–15s  
**Source:** PixVerse V6 benchmark and official guide

```
Shot 1:
Aerial establishing shot of a modern urban architecture firm's glass office building at dawn.
Golden light on glass façade. Camera slowly cranes down to street level.
Cold blue shadows, warm sunrise backlighting. Documentary architectural style.

Shot 2:
Interior — same building. Young architect in casual black clothing stands at a large drafting
table reviewing blueprint drawings. Natural morning light through floor-to-ceiling windows.
Medium tracking shot following from side at chest height.
Same building materials and light quality as Shot 1. Warm neutral interior tones.

Sound: ambient city sound fading in Shot 1 → muffled interior silence in Shot 2,
paper shuffling, pen on drafting surface.

Negative: character drift, lighting jump, style mismatch between shots, extra people.
```

**Technique notes:**
- Shot 1 establishes environment vocabulary: `"glass office building"`, `"golden light on glass façade"`, `"documentary architectural style"`
- Shot 2 explicitly references Shot 1: `"same building"`, `"Same building materials and light quality as Shot 1"` — the multi-shot engine uses these text anchors
- `"Same building materials and light quality"` — consistent vocabulary enables spatial tracking across shots
- Camera: Shot 1 = single move (`crane down`); Shot 2 = single move (`tracking from side`) — each shot within the 2-move limit
- Audio transition described explicitly: `"fading in Shot 1 → muffled interior silence in Shot 2"` — the audio transition narrative
- Negative prompt covers the multi-shot specific failure modes (character drift, lighting jump, style mismatch)

---

## Quick-Start Templates by Content Type

### Corporate / Commercial Character
```
[Job title/context] [gender] in [age range], [clothing], [expression].
[Action + pace] through [specific environment, materials, lighting].
[Shot size] [camera movement], [angle or tilt if applicable].
[Style anchor: "corporate commercial aesthetic"], [color grade], [depth cue].

Negative: blurry, extra fingers, morphing, inconsistent lighting.
```

### Product Close-Up
```
[Shot scale: "Extreme macro close-up / Close-up"] of [product + material + color] on [surface + material].
[Environmental motion: steam, smoke, droplets, particles].
[Lighting: source + direction + quality].
Camera: [locked-off or minimal move], [focus behavior].
[Style: "premium product photography aesthetic"], [tones], [material detail level].
Sound: [ambient room tone], [material-specific contact sound].

Negative: warping, extra objects, overexposed highlights.
```

### Action / High Energy
```
[Camera angle + speed] of [subject + physical identity].
[Environmental chaos in literal physical terms].
[Handheld camera shake / gimbal-stable] + [specific physical details].
[Spatial relationship: subject position relative to environment].
[Style: "cinematic color grade"], [quality].

Negative: subject blur, subject lost in background, unnatural physics.
```

### Multi-Shot Narrative
```
Shot 1:
[Camera] establishing [environment + time of day + lighting].
[Movement]. [Style keywords].

Shot 2:
[Subject with SAME descriptors as Shot 1 if they appear].
[Same environment vocabulary]. [New action]. [Camera]. [Same style keywords].

Sound: [audio in Shot 1] → [audio transition] → [audio in Shot 2].

Negative: character drift, lighting jump, style mismatch, extra people.
```

### Lip-Sync / Dialogue
```
[Subject + physical identity anchors].
[Action with physical cues, not emotional labels].
[Camera: shot size + single camera move].
Style: [aesthetic], [light], [tone].
Maintain [specific features] consistently.

[Language] dialogue — [Speaker (Tone)]: '[dialogue text]'

Negative: identity drift, face morph, stiff movement.
```

---

## Pre-Generation Checklist

**Prompt structure:**
- [ ] Subject description leads the prompt?
- [ ] One primary action described with a pace qualifier?
- [ ] Maximum 2 camera moves specified?
- [ ] All descriptors are literal and observable (not abstract)?
- [ ] Style uses specific genre anchors (not vague adjectives)?
- [ ] Negative prompt included?

**Multi-shot specific:**
- [ ] Core character descriptors repeated verbatim in every shot?
- [ ] Environment vocabulary identical across shots (same exact words)?
- [ ] Style keywords consistent across all shots?
- [ ] Audio transition described between shots?

**Parameters:**
- [ ] Draft at 360p/540p first?
- [ ] `thinking_type: enabled` for drafting, `disabled` for finals?
- [ ] Aspect ratio set before generation (16:9, 9:16, 1:1)?
- [ ] Audio mode selected (and is it the last step in the pipeline)?
- [ ] Seed noted from any strong result?

**Limitations check:**
- [ ] No crowds with individual face requirements?
- [ ] No facial extreme close-up with high motion?
- [ ] No in-frame text that must be legible?
- [ ] No 3+ camera moves in a single shot?
- [ ] 1080p + `motion_mode: fast` not combined (documented incompatibility)?
