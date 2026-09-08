# HappyHorse 1.0 — Example Prompts

All examples sourced and annotated from official HappyHorse 1.0 documentation. Each example includes the formula label, the complete prompt, and technique notes.

---

## Example 1 — Simple T2V (Character Focus)

**Formula:** Subject + Scene + Motion  
**Target length:** ~20 words  
**Best for:** Single-shot character movement, social content, quick ideation

```
A young woman in a red coat walks down a wet city street at night,
neon reflections on the pavement, slow tracking shot.
```

**Technique notes:**
- Subject and action come first — anchors the render
- Environment in the middle — sets scene without competing
- Camera cue at the end — receives maximum weight for motion behavior
- No audio specified here; add for production use: `footsteps on wet pavement, distant traffic, no music`
- At ~20 words, this is at the ideal token economy

**Production upgrade:**
```
A young woman in a red coat walks down a wet city street at night,
neon reflections on the pavement. Footsteps on wet pavement, distant
traffic hum, occasional car horn. Slow tracking shot. 1080p, 9:16, 6 seconds.
```

---

## Example 2 — Dialogue / Lip-Sync Scene

**Formula:** Scene + Subject + Action + Audio + Camera  
**Target length:** 60–80 words acceptable for dialogue complexity  
**Best for:** Talking head, character conversation, multilingual content

```
A sunlit Paris café, late morning. A woman in her 30s with dark curly hair
sits across from her friend at a marble table, warm amber light from the
window. She leans forward, smiling, and speaks — dialogue in French:
"Tu as l'air fatigué ce matin, ça va?" No music, ambient café chatter
and espresso machine hissing, occasional ceramic clink. Locked-off medium
two-shot, eye level. 1080p, 16:9, 8 seconds.
```

**Technique notes:**
- Dialogue in quotes triggers the lip-sync pathway
- Language specified explicitly (`in French`) ensures phoneme alignment
- Three-layer audio described: foreground (dialogue) + midground (clinking) + background (chatter + machine)
- `Locked-off` camera chosen for dialogue stability — moving camera competes with lip-sync
- `No music` stated explicitly to prevent guessed audio bed
- Scene set before subject — location as anchor for a conversation shot

---

## Example 3 — Environment / Landscape

**Formula:** Scene + Timing + Motion + Camera + Lighting  
**Target length:** 40–60 words  
**Best for:** Establishing shots, nature content, atmospheric B-roll

```
A vast Mongolian steppe at golden hour, amber light cutting low across
the grassland. Wind sweeps through the tall grass in waves, a lone eagle
circles far above. Helicopter aerial establishing shot sweeping left to
right, gradual reveal of a distant mountain range. Soft orchestral
ambient, wind through grass. 1080p, 16:9, 10 seconds.
```

**Technique notes:**
- No character anchor needed — environment IS the subject
- Camera cue at end with directional specification: "sweeping left to right"
- Audio explicitly described: orchestral ambient + wind foley (two layers)
- 10-second duration justified for landscape reveal — sufficient to show the sweep
- "Gradual reveal" is both a motion description and a narrative instruction

---

## Example 4 — Action / Motion Sequence

**Formula:** Subject + Action + Scene + Motion Intensity + Camera  
**Target length:** 50–70 words  
**Best for:** Sports, athletic content, high-energy sequences

```
A sprinter in a red athletic vest at the finish line of a 100-meter track,
face tight with exertion, jaw clenched. He breaks the finish tape with a
forward chest thrust, arms swinging at maximum amplitude. The background —
blurred track and audience — rushes past. Fast handheld tracking shot with
slight shake matching the impact moment. No music, crowd roar building to
a peak, finish-line PA announcement. 1080p, 16:9, 5 seconds.
```

**Technique notes:**
- Motion intensity explicitly named: "maximum amplitude" — the model reads intensity qualifiers
- Handheld shake specified as a motion cue **matched to the action** — purposeful camera behavior
- Background described as motion blur — sets physics expectation
- Audio peak timed to visual climax: "building to a peak, finish-line PA announcement"
- 5 seconds for a single athletic beat — correct duration for this use case

---

## Example 5 — Camera Movement Focus

**Formula:** Scene + Subject + Single Camera Move + Lighting  
**Target length:** 40–60 words  
**Best for:** Cinematography demos, contemplative scenes, focus pulls

```
Dim workshop interior, 1920s. A glassblower shapes molten glass on a
blowpipe, furnace light illuminating his face in deep amber and orange.
Slow dolly-in from medium shot to close-up on his face as the glass bulb
inflates. Hard light from the furnace mouth, deep shadows. Ambient:
furnace hiss, low roar of fire, metal tapping. 1080p, 16:9, 8 seconds.
```

