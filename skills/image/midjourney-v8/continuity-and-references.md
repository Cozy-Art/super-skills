# Midjourney V8 — Continuity & References

In V8.1/V8.2 there is no Omni Reference and no Character Reference. Continuity is carried by **(1) the V8.2 Edit model's image references, (2) verbatim text blocks, and (3) one stable style system.** Seeds only help compare prompt changes.

## 1. Choose the Reference Tool by Intent

| Goal | Tool |
|---|---|
| Similar composition / content / colour | Image prompt (URL first, `--iw`) |
| Same overall look | `--sref` URL or code, `--sw` |
| Personal or project aesthetic | `--p` profile or moodboard |
| Same person / object / product in a new image | V8.2 Edit with that image as a reference (up to 4) |
| Change one region | Edit → inpaint (selected pixels only) |
| Extend the frame | Edit → outpaint / Pan / Zoom Out |
| Rebuild surfaces, keep structure | Edit (replaces Retexture) |
| Reuse a past job | Lightbox **Use** buttons: as Image Prompt, as Style Reference, or copy prompt |
| Animate an exact image | Video start frame |

Need V7 Omni Reference specifically? It only works with `--v 7` — that means leaving V8.

## 2. Housekeeping

- Keep a project log per keeper: prompt, version, every parameter, sref/profile/moodboard codes, seed, attached references (in order) and parent job ID.
- Download originals; keep folders `identity/`, `wardrobe/`, `locations/`, `style/`, `approved-shots/`.
- Host references at stable public URLs for Discord (`--sref`, `--edit`, `--end`, image prompts all need reachable URLs).
- Archive V7 originals before editing them in V8.2 — Edit can reinterpret structure and style.

## 3. Character Consistency Protocol

1. **Write an identity clause** and never paraphrase it:
   ```
   a 32-year-old Afro-Latina starship engineer, heart-shaped face, warm brown skin,
   close-cropped black curls, small scar through her right eyebrow, dark brown eyes,
   cobalt pressure suit with an orange triangular shoulder patch
   ```
2. **Generate an identity master:** clean, unobstructed face, signature wardrobe, even light, plain backdrop, `--ar 4:5 --raw --s 75 --c 0`.
3. Optional: a turnaround/reference sheet (front, three-quarter, profile, full body) — then crop single views to use as references.
4. **For every new shot:** open Edit, attach the identity master (and a full-body or wardrobe ref if needed — max 4 total), paste the identity clause, then describe the new pose/scene.
5. **Say what may change and what must stay:** "She now kneels by the reactor. Keep her face, scar, hair and suit exactly."
6. Change **one** dimension per shot: pose, lens, wardrobe or environment.
7. Keep `--c 0–5`, `--w 0`, moderate `--s`, same style system and aspect family.
8. Correct drift (hands, patch, scar side) with inpaint — don't re-roll the whole frame.

**Reference slot roles (max 4):**

| Slot | Role |
|---|---|
| 1 | Identity master (face + hair) |
| 2 | Full body / wardrobe |
| 3 | Location or previous approved shot |
| 4 | Prop or second character |

State each role in the prompt ("the woman from the first reference, the jacket from the second"). Ordering semantics beyond "up to 4" aren't documented — naming roles explicitly is the safe habit.

## 4. Style Lock

A prose block pasted identically into every prompt:
```
restrained 1970s political-thriller photography, 40mm lens, deep focus, cool fluorescent
key with warm practicals, olive, tobacco and cream palette, low saturation, fine 35mm grain
```
Then add **one** of: an sref set (same URLs/codes, same `--sw`), a profile, or a moodboard. Keep `--s` constant across the sequence. V7 srefs, moodboards and profiles carry into V8; re-check profiles because V8.2's taste model changed.

## 5. Multi-Shot / Storyboard Sequencing

1. Define the bible: identity clause(s), wardrobe state, prop states, time of day, palette, aspect ratio, lens family, style lock.
2. Approve one establishing frame per location and one identity master per character.
3. Generate **one shot per prompt** — a single still can't hold sequential beats.
4. Write screen direction explicitly: "moving left to right", "looking frame left".
5. Repeat location anchors: window count, door colour, major prop placement.
6. When the next frame must inherit visual facts, attach the previous approved shot as an Edit reference.
7. Inpaint continuity errors (hands, props, wardrobe) instead of regenerating.
8. Keep the whole sequence on one version (`--v 8.2`) — mixing versions changes look.

**Shot template:**
```
[shot size, angle, lens], [IDENTITY CLAUSE] [action, screen direction], in [location anchors],
[light matching the establishing frame], [STYLE LOCK] --ar 16:9 --raw --s 75 --c 0 --v 8.2
```
Settings line lists the attached references in order with roles.

## 6. Seeds

- `--seed N` (0–4294967295) fixes the starting noise; V8 seed reruns are ~99% identical.
- Use it to A/B a **single** wording change. Any prompt edit changes the image; it is not a character ID.
- `--w` reduces seed stability. Seeds don't carry across versions.
- "Run batch as HD" reruns an SD job's seed-locked prompt at 2K — the easiest way to keep a draft's composition in HD.

## 7. Variation Discipline

- Vary (Subtle/Strong) and Remix from a keeper rather than re-rolling from text.
- Branch every new shot from the cleanest master, not a long chain of edits.
- Pan / Zoom Out / Vary Region downscale HD to SD — upscale afterwards.

## 8. Handoff to Video

- Animate only approved keyframes. Image-gen parameters are stripped; srefs, image prompts and Edit references don't apply to video.
- Motion prompt describes **only change** from the start frame: subject action, environment motion, camera move.
- Continuity tools: `--end URL` lands the clip on a chosen frame (e.g. the next shot's opening keyframe); `--loop` returns to the start frame; Extend (+4 s ×4, 21 s max) continues the same take — Extend Manual lets you redirect the action.
- Start `--motion low --raw --bs 1`; go High only for genuinely large movement and accept more artifacts.
- Keep matching aspect ratios between keyframes so SD/HD video dimensions line up across a sequence.
