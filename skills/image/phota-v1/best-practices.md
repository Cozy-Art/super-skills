# Phota — Best Practices Guide

## The Inverted Prompt Paradigm

**Phota inverts everything you know about AI image prompting.**

In every other image model, you spend most of your prompt describing the subject — hair color, eye shape, clothing, body type, age, ethnicity. In Phota, all of that is handled by the trained profile. The `[[profile_id]]` carries identity information with higher fidelity than any text description you could write.

This means your entire prompt budget is freed for what actually matters: **the photographer's creative brief**.

### The Old Way (Other Models):
```
A woman in her early 30s with cropped silver hair, sharp cheekbones, 
wearing a tailored charcoal wool coat with brass buttons, confident 
expression, standing in a rain-soaked Tokyo alleyway at dusk, neon 
reflections on wet pavement, shot on ARRI Alexa, 85mm lens...
```
→ Half the prompt describes what the person looks like.

### The Phota Way:
```
Professional environmental portrait of [[abc123]], three-quarter length, 
standing in a rain-soaked Tokyo alleyway at dusk. Neon reflections on wet 
pavement. Soft ambient neon light from signs above, warm backlight from 
a ramen shop doorway. 85mm lens feel, shallow depth of field, Kodak 
Portra 400 color rendering. Confident posture, direct gaze at camera.
```
→ Every word is creative direction. Zero words wasted on appearance.

---

## Profile Training: The Foundation of Everything

The quality of your profile training set is the single most important determinant of identity fidelity. A mediocre prompt with a great profile produces better results than a perfect prompt with a weak profile.

### What Makes a Great Training Set

**Variety is the goal, not volume.** Ten sharp, varied photos outperform 40 near-identical shots.

**Angle coverage:**
- Full frontal face (direct to camera)
- Three-quarter turn (left and right)
- Profile view (left and right)
- Slightly elevated angle (as in a group photo)
- Slightly below eye level (looking up)

**Lighting coverage:**
- Natural daylight (outdoor, window light)
- Indoor artificial light
- Overcast / diffused light
- Studio or direct flash
- Mixed lighting

**Expression range:**
- Neutral / resting
- Genuine smile (eyes involved, not forced)
- Pensive / contemplative
- Animated / laughing
- Serious / direct

**Framing variety:**
- Tight headshot (face fills frame)
- Shoulders-up portrait
- Waist-up environmental
- At least 2-3 photos where face is large and sharp in frame

### Training Photo Red Flags

| Red Flag | Why It Hurts | Alternative |
|----------|-------------|-------------|
| Sunglasses | Hides eye area, weakens eye fidelity | Use photos without eye-covering accessories |
| Heavy Instagram filters | Distorts skin tone and facial geometry | Use unfiltered or lightly edited photos |
| Strong backlight silhouettes | Face is underexposed, features lost | Use front-lit or side-lit photos |
| All same pose/angle | Profile only learns one view | Include variety across all angles |
| All same lighting | Profile can't adapt to new lighting in generation | Include indoor, outdoor, overcast, flash |
| Group photos only | Phota may train on wrong person (majority face) | Include solo photos; use solo photos exclusively if possible |
| Tiny face in frame | Insufficient resolution on facial features | Crop to ensure face is large and sharp |

### The Training-Generation Feedback Loop

1. **Train** with initial 30–50 photos (~15 min)
2. **Generate** a simple studio headshot as a test
3. **Evaluate** — does it look exactly like the person?
4. If identity is weak or wrong:
   - Check if training included enough angle/lighting variety
   - Add more photos covering underrepresented conditions
   - Retrain
5. If identity is strong: proceed to creative work

---

## Generate Mode: Prompting Like a Photographer

### The Prompt Formula

```
[Portrait style] + [[profile_id]] + [framing] + [expression/pose] + 
[lighting] + [background/setting] + [technical/lens look]
```

### Component Guide

**1. Portrait Style** — The creative anchor
- "Professional studio headshot"
- "Artistic noir portrait"
- "Casual lifestyle portrait"
- "Environmental corporate portrait"
- "Editorial fashion portrait"
- "Candid documentary portrait"