**Technique notes:**
- Single camera move (dolly-in only) — not stacked with any second cue
- Move is purposeful and tied to action: reveals face "as the glass bulb inflates"
- Furnace light described specifically (direction, color temperature) — not "dramatic lighting"
- Audio tied directly to visible action: furnace, fire, metal
- "1920s" period anchor relies on model's world knowledge — effective for well-documented eras

---

## Example 6 — Style / Mood Variation (3D Cartoon)

**Formula:** Style tag + Scene + Subject + Motion + Color  
**Target length:** 40–60 words  
**Best for:** Animation, fantasy, stylized content, non-photorealistic output

```
3D cartoon style, a surreal dream where everything is made of corn. Two
small characters ride a corn train through giant corn cobs and kernels.
The scene is bathed in warm golden light, dreamlike quality. The train
moves smoothly, its wheels shaped from perfectly formed kernels. Wide
cinematic shot, slight crane up as the train rounds a bend, soft
whimsical orchestral score. 1080p, 16:9, 6 seconds.
```

**Technique notes:**
- **Style keyword leads the prompt** — this sets the rendering mode before the model starts generating
- Stylized content is the one case where style descriptors like "dreamlike quality" carry weight
- Camera cue at end, as always: "slight crane up as the train rounds a bend"
- Audio matched to tone: "whimsical orchestral score" — note this is the one case where a music style descriptor is useful (not generic "cinematic music")
- "Perfectly formed kernels" is a detail that signals intentional stylization

---

## Example 7 — Multi-Shot Narrative Sequence

**Formula:** Protagonist description once + numbered shot beats with individual camera/audio  
**Target length:** 100–150 words total across all shots  
**Best for:** Short films, product narratives, brand storytelling, social series

```
Protagonist: A female florist in her late 20s, red apron, dark hair in a
loose bun, warm natural makeup.

Shot 1 (0–2s): Wide shot — florist arranges a large peony bouquet on a
wooden worktable in a sunlit shop, morning light through windows, ambient
acoustic guitar, clipping scissors.

Shot 2 (2–5s): Medium tracking shot — she carries the finished bouquet
from the workbench toward the front counter, footsteps on hardwood,
bouquet rustling.

Shot 3 (5–8s): Close-up, locked-off — the bouquet placed on the counter
in front of a customer's hands, soft laughter from both, natural room
tone, no music.
```

**Technique notes:**
- Protagonist described **once at top** — not repeated per shot (saves tokens, prevents drift)
- Each shot independently prompted with its own camera direction and audio
- Character consistency implied across all three beats by the protagonist anchor
- Shot timing adds up to 8 seconds total
- Audio evolves naturally across shots: music → footsteps → natural room tone
- "No music" on Shot 3 is a deliberate choice that creates intimacy — stated explicitly

---

## Additional Patterns

### Product Close-Up
```
A [product name/description] on [surface], [ambient light description].
[Specific motion: rotate/lift/open]. [Camera: close-up, movement direction].
[Audio: product sounds, no music]. 1080p, 1:1, 5 seconds.
```

### Talking Head (English)
```
[Location, time of day]. [Subject description], [posture/gaze direction].
[Subject] says — dialogue in English: "[line]" — EXACT, verbatim.
[Audio: room tone description, no music]. Locked-off medium shot, eye level.
1080p, 16:9, [duration]s.
```

### Environment Reveal with Audio Arc
```
[Location, time of day]. [Key visual elements].
[Motion: what moves, how].
[Camera: single directional move].
[Lighting: direction, quality, temperature].
[Audio: foreground foley], [midground action sounds], [background ambient].
[Music: on/off + description if on].
1080p, 16:9, [8–12]s.
```

### I2V Animation (Motion Only)
```
[Single motion description: what moves, direction, intensity].
[Camera: one cue, small scale].
[Audio: foreground + midground + background].
[No music / Music: description].
[duration]s.
```
*Do not describe the image — it is already the first frame.*

### Video Edit (Surgical)
```
Change only [specific element]. Keep [A], [B], [C] exactly the same.
[A], [B], [C] remain unchanged.
Reference: [Image 1] — [describe the reference image's role].
```

---

## Quick Diagnostic: Is My Prompt Correct?

Run through this checklist before generating:

- [ ] Is subject/action first?
- [ ] Is camera cue last?
- [ ] Is prompt ~20 words for a simple shot? (Or using multi-shot format if complex?)
- [ ] Is dialogue in quotation marks with language specified?
- [ ] Are all three audio layers named?
- [ ] Is there a music direction (on/off)?
- [ ] Are there 2 or fewer camera cues?
- [ ] Have I avoided "cinematic," "epic," "masterpiece," and booru tags?
- [ ] In I2V mode: am I only describing motion/camera/audio, not the image itself?
- [ ] In video-edit mode: am I changing one element at a time and restating invariants twice?
