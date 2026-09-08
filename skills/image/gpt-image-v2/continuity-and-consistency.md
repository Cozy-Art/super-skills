# GPT Image 2 — Continuity and Consistency Features

How to maintain character identity, visual style, and scene consistency across generations.

---

## Character Consistency Strategy

GPT Image 2 achieves character consistency through **multi-turn reference**, not session memory locking. The model does not automatically remember characters between turns.

### The 5-Step Workflow

1. **Establish an anchor image** — Generate a detailed first image with the character described precisely:
   - Age, build, body proportions
   - Face, hair color and style, skin tone
   - Unique markers (birthmark, scar, distinctive feature)
   - Clothing (specific items, colors, fit)

2. **Name the character** — Assign a name and use it consistently in every follow-up prompt:
   ```
   Character name: LENA
   Continue using LENA as defined in Image 1.
   ```

3. **Re-upload the reference image** at each new scene request to reset the model's visual anchor — do not rely on the model remembering from a previous turn

4. **Specify every identity detail explicitly** in continuation prompts — do not write "same character as before"; write out the details:
   ```
   LENA — light tan skin, round face, large almond-shaped hazel eyes,
   shoulder-length black hair with front bangs, wearing a green hooded tunic
   ```

5. **Use close-up reference photos** — Full-body shots lose facial detail; close-up portraits preserve features more reliably

### Continuation Prompt Pattern

```
Continue the story using the same character.
The same [CHARACTER NAME] is [new action in new scene].
Keep the same face, same [clothing], same proportions, same [hair],
same [distinguishing features], same color palette.
Do not redesign the character.
No text. No watermark.
```

---

## DNA Template — Multi-Scene Storyboard Setup

For sequences, series, or storyboard work, prepend a **DNA Template** at the start of each session. This defines the visual contract across all images.

### Template Format

```
DNA Template:
All images use [aspect ratio], [art style].
Session: [project name or description].

Characters:
[Character A name]: [age, build, skin, hair, eyes, unique markers, clothing]
[Character B name]: [same level of detail]

Environment: [location, architectural style, lighting baseline]
Visual style: [color palette, rendering approach, line weight, texture]
Aspect ratio: [consistent across session]
```

### Example DNA Template

```
DNA Template:
All images use 3:2 aspect ratio, watercolor anime style.
Session: visual scenes for 'The Harmony of Three.'

Characters:
- Identical triplet sisters: Hi, Fu, and Mi
- Light tan skin, round face, large almond-shaped hazel eyes
- Shoulder-length black hair with front bangs
- Hi: pink ribbon | Fu: silver pendant | Mi: holds a small diary

Visual style: soft watercolor, gentle linework, muted pastel tones.
Ambient diffused lighting, no hard shadows. Medium-wide framing.
I will provide scenes one at a time.
```

### Scene Prompt After DNA Template

```
[DNA Template as above]

Scene 1: The three sisters sit together at a wooden table in a sunlit kitchen,
Hi pouring tea, Fu reading a book, Mi writing in her diary.
Same art style and color palette as DNA Template.
No text. No watermark.
```

---

## Image-to-Image / Reference Image Workflow

The edit endpoint (`/v1/images/edits`) accepts 1–16 reference images.

### Labeling Protocol

Label each input image by its role — this is essential for multi-image edits:

```
Image 1: base scene to preserve.
Image 2: style reference.
Image 3: jacket to apply to the subject.

Apply the color palette and brushwork from Image 2 to Image 1.
Preserve all subject matter, composition, and proportions from Image 1.
```

### Drawing-to-Photo

Specify whether the input layout is a suggestion or a contract:

```
Turn this drawing into a photorealistic landscape image.
Preserve the exact layout, horizon line, river path, mountain placement,
tree placement, and overall perspective. [layout = contract]
Choose realistic materials and lighting consistent with a quiet sunrise scene.
Do not add new objects or text.
```

### Multi-Image Compositing (Virtual Try-On Pattern)

