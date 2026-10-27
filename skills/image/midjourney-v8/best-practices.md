# Midjourney V8 — Best Practices

## 1. Detail Level: Visible Evidence Over Adjectives

V8 follows longer, more specific prompts better than V7 — and literalizes more of what you write. Every phrase should name something the camera would see.

| Weak | Better |
|---|---|
| `cinematic` | `low-angle 35mm still, hard cyan backlight, amber practicals in the background` |
| `beautiful woman in city` | `a middle-aged bicycle courier in a yellow rain shell pauses beneath a red traffic signal` |
| `highly detailed` | `rain beads on waxed cotton, chipped enamel on the handlebars` |
| `dramatic lighting` | `single bare bulb overhead, hard shadows falling down the stairwell` |
| `vintage` | `faded mid-1970s colour-negative film, cool green shadows, visible grain` |
| `professional product shot` | `three-quarter product angle, narrow white strip light along the bezel, graduated gray backdrop` |

Prioritise: distinctive subject traits · spatial relationships (left/right, foreground/background, facing direction) · one clear action · shot size before lens jargon · one dominant light source · a 2–4 colour palette · materials and surface behaviour · delivery composition (negative space for copy, mobile-safe placement).

## 2. Hierarchy and Priority (no `::` in V8)

Multi-prompt weights are incompatible with V8.1/V8.2. Priority comes from:

1. **Order** — the subject and its defining traits first.
2. **Specificity** — the more concretely something is described, the more it wins.
3. **Repetition of nothing** — don't restate the subject in synonyms; it muddies, not strengthens.
4. **Dials** — `--raw` + lower `--s` for literal control; higher `--s` / `--p` for aesthetic.

## 3. Negatives: `--no`, Not Prose

`--no cars text crowds` is a parameter. Writing "without cars" or "don't show text" in the description can put cars and text *into* the image.

- Name visible categories: `--no hands wrists extra watches logos`.
- Keep the list short and specific; don't paste generic defect lists ("bad anatomy, blurry, deformed").
- Better still, describe what fills the space: "an empty platform", "clean unmarked label".

## 4. Composition by Shot Type

- **Close-up:** feature detail, eye direction, expression; simplify the background.
- **Medium portrait:** torso, hands, action; 50–85mm language.
- **Wide establishing:** geography, scale, atmosphere, *where the subject sits in frame*.
- **Layered depth:** one foreground occluder, midground subject, background anchor.
- **Negative space:** say which side and why — "subject on the right third, clean fog on the left for a title".
- **Symmetry:** state the central axis and the repeating architecture.
- **Top-down:** "overhead orthographic view, minimal perspective" to kill unwanted perspective.
- **Action freeze:** peak instant, limb/prop direction, shutter look, debris path, where blur is and isn't.
- **Wide ratios (21:9):** assign left, centre and right or you get dead space.
- **Vertical (9:16):** stack the depth — sky, subject, ground — and keep the subject mobile-safe.

Validate unusual compositions at 2:3 / 3:2 / 16:9 before pushing to extreme ratios.

## 5. Camera Language for Stills

V8 stills have no camera-motion controls. Viewpoint and optics are written into the prompt; motion words produce the *look* of motion.

```
extreme close-up · eye level · low-angle hero · overhead bird's-eye · over-the-shoulder
24mm wide · 35mm · 50mm natural · 85mm portrait · 200mm compressed telephoto
shallow depth of field · deep focus · foreground occlusion · dutch angle
panning motion blur · long-exposure light trails · tracking-shot composition
```

Pick **one** viewpoint and **one** lens behaviour. "Composition designed for a slow dolly out" is useful when the still will be animated.

## 6. Typography

- Quote exact words: `the title "SIGNAL ZERO" in condensed uppercase lettering at the top`.
- One headline + one short line beats a paragraph. Each extra label lowers reliability.
- State placement, type character, hierarchy and colour.
- Use `--raw` and moderate `--s` (100–250) for legible layouts; high stylize decorates letterforms.
- Fix stray glyphs with an Edit inpaint rather than re-rolling the whole poster.
- Check text at `--hd` before delivery.

## 7. Style Systems — Use One at a Time

| System | Carries | Best for |
|---|---|---|
| `--sref URL` | colour, medium, texture, lighting of an image | matching an existing frame |
| `--sref code` / `random` | a stored style | discovery, house looks |
| `--p` profile | your learned taste from ratings | personal aesthetic |
| `--p moodboard-code` | a curated image set | project look |
| Prose style block | whatever you describe | portability, fine control |

- Stacking sref + profile + moodboard at high strength produces mush. Pick one, then tune `--sw` (sref) or `--s` (profile).
- srefs do not copy people or objects — use the Edit model for identity.
- `--sw` and `--sv` don't combine with moodboards.
- The Edit model may need extra prompt direction to honour moodboards/srefs.
- Prefer describing visual traits over naming living artists.

## 8. Image Prompts vs Edit References

- **Image prompt** (URL first, `--iw 0–3`): borrows composition, content and colour loosely. Inspiration, not copying.
- **Edit reference** (V8.2 Edit, up to 4): carries a specific person, object or scene into the result, or edits it directly.

If the user says "keep *this* character / product", it's an Edit job.

## 9. Edit Instructions

Three-part pattern:
```
Change: replace the paper cup with a clear glass of iced tea.
Keep: her face, hairstyle, coat, pose, framing and window light.
Look: photoreal condensation, pale amber tea, reflections consistent with the window.
```
- One conceptual change per pass. Targeted (selected-region) edits only change selected pixels, so repeated local edits don't degrade the rest.
- For outpaint, describe what occupies the new canvas, not the existing image.

## 10. Prompt Length

No official V8 maximum. Practical: simple 10–30 words · editorial 40–90 · complex 80–150 where every phrase has a job. Keep descriptive text < ~1,024 characters for API portability (resellers enforce it upstream; Edit/Remix prompts allow more). 70 precise words beat 250 words of synonyms.

## 11. Common Mistakes

| Mistake | Result | Fix |
|---|---|---|
| Adjective pile | Generic, unfocused image | Subject, action, space, light, material |
| Conflicting mediums | Muddy compromise | One medium + one supporting influence |
| Lens shopping list | Confused perspective | One viewpoint, one lens |
| "no X" in prose | X appears | `--no X` or describe what fills the space |
| `--q 2` / `--q 4` on V8 | Incompatible | Remove; use `--hd` for finals |
| `--oref` / `--cref` on V8 | Unsupported | Edit model references |
| `::` weights | Incompatible on V8 | Order + specificity |
| High `--s`, `--c`, `--w` together | Prompt adherence collapses | Raise one dial at a time |
| Seed as identity lock | Face drifts with any prompt change | Edit references + identity clause |
| Parameters mid-prompt or with commas | Parse errors / ignored | All params last, no punctuation |
| Decimal aspect (`1.85:1`) | Invalid | Integers (`37:20`) |
| `--ar 21:9 --hd` assumptions beyond 4:1 | Rejected / clamped | HD caps at 4:1 |
| Long paragraphs of on-image text | Garbled glyphs | Short quoted copy, fix with Edit |
| Several style systems at max | Incoherent look | One system, tuned |
| Image-gen params on a video job | Stripped / ignored | Only `--motion --raw --loop --end --bs` |
| Re-describing the whole scene in a motion prompt | Drift from the start frame | Describe only what moves |
