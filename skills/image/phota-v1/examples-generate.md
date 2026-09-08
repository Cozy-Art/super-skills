# Phota — Generate Mode Examples

Examples for creating new photographs from text prompts with identity-preserving profile references. Each example demonstrates the photographer's brief approach — lighting, lens, framing, expression, setting — with zero words spent describing the person's appearance.

**Critical rule:** `[[profile_id]]` carries identity. Never describe what the person looks like.

**Canonical Projects (adapted for portrait photography context):**
- 🎬 **Shadows of Ashford** — 1940s noir: detective character portraits
- 🚀 **Stellar Drift** — Sci-fi: astronaut character portraits and BTS stills
- 🎵 **Neon Pulse** — Music video: performer portraits and promo shots
- 🌸 **Aurelia** — Luxury brand: model portraits for fragrance campaign
- ⚔️ **Iron Crown** — Dark fantasy: character portraits and cast photos
- 🌊 **Forgotten Waters** — Documentary: subject portraits of fishermen

---

## PROFESSIONAL HEADSHOTS

### Example 1: Corporate Headshot — Clean Studio (Universal)
```
Prompt: Professional studio headshot of [[profile_id_1]], chest up. 
Clean neutral gray background. Soft key light from upper left, subtle 
rim light separating hair from background. Natural skin texture, 
realistic eye detail. Confident expression, direct gaze at camera, 
slight natural smile. 85mm lens look, shallow depth of field, 
premium editorial finish. Photoreal, no plastic smoothing.

Mode: Generate
Resolution: 4K
Aspect Ratio: 3:4
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: The universal professional headshot. 85mm provides 
classic portrait compression. Key+rim two-light setup is standard 
corporate. "No plastic smoothing" prevents AI beautification. 
Generate 4 variations to select the best expression capture.
```

---

### Example 2: Creative Noir Headshot (Shadows of Ashford)
```
Prompt: Artistic noir studio headshot of [[profile_id_1]], chest up. 
Introspective expression, gaze directed slightly off-camera, subtle 
three-quarter head tilt. Single motivated source light from camera 
right — strong chiaroscuro, deep shadow fill on left side of face. 
Background: dark studio, out-of-focus warm practical light in far 
corner. 85mm f/1.4 equivalent look, shallow depth of field, high 
contrast black-and-white, silver gelatin print aesthetic. Film grain, 
realistic skin texture, preserved hair detail. Photoreal, no 
over-retouching.

Mode: Generate
Resolution: 4K
Aspect Ratio: 3:4
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Single-source chiaroscuro creates the noir mood. 
"Silver gelatin print aesthetic" anchors the black-and-white 
rendering to a specific photographic process (not generic B&W). 
Off-camera gaze + head tilt adds character without risking identity 
drift. The warm practical light in the background adds depth to the 
otherwise dark environment.
```

---

### Example 3: LinkedIn Professional — Environmental (Universal)
```
Prompt: Professional environmental portrait of [[profile_id_1]], 
three-quarter length, standing in a modern office with glass walls 
and blurred colleagues in background. Warm natural window light 
from the left, supplemented by soft overhead office lighting. 
Approachable, genuine smile with relaxed shoulders. Business casual 
attire visible. 50mm lens feel, moderate depth of field showing 
office context. Clean, contemporary corporate photography. Photoreal.

Mode: Generate
Resolution: 4K
Aspect Ratio: 1:1
Num Images: 4
Output Format: jpeg
Profiles Referenced: [profile_id_1]

Director's Notes: Environmental portrait with office context — 50mm 
gives wider view than 85mm to include setting. Square format for 
LinkedIn profile image. "Blurred colleagues" adds workplace energy 
without competing subjects. "Approachable, genuine smile" is more 
specific than "friendly" and produces better expressions.
```

---

## CREATIVE PORTRAITS

### Example 4: Astronaut Cast Portrait (Stellar Drift)
```
Prompt: Cinematic character portrait of [[profile_id_1]], waist up, 
wearing a space suit (helmet off, held under one arm). Standing against 
a dark industrial background with subtle blue practical lights. 
Confident, resolute expression, looking directly at camera. Hard 
key light from upper left creating defined shadows on the face, 
cool blue fill from the right. ARRI Alexa color science, 100mm 
lens feel, extremely shallow depth of field. Cinematic science 
fiction promotional portrait. Photoreal, detailed skin texture.

Mode: Generate
Resolution: 4K
Aspect Ratio: 16:9
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Cast promotional portrait — the type you see on 
movie posters and press kits. ARRI Alexa reference provides cinematic 
color rendering. 100mm telephoto compression flatters the face while 
isolating from the background. Hard key light creates the dramatic 
contrast expected in sci-fi character portraiture.
```

---