**2. [[profile_id]]** — Identity lock (REQUIRED)
- Always include exactly as `[[profile_id]]`
- For multi-person: `[[id1]] and [[id2]]`
- Never supplement with physical description

**3. Framing** — Camera distance and crop
- "Tight close-up, face only"
- "Chest up" (classic headshot)
- "Three-quarter length" (waist up)
- "Full body, standing"
- "Environmental wide, subject in context"

**4. Expression/Pose** — What the person is doing
- "Warm natural smile, relaxed"
- "Confident and direct gaze at camera"
- "Introspective, looking slightly off-camera"
- "Animated, mid-laugh"
- "Serious, contemplative, three-quarter head tilt"
- Include body language: "arms crossed," "leaning against wall," "hands in pockets"

**5. Lighting** — The single most impactful creative element
- **Direction:** "Key light from upper left," "backlit rim light," "front-fill from reflector"
- **Quality:** "Soft diffused," "hard direct," "dappled through leaves"
- **Color temperature:** "Warm golden," "cool daylight," "mixed tungsten and daylight"
- **Named setups:** "Rembrandt lighting," "butterfly lighting," "split lighting," "chiaroscuro"
- **Practical sources:** "Window light from the left," "neon sign spill," "fireplace glow"

**6. Background/Setting** — The environment
- "Clean neutral gray studio background"
- "Blurred office environment, shallow depth of field"
- "Outdoor park bench, autumn foliage bokeh"
- "Dark studio with single warm practical light in background"
- "City rooftop at golden hour, skyline soft behind"

**7. Technical/Lens Look** — Camera character
- "85mm lens look, shallow depth of field" (classic portrait)
- "50mm, moderate depth, environmental context visible" (documentary)
- "Medium format feel, Fujifilm GFX rendering" (editorial)
- "35mm wide, environmental, slight barrel distortion" (lifestyle)
- Film stock references: "Kodak Portra 400 tones," "Tri-X B&W grain"
- "Photoreal, natural skin texture, no plastic smoothing"

---

## Edit Mode: Surgical Changes

### The Edit Prompt Formula

```
Keep [what stays unchanged]. [Change only this specific thing.]
```

### Rules of Edit Mode

1. **Declare what's preserved FIRST** — lighting, framing, identity, background
2. **Describe the change second** — one specific modification
3. **One change per pass** — resist the urge to fix everything at once
4. **Include profile reference** — `[[profile_id]]` locks identity through the edit
5. **Add "Photoreal" guard** — "Photoreal, no plastic smoothing, no over-retouching" prevents AI beautification drift

### Common Edit Operations

**Expression change:**
```
Keep the same person and identity exactly. Adjust only the facial 
expression: soften into a natural relaxed smile. Keep eyes and face 
shape consistent. Preserve lighting and background.
```

**Lighting adjustment:**
```
Keep identity, pose, and background unchanged. Shift the key light 
from flat front to soft Rembrandt from the left. Allow natural shadow 
fall on the right side of the face. Keep expression the same.
```

**Background swap:**
```
Keep [[abc123]]'s identity, expression, pose, and lighting exactly the 
same. Replace the background only: change from studio gray to a blurred 
outdoor park scene with warm golden hour bokeh. Adjust rim light to 
match new warm outdoor setting.
```

**Reframing:**
```
Keep [[abc123]]'s identity and expression unchanged. Reframe from 
waist-up to a tight chest-up headshot. Maintain the same lighting 
quality and background.
```

**Person removal:**
```
Convert to a solo portrait of [[abc123]]. Remove all other people 
from the frame. Keep the background and lighting the same. Fill the 
empty space naturally.
```

---

## Multi-Person Group Shot Workflow

### Step-by-Step

1. **Prerequisites:** Both subjects must have trained profiles
2. **Collect reference images:** 1–2 photos of each person (can be from different occasions)
3. **Upload as input images** (Edit mode)
4. **Write the composite prompt:**

