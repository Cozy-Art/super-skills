---
name: pixverse-v6-prompts
description: Generate optimized prompts for PixVerse V6 — the March 2026 production video generation model with 15-second 1080p single-pass generation, native multi-shot storytelling engine, integrated audio synthesis, and 20+ cinematic lens controls. Use this skill whenever a user mentions PixVerse V6, PixVerse video generation, or asks for prompts targeting pixverse.ai or WaveSpeed AI with PixVerse models. Also trigger for workflows involving the 5-part literal prompt formula, multi-image character reference for identity consistency, thinking_type toggle (enabled/disabled/auto), multi-shot structured sequences, lip-sync TTS or external audio upload, first/last frame interpolation, or video extension via source_video_id. Always use this skill — V6 requires literal observable physical descriptions (not creative metaphors), subject anchoring before action, maximum 2 camera moves per shot, and explicit negative prompts to prevent common artifacts.
---

# PixVerse V6 Prompt Generator

Generate optimized prompts for PixVerse V6 — a production video platform with native multi-shot engine, integrated audio, and 20+ cinematic lens controls. Released March 30, 2026.

## The Master Principle

**Literal physical description beats creative abstraction.**

V6's reasoning engine performs better with observable, concrete visual instructions than with abstract stylistic language.

| ❌ Creative (avoid) | ✅ Literal (use) |
|--------------------|-----------------|
| "A magical and energetic forest scene with dramatic lighting" | "Wide tracking shot through pine trees, morning side light, a fox walking steadily from left to right, leaves rustling" |
| "Beautiful cinematic car shot" | "A silver car driving on a dry road. The sun shines on the car roof. The camera follows from behind." |
| "Dramatic, epic, stunning" | Specific physical actions: "low-angle tracking, handheld shake, sparks from metal joints" |

**Official V6 example from PixVerse documentation:**
```
A silver car driving on a dry road. The sun shines on the car roof.
The camera follows the car from behind.
```

## The 5-Part Prompt Formula

Every effective V6 prompt follows this structure:

```
[Subject] → [Action/Motion] → [Environment] → [Camera] → [Style]
```

| Block | What to include | ✅ Good | ❌ Bad |
|-------|----------------|---------|--------|
| **Subject** | Age, clothing, expression, physical details | "Mid-40s woman, black blazer, confident expression" | "A woman" |
| **Action** | One motion verb + pace qualifier | "Walking slowly toward the camera, natural stride" | "Moving" |
| **Environment** | Location, depth, spatial context | "Modern lobby, glass walls, marble floor, afternoon sun" | "Office" |
| **Camera** | Shot size + movement (max 2) | "Medium tracking from chest height, slight upward tilt" | "Normal view" |
| **Style** | Aesthetic, color grade, quality | "Corporate commercial, cool neutral tones, sharp focus" | "Looks good" |

## Hard Rules

**1. Subject anchors first.** Early tokens receive disproportionate model weight — describe the subject before any action or environment.

**2. One primary action per clip.** Multiple competing movements cause choppy, incoherent results.

**3. Maximum 2 camera moves per shot.** V6 reliably handles 1–2; a third move is commonly ignored in testing.

**4. Always use pace qualifiers.** Without "slowly," "gently," "rapidly," or "steadily," V6 defaults to a medium pace that may not match intent.

**5. Negative prompts are supported and effective.** Always include: `"blurry, extra fingers, morphing, inconsistent lighting, duplicate limbs"` as a minimum.

**6. Multi-shot: repeat descriptors verbatim.** Same subject vocabulary, same environment vocabulary, same style vocabulary in every shot.

## thinking_type Strategy

| Value | When to use |
|-------|------------|
| `enabled` | Drafting — model rewrites and enhances your prompt; discovers effective phrasings |
| `disabled` | Production — generates exactly from your prompt; use once a prompt is tested |
| `auto` (default) | General use — model decides based on complexity |

**Workflow:** Use `enabled` to find what works → switch to `disabled` for reproducible finals.

## Audio Modes (Three, Mutually Exclusive)

| Mode | How to activate |
|------|----------------|
| AI-generated ambient + SFX | `generate_audio_switch: true` |
| TTS with scripted dialogue | `lip_sync_tts_speaker_id` + `lip_sync_tts_content` (≤200 chars) |
| External audio (MP3/WAV) | `audio_media_id` |

**Add audio last** — after the visual is finalized. Audio adds per-second cost.

## Draft → Production Pipeline

1. **Draft at 360p/540p** — validate composition, motion, character
2. **Test 2–4 seeds** — distinguish model variation from prompt ambiguity
3. **`thinking_type: enabled`** for drafts → `disabled` for finals
4. **One variable at a time:** camera → motion pace → lighting/style
5. **Production at 1080p** once prompt is locked
6. **Enable audio last** — add to final render only

## Reference Files

Load these when you need depth on a specific topic:

- **`parameters.md`** — Complete API parameter tables (V6 WaveSpeed schema and legacy platform schema), all 20+ V6 cinematic lens controls, aspect ratio options, pricing table by resolution and audio, legacy `camera_movement` enum values, `motion_mode` and `quality` constraints, and V5.6 → V6 migration comparison.

- **`best-practices.md`** — Literal method deep-dive with comparison table, subject anchoring rules, motion and camera discipline (pace qualifiers, max 2 moves, handheld vs. gimbal), style vocabulary, thinking_type strategy, motion strength slider guidance, negative prompt library, known V6 limitations (crowd faces, facial close-ups, text rendering), and content filter workarounds.

- **`continuity-and-references.md`** — Multi-image character reference workflow (upload angles, API schema), multi-shot engine operation (descriptor repetition rules, vocabulary consistency), transition prompting for manual chaining, first/last frame interpolation, LipSync/TTS modes (syntax, character limit, multilingual), and video extension workflow.

- **`examples.md`** — All 5 annotated example prompts: corporate headshot/walk, action/destruction, product commercial, anime character with Japanese dialogue/lip-sync, and multi-shot brand narrative. Includes quick-start templates by content type and a pre-generation checklist.
