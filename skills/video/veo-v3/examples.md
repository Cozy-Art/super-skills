# Veo 3.1 — Examples

All prompts follow the five-part formula: **Cinematography + Subject + Action + Context + Style & Ambiance**

**How to read these.** The fenced block is the prompt — that whole string, and nothing else, is what
gets pasted into the tool. The bold line underneath is the **settings**, which live in the tool's own
controls and must never be written into the prompt text. That separation is the point of the format,
not a formatting habit.

**Note what is absent.** No example points at a reference image. Where a prompt uses references
(examples 2 and 3), the character is **re-described in prose** and the images are attached separately.
Veo has no in-prompt reference token — see `continuity-and-references.md`. If you find yourself
wanting to write `@Image1`, write the description instead.

---

## CHARACTER-FOCUSED EXAMPLES

### Example 1: Character Introduction with Dialogue
```
A medium close-up tracking shot follows a weathered detective in a brown trench coat and fedora as he walks through a rain-slicked alley at night. He moves with calm, deliberate steps, examining graffiti on brick walls, occasionally glancing over his shoulder. The setting is a narrow urban alley with neon signs reflecting in puddles, shrouded in heavy fog. Film noir aesthetic with deep shadows, high contrast, and cool blue undertones creates a tense, mysterious atmosphere. The detective murmurs, "Someone's been here recently." SFX: footsteps splashing in water. Ambient noise: distant traffic and rain pattering.
```
**Resolution:** 720p or 1080p | **Duration:** 8s | **Aspect:** 16:9  
**Reference Images:** Upload 1-2 character reference photos

---

### Example 2: Same Character, Different Scene (Using References)
```
A low-angle static shot captures the detective from Example 1 sitting at a cluttered desk in a dimly lit office. He leans forward, studying photographs spread across the surface, occasionally moving them with his finger to compare details. The office has wood paneling, a single desk lamp providing harsh side lighting, and venetian blinds casting shadows. Film noir continues with golden lamp light cutting through darkness. The detective whispers, "This connects to the waterfront case." SFX: papers rustling. Ambient noise: clock ticking, distant city sounds through window.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 16:9  
**Reference Images:** Use SAME character images from Example 1  
**Seed:** Use same seed for consistency

---

### Example 3: Character Extension (Building 15s Sequence)

**Initial 8s:**
```
A medium shot tracks a space captain in a sleek uniform walking onto the bridge of a starship. She moves with confident purpose, nodding to crew members as she approaches the captain's chair. The bridge is high-tech with glowing holographic displays and a large viewscreen showing stars. Clean, futuristic aesthetic with cool blue lighting and bright accent lights creates a professional, anticipatory mood. The captain announces, "Status report." SFX: footsteps on metal floor. Ambient noise: gentle hum of ship systems.
```

**7s Extension:**
```
The captain settles into the chair as a crew member approaches with a data pad. She accepts it, her expression shifting to concern as she reads. The viewscreen in background flickers, showing an approaching vessel. She declares firmly, "Red alert." SFX: alert klaxon begins. Ambient noise: system hum intensifies.
```

**Resolution:** 720p (required for extension) | **Aspect:** 16:9  
**Total:** ~15 seconds through extension workflow

---

## ENVIRONMENT-FOCUSED EXAMPLES

### Example 4: Establishing Shot - Cyberpunk City
```
A crane shot starts low between towering skyscrapers and ascends smoothly, revealing a vast cyberpunk metropolis at night. Neon signs in pink, blue, and green illuminate rain-slicked streets far below where tiny figures and vehicles move. Flying cars streak past at eye level as the camera continues rising. The cityscape extends to the horizon under dark storm clouds with occasional lightning. Blade Runner-inspired aesthetic with heavy contrast, vibrant neon colors against deep blacks, and atmospheric rain creates an electric, overwhelming urban atmosphere. SFX: distant thunder rumbling. Ambient noise: layered city sounds, rain, distant sirens.
```
**Resolution:** 4K | **Duration:** 8s | **Aspect:** 16:9

---

### Example 5: Natural Environment - Forest Morning
```
A slow dolly-forward through ancient forest at dawn, pushing between moss-covered trees toward a clearing. Shafts of golden morning sunlight pierce through the canopy, creating visible light beams in mist. Small woodland creatures scatter as the camera approaches. The forest floor is carpeted with ferns and fallen leaves, with a gentle stream visible to the left. Ethereal, magical atmosphere with warm golden light diffused through fog, creating a serene, mystical mood. SFX: gentle stream babbling. Ambient noise: birds chirping, leaves rustling in breeze.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 16:9

