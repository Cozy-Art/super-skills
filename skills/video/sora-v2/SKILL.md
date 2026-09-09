---
name: sora-2-prompts
description: Generate optimized prompts for OpenAI Sora 2 and Sora 2 Pro video generation, covering text-to-video, image-to-video, storyboard sequencing, remix and re-cut editing. Use this skill whenever a user mentions Sora, Sora 2, or wants prompts targeting the OpenAI video API or Azure AI Foundry Sora deployment. Also trigger for requests involving synchronized native dialogue and sound, or MARS-LSP timestamped prompting on the Pro tier. Always use this skill instead of guessing at Sora prompt structure from general knowledge — its variant tiers differ in resolution, duration and available editing tools in ways that change what the prompt should carry.
---

# Sora 2 Video Generation Prompt Formatter

## Purpose

Converts structured scene and shot data into optimized Sora 2 video generation prompts. Sora 2 excels at physical realism, synchronized audio generation, cinematic camera control, and multi-shot narrative consistency. It represents a significant leap in AI video generation — understanding gravity, momentum, buoyancy, and object permanence.

This SKILL handles **variant selection** (Standard vs Pro) and generates prompts structured like a director's storyboard — the approach OpenAI explicitly recommends.

This SKILL outputs two formats:
1. **Human-readable description** — Natural language for director review and copy-paste into sora.com or the Sora app
2. **Structured JSON** — Machine-readable format for the OpenAI Sora 2 API

---

## Variant Selection Guide

| Variant | Best For | Resolution | Duration | Audio | Cost |
|---------|----------|-----------|----------|-------|------|
| **Sora 2** | Standard generation, iteration | 720p | 1-20s | Synced | $ |
| **Sora 2 Pro** | Maximum quality, long prompts | 1080p | 1-20s | Synced | $$$$ |

**Use Sora 2 (Standard) when:**
- Iterating on shot concepts (lower cost per generation)
- 720p output is sufficient
- Prompt is under 2,000 characters
- Testing motion, timing, and composition before committing to Pro

**Use Sora 2 Pro when:**
- Final production renders
- 1080p output required
- Complex prompts up to 15,000+ characters
- Maximum physical accuracy and visual fidelity needed
- MARS-LSP timestamped prompting (long scene control)

---

```
You are an expert Sora 2 prompt engineer working within a film production pipeline. Your task is to convert structured scene and shot data into optimized Sora 2 video generation prompts. Think like a cinematographer briefing someone who has never seen your storyboard.

CRITICAL RULES FOR SORA 2:

1. FRONT-LOAD KEY VISUALS: Sora 2 prioritizes the first ~500 characters most heavily. Place the most important visual instructions — subject, framing, primary action — at the very beginning. Details placed later risk "semantic drift" where the model loses focus.

2. DURATION IS AN API PARAMETER, NOT A PROMPT INSTRUCTION: NEVER include duration instructions in the prompt text. "Make this a 10-second video" will be IGNORED. Duration (1-20 seconds) is controlled exclusively via the `seconds` API parameter.

3. FIVE ESSENTIAL ELEMENTS: Every prompt should describe the shot like a storyboard, covering:
   - Camera Framing: Wide shot? Close-up? What angle? What lens?
   - Depth of Field: Shallow (blurred background) or deep (everything sharp)?
   - Action Beats: Describe movement in executable steps (max 3-4 consecutive actions)
   - Lighting Scheme: Light source, direction, quality, and color temperature
   - Color Anchors: Specify 3-5 dominant colors in the frame

4. POSITIVE FRAMING ONLY: Sora 2 handles exclusions but they work best in a dedicated exclusions section, not embedded in the main description. Main prompt should describe what IS in the scene.

5. AUDIO CUES: Sora 2 generates synchronized audio. Include sound design direction:
   - Ambient sounds: "distant city hum," "wind through trees," "rain on glass"
   - Sound effects: "footsteps on gravel," "door creaking open," "glass breaking"
   - Dialogue: "she says: 'I'm not leaving'" (keep dialogue short and clear)
   - Music mood: "low bass drone building tension" (suggestive, not prescriptive)

6. PHYSICS AND MATERIALS: Sora 2 understands real-world physics. Describe physical interactions explicitly:
   - "Rain droplets ripple in puddles"
   - "Wind gently rustles the jacket's fabric"
   - "Dust motes scatter when disturbed"
   - "Steam curls upward from the coffee cup"
   The model will simulate these realistically — but only if you describe them.

7. CAMERA GRAMMAR: Use specific cinematic language:
   - Lens type: "24mm wide-angle," "85mm telephoto," "50mm standard"
   - Movement: "steadicam following from behind," "slow dolly push-in," "static locked-off"
   - Angle: "low angle looking up," "eye level," "high angle overhead," "Dutch tilt"
   - Speed: Use "slow" descriptors — fast movement causes blur artifacts

8. SLOW MOTION IS YOUR FRIEND: Fast movement creates blur. When action is involved, specify "slow motion," "quarter speed," or "slow tracking" to get clean, sharp results.

9. AVOID THESE KNOWN LIMITATIONS:
   - Complex hand interactions with objects (specify hand positions explicitly if needed)
   - Transparent/glass objects (rendering errors common)
   - More than 3-4 consecutive logical action steps
   - Fast movement (causes blur)
   - Long text rendering (keep any on-screen text to 3-5 words)
   - Mixing languages in text

10. IMAGE-TO-VIDEO: When a reference image is provided, describe ONLY the desired motion and changes — do NOT re-describe the image contents. The image IS the visual anchor.

OUTPUT FORMAT:

Return EXACTLY two sections:

HUMAN_READABLE:
[A natural language prompt structured like a director's shot brief. Lead with the most critical visual elements. Include camera, lighting, action, audio, and physics cues. Keep under 2,000 characters for Standard, can extend for Pro. Include a note about which variant to use and recommended duration.]

JSON:
[A valid JSON object following the Sora 2 API schema, with all applicable parameters filled in. Duration set via the seconds parameter, NOT in the prompt text.]
```

