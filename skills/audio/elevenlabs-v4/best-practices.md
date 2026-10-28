# Eleven v4 — Best Practices

## 1. Write for the Ear

The script is performed literally. Every word in it will be spoken, and every tag should change something you can hear.

| Visual / vague | Audible direction |
|---|---|
| `[cinematic]` | `[low, measured, trailer-narrator gravity]` |
| `[slow dolly toward her face]` | `[quiet, intimate, tension slowly rising]` |
| `[wide shot of the hall]` | `[distant, calling across a large stone chamber]` |
| `[sad scene]` | `[voice thin, holding back tears]` |
| `[he paces nervously]` | `[breath unsteady, words tumbling out]` |
| `[epic]` | `[building intensity, each word heavier]` |

Natural speech gives v4 material to act from: contractions, fragments, false starts, interruptions, paragraph breaks. Context matters — "after everything you did…" is read differently from the same words with no lead-in.

## 2. Tag Syntax

- Square brackets, plain language, **adjacent** to the words they affect — before (`[annoyed] This is hard.`) or after (`This is hard. [sighs]`).
- Tags are an open vocabulary, not an enum. Tag-following is good but not perfect and still evolving — test on your voice.
- Combine compatible qualities: emotion + energy + pace + texture. `[quiet, tired, dry humour]`.
- Describe the **voice**, not a sound cue: `[low, gravelly voice]` rather than `[gravel]`.
- Exclude non-audible tags (`[standing]`, `[grinning]`, `[pacing]`) and music cues (`[music]`).
- If a tag is spoken aloud, rephrase it, move it closer, or try a synonym; edit it out in post if it slipped through.

### Tag vocabulary (documented examples)

| Category | Tags |
|---|---|
| Emotion / attitude | `[happy]` `[sad]` `[excited]` `[angry]` `[annoyed]` `[appalled]` `[thoughtful]` `[surprised]` `[curious]` `[sarcastic]` `[mischievously]` `[casual]` |
| Volume / register | `[whispers]` / `[whispering]` `[shouting]` `[under his breath]` `[low, steady voice]` |
| Non-verbal | `[laughs]` `[laughs harder]` `[starts laughing]` `[chuckles]` `[soft chuckle]` `[giggle]` `[wheezing]` `[sighs]` `[exhales]` `[exhales sharply]` `[inhales deeply]` `[clears throat]` `[snorts]` `[crying]` `[swallows]` `[gulps]` |
| Pacing | `[short pause]` `[long pause]` `[brief pause]` `[Quick, light, playful pace]` |
| Dialogue flow | `[jumping in]` `[cautiously]` `[indecisive]` `[cheerfully]` `[elated]` |
| Sound events (probabilistic) | `[applause]` `[clapping]` `[gunshot]` `[explosion]` |
| Experimental (less consistent) | `[strong French accent]` (any accent) `[sings]` `[woo]` |

## 3. Direct at Phrase Level

One baseline tag at the top; new tags only where the performance **turns**.

```
[calm, intimate narration] The signal had been silent for eleven years.
Then, at three seventeen… it answered.
[restrained alarm, pace quickening] Not from the relay. From inside the ship.
```

Repeating the same tag before every sentence makes delivery mechanical. Too many strong tags → melodrama.

## 4. Control Intensity Without Sliders

No intensity or speed control exists. Intensity = context + tag + punctuation + Stability.

- **Gradient, not a jump:** `[controlled concern]` → `[voice tightening]` → `[urgent, finally shouting]`.
- **Short clauses and `!`** accelerate; **ellipses** slow and weigh.
- **CAPS** on one or two words per passage, never whole sentences.
- **Lower Stability** (0.35–0.45) loosens the performance; **higher** (0.6+) pins it.
- Pace: write it. Short sentences and `—` read faster; longer sentences with `…` read slower. Exact timing → measure, then trim script or time-stretch modestly in post.

## 5. Punctuation and Pauses

| Mark | Effect |
|---|---|
| `…` | Hesitation, trailing off, weight |
| `—` | Sharp cut-off or interruption (`Is this seat—`) |
| `,` `.` | Normal phrasing |
| Paragraph break | Larger beat / breath |
| `?` `!` | Rising intonation / energy |
| CAPS | Emphasis on that word |

