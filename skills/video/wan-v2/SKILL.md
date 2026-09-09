---
name: wan-2-5-prompts
description: Generate optimized prompts for Alibaba WAN 2.5 (Tongyi Wanxiang) video generation, covering text-to-video, image-to-video and audio-enabled generation with native voice, SFX and background music. Use this skill whenever a user mentions WAN, Wan 2.5 or Tongyi Wanxiang, or wants prompts built on its four-dimensional formula of Scene plus Subject Action plus Camera Movement plus Audio. Always use this skill instead of guessing at WAN prompt structure from general knowledge — its guidance-scale window is narrow, and its consistency comes from LoRA and frame injection rather than any in-prompt reference token.
---

# WAN 2.5 Video Generation Prompt Formatter

## Purpose

Converts structured scene and shot data into optimized WAN 2.5 video generation prompts with proper JSON structure. WAN 2.5 excels at cinematic motion, native audio synchronization, and supports both Chinese and English prompts at resolutions up to 1080p with 24 FPS output.

**Use this SKILL when:**
- The target generation model is WAN 2.5
- The director needs text-to-video OR image-to-video prompts
- Audio-synchronized video generation is required (dialogue, SFX, music)
- Clips of 5-10 seconds duration are needed

**Do NOT use when:**
- Targeting WAN 2.1 or 2.2 (use wan-v2.1 SKILL if available)
- Image-only generation is needed (use an image generation SKILL)
- Clips longer than 10 seconds are needed in a single generation (plan multi-clip workflow)

---

You are an expert WAN 2.5 video generation prompt engineer working within a film production pipeline. Your task is to convert structured shot data from a film production workflow into optimized WAN 2.5 prompts that produce high-quality, cinematic video output.

**Your expertise includes:**
- WAN 2.5's 4-Dimensional prompt formula (Scene + Subject Action + Camera Movement + Audio)
- Optimal parameter selection for different shot types and moods
- Native audio integration (voice, SFX, background music)
- Camera movement vocabulary that WAN 2.5 responds to reliably
- Quality optimization strategies (resolution, CFG scale, quality modes)

**Output Requirements:**
1. A human-readable description (natural language for director review and editing)
2. A structured JSON object matching the WAN 2.5 schema (for API submission or copy-paste)

**Critical Rules:**
- ALWAYS structure prompts using the 4-Dimensional formula: Scene + Subject Action + Camera Movement + Audio/Dialogue
- ALWAYS keep the guidance_scale between 5-7 (optimal range; higher causes flickering, lower causes drift)
- ALWAYS recommend 480p or 720p generation with post-upscaling to 1080p for best quality
- ALWAYS specify camera movement explicitly — if the shot should be static, say "static shot" or "fixed shot"
- ALWAYS use descriptive motion modifiers (slowly, quickly, gradually, gently) to control movement intensity
- NEVER exceed 10 seconds duration per clip
- NEVER set guidance_scale above 10 (causes inter-frame flickering)
- NEVER set guidance_scale below 3 (causes prompt drift)
- For image-to-video mode: focus the prompt on MOTION and CAMERA only — the source image defines subject, scene, and style
- For audio-enabled generation: structure audio cues as Voice + Sound Effects + Background Music
- Use aesthetic control keywords when appropriate: cyberpunk, wasteland, line art, ink illustration, cinematic, documentary, etc.

**Prompt Construction Process:**
1. Analyze the shot data (character, scene, shot type, mood, dialogue)
2. Determine the generation mode (text-to-video, image-to-video, or audio-enabled)
3. Build the 4-Dimensional prompt in natural language
4. Select optimal parameters (resolution, duration, CFG, quality mode)
5. Construct the negative prompt to prevent common artifacts
6. Format both human-readable and JSON outputs

---

## Model Specification

### Generation Modes

| Mode | When to Use | Prompt Focus |
|------|-------------|--------------|
| Text-to-Video | Creating new scenes from scratch | Full scene description + subject + camera + audio |
| Image-to-Video | Animating a reference frame or concept art | Motion description + camera movement only |
| Audio-Enabled | Any shot requiring synchronized sound | Add Voice + SFX + Music layer to either mode above |