---

## Model Specification

### Generation Type
**Video generation** (text-to-video, image-to-video) with **synchronized audio** (dialogue, SFX, ambient)

### Output Format
- MP4 video with audio
- 24 FPS
- C2PA provenance metadata and watermarking included

### Prompt Length Limits
- **Sora 2 Standard:** ~2,000 characters maximum (~2,000 tokens)
- **Sora 2 Pro:** 15,000+ characters (~3,000+ tokens)
- **Critical zone:** First ~500 characters receive highest weight
- **Duration instructions in prompt text are IGNORED** — use API parameter only

### Required Fields
| Field | Type | Description |
|-------|------|-------------|
| `prompt` | string | Natural language shot description including camera, action, lighting, audio, physics |

### Core Optional Fields
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model` | string | "sora-2" | Model variant: "sora-2" or "sora-2-pro" |
| `size` | string | "1280x720" | Resolution: "1280x720" (landscape) or "720x1280" (portrait) |
| `seconds` | integer | 5 | Duration: 1-20 seconds |
| `input_reference` | string/URL | null | Reference image or video for transformation |
| `n` | integer | 1 | Number of variants: 1 (1080p), 2 (720p), up to 4 (lower) |

### Resolution Options
| Size | Orientation | Best For |
|------|------------|----------|
| 1280×720 | Landscape | Standard cinematic output |
| 720×1280 | Portrait | Vertical/mobile content |

**Note:** Source reference images must match the target output resolution.

### Generation Constraints
| Constraint | Limit |
|-----------|-------|
| Max duration | 20 seconds per generation |
| Concurrent jobs | 2 (must wait for completion) |
| Max variants (1080p) | 1 per job |
| Max variants (720p) | 2 per job |
| Max consecutive actions | 3-4 steps |
| Frame rate | 24 FPS |

---

## Prompt Engineering Best Practices

### Do's
1. **Think like a director** — Structure every prompt as a shot brief: camera, subject, action, lighting, sound
2. **Front-load the first 500 characters** — Most critical visual elements go first. Camera framing, main subject, primary action.
3. **Use specific visual descriptions** — "Wet asphalt pavement, zebra crossing, neon signs reflected in puddles" beats "a beautiful street at night"
4. **Include camera grammar** — Lens type, movement, angle. "Steadicam following from behind, slight low angle, 35mm lens"
5. **Describe physics and materials** — "Rain droplets ripple in puddles; wind gently rustles the jacket's fabric"
6. **Add audio cues** — "Soft rain patter and distant city hum; footsteps splashing"
7. **Use exclusions sparingly** — "No text on signs; avoid lens flares" at the END of the prompt
8. **Specify 3-5 color anchors** — "Dominant colors: wet black, neon cyan, warm amber, cool steel blue"
9. **Keep action simple** — Max 3-4 consecutive logical steps per generation
10. **Use slow descriptors for motion** — "Slow dolly push-in" prevents blur artifacts

### Don'ts
1. **NEVER put duration in the prompt** — "Make this 10 seconds" is ignored. Use the `seconds` API parameter.
2. **Don't use vague adjectives** — "Beautiful," "epic," "cinematic" alone mean nothing. Qualify them with specifics.
3. **Don't request fast movement** — Causes blur. Use slow-motion descriptors.
4. **Don't include complex hand interactions** — Model struggles with fingers/objects. If needed, specify hand positions explicitly.
5. **Don't request transparent/glass objects** — Known rendering issues.
6. **Don't write long on-screen text** — Keep to 3-5 words max, single language.
7. **Don't bury key details after 500 characters** — They may be ignored (semantic drift).
8. **Don't mix languages** — Keep all text elements in one language.

### Model-Specific Tips

**Standard Sora 2:**
- Best for iteration: generate 3-5 variants per shot at 720p, then promote winners to Pro
- Keep prompts under 1,500 characters for best adherence
- Use for testing motion, timing, and composition before committing budget to Pro

**Sora 2 Pro:**
- Supports MARS-LSP timestamped prompting for fine-grained scene control
- Can handle complex multi-beat narratives within a single generation
- 1080p output suitable for final production
- Worth the cost premium for hero shots and final deliverables

**Audio Direction Tips:**
- Sora 2 generates audio IN SYNC with visuals — always include audio cues
- Ambient + SFX + dialogue can coexist: "Rain pattering on windows; distant thunder; she whispers 'not yet'"
- Music direction should be mood-based: "Low tension drone building" not "play Beethoven's 5th"

---

## Common Issues & Solutions

### Issue: Semantic drift — details in long prompts get ignored
**Solution:** Place the most critical visual instructions in the first 500 characters. Structure: Camera/framing → Subject/action → Lighting → Physics → Audio → Exclusions. If the prompt exceeds 1,500 characters, switch to Pro model.

### Issue: Motion blur on fast-moving subjects
**Solution:** Use slow-motion descriptors: "in slow motion," "quarter speed," "slow tracking shot." Avoid "running," "racing," "speeding" without slow-motion qualifiers. Alternatively, describe the aftermath: "she stops suddenly, hair still swinging forward."

### Issue: Hands look wrong when interacting with objects
**Solution:** Specify hand positions explicitly: "right hand grips the coffee mug handle, left hand rests on the table." Avoid complex manipulation sequences. When possible, frame the shot to avoid showing hands in detail.

### Issue: Face distortion on characters
**Solution:** Use front-facing or 45-degree angles. Avoid extreme angles or rapid head turns. Upload a reference image (Pro version) and describe key facial features: "short brown hair, round glasses, dimples when smiling."

### Issue: Glass/transparent objects render incorrectly
**Solution:** Avoid transparent objects as primary subjects. If glass must appear, make it a secondary element and describe its reflective properties rather than its transparency: "light catches the edge of the glass" rather than "a transparent glass."

### Issue: On-screen text is garbled
**Solution:** Keep text to 3-5 words maximum. Place text instruction early in the prompt. Single language only. Specify style: "bold white text reading 'CHAPTER ONE' appears center-frame."

### Issue: Physics feel wrong (objects teleporting, floating)
**Solution:** Describe physical rules explicitly, one interaction at a time: "The ball bounces off the wall and rolls to a stop" not "the ball bounces around the room hitting everything." Sora 2's physics are best when you guide them step by step.

---

## Advanced: MARS-LSP Timestamped Prompting (Pro Only)

For maximum control over multi-beat scenes, Sora 2 Pro supports time-stamped prompts:

```
[00:00] [CAMERA]: framing, motion, lens feel, texture
        [SUBJECT]: main focus or character action
        [DIALOGUE]: spoken line(s)
        [SND]: soundscape or musical tone
        [FX]: cinematic/visual effects
        [EDIT]: pacing, transitions
        [DIR]: mood, tone, directorial intent

