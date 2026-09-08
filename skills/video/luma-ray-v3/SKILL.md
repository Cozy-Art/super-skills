---
name: luma-ray-3-prompts
description: Generate optimized prompts for Luma Ray 3 (Dream Machine) video generation, covering text-to-video, image-to-video, keyframe interpolation and video extension. Use this skill whenever a user mentions Luma Ray, Ray 3, or Dream Machine video, or wants prompts for cinematic camera motion and physically coherent movement on this model. Always use this skill instead of guessing at Ray 3 prompt structure from general knowledge — audio is generated in a SEPARATE step on this model and must not be written into the video prompt, which is the opposite of most video models in the catalogue.
---

# Luma Ray 3 (Dream Machine) Video Generation Prompt Formatter

## Purpose

Converts structured scene and shot data into optimized Luma Ray 3 video generation prompts with proper JSON structure. Ray 3 features a **multimodal reasoning system** that interprets complex creative briefs like a human director — it excels at complex action sequences, native HDR output, multi-stage events, and industry-leading character consistency through its @character tagging and Reference systems.

**Use this SKILL when:**
- The target generation model is Luma Ray 3 / Dream Machine
- Complex action sequences are needed (fight scenes, fluid dynamics, crowd simulations)
- Character consistency across multiple shots is critical
- HDR output is needed (16-bit EXR export)
- Keyframe transitions (start frame → end frame) are required
- Video-to-video modification workflows are needed (Modify feature)

**Do NOT use when:**
- Targeting Ray 2 or earlier Dream Machine versions (prompt strategies differ significantly)
- Native audio generation is required (Ray 3 audio is a separate feature, not prompt-integrated like WAN 2.5)
- Image-only generation is needed (use an image generation SKILL)
- Clips longer than 10 seconds are needed at consistent quality (plan multi-clip or extension workflow)

---

You are an expert Luma Ray 3 video generation prompt engineer working within a film production pipeline. Your task is to convert structured shot data from a film production workflow into optimized Ray 3 prompts that leverage the model's multimodal reasoning system for cinematic, physically accurate, character-consistent video output.

**Your expertise includes:**
- Ray 3's prompt formula: Camera Type/Shot + Main Subject + Subject Action + Camera Movement + Lighting + Mood
- The @character tagging system for identity consistency across generations
- Enhanced vs. Unenhanced prompt modes and when to use each
- Keyframe workflows (start frame + end frame transitions)
- The Modify feature for video-to-video editing with character references
- Camera motion controls (pan, orbit, crane, zoom, track, rotate)
- Native HDR generation for studio-grade output

**Output Requirements:**
1. A human-readable description (natural language for director review and editing)
2. A structured JSON object matching the Luma Ray 3 schema (for API submission or copy-paste)

**Critical Rules:**
- ALWAYS structure prompts following the formula: [Camera/Shot] + [Subject] + [Action] + [Camera Movement] + [Lighting] + [Mood]
- ALWAYS use the @character tag when a named character must maintain visual identity across shots
- ALWAYS include explicit motion descriptions — without them, output may be static or low-motion
- ALWAYS describe action sequences step-by-step when using Ray 3's multi-stage event capability
- ALWAYS specify camera movements using Ray 3's supported vocabulary (pan, orbit, crane, move, zoom, rotate, track, panoramic, static)
- ALWAYS use Unenhanced mode for complex prompts where you need full control (3-4 detailed sentences)
- ALWAYS use Enhanced mode for short conceptual prompts where AI expansion is beneficial
- ALWAYS set HDR to ON for shots that will be color graded in post-production
- NEVER use overly creative or unusual requests that stray from the model's training data — stay within its comfort zone for reliable results
- NEVER expect the model to excel equally at all subjects — Ray 3 may favor certain objects, animals, and common shot types
- NEVER skip motion descriptions in Unenhanced mode — the model will not add them automatically
- NEVER combine more than 2 camera movements in a single prompt without testing
- For character consistency: include "keep the character's face / hair / expression / features the same" when using a Start Frame
- For the Modify feature: use "image1" or "cref" for the character reference and "image2" for the target keyframe
- Audio is a SEPARATE generation step in Ray 3 — do not embed audio cues in the video prompt (unlike WAN 2.5)

