# Kling 4.0 — Best Practices

## 1. Write for Control, Not Length

Kling 4.0 takes up to 8,000 tokens, and its guide says simple prompts work ("An old man ranting about AI." is an official example) — the model fills in story, blocking and camera. When you *do* describe something clearly and in detail, it follows it without adding its own interpretation. So:

- Short prompt → Kling directs. Fine for ideation.
- Detailed prompt → you direct. Every added line should pin a controllable variable: identity, prop, spatial position, camera path, light direction, sound timing.
- Use descriptive, concrete language. Avoid abstract terms ("epic", "premium", "cinematic") unless you also say what produces them: lens feel, light direction, texture, movement, composition.

## 2. The Four-Part Template

Kling's recommended Omni Reference structure:

```
[Asset roles]
@Image1 defines ___; preserve its ___.
@Image2 defines ___; preserve its ___. Reference the ___ of @Video1.
[Overall settings]
Scene and texture: ___; visual style: ___; camera tone: ___.
[Sequence of events]
0–X s: ___ (visuals + action + emotion)
X–Y s: ___ (camera movement + additional details)
Y s–end: ___ (closing shot)
[Audio]
Dialogue/voice-over + ambient sounds + music + sound effects
```

The bracketed headings are organisational — you can keep them or write the sections as plain paragraphs. The order matters more than the labels.

## 3. Asset Roles (the highest-leverage line)

- One sentence per asset: what it **defines** and what to **preserve**. `@Image1 defines the courier's face, hair and green rain jacket; preserve them exactly.`
- Say what an asset must **not** contribute. Video references especially: `@Video1 supplies only the running rhythm and landing mechanics. Do not inherit its actor or location.` Kling notes that explicit exclusions improve results.
- Use the right verb for the job: *defines / preserve* (identity, product), *reference the composition of* (framing), *use as the reference for camera movements and shot pacing* (camera), *for the fight choreography and attack timing* (motion), *first frame / last frame* (Keyframes).
- Multi-character: `Reference the facial features of the characters in @Image1, @Image2, and @Image3, keeping them strictly consistent.` Then refer to each by a short description in the action so it's clear who does what.
- Numbering follows upload order. Write the prompt after you know the order, and keep that order in the settings line.

## 4. Sequence of Events

- Chronological, present tense, one beat per line. Each beat: who moves, how, where they end up.
- Timecodes (`0–4s:`) are endorsed by Kling's template and its storyboard examples (`Shot 1 — 0.00–4.00s: …`). Make them sum to the duration you set; don't timecode past the end.
- Action that must be physically believable: **start position → obstacle → contact point → landing → camera follow-through.**
- Character beats: emotional turn, eye-line shift, a hand action, a restrained camera move — not mood labels.
- Long clips (20–30 s) need causal progression: each beat changes something (position, information, light, emotion). A weak concept stretched to 30 s drifts; shorten it or add beats.

## 5. Continuous Take vs. Multi-Shot

Multi-shot is **on by default** — Kling splits shots and organises pacing itself.

| Intent | Write |
|---|---|
| One take | `One continuous shot with no cuts, angle changes, or scene changes.` / `one continuous master shot with no visible cuts` |
| Controlled cuts | Labelled shots with times and shot sizes: `Shot 1 (0–6s): Wide shot… Shot 2 (6–12s): Side-tracking medium shot…` and say "hard cut" where you want one |
| Let Kling decide | Describe the sequence; omit shot labels |

Never ask for a continuous move and imply cuts in the same prompt.

## 6. Camera

- Shot size + angle + **one** movement per shot + where it lands: `Begin at tabletop height, move in a slow half-orbit from the lamp's left side to its front, then settle into a symmetrical product composition.`
- Natural language only — no numeric camera controls are documented for 4.0. For a precise path, supply a camera reference video (`@Video1 as the reference for camera movements and shot pacing`).
- Wide formats (21:9): anchor geometry, horizon and light direction so the move has something stable to travel across.
- Restraint reads as quality in close-ups: slow push-in, slight drift, locked-off.