```
Image 1: the subject to preserve.
Image 2: garment A reference.
Image 3: garment B reference.
Image 4: footwear reference.

Dress the subject from Image 1 using the clothing from Images 2, 3, and 4.
Preserve their face, facial features, skin tone, body shape, hands, pose,
hair, expression, background, camera angle, framing, and lighting exactly.
Replace only the clothing.
Fit the garments naturally with realistic folds, drape, occlusion, and shadows.
Do not add jewelry, bags, text, or logos.
```

---

## Style Transfer

"Same style" alone is insufficient — name the parts explicitly:

```
Use the same visual language as the input image:
chunky pixel forms, limited arcade palette, bright glow accents,
clean silhouette edges, playful 1980s poster energy.
Generate a new scene of a motorcycle chase through a neon desert at night.
White background. No watermark.
```

### Style Description Components

To transfer a style without using artist names (which can trigger moderation):

1. **Color palette:** "limited arcade palette," "muted pastels," "high-contrast monochrome with one accent color"
2. **Rendering approach:** "soft watercolor," "chunky pixel forms," "flat vector illustration"
3. **Line weight:** "bold outlines," "no outlines," "gentle linework"
4. **Texture:** "grain texture," "smooth gradients," "rough brushwork"
5. **Energy/era:** "1980s poster energy," "1940s editorial illustration," "contemporary Scandinavian"

---

## Seed-Based Reproducibility

Set `seed` to a fixed integer to reduce variance between runs.

**Critical limitation:** Seed + same prompt = "close, not identical." The seed reduces variance but **does not guarantee identical output.**

**For guaranteed reproducibility:** Cache the output bytes — do not re-generate.

```python
# Set seed for reduced variance
response = client.images.generate(
    model="gpt-image-2",
    prompt=your_prompt,
    seed=42,
    quality="high",
    size="1536x1024",
)
# Save immediately — don't rely on URL response (expires in 1 hour)
import base64
png_bytes = base64.b64decode(response.data[0].b64_json)
Path("output.png").write_bytes(png_bytes)
```

---

## Batch Generation for Coherent Variants

Setting `n > 1` returns multiple images that share composition and style — this is fundamentally different from calling the endpoint N times in parallel (which produces unrelated images).

**Use for:**
- Multiple versions of a hero image with consistent style
- Product lineup with shared lighting
- Character in multiple expressions, same visual treatment

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="Four hero illustrations for API documentation, shared color palette, shared line weight.",
    size="1536x1024",
    quality="high",
    n=4,
    thinking="low",
)
```

---

## Iterative Editing Strategy

**Edit-over-regenerate is the core discipline.** Regenerating from scratch is the primary source of brand and character drift in production workflows.

### The Three-Sentence Edit Pattern

Every object edit should have exactly three components:

1. **What changes:** "Replace the parked car with a vintage bicycle."
2. **What stays locked:** "Preserve the house, fence, driveway, landscaping, lighting direction, and time of day exactly."
3. **Physical realism:** "Match the bicycle scale and shadow pattern to the existing scene."

### One Revision Per Turn

Small, iterative edits outperform one giant rewrite:
- Turn 1: Adjust lighting
- Turn 2: Change character's clothing color
- Turn 3: Add a prop to the background

Attempting all three in one edit call produces less reliable results than three sequential single-change passes.

### Preserve List Repetition

Repeating the preserve list strengthens the model's adherence to constraints:

```
Change only the jacket color to deep burgundy.
Keep the face, hair, skin tone, pose, background, and lighting exactly the same.
Face, hair, skin tone, pose, background, and lighting remain unchanged.
```

Restating the preserve list twice doubles its constraint weight in the model.

---

## Session Management

### Session Noise Bug
A known bug causes noise artifacts to amplify across images in the same session when image data is reused. Symptoms:
- Increasing visual noise in successive generations
- Images looking identical despite different prompts

**Fix:** Restart the session (reload the page). There is no prompt-based fix.

### Style/Seed Contamination
Images in the same session currently share style/seed context. If you need truly independent generations (e.g., testing different styles), start a new session for each.

### URL Expiry
Response URLs expire after **1 hour**. Always:
- Use `response_format="b64_json"` in production
- Save bytes to disk immediately
- Copy to own S3/CDN before sharing with anyone