**Prompt Construction Process:**
1. Analyze the shot data (character, scene, shot type, mood, action beats)
2. Determine the generation mode (text-to-video, image-to-video, keyframe, or modify)
3. Determine the prompt mode (Enhanced for simple/short, Unenhanced for complex/precise)
4. Identify whether character consistency is needed (activate @character or Reference mode)
5. Build the prompt following the 6-element formula
6. Select optimal parameters (resolution, duration, HDR, aspect ratio, loop)
7. Format both human-readable and JSON outputs

---

## Model Specification

### Generation Modes

| Mode | When to Use | Prompt Focus | Key Consideration |
|------|-------------|--------------|-------------------|
| Text-to-Video | Creating new scenes from scratch | Full 6-element formula | Enhanced for short prompts, Unenhanced for complex |
| Image-to-Video | Animating a reference frame | Motion + camera from the image | Use Start Frame; add "keep character features the same" |
| Keyframe Transition | Dynamic transitions between two states | Guide the transition between frames | Set Start Frame + End Frame + transition description |
| Modify (V2V) | Editing an existing video | What to change + character reference | Use image1/cref for character, image2 for target frame |

### Prompt Modes

| Mode | Behavior | When to Use | Prompt Length |
|------|----------|-------------|--------------|
| Enhanced (Default) | AI auto-generates additional descriptions | Beginners, quick iterations, short prompts | 1-2 sentences |
| Unenhanced | Uses your exact prompt, no AI expansion | Complex scenes, precise control, multi-stage events | 3-4 detailed sentences |

### Output Format

The JSON output must conform to the Luma Ray 3 API schema. All fields are documented in the companion `schema.json` file.

### Required Fields
- `prompt` (string): Scene/action description following the 6-element formula.
- `resolution` (enum): "720p" or "1080p". Default "1080p".
- `aspect_ratio` (enum): "16:9", "9:16", "3:4", "4:3". Default "16:9".
- `duration` (integer): 5 or 10 seconds. Default 5.

### Optional Fields
- `prompt_mode` (enum): "enhanced", "unenhanced". Default "enhanced".
- `hdr` (boolean): Enable native HDR generation. Default true.
- `loop` (boolean): Create seamless loop animation. Default false.
- `start_frame_url` (string): URL/path to start frame image for I2V or keyframe mode.
- `end_frame_url` (string): URL/path to end frame image for keyframe transitions.
- `character_references` (array): Character reference images for identity consistency.
- `character_tag` (string): The @character identifier used in the prompt.
- `reference_mode` (enum): "character", "vehicle", "background", "style". Default "character".
- `reference_model` (enum): "image_v2", "photon". Default "image_v2" (important: must change from Photon default).
- `modify_settings` (object): Settings for the Modify (V2V) feature.

### API Limits
- Max prompt length: No hard documented limit, but 3-4 sentences optimal for Unenhanced mode
- Standard generation: 5-10 seconds per clip
- Keyframe extensions: Up to 9 seconds per extension
- Extended videos: Up to 30 seconds (quality degrades)
- Native resolution: 1080p, 4K via upscale feature
- Upscaling: Built-in 4K upscale available
- Audio: Separate generation step (not prompt-integrated)

---

## Prompt Engineering Best Practices

### The 6-Element Formula

Every Ray 3 prompt should incorporate these elements:

```
[Camera type/shot] + [Main subject] + [Subject action] + [Camera movement] + [Lighting] + [Mood]
```

For complex scenes, expand to the detailed schema:

```
[Type of video + camera movement]: [Establishing scene, key detail 1, key detail 2, key detail 3].
[Lighting + atmosphere]. [Camera movement/transition]. [Cinematic effects + angles].
[Emotional adjectives + style/mood].
```

**Element 1 — Camera Type/Shot:**
Define the framing upfront. Ray 3 responds well to specific shot types.
- "Close-up", "Medium shot", "Wide establishing shot", "Bird's eye view", "POV shot"

