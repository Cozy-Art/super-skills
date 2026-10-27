# Fish Audio Drama 3 — Best Practices

## 1. Direct an Actor, Not a Tag Parser

Drama 3 reads square-bracket direction as a brief to a performer. The strongest briefs name **what the character is trying to do** and **why**, then the feeling and pace that follow from it.

| Dimension | Example |
|---|---|
| Intention | `[trying to reassure him without revealing the danger]` |
| Emotional state | `[barely containing her anger]` |
| Listener | `[speaking gently to a frightened child]` |
| Physical condition | `[out of breath after running upstairs]` |
| Vocal placement | `[close to the microphone, intimate and warm]` |
| Pace | `[slowly, leaving space after each sentence]` |
| Transition | `[the confidence cracks halfway through]` |

| Weak | Better |
|---|---|
| `[angry] [sad] [afraid] [fast]` | `[angry with himself, talking too fast to hide the fear]` |
| `[dramatic]` | `[holding back tears, determined not to let him hear it]` |
| `[old man voice]` | Pick an older voice; cue delivery: `[tired, slow, every word costs effort]` |
| `[cinematic, wide shot]` | `[projecting across a large, empty hall]` |
| `She pauses, then:` (unbracketed) | `[a long beat, then quietly]` |

- One clause, one coherent objective. Long or malformed briefs disturb rhythm and can be vocalized.
- Directions can be written in another language than the dialogue — useful for multilingual crews.
- Describe only what is **audible**. The model has no picture.

## 2. Persistence and Placement

- A bracket applies **from its position until the next direction**. Put it immediately before the words it governs.
- Several brackets inside one line shift delivery within that line — use this for turns, not decoration.
- New beat → new bracket. Don't park one paragraph-long brief at the top of a scene.
- Prefer starting a line with a direction or a spoken word, not a point event or filler; some stacks report trailing silence when text opens with `[laughs]` or `Um…`.

## 3. Point Events

Write the sound **exactly where it happens**. The vocabulary is open natural language, not a closed list.

```
I thought you had left. [shaky breath] I searched everywhere.
[small, disbelieving laugh] And you were here the entire time.
```

| Abstract | Physical (better) |
|---|---|
| `[laughing]` | `[a short, involuntary laugh]` |
| `[sad]` before a line | `[voice breaks]` at the word where it breaks |
| `[pause]` | `[brief pause]` · `[long pause]` · or a full stop + new line |
| `[scared]` | `[sharp intake of breath]` |

Useful anchors: `[sighs]` `[laughs]` `[gasps]` `[coughs]` `[swallows]` `[shaky breath]` `[voice breaks]` `[brief pause]` `[long pause]`. Give the event narrative context — a laugh after a line that earns it sounds real; a laugh in a vacuum sounds pasted.

## 4. Paired (Word-Scoped) Tags

Seven are documented. They change **only** the wrapped words and end exactly at the closing tag.

| Tag | Effect |
|---|---|
| `<whisper>…</whisper>` | Whisper the span |
| `<emphasis>…</emphasis>` | Emphasize |
| `<soft>…</soft>` | Soften |
| `<fast>…</fast>` | Speed up |
| `<slow>…</slow>` | Slow down |
| `<stress>…</stress>` | Marked verbal stress |
| `<forceful>…</forceful>` | Deliver forcefully |

- Paired tag = change that must stop at a word. Bracket = change that should carry on.
- Wrap the smallest span that carries the meaning: `<stress>one</stress> line`, not the sentence.
- Close every tag; don't nest. One or two per line — stress everything and nothing lands.

## 5. Language Tags (experimental)

`<french>` `<spanish>` `<german>` `<japanese>` `<chinese>` `<korean>` `<italian>` are shown by Fish; the list is not stated as complete and support is "not guaranteed for every language or voice".

- Wrap only the switched words; keep the surrounding language untagged.
- Use a voice cloned from someone fluent in both languages; test the pair by ear.
- Already-multilingual text may switch on its own without tags.

## 6. Pronunciation

1. Respell one-offs in the script (changes captions).
2. A pronunciation dictionary for recurring names (Fish API `pronunciation_dictionary`).
3. Phoneme tags for exact control: `<|phoneme_start|>EH1 N JH AH0 N IH1 R<|phoneme_end|>` — English CMU Arpabet (`1` primary stress, `0` unstressed), Chinese pinyin, Japanese romaji.

Write numbers, dates and acronyms as they should be said when normalization guesses wrong.

## 7. Punctuation Is Timing

| Mark | Effect |
|---|---|
| `.` / new line | Boundary and breath — also a preferred chunk split |
| `,` | Light phrasing break |
| `—` | Interruption or pivot |
| `…` | Hesitation (sparingly) |
| `?` `!` | Contour / energy — one `!` is enough |
| blank line | Strongest separation between beats |

Short sentences carry action; long, comma-led sentences carry thought. Split long unpunctuated paragraphs.

## 8. Scene Blocking (Native Syntax)

```
<|speaker:0|> [quietly suspicious] You came alone?

<|speaker:1|> [breathless, trying to recover]
Yes. <emphasis>Completely</emphasis> alone.

<|speaker:0|> [does not believe him]
Then whose car is outside?
```

- Every turn starts with its speaker tag and its own reaction brief — the reaction is the performance.
- Keep turns short in fast exchanges; the chunker groups at most three speakers per internal chunk, so a crowd scene alternating six voices line by line is chunked more often.
- ComfyUI node: replace `<|speaker:N|>` with `@VoiceN+1` (`@Voice1` = first connected voice), ≤5 voices, each must appear.

## 9. Revision Notes

On a surface that keeps prior takes in context, the next turn is read as a **director's note on the previous take**. The technical report's example form is relative: `[softer and warmer versus previous]`.

| Good revision note | Why |
|---|---|
| `[more restrained than the previous take]` | Relative, one axis |
| `[keep the timing, but soften the final sentence]` | Says what to preserve |
| `[same read; longer pause before "come back"]` | Localized |
| `[preserve the laugh; make the first line less defensive]` | Keeps the win |

Avoid absolute re-briefs (`[sad]`) in a revision turn — they invite a fresh performance instead of an adjustment. On a stateless endpoint, write a normal, complete brief and call the result a new take.

## 10. Failure Modes

| Failure | Fix |
|---|---|
| Flat acting | Add intention, listener and physical condition; shorter sentences |
| Direction read aloud | Shorten; close the bracket; put words after it |
| Muddy, unstable line | Remove contradictory directions; one objective |
| Bad laugh / gasp | Describe it physically and give it a reason in the text |
| Weak word control | Paired tag around only the target words |
| Character drift | Restore references, cast map, sampling and history; lower `temperature` |
| Voices swapped | Speaker numbers reshuffled or reference order changed — restore the cast map |
| Wrong name | Phonemes or dictionary, not rerolls |
| Trailing silence / long tail | Cap `max_new_tokens` near expected length; don't open with an event or filler |
| `@Voice1` heard or ignored | Wrong surface — native tags outside ComfyUI |
| `(happy)` spoken | S1 parentheses — convert to brackets |
| Edit sounds pasted in | More surrounding context, or revise from the accepted take |