---

### Example 6: Interior - Abandoned Space Station
```
A handheld POV shot moves cautiously through a dark, abandoned space station corridor. The camera sways slightly as if the viewer is walking, occasionally stopping to examine broken control panels and flickering emergency lights. Debris floats in zero gravity, drifting past the camera. The corridor is industrial with exposed wiring, shattered glass, and scorch marks on walls. Tense, eerie atmosphere with harsh emergency lighting creating deep shadows and red warning lights pulsing intermittently. SFX: electrical crackling from damaged systems. Ambient noise: distant groaning of metal structure, air recycling system failing.
```
**Resolution:** 720p | **Duration:** 8s | **Aspect:** 16:9

---

## ACTION & MOTION EXAMPLES

### Example 7: Chase Sequence
```
A fast tracking shot races behind a parkour athlete as they sprint across rooftops in an urban environment. The athlete leaps from one building to another, rolling smoothly upon landing and immediately continuing forward. The camera maintains pace, occasionally bouncing with the athlete's movements. The setting is daylight downtown with office buildings, air conditioning units, and pigeon flocks scattering. Dynamic, energetic aesthetic with natural lighting, motion blur on background, and saturated colors creates an exhilarating, pulse-pounding mood. SFX: footsteps pounding on concrete, clothing rustling. Ambient noise: city traffic below, wind rushing past.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 21:9 (cinematic)

---

### Example 8: Martial Arts Combat
```
A medium shot circles around two martial artists mid-combat in a traditional dojo. The fighters exchange rapid strikes, one attacking with a spinning kick while the other blocks and counters. Their movements are fluid and precise, gi uniforms snapping with each motion. The dojo has wooden floors, paper walls, and afternoon sunlight streaming through. Classical aesthetic with warm natural light, slight slow-motion effect on impact moments, and focused intensity creates a dramatic, skillful atmosphere. SFX: impacts, cloth snapping, fighters exhaling with effort. Ambient noise: dojo quietness, distant street sounds.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 16:9

---

### Example 9: Vehicle Action
```
A low-angle tracking shot follows a vintage motorcycle speeding down an empty desert highway at sunset. The camera keeps pace alongside the bike, capturing the rider leaning into motion, helmet reflecting orange sunlight. The motorcycle's chrome gleams as wheels blur with speed. The setting is an endless straight desert road with mountains silhouetted on the horizon under a spectacular sunset sky. Cinematic road movie aesthetic with warm golden hour light, slight lens flare, and rich color saturation creates a liberating, nostalgic mood. SFX: engine roaring, wind rushing. Ambient noise: empty desert silence beneath mechanical sounds.
```
**Resolution:** 4K | **Duration:** 8s | **Aspect:** 21:9

---

## STYLE & MOOD VARIATIONS

