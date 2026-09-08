# PixVerse V6 — Best Practices Guide

---

## The Literal Method: Why It Beats Creative Language

V6's internal reasoning engine is optimized for observable physical descriptions. Abstract stylistic language — "magical," "epic," "stunning," "dramatic" — forces the model to interpret creative intent, introducing unpredictable variance. Physical descriptions give it a target.

**The test:** Can you photograph it? If yes, it belongs in the prompt. If not, translate it into something you can photograph.

| Creative abstraction | Physical translation |
|---------------------|---------------------|
| "Dramatic scene" | "Low-angle tracking shot, handheld shake, sparks from metal joints" |
| "Beautiful morning" | "Warm golden side light from the left, soft haze, long shadows on the ground" |
| "Tense atmosphere" | "Subject still, no camera movement, silence except for faint ambient hum" |
| "Magical forest" | "Wide tracking through pine trees, morning side light, fog in the mid-ground" |
| "Cinematic quality" | "Cinematic realism, shallow depth of field, color graded cool blue highlights" |

The model doesn't know what "beautiful" means as a visual instruction. It does know what "warm golden side light from the left" means.

---

## Subject Anchoring

Subject anchoring is the highest-leverage element in V6 prompting.

**Rules:**

1. **Subject always comes first** — early tokens receive disproportionate model weight. If your subject is buried after environment description, character identity is weakened.

2. **3–4 physical descriptors minimum:** age/build, clothing, expression, hair — enough to anchor identity without over-constraining motion.

3. **Maximum 2 main characters per shot.** V6 maintains individual face consistency well with 1–2 subjects. Crowds produce a "clone army" effect — faces become near-identical. Workaround: describe groups as "pedestrians in soft focus background."

4. **For multi-image character reference:** upload 3+ reference images from different angles (front, 3/4, side) to give the model a full identity model.

**Good subject anchor:**
```
"Professional woman in her early 40s, black blazer and white shirt, confident expression."
```

**Weak subject anchor:**
```
"A woman walking through an office."
```

---

## Motion and Camera Discipline

### One Primary Action Per Clip

Multiple competing motions in a single generation cause choppy, incoherent output. One clear primary action is the discipline.

✅ `"Walking slowly toward the camera, natural stride"`  
❌ `"Walking toward the camera while looking back, reaching for something, turning sideways"`

### Pace Qualifiers Are Mandatory

Without a pace qualifier, V6 defaults to a medium pace that may not match intent. Always specify:

| Intensity | Keywords |
|-----------|---------|
| Slow / gentle | `slowly`, `gently`, `gradually`, `softly`, `drifting` |
| Medium | `steadily`, `naturally`, `at a normal pace` |
| Fast / energetic | `rapidly`, `quickly`, `vigorously`, `urgently` |

### Maximum 2 Camera Moves Per Shot

V6 reliably handles 1–2 camera instructions. In structured testing, a 3-move sequence (pull-back + crane-up + pan right) produced the first two moves while ignoring the third. Stick to 1–2.

✅ `"Medium tracking shot from chest height, slight upward tilt"`  
❌ `"Tracking shot that pulls back, cranes up, pans right, and slowly zooms in"`

**Split complex moves across shots** in a multi-shot sequence instead.

### Handheld vs. Gimbal

| Handheld | Gimbal-stable |
|----------|--------------|
| Action sequences | Product demos |
| Documentary style | Beauty content |
| High-energy scenes | Corporate commercial |
| Concert/events | Architectural walkthrough |

For commercial, beauty, or product content — explicitly write `"gimbal-stable"` to prevent handheld shake being applied by default.

### Effective Camera Vocabulary

These terms from the legacy `camera_movement` API enum also work in V6 text prompts:

`dolly-in` · `pull back` · `tracking shot` · `pan left/right` · `crane up` · `zoom in/out` · `quickly zoom in` · `smooth zoom in` · `hitchcock zoom` · `whip pan` · `camera rotation` · `super dolly out` · `left follow` · `right follow` · `fix background`

---

## Style and Tone Vocabulary

