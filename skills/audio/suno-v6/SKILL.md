---
name: suno-v6-prompts
description: Generate optimized Style, Lyrics and Exclude fields plus settings for Suno v6 music generation (v6, v6-wild, v6-mini). Use whenever a user mentions Suno, Suno v6, v6-wild, v6-mini, suno.com, or wants AI-generated songs, instrumentals, soundtrack cues, jingles, duets, covers, remasters, extends, Replace Section edits, mashups, music from an image or video, Voices / Custom Model consistency, or stems. Also use when migrating v4/v4.5/v5/v5.5 tag-cloud prompts to v6, since all pre-v6 models are retired and v6 reads producer-brief sentences, a Variety slider and Max Mode. Covers Simple-mode briefs, Custom-mode Style + Lyrics with [section] meta tags, duet labelling, and multi-song continuity. Do not guess Suno syntax from general knowledge or older-version metatag recipes.
---

# Suno v6 — Prompt Generation Skill

Suno v6 is a family of music models (`v6`, `v6-wild`, `v6-mini`) that turn text, lyrics, audio, songs, images and video into full songs up to 8 minutes. It is audio only — no visuals, no camera, no aspect ratio. Every generation returns **two** takes.

## The Three Rules That Override Everything

1. **Write a producer brief, not a tag cloud.** Tell the musicians and engineer what to do: who plays what, how the song grows, what sits forward in the mix. "Palm-muted guitar drives the verses" beats "electric guitar, energetic".
2. **Positives in Style, negatives in Exclude.** Never write "no saxophone" in Style — the word itself pulls sax in. Put `saxophone` in the Exclude field.
3. **Style is the global map; Lyrics tags are local cues — they must agree.** A `[massive EDM drop]` tag inside a "restrained acoustic ballad" Style gets thinned or ignored. Keep section cues short and consistent with Style.

## Where Things Go (why "settings" appear in text)

Suno has **no fields for BPM, key, duration or structure**. Those are written into the Style text (BPM, key, groove, target length) and the Lyrics (section tags) — that is genuine Suno syntax, not a format leak. True UI settings — model, Variety, Weirdness, Style Influence, Audio Influence, Max Mode, Instrumental, Vocal Gender, references — go only on the Suggested settings line.

## Style Field Order — IDENTITY → PULSE → PLAYERS → PERFORMANCE → ARC → MIX → ENDING

| # | Layer | Example |
|---|---|---|
| 1 | Identity | "Nocturnal 1980s synthwave, lonely and reflective" |
| 2 | Pulse | "108 BPM, steady four-on-the-floor, laid-back pocket" |
| 3 | Players | "Gated drums; pulsing octave bass; glassy arpeggio hook" |
| 4 | Performance (voice) | "Low detached baritone, close and dry, opens up on chorus" |
| 5 | Arc | "Sparse intro, bass enters verse 2, wide final chorus" |
| 6 | Mix | "Vocal forward and dry; synths wide but under the voice" |
| 7 | Ending | "Four-bar resolved ending, no fade" |

```
[GENRE/SUBGENRE, ERA, MOOD]. [BPM + GROOVE]. [VOCALIST + DELIVERY].
[DRUMS ROLE]. [BASS ROLE]. [LEAD/SUPPORT ROLES]. [SECTION-BY-SECTION ARC].
[2–3 MIX RELATIONSHIPS]. [ENDING BEHAVIOUR].
```

**Length:** Style field limit ~1,000 characters (counter in the live composer); aim for **300–700**. Lyrics ~5,000 characters. One dominant genre plus at most one or two influences.

## Decide the Surface / Operation First