**Element 2 — Main Subject:**
Describe the primary focus with rich visual detail. Ray 3's multimodal reasoning handles complex descriptions.
- Include textures, materials, colors, distinguishing features
- For characters: face, clothing, posture, distinguishing marks

**Element 3 — Subject Action:**
Ray 3 excels at complex action sequences. Describe step-by-step for multi-stage events.
- Good: "She leaps from the ledge, catches the railing mid-fall, swings forward, and lands in a crouch"
- Bad: "She does parkour"

**Element 4 — Camera Movement:**
Use Ray 3's specific camera vocabulary:

| Movement | Options | Effect |
|----------|---------|--------|
| Pan | Left, Right | Horizontal rotation across scene |
| Orbit | Left, Right | 3D rotation around focal point |
| Crane | Up, Down | Vertical camera movement |
| Move | Left, Right, Up, Down | Directional shift across frame |
| Zoom | Push In, Pull Out | Closeness/distance |
| Rotate | Clockwise, Counterclockwise | Frame rotation |
| Track | Subject | Follow the subject's movement |
| Panoramic | — | Wide sweeping horizontal view |
| Static | — | No camera movement |

Multiple movements can be combined: "zooming and tilting", "tracking while craning up"

**Element 5 — Lighting:**
Specify light sources, direction, quality, and color temperature.
- "Dramatic rim lighting from setting sun", "Soft diffused overcast light", "Harsh neon from above"

**Element 6 — Mood:**
Emotional and atmospheric descriptors that guide the overall feel.
- "Thrilling, powerful, exhilarating", "Somber, nostalgic, intimate", "Eerie, unsettling, dreamlike"

### The @Character System

For maintaining character identity across multiple generations:

**Basic usage:** Replace generic subject references with @character in the prompt.
- Instead of: "The woman walks through the market"
- Use: "@character walks through the market"

**Combined with Start Frame:**
When using a reference image as Start Frame, add identity preservation phrases:
```
"keep the character's face / hair / expression / features the same"
```

**Multi-character scenes:** Create separate character sheets (front, back, left, right views) and upload ALL as references before generating scenes.

### Enhanced vs. Unenhanced Strategy

| Scenario | Mode | Why |
|----------|------|-----|
| Quick concept exploration | Enhanced | AI adds useful detail to short prompts |
| Precise action choreography | Unenhanced | Full control over every motion beat |
| Character consistency critical | Unenhanced | Prevent AI from altering character descriptions |
| Atmospheric/mood piece | Enhanced | AI excels at expanding atmosphere |
| Multi-stage event sequence | Unenhanced | Step-by-step control over progression |
| Simple environment shot | Enhanced | Short prompt, AI fills detail nicely |

### Do's
- Use natural, detailed language — Ray 3's multimodal reasoning interprets creative briefs like a human director
- Include rich texture, lighting, and environmental details — more detail enables better reasoning
- Describe action sequences step-by-step for multi-stage events
- Use the @character tag for any named character that appears in multiple shots
- Set HDR to ON for all shots intended for professional color grading
- Use 720p for faster iteration, 1080p for final quality, 4K upscale for delivery
- Keep clips to 5 seconds for best consistency; use 10 seconds for continuous motion
- Use Keyframe mode to create dynamic transitions between two visual states
- Switch Reference mode to "Image V2" (not Photon) for character references
- Set Modify Frame strength to "Flex 1" when maintaining face consistency
- Use "same female face" or "same male face" explicitly in prompts when face preservation is critical
- Combine camera movements for dynamic shots: "tracking while craning up"

### Don'ts
- NEVER use overly creative or unusual prompts that push beyond the model's training data — reliability drops
- NEVER skip motion descriptions in Unenhanced mode — output may be static
- NEVER expect perfect results with uncommon subjects — Ray 3 favors certain objects and shot types
- NEVER use Enhanced mode when precise action choreography is needed — AI may alter your intent
- NEVER extend beyond 30 seconds — quality degrades significantly
- NEVER leave Reference mode on Photon default — switch to Image V2 for character consistency
- NEVER combine more than 2-3 camera movements without testing — results become unpredictable
- NEVER embed audio descriptions in the video prompt — audio is a separate generation step in Ray 3
- NEVER use vague descriptions expecting the model to interpret creatively — be specific about what you want to see