### Example 5: Musician Promo — Neon Lit (Neon Pulse)
```
Prompt: Music industry promotional portrait of [[profile_id_1]], 
chest up, leaning against a brick wall in an urban alley. Hot pink 
neon light from a sign above camera right casting colored light 
on one side of the face, cool cyan ambient from the opposite side. 
Confident, magnetic expression with slight knowing smile. 
CineStill 800T film look with halation glow around the neon 
highlights. 35mm lens, moderate depth of field showing alley 
context. Gritty, urban, electric. Photoreal.

Mode: Generate
Resolution: 4K
Aspect Ratio: 9:16
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Portrait orientation (9:16) for social media / 
streaming platform use. CineStill 800T provides authentic halation 
around neon sources. Dual-color lighting (pink + cyan) creates the 
signature neon aesthetic. 35mm is wider than typical portrait lens — 
includes environmental context for the "urban musician" narrative.
```

---

### Example 6: Fantasy Character Portrait (Iron Crown)
```
Prompt: Epic fantasy character portrait of [[profile_id_1]], chest up, 
wearing medieval armor and fur cloak. Battle-weary but resolute 
expression, direct forward gaze. Warm torchlight from the lower 
left casting upward shadows, cold blue rim light from behind 
separating the subject from a dark stone wall background. 
Oil painting quality with visible texture but photorealistic face. 
85mm lens feel, shallow depth of field. Dark, dramatic, epic. 
Photoreal face and skin, painterly treatment on armor and setting.

Mode: Generate
Resolution: 4K
Aspect Ratio: 3:4
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Hybrid approach — photorealistic face preservation 
with painterly treatment on costume and setting. This leverages 
Phota's strength (face fidelity) while allowing artistic freedom 
on everything else. Torchlight from below is classic fantasy 
portrait lighting. Cold rim light prevents the subject from 
merging with the dark background.
```

---

## LUXURY BRAND / COMMERCIAL

### Example 7: Fragrance Campaign Portrait (Aurelia)
```
Prompt: Luxury editorial portrait of [[profile_id_1]], close-up 
from shoulders, three-quarter head angle turned slightly left. 
Serene, elegant expression with lips slightly parted, eyes 
looking past camera. Soft beauty lighting with large key light 
directly above camera (butterfly/Paramount setup), subtle warm 
fill from below. Golden bokeh highlights scattered in background. 
Medium format feel, Hasselblad X2D rendering quality. Warm amber 
and ivory color palette. Skin texture preserved, editorial 
beauty retouching level (not plastic). Luxury fragrance campaign 
quality.

Mode: Generate
Resolution: 4K
Aspect Ratio: 4:3
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Butterfly/Paramount lighting is the classic beauty 
setup — flattering on all face shapes, creates the signature nose 
shadow. Medium format reference produces the shallow DOF and skin 
rendering quality expected in luxury advertising. "Editorial beauty 
retouching level (not plastic)" walks the line between polished 
and natural.
```

---

### Example 8: Behind-the-Scenes Production Still (Stellar Drift)
```
Prompt: Behind-the-scenes production photograph of [[profile_id_1]], 
candid three-quarter length, sitting in a director's chair on a 
film set with lighting rigs and crew visible in the blurred 
background. Relaxed, natural smile, looking slightly off-camera 
as if mid-conversation. Available light from set practicals — 
mixed color temperature, slightly warm. Documentary/BTS photography 
style, Leica M10 with 35mm Summilux feel. Authentic, unposed, 
photojournalistic. Photoreal, no post-processing.

Mode: Generate
Resolution: 1K
Aspect Ratio: 3:2
Num Images: 4
Output Format: jpeg
Profiles Referenced: [profile_id_1]

Director's Notes: BTS photography demands the opposite of studio 
perfection — it's candid, available-light, and authentic. Leica M10 
reference provides documentary authority. 35mm is a classic 
photojournalist focal length. "No post-processing" fights any 
tendency toward polished commercial output. JPEG output for 
quick social media publishing.
```

---

## DOCUMENTARY / ENVIRONMENTAL

### Example 9: Fisherman Environmental Portrait (Forgotten Waters)
```
Prompt: Documentary environmental portrait of [[profile_id_1]], 
three-quarter length, standing on cracked dry earth where a lake 
once was, a weathered fishing boat visible behind. Overcast 
morning, soft diffused light with no harsh shadows. Weathered, 
honest expression, looking directly at camera with quiet dignity. 
Leica Q3 with 28mm lens feel, deep focus showing environmental 
context. Muted warm earth-tone palette. Raw, unretouched, 
documentary photography. No post-processing, no color grading. 
Photoreal.

Mode: Generate
Resolution: 4K
Aspect Ratio: 3:2
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Documentary portrait — the person's identity is 
preserved via profile, but the creative direction is purely 
documentary: overcast light, 28mm environmental, unretouched. 
"Quiet dignity" is a specific expression cue that works better 
than "serious" or "sad." The environmental context (cracked earth, 
boat) tells the story without additional narration.
```

---

## MULTI-PERSON PORTRAITS

