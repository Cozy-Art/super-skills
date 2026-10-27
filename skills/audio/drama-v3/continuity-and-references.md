# Fish Audio Drama 3 — Continuity & Voice References

Drama 3 treats references, earlier takes and the next request as one text-and-audio conversation: the system turn holds instructions and voice references, the user turn holds text, the assistant turn holds audio. Continuity is strongest when the serving layer keeps that conversation; on a stateless endpoint it is carried by the **cast map, the references and a pinned config** — and by the accepted audio file itself.

## 1. The Cast Map (freeze it first)

```
CAST — "Signal" (Drama 3)
speaker 0 = MARA, lead investigator   → reference_id mara-v3
speaker 1 = SOL, station AI           → reference_id sol-v2
speaker 2 = CAPTAIN REYES             → reference_id reyes-v1
speaker 3 = NARRATOR                  → reference_id narr-v1
```

- One ID per character for the whole project, 0–15. Never reuse a number for someone else in the same continuity chain, even if that character is absent from a scene.
- Hosted Fish API: `reference_id` array position **is** the speaker number — pad absent characters or keep the array in cast order. Open runtimes: map each reference to its speaker explicitly; don't rely on upload order.
- ComfyUI: `@Voice1`… numbers follow the node's connected-voice slots (≤5). Keep a separate slot map and translate; never send `@Voice` labels anywhere else.
- Casts larger than 16 (or 5 in ComfyUI) → split by scene with the same map, or render minor roles separately.

## 2. References

Every inline reference needs the audio **and an exact transcript** — a wrong transcript degrades similarity, timing and intelligibility.

| | Stored voice (`reference_id`) | Inline reference (`references`) |
|---|---|---|
| Fish API | `POST /model` → `_id` | MessagePack `{audio, text}`; 2-D array for multi-speaker |
| Fish Speech | `POST /v1/references/add` (`id`, `audio`, `text`) | `{audio, text}` + speaker mapping |
| SGLang-Omni | — | `{audio_path, text}` |
| vLLM-Omni | — | `ref_audio` + `ref_text` |
| Use for | anything heard twice | tests, one-offs |

Recording a clean reference:
- One person, dry close-mic, no music, no overlapping speech, little room echo.
- Baseline register — a whispered-only clip makes energetic reads hard; Drama 3 is designed so laughter, crying and whispers are no longer "flattened by the reference", but the reference still biases timbre and placement.
- Two or three complementary clips beat one long contaminated recording; Drama 3 clones from multiple samples per voice. Each extra clip costs context and preprocessing.
- Fish's hosted cloning guidance: ≥10 s, ideally 2–3 clips of 15–20 s; up to 20 files per stored model.
- Only clone voices you own or have explicit permission to use. Local weights enforce nothing — the obligation is yours (the Community License bans cloning a real person without consent).

## 3. The Voice Bible (per character)

```
MARA — speaker 0 — mara-v3
Baseline brief: [low, precise, tired but never careless]
Range: dry humour → cold fury (anger goes quieter, never louder)
Events she uses: [short exhale through the nose] instead of laughs
Pronunciation: "Vereen" = <|phoneme_start|>V ER0 IY1 N<|phoneme_end|>
Settings: temperature 0.65 · top_p 0.7 · format wav
Master take: s01e02_sc14_take06.wav
```

Paste the baseline brief at her first line in every scene; change only what the beat needs. Never change the reference and the direction vocabulary at the same time — you won't know which caused a difference.

## 4. Long-Form and Chunk History

On Fish Speech the Drama 3 chunker splits long text at ~300 UTF-8 bytes (sentence → clause → space), keeps `<|…|>` tokens, paired tags and brackets whole, groups ≤3 speakers per chunk, **pins the first chunk** for the whole run and carries the latest chunk forward.

- Send a scene as **one** request and let it chunk. Splitting into unrelated calls throws away the pinned first chunk and generated history.
- Make the opening of a long request representative: the first chunk anchors every later one, so open with the principal voices at their baseline.
- Write sentence and clause punctuation where you would accept a cut.
- `single_chunk` (Fish Speech) renders in one pass — up to 2,048 frames ≈ 95 s with `max_new_tokens: 0`; total output is capped at 10,240 frames minus the prompt.
- Hosted API: keep `condition_on_previous_chunks: true` and `latency: normal`.
- Insert editorial checkpoints: approve scene by scene rather than rendering an hour blind.

## 5. Revision Chains (history-capable surfaces only)

Revision is a model-level capability: earlier takes stay in context **as audio**, and the next turn's note is read relative to them. A transcript alone does not recreate it.

1. Render take 1; accept it or not.
2. Next turn: same line, a **relative** note — `[sadder than the previous take, less theatrical; keep the breath before the last sentence]`.
3. Keep sampling equal or slightly lower than the accepted take to limit drift.
4. Chain further notes on top; each prior take stays in history (SGLang-Omni: append it to `previous_takes`).

| Surface | Revision |
|---|---|
| SGLang-Omni | `previous_takes` — editing as continuation (model card) |
| Fish API, vLLM-Omni, OpenRouter | Not exposed — re-take and choose |
| Fish Speech server, ComfyUI | Not documented — test before promising |

## 6. Infilling and Local Corrections

Drama 3 can replace a word or sentence inside existing speech while the surrounding audio stays natural. The model card's example changes `by noon` to `by five` with the earlier takes in context.

- On a history-capable surface: send the **full corrected line** plus a "change only X, keep everything else" note, with the accepted take(s) as history.
- Exact edit-region controls (prefix/suffix boundaries) are integration-specific; the public hosted endpoint has none. Fish's own editing interface has been reported as limited-access (unverified — confirm on your platform).
- Fallback anywhere: re-render the line with one sentence of context either side using the same cast, references and settings, then cut at a breath.

## 7. Consistency Across Takes and Sessions

1. Same surface, checkpoint revision and runtime revision for a character's whole arc.
2. Same cast map, references and reference transcripts.
3. Same `temperature`, `top_p` (and `seed` where the runtime has one), format, sample rate.
4. Same direction vocabulary and spelling for recurring states and names.
5. A seed is not continuity: it does not fix timbre and isn't reproducible across hardware, kernels or revisions. **The accepted audio is the continuity master.**
6. Regression-test the voice bible whenever Fish updates the preview model or your runtime.

## 8. Take Records

Store beside every accepted take:

```json
{"surface": "fish-api", "model": "drama-3", "runtime_revision": null,
 "cast_map": {"0": "MARA", "1": "SOL"}, "reference_ids": ["mara-v3", "sol-v2"],
 "temperature": 0.65, "top_p": 0.7, "script_file": "sc14.txt",
 "output": "sc14_take06.wav", "parent_take": "sc14_take04.wav", "accepted": true}
```

Keep WAV/PCM masters; transcode to MP3/Opus only for review copies.

## 9. Handoff to the Edit

Drama 3 delivers dry 44.1 kHz mono speech. One multi-speaker render is a single track — if the mix needs per-character stems or alternate takes per line, render characters separately with the same references and settings. Ambience, Foley, music, reverb, distance and panning are added in the DAW; for lip-sync models feed the approved WAV, never a re-render.