## 7. Light, Style, Texture

- Name the source and direction: `cool window light from frame-left; a warm desk lamp lights the envelope`.
- Style as concrete material: `rendered as stitched felt`, `16mm grain, lifted blacks`, `wet asphalt reflecting sodium light`.
- Style transitions: say the transformation changes **materials, not identity**, and list what stays (markings, pose, geometry, gaze).

## 8. Audio, Stereo and Dialogue

- Give audio its own section and separate the layers: dialogue → ambience → effects → music.
- Dialogue in quotation marks, **in the language it should be spoken**. Describe the voice: age, tone, speaking speed, emotion. Attribute each line to a visibly distinct speaker by description (`the older man at the counter says…`).
- Accents/dialects: name them (`in a British accent`, `in Cantonese`).
- Stereo: place sources — `wind crossing from left to right`, `a train passes off frame-right`, `footsteps approach from behind camera`.
- Sync effects to visible events (`the parcel touches the wooden bench`).
- If you want no score, say `no background music`; Kling lists it as one of the two negatives worth writing.

## 9. On-Screen Text and Subtitles

Kling 4.0 renders multilingual text, emoji and logos that stay stable during camera moves.
- Quote exact copy and say where it sits: `a neon sign above the door reads "OPEN LATE" in uppercase`.
- Subtitles on purpose: give font size, alignment, display duration and sync with dialogue.
- Subtitles not wanted: `No subtitles.` (the other necessary negative). Add `no text overlays, logos or watermarks` if the scene invites them.

## 10. Negative Instructions

Kling's guide: negative instructions can increase errors; only **no subtitles** and **no background music** are truly necessary. So:
- Don't paste Kling 3.x negative lists ("smiling, extra fingers, morphing…").
- Turn other exclusions into positive description (`an empty platform, benches bare` rather than "no people").
- Exception that *helps*: exclusions about what a reference must not contribute ("do not inherit its location").

## 11. Editing Prompts

- Start with **`Edit @Video1.`** — "Reference @Video1" alone may be treated as reference-based generation.
- One scoped change per pass: add, remove, replace (characters, environment, objects), restyle, or change camera angle/movement.
- Say when it applies if it isn't the whole clip (`When the box is opened again at the end, add @Element1 lying inside asleep.`).
- Close with preservation: `Keep everything else unchanged.` or `Preserve the original composition, shots, and actions.`

## 12. Common Mistakes

| Mistake | Fix |
|---|---|
| References attached but never mentioned | One role line per asset, numbered by upload order |
| `@Video1` copies the actor/location you didn't want | State what to take *and* "do not inherit its actor or location" |
| "Reference @Video1, change the sky" | `Edit @Video1. Replace the sky with… Keep everything else unchanged.` |
| Edit changes unrelated parts | Narrow the change, add timing, add a preserve line |
| "Make it premium and cinematic" | Lens feel, light direction, texture, movement, composition |
| Unwanted cuts in a "single take" | `one continuous shot with no cuts, angle changes, or scene changes` |
| Continuous move + "cut to" in one prompt | Pick one; use labelled shots for cuts |
| 30 s clip feels aimless | Add beats with cause and effect, or shorten |
| Action breaks physically | Start → obstacle → contact → landing; or a motion reference / keyframes |
| Timecodes don't add up to the duration | Re-time beats to the duration you set |
| Long Kling 3.x negative list | Keep only "no subtitles" / "no background music" as needed |
| `@Character says, "…"` (3.x habit) | Describe the speaker; quote the line; `@` is now for assets |
| Duration / aspect written in the prompt that disagrees with the UI | Settings line only; prose must agree |
| Reference assets in Keyframes mode | Switch to Omni Reference, or carry identity in the keyframes |
| Wrong-language dialogue | Write the line in the language to be spoken |