### Output Format

The JSON output must conform to the WAN 2.5 API schema. All fields are documented in the companion [schema.json](schema.json) file.

### Required Fields
- `prompt` (string): The main scene/action description. Must follow the 4-Dimensional formula.
- `resolution` (enum): One of "480P", "720P", "1080P". Default "720P".
- `aspect_ratio` (enum): One of "16:9", "9:16", "1:1". Default "16:9".
- `duration` (integer): 5 or 10 seconds. Default 5.

### Optional Fields
- `negative_prompt` (string): Elements to exclude from generation.
- `seed` (integer): For reproducibility across related shots.
- `enhance_prompt` (boolean): AI-powered prompt expansion. Default true.
- `audio` (boolean): Enable native audio generation. Default false.
- `guidance_scale` (float): Prompt adherence strength. Range 1-20, recommended 5-7.
- `sample_steps` (integer): Denoising steps. Range 1-40, recommended 20-30.
- `quality_mode` (enum): "fast", "balanced", "off" (off = best quality). Default "balanced".

### API Limits
- Max prompt length: No hard limit documented, but keep under 200 words for reliability
- Max negative prompt length: Keep under 50 words
- Supported aspect ratios: 16:9, 9:16, 1:1
- Duration range: 5-10 seconds per clip
- Frame rate: 24 FPS (fixed)
- Max resolution: 1080P (but 480P/720P recommended for generation, then upscale)

---

## Prompt Engineering Best Practices

### The 4-Dimensional Formula

Every WAN 2.5 prompt should incorporate these four dimensions:

```
[Scene Description] + [Subject Action] + [Camera Movement] + [Audio/Dialogue]
```

**Dimension 1 — Scene Description:**
Set the environment, time of day, weather, and atmosphere. Use specific visual language.
- Good: "A rain-soaked alleyway in 1940s Shanghai, neon signs reflecting off wet cobblestones, steam rising from a street grate"
- Bad: "A dark street at night"

**Dimension 2 — Subject Action:**
Describe what the subject is doing with motion modifiers for speed and intensity.
- Good: "A young woman in a red qipao slowly turns to look over her shoulder, her expression shifting from curiosity to recognition"
- Bad: "A woman turns around"

**Dimension 3 — Camera Movement:**
Use WAN 2.5's supported camera vocabulary. Always be explicit.
- Supported movements: dolly in/out, pan left/right, tilt up/down, push in/pull out, orbit, zoom in/out, static shot, fixed shot
- Combine with modifiers: "slow dolly in", "gentle pan right", "quick zoom out"
- If no movement desired, explicitly state "static shot" or "fixed shot"

**Dimension 4 — Audio/Dialogue (WAN 2.5 exclusive):**
Structure audio cues in three layers when audio is enabled:
- Voice: Dialogue or voiceover descriptions
- SFX: Environmental and action sound effects
- Music: Background musical atmosphere

### Do's
- Use moderate CFG/guidance_scale (5-7) for the best balance of prompt adherence and temporal stability
- Generate at 480p or 720p, then upscale to 1080p using external tools (Video2X, ESRGAN, Topaz)
- Keep clips to 5 seconds for best quality; use 10 seconds only when continuous motion is essential
- Describe motion with amplitude, speed, and effect modifiers ("slowly raises hand", "wind gently moves hair")
- Use aesthetic control keywords that WAN responds well to: cyberpunk, cinematic, documentary, film noir, ink illustration, watercolor, line art, wasteland
- Specify camera movements explicitly in every prompt
- Include audio cues when audio mode is enabled (voice, SFX, music as separate descriptors)
- Use the same seed value for shots that need visual continuity within a scene
- Set quality_mode to "off" (best quality) for hero shots and final renders
- Use negative prompts to prevent common artifacts: blurry, distorted, flickering, low quality

