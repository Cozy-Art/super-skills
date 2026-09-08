# Gemini Omni Flash — Best Practices

Depth on prompt construction. The hard rules live in `SKILL.md`.

---

## Decide first: one take or a sequence?

Omni Flash defaults to **an edited sequence of several shots**, not a continuous take. Inside a 3–10
second clip that means very short shots — three or four cuts in eight seconds.

Neither behaviour is wrong; the mistake is not choosing.

**For a single continuous take, say so explicitly:**

```
A single continuous take, no cuts.
```

**For a sequence, shape it rather than accepting the model's choices** — use timecodes.

This is the first decision on every prompt for this model, and the one most often skipped.

---

## The six descriptive dimensions

Google's guidance implies a working framework. Omitting a dimension lets the model default, and its
defaults are strong.

| Dimension | Example |
|---|---|
| **Shot framing / camera motion** | `low-angle medium shot, slow push in` |
| **Style** | `documentary realism, handheld` |
| **Lighting** | `overcast north light, deep falloff` |
| **Location** | `a disused railway platform` |
| **Action** | `she sets the case down and does not pick it up again` |
| **On-screen text** | usually: `No on-screen text.` |

**Longer, specific prompts outperform short ones here** — up to the point of internal contradiction or
redundancy. This differs from models where terseness wins. Cover the six dimensions; don't pad beyond
them.

**On the sixth:** text rendering is a stated limitation on the model card. If legible on-screen type
matters, this is the wrong model. Usually the right instruction is to suppress it.

---

## Timecode blocking

The way to control a multi-shot result rather than accepting whatever cut the model chooses.

```
[0-3s] Wide establishing shot of the platform, rain blowing across it.
[3-6s] Tight on the departure board as the letters roll over.
[6-10s] The board settles. Platform lights come up.
```

**Rules:**

- **Keep ranges continuous.** Gaps leave the model improvising
- **Stay inside the duration.** Three beats is comfortable in 10 seconds; four is pushing it. Two beats
  is right for a 6-second clip
- **One beat per range.** These shots are 2–4 seconds; they hold one idea each
- Natural-language timing ("after two seconds," "at the halfway point") also works, but bracketed
  ranges are more reliable with more than one beat

---

## Editing — brevity is the technique

Conversational editing is this model's real strength, and the prompts are shorter than people expect.

**Describe only the change.**

```
✅ Make it night.
✅ Slow the camera move down.
✅ Remove the second character.

❌ The same woman in the same red coat walking down the same wet street, but
   now it is night-time, with the streetlights on and the sky fully dark, and
   the same slow push-in as before…
```

Google's guidance is explicit that simple edit instructions outperform verbose ones. Restating the
scene gives the model a chance to reinterpret it.

**Preserve explicitly when an edit risks collateral change:**

```
Make it night. Keep everything else the same.
```

That is Google's own documented preserve instruction and it is worth using by default on anything but
the most trivial edit.

**Chain edits one change at a time.** Three changes in one turn produces three interpretations at once.
Four short turns beat one long one, and each turn is cheap relative to a regeneration.

**Retention gates editing.** If a clip was generated without being stored, it cannot be edited in a
later turn. See `parameters.md` — the fastest configuration silently disables this.

---

## Audio

Native and synchronized. Write it as prose alongside the picture — ambience, effects, texture.

```
Rain on a tin canopy, the mechanical clatter of split-flap letters, a
distant announcement too muffled to parse.
```

**Scripted dialogue is not available.** There is no documented way to put specific words in a
character's mouth, voice editing is unsupported, and the model card states speech-changing capability
is currently restricted.

`No dialogue.` works as a suppression instruction, and is often the right call — an unscripted vocal
performance under a scene you didn't write lines for is usually worse than silence.

For scenes needing specific spoken words, generate the audio separately and lay it against this
picture, or route elsewhere.

---

## Negation

**No negative-prompt field exists** — Google lists negative-prompt parameters among the explicitly
unsupported inference controls. Exclusions go in the prompt text, which Google's own guidance directs.

```
No dialogue.
No on-screen text.
No cuts.
```

Positive description first. Keep exclusions short, specific and at the end.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Got a cut sequence, wanted one shot | The default is multi-shot | `A single continuous take, no cuts.` |
| Shots feel rushed | Too many beats for the duration | Three beats max in 10 s; two in 6 s |
| Model improvises between beats | Gap between timecode ranges | Keep ranges continuous |
| Edit changed more than asked | No preserve instruction | Add `Keep everything else the same.` |
| Edit reinterpreted the scene | Edit prompt restated the whole scene | Describe only the change |
| Clip cannot be edited afterwards | Result was not stored | Retention must be on — see `parameters.md` |
| Video reference ignored | Video refs are accepted by the schema but not processed | Documented as not working; don't plan around it |
| Audio reference rejected | Audio uploads unsupported | Not available in the current version |
| Unwanted spoken words | Native audio filling silence | `No dialogue.` |
| Illegible on-screen text | Stated model limitation | Suppress it, or route elsewhere |
| Result flat and default-looking | Descriptive dimensions omitted | Cover framing, style, lighting, location, action |
| Regional failure editing footage | Uploaded-video editing is restricted in EEA / CH / UK | Edit model-generated clips instead |

---

## Iterating

**This is the model where iteration is the workflow**, not a fallback. Generate something roughly
right, then converge across turns with short single-change edits. Each turn is cheap, and the
conversational chain preserves what you have already approved.

**Change one thing per turn.** The whole advantage of conversational editing disappears if a turn
contains three changes — you lose the ability to attribute the result to any one of them.

**Budget realistically.** At roughly $0.10 per second of output, a 10-second clip is about $1, and an
edit turn regenerates the clip. A ten-turn refinement session on a 10-second piece is around $10.
Cheap for the control, but not free — worth knowing before an open-ended session.
