# Fish Audio Drama 3 — Annotated Examples

Every example is two-part: **script** (the `text` / `input` value) + **settings**. Settings never appear in the script; on the Fish API the model is a header.

---

## 1. Character Monologue

```
[late at night, exhausted but unwilling to admit defeat, speaking quietly to herself]
I have rewritten this message twelve times.

[small, embarrassed laugh] Thirteen, if we count the one I deleted before breakfast.

[more certain now]
But this one says what I actually mean: <emphasis>I am not leaving.</emphasis>
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: <lena> · temperature: 0.7 · top_p: 0.7 · format: wav 44.1k · takes: 3`

**Technique:** one acting objective per beat; the event sits inside the beat it belongs to; a paired tag lands the final phrase without changing the rest of the line.

---

## 2. Emotional Turn Inside One Line

```
[calm and affectionate, speaking to someone standing very close]
I kept every letter you sent.
[the warmth fades as an old suspicion returns] Every letter except the one from Paris.
<whisper>You never explained that one.</whisper>
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: <iris> · temperature: 0.75 · top_p: 0.75 · format: wav 44.1k`

**Technique:** the second bracket replaces the first exactly where the subtext shifts; the whisper is scoped so it ends with the sentence.

---

## 3. Two-Character Confrontation

```
<|speaker:0|> [controlled anger, keeping his voice low]
You moved the money without telling me.

<|speaker:1|> [defensive at first, then ashamed]
I was trying to protect us.

<|speaker:0|> [a short, disbelieving laugh] By emptying the account?

<|speaker:1|> [voice breaking]
By making sure there was still something left to save.
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: [<tomas>, <ines>] · temperature: 0.7 · top_p: 0.75 · format: wav 44.1k · takes: 3`

**Technique:** array order = speaker number; each turn opens with its own reaction brief. The laugh is the reaction, so it leads speaker 0's third line.

---

## 4. Action Sequence

```
<|speaker:0|> [running, breathless, shouting into a radio]
North stairwell! They're coming up fast. [sharp breath]
I need that door open <forceful>now</forceful>!

<|speaker:1|> [focused, typing quickly, words clipped]
Eight seconds.

<|speaker:0|> [frustrated, nearly shouting] We do not have eight seconds!

<|speaker:1|> [sudden relief] You do now. Move!
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: [<kade>, <ops>] · temperature: 0.8 · top_p: 0.85 · format: wav 44.1k · takes: 4`

**Technique:** physical state in the brief, short sentences, the breath placed mid-turn. Higher sampling for range — audition takes. Radio processing goes in post.

---

## 5. Cinematic Narration

```
[deep, unhurried narration, leaving space after each sentence]
At three seventeen in the morning, every light in the city went out.

[closer and quieter, as if sharing forbidden knowledge]
Every light except one.

<slow>The room at the top of Meridian Tower.</slow>
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: <narrator> · temperature: 0.55 · top_p: 0.65 · latency: normal · format: wav 44.1k`

**Technique:** time written as words to avoid normalization surprises; lower sampling for a stable narrator; `<slow>` scoped to the reveal.

---

## 6. Multilingual Scene (experimental tag)

```
<|speaker:0|> [warm, welcoming] Your table is ready, madame.

<|speaker:1|> [relieved, switching naturally into French]
<french>Merci. J'attends cette soirée depuis très longtemps.</french>

<|speaker:0|> [gently curious] A special occasion?

<|speaker:1|> [softly, almost to herself] You could say that.
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: [<host>, <claire_bilingual>] · temperature: 0.65 · top_p: 0.7 · language: en · format: wav 44.1k`

**Technique:** only the switched words are tagged; speaker 1 uses a voice cloned from a bilingual speaker. Language tags are experimental — check by ear.

---

## 7. ComfyUI Fish Audio Node (wrapper syntax)

```
@Voice1 [deep, composed narrator] Every city has a secret.
@Voice2 [young, skeptical, trying not to sound afraid] And you expect me to believe you found ours?
@Voice1 [leans in, conspiratorial] I did not find it. <whisper>It found me.</whisper>
```
**Settings:** `surface: ComfyUI Fish Audio TTS · model: drama-3 · voices: slot 1 = <narrator>, slot 2 = <kid>`

**Technique:** `@VoiceN` follows the node's connected-voice slots (≤5) and every connected voice must appear. This text is **not** valid for the Fish API — there it becomes `<|speaker:0|>` / `<|speaker:1|>` with a `reference_id` array.

---

## 8. Five-Character Scene With a Frozen Cast Map

```
<|speaker:3|> [dry narrator, matter-of-fact] The briefing lasted four minutes.

<|speaker:2|> [clipped, impatient, used to being obeyed] Reyes. Status.

<|speaker:0|> [low, precise, tired but never careless] The relay is gone. So is the backup.

<|speaker:4|> [nervous, too quick] That's — that's not possible, I checked it myself.

<|speaker:1|> [calm, synthetic warmth] You checked it nine hours ago, Tavi.

<|speaker:2|> [a long beat, then quietly] Then we're on our own.
```
**Settings:** `surface: Fish API · model: drama-3 · reference_id: [<mara>, <sol>, <reyes>, <narrator>, <tavi>] · temperature: 0.7 · top_p: 0.7 · format: wav 44.1k`

**Technique:** speaker numbers come from the project cast map (MARA 0, SOL 1, REYES 2, NARRATOR 3, TAVI 4), not from who speaks first. The chunker groups ≤3 speakers per internal chunk; send it as one request so history carries.

---

## 9. Revision Note (history-capable surface)

```
[sadder than the previous take, but less theatrical; keep the original timing and the breath before the last sentence]
I knew you would come back. I just did not know whether I would still be here.
```
**Settings:** `surface: SGLang-Omni /v1/tts · model: fishaudio/drama-3 · references: [{audio_path: <june.wav>, text: <exact transcript>}] · previous_takes: [<take 1>] · temperature: 0.65 (≤ accepted take) · top_p: 0.7`

**Technique:** the note is **relative** and names what to preserve. Without take history (Fish API, vLLM-Omni) this same text is just a new take — rewrite it as a complete brief instead.

---

## 10. Infill-Style Correction

```
[match the accepted performance exactly; change only the day, keep all surrounding timing]
The inspection is scheduled for Thursday at nine.
```
**Settings:** `surface: SGLang-Omni /v1/tts · model: fishaudio/drama-3 · same references · previous_takes: [<accepted take: "…for Tuesday at nine.">] · temperature: 0.6`

**Technique:** send the full corrected line with the accepted take in history. The prompt alone does not infill — the serving layer must supply the prior audio. Fallback: re-render with a sentence either side and cut at a breath.

---

## 11. Pronunciation Lock (Fish Speech, local)

```
<|speaker:0|> [clear, confident briefing]
Welcome aboard the <|phoneme_start|>V ER0 IY1 N<|phoneme_end|>. I'm your systems <|phoneme_start|>EH1 N JH AH0 N IH1 R<|phoneme_end|>.
```
**Settings:** `surface: Fish Speech /v1/tts (MessagePack) · checkpoint: drama-3 · reference_id: mara-v3 (speaker 0) · temperature: 0.6 · top_p: 0.7 · max_new_tokens: 0 · format: wav`

**Technique:** Arpabet with stress digits for an invented ship name and a stress-sensitive word; recurring names belong in the voice bible. `max_new_tokens: 0` uses the model's own per-chunk cap; no per-request model field exists on the open server.
