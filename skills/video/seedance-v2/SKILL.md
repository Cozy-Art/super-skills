---
name: seedance-2-0-prompts
description: Generate optimized prompts for ByteDance's Seedance 2.0 video generation model — a unified multimodal system producing cinematic video with native synchronized audio (dialogue, lip-sync, sound effects, ambient, music), native multi-shot scene cuts within a single generation, and three input modes: text-to-video, image-to-video (with first/last frame control), and reference-to-video (up to 9 images, 3 video clips and 3 audio clips in one generation, also used for video editing and extension). Use this skill whenever a user mentions Seedance, Seedance 2.0, ByteDance video generation, or wants a prompt for T2V, I2V or R2V workflows on this model. Always use this skill instead of guessing at Seedance's prompt structure — its six-block sentence formula, reference-token syntax (@Image1/@Video1/@Audio1), native scene-cut phrasing, and the rule against embedding format parameters in prompt text are model-specific and not obvious.
---

# Seedance 2.0 Prompt Generator

Generate optimized prompts for ByteDance's Seedance 2.0 — a unified multimodal video model that takes text, image, video, and audio inputs and produces a single cinematic clip with natively synchronized sound. No post-production audio layering: the model generates picture and sound together, in one pass.

**This skill produces prompt text, not API calls.** The output is handed to a person, who pastes it into whatever tool they're actually generating with — a playground, a console, a third-party UI. Every generated result should therefore ship as two clearly separated pieces: the **prompt** (natural-language text, ready to paste into the prompt field) and a short **suggested settings** line (resolution, duration, aspect ratio, audio) for whatever dropdowns or sliders sit next to that field. Never merge the two.

## The One Rule That Overrides Everything

**Settings do not belong in the prompt text.** "16:9," "1080p," "10 seconds," "4K," "vertical" — none of it goes in the sentence. Seedance's own guidance is explicit about this, and it's easy to violate out of habit if you're used to models where stuffing `--ar 16:9` or "4K, 16:9" into the prompt is normal. On Seedance 2.0, format words in the text just burn budget that should go to subject, action, camera, light, and sound — and they don't reliably override the actual settings control anyway.

Every word in the prompt should describe what happens on screen or on the soundtrack. Nothing else.

## Six-Block Prompt Formula

Seedance 2.0's own prompt guide recommends 2–3 concise sentences covering six blocks, in this order:

| Block | Covers | Example fragment |
|---|---|---|
| 1. Subject | Who/what is in frame — age, clothing, number of subjects | "A woman in her thirties with short black hair and a grey wool coat" |
| 2. Action / Motion | One clear primary action — not a chain of actions | "walks toward the camera and smiles" |
| 3. Camera | Movement + framing — the single biggest quality lever | "medium slow dolly-in shot" |
| 4. Setting & Lighting | Concrete place + specific light quality | "soft overcast daylight on a city sidewalk" |
| 5. Style | One visual treatment, not a stack of adjectives | "clean documentary style" |
| 6. Audio | Ambient, effects, music, or dialogue | "quiet street ambience, footsteps, distant traffic" |

Blocks 1–3 tend to read as one sentence, 4–5 as a second, and 6 as a third. That's the sweet spot — long adjective-heavy paragraphs consistently underperform a tight three-sentence version.

## Syntax Rules (Hard)

- ✅ Plain natural-language sentences — English or Chinese; English with concrete cinematography terms is the most predictable
- ✅ Dialogue in double quotes — this is what triggers lip-sync and voice generation: `she says, "Your one-line hook," calm and confident`
- ✅ Native scene cuts written directly into the text: `"...Cut scene to the octopus football game under the sea."` — Seedance 2.0 can render multiple shots inside one generation without a separate multi-shot mode
- ✅ Reference tokens in Reference-to-Video: `@Image1`, `@Video1`, `@Audio1` (see below)
- ✅ One primary action per clip — split additional beats into separate prompts or into a scene-cut
- ❌ Format words in the text: aspect ratio, resolution, duration, "4K" — these are settings, not prompt content
- ❌ Adjective soup: "epic, hyperrealistic, 8K, masterpiece" — replace with a specific camera move, light quality, or setting detail
- ❌ Long negation lists: "no blur, no distortion, no extra fingers" tends to backfire — describe what you want instead
- ❌ Omitting the camera entirely — even a minimal instruction ("static locked shot") beats no instruction; clips read as flat without one
- ❌ Chaining unrelated actions in one clause: "walks in, sits, opens laptop, starts typing" — pick the one beat that matters, or cut to the next

