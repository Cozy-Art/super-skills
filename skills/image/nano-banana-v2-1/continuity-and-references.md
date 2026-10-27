# Nano Banana 2.1 — Continuity & References

Nano Banana 2.1 has no seed and no identity token. Continuity is carried by **reference images** (up to 14 per request) and by the **conversation thread** (`previous_interaction_id`). Multi-turn character consistency is one of 2.1's specific improvements over Nano Banana 2 — but still QA every frame.

## 1. Reference Capacity

| Kind | Max | Typical use |
|---|---|---|
| Character references | 4 | Faces / people whose identity must hold |
| Object references | 10 | Products, props, wardrobe, vehicles, locations, style frames |
| Total | 14 | Mixed in one request |

Attach only what the shot uses — unused references add ambiguity and input cost.

## 2. Binding References: Content + Role

Google's own examples point at attachments by **what they are**, never by token: "An office group photo of these people…", "Using the attached napkin sketch as the structure and the attached fabric sample as the texture…". Do the same, and give each one a job:

```
Using the attached portrait as Maya's identity, the green bicycle photo as the
bike, and the waterfront photo as the location and light — take only the palette
and grain from the film still.
```

- **Role, then preservation list.** "Preserve the bicycle's step-through frame, tan saddle and front basket."
- **Ordinals are a tiebreaker, not syntax.** Input blocks are ordered, so "the second image" resolves; many hosting platforms (fal, Runware) teach "image 1 / image 2" and it works there. Pair it with content — "the green bicycle (image 2)" — so the binding survives reordering.
- **Scope style references:** "take nothing else from it", or its subject walks into your shot.
- **One final lighting model:** references shot in different light need one stated final direction and quality.

**Reference roster** (a working note for the person assembling the request — the prompt itself says the roles in prose):

```
1 CAST     Maya — preserve oval face, eyebrow scar, dark curls
2 PRODUCT  bottle — silhouette, cap, amber glass, exact label
3 LOCATION cottage — architecture, window placement
4 LOOK     film still — palette, grain, contrast only
```

## 3. Character Consistency Protocol

1. **Character sheet first:** neutral even light, plain backdrop, face visible; full body, face close-up, and the side/rear views the story needs.
2. Write a compact **identity block** of 3–6 visible anchors and paste it word-for-word into every prompt:
   ```
   Maya: early thirties, oval face, dark shoulder-length curls, thin scar through
   the left eyebrow, small gold stud earrings.
   ```
3. Attach the same approved sheet(s) as the character reference in every shot.
4. State what may change and what must not: "She now wears a rust suede jacket. Keep her face, scar, hair and age identical to the portrait."
5. Change **one major variable per request** — pose, location, costume or light.
6. Up to 4 characters per request; for crowds beyond that, describe extras generically.

## 4. Multi-Turn Editing (the thread)

Each follow-up sends `previous_interaction_id` and a narrow instruction:

```
Change only the jacket from navy wool to rust suede. Keep the face, pose, hands,
background, camera position and lighting unchanged.
```

- Narrow turns hold best: "Change only X; preserve A, B, C."
- After 3–4 turns, or the first sign of drift, **restart from the master** and apply every approved change in one numbered prompt.
- Changing size tier is a new render — attach the approved image and ask to recreate it at higher fidelity, preserving composition, identity, light and palette.

## 5. Style Lock

A reusable sentence pasted verbatim into every prompt of a project:

```
Style: restrained 35mm science-fiction drama — practical sets, cool green
shadows, amber utility lights, natural skin texture, fine grain, low saturation.
```

For a stronger lock, attach one approved style frame scoped to "palette, contrast and grain only". If your platform supports a system instruction, the style lock can live there (unverified for image models — confirm on your platform).

## 6. Storyboard / Multi-Shot Sequencing

1. Build masters first: character sheets, environment plates, prop/product shots.
2. Give each shot an ID, framing, action beat and its reference list.
3. **Generate every shot from the masters, not from the previous shot** — an error in frame 2 shouldn't propagate to frames 3–10.
4. Keep screen direction and eyelines consistent; say them ("running toward frame left").
5. End every prompt with the same identity block and style lock.
6. QA faces, hands, wardrobe, labels, left/right placement, geography and copy on every frame.

**Shot template:**
```
[Shot size + angle + lens]. Maya from the portrait reference [action, screen
direction] in [location from the cottage reference]. [Light, matching the
location]. [Identity block]. [Style lock]. Keep [shot-specific invariants].
```

## 7. Product and Brand Consistency

- Reference the product with clean, evenly lit shots; add the angles the composition needs.
- Quote the label wording exactly and say "preserve the label exactly as in the product reference".
- Name construction details (cap shape, seams, hardware) — they're what drift first.

## 8. Video and PDF Context

A video or PDF can be the reference for a still — poster, thumbnail, keyframe, summary infographic. Say which moment, page or content to use. Output is always a still.

## 9. Handoff to Video Models

2.1 makes no video. Approved stills are strong first/last frames or character references for an image-to-video model. Generate them with the same identity block, style lock and screen direction so the video model inherits consistent anchors.
