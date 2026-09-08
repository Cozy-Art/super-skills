# HappyHorse 1.0 — Continuity and Reference Features

How to maintain character identity, scene consistency, and visual continuity across generations.

---

## Seed-Based Reproducibility

Set `seed` to a fixed integer (0–2,147,483,647) to reproduce exact outputs when all other parameters remain constant.

**Workflow:**
1. Run a prompt with random seed — note the seed from the output metadata
2. Copy that seed to your next run with the same prompt
3. Confirm determinism across two generations before tweaking
4. When adjusting parameters, change one variable at a time and re-confirm

Seeds are the lowest-cost form of iteration control. Use them from the very first generation.

---

## Image-to-Video (I2V) — Keyframing

The I2V endpoint uses the uploaded image as the **literal first frame** of the video. The model animates from that exact visual state.

### Prompt Rules for I2V

Only describe what **changes**:
- Motion type and direction
- Camera movement
- Audio layers
- Lighting evolution (if intentional)

**Never describe the image itself** — it's already the first frame. Redescribing creates text-vs-image conflict and wastes the token budget.

### Character Consistency Across Clips

Use the **same reference image** for the same character across every I2V generation in a sequence. The image anchors identity more reliably than text descriptions.

### I2V Motion Scale

| Motion scale | Description | When to use |
|-------------|-------------|-------------|
| "slow push-in, no more than 5%" | Minimal camera movement | Product shots, portraits |
| "slow tracking shot" | Gentle follow | Walking scenes, subtle movement |
| Avoid large camera moves | Breaks source composition | — |

Large camera moves (dramatic zooms, wide pans) conflict with the fixed first frame and break the source composition.

---

## frameImages — First/Last Frame Control (Runware API)

The `frameImages` parameter pins specific images to specific frame positions.

### Options

| Value | Behavior |
|-------|----------|
| Single image (no frame specified) | Defaults to first frame |
| `frame: "first"` | Explicitly pins to first frame |
| `frame: "last"` | Pins to last frame |
| `frame: -1` | Last frame (zero-based indexing) |
| `frame: N` (integer) | Specific frame position (zero-based) |

### Bookend Generation

Provide both a first-frame and a last-frame image. The model fills in all motion between the two fixed visual states. This is powerful for:
- Controlled transitions between two known compositions
- Before/after reveals with guaranteed endpoints
- Brand sequences where start and end frames are mandated

**Example:**
```json
{
  "frameImages": [
    { "url": "opening_frame.jpg", "frame": "first" },
    { "url": "closing_frame.jpg", "frame": "last" }
  ],
  "prompt": "Slow fade from morning to evening, light shifting from cool blue to warm amber. No camera movement. Ambient birdsong transitioning to crickets.",
  "duration": 8
}
```

---

## Reference-to-Video (R2V) — Subject Consistency

The `reference-to-video` endpoint accepts **1–9 reference images** to maintain subject identity, style, and scene continuity.

### Prompt Structure for R2V

Index each image explicitly in the prompt and describe how they interact:

```
Image 1: [describe what this image contains]
Image 2: [describe what this image contains]
Image 3: [describe what this image contains]

[Scene prompt describing how they combine: "Place the bag from Image 1 
into the scene of Image 3, matching the lighting of Image 2."]
```

### R2V Use Cases

| Use case | Reference image strategy |
|----------|------------------------|
| Product placement | Image 1: product; Image 2: target environment; Image 3: lighting reference |
| Character in scene | Image 1: character portrait; Image 2: scene environment |
| Multi-reference compositing | Images 1–3: subject from different angles; Images 4–5: style/scene references |
| Brand consistency | Images 1–2: brand assets; Image 3: talent reference; Image 4: location |

### R2V Tips

- Up to 9 images — use all slots if you have them; more references = tighter identity lock
- Images of the same subject from different angles give better consistency than one image repeated
- Separate style references (how it should look) from subject references (who/what appears)
- Always name which image does what in the prompt text

---

## @element Token Compositing (fal API)

Named assets defined in `happyhorse_elements` and referenced in the prompt with `@element_name`.

### Structure