### Replace Vague Adjectives with Specific Genre Names

| ❌ Vague | ✅ Specific genre anchor |
|---------|------------------------|
| "Good quality" | "Corporate commercial aesthetic, professional quality" |
| "Artistic style" | "Documentary style" / "Pixar 3D animation" / "Anime cinematic" |
| "Nice lighting" | "Soft warm window light from the left" |
| "Modern look" | "Contemporary editorial aesthetic, clean color grade" |
| "Dramatic" | "High contrast, deep shadows, single key light" |

### Color Grade Beats Mood

❌ `"cold and isolated feeling"` → ✅ `"cool blue-white tones, desaturated mid-range"`  
❌ `"warm and romantic atmosphere"` → ✅ `"warm amber tones, soft candlelight fill, shallow depth"`

### `style` API Parameter Warning

The `style` parameter (`anime`, `3d_animation`, `cyberpunk`, `comic`, `day`) is a strong genre override. Avoid it for photorealistic generation — it pushes output toward stylized looks even when you don't want it.

Use the `style` parameter **only** when you need a dominant genre override, not as a quality enhancer.

---

## Negative Prompts: Always Include

V6 fully supports negative prompts up to 2,048 characters. They are highly effective at preventing specific artifacts.

### Minimum Effective Negative (All Prompts)
```
blurry, extra fingers, morphing, inconsistent lighting, duplicate limbs
```

### For Character Content (Add)
```
identity drift, face morph, deformed hands, extra limbs, double face
```

### For Multi-Shot (Add)
```
character drift, lighting jump, style mismatch between shots, extra people
```

### For Product/Commercial (Add)
```
warping, extra objects, logo distortion, overexposed highlights, lens flare
```

### For Action/High Motion (Add)
```
subject blur, subject lost in background, unnatural physics, visual noise
```

---

## Known V6 Limitations

### Crowd Diversity
V6 produces near-identical faces when generating groups of people. **Workaround:** Describe groups as "pedestrians in soft focus background," "crowd in blurred background" — save face detail for the primary subject.

### Facial Close-Ups
Extreme close-ups on human faces at high motion levels risk uncanny valley artifacts. **Workaround:** Don't exceed medium close-up for face shots. Avoid extreme macro on human skin. Use Pro/high quality settings when close-ups are necessary.

### Text Rendering
On-screen text is unreliable at small sizes. **Workaround:** Use only clean geometric display text for any in-frame text. Add body copy, subtitles, and labels in post-production.

### Complex Multi-Step Camera Instructions
The third camera move in a sequence is commonly ignored. **Workaround:** Maximum 2 camera moves per shot; use multi-shot structure for complex camera sequences.

### Audio Sync on Rhythmic Action
Timing inference is imprecise for rhythmic actions. **Workaround:** Describe beats explicitly: `"sticks hit snare on every downbeat"` rather than just `"drummer playing"`

### Content Filter False Positives
Legitimate content (martial arts, period drama) can be blocked by over-aggressive content filters. **Workaround:** Rephrase to remove combat/fighting language. Use "action choreography" instead of "fight scene." Use period-appropriate vocabulary without violence references.

---

## Draft → Production Pipeline

1. **360p/540p first** — validate composition, motion, character
2. **Test 2–4 seeds** — distinguish model variation from prompt ambiguity before changing the prompt
3. **`thinking_type: enabled`** for all draft iterations
4. **Iterate one variable at a time:** camera first → motion pace → lighting/style → audio
5. **Lock prompt → switch to `thinking_type: disabled`** for reproducible finals
6. **1080p render** once the prompt produces correct visual results
7. **Add audio last** — `generate_audio_switch: true` on the final 1080p render

---

## Motion Strength Slider (Web UI Only)

Available in the V6 web UI; no API equivalent documented as of April 2026.

| Setting | When to use |
|---------|------------|
| Decreased | Product demos, portrait content, beauty, commercial |
| Default | General use, narrative content, nature |
| Default/increased | Action sequences, sports, high-energy content |

Use lower motion strength to prevent over-animation on subjects that should be relatively still.
