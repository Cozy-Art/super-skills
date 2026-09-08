# Kling 3.0 - Best Practices Guide

## The 5-Layer Structure (Mandatory)

Every Kling 3.0 prompt must follow this production-style structure:

**Scene → Characters → Action → Camera → Audio & Style**

This order helps Kling understand context before introducing movement and complexity.

---

## Layer 1: Scene/Context (The Anchor)

**Always start by grounding the scene.** Kling needs environmental context first.

### What to Include:
- **Location type**: Indoor/outdoor, urban/nature, specific room
- **Time of day**: Morning, sunset, night, golden hour
- **Atmospheric conditions**: Clear, foggy, rainy, smoky
- **Overall mood**: Tense, peaceful, mysterious

### ✅ Good Examples:
```
Quiet rooftop at night with distant city lights and a cool breeze.
```
```
Bustling coffee shop interior during morning rush, warm lighting through large windows.
```
```
Abandoned warehouse at dusk, dust particles visible in fading light.
```

### ❌ Avoid:
- Starting with character actions before establishing where they are
- Vague locations: "a place", "somewhere nice"
- No environmental detail

---

## Layer 2: Characters/Subject

**Describe who/what appears with specific visual details.**

### What to Include:
- Physical characteristics (age, build, distinctive features)
- Clothing and style
- Posture and bearing
- Unique identifiers (hair, accessories, scars)

### ✅ Good Examples:
```
A weathered detective in his 50s wearing a brown trench coat and fedora, hands in pockets.
```
```
Young woman in athletic wear with a high ponytail, focused expression, yoga mat under arm.
```
```
Sleek chrome robot with glowing blue joints, humanoid but distinctly mechanical.
```

### ❌ Avoid:
- Generic descriptions: "a person", "someone"
- Missing visual details
- Conflicting descriptions

---

## Layer 3: Action Timeline (Sequential)

**THIS IS CRITICAL FOR KLING 3.0:** Break actions into sequential steps, don't stack them.

### Use Temporal Markers:
- First... then... finally...
- Initially... after... eventually...
- She begins by... next... concluding with...

### ✅ Good Example:
```
First, she slows her pace and glances around cautiously. Then she crouches beside 
a parked car, examining something on the ground. Finally, she stands and continues 
walking with renewed purpose.
```

### ❌ Bad Example (Stacked):
```
She walks, looks around, crouches, examines ground, stands up, and walks away quickly 
while checking her phone and adjusting her bag.
```
**Problem:** Too many simultaneous actions confuse the model.

### Keep Actions Realistic:
- Physically possible movements
- Appropriate timing for duration
- Clear cause and effect

---

## Layer 4: Camera Movement

**Kling 3.0 excels with specific cinematic language.**

### Essential Camera Terms

**Shot Types:**
- Wide shot / Establishing shot
- Medium shot
- Close-up / Extreme close-up
- Over-the-shoulder
- POV (Point of View)
- Two-shot (two subjects in frame)

**Camera Movements:**
- **Dolly push/in**: Camera moves toward subject
- **Dolly out**: Camera moves away from subject
- **Pan left/right**: Horizontal rotation
- **Tilt up/down**: Vertical rotation
- **Tracking shot**: Camera follows subject's movement
- **Crane shot**: Vertical movement (up/down)
- **Whip-pan**: Extremely fast pan creating blur
- **Handheld**: Natural camera shake
- **Shoulder-cam drift**: Subtle documentary-style movement

**Lens Effects:**
- Shallow depth of field
- Rack focus (shift focus between subjects)
- Telephoto compression
- Wide-angle distortion

### ✅ Good Examples:
```
Slow dolly-in on the detective's face, shallow depth of field isolating him from background.
```
```
Handheld tracking shot following the runner through crowded street.
```
```
Crane shot ascending from ground level to reveal city skyline.
```

### ❌ Avoid:
- No camera mention at all
- Generic "cinematic shot"
- Contradictory movements
- Overly complex camera choreography

---

## Layer 5: Audio & Style

### Audio Components

**1. Character-Attributed Dialogue (Critical for Lip-Sync):**

**Syntax:** `@Character name says, "dialogue"`

**✅ Good Examples:**
```
@Detective murmurs, "This must be it. The secret code."
```
```
@Woman responds calmly: "I know exactly what you're thinking."
```

**Key Rules:**
- Always use @ symbol before character name
- Include emotion/tone verb: murmurs, shouts, whispers, declares
- Keep dialogue natural and concise
- Use quotation marks

**2. Ambient Sound:**
Describe environmental audio:
```
Distant traffic hum and occasional car horn.
```
```
Gentle rain pattering, thunder rumbling far away.
```
```
Coffee machine hissing, quiet conversation murmur, jazz music softly playing.
```