| User wants | Surface / tool | Prompt pattern |
|---|---|---|
| Quick idea, conversational, multi-reference | Simple mode | 1–4 sentence brief; give each reference one role |
| Full control of song + words | Custom mode | Style + Lyrics + Exclude + Title |
| Instrumental / score cue | Custom + Instrumental on | Style carries the arc; Lyrics empty or section tags only |
| Longer / new ending | Extend (then Get Whole Song) | Restate groove, singer, destination + transition cue |
| Fix one lyric or passage | Replace Section / plain-language edit | "Replace only X. Keep Y unchanged." |
| Polish, same performance | Remaster (Subtle / Normal / High) | No new prompt needed |
| New singer/genre, same song | Cover | New Style; keep lyrics |
| Combine songs / sample / isolate | Simple mode, v6 | "Vocals from Song A, drums from Song B…" |
| Recurring singer or catalog sound | Voices / Custom Model | See continuity reference |
| Separate parts for a DAW | Get Stems | Generate with clear arrangement first |

## Quick Syntax Reference

- **Section tags:** own line, square brackets — `[Intro] [Verse 1] [Pre-Chorus] [Chorus] [Bridge] [Instrumental Break] [Final Chorus] [Outro] [End]`.
- **Composite section cues:** `[Chorus - full-band lift, stacked harmonies]` — v6 reads these as performance direction. Section level only; never one per line.
- **Backing vocals / ad-libs:** parentheses — `(toward the morning)`. Sparingly.
- **Duets:** define `Singer A` / `Singer B` once in Style; label sections `[Verse 2 - Singer B]`. Keep names out of lyric lines.
- **Exclude:** comma-separated nouns — `trap hi-hats, spoken intro, crowd noise, abrupt ending`.
- **Artists:** describe properties (era, register, harmony, production), not "in the style of [artist]".

Tags, BPM, bar counts and keys are strong guidance, not a formal grammar. Full rules → [best-practices.md](best-practices.md).

## Output Format (always two parts)

1. **Prompt fields** — each in its own code block, labelled: **Style**, **Lyrics** (with section tags), **Exclude** (if any), **Title**. Simple-mode requests get one **Brief** block instead.
2. **Suggested settings** — one line, e.g.
   `model: v6 · Instrumental: off · Variety: 0 · Weirdness: 30% · Style Influence: high · Max Mode: on (>2 min) · refs: none`

## Things That Will Break the Request

- Negatives written in Style ("no drums") — they get added.
- Per-line bracket tags or long bracket paragraphs — instructions get **sung** or phrasing destabilises.
- Six genres at once, contradictory Style vs section tags — v6 averages or drops one.
- Variety above 0 when testing a precise brief — it rewrites your style text.
- `Singer A:` inside lyric lines — may be sung literally.
- Expecting a seed, exact sample-accurate BPM/bar counts or frame-accurate timing — none exist; fix in Studio/DAW.
- Choosing v6 / v6-wild on a free plan — only v6-mini is available.
- Pre-v6 model names (v4.5, v5, v5.5) — retired for new generations.

## Iteration Workflow

1. Sketch directions on `v6-mini` (or `v6-wild` for genre collisions), Variety 0 so you're testing the words.
2. Move the winning brief to `v6`; change **one** control per run and compare both takes.
3. Lock structure and lyrics; turn on Max Mode for songs over 2 minutes or close covers.
4. Repair locally — Replace Section, lyric edit, Extend, Remaster — never regenerate a mostly-good song.
5. Log the recipe (model, fields, Exclude, sliders, Max Mode, refs, chosen take). Reuse Prompt repopulates fields but does not reproduce the audio.
6. Export WAV / stems for finishing.

## Reference Files

- **[parameters.md](parameters.md)** — models and plan access, every slider and toggle, Max Mode, durations, uploads, credits, stems, downloads, recommended combinations, v5.5 → v6 migration.
- **[best-practices.md](best-practices.md)** — producer-brief craft, instrument roles, arc, mix language, lyric writing, tag/parentheses/duet rules, Exclude, common-mistakes table.
- **[continuity-and-references.md](continuity-and-references.md)** — music bible, Voices, Custom Models, reference role assignment, Extend/Replace/Cover/Remaster continuity, multi-cue scoring, stems.
- **[examples.md](examples.md)** — annotated Simple briefs and Custom Style/Lyrics/Exclude sets with settings.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
