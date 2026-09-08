# GPT Image 2 — Example Prompts

All examples sourced and annotated from official GPT Image 2 documentation. Each includes the formula, complete prompt, recommended parameters, and technique notes.

---

## Example 1 — Photoreal Editorial Portrait

**Formula:** Scene + Subject + Details + Use case + Constraints  
**Parameters:** `quality: "high"` · `size: "1024x1536"` (portrait)

```
Scene:
A narrow cobblestone alley in Lisbon at golden hour.

Subject:
A man in his 40s leaning against a tiled wall, arms crossed.

Important details:
Worn linen shirt, slightly stubbled, direct gaze, warm side light from the
setting sun, long shadow falling across the tiles, 50mm feel, natural skin texture.

Use case:
Editorial travel magazine photograph.

Constraints:
No watermark, no logos, no posed glamour.
```

**Technique notes:**
- "50mm feel" = correct way to describe focal length (not "50mm f2.0")
- "No posed glamour" in Constraints prevents the model defaulting to commercial stock aesthetics
- Golden hour named explicitly rather than "beautiful light"
- `quality: "high"` needed for skin texture and fabric detail

---

## Example 2 — Character Consistency: Children's Book Anchor

**Formula:** Character definition → Continuation with explicit identity carryover

**Anchor prompt:**
```
Create a children's book illustration introducing a main character.
A young forest helper wearing a green hooded tunic, soft brown boots,
and a small belt pouch. Kind expression, gentle eyes, warm but brave personality.
Hand-painted watercolor look, earthy colors, soft outlines, whimsical but grounded.
No text. No watermark.
```

**Continuation prompt (new scene, same character):**
```
Continue the children's book story using the same character.
The same forest helper is rescuing a frightened squirrel after a winter storm.
Keep the same face, same green hooded tunic, same proportions,
same color palette, and same gentle personality.
Same watercolor look, snowy forest light, warm comforting mood.
Do not redesign the character.
No text. No watermark.
```

**Technique notes:**
- Character described in terms the model can render, not personality abstractions
- "Do not redesign the character" is a strong constraint that prevents the model drifting
- Re-upload the anchor image when submitting the continuation prompt for best results
- Style described in visual terms: "hand-painted watercolor look, earthy colors, soft outlines"

---

## Example 3 — Documentary Landscape / Still Life

**Formula:** Observational description with specific material and light details  
**Parameters:** `quality: "high"` · `aspect: 3:2` · `thinking: "low"`

```
Create a color documentary photograph of a fishmonger unpacking crates of mackerel
onto crushed ice at a small coastal market just after dawn. Steam from breath in the
cold air, rubber boots, wet concrete floor, incandescent work lamp spilling warm
light, a paper ledger with handwritten prices clipped to a wooden post. Realistic
skin texture and fish scales, shallow depth of field, 35mm feel. No commercial
styling, no watermark.
```

**Technique notes:**
- No six-element headers needed — the description is naturally ordered (scene → subject → details)
- Every material named specifically: crushed ice, rubber boots, wet concrete, paper ledger
- Light source named specifically: "incandescent work lamp spilling warm light"
- "35mm feel" (not "35mm lens") is the correct phrasing
- "No commercial styling" explicitly pushes away from stock-photo aesthetic
- `thinking: "low"` because no text or counted elements — basic scene composition

---

## Example 4 — Text Rendering: Diner Menu Board

**Formula:** Scene with typography-as-subject  
**Parameters:** `quality: "high"` · `thinking: "medium"`

```
Create a photoreal photograph of a 24 hour diner menu board at 5 in the morning,
shot from the counter seat at slight angle. Plastic letter tracks, uneven letter
spacing, one missing letter slot, yellowed light from incandescent bulbs, legible
prices, categories labeled BREAKFAST, GRIDDLE, SANDWICHES, SIDES, DRINKS, and a
daily special that reads CHICKEN FRIED STEAK 8.25. The type must be 100 percent
readable and physically believable. No watermark, no brand logos, no text artifacts.
```

**Technique notes:**
- Text categories in ALL CAPS to trigger literal text rendering
- Specific text (`CHICKEN FRIED STEAK 8.25`) in ALL CAPS
- "100 percent readable and physically believable" is both a quality cue and a constraint
- "No text artifacts" in Constraints explicitly blocks hallucinated characters
- `thinking: "medium"` needed because of multiple text elements with specific labels
- `quality: "high"` is mandatory for any prompt with required readable text

---

## Example 5 — UI Mockup: Mobile App Onboarding

**Formula:** Screen type + exact copy in quotes + hierarchy + style  
**Parameters:** `quality: "high"` · `size: "1024x1536"` · `thinking: "medium"`

```
Create a vertical mobile onboarding screen for a fictional app called NESTING.
Headline: WELCOME TO NESTING.
Supporting line: A quieter way to gather people around a table.
Buttons: Get started, I already have an account.
Small line illustration of three plates and two wine glasses.
Warm cream background, coral primary button, rounded sans serif,
clean spacing, exact readable copy.
No watermark. No real app branding.
```

**Technique notes:**
- All text that must appear is spelled out exactly (including capitalizations)
- Button labels quoted implicitly through precise listing
- "Exact readable copy" is both instruction and constraint
- Style described visually: "warm cream background, coral primary button, rounded sans serif"
- "No real app branding" prevents the model from inserting known app logos or UI patterns
- `size: "1024x1536"` = mobile portrait aspect ratio

