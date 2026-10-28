# Eleven v4 — Annotated Examples

Every example is two-part: **script** (spoken words + inline tags + IPA) + **suggested settings**. Model, voice settings, format and effects never appear in the script.

---

## 1. Simple Character Line

```
[warm, confident, conversational] Welcome back. I saved your place by the window.
```
**Settings:** `model: eleven_v4 · stability: 0.50 · similarity: 0.75 · output: mp3_44100_128`

**Technique:** one baseline tag, no local changes. Short, natural text lets v4 infer the rest.

---

## 2. Intimate Character Beat

```
[low, steady voice, restrained urgency] Keep the lantern covered.
If they see the light, they'll know we crossed the river.

[long pause]
[quietly, controlled fear] I heard them at the bridge… not soldiers. Something else.
```
**Settings:** `model: eleven_v4 · stability: 0.42 · similarity: 0.75 · output: wav_48000`

**Technique:** baseline → paragraph break + pause tag for the beat → one local emotional turn. Ellipsis carries the hesitation. No SSML.

---

## 3. Documentary Narration

```
[quiet, measured documentary narration] Before sunrise, the salt marsh is almost silent.
A thin wind moves through the reeds… then thousands of wings rise at once.

[soft awe, a little more breath] For a few seconds, the entire horizon seems alive.
```
**Settings:** `model: eleven_v4 · stability: 0.58 · similarity: 0.75 · output: wav_44100`

**Technique:** the environment is conveyed through words and the narrator's reaction, not SFX tags. Real reeds and wings → separate SFX layer.

---

## 4. Action Escalation

```
[focused, clipped delivery] Reactor pressure is climbing. Seal the lower deck.

[controlled concern, pace quickening] The port valve isn't responding.

[voice tightening] It's not— it's still climbing.

[urgent, finally shouting] Everybody away from the bulkhead — NOW!
```
**Settings:** `model: eleven_v4 · stability: 0.38 · similarity: 0.75 · output: wav_48000`

**Technique:** a four-step intensity gradient rather than a jump to maximum; CAPS on a single word; lower Stability so the escalation has room. Alarms and impacts rendered separately for frame-accurate sync.

---

## 5. Audio "Camera Move" (push-in)

```
[distant, calling across a large stone chamber] Mara! Can you hear me?

[closer now, breath unsteady] Mara… answer me.

[very close, almost a whisper] Please.
```
**Settings:** `model: eleven_v4 · stability: 0.45 · similarity: 0.75 · output: wav_48000`

**Technique:** a visual push-in translated into audible distance and intimacy. For a physically convincing move, render each line dry and automate distance/reverb in a DAW — or per line via `audio_effects.distance` (e.g. 0.8 → 0.4 → 0).

---

## 6. Two-Character Dialogue

```
CAPTAIN:  [measured, hiding exhaustion] We have enough fuel for one landing.
ENGINEER: [incredulous, then dry amusement] One landing? That's your good news?
CAPTAIN:  [quietly] The good news is that we only need one.
ENGINEER: [soft laugh, settling into resolve] Then point us home.
```
**Settings:** `model: eleven_v4 · endpoint: text-to-dialogue · stability: 0.48 · similarity: 0.75 · output: wav_48000`

```json
{
  "model_id": "eleven_v4",
  "inputs": [
    {"voice_id": "CAPTAIN_VOICE_ID",  "text": "[measured, hiding exhaustion] We have enough fuel for one landing."},
    {"voice_id": "ENGINEER_VOICE_ID", "text": "[incredulous, then dry amusement] One landing? That's your good news?"},
    {"voice_id": "CAPTAIN_VOICE_ID",  "text": "[quietly] The good news is that we only need one."},
    {"voice_id": "ENGINEER_VOICE_ID", "text": "[soft laugh, settling into resolve] Then point us home."}
  ],
  "settings": {"stability": 0.48, "similarity": 0.75}
}
```

**Technique:** labels are for the human-readable script only; the API maps each turn to a `voice_id`. Dialogue settings use `similarity` (not `similarity_boost`). Well under the 2,000-character ceiling.

