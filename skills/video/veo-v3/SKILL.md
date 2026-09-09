---
name: veo-3-1-prompts
description: Generate optimized prompts for Google DeepMind Veo 3.1, a cinematic video model with native synchronized audio, strong camera control and support up to 4K. Use this skill whenever a user mentions Veo, Veo 3, or Veo 3.1, or wants prompts for text-to-video, image-to-video, first/last-frame interpolation or video extension on Vertex AI or the Gemini API. Also trigger for requests involving its five-part formula, quoted dialogue with lip-sync, or timestamp prompting within a single clip. Always use this skill instead of guessing at Veo prompt structure from general knowledge — Veo binds reference images through an API array with no in-prompt token at all, so any @Image-style pointer written into the prose is wrong.
---

# Veo 3.1 - Prompt Generation Skill

## Model Overview

Veo 3.1 is Google DeepMind's latest video generation model, released October 2025. It excels at cinematic video creation with native audio generation, improved character consistency, and support for resolutions up to 4K. The model specializes in camera-aware cinematography and natural audio-visual synchronization.

**API Model ID:** `veo-3.1-generate-preview` (standard) or `veo-3.1-fast-generate-preview` (faster)

---

You are a prompt engineer specializing in Veo 3.1, Google DeepMind's state-of-the-art video generation model. Your role is to craft cinematic prompts that leverage Veo's native audio generation, sophisticated camera controls, and multi-reference consistency features for professional video content.

**This skill produces prompt text, not API calls.** The output goes to a person, who pastes it into
whatever tool they are generating with. Every result ships as clearly separated pieces: the **prompt**
and a short **suggested settings** line for the controls beside it. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** Resolution, duration, aspect ratio, seed, "4K",
"vertical" — none of it goes in the sentence. They are API parameters with their own controls, and
words spent on them are words not spent on cinematography, subject, action, context and sound. Veo's
sweet spot is 100–180 words; there is no room to waste.

## There Is No Reference Token

The one thing most likely to be got wrong on this model. **Google documents no in-prompt token of any
kind** — not `@Image1`, not `<IMAGE_1>`, not a bare ordinal. References bind through the
`referenceImages[]` API array, and every first-party example simply **re-describes** the subject in
prose.

Writing `@Image1` into a Veo prompt either renders as literal text in the video or is silently
ignored. Describe the character; do not point at the image. See `continuity-and-references.md`.

### Core Principles

1. **The Five-Part Formula is mandatory** - Every prompt must include: Cinematography + Subject + Action + Context + Style & Ambiance
2. **Optimal length is 100-180 words (3-6 sentences)** - Longer prompts confuse the model
3. **Camera direction is essential** - Veo excels with specific cinematography language
4. **Audio is native, not optional** - Always specify dialogue, SFX, and ambient sound
5. **Design moments in progress, not complete stories** - Focus on ongoing action rather than story arcs

### The Five-Part Prompt Formula

```
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
```

**Cinematography:** Camera work, shot composition, lens effects
- Examples: "Medium tracking shot", "35mm lens", "gentle dolly-in", "crane shot ascending"

**Subject:** The "who" or "what" the video focuses on
- Examples: "A seasoned detective", "a miniature dragon", "an elderly craftsman"

**Action:** What the subject is doing (verbs and movements)
- Examples: "walks with calm deliberate steps", "extracts a data chip", "examines ancient scroll"

**Context:** Where and when—environment, time, weather
- Examples: "rain-slicked street in forgotten city", "sunlit workshop at dawn", "neon-lit alley"

**Style & Ambiance:** Lighting, tone, artistic style, color palette
- Examples: "film noir with deep shadows", "warm golden hour glow", "ethereal dreamlike quality"

### Audio Specifications

**Dialogue Format:**
```
A detective murmurs, "This must be it. The secret code."
```
- Use quotation marks
- Name the speaker
- Keep to 1-2 short lines per 8-second clip
- Frame shots to show the mouth clearly

**Sound Effects:**
```
SFX: thunder cracks in the distance
```

**Ambient Noise:**
```
Ambient noise: the quiet hum of a starship bridge
```

### Veo 3.1-Specific Capabilities

- **Native audio generation**: Dialogue, SFX, ambient sound with perfect lip-sync
- **Reference images**: Up to 3 images for character/style consistency
- **First/last frame control**: Interpolation between specific visual states
- **Video extension**: Extend previous videos by 7 seconds, up to 20 times (~148s total)
- **High resolution**: 720p, 1080p, and 4K support
- **Two aspect ratios**: 16:9 (landscape) and 9:16 (portrait)

### Common Pitfalls to Avoid

- Vague prompts without all five formula elements
- No camera direction = static, dull scenes
- Complex simultaneous actions (break into sequences)
- Dialogue longer than 1-2 short lines
- Ignoring reference images for consistency
- Complete story arcs instead of ongoing moments
- Multiple conflicting style instructions
- Using "no" or "don't" in prompts (use positive exclusions)

---

## Timestamp Prompting

For multi-shot sequences within 8 seconds:
```
[00:00-00:02] Medium shot. Detective at desk, examining evidence...
[00:02-00:04] Footsteps echo on wooden floor...
[00:04-00:06] Close-up on detective's face, realization dawning...
```

## Negative Prompts

Describe exclusions positively, without "no" or "don't":
- ❌ "no walls" or "don't show buildings"
- ✅ Add to negative_prompt parameter: "wall, frame, urban background, man-made structures"

Prefer solving it in the positive prompt. Google's guidance is that describing what should be there
beats listing what should not.

## Suggested Settings

Pair every prompt with a settings line. Never put these in the prompt text. Full table in
`parameters.md`.

- **Resolution:** `720p` · `1080p` · `4k` — and this decides the duration, see below
- **Duration:** `4` · `6` · `8` seconds. **4s and 6s exist only at 720p.** 1080p and 4K are 8s only,
  and attaching reference images forces 8s at any resolution
- **Aspect ratio:** `16:9` or `9:16`. Those are the only two
- **Audio:** leave `generateAudio` on — native sound is the reason to choose this model
- **Seed:** fix it whenever a shot belongs to a sequence
- **Extension:** 720p only, +7s per pass, up to 20 passes (~148s)

**Plan the sequence before the shot.** Anything over 8 seconds has to be built at 720p, because
extension is 720p-only. There is no path to a 4K minute.

---

## Reference Files

- `parameters.md` — Every documented parameter with its real enum and default, the resolution/duration
  coupling, extension limits and the two-day storage window, and what Google does not publish
- `continuity-and-references.md` — How identity actually binds on this model, why there is no in-prompt
  token, and the locked-description + same-references + fixed-seed workflow
- `best-practices.md` — The five-part formula in depth, cinematography vocabulary, audio techniques
- `examples.md` — 17 annotated prompts across character, environment, action, style, audio and the
  special techniques (first/last frame, timestamp prompting), plus quick-start templates

---

## Important Notes

**Output Specifications:**
- Format: MP4 with native audio
- Frame rate: 24 fps
- Durations: 4s, 6s, 8s base (extendable to ~148s)
- SynthID watermark: Mandatory on all outputs

**Generation Costs:**
- 720p: Fastest, lowest cost
- 1080p: Moderate latency, medium cost
- 4K: Highest latency and cost

**Platform:**
- Available via Google Cloud Vertex AI
- Gemini API integration
- Requires Google Cloud account

**Key Differences from Veo 3:**
- Richer native audio with perfect lip-sync
- Better prompt adherence for complex camera moves
- Improved character consistency across shots
- 1080p and 4K support (Veo 3 was 720p only)
- Enhanced motion realism and physics

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
