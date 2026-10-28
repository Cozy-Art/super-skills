# kling-v4 — build notes

Human-facing build notes. Not loaded as part of the skill.

**Built:** 2026-10-19 · **Skill version:** 1.0 · **Model:** Kling 4.0 / 4.0 Flash (Kuaishou)

Built from the Kling 3.0 skill (`video/kling-v3`) as craft base plus a Kling 4 delta research document. Kling 3.x facts were re-checked rather than inherited; several did not survive (below).

---

## Research verification

Corrections:
- Asset limits attributed to "reviewed guide material" / "community testing" (10 images, 7 elements incl. 3 video, 3 voice profiles) → all confirmed first-party, with added per-file limits: images ≤ 30 MB, aspect 2:5–5:2; videos 3–30 s each, ≤ 30 s combined, ≤ 300 MB; video-element source footage 3–8 s; voice profiles 5–30 s audio, ≤ 50 MB — https://kling.ai/quickstart/kling-4-model-user-guide
- Reference tokens "in official educational material and community guides" → first-party: "Assets are automatically numbered in upload order, such as @Image1, @Image2, and @Video1"; `@Element1` also used; the guide shows both `@Image1` and `@Image 1` spellings — same URL
- Editing template "Edit @Video1. Change: … Timing: … Preserve: …" (research's own construction) → Kling's documented pattern is `Edit @Video1. [change]. Keep everything else unchanged.`, with the warning that "Reference @Video1" alone may be read as reference-based generation — same URL
- Negative prompting "unverified" → first-party policy: minimise negative instructions; "Only two types of negative instructions are truly necessary: no subtitles and no background music." This reverses the Kling 3.x base skill's "negative prompts are essential" — same URL
- Prompt structure "no mandatory schema; useful optional sections" → Kling publishes a four-part Omni Reference template (Asset Roles / Overall Settings / Sequence of Events with `0–X s` timecodes / Audio) — same URL
- Keyframes "up to 10" → confirmed, plus: positions anywhere on the timeline; Keyframes entry **does not accept reference assets**; aspect follows the first keyframe (21:9/16:9/1:1/9:16 without images, no Auto) — same URL
- Launch "dated October 15 by the official release history" → the first-party user guide is dated 14 Oct 2026; announcement (30 Sep) said early access from 28 Sep and "wider rollout coming in October"; open-to-all coverage dated 15–16 Oct. Release-history page is client-rendered and returned no text — https://kling.ai/blog/kling40-kling-visual-realism-creative-control-introducing-storytelling
- 10-bit HDR "positioning" → Kling marks it "coming soon" (announcement, upgrade table); one spec table lists it as new — conflicting first-party, treated as not live — https://kling.ai/blog/kling-4-ai-video-model
- Two-minute extension "future capability" → confirmed "coming soon" first-party — announcement URL above
- Audio "two-channel stereo" → confirmed; added the first-party language list (zh, en, ja, ko, es, pt, de, fr, hi; Sichuanese/Cantonese; Beijing/Northeastern/Taiwanese Mandarin accents; American/British/Indian English) — user guide URL
- Kling 3.0 baseline in the research ("3–15 s", "one video ≤ 15 s") → confirmed by Kling's own 4 vs 3 comparison, which also gives 3.0 audio as single-channel and 3.0 dynamic range 8-bit SDR — https://kling.ai/blog/kling-4-vs-3
- Base-skill (Kling 3.x) items not carried forward because nothing first-party documents them for 4.0: CFG scale 0–1, Normal/Fun/Spicy modes, face-adherence 42–100, `@Character says` lip-sync token, fixed 30 fps, H.264/H.265 MP4 output, long negative-prompt template, 3-minute extension.
- API "integration-specific" → at launch Kling's developer platform showed "Kling 4.0 API Coming Soon"; no model ID or schema published (creaa.ai tracker, 16 Oct, citing https://kling.ai/dev). fal early access documents duration 3–30 s, `generate_audio`, 720p/1080p, Flash 720p ≤ 20 s, and the same `@Image1 / @Video1 / @Element1` tokens — https://fal.ai/kling-4

Unverified (marked in the skill as "confirm on your platform" or conditional):
- 4K availability at launch (listed by Kling; fal and launch coverage list 720p/1080p only).
- 4.0 Flash limits (≤ 20 s, 720p) — fal only; Kling publishes no Flash spec table.
- Frame rate, container/codec, bitrate — not published for 4.0.
- Native audio in Keyframes mode — the Keyframes spec table has no audio row.
- How voice profiles bind to characters/elements (fal: "up to 3 elements can carry a voice"); no in-prompt voice token documented.
- Whether typed `@Image1` text binds identically to assets picked from the prompt-box picker.
- Editing clip minimum (Kling 3 s vs. fal 2 s), per-plan quotas, credit pricing.

---

Built & Maintained by Jason Cozy @ Visual Horizon Studio • MIT License • Please use responsibly