**3. Sound Effects:**
Specific action sounds:
```
Footsteps echoing on metal stairs.
```
```
Papers rustling as hands shuffle through documents.
```
```
Glass shattering, alarm blaring in distance.
```

### Style Components

**Lighting:**
- Golden hour glow
- Harsh overhead fluorescent
- Neon signs casting colored light
- Soft window light
- Candlelight flickering

**Color Grading:**
- Film noir high contrast
- Desaturated blues and grays
- Warm vintage tones
- Vibrant saturated colors

**Texture/Aesthetic:**
- Film grain texture
- Lens flares
- Bokeh background
- Smoke wisps
- Dust particles in light beams

---

## Negative Prompts (Essential)

**Kling 3.0 has specific tendencies that negative prompts combat:**

### Default Issues:
1. **Smiling default**: Characters default to happy expressions
2. **Hand morphing**: Fingers multiply or distort
3. **Physics errors**: Unrealistic object interactions

### Recommended Negative Prompt Template:
```
smiling, laughing, cartoonish, bright colors, morphing, disfigured hands, 
extra fingers, blurry text, low resolution, robotic movement
```

### When to Add More:
- **For serious scenes**: Add "cheerful, upbeat"
- **For realistic content**: Add "animated, stylized, painted"
- **For humans**: Add "extra limbs, deformed body"
- **For clarity**: Add "blurry, out of focus, low quality"

---

## Multi-Shot Storyboard Format (3.0 Omni)

### Syntax Structure:
```
**Shot 1 (Xs):** [Camera] [Description] @Character: "[dialogue]"
**Shot 2 (Xs):** [Camera] [Description] @Character: "[dialogue]"
```

### Complete Example:
```
**Shot 1 (5s):** Wide establishing shot. A detective enters a dimly lit office, 
scanning the room cautiously. Slow dolly-in following his movement. Noir aesthetic 
with harsh desk lamp creating deep shadows.

**Shot 2 (6s):** Medium shot. The detective approaches the desk, examining 
scattered papers with focused intensity. @Detective murmurs, "Someone was here 
recently." Handheld camera slight shake. Papers rustling sound.

**Shot 3 (4s):** Close-up on detective's face as realization dawns, eyes widening 
slightly. Rack focus from papers to face. Tense atmosphere. Clock ticking in silence.
```

### Best Practices:
- Plan total duration across all shots
- Logical shot progression (wide → medium → close)
- Each shot has distinct camera/action
- Dialogue attributed to characters
- Consistent lighting/mood across shots

---

## Elements System (Character Consistency)

### How Elements Work:
Upload 1-4 reference images to maintain character consistency across generations.

### Face Adherence Settings:

| Value | Effect | When to Use |
|-------|--------|-------------|
| **42** | Similar face, natural variation | Different scenes, allow styling changes |
| **70** | Strong similarity | Multi-shot sequences, consistent character |
| **85** | Very strict | Exact character replication needed |
| **100** | Copy-paste | Identical appearance critical |

### Reference Type Options:

**Face Only:**
- Maintains facial features
- Allows clothing/pose variation
- Best for: Different outfits, various contexts

**Subject:**
- Includes body, clothing, pose
- More complete consistency
- Best for: Scene continuity, wardrobe matching

**Entire Image:**
- Preserves full composition and style
- Strictest adherence
- Best for: Exact recreation, specific look

### Elements Workflow:

**Step 1:** Generate Hero Character Shot
```
Detailed character description, clear front-facing view, good lighting
```
Set face adherence: 70-85

**Step 2:** Extract Best Frames
Save frames showing:
- Front view (primary reference)
- Side profile
- Three-quarter angle
- Different expressions

**Step 3:** Use as References
Upload 1-4 frames as Elements for subsequent generations.

**Step 4:** Maintain Consistency
- Use same references across all related shots
- Keep face adherence value consistent
- Match lighting style in prompts

---

## Sequential Action Structuring

### The Problem:
❌ "A chef chops vegetables, tosses them in pan, seasons, plates, and garnishes."

**Why it fails:** Too many actions stacked without timing or sequence.

### The Solution:
✅ "First, the chef rapidly chops vegetables with precise knife work. Then, he tosses 
them into a hot wok with a swift motion. Finally, he plates the dish with careful 
attention to presentation."

**Why it works:** Clear progression, temporal markers, realistic timing.

### Templates:

**For 5-second clips:**
```
[Action 1] occurs. [Action 2] follows smoothly. [Action 3] completes the motion.
```

**For 10-second clips:**
```
Initially, [action 1]. After [duration/transition], [action 2]. Then [action 3]. 
Finally, [action 4] concludes the sequence.
```

**For 15-second clips:**
```
The sequence begins with [action 1]. Next, [action 2] unfolds as [detail]. 
This transitions to [action 3] where [detail]. Eventually, [action 4] occurs. 
Finally, [action 5] brings closure.
```