### Example 10: Film Noir Style
```
A static medium shot frames a femme fatale in a sequined evening gown standing in a smoky jazz club doorway. She poses dramatically with one hand on the door frame, cigarette holder in the other, backlit by harsh white light from behind. The club interior shows dim tables with patrons in shadows and a stage with band silhouettes. Classic 1940s film noir aesthetic with extreme high contrast black and white, hard shadows, and diffused smoke creates a seductive, dangerous atmosphere. She declares coolly, "I've been expecting you, detective." SFX: jazz music muffled in background. Ambient noise: glasses clinking, low conversation murmur.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 4:3 (period ratio)

---

### Example 11: Sci-Fi Horror Style
```
A slow dolly-in on a lone astronaut in a damaged spacesuit floating in a dark cargo bay. The astronaut rotates slowly in zero gravity, their visor reflecting flickering emergency lights. Behind them, something large and organic pulses in the shadows, barely visible. The cargo bay is industrial with floating debris, sparking wires, and condensation on metal surfaces. Sci-fi horror aesthetic with harsh contrast, green and red emergency lighting, and grainy texture creates a terrifying, isolating mood. The astronaut's breath echoes in helmet, heavy and panicked. SFX: suit systems beeping urgently. Ambient noise: deep space silence punctuated by distant metallic groans.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 16:9

---

### Example 12: Dreamlike Fantasy
```
A gentle crane shot ascends through a fantastical library where books float in mid-air, their pages turning by themselves. A young woman in flowing robes walks between the floating volumes, occasionally reaching out to touch one, causing it to glow softly. The library extends infinitely upward, with spiraling staircases and glowing orbs of light drifting lazily. Ethereal fantasy aesthetic with soft focus, pastel colors dominated by purples and golds, and luminescent highlights creates a magical, contemplative atmosphere. She whispers in wonder, "So much knowledge, waiting to be discovered." SFX: pages rustling softly. Ambient noise: distant chiming like wind chimes, barely audible whispers.
```
**Resolution:** 4K | **Duration:** 8s | **Aspect:** 9:16 (vertical, mobile)

---

### Example 13: Documentary Realism
```
A handheld medium shot follows a master potter at their wheel in a sunlit workshop. The potter's weathered hands shape wet clay with practiced skill, occasionally dipping fingers in water. The camera orbits slightly, capturing the concentration on the potter's face and the emerging form. The workshop has tools on walls, completed works on shelves, and large windows allowing natural light. Documentary realism aesthetic with natural lighting, slight camera shake suggesting human operator, and warm earthy tones creates an authentic, meditative mood. Workshop sounds: wheel humming, water splashing, tools clinking. Ambient noise: distant birds through open window.
```
**Resolution:** 1080p | **Duration:** 8s | **Aspect:** 16:9

---

## SPECIAL TECHNIQUES

### Example 14: First/Last Frame Interpolation
```
**First Frame:** Character standing in doorway, hand on handle, about to enter
**Last Frame:** Character seated at desk inside room, working
**Prompt:** A smooth tracking shot follows a businessman entering his office. He walks from the doorway across the room, removing his jacket and hanging it on a rack, then settling into his chair at the desk. The office is modern with glass walls, city view, and minimalist furniture. Professional atmosphere with natural window light transitioning to warmer interior lighting creates a routine, focused mood. SFX: door closing, footsteps, chair sliding. Ambient noise: muffled office ambiance.
```
**Duration:** 8s | **Resolution:** 1080p

---

### Example 15: Multi-Shot Sequence (Timestamp Prompting)
```
[00:00-00:02] Close-up on a scientist's gloved hands carefully removing a glowing vial from a secure container in a high-tech laboratory. The hands move with extreme caution.

[00:02-00:04] Cut to medium shot of the scientist's face, sweat beading on forehead, eyes fixed intently on the vial. They whisper nervously, "This is it. The cure."

[00:04-00:06] Over-the-shoulder shot as they walk toward a containment chamber, the vial held firmly. Laboratory equipment blinks and hums around them.

[00:06-00:08] Wide shot showing the scientist placing the vial into the chamber, sealing it shut. Relief visible in their posture as they step back.

Sterile laboratory aesthetic with cool fluorescent lighting and gleaming metal surfaces. SFX: container hissing open, vial clinking, chamber sealing. Ambient noise: ventilation system, equipment humming.
```
**Duration:** 8s | **Resolution:** 1080p

