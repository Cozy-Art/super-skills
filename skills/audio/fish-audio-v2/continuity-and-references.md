# Fish Audio — Continuity & Voice References

There is no seed, no session and no "previous generation ID" on `/v1/tts`. **Voice continuity is carried by the voice model (`reference_id`) plus a pinned request config.** Delivery continuity is carried by consistent direction language. Everything else is editorial.

## 1. Housekeeping That Makes Continuity Possible

- Store, per approved file: script text, `model` header, `reference_id`(s), full JSON body, output format/rate, take number.
- Name files `scene_speaker_take_configver.wav`.
- Keep a `voices/` folder: source recordings, transcripts, model IDs, master reference clips.
- Pin every parameter explicitly — raw API, SDK and streaming surfaces have different defaults (`chunk_length` 300 vs 200, `latency` normal vs balanced).

## 2. Voice References: Stored Model vs Inline

| | Stored voice model (`reference_id`) | Inline zero-shot (`references`) |
|---|---|---|
| Created by | `POST /model` (or web app) | Sent with every request |
| Transport | JSON fine | **MessagePack only**; each item `{audio, text}` |
| Quality / latency | Better quality, lower latency (Fish's recommendation) | Extra transfer each call |
| Continuity | Identical identity every call | Different clips → identity shifts |
| Use for | Any series, character, brand voice | Quick tests, one-offs |

**Rule:** anything that will be heard twice gets a stored model.

## 3. Recording a Clean Reference

Fish's guidance:
- At least **10 seconds**; ideal **2–3 clips of 15–20 s** that form a complete paragraph. If the clone sounds robotic, record **30–60 s**.
- Quiet room, mic about a hand's width from the mouth, steady volume, ~0.5 s pauses between sentences.
- One speaker only. No music, TV, traffic, AC, fans, fridges. No big swings in volume or emotion inside a clip.
- Formats: WAV, MP3, FLAC. Up to 20 files per model; supply `texts` transcripts (else ASR is run). `enhance_audio_quality` defaults to `true`.

Practical additions:
- The reference's performance biases output. A whispered-only reference makes energetic narration hard — record the voice at its **baseline** register.
- Need distinct styles (calm narrator vs. hype promo) from the same person? Fish suggests recording the same text in different tones — create **separate models per style** rather than one muddled model.
- Only clone voices you have the rights and consent to use.

## 4. Designed Voices (no recording)

1. `POST /v1/voice-design` with `instruction` (voice, age, tone, accent, pacing, context) and a short `reference_text` so every candidate reads the same line. `n` = 2–4.
2. Audition; regenerate with sharper wording or a fixed `seed` to compare variations.
3. Promote the winner to a persistent voice: create a model from the candidate audio (optionally with `voice_design_signatures`, which tags the model `source=voice_design`).
4. From then on, treat it exactly like a cloned voice — reuse the `_id`.

## 5. The Voice Bible (one per character / brand voice)

```
VOICE: Captain Ilse Var — model 7f3c…  (s2.1-pro)
Baseline: low, measured, dryly amused, rarely raises her voice.
Range: calm → controlled anger. Never shouts; anger goes quieter.
Pace: prosody.speed 0.95 · temperature 0.6 · top_p 0.7 · latency normal · chunk 300
Pronunciation: dict "ilse-var-v2" — Ilse = ILL-suh, Valtoria = val-TOR-ee-uh
Master clips: voices/ilse/master_calm.wav, master_angry.wav
```

Paste the **baseline cue** verbatim at the start of each scene, e.g. `[low, measured, dryly amused]`, then change only what the beat needs. Never change both the reference voice and the direction language between scenes — if a scene sounds wrong, you won't know which caused it.

## 6. Consistency Across Takes and Sessions

1. Same `model` header for the whole project (don't mix `s2.1-pro` and `drama-3` within one character's scene unless deliberately A/B testing).
2. Same `reference_id`.
3. Same `temperature`, `top_p`, `prosody`, `latency`, `chunk_length`, `format`, `sample_rate`.
4. Same direction vocabulary for recurring states.
5. Same spelling, punctuation and number formatting for recurring lines.
6. Lower `temperature` (0.4–0.55) for anything that must match across sessions; expressive settings trade consistency for range.
7. Takes are not reproducible — **keep the file**, not just the request.

## 7. Long-Form (audiobook, documentary, course)

- Split at scene/paragraph/semantic boundaries, not arbitrary character counts. Keep each request comfortably sized (≤ ~3,000 chars is portable across wrappers; the web app counter is 30,000 — confirm your platform's cap).
- `latency: normal`, `chunk_length: 250–300`, `condition_on_previous_chunks: true` — Fish conditions each internal chunk on the previous audio.
- Repeat the narrator's baseline cue at the top of every request so each segment starts in the same register.
- Loudness-match and master the assembled sequence; `normalize_loudness` helps but isn't mastering.

## 8. Pickups and Fixes

- Re-render the bad line **with one sentence before and after** for context, then cut at a breath or pause.
- Keep the original config; only change the line's cue or wording.
- Mispronunciation → dictionary entry or phoneme tag, not repeated rerolls.
- Identity wobble on one line → drop `temperature` for that line only, then crossfade.

## 9. Multi-Speaker Casting

- Fix a **cast order** and never reorder it: `reference_id: ["narrator", "captain", "engineer"]` → speakers 0, 1, 2 in every scene.
- Zero-shot multi-speaker: `references` becomes a 2-D array, one inner array per speaker, aligned with the `reference_id` index.
- For tight edit control (separate stems per character, alternate takes per line), render speakers separately with the same voice IDs instead of one dialogue pass.
- Drama 3 handles larger casts in one text (third-party reports cite up to 16 — unverified, confirm on your platform).

## 10. Streaming Continuity (agents)

- One voice model per agent persona; never swap mid-session.
- `latency: balanced` (~300 ms TTFA), send complete words with spaces, buffer 5–10 words before sending, buffer 2–3 audio chunks before playback, keep chunk sizes consistent.
- Fix sampling low (0.3–0.45) so the agent sounds the same on turn 1 and turn 100.

## 11. Handoff to Video / Edit

Fish produces dry mono speech. Sync to picture at the edit layer: shared shot IDs and script line IDs, timestamped streaming endpoints when word alignment matters (lip-sync, captions). Ambience, Foley, music, reverb, panning and distance are added in the DAW. For audio-driven video/lip-sync models, feed the approved WAV, not a re-render.