---

## Cinematic Motion Verbs

### Instead of "moves":
- glides smoothly
- drifts lazily
- shifts deliberately
- surges forward
- retreats cautiously

### Instead of "walks":
- strides confidently
- shuffles wearily
- rushes frantically
- saunters casually
- creeps silently

### Instead of "looks":
- gazes intently
- glances nervously
- scans methodically
- peers suspiciously
- studies carefully

### Camera-Specific Verbs:
- pushes in
- pulls back
- sweeps across
- orbits around
- ascends slowly
- descends dramatically

---

## Texture and Detail Enhancement

### Add Sensory Details:
- **Visual textures**: grain, reflections, condensation, fabric sheen
- **Light qualities**: harsh, soft, dappled, colored, flickering
- **Atmospheric elements**: smoke, dust, mist, steam, rain
- **Material properties**: glossy, matte, weathered, pristine, worn

### ✅ Enhanced Example:
```
Noir-style office with film grain texture. Venetian blinds cast striped shadows 
across worn wooden desk. Dust particles visible in harsh desk lamp beam. Detective's 
leather jacket shows wear and creases. Condensation on window glass reflects neon 
signs from street below.
```

**Result:** Rich, cinematic visual quality with depth.

---

## Common Issues & Solutions

### Issue: Static, Boring Output
**Problem:** No camera movement specified  
**Solution:** Always include camera movement: "Slow dolly-in", "Tracking shot", "Handheld POV"

### Issue: Character Smiling When Shouldn't
**Problem:** Kling's default happy expression  
**Solution:** Negative prompt: "smiling, laughing, cheerful"

### Issue: Hands Morphing/Extra Fingers
**Problem:** Common AI artifact  
**Solution:** Negative prompt: "disfigured hands, extra fingers, morphing, deformed"

### Issue: Physics Errors (Objects Floating, Weird Interactions)
**Problem:** Vague spatial descriptions  
**Solution:** Explicit spatial language: "hand firmly gripping handle", "feet planted on ground", "making direct contact with"

### Issue: Too Many Changes/Chaotic Output
**Problem:** More than 7 distinct visual elements  
**Solution:** Combine items into categories, focus on 5-7 core elements maximum

### Issue: Character Inconsistent Between Shots
**Problem:** Not using Elements or low face adherence  
**Solution:** Upload references, set face adherence 70-100

---

## Video Extension Workflow

### For Sequences >15 Seconds:

**Step 1:** Generate Initial 15s
Full prompt with all 5 layers, establish character/scene.

**Step 2:** Continuation Prompt
Describe what happens next:
```
The detective stands from desk, walks slowly to window, peers out at 
rain-soaked street below, deep in thought.
```

**Step 3:** Multiple Extensions
Continue extending by 15s increments up to 3 minutes total.

**Best Practices:**
- Maintain consistent Elements references
- Keep lighting/mood consistent
- Natural action progression
- Smooth transitions between segments

---

## Quick Reference Checklist

Before submitting a Kling 3.0 prompt:

- [ ] **Layer 1**: Scene/context established
- [ ] **Layer 2**: Character/subject described
- [ ] **Layer 3**: Actions in sequential timeline
- [ ] **Layer 4**: Camera movement specified
- [ ] **Layer 5**: Audio attributed, style defined
- [ ] **Negative prompt**: Includes core negatives
- [ ] **Elements**: References uploaded if character consistency needed
- [ ] **Duration**: Appropriate for action complexity
- [ ] **Face adherence**: Set 70-100 for consistency

---

## Template Examples

### Dialogue Scene Template:
```
[Location and atmosphere]. [Character description] [sequential action timeline]. 
[Camera movement]. @Character [verb], "[dialogue]." [Ambient sound]. [Style/lighting].

Negative: smiling, laughing, morphing, disfigured hands
```

### Action Sequence Template:
```
[Environment and conditions]. [Subject description] [action 1], then [action 2], 
finally [action 3]. [Dynamic camera tracking]. [Sound effects]. [Cinematic style].

Negative: robotic movement, unrealistic physics, low resolution
```

### Multi-Shot Template:
```
**Shot 1 (Xs):** [Wide camera]. [Establishing context]. [Subject introduction]. 
[Atmosphere].

**Shot 2 (Xs):** [Medium camera]. [Subject action]. @Character: "[dialogue]." 
[Audio details].

**Shot 3 (Xs):** [Close camera]. [Reaction/emotion]. [Style emphasis].

Negative: [comprehensive negatives]
```

---

**Pro Tip:** Kling 3.0 rewards specificity and structure. The more detailed your 5-layer structure, the better your results. Always use negative prompts and Elements for professional-quality output.
