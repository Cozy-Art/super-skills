# Fish Audio — Annotated Examples

Every example is two-part: **script** (the `text` value — spoken words + inline cues) + **suggested settings**. API settings never appear in the script; the `model` is a header.

---

## 1. Warm Character Narration

```
[warm, reflective, speaking as if to one close friend] I used to think the lighthouse was warning ships away. [break] Now I understand. It was showing them how to come home.
```
**Settings:** `model: s2.1-pro · reference_id: <narrator> · temperature: 0.6 · top_p: 0.7 · speed: 0.92 · latency: normal · format: wav 44.1k`

**Technique:** one composite cue (emotion + relationship to listener) carries the whole passage; `[break]` and the period do the timing instead of extra adjectives.

---

## 2. Customer-Service Agent (streaming)

```
[calm, professional, and reassuring] I found the duplicate charge. You will [emphasis] not be billed twice. The pending transaction should disappear within three business days.
```
**Settings:** `model: s2.1-pro · reference_id: <agent> · temperature: 0.35 · top_p: 0.55 · latency: balanced · chunk_length: 120 · format: opus 48k`

**Technique:** low sampling for turn-to-turn consistency; one `[emphasis]` placed directly before the key word; numbers written as words to dodge normalization surprises.

---

## 3. Documentary Voiceover

```
[quietly awed, measured documentary delivery] At dawn, the salt flats hold the sky like a mirror. [long-break] For a few minutes there is no visible horizon; only light, water, and the distant movement of flamingos.
```
**Settings:** `model: s2.1-pro · reference_id: <narrator> · temperature: 0.55 · top_p: 0.65 · speed: 0.9 · latency: normal · chunk_length: 300 · format: wav 44.1k`

**Technique:** the model generates narration, not wind or birds — `[long-break]` leaves room for an ambience bed added in post. Semicolon keeps the second thought connected.

---

## 4. Action Beat

```
[breathless after running, speaking urgently] Maya, don't take the bridge! [gasping] The supports are moving. [shouting over the noise] Go through the tunnel, now!
```
**Settings:** `model: s2.1-pro · reference_id: <maya_partner> · temperature: 0.75 · top_p: 0.8 · speed: 1.12 · latency: normal · format: wav 44.1k` — render 3–4 takes.

**Technique:** a new cue at each change in delivery; a vocal sound (`[gasping]`) placed exactly where it happens. High-emotion lines vary more, so plan to pick from takes.

---

## 5. Multi-Speaker Scene (one render)

```
<|speaker:0|>[controlled anger] You knew the signal was artificial.
<|speaker:1|>[defensive, then faltering] I knew it repeated. That's not the same thing.
<|speaker:0|>[quietly, with disappointment] You changed our course anyway.
<|speaker:1|>[barely audible] Yes.
```
**Settings:** `model: s2.1-pro · reference_id: ["<captain>", "<scientist>"] · temperature: 0.65 · top_p: 0.75 · speed: 0.96 · latency: normal · format: wav 44.1k`

**Technique:** array order = speaker index; each turn has its own reaction cue. The captain's anger goes *quieter*, matching her voice bible.

---

## 6. Drama 3 — Scoped Tags for a Directed Performance

```
[barely holding it together, forcing a smile] I'm fine. Really. [shaky breath] You should go. <whisper>Go on without me.</whisper> <forceful>Don't</forceful> look back.
```
**Settings:** `model: drama-3 · reference_id: <sheila> · temperature: 0.7 · top_p: 0.75 · latency: normal · format: wav 44.1k` — render several takes.

**Technique:** bracket sets the whole line's subtext; scoped tags change only the wrapped words. Scoped `<…>` tags are Drama-3-only — on `s2.1-pro` rewrite as `[whispering]` before the phrase.

---

## 7. Drama 3 — Language Switch + Cross-Language Direction