---

## 7. Interruption and Trail-Off

```
GUEST: [cautiously] Hello, is this seat—
HOST:  [jumping in] Free? [cheerfully] Yes, it is!
GUEST: [indecisive] Great, then can I get, uhhh… actually, what's good here?
```
**Settings:** `model: eleven_v4 · endpoint: text-to-dialogue · stability: 0.45 · similarity: 0.75`

**Technique:** em dash ends the cut-off turn, `[jumping in]` opens the next; filler and ellipsis carry the hesitation. Two tags inside one turn mark a mid-line shift.

---

## 8. Multilingual Brand Read with IPA

```
[clear, elegant, quietly optimistic] At Asterion — "/æˈstɪəriən/" — we design tools that help ideas travel.
```
```
[warm and natural] Creamos para personas curiosas, en cualquier lugar del mundo.
```
**Settings:** `model: eleven_v4 · stability: 0.60 · similarity: 0.80 · language_code: en / es (one render each) · dictionary: brand-names v2 · output: mp3_44100_192`

**Technique:** IPA in slashes with stress marks for the brand name; each language rendered separately with its own `language_code`. v4 gives the Spanish read a native accent while keeping identity — get each language approved. For a recurring campaign, move the IPA into a pronunciation dictionary.

---

## 9. Voice-Agent Turn (real time)

```
[friendly, efficient] Got it — your table for four is booked for seven thirty tonight. Anything else I can help with?
```
**Settings:** `model: eleven_v4_turbo · transport: TTD WebSocket · voices: [AGENT_VOICE_ID] (one only) · stability: 0.60 · similarity: 0.75 · output: ulaw_8000 (telephony) or opus_48000_64`

```json
{"inputs": [{"text": "[friendly, efficient] Got it — your table for four is booked for seven thirty tonight. Anything else I can help with?", "voice_id": "AGENT_VOICE_ID", "new_turn": true}]}
```

**Technique:** one high-confidence tag, numbers in spoken form ("seven thirty", not "7:30"), turn ends with `new_turn: true`. The line clears the ~40-char / 8-word buffer, so audio starts immediately.

---

## 10. Audiobook Segment (stitched)

```
[unhurried, warm narration] Chapter Three. The house on Calder Street had been empty for a decade, though nobody in the village would say so out loud.

Mrs. Pell, who swept her front step every morning at exactly seven, swore she'd seen a light upstairs. [slight, knowing lilt] Twice.
```
**Settings:** `model: eleven_v4 · stability: 0.60 · similarity: 0.75 · output: wav_44100 · previous_request_ids: ["<chapter 2 final segment ID>"]`

**Technique:** segment ≈ 300 characters at a paragraph boundary; stitched to the last segment of the previous chapter. One small local colour tag; the narrator's baseline comes from the voice and the manifest, not from a re-description.

---

## 11. Regenerated Middle Clip

```
[quietly, controlled fear] I heard them at the bridge… not soldiers. Something else.
```
**Settings:** `model: eleven_v4 · same voice + settings as neighbours · previous_request_ids: ["r3", "r4"] · next_request_ids: ["r6"]`

**Technique:** a fix for one bad line. Neighbouring IDs on both sides (previous: closest last; next: closest first) let the new take match level, pace and tone at both joins. Same model as the neighbours.

---

## 12. Phone-Call Effect via `audio_effects`

```
[hushed, hurried, slightly out of breath] It's me. Don't call back on this line. I'll explain tomorrow.
```
**Settings:** `model: eleven_v4 · stability: 0.45 · similarity: 0.75 · output: mp3_44100_128 · audio_effects: {filter_preset_id: "phone", background_noise_id: "<from catalog>"}`

**Technique:** the "phone" character is an effect, not words in the script — the tag only describes the vocal performance. Look up valid IDs via `GET /v1/audio-effects/catalog`. No reverb or pan here, so a PCM output would also be valid; adding `environment_id` or `pan` would need MP3/Opus/WAV. For final mixes, prefer rendering dry and filtering in post.
