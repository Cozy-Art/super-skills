# PixVerse V6 — Continuity and Reference Features

---

## Multi-Image Character Reference (V6's Primary Consistency Tool)

V6's biggest consistency upgrade from V5.5: accepts multiple reference images of the same character and locks visual identity across all shots.

### How It Works

- Upload multiple angles of the subject (front, 3/4, side) in the web UI's reference image uploader
- V6 builds an internal identity model from the full angle set
- Clothing, facial features, hair, and body proportions remain stable across camera angle changes, lighting shifts, and multi-shot transitions

### Recommended Reference Set

| Angle | Why it matters |
|-------|---------------|
| Front-facing | Primary facial feature lock |
| 3/4 turn | Profile-to-front range |
| Full side | Ear, jaw, and silhouette definition |

**Minimum:** 1 reference image (I2V mode)  
**Recommended for consistency:** 3+ reference images from different angles

### API Usage

Pass as an ordered image array in third-party API schemas (WaveSpeed, Dzine). Full V6 API schema for multi-image reference is published by third-party platforms until PixVerse releases official V6 API documentation.

### Combined with Text Descriptors

For maximum identity stability: combine multi-image reference with explicit text descriptors in the prompt.

```
"Woman with short copper-red hair, freckles, green eyes, grey wool coat."
```

Both the visual reference and the text description reinforce each other. Use both.

---

## Multi-Shot Engine (Native V6 Continuity)

V6's multi-shot engine internally tracks spatial relationships, lighting logic, and surface materials between shots — eliminating the seam artifacts that required manual stitching in V5.6.

### Operational Rules

**Rule 1: Repeat core character descriptors in every shot.**
The engine uses text descriptors as anchors, not just images. A character described only in Shot 1 may drift in Shot 2 without text reinforcement.

```
Shot 1: "A woman with short auburn hair, dark blue jacket..."
Shot 2: "The same woman with short auburn hair, dark blue jacket, now indoors..."
```

**Rule 2: Use identical vocabulary for shared elements.**
Vocabulary consistency helps the engine track spatial continuity. If Shot 1 says "marble floor," Shot 2 must also say "marble floor" — not "polished stone surface" or "light-colored floor."

| Shot 1 | Shot 2 — consistent ✅ | Shot 2 — inconsistent ❌ |
|--------|----------------------|------------------------|
| "marble floor" | "marble floor" | "polished stone surface" |
| "glass office building" | "same glass office building" | "modern structure with windows" |
| "warm amber tones" | "warm amber tones" | "golden light" |

**Rule 3: Establish environment vocabulary once, reference it in subsequent shots.**
Shot 1 establishes the environment in detail. Subsequent shots reference it briefly with consistent terminology rather than re-establishing from scratch.

### Multi-Shot Prompt Structure

```
Shot 1: [Full 5-part description: subject + action + environment + camera + style]

Shot 2: [Subject with same key descriptors] + [new action] + [environment — same vocabulary] + [camera] + [same style keywords]

Shot 3: [Same pattern...]

Audio: [ambient description across shots, noting changes between shots]
```

### Best Use Cases

- Product reveals and brand narratives
- Short documentary cutaways
- Narrative ad spots with scene changes
- Before/after sequences with character continuity

---

## Transition Prompting (Manual Chaining for Edge Cases)

For sequences not handled by the multi-shot engine, or when chaining separate generations:

**Clip 1 ending:**
```
"Scene ends with character opening door and stepping through threshold."
```

**Clip 2 opening:**
```
"Scene begins with the same character emerging from the doorway into the new room,
matching the exit position and facing direction from the previous clip."
```

Explicit spatial handoff at clip boundaries is the most reliable method for seamless stitching. Match:
- Character position in frame
- Facing direction
- Body posture
- Lighting direction and color temperature

---

## First/Last Frame Interpolation

Available via legacy API parameters `first_frame_img` and `last_frame_img`. Supply two keyframe images and V6 generates all frames in between.

### How It Works

1. Supply `first_frame_img` — the opening visual state
2. Supply `last_frame_img` — the closing visual state
3. Write a prompt describing the motion and transformation between them
4. V6 interpolates motion, lighting, and transformation across the intermediate frames

### Best Use Cases

- Before/after product reveals (packaged → opened)
- Stylized character transitions (formal → casual)
- Controlled scene dissolves (day → evening)
- Object transformation sequences

### Prompt for First/Last Frame

Focus on the **transition quality** — how the change happens, not what the start and end states look like (those are already provided):

```
"Smooth, gradual transition. Lighting shifts from cool morning to warm afternoon.
The change is natural and physically motivated."
```

---

## LipSync and TTS Modes

Three audio input modes — mutually exclusive. Choose one per generation.

### Mode 1: AI-Generated Ambient + SFX

```json
"generate_audio_switch": true
```

Produces synchronized ambient soundscapes and effects matching on-screen content. Not music generation.

Best for: atmospheric scenes, nature, product video, environmental storytelling.

### Mode 2: TTS with Scripted Dialogue

```json
"lip_sync_tts_speaker_id": "[speaker_id]",
"lip_sync_tts_content": "[script text ≤200 chars]"
```

Built-in TTS engine with multilingual support. V6 demonstrated reliable lip-sync with Japanese dialogue in official benchmarks.

**Encoding note:** Do not use UTF-8 encoding for TTS content. For CJK characters (Chinese, Japanese, Korean), test carefully — TTS mode is the recommended path for non-Latin dialogue.

**Multilingual dialogue syntax (in prompt):**
```
Japanese dialogue — Male (Gentle): 'お疲れ様、夜の古街は危ないですよ.'
Female (Surprised): 'あ、あなたは…妖ですか？'
```

### Mode 3: External Audio Upload

```json
"audio_media_id": "[media_id_from_upload]"
```

Upload MP3 or WAV. Model syncs lip movement to the provided audio track.

Best for: professional voiceover, pre-recorded music, licensed sound design.

---

## Video Extension (Extend Feature)

The web UI's `Extend` button and the API's `source_video_id` parameter continue a generated video from its last frame.

### Workflow

1. Generate initial clip
2. Submit that clip via `Extend` (UI) or `source_video_id` (API)
3. Write a new prompt describing what happens next

### Extension Prompt Rules

- **Repeat subject and environment descriptors verbatim** from the original prompt
- **Describe only new motion or changes** — don't re-establish what already exists
- **Maintain the same resolution and aspect ratio** for seamless continuity

**Extension prompt template:**
```
[Exact subject description from original]. [Exact environment description from original].
[New action or motion that begins at the extension point].
[Camera behavior for this extension].
[Same style keywords from original].
```

### Audio in Extensions

If audio was enabled in the original, enable it in the extension with the same audio mode to maintain continuity. If switching audio mode (e.g., from ambient to TTS), note that audio texture will change at the seam.

---

## Seed Strategy for Consistency

The `seed` parameter reproduces a specific generation when all other parameters remain constant.

**Workflow:**

1. Generate 2–4 results with random seeds — evaluate which visual interpretation is correct
2. Note the seed from the best result
3. Lock that seed for all subsequent iterations
4. Change only the prompt (not parameters) to maintain seed-consistent visual treatment

**Cross-generation consistency:** Use the same seed across related generations (same character in different locations) to maintain consistent lighting interpretation and color treatment. Not as robust as multi-image reference, but useful for style consistency.
