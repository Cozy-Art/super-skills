# FLUX 3 Video — Best Practices

Depth on prompt construction. The hard rules live in `SKILL.md`; this file covers the craft.

---

## Prose shape and ordering

FLUX 3 takes one free-text string. Order matters because the model anchors on what it reads first.

```
[Subject + action] → [Setting + light] → [Camera] → [Audio] → [Constraints]
```

Write it as connected prose, not a tag stack. Comma-separated keyword grids
("cinematic, moody, 8k, masterpiece, detailed") consistently underperform a sentence that says what is
happening.

**One primary action per shot.** "Walks in, sits, opens the ledger, begins writing" is four beats
competing for the same seconds. Pick the beat that matters, or cut to the next shot.

---

## Shot vocabulary beats thematic vocabulary

The single highest-leverage substitution in FLUX 3 prompting.

| ❌ Thematic | ✅ Shot |
|---|---|
| "cinematic and dramatic" | "handheld medium shot, slight lag on the pan" |
| "epic establishing shot" | "slow crane rise from ground level to rooftop height" |
| "moody lighting" | "single practical lamp camera-left, deep falloff into the corners" |
| "beautiful and atmospheric" | "low sun raking across the water, long shadows toward camera" |
| "intense close-up" | "tight close-up, shallow focus, eyes sharp and the background dissolved" |

Thematic words describe how you want to feel about the result. Shot words describe something the model
can execute. Every thematic adjective you replace with a camera, lens or light instruction buys you
control.

**Even a minimal camera instruction beats none.** "Locked-off wide" is a real choice. Clips written with
no camera language at all read flat and default toward a static medium shot.

---

## The three audio layers

Audio is generated with the frames, so it needs directing with the same specificity as the picture.
Prompts that mention sound only as a trailing "with ambient noise" get generic beds.

### 1. Speech

**The trigger is double quotes.** BFL: *"Quote the line in your prompt and the character says it."*

```
A presenter speaks to the lens: "Storm season is here."
```

Working rules:

- **Attribute immediately before the line.** The speaker description and the quote should be adjacent,
  so there is no ambiguity about who is talking.
- **Add a delivery note.** `low and even`, `rushed, half-swallowed`, `warm, unhurried`. This shapes the
  performance; without it you get a neutral read.
- **Budget one sentence per five seconds.** A 5s clip holds one short line comfortably. Two lines in a
  5s clip produces rushed delivery or truncation.
- **Frame the mouth if lip-sync matters.** A line delivered in a wide shot from behind gets no benefit
  from lip-sync. Pair dialogue with framing that shows the face.
- **Multilingual works.** Name the language in the prose if it isn't obvious from the line.

### 2. Effects

Discrete, motivated sounds tied to something visible.

```
boots on wet gravel, a latch turning over, fabric dragging against stone
```

Tie each effect to an on-screen cause. Effects with no visible source tend to be dropped or land at the
wrong moment.

### 3. Ambience

The continuous bed. One or two elements, not a list.

```
low wind across open moorland, distant rooks
```

Ambience is what carries across a hard cut in a multi-shot generation, so choosing it deliberately is
what makes a two-shot sequence feel like one scene.

### Ordering audio

Speech first, then effects, then ambience — foreground to background. This matches how the mix reads
and keeps the most important element from being buried behind a list of textures.

---

## In-prompt negation — the FLUX 3 exception

Most models in this catalogue punish negation. FLUX 3 endorses it.

There is no `negative_prompt` parameter, and BFL's general guidance says most FLUX models don't support
negative prompts. But BFL's own FLUX 3 Video examples use in-prompt negation deliberately, and their
troubleshooting table lists it as the fix:

```
No on-screen text, no subtitles.
No announcer delivery, no sales voice.
No music, no second voice.
```

**How to use it well:**

- **Positive description first, negation second.** Negation is a corrective, not a foundation. A prompt
  that is mostly "no X, no Y, no Z" gives the model nothing to build.
- **Reach for it when something keeps appearing.** Spurious subtitles, an unwanted music bed, a second
  voice, on-screen text — these are the documented use cases and the ones it handles well.
- **Be specific about what you're excluding.** "No announcer delivery, no sales voice" works because it
  names a performance register. "No bad audio" does not.
- **Keep it short.** Two or three exclusions at the end. A long negation list starts competing with the
  description for attention.

---

## Multi-shot in one generation

The strongest tool FLUX 3 has, and under-used. Continuity holds across a hard cut inside a single
generation — character, look, and one audio bed carrying through — which is exactly what you cannot get
across two separate generations.

```
SHOT ONE — [description]. HARD CUT. SHOT TWO — [description].
```

Practical guidance:

- **One beat per shot.** The shot structure is not an excuse to stack more action.
- **Two or three shots is realistic** inside the duration cap. Five is not.
- **Keep the ambience constant across the cut** unless the location changes — it is what makes the cut
  read as a cut rather than two clips.
- **Prefer this over two generations** whenever the shots must match. It is the only continuity
  guarantee the model offers.

---

## Image-continuation: describe the delta

When keyframes supply the frames, the images already carry their own content. Redescribing them wastes
the prompt and can fight the conditioning.

**Describe only what changes** — motion, camera, light shift, sound.

```
❌ A weathered stone gatehouse under grey sky, ivy on the left wall, a lantern
   hanging by the door. The camera pushes in slowly.

✅ Slow push in toward the door as the lantern swings and settles. Wind rises,
   then drops. Iron hinges complaining under the gust.
```

And never write *"the character from the first reference image."* There is no reference slot — see
`continuity-and-references.md`.

---

## Mistakes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Flat, static-feeling clip | No camera language | Add one concrete instruction, even "locked-off wide" |
| Generic or absent sound | Audio mentioned as a trailing clause | Write the three layers explicitly, foreground to background |
| Dialogue not spoken | Line not in double quotes | Quote it exactly; that is the documented trigger |
| Dialogue rushed or cut off | Too many words for the duration | One sentence per ~5 seconds |
| Lip-sync doesn't read | Speaker's face not in frame | Pair the line with framing that shows the mouth |
| Unwanted subtitles or on-screen text | Model's default tendency | `No on-screen text, no subtitles.` — vendor-endorsed here |
| Unwanted music bed under dialogue | Model filling silence | `No music, no second voice.` |
| Keyframes ignored or fought | Prompt redescribes the images | Describe only the motion between them |
| Character drifts between clips | Expecting cross-generation identity | There is none — use one multi-shot generation instead |
| Cluttered, unfocused result | Multiple actions stacked | One primary action per shot |

---

## Iterating

Change **one layer at a time**. If a clip is close but the camera is wrong, change only the camera
instruction and regenerate — changing camera and lighting and audio together tells you nothing about
which edit helped.

Use `draft` for this loop. It is fast and cheap, and when a take is approved, `draft_enhance` re-renders
*that same take* at full quality from the cached bundle rather than re-rolling. Exploring in draft and
enhancing once is substantially better economics than iterating at full quality.
