# LTX-2.3 — Best Practices

## 1. Detail Budget: One Unambiguous Shot

Official guidance: one flowing present-tense paragraph, roughly 4–8 descriptive sentences, covering shot, scene, action, characters, camera and audio. Every sentence should add an action, a spatial relationship, a camera behaviour, a visual property or a sound cue.

| Sentences | Job |
|---|---|
| 1 | Primary action — open with what happens |
| 1–2 | Character appearance + physical behaviour |
| 1 | Environment + atmospheric motion |
| 1–2 | Camera: opening framing → movement → landing composition |
| 1 | Light, palette, texture, lens |
| 1 | Sound: ambience, synced effects, music, dialogue, or silence |

There is no official word cap beyond the 5,000-character field; quality usually peaks around 60–180 words. Filling the field rarely helps.

| Weak | Better |
|---|---|
| `cinematic` | `A slow dolly in from a low medium shot, warm practical lamps against cool blue window light` |
| `epic action` | `She clears one gap, lands hard, and slides under a half-closed gate` |
| `sad` | `Her lower lip tightens and she exhales against the glass` |
| `dynamic camera` | `The camera tracks backward at her walking pace and ends on a centered medium shot` |
| `nice ambience` | `Soft rail noise, rain on the window, a distant announcement in muffled French` |

## 2. Chronology Is the Structure

LTX reads the paragraph as a timeline. Order events as they happen; use transitions for beats:

```
The shot begins… As she reaches the door… The camera then… By the final moment…
```

- Write pauses in. The model times action to what's written — it won't add a beat you didn't ask for.
- One primary action + one secondary reaction per 6–10 s clip.
- End with the landing state: "The move ends in a symmetrical wide shot with the doorway centered."

## 3. Camera Language

**Presets (`camera_motion`)** — `dolly_in`, `dolly_out`, `dolly_left`, `dolly_right`, `jib_up`, `jib_down`, `static`, `focus_shift`. Each is one discrete move; there is no strength or speed value.

| Need | Do |
|---|---|
| Move matches a preset | Set the preset **and** describe the same move in prose |
| Pan, tilt, orbit, handheld, tracking, crane arc | Omit the field; describe in prose |
| Two moves (e.g. pull out + rise) | Pick the dominant one as preset, or prose only; time any handoff explicitly |
| Locked-off | `static` + "the camera remains locked; all motion is in the subject" |
| Rack focus | `focus_shift` + name the foreground subject, background subject and handoff moment |

Prose rules from the official guide:
- Say **how and when** the camera moves, relative to the subject ("tracks backward at waist height in front of her").
- Describe what the subject is doing **after** the move begins, and what the frame reveals — it helps the model complete the motion.
- Never mix "locked static camera" with "fast orbit" without stating when behaviour changes.

## 4. Match Detail to Shot Size

| Shot | Put detail into | Keep motion |
|---|---|---|
| Extreme close-up | one feature, micro-expression, texture | minimal displacement |
| Close-up | eyes, breath, skin/fabric, small hand/face motion | face, shoulders, hands |
| Medium | gesture, dialogue, short moves | general purpose |
| Wide / establishing | geography, blocking, scale, weather motion | large displacement tolerated |
| Over-the-shoulder | whose shoulder, where focus rests | small |
| Aerial / overhead | simple, explicit paths | slow, readable |

Don't ask a close-up to perform full-body action — widen the shot or shrink the action.

**Vertical (9:16):** stack depth vertically, keep action readable in the narrow frame, prefer jib/vertical movement over lateral dollies.

## 5. Audio and Dialogue

LTX-2.3 generates sound with the picture, so the prompt is also a sound brief.

- **Layer it:** ambience (room tone, wind, traffic) → synced effects tied to visible events (footfalls, gate impact) → music (genre, instrument, when it enters) → speech.
- **Dialogue:** quote it exactly, name speaker, language and accent: `the old man says in Brazilian Portuguese, "Ainda não."` Keep lines short enough to fit with the action; one speaker per line is most reliable.
- **Say what's absent:** "no music", "no dialogue", "no applause". Audio defaults on; unspecified slots get filled.
- **Tie sound to timing:** "a low tone blooms only when the full cavern is revealed".
- **Silent deliverable?** `generate_audio: false` instead of prompting for silence.
- Screenplay-style layout is acceptable when dialogue, multiple beats or precise timing demand it — keep the same fundamentals.

## 6. Image-to-Video Prompting

- The image supplies appearance. Spend the prompt on **what happens next**: subject motion, environmental motion, camera, light changes, audio.
- Name the 2–3 properties that must stay stable ("her coat, hairstyle and the stage geometry remain unchanged").
- Prefer a single continuous take from the first frame unless you deliberately describe a cut away.
- Prompt motion consistent with the image's perspective — an eye-level still won't become an aerial cleanly.
- First + last frame: both images need compatible identity, geometry, lighting and orientation; describe a physically plausible path between them.

## 7. Positive Framing (native API has no negative prompt)

Describe what fills the space: "an empty platform, benches bare" instead of "no people". Locally, the negative encoder exists — use it only for failures you've actually observed.

## 8. Lighting and Look

- One primary source + compatible practicals/fill. Conflicting sources break continuity.
- Name palette, texture, lens character: "cool fluorescent key, warm desk practicals, olive and tobacco palette, fine 35mm grain".
- Style: one medium, one era, one supporting effect.

## 9. Known Weak Spots

| Weak spot | Workaround |
|---|---|
| Readable text, logos, UI | Add in post, or bake into the I2V source frame and keep it still |
| Complex/chaotic physics | Simplify the event; use a control workflow locally |
| Crowded casts | One subject; block small groups explicitly by position and wardrobe |
| Large multi-event sequences | Split into shots; extend for continuity |
| Exact on-screen text over time | Not guaranteed across frames |

## 10. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Keyword / tag soup | Lost chronology and relationships | Present-tense sentences in time order |
| Describing a still image | Little or muddy motion | Every sentence gets a verb |
| Re-describing the I2V source | Wasted budget, drift | Describe the change, not the pixels |
| Several unrelated actions | Split attention | One action + one reaction |
| Two simultaneous camera moves | Drifting framing | One move or a timed handoff |
| No landing composition | Ending wanders | State the final frame |
| Abstract emotion | Blank faces | Breath, jaw, eyes, posture, hands |
| Audio left unspecified | Random music/voices | Specify layers or state silence |
| Dialogue overload | Rushed speech, cut lines | Short quoted lines, room for action |
| Preset contradicts prose | Weak adherence, wobble | Make field and prose agree |
| Settings in the prompt text | Ignored or misread | Put them in request fields |
| Pasting prompts from other models | Underperforms | Rewrite into LTX chronology |
| 4K before blocking is approved | Expensive failures | Fast 720p/1080p first |
| Raising CFG on distilled weights | Oversaturation, artifacts | Keep CFG 1; rewrite or add image input |
| `negative_prompt` / `seed` on native API | Rejected or ignored | Wrapper/local only |