---

## AUDIO-FOCUSED EXAMPLES

### Example 16: Dialogue-Heavy Scene
```
A medium two-shot frames a lawyer and client across a mahogany desk in a traditional office. The lawyer leans forward, gesturing with a pen as she explains. The client sits back, arms crossed, listening with a skeptical expression. The office has law books lining walls, green desk lamp, and afternoon sunlight through venetian blinds creating shadow patterns. Professional atmosphere with warm tungsten lighting mixed with natural light creates a tense negotiation mood. The lawyer states firmly, "You need to take this deal." The client responds quietly, "I'm not so sure." SFX: papers shuffling on desk. Ambient noise: clock ticking, muffled city street sounds.
```
**Duration:** 8s | **Resolution:** 1080p  
**Note:** Two short lines, both speakers visible

---

### Example 17: Sound Effects Showcase
```
A static wide shot captures a blacksmith's forge at work. The blacksmith hammers glowing metal on an anvil, sparks flying with each strike. They pause to examine the work, then plunge it into water creating a cloud of steam. The forge glows orange in the dim workshop, tools hanging on walls, and small window providing minimal light. Dark, atmospheric aesthetic with dramatic forge lighting and deep shadows creates a rhythmic, industrial mood. SFX: hammer ringing on anvil, metal hissing in water, forge crackling. Ambient noise: bellows pumping air, distant village sounds.
```
**Duration:** 8s | **Resolution:** 1080p

---

## RESOLUTION/FORMAT EXAMPLES

### 720p - Rapid Iteration
```
A medium tracking shot follows a chef preparing a dish in a busy kitchen. Quick movements: chopping vegetables, tossing ingredients in a pan, plating with precision. Professional kitchen with stainless steel, bright lighting, steam rising. Dynamic cooking show aesthetic with warm lighting and energetic pacing. SFX: knife on cutting board, pan sizzling. Ambient noise: kitchen bustle.
```
**Use:** Fast concept testing, extension workflows

---

### 1080p - Professional Deliverable
```
An elegant dolly shot glides through a high-end fashion boutique as a model walks between display racks. She touches fabrics, examining pieces with refined appreciation. Minimalist boutique with white walls, marble floors, designer clothing on racks, and sophisticated lighting. Luxury aesthetic with soft focused lighting and muted elegant colors. SFX: heels on marble. Ambient noise: subtle classical music.
```
**Use:** Client presentations, final deliverables

---

### 4K - Hero Shot Maximum Quality
```
A slow crane shot reveals a majestic ancient temple hidden in jungle at golden hour. The camera ascends from ground level through vine-covered stone structures up to reveal the temple's peak against a spectacular sunset sky. Moss and vegetation reclaim carved stone, with monkeys visible on distant walls. Epic cinematic aesthetic with rich golden light, deep color saturation, and atmospheric haze. SFX: jungle birds calling. Ambient noise: wind through leaves, distant waterfall.
```
**Use:** Showcase pieces, maximum quality final renders

---

## Quick Reference Templates

**Dialogue Scene:**
[Shot + movement] [subject description] [action] in [context]. [Subject] [emotion verb], "[dialogue]." [Style]. SFX: [sound]. Ambient: [soundscape].

**Action Sequence:**
[Dynamic camera] [subject] [action verb] through [environment]. [Motion details]. [Style]. SFX: [action sounds]. Ambient: [environment sounds].

**Establishing Shot:**
[Wide/crane shot] reveals [environment] at [time]. [Weather/atmosphere]. [Style and lighting]. SFX: [environmental]. Ambient: [soundscape].

---

**Pro Tip:** Start every new scene with a clear establishing shot using references, then build subsequent shots using extension or new generations with same references/seed for consistency.
