# Sonilo — Continuity & References

Sonilo has no seed (ComfyUI's seed widget is ignored), no "continue / extend this track", no audio-reference or melody-conditioning input, and `task_id` is a polling handle, not a creative reference. **Sonic continuity is carried by three things you control:** verbatim identity text, a locked picture timeline, and an archive of chosen outputs.

## 1. Housekeeping That Makes Continuity Possible

- Download every chosen result on success; don't plan on regenerating the same track.
- Keep a project library: `identity/` (text blocks), `cuts/` (source video versions + hash), `cues/` (chosen audio), `requests/` (JSON of every call).
- For each keeper record: endpoint, exact prompt(s), segments JSON, all params, source-cut hash/version, `task_id`, date, chosen variant index, license tier.

## 2. Sonic Identity Block

The audio equivalent of a style lock. Write it once, paste it **unchanged** into every prompt of a series, campaign or character:

```
SERIES IDENTITY: warm analog pulse, muted felt-piano four-note motif, brushed
percussion, restrained optimism, intimate mix, instrumental, no brass, no vocals.
```

Rules:
- Fix three things: **motif description**, **core instrument family**, **emotional vocabulary**.
- Vary only the episode-specific arc and intensity, appended after the block.
- Keep it short (≤35 words) so it still fits video-prompt length targets.
- For video-to-music, pair a consistent identity block with a consistent `prompt_influence` (e.g. 0.65) across episodes — changing influence changes how strongly the identity holds.

## 3. Character / Leitmotif Consistency

Sonilo can't receive a melody, so a "theme" is a described timbre-and-gesture, not notes:

```
THEME — MARA: solo felt piano, rising three-note figure, soft contrabass
underneath, patient and curious, slightly haunted.
```

1. Generate the theme once with text-to-music at `variants_num 3–4`; choose a **hero** take and archive it.
2. In later scenes, use the same THEME text inside the segment where the character dominates.
3. Expect family resemblance, not the same melody. If an exact recurring melody matters, cut the hero take into the edit yourself.

## 4. Multi-Shot / Multi-Scene Timelines

1. **Lock the cut** before generating. Retiming afterward breaks the conditioning.
2. **One request for the whole timeline** when it fits the endpoint cap (360 s music / 480 s SFX & sound). The model gets cross-shot context and resolves to a real ending.
3. **Broad scene segments**, not one per cut.
4. **Repeat identity terms** in adjacent segment prompts; change one dimension at each boundary.
5. **Over the cap?** Split at a natural musical break (scene change with a pause or hard cut), reuse the same identity block and influence, end part A on `"resolve to a quiet cadence"` and open part B with `"enter from near-silence"` so the join hides in the edit.
6. **Review against picture:** opening, first cut, emotional turn, reveal, last frame.

### Segment continuity template

```json
[
  {"start": 0,  "end": 12, "prompt": "intro: SERIES IDENTITY, sparse, piano motif alone"},
  {"start": 12, "end": 30, "prompt": "verse: same motif, add brushed percussion and pulse"},
  {"start": 30, "end": 45, "prompt": "chorus: motif returns fuller, add warm pad, peak energy"},
  {"start": 45, "end": 55, "prompt": "outro: strip back to piano motif, clean final cadence"}
]
```

## 5. Music + SFX Continuity

- **One synchronized deliverable:** prefer `video-to-sound` (`music_prompt` + `sfx_prompt` + shared `segments`) over separately chaining video-to-music and video-to-sfx.
- **Separate passes** (for independent mixing control): run both on the **same cut file**; keep music prompts free of Foley words and SFX prompts free of music words (`no music` in the SFX policy).
- **Ambience continuity across scenes:** an SFX policy line such as `continuous location ambience; keep room tone consistent within each scene` plus segments at location changes.

## 6. Voice / Speech Continuity

Sonilo doesn't generate voices; it **keeps** yours:
- `preserve_speech` — isolates dialogue from the source and keeps it over the new score.
- `keep_original_sound` (video-to-video-*) — keeps the entire source track (dialogue + ambience) as the voice layer.
- `ducking` — adds a dialogue-safe mix alongside the clean score.
- `audio-ducking` endpoint — post-hoc VO-over-music when both already exist.
Use the same choice across every episode so dialogue level and texture match.

## 7. Video & Image References

- Video endpoints need a real video stream (`video` upload or `video_url`). Audio-only, renamed audio or cover-art-only files are rejected (422).
- No still-image conditioning. For a single still, build a short hold or subtle motion clip in an editor and score that, or use text-to-music / text-to-SFX.
- AI-generated video works as input — score the final approved render, not a draft that will be re-rendered with different timing.

## 8. Iteration Without Seeds

- Generate 2–4 variants once and **select** rather than re-rolling a single take.
- Evaluate candidates against the full picture (and dialogue), not in isolation.
- To "fix" a take, change one variable (influence, one segment prompt, one exclusion) and generate fresh variants — treat each as a new roll.
- Final masters: re-run the winning request at `wav`, `variants_num 1`, or keep the winning WAV if it was already async/WAV.

## 9. Handoffs

| From | To | Pass along |
|---|---|---|
| `video-analysis` | video-to-music / sound | its brief → condense into a ≤35-word prompt + segment timings |
| text-to-music theme | video-to-music score | identical THEME / IDENTITY text |
| video-to-music | `audio-ducking` | chosen score + final VO |
| Any Sonilo audio | your NLE / DAW | WAV + segment timings as markers for frame-critical trims |
| Video model (any) | Sonilo | final locked render; re-score if the video is re-generated |