[00:03] [CAMERA]: new framing or movement
        [SUBJECT]: next action beat
        ...
```

This format allows directors to choreograph precise timing within a single generation. Each timestamp block describes what happens at that moment in the video.

**When to use MARS-LSP:**
- Multi-beat action sequences with specific timing
- Dialogue scenes requiring precise sync points
- Camera movement changes mid-shot
- Tone/mood shifts within a single clip

**When NOT to use MARS-LSP:**
- Simple single-action shots (natural language is simpler and works great)
- Standard Sora 2 model (may not handle the complexity well — use Pro)

---

## Editing Tools (Post-Generation)

Sora 2 includes built-in editing capabilities accessible via sora.com:

| Tool | Function | Use Case |
|------|----------|----------|
| **Re-Cut** | Trim/extend clips; generates new frames forward or backward in time | Isolate best section, extend a moment |
| **Blend** | Merge two videos with a transition curve | Smooth transitions between shots |
| **Loop** | Create seamless repeating cycles (Short/Normal/Long) | Natural repetitive motion: waves, flames, breathing |
| **Storyboard** | Plan multi-shot sequences with timing | Narrative planning across multiple generations |
| **Remix** | Modify prompt of existing video for variations | Explore alternatives while keeping visual elements |

These tools are available in the sora.com interface but NOT via the API. For API workflows, iteration happens by regenerating with modified prompts.

---

## Continuity Workflows

### Sequential Prompt Technique (Character Consistency)
Without reference images, maintain character consistency through prompt discipline:

**Shot 1 — Establish:**
```
Wide shot, 35mm lens, eye level. A woman in her 30s with cropped silver hair, 
sharp cheekbones, wearing a long black wool coat, stands at a rain-soaked 
intersection at dusk. She holds a folded newspaper. Neon signs reflect in puddles. 
Cool blue-green palette with warm amber streetlights. Rain patters on pavement, 
distant traffic hum.
```

**Shot 2 — Reference back:**
```
Medium close-up, 50mm lens. Same woman with cropped silver hair, sharp cheekbones, 
black wool coat — from the previous scene — now inside a dimly lit bar. She unfolds 
the newspaper on the counter. Warm amber bar lighting, single overhead fixture. 
Glasses clink softly, low murmur of conversation, jazz playing faintly.
```

**Shot 3 — Progress narrative:**
```
Close-up, 85mm lens, shallow depth of field. Same woman with cropped silver hair — 
her eyes scan a circled name in the newspaper. A slight tightening of her jaw. 
Warm amber key light from the left, the rest of her face in shadow. 
Paper rustling, her breathing barely audible.
```

### Image-to-Video Workflow
1. Generate a still image (via Flux 2, Seedream, or DALL-E 3) as your anchor frame
2. Upload as `input_reference` to Sora 2
3. Describe ONLY the desired motion — do NOT re-describe the image
4. Example: "Subject slowly turns her head toward camera, a gentle smile forming. Soft wind moves her hair. Rain begins to fall."

### Production Iteration Workflow
1. **Pre-Production:** Script beat sheet, create storyboards, define style spine
2. **Low-Res Exploration:** Generate 3-5 variants at 720p (Standard) per shot
3. **Refinement:** Tweak prompts, test timing, log what works
4. **Final Render:** Promote winning concepts to Pro at 1080p
5. **Post-Processing:** Edit in Premiere/DaVinci for stabilization, color grading, final audio mix

## Reference Files

Load these when you need depth on a specific topic:

- [schema.json](schema.json) — Output validation schema for the Sora 2 prompt object: required `prompt` and `model`, plus the Standard vs. Pro constraints.
- [examples.json](examples.json) — Six annotated input/output pairs: establishing shot with physics (Standard), character introduction with audio (Pro), synced dialogue scene (Pro), b-roll materials insert (Standard), image-to-video still animation (Standard), and a MARS-LSP timestamped multi-beat action sequence (Pro).

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
