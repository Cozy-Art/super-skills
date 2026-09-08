# Luma Uni-1.1 — Continuity and Reference Features

---

## Reference Role System

The foundation of all reference-based work in Uni-1.1.

### Syntax

```
Use IMAGE1 ([brief description]) as a [ROLE] reference.
```

### Available Roles

| Role | What it controls |
|------|----------------|
| `CHARACTER` | Facial features, identity, physical appearance |
| `STYLE` | Artistic treatment, rendering aesthetic |
| `COMPOSITION` | Framing, layout, spatial arrangement |
| `COLOR PALETTE` | Dominant colors, tonal relationships |
| `LIGHTING` | Light direction, quality, color temperature |
| `TEXTURE` | Surface materials, tactile qualities |
| `MOOD` | Emotional atmosphere, tonal register |

### Authority Isolation

When using multiple references, prevent one from overriding another:

```
Treat each reference as having authority over its assigned layer only.
```

Without this clause, references can bleed into each other's domains.

---

## Character Consistency Across Scenes

### The 4-Step Official Workflow

1. **Create a canonical reference** — generate a clean, front-facing, neutral-expression image of the character (or use a photograph)
2. **Reuse as IMAGE1 (CHARACTER)** — include this reference in every subsequent prompt with the CHARACTER role
3. **Use identical label syntax** — the label string must be consistent across all prompts in the series
4. **Combine with seed locking** — lock the seed after a strong result to reinforce visual identity

### Character Consistency Template

```
Use IMAGE1 ([character description with distinguishing features]) as a CHARACTER reference.
Preserve her/his [facial features, hair color, specific markers] exactly.
New scene: [describe new environment and action].
[Camera, lighting, style for the new scene.]
```

**Example:**
```
Use IMAGE1 (woman with short copper-red hair, freckles, green eyes, late 20s) as a CHARACTER reference.
Preserve her facial features, hair color, and freckle pattern exactly.
New scene: she is reading at a wooden desk in a sunlit library, afternoon light from a high window,
warm tones, cinematic depth of field, editorial photography style.
```

### Across Multiple Scenes

Keep everything about the reference declaration identical across all prompts. Change only the scene description:

```
Prompt 1: Use IMAGE1 (copper-red hair, freckles) as a CHARACTER reference. ... Scene: café.
Prompt 2: Use IMAGE1 (copper-red hair, freckles) as a CHARACTER reference. ... Scene: park at dusk.
Prompt 3: Use IMAGE1 (copper-red hair, freckles) as a CHARACTER reference. ... Scene: rainy street.
```

---

## Multi-Reference Architecture for Series Production

For consistent visual series (product campaigns, editorial spreads, storyboards):

### Layer Assignment Pattern

```
IMAGE1 → character identity
IMAGE2 → visual style
IMAGE3 → lighting setup
IMAGE4 → environment/location
Treat each reference as having authority over its assigned layer only.
```

### Maximum Throughput

- `type: "image"`: up to **9 reference images**
- `type: "image_edit"`: up to **8 reference images**

### Budget for References

Up to 9 references per call, each adding $0.0030 to the base price. For a 4-reference call with `uni-1`:
- Base: $0.0404
- 4 refs: +$0.0120
- Total: $0.0524

Use `uni-1-max` for reference-heavy generations where quality matters most.

---

## Create → Modify Workflow Chain

The most powerful iterative production workflow:

### Step-by-Step

1. **Create** (`type: "image"`) — generate freely without constraints on existing material
2. **Review outputs** — pick the composition and mood that works best
3. **Modify** (`type: "image_edit"`) — use the best output as `source`, apply targeted refinements
4. **Chain multiple Modify passes** — each pass refines specific elements while preserving structure

### Modify Prompt Structure

Always include both:
1. **What changes** — be specific and surgical
2. **What stays** — list everything that must remain identical

```
Change [element(s)]. Update [what changes with the element].
Keep [everything else] unchanged.
```

### Example Chain

**Create (exploration):**
```json
{
  "type": "image",
  "prompt": "A quiet French village square at dusk, cobblestones, central fountain, warm café lights, impressionist style, golden-hour atmosphere.",
  "aspect_ratio": "16:9",
  "model": "uni-1"
}
```

**Modify Pass 1 (time of day):**
```json
{
  "type": "image_edit",
  "source": { "url": "https://cdn.your-app.com/village-dusk.jpg" },
  "prompt": "Change the time of day to early morning mist. Update sky, light direction, shadows, and color temperature to cool blue-grey. Keep all architecture, fountain, and cobblestone composition unchanged.",
  "model": "uni-1"
}
```

**Modify Pass 2 (style refinement):**
```json
{
  "type": "image_edit",
  "source": { "url": "https://cdn.your-app.com/village-morning.jpg" },
  "prompt": "Deepen the impressionist brushwork texture throughout. Increase visible paint strokes on the fountain and cobblestones. Keep the composition, color palette, and lighting exactly as they are.",
  "model": "uni-1"
}
```

---

## Image-to-Image with Style Reference

Combine `source` (the image to modify) with `image_ref` (a style to apply):

```json
{
  "type": "image_edit",
  "source": { "url": "https://cdn.your-app.com/base-photo.jpg" },
  "image_ref": [
    { "url": "https://cdn.your-app.com/color-grade-reference.jpg" }
  ],
  "prompt": "Apply the color grading from IMAGE1 to this photo. Preserve subject, composition, and all content unchanged."
}
```

This is the correct pattern for:
- Color grade transfer
- Style transfer while preserving subject
- Relighting with a reference lighting setup

---

## Multi-Panel / Storyboard Generation

Uni-1.1 natively supports storyboard generation with consistent style.

### Prompt Structure

Describe the sequence panel by panel:

```
A 4-panel storyboard sequence:
Panel 1 — [action/description].
Panel 2 — [action/description].
Panel 3 — [action/description].
Panel 4 — [action/description].
[Consistent style instruction throughout.]
```

### Example

```
A 4-panel storyboard sequence:
Panel 1 — character enters a dark doorway, silhouetted against street light.
Panel 2 — close-up on her face, concerned expression, shadows across eyes.
Panel 3 — POV shot of an empty room, overturned furniture, single lamp on floor.
Panel 4 — character turns to leave, hand on door frame, looking back over shoulder.
Consistent film noir lighting, ink-wash illustration style, high contrast throughout.
```

**Tips:**
- Use a fixed seed across all panels for coherence
- Include the same character reference (IMAGE1 as CHARACTER) in each generation
- Specify consistent style at the end of the prompt, not per-panel

---

## Board Context Retention (Luma App)

In the Luma App web interface, Dream Machine retains visual context within a board session.

**Workflow:**
- Build iteratively on the same board rather than starting new sessions
- Use progressive prompts that reference the previous state: `"Add a golden hour glow"` → `"Include a small cottage in the distance"` → `"Transition into a starry night"`
- The model maintains coherent visual direction across the board's history

This board-level context is not available via the API (each API call is stateless).

---

## Reference Image Constraints

| Constraint | Value |
|-----------|-------|
| Max references, `image` type | 9 |
| Max references, `image_edit` type | 8 |
| Max file size per reference | 50 MB |
| URL requirement | Publicly accessible |
| Accepted input | URL or base64 with `media_type` |

---

## Seed + Reference Combination

For maximum consistency in a series:

1. Generate canonical reference image (no seed set)
2. Pick best result — note seed
3. Lock seed for all subsequent calls
4. Use canonical reference as IMAGE1 in all subsequent prompts
5. Change only the scene description between calls

This combination gives you both identity lock (reference) and visual coherence (seed).
