# Kling 4.0 — Parameters

*Verified against kling.ai first-party pages — the Kling 4.0 Model User Guide (kling.ai/quickstart/kling-4-model-user-guide, dated 14 Oct 2026), "Inside Kling 4.0" (kling.ai/blog/kling-4-ai-video-model), the 4.0 announcement (kling.ai/blog/kling40-kling-visual-realism-creative-control-introducing-storytelling) and the 4.0 vs 3.0 comparison (kling.ai/blog/kling-4-vs-3) — plus fal's Kling 4 early-access page (fal.ai/kling-4), October 2026.*

**The interface is the source of truth.** Kling 4.0 shipped with several features labelled "coming soon" and a developer API that was not yet published at launch. Anything below marked *(unverified — confirm on your platform)* is from secondary sources or is rollout-dependent.

## Models

| Model | What it is | Status |
|---|---|---|
| **Kling 4.0** | Full model: Omni Reference, Keyframes, editing, stereo audio | Early access from late Sep 2026; opened to all users on the Kling web app mid-Oct 2026 |
| **Kling 4.0 Flash** | "Faster generation and greater cost efficiency" | Early access for Ultra Yearly subscribers from 28 Sep 2026; wider availability depends on plan |

Flash limits per fal: up to **20 s**, **720p only** *(unverified on kling.ai — confirm on your platform)*. Kling has not published a full Flash vs. full comparison.

## Entry Points

| Entry | Purpose | Accepts |
|---|---|---|
| **Omni Reference** (default) | Text-to-video, reference-guided generation, and video editing | text + images, videos, elements, voice profiles |
| **Keyframes** (Multiple Keyframes) | Timeline control with first, middle and last frames | text + up to 10 keyframe images. **Does not accept reference assets.** |

## Core Options

| Option | Omni Reference | Keyframes |
|---|---|---|
| Prompt | ≤ 8,000 tokens | ≤ 8,000 tokens |
| Duration | 3–30 s, 1 s increments, **default 10 s** | 3–30 s, 1 s increments, **default 10 s** |
| Aspect ratio | 21:9 · 16:9 · 1:1 · 9:16 · Auto — **default Auto** | Follows the first keyframe; without images 21:9 · 16:9 · 1:1 · 9:16 |
| Resolution | 720p · 1080p · 4K (see rollout) | 720p · 1080p · 4K (see rollout) |
| Multi-shot | On by default — the model splits shots and paces them | — |
| Audio | Two-channel stereo, native dialogue/ambience/effects/music | not stated for Keyframes *(unverified — confirm on your platform)* |

**Rollout status (Oct 2026):**
- **4K** — listed in Kling's spec tables, but launch coverage and fal list 720p/1080p only; treat as "if your plan/interface offers it".
- **10-bit HDR (1080p/4K)** — Kling's own pages say "coming soon" (one spec table lists it as new; the upgrade table and announcement say coming soon).
- **Extend up to 2 minutes** — "coming soon".
- **Developer API** — Kling's developer platform listed "Kling 4.0 API Coming Soon" at launch; no model ID or request schema published *(confirm on your platform)*. fal exposes a `generate_audio` per-request switch and 3–30 s duration in early access.

Not published by Kling for 4.0: frame rate, container/codec, bitrate, seed, CFG/guidance, motion strength, negative-prompt field, camera-control presets, per-plan quotas, credit pricing. Don't send or promise any of them.

## Omni Reference Limits

| Input | Limit |
|---|---|
| **All references combined** | **15 assets** across images, videos, elements and voice profiles (individual limits apply inside the 15) |
| Images | up to 10 · ≤ 30 MB each · aspect 2:5–5:2 · subject images, character turnarounds, image grids, storyboards, wireframes |
| Videos | up to 5 · 3–30 s each · **≤ 30 s combined** · ≤ 300 MB each |
| Elements (subjects) | up to 7, including up to 3 video elements · video-element source footage 3–8 s |
| Voice profiles | up to 3 per task · 5–30 s of audio each · ≤ 50 MB per file · can come from different assets |
| Editing | up to 5 input clips in one editing task, each 3–30 s (fal: 2–30 s) |

fal also states "up to 3 elements can carry a voice" *(unverified on kling.ai)*. Video references, edit sources and video elements all draw on the same 5-video / 30-second budget.

## Keyframes Limits

| Input | Limit |
|---|---|
| Keyframe images | up to 10 · ≤ 30 MB each · aspect 2:5–5:2 |
| Positions | first frame, last frame, first + last, and middle frames at any point on the timeline |
| References | none — keyframes only |

## Reference Token Syntax

Assets are numbered automatically in upload order: `@Image1`, `@Image2`, `@Video1`, `@Element1`. Kling's guide uses both `@Image1` and `@Image 1`; the no-space form is the one its spec text uses. Whether pasted text binds the same way as an asset chosen from the prompt box's picker is not documented *(confirm on your platform)*. Hosts may differ (fal documents the same `@Image1 / @Video1 / @Element1` form).

## Audio

- Two-channel stereo; lip-sync improved over 3.x.
- Languages: Chinese, English, Japanese, Korean, Spanish, Portuguese, German, French, Hindi. Chinese dialects: Sichuanese, Cantonese. Chinese accents: Beijing, Northeastern, Taiwanese Mandarin. English accents: American, British, Indian.
- Dialogue: quoted, written in the target language. Voice character: describe age, vocal tone, speaking speed, emotion — or supply a voice profile.

## Kling 3.0 → 4.0 (first-party comparison)

| | 3.0 | 4.0 |
|---|---|---|
| Duration | 3–15 s | 3–30 s |
| Multiple keyframes | not supported | up to 10 |
| Prompt | — | up to 8,000 tokens |
| Dynamic range | 8-bit SDR | 10-bit HDR at 1080p/4K (coming soon) |
| Aspect | — | adds 21:9 |
| Audio | single-channel; 5 languages | two-channel stereo; adds Portuguese, German, French, Hindi |
| References | 7 images/subjects without video, or 1 video (≤ 15 s) + 4 | 10 images + 7 subjects + 5 videos (30 s), 15 total |
| Editing | via 3.0 Omni workflows | integrated; up to 5 input clips |

## Recommended Starting Combinations

| Goal | Setup |
|---|---|
| Character performance | Omni Reference · 1 identity image (or element) + 1 location image · 8–12 s · 1080p |
| Product spot | Omni Reference · product stills + 1 camera/pacing video · 10–20 s · 1080p |
| Storyboard control | Keyframes · only the milestone frames you have approved |
| Ideation | 4.0 Flash if offered (else 720p) · short durations first |
| Revision | Omni Reference edit · the approved clip as `@Video1` + one scoped change |
| Ultrawide environment | Omni Reference · 21:9 · continuous camera move · 10–15 s |