```
[tired but polite, ordering at a café counter] Hi, could I get <french>un café crème et un croissant, s'il vous plaît</french>? Thanks.
```
**Settings:** `model: drama-3 · reference_id: <bilingual_voice> · temperature: 0.6 · top_p: 0.7 · language: en · format: mp3 192`

**Technique:** wrap only the switched words; use a voice cloned from a bilingual speaker. Language tags are experimental — verify by ear.

---

## 8. Pronunciation Lock

```
[confident product-launch energy] Meet Valtoria. [break] I am an <|phoneme_start|>EH1 N JH AH0 N IH0 R<|phoneme_end|>, and Valtoria is the tool I always wanted.
```
**Settings:** `model: s2.1-pro · reference_id: <host> · temperature: 0.6 · top_p: 0.7 · pronunciation_dictionary: [{"items":[{"key":"Valtoria","value":"val-TOR-ee-uh"}]}] · format: wav 44.1k`

**Technique:** dictionary for the recurring brand name (every line, every session); phoneme tags (CMU Arpabet, `1` = primary stress) for one exact word. Phoneme tags are documented on the Drama 3 page — test on S2.1-Pro before relying on them there.

---

## 9. Voice Design → Reusable Voice

Request to `POST /v1/voice-design` (header `model: voice-design-1`):
```json
{"instruction": "Warm, gravelly baritone in his sixties, unhurried pacing, slight Scottish lilt, speaks like a lighthouse keeper telling a story by the fire. Intimate, never theatrical.",
 "reference_text": "The fog came in at dusk, the way it always does.",
 "n": 4, "language": "en"}
```
**Settings:** `n: 4 · num_step: 32 (default) · guidance_scale: 2 (default)` — then create a model from the winning candidate and use its `_id` as `reference_id`.

**Technique:** describe voice, age, tone, accent, pacing and context in one paragraph; a shared `reference_text` (≤150 chars) makes candidates comparable. $0.01 per request regardless of `n`.

---

## 10. Audiobook Chapter Segment

```
[low, measured, dryly amused, rarely raising his voice] Chapter Seven. [long-break]
The letter arrived on a Tuesday, which was the first strange thing about it. Nobody in Harrow Lane received post on Tuesdays.

[a shade more serious] The second strange thing was the handwriting. It was his own.
```
**Settings:** `model: s2.1-pro · reference_id: <narrator> · temperature: 0.5 · top_p: 0.65 · speed: 0.93 · latency: normal · chunk_length: 300 · condition_on_previous_chunks: true · format: wav 44.1k`

**Technique:** the baseline cue from the voice bible opens every segment verbatim; a small graded shift (`a shade more serious`) instead of a new emotion; paragraph breaks give structural pauses.

---

## 11. S1 → S2.1-Pro Migration

```
// S1 script (header: s1)
(happy) Welcome back! (whispering) I saved you a seat (near the window).
```
```
// S2.1-Pro script (header: s2.1-pro)
[happy] Welcome back! [whispering] I saved you a seat (near the window).
```
**Settings:** `model: s2.1-pro · reference_id: <same voice> · normalize_loudness: false (only if matching old S1 masters) · temperature: 0.7 · top_p: 0.7`

**Technique:** only control tags convert — the grammatical parenthesis stays. Set the header explicitly (the JS SDK still defaults to `s1`); re-listen, since `repetition_penalty` no longer has any effect.

---

## 12. Inline Zero-Shot Clone (one-off test)

```
[friendly, casual] Hey, this is a quick test of the cloned voice. How does it sound?
```
**Settings:** `model: s2.1-pro-free · Content-Type: application/msgpack · references: [{audio: <15–20 s clean WAV bytes>, text: "<exact transcript>"}] · temperature: 0.7 · top_p: 0.7 · format: mp3 128`

**Technique:** MessagePack is mandatory for inline `references`, and each reference needs its transcript. If the test passes, create a stored model — don't keep sending inline audio for production.