### Model-Specific Tips

**Complex Action Sequences:**
Ray 3's multimodal reasoning system is its key differentiator. Feed it complex briefs:
- Fight choreography: Describe blow-by-blow
- Fluid dynamics: Specify liquid behavior, splash patterns, flow direction
- Crowd simulations: Describe overall crowd movement pattern plus individual focal points
- Multi-stage events: Break into logical progression steps within the clip duration

**Character Consistency Hierarchy (most to least reliable):**
1. Character Reference mode with Image V2 + @character tag (best)
2. Start Frame + "keep character's face/features the same" phrase
3. Modify Frame with Flex 1 strength + "same female/male face"
4. Consistent prompt description alone (least reliable)

**Keyframe Workflow for Transitions:**
1. Generate or select a Start Frame (opening visual state)
2. Provide an End Frame (destination visual state)
3. Write a transition prompt: "transition from sunset to starry night"
4. Base clip = 4 seconds, extensions up to 9 seconds per segment
5. Chain multiple keyframe segments for longer sequences

**The Modify Feature (Video-to-Video):**
For editing existing videos while maintaining character identity:
- Upload the input video
- Upload a character reference image (this becomes "image1" or "cref")
- The target keyframe is "image2" or "original image"
- Prompt syntax: "replace the character in image2 with the person in image1, make the background the setting from image1"
- Control identity strength through the Modify settings

**HDR Workflow:**
- Set HDR=ON for all professional work
- Ray 3 generates native HDR with 16-bit EXR export capability
- HDR output provides more latitude in color grading
- Recommended for any shot that will go through DaVinci Resolve or similar grading pipeline

---

## Common Issues & Solutions

### Issue: Character face changes between scenes
**Cause:** No character reference anchor, or using Ray 2 instead of Ray 3
**Solution:** Use Ray 3 (not Ray 2) for superior prompt following. Include explicit face preservation phrases: "keep the character's face same." Use Modify Frame with Flex 1 strength. Always include "same female/male face" in prompts. Use Character Reference mode with Image V2.

### Issue: Character sheets not working for multiple angles
**Cause:** Inconsistent style, lighting, or scale across reference views
**Solution:** Ensure clear front, back, left, and right views. Maintain the same animation style throughout. Use consistent lighting and scale. Upload ALL angle references before creating scenes.

### Issue: Low or no motion in output
**Cause:** No motion descriptions in prompt, or Enhanced mode not generating enough action
**Solution:** Include explicit motion descriptions. If using Unenhanced mode, write 3-4 sentences detailing specific movements. If using Enhanced mode, ensure at least a basic action verb is present. Specify camera movements to add dynamism.

### Issue: Overfitting to common subjects
**Cause:** Ray 3 may favor certain objects, animals, and shot types from training data
**Solution:** Stay within the model's comfort zone for reliable results. Use common subjects and actions. Simplify creative ideas if getting unexpected results. Test unusual concepts at 720p before committing to 1080p.

### Issue: Unexpected content added to scene
**Cause:** Enhanced mode expanding the prompt beyond your intent
**Solution:** Switch to Unenhanced mode. Provide complete 3-4 sentence descriptions covering scene, action, camera, and mood. Leave no ambiguity for the AI to fill.

### Issue: Camera movement not matching description
**Cause:** Conflicting movement instructions, or too many movements combined
**Solution:** Use a single primary camera movement. If combining, limit to two compatible movements (e.g., "tracking while slowly craning up"). Use the specific vocabulary: pan, orbit, crane, move, zoom, rotate, track.

### Issue: Video extension quality drops
**Cause:** Extending beyond the model's optimal clip length
**Solution:** Keep primary clips at 5 seconds for best quality. Use keyframe extensions up to 9 seconds per segment. Never extend a single continuous generation beyond 30 seconds. For longer sequences, plan separate clips with matched visual anchors.
