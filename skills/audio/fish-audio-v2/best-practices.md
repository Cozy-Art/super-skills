# Fish Audio — Best Practices

## 1. Write Scripts, Not Descriptions

Fish only hears two things: words to speak and bracketed direction. There is no scene, camera or appearance channel. Every non-spoken instruction must sit inside `[ ]` (or a Drama 3 scoped tag) and must describe something **audible**.

| Weak | Better |
|---|---|
| `[cinematic]` | `[low, measured, close to the mic]` |
| `[sad scene in the rain]` | `[quietly, trying not to cry]` |
| `[old man]` (to change the voice) | Pick an older voice model; cue only delivery: `[tired, slow, gravelly with age]` |
| `[happy excited joyful thrilled ecstatic]` | `[quietly ecstatic, trying to stay professional]` |
| `[very very angry 10/10]` | `[furious, barely containing it]` |
| `She pauses, then says:` (unbracketed) | `[a long beat, then quietly]` |

Direction describes **emotion + energy + pace + loudness + breath state + relationship to the listener**. Brief it the way you'd brief a voice actor.

## 2. Cue Vocabulary (S2.1-Pro / S2-Pro / Drama 3)

Free-form descriptions work; these are the documented anchors.

| Category | Examples |
|---|---|
| Emotion (49 listed) | `[happy]` `[sad]` `[angry]` `[excited]` `[calm]` `[nervous]` `[confident]` `[surprised]` `[curious]` `[sarcastic]` `[determined]` `[resigned]` |
| Tone | `[in a hurry tone]` `[shouting]` `[screaming]` `[whispering]` `[soft tone]` `[emphasis]` |
| Vocal sounds | `[laughing]` `[chuckling]` `[sobbing]` `[crying loudly]` `[sighing]` `[groaning]` `[panting]` `[gasping]` `[yawning]` `[snoring]` `[clear throat]` |
| Special | `[audience laughing]` `[background laughter]` `[crowd laughing]` |
| Pauses | `[break]` (short) · `[long-break]` (long) |

Plain text like `Ha, ha, ha` also produces laughter. Cues add no latency and don't count toward token limits.

## 3. Placement Rules

- **Sentence-level emotion → start of the sentence.** Don't park a cue far from the line it controls.
- **Sounds, pauses, tone shifts → exactly where they happen**, mid-sentence if needed.
- **New beat, new cue.** Arcs work sentence by sentence, not as one stacked tag at the top of a paragraph.
- **`[emphasis]` immediately before the stressed phrase**, sparingly — stress everything and nothing stands out.
- **Max three combined emotions per sentence; one primary is best.** Stacked brackets are allowed (`[sad][whispering]`) but count toward that limit.
- **Don't over-tag short text.** A cue every few words makes delivery choppy.

## 4. Intensity by Description

No numeric strength exists. Grade with words:

```
[slightly worried] → [visibly nervous but trying to sound composed] → [panicking, words tumbling out]
[mildly amused] → [laughing nervously] → [helpless with laughter]
```

## 5. Punctuation = Timing

| Mark | Effect |
|---|---|
| `.` | Clear boundary, breath |
| `,` | Light phrasing break |
| `;` | Connected thought, stronger pause |
| `—` | Interruption / pivot (sparingly) |
| `…` | Hesitation — overuse sounds unnatural |
| `?` | Interrogative contour |
| `!` | Energy — can overdrive expressive cues; one is enough |
| blank line | Strongest structural break |

Long unpunctuated paragraphs produce bad breath groups. Split them.

## 6. Drama 3 Extras

- **Scoped tags** change only the wrapped words: `<whisper>` `<emphasis>` `<soft>` `<fast>` `<slow>` `<stress>` `<forceful>`.
  `I'm fine. Really. <whisper>Go on without me.</whisper>`
- **Directions can be in a different language from the script** (e.g. English direction over a Japanese line).
- **Language tags (experimental):** `<french>…</french>`, `<spanish>`, `<german>`, `<japanese>`, `<chinese>`, `<korean>`, `<italian>`. Wrap only the switched words; use a voice cloned from a speaker fluent in both languages. The model may switch on its own if text is already multilingual.
- Positioned for **rendered, scripted lines**; for live agents use `s2.1-pro`. Takes vary — render a few, keep the best.
- Scoped `<…>` tags are documented for Drama 3 only; on S2.1-Pro use bracket equivalents (`[whispering]`, `[emphasis]`).

## 7. Pronunciation

Order of preference:

1. **Respell in the script** for one-offs (`Nguyen` → `Win`) — cheapest, but changes captions.
2. **`pronunciation_dictionary`** for recurring names/brands: inline `{"items":[{"key":"Valtoria","value":"val-TOR-ee-uh"}]}` or saved `{id, version}` (≤3 dictionaries; unresolvable refs dropped silently — test).
3. **Phoneme tags** for exact control: `<|phoneme_start|>EH1 N JH AH0 N IH0 R<|phoneme_end|>`
   English = CMU Arpabet (`1` primary stress, `0` unstressed) · Chinese = pinyin · Japanese = romaji.

Also: write numbers, dates, currency and acronyms the way they should be said when `normalize` guesses wrong ("ten thirty", "A-P-I" vs "appy"). Set `language` for correct normalization of mixed-locale text.

## 8. Dialogue Blocking

```
<|speaker:0|>[trying to stay calm] Did you lock the north door?
<|speaker:1|>[breathless] I did. Something opened it from the other side.
<|speaker:0|>[a long beat, then quietly] Turn off your flashlight.
```

- `reference_id` array order = speaker index (0-based). Same index = same character, every scene.
- Short turns; each turn carries its own cue — the reaction is the performance.
- Directions (and Drama 3 scoped tags) work inside each turn.
- S1 can't do this — render per speaker and stitch.

## 9. Visual → Audio Translation

The model can't pan, place or reverberate. Translate shot language into delivery; do the rest in the mix.

| Visual idea | Direction in script | In post |
|---|---|---|
| Close-up | `[intimate, barely above a whisper, close to the mic]` | dry, present |
| Wide shot | `[projecting across a large space]` | reverb, distance EQ |
| Push-in | start `[addressing the room]` → end `[quietly, to one person]` | automate reverb down |
| Chase | `[breathless, clipped phrases]` + `[panting]` | add footsteps/Foley |
| Establishing | sparse lines + `[long-break]` | ambience bed |

## 10. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| `(happy)` on S2 / Drama 3 | Spoken or ignored | `[happy]` |
| Unbracketed stage directions | Read aloud | Bracket them |
| Visual prose in brackets | Irrelevant conditioning | Audible delivery only |
| Trying to change timbre with cues | Voice stays the reference | Change `reference_id` |
| >3 emotions per sentence | Muddy, unstable | One primary + at most two modifiers |
| Cue every few words | Choppy | Cue at sentence/beat boundaries |
| `model` header omitted | Silent `s2.1-pro` (or SDK default `s2-pro`/`s1`) | Set it explicitly |
| Max temperature/top_p | Identity, timing, pronunciation drift | Start 0.7/0.7, lower for consistency |
| Tiny chunks for narration | Boundary artifacts | 200–300, `normal` |
| Huge chunks for live agents | Slow first audio | 100–180, `balanced` |
| Noisy/reverberant reference | Room and noise cloned | Clean, dry, single speaker |
| New inline sample per line | Voice wanders | One voice model ID |
| Expecting `seed` or `duration` | Field doesn't exist | Save takes; edit length in script/speed |
| Scoped tags on `s2.1-pro` | Undocumented — may be spoken | Drama 3, or bracket equivalents |