### Example 10: Two-Person Cast Portrait (Shadows of Ashford)
```
Prompt: Film noir two-person portrait of [[profile_id_1]] and 
[[profile_id_2]], both chest up. [[profile_id_1]] stands slightly 
in front, three-quarter turn, looking at camera with suspicion. 
[[profile_id_2]] stands behind and to the right, partially in 
shadow, looking past [[profile_id_1]] with a calculating expression. 
Single harsh light from upper left creating deep shadows. High 
contrast black and white, pushed Tri-X 400 grain. 50mm lens, 
moderate depth with both faces sharp. Classic noir character 
portrait, dramatic and tense. Photoreal faces.

Mode: Generate
Resolution: 4K
Aspect Ratio: 16:9
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1, profile_id_2]

Director's Notes: Multi-profile generation — both identities 
preserved simultaneously. Spatial relationship (one in front, one 
behind) creates narrative hierarchy. Different expressions for 
each character (suspicion vs calculating) establish character 
dynamic. Single harsh light source creates the noir aesthetic 
while ensuring both faces are recognizable.
```

---

### Example 11: Family/Team Group Portrait (Universal)
```
Prompt: Warm group portrait of [[profile_id_1]] and [[profile_id_2]], 
three-quarter length, standing side by side in a sunlit outdoor 
garden setting. Both looking at camera with genuine, relaxed 
smiles. Soft golden hour light from behind and to the left, 
creating warm rim light on hair and shoulders, with a soft 
reflector fill from the front. Lush green garden bokeh in 
background. 85mm lens feel, shallow depth of field with both 
faces in sharp focus. Natural, joyful, editorial family 
photography quality. Photoreal, natural skin.

Mode: Generate
Resolution: 4K
Aspect Ratio: 4:3
Num Images: 4
Output Format: jpeg
Profiles Referenced: [profile_id_1, profile_id_2]

Director's Notes: Classic outdoor two-person portrait. Golden hour 
backlight + reflector fill is the standard recipe for flattering 
natural light portraits. Both faces must be sharp — "both faces 
in sharp focus" prevents the model from putting one person out 
of focus. 85mm keeps compression flattering for both subjects.
```

---

## PET PORTRAITS

### Example 12: Pet Portrait (Universal)
```
Prompt: Professional pet portrait of [[pet_profile_id]], chest-level 
angle looking directly at camera. Studio setup with clean white 
seamless background. Soft key light from upper left with fill 
reflector on the right. Sharp focus on eyes and nose, natural fur 
texture visible. Alert, engaged expression. 100mm macro lens feel, 
moderate depth of field. Commercial pet photography quality. 
Photoreal, no smoothing of fur texture.

Mode: Generate
Resolution: 4K
Aspect Ratio: 1:1
Num Images: 4
Output Format: png
Profiles Referenced: [pet_profile_id]

Director's Notes: Phota supports pet profiles (cats and dogs). 
Same prompting principles apply — the profile handles identity; 
the prompt handles photography. "Chest-level angle" means camera 
is at the animal's height, not human standing height. 100mm 
provides flattering compression even for animal faces.
```

---

## SPECIALIZED USE CASES

### Example 13: Dating Profile Photo (Universal)
```
Prompt: Natural, authentic portrait of [[profile_id_1]], waist up, 
in a casual coffee shop setting. Warm window light from the left 
creating soft, flattering shadows. Genuine, approachable expression 
with natural relaxed smile, looking directly at camera. Casual 
clothing visible. 50mm lens feel, moderate depth of field with 
cafe interior softly blurred in background. Warm color temperature. 
Authentic, not over-processed, natural skin. Looks like a friend 
took a great photo of you. Photoreal.

Mode: Generate
Resolution: 1K
Aspect Ratio: 3:4
Num Images: 4
Output Format: jpeg
Profiles Referenced: [profile_id_1]

Director's Notes: Dating profile photos need to look authentic — NOT 
like a professional shoot. "Looks like a friend took a great photo" 
is the creative direction. 50mm is the classic "normal" lens that 
doesn't look telephoto-compressed or wide-angle-distorted. Window 
light is inherently flattering and believable.
```

---

### Example 14: Author Photo — Book Jacket (Universal)
```
Prompt: Author portrait of [[profile_id_1]], chest up, seated in 
a leather armchair in a book-lined study. Soft warm light from a 
desk lamp on the left, cool fill from a window on the right. 
Thoughtful, intelligent expression, slight smile, looking at camera 
with one hand resting on the chair arm. 85mm lens, shallow depth 
of field blurring the bookshelf background. Warm, inviting, 
intellectual. Rich tones. Editorial quality for book jacket. 
Photoreal, natural skin texture.

Mode: Generate
Resolution: 4K
Aspect Ratio: 3:4
Num Images: 4
Output Format: png
Profiles Referenced: [profile_id_1]

Director's Notes: Book jacket portraits require a specific quality — 
intelligent, approachable, authoritative. The book-lined study is 
the canonical author setting. Dual light sources (warm practical 
lamp + cool window) create dimension. "One hand resting on chair arm" 
adds a natural pose element without overcomplicating.
```

---

## Version Information

- **Examples Version:** 1.0
- **Covers:** Phota Generate mode across portrait photography categories
- **Last Updated:** 2026-04-18
- **Maintained By:** Visual Horizon Studio