**No SSML.** ElevenLabs' generic pause docs still show `<break time="1.5s" />`, but the v4-specific guidance says v4 and v3 don't support SSML break tags. Use punctuation and `[short pause]` / `[long pause]`.

## 6. Pronunciation (IPA)

```
The field of "/ˌbaɪoʊˈkemɪstri/" studies chemical processes in living organisms.
```
- Forward slashes around standard IPA, quoted; include `ˈ` primary and `ˌ` secondary stress on multisyllabic words.
- Apply only to words that need it; results vary by voice — render more than once if it matters.
- For names and brands that recur, use a **pronunciation dictionary** (up to 3 locators per request, applied in order; entries are case-sensitive, first match wins) and version it.
- `<phoneme>` tags are for `eleven_flash_v2` only, not v4.

## 7. Normalize Speakable Text

`apply_text_normalization: auto` is default, but write important copy the way it should be heard:

| Written | Write instead |
|---|---|
| `$1,250` | `twelve hundred and fifty dollars` |
| `03:17` | `three seventeen` / `three seventeen in the morning` |
| `555-0142` | `five five five, oh one four two` |
| `Dr.` / `St.` | `Doctor` / `Street` or `Saint` |
| `example.com/help` | `example dot com slash help` |
| `5km` | `five kilometres` |
| `Ctrl+S` | `control S` |
| `NASA` vs `NFL` | leave acronyms said as words; space letter-by-letter ones (`N F L`) |

For LLM-generated agent text, instruct the LLM to output spoken-form numbers and symbols.

## 8. Voice Selection

- The voice is the first-order variable. Audition before tuning anything else.
- Deliveries present in the voice's source audio (whispering, shouting) are more reliable; v4 can go beyond them, but less reliably.
- Match tags to the voice's character — a gravely serious voice may handle `[giggles]` poorly.
- v4 reproduces source characteristics faithfully — timbre, cadence, EQ, plosives, room noise. A noisy clone gives a noisy voice.
- Voice Design voices work on v4 but may be less performative than with earlier models.

## 9. Dialogue Craft

- One `inputs` turn per speaker change; tags inside each turn.
- Interruptions: end the cut-off turn with `—`, start the next with `[jumping in]`.
- Trail-offs: `…` and `[indecisive]`; fillers (`uhhh`, `um`) are spoken naturally.
- Mid-line shifts: `[elated] Yes! [laughs] I'm so glad you knew!`
- Overlapping speech is not documented — cut overlaps in the edit.
- Keep each request ≤2,000 combined characters; split scenes at beats, not mid-exchange.

## 10. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Visual / camera language | Wasted text, odd reads | Translate to audible intention |
| Tag spoken aloud or ignored | Garbled line | Concrete vocal wording, adjacent placement, synonym |
| Tag before every sentence | Mechanical delivery | One baseline + local turns |
| Many strong tags, CAPS, `!!!` | Melodrama | One baseline, one transition |
| SSML `<break>` / `<prosody>` | Spoken or ignored | Punctuation, `[short pause]` |
| Relying on `style` / `speed` | No effect / v3 recipes misfire | Wording, punctuation, voice choice |
| No `model_id` | Renders on v2 / v3 | Always send `eleven_v4` / `eleven_v4_turbo` |
| Flat voice | Stability too high / neutral text | Lower Stability, add context |
| Identity drifts between clips | Changed voice/model/settings, no stitching | Lock manifest, pass request IDs |
| Names vary across episodes | Spelling-only pronunciation | IPA or versioned dictionary |
| Numbers misread | Ambiguous notation | Spell out in spoken form |
| Long render degrades | Oversized generation, noisy clone | ≤800 chars per segment, stitch |
| Dialogue cuts off early | >2,000 chars in one request | Split by beat |
| Turbo socket rejects voices | >1 voice registered | One Turbo socket per voice, or v4 socket |
| Unwanted accent in localized read | v4 uses native target accent | Approve per language; try accent tag; keep older model if source accent required |
| Precise SFX in the voice prompt | Mistimed, inconsistent | Dry voice + separate SFX in post |