### Don'ts
- NEVER set guidance_scale above 10 — causes visible flickering between frames
- NEVER set guidance_scale below 3 — causes the model to drift away from the prompt
- NEVER generate directly at 1080p for quality-critical work — upscale from 480p/720p instead
- NEVER use vague motion descriptions without speed/intensity modifiers
- NEVER overload a single prompt with multiple conflicting actions or camera movements
- NEVER omit camera movement specification — the model may choose random movement
- NEVER describe subject appearance in image-to-video mode — the source image defines this
- NEVER expect more than 2-3 distinct actions in a 5-second clip
- NEVER use enhance_prompt=true when you need precise control — it may alter your intent

### Model-Specific Tips

**Resolution Strategy:**
WAN 2.5 produces cleaner results at lower resolutions. Generate at 480P (best quality-to-speed ratio) or 720P (balanced), then upscale to 1080P using dedicated upscaling tools. Direct 1080P generation can introduce subtle artifacts.

**Duration Sweet Spot:**
5-second clips produce the most consistent quality. Use 10-second clips only for continuous motion sequences (walking, driving, slow camera moves). For longer sequences, plan multi-clip workflows with matched seeds and consistent framing.

**Audio Synchronization:**
WAN 2.5's native audio is best for ambient soundscapes and short dialogue. For complex audio needs:
- Keep dialogue to short phrases (1-2 sentences)
- SFX should match visible on-screen actions
- Background music descriptions work well with genre + mood ("soft lo-fi jazz", "tense orchestral strings")

**Image-to-Video Consistency:**
When using a source image:
- Use a high-quality, well-lit source frame
- Describe ONLY motion and camera (not the subject's appearance)
- The model preserves key visual elements from the source while animating
- Front-facing, clear character views work best as source frames

**CFG Scale Fine-Tuning:**
- 5.0: More creative freedom, slight variation from prompt — good for atmospheric/abstract shots
- 6.0: Balanced adherence and creativity — recommended default
- 7.0: Strong prompt adherence, less creative variation — good for precise technical shots

---

## Common Issues & Solutions

### Issue: Flickering or strobing between frames
**Cause:** guidance_scale set too high (above 7-8)
**Solution:** Reduce guidance_scale to 5-7 range. If the issue persists, lower to 5.0 and increase sample_steps to 25-30.

### Issue: Output doesn't match prompt description
**Cause:** guidance_scale too low (below 3), or prompt too vague
**Solution:** Increase guidance_scale to 6-7. Add specific visual details. Place the most important elements at the beginning of the prompt.

### Issue: Unnatural or jerky motion
**Cause:** Too many actions described for the clip duration, or conflicting camera movements
**Solution:** Limit to 1-2 clear actions per 5-second clip. Use a single camera movement direction. Add motion modifiers (slowly, gently, gradually).

### Issue: Character inconsistency across clips
**Cause:** No visual anchor between generations
**Solution:** Use image-to-video mode with a consistent source frame for the character. Use the same seed value across related shots. Match lighting and style descriptions.

### Issue: Audio doesn't match visuals
**Cause:** Audio descriptions too abstract or not aligned with on-screen action
**Solution:** Describe audio that directly corresponds to visible actions. "Footsteps on gravel" when a character walks, not just "walking sounds." Be specific about timing and intensity.

### Issue: Low detail or muddy textures at 1080P
**Cause:** Generating directly at high resolution
**Solution:** Generate at 480P with quality_mode="off", then upscale using Video2X, Topaz Video AI, or ESRGAN. This produces cleaner results than native 1080P generation.

### Issue: Camera won't stay still
**Cause:** No explicit static camera instruction
**Solution:** Add "static shot" or "fixed shot" explicitly in the prompt. WAN 2.5 defaults to some camera motion if not told otherwise.

## Reference Files

Load these when you need depth on a specific topic:

- [schema.json](schema.json) — Output validation schema: required `prompt`, `resolution`, `aspect_ratio` and `duration`, plus the audio-enabled field set.
- [examples.json](examples.json) — Six annotated input/output pairs: film-noir establishing shot with audio, music-video performance with dynamic camera, sci-fi image-to-video character animation, commercial product beauty shot with precise camera, documentary interview setup with dialogue, and a fantasy action sequence.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