```
Create a single group photo combining [[id1]] from Image 1 and 
[[id2]] from Image 2. Match the lighting, background, and perspective 
of Image 1. Position [[id2]] standing to the right of [[id1]], 
slightly turned toward them. Both should appear naturally lit as if 
photographed together in the same moment. Photoreal, natural shadows, 
no compositing artifacts.
```

### Group Shot Pitfalls

| Pitfall | Prevention |
|---------|-----------|
| People look pasted in | Add "Match lighting and perspective of [source image]" |
| Scale mismatch | Specify relative positioning: "standing beside," "seated next to" |
| Eye-line disconnect | Add "Both looking at camera" or "Looking at each other" |
| Shadow inconsistency | Add "Natural shadows consistent with single light source" |

---

## Memory Rescue Workflow

Phota's unique strength — restoring old, damaged, or technically poor photos:

### How It Works

1. Upload the degraded photo as input image
2. Reference the person's `[[profile_id]]` in the edit prompt
3. Phota uses the trained profile to lock identity, even from:
   - Blurry or out-of-focus photos
   - Heavily underexposed or overexposed shots
   - Damaged or faded prints
   - Low-resolution scans
4. The edit prompt specifies quality improvements

### Memory Rescue Prompt Template

```
Restore this photo of [[profile_id]]. Preserve the original composition, 
setting, and moment. Fix only the technical quality: correct exposure, 
reduce noise, improve sharpness, and restore natural color balance. 
Keep the person's identity, expression, and pose exactly as captured. 
Photoreal, period-appropriate color rendering.
```

---

## Phota vs. Other Image Models — Prompt Strategy Differences

### What Phota Handles vs. What You Handle

| Responsibility | Phota Handles (via Profile) | You Handle (in Prompt) |
|---------------|---------------------------|----------------------|
| **Identity** | Face, bone structure, expression range | Nothing — let the profile work |
| **Style** | Follows photographic language | Lighting recipe, lens feel, mood |
| **Composition** | Follows framing instructions | Camera distance, angle, crop |
| **Expression** | Generates within person's actual range | Target expression explicitly |
| **Setting** | Generates based on description | Environment, background, time of day |

### When to Use Phota vs. Other SKILLs

**Use Phota when:**
- A real person's likeness must be preserved accurately
- Professional headshots or portrait photography
- Fixing expressions or lighting in existing photos
- Compositing group shots from separate photos
- Restoring damaged or degraded photos
- Building a consistent portrait series of a real person

**Use Seedream/Grok/Mystic when:**
- Creating fictional characters (no real person)
- Landscapes, products, environments (no identity preservation needed)
- Abstract or fantasy art
- Text rendering in images
- Non-portrait photography

---

## Troubleshooting

### Identity Doesn't Match
- Verify `[[profile_id]]` is in the prompt text (not just uploaded)
- Check training set for variety — add missing angles/lighting
- Reduce prompt complexity — simpler prompts sometimes preserve identity better
- Add identity lock phrase: "Preserve identity and facial features exactly"

### Output Looks Over-Processed / Plastic
- Add "Photoreal, natural skin texture, no plastic smoothing, no over-retouching"
- Remove superlatives ("gorgeous," "stunning") which can trigger beautification
- Specify film stock for natural rendering: "Kodak Portra color science"

### Expression Looks Forced
- Specify the expression with nuance: "subtle warm smile, eyes slightly crinkled" not "big smile"
- Consider the person's natural expression range — the profile learned from real photos
- Try "relaxed" or "natural" modifiers before the expression word

### Multiple Edits Compounding Errors
- Reset to original image and re-do with single combined change
- Or work forward but limit to ONE change per pass
- Always include identity lock phrases in every edit

### 4K Output Not Working
- Resolution defaults to 1K — must explicitly set `"resolution": "4K"`
- Verify your platform/plan supports 4K output

---

## Version Information

- **Guide Version:** 1.0
- **Covers:** PhotaLabs Phota (Generate, Edit, Enhance modes)
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