## Mode Selection

| Mode | Use when | Requires |
|---|---|---|
| **Text-to-Video** | Fully imagined scene, no existing visual asset | Prompt only |
| **Image-to-Video** | You need to preserve an exact look — product shot, hero frame, photo brought to life | Prompt + 1 image (first frame). Add a 2nd image to pin the last frame too |
| **Reference-to-Video** | Character/style/camera continuity across clips, multimodal combination, video editing, or video extension | Prompt + up to 9 images / 3 videos / 3 audio clips (any combination, total ≤ 12 files) |

## Quick-Start Templates

### T2V — Simple (3-sentence formula)
```
[Subject]. [Camera + framing], [setting + lighting]. [Style], [audio].
```
**Example:**
```
A woman in her thirties with short black hair and a grey wool coat walks
toward the camera and smiles. Medium slow dolly-in shot, soft overcast
daylight on a city sidewalk. Clean documentary style, quiet street
ambience with footsteps and distant traffic.
```

### T2V — Dialogue / Lip-Sync
```
[Subject + setting]. [Subject] [action], and speaks — [dialogue tag]:
"[exact line]," [delivery description]. [Camera]. [Ambient audio].
```
Dialogue must be in double quotes. Add a delivery note (tone, pace) — it steers the voice performance, not just the words.

### I2V — Motion Only
```
[Motion description]. [Camera cue]. [Audio].
```
The uploaded image is already the first frame — never redescribe it. Only describe what changes: motion, camera, light shift, sound.

### R2V — Reference-Driven
```
@Image1 [role it plays]. [Subject/action beat]. [Camera]. [Audio].
```
**Example:**
```
@Image1 shows a product on a marble surface. Slow dolly-in with dramatic
side lighting, dust particles floating in the air. Subtle ambient room
tone, soft click as the camera settles.
```

### Video Edit (change an existing clip)
```
Recreate the scene from @Video1 but [the one change]. Keep [invariant A]
and [invariant B] exactly as they were.
```
**Example:**
```
Recreate the scene from @Video1 but replace the background with the
environment from @Image1. Keep the subject's motion and camera movement
unchanged.
```

### Video Extension (continue a clip)
```
Continue directly from @Video1: [what happens next]. Maintain the same
character, environment, and style throughout.
```

### Native Multi-Shot (scene cuts, one generation)
```
[Shot 1 description]. Cut scene to [shot 2 description].
```
No separate multi-shot parameter — the cut lives in the prose. Keep each shot to one clear beat; two to three shots is a realistic ceiling within the duration cap.

## Reference Tokens (Reference-to-Video)

Default to `@Image1`, `@Video1`, `@Audio1` — this is what shows up in ByteDance's own example calls and the official fal.ai repo. Some documentation and third-party tools instead show bracket style (`[Image1]`, `[Video1]`, `[Audio1]`) — the docs aren't fully consistent with each other on this point. If the director reports a tool isn't picking up the reference, suggest trying the bracket form, or fall back to plain-language reference ("the character from the first reference image") as a universal option that works regardless of tool.

## Suggested Settings

Pair every prompt with a short settings line. Typical range across tools (see `parameters.md` for the full table and provider variation):

- **Resolution:** 480p or 720p baseline; some tools expose 1080p or higher — take it if offered, it doesn't change the prompt
- **Duration:** `auto` (model decides) or 4–15 seconds; a few tools advertise longer
- **Aspect ratio:** `auto`, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16
- **Audio:** on by default — leave it on unless the director specifically wants a silent draft. Unlike some models, turning audio off doesn't reliably save cost on Seedance 2.0, so there's little reason to disable it

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Full settings reference across providers (fal.ai baseline plus BytePlus/Volcano Engine and reseller variants), resolution × aspect-ratio pixel tables, endpoint names for context, and where the documented ceilings genuinely disagree.

- **`best-practices.md`** — Deep guidance on the six-block formula, camera language, lighting/style vocabulary, dialogue and lip-sync mechanics, what to avoid with a mistakes/fixes table, and the iterative refinement workflow (generate 2–3 variants, adjust one block at a time).

- **`continuity-and-references.md`** — Character and style consistency across generations, how to chain clips with Reference-to-Video, the video-editing and video-extension patterns in depth, and how this maps onto a Continuity-Anchor–style production workflow.

- **`examples.md`** — Seven annotated example prompts: simple T2V character shot, dialogue/lip-sync scene, environment/b-roll, product I2V, vertical social ad, reference-to-video continuity, and video editing/extension. Each includes the formula breakdown and technique notes.