---

## Example 6 — Quiet Still Life / Documentary Portrait

**Formula:** Tight subject description with material and light specificity  
**Parameters:** `quality: "high"` · `size: "1024x1024"`

```
Create a tight medium format portrait of an elderly woman's hands peeling garlic at
a worn wooden kitchen table. Window light from camera left, faded floral housedress
sleeves, a chipped porcelain bowl half full of peeled cloves, papery garlic skins
scattered. Every wrinkle and nail imperfection visible, warm color palette, no
stylization. No watermark.
```

**Technique notes:**
- "Tight medium format portrait" gives framing without camera jargon
- "Window light from camera left" — direction named, quality implied by context
- Every material is named: worn wood, faded floral fabric, chipped porcelain, papery skins
- "Every wrinkle and nail imperfection visible" is a specific instruction against retouching
- "No stylization" = keep it documentary, not illustrative
- No thinking mode needed — purely atmospheric with no counted elements or text

---

## Example 7 — Multi-Image Compositing: Virtual Try-On

**Formula:** Label images by role → change instruction + comprehensive preserve list  
**Parameters:** `quality: "high"` · Edit endpoint with 4 reference images

**Prompt:**
```
Image 1: the woman to preserve.
Image 2: the tank top reference.
Image 3: the jacket reference.
Image 4: the boots reference.

Dress the woman from Image 1 using the clothing from Images 2, 3, and 4.
Preserve her face, facial features, skin tone, body shape, hands, pose,
hair, expression, background, camera angle, framing, and lighting exactly.
Replace only the clothing.
Fit the garments naturally with realistic folds, drape, occlusion, and shadows.
Do not add jewelry, bags, text, or logos.
```

**API call:**
```python
response = client.images.edit(
    model="gpt-image-2",
    image=[
        open("person.png", "rb"),
        open("tank_top.png", "rb"),
        open("jacket.png", "rb"),
        open("boots.png", "rb"),
    ],
    prompt="<prompt above>",
    quality="high",
)
```

**Technique notes:**
- Images labeled by role at the top — essential for multi-image edits
- "Preserve" list is exhaustive and explicit — every identity element listed
- "Replace only the clothing" is the single-change constraint
- Physical realism stated explicitly: "realistic folds, drape, occlusion, and shadows"
- "Do not add jewelry, bags, text, or logos" closes common failure modes in compositing

---

## Additional Templates

### Standard Editorial Portrait
```
Scene: [Location, time of day]
Subject: [Person description — age, build, clothing, gaze, body framing]
Important details: [Lighting direction + quality, surface materials, lens feel]
Use case: Editorial [publication type] photograph.
Constraints: No watermark, no logos, no [specific aesthetic to avoid].
```
*Quality: `high` · Thinking: `off` to `low`*

### Product Photography
```
Scene: [Surface type and environment]
Subject: [Product with exact materials named]
Important details: [Lighting setup, camera angle, label text in quotes if needed]
Use case: Product mockup / commercial product photograph.
Constraints: No watermark, no extra objects, no label drift.
```
*Quality: `high` · Thinking: `low` (add `medium` if label text must be exact)*

### Technical Diagram / Infographic
```
Create a [diagram type] showing [subject].
[Numbered elements]: [Element A], [Element B], [Element C] — list every labeled component
[Arrows/connections]: [describe flow or relationships]
[Style]: [sharp sans-serif / clean lines / background color]
Constraints: No watermark, no extra labels, no text artifacts.
```
*Quality: `high` · Thinking: `medium` to `high`*

### Single-Change Edit (Three-Sentence Pattern)
```
Change only: [specific element]
Preserve: [face/identity/pose/lighting/background/framing — list every invariant]
Physical match: [scale/shadow/lighting match instruction]
[Preserve list repeated]: [same list restated]
```
*Use edit endpoint · Quality: `high`*

### Multi-Scene Series (DNA Template)
```
DNA Template:
All images use [aspect ratio], [art style].
Characters: [name + full visual description for each]
Visual style: [color palette, rendering, line weight, texture]

Scene [N]: [new action and context]
Same style, same characters, same color palette.
No text. No watermark.
```

---

## Quick Diagnostic: Is My Prompt Correct?

- [ ] Does it describe visual facts, not feelings?
- [ ] Is "photorealistic" included if I want a real-photo look?
- [ ] Are all literal text elements in quotes or ALL CAPS?
- [ ] Is font style, color, and placement specified for each text element?
- [ ] Is "no extra words, no duplicate text" in Constraints?
- [ ] Have I named the lighting source and direction?
- [ ] Have I named specific materials (not "realistic texture")?
- [ ] Is the thinking level appropriate? (contains numbers/labels → `medium`+)
- [ ] Is quality set to `high` for any text, UI, or close-up portrait?
- [ ] If editing: does the prompt follow the three-sentence pattern?
- [ ] If editing: is the preserve list stated twice?
- [ ] If using reference images: is each image labeled by role?
- [ ] Is `background: "transparent"` absent? (not supported)
- [ ] If character series: is the anchor image being re-uploaded each turn?
- [ ] Have I avoided living artist names? (use style descriptions instead)