```json
{
  "happyhorse_elements": [
    {
      "name": "my_bag",
      "description": "A tan leather tote bag with brass hardware and a front pocket",
      "images": ["front_view.jpg", "side_view.jpg", "detail_shot.jpg"]
    },
    {
      "name": "my_brand_logo",
      "description": "A minimal black circular logo with serif text",
      "images": ["logo_black.png", "logo_white.png"]
    }
  ],
  "prompt": "The @my_bag sits on a marble café table. A customer's hand reaches into frame to pick it up. The @my_brand_logo is visible on a receipt beside it. Soft window light from camera-left. Close-up product shot, slight dolly-in. Ambient café sounds, no music. 1080p, 16:9, 6 seconds."
}
```

### Element Rules

- Maximum **3 elements** per task
- 2–4 images per element (different angles/conditions recommended)
- Each element treated as a distinct asset — not blended into a composite
- `name` field becomes the `@token` used in the prompt
- Use lowercase, no spaces in element names: `my_bag` not `My Bag`

---

## Multi-Shot Sequencing (fal Multi-Shot Endpoint)

Up to **5 shots** per call, each up to 12 seconds, generated with character identity and visual style preserved across cuts.

### Structure

```
Protagonist: [Single character description — written once, not repeated per shot]

Shot 1 (0–Xs): [Camera]. [Scene and action]. [Audio].
Shot 2 (X–Ys): [Camera]. [Scene and action]. [Audio].
Shot 3 (Y–Zs): [Camera]. [Scene and action]. [Audio].
Shot 4 (Z–Ws): [Camera]. [Scene and action]. [Audio].
Shot 5 (W–Vs): [Camera]. [Scene and action]. [Audio].
```

**When `multi_shots` is true:** Set final `duration` equal to the sum of all shot durations, or omit entirely.

### Multi-Shot Tips

- Write the protagonist description **once at the top** — repeating it per shot wastes tokens and can create drift
- Each shot should have its own camera direction — don't carry a camera move implicitly
- Name audio per shot; don't assume continuity unless you state it
- Multi-shot mitigates the 5-second character consistency limit by treating each beat as semi-independent

### Multi-Shot vs. Video Edit

| Approach | When to use |
|----------|-------------|
| Multi-shot (single call) | Planned sequences with known shot structure |
| Sequential video-edit passes | Discovered sequences, iterative building |

---

## Natural-Language Video Editing

The `/video-edit` endpoint modifies an existing clip while preserving its original structure, composition, and motion.

### Two Edit Modes

**Global edits:** Apply changes across the entire clip
- Recoloring the sky
- Shifting visual style (day → night, summer → winter)
- Changing season or time of day
- Adjusting color grade

**Local edits:** Target a specific region or element
- Swap an object
- Change a character's outfit
- Replace a background element
- Add or remove a prop

### The Phrase-of-Record for Surgical Edits

```
Change only [X]. Keep [A], [B], [C] exactly the same. [A], [B], [C] remain unchanged.
```

Restate the preserve list **twice** — the model treats both the change instruction and the preserve list as constraints, and listing invariants twice raises their weight.

### Reference Images in Video Edit

Reference images use `[Image 1]`–`[Image 9]` syntax — square brackets, spaced, numbered by
upload order in the `media` array:

```
Swap the character's jacket for the leather jacket shown in [Image 1].
Keep the character's face, hair, body position, and all background elements
exactly the same. Face, hair, body, and background remain unchanged.
```

### Iterative Single-Change Strategy

Each edit pass should change **at most one or two elements**. Multi-region edits in one call produce drift artifacts.

**Workflow:**
1. Base clip generated at 720p
2. Edit pass 1: Change only the lighting
3. Edit pass 2: Change only the character's outfit
4. Edit pass 3: Change only the audio bed
5. Final pass: Upscale to 1080p

Never attempt all changes in one call.

---

## Known Limitations

| Limitation | Mitigation |
|------------|-----------|
| Character drift beyond ~5 seconds | Use multi-shot mode; keep individual shots under 5s |
| Complex multi-object motion conflicts | Break into sequential single-change edit passes |
| Post-April 2026 brand identities/designs not in world knowledge | Provide reference images rather than relying on model inference |
| H100 recommended for full performance | Consumer GPU support was pending at launch |
| Closed source — API access only | Use fal.ai, Runware, WaveSpeed, or Cloudflare AI endpoints |
