# Eleven v4 — Continuity & Voice Consistency

Eleven v4 has no image or waveform reference input in the text field. **Continuity is carried by four things:** the `voice_id` (and the audio it was cloned from), locked generation settings, pronunciation dictionaries, and request stitching between neighbouring clips. Describing the voice in the script is not a continuity tool.

## 1. The Production Manifest

Create one per project before the first render and never change it mid-sequence without re-rendering neighbours.

```
PROJECT: The Long Signal — S1
MODEL: eleven_v4            (final)   · eleven_v4 also for drafts — never mix models across adjacent clips
TRANSPORT: Text to Dialogue (batch)
OUTPUT: wav_48000            (drafts: mp3_44100_128)
NORMALIZATION: auto, critical copy pre-normalized
LANGUAGE: en
DICTIONARIES: long-signal-names v3
SEED POLICY: fixed per line for A/B tests only
VOICES:
  MARA    voice_id=…  PVC (v4 fine-tuned)  stability 0.45  similarity 0.75
  OKAFOR  voice_id=…  IVC                   stability 0.50  similarity 0.80
  NARR    voice_id=…  Library               stability 0.60  similarity 0.75
```

Log per take: script, voice ID, model, settings, format, seed, request ID, verdict.

## 2. Character Voice Bible

Kept **outside** the script — v4 has no hidden system-prompt layer, so anything in the text is spoken or performed.

```
MARA VENN
Baseline: measured, low, dry; hides fear with understatement
Pace: unhurried; speeds up only under real threat
Tested tags: [dry, understated] [quietly, controlled fear] [soft laugh]
Avoid: [shouting] (voice cracks), [giggle] (off-character)
Pronunciations: Venn /vɛn/, Asterion /æˈstɪəriən/
Escalation ladder: [controlled concern] → [voice tightening] → [urgent]
```

Rule: don't re-specify age, accent or timbre in tags unless the story changes them — the voice ID already carries identity, and contradicting it causes drift.

## 3. Voice Identity Assets

| Voice source | Consistency | Use |
|---|---|---|
| Professional Voice Clone (PVC) | Highest; fully supported on v4 | Lead characters, narrators, brand voices. Fine-tune for v4 in My Voices (plus button next to Eleven v4). |
| Instant Voice Clone (IVC) | High on v4, no training step | Prototypes, secondary characters |
| Voice Library | Stable, shared | Fast casting |
| Voice Design | Works, may be less performative on v4 | Exploration |

Cloning source audio (official guidance):
- Only the target voice — no music, noise, pops or room reflections.
- RMS around −23 to −18 dB, true peak below −3 dB.
- IVC: 1–2 minutes of consistent audio. PVC: at least 30 minutes, ideally 2+ hours.
- Consistent mic distance and tone; a **single speaking style** (avoid mixing whispering and shouting in training data while ElevenLabs evaluates varied datasets on v4).
- v4 reproduces source flaws as faithfully as identity — clean first.

`use_pvc_as_ivc: true` trades some PVC fidelity for lower latency and more expressiveness; pick one per character and keep it.

## 4. Request Stitching (clip-to-clip continuity)

Every generation returns a request ID. Feed it to neighbours so prosody, level and identity flow across the join.

**Linear narration:**
1. Split at scene / paragraph / emotional boundaries (≤ ~800 chars when quality matters).
2. Render segment 1 → store request ID `r1`.
3. Render segment 2 with `previous_request_ids: ["r1"]`.
4. Segment 3 with `previous_request_ids: ["r1", "r2"]` (dialogue: **closest clip last**, up to 3).

**Repairing a middle clip:**
```json
{
  "model_id": "eleven_v4",
  "text": "…corrected segment 5…",
  "previous_request_ids": ["r3", "r4"],
  "next_request_ids": ["r6"]
}
```
`next_request_ids`: **closest clip first**. Passing both sides is what makes a regenerated line sit naturally.

Rules:
- Same model on both sides of a join — stitching works best that way.
- If request IDs are sent, `previous_text` / `next_text` are ignored (TTS).
- `enable_logging: false` (zero retention) disables stitching.
- Without IDs, short context text helps: TTS `previous_text` / `next_text`; dialogue `previous_text` / `future_text` (≤100 chars each).
- Stitching doesn't replace post: loudness-match and crossfade joins.

## 5. Multi-Scene Continuity

Beat sheet per scene, kept outside the spoken text:

```
Scene 4 baseline: intimate, exhausted, low volume
MARA: measured; dry humour masks fear
OKAFOR: quicker; tension rises after his third line
Pronunciations: Asterion /æˈstɪəriən/
Out: unresolved, quieter rather than louder
```

Translate only the current beat into inline tags. Carry the scene's last request ID into the first render of the next scene if they cut together.

- Keep the **same voice per character** across every scene and episode; changing settings is as disruptive as changing the voice.
- Keep tag vocabulary consistent per character — use the bible's tested tags.
- Version pronunciation dictionaries; pin the version in the manifest so episode 9 says names like episode 1.
- When re-recording a series after a model change, re-render whole scenes, not single lines.

## 6. Dialogue Scenes

- `inputs` order = performance order; ≤10 unique voices, ≤2,000 chars per request.
- Split long scenes at beats; stitch the parts with request IDs.
- One `settings` object applies to the whole dialogue request — if two characters need very different Stability, render their lines in separate requests or accept a shared middle value.

## 7. Cross-Language Consistency

- Same language as the reference → reference accent preserved.
- Different language → v4 speaks fluently with a **native target accent** while keeping speaker identity.
- If the source accent must carry (e.g. a French character speaking English), try an accent tag `[strong French accent]` experimentally; otherwise keep an older model for that character.
- Set `language_code` for each localized render; approve every language with a native listener.

## 8. Real-Time Session Continuity (Turbo)

- One TTD WebSocket session = continuous prosodic context; keep it open across turns (send `keep_alive` within the 20 s timeout).
- `voice_settings` and dictionaries can only be set in the first message — lock them there.
- `eleven_v4_turbo` = one voice per socket. Multi-character live scenes: one socket per character (each with fixed settings), or `eleven_v4` on one socket with up to 10 voices at higher latency.
- Mark speaker boundaries with `new_turn: true`. Use PCM if you need exact per-turn audio boundaries.
- Agents: when transferring between agents, `preserve_voice_settings` keeps the voice/model/settings consistent.

## 9. Reproducibility Expectations

- `seed` (0–4,294,967,295) narrows variation for A/B tests; it doesn't guarantee identical audio.
- Higher Stability = more repeatable reads, at the cost of liveliness.
- Approved audio is the source of truth — save the file, don't plan to "re-roll the same take".
- Need an exact existing performance in another voice? Use Speech-to-Speech / Voice Changer, not a text prompt.
