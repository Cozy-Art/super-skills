# MiniMax Hailuo 2.3 - Best Practices Guide

## The Golden Rule: 4-6 Seconds Maximum

**This is the most important guideline for Hailuo 2.3.**

### Why 4-6 Seconds?

- **Peak temporal coherence**: Frame-to-frame pixel consistency is highest
- **No character drift**: Features stay consistent throughout
- **Better physics**: Environmental interactions remain realistic
- **Commercial pacing**: Aligns with standard B-roll timing
- **Maximum fidelity**: Higher quality per frame

### Temporal Trimming Workflow

Generate 4-second clips → Use middle 2 seconds → This is where coherence peaks

**The model has stabilized understanding of initial frame but hasn't begun to lose context.**

---

## Natural Language Prompting

**Hailuo responds best to simple, clear descriptions.**

### ✅ Good Approach:
```
A professional chef in a modern kitchen with steam rising from a pan. He tosses 
ingredients with fluid motion while the camera slowly circles around him. Warm 
ambient lighting, cinematic feel.
```

### ❌ Bad Approach (Overly Complex):
```
[SHOT TYPE: Medium] + [SUBJECT: Chef, male, 40s, white uniform, professional 
demeanor] + [ACTION SEQUENCE: Step 1: Pick up pan, Step 2: Add ingredients, 
Step 3: Toss with precision] + [ENVIRONMENT: Kitchen, modern, stainless steel...] 
[LIGHTING: Warm, 3200K, key light from left...]
```

**The second example is overengineered. Hailuo prefers natural language.**

---

## The 5-Part Formula

Two valid structures - use what fits the scene:

### Structure A: Camera-First
```
[Camera Shot + Motion] + [Subject + Description] + [Action] + [Scene + Description] + [Lighting/Style]
```

**Example:**
```
[Slow dolly forward], a young woman in a flowing dress walks through a sunlit 
meadow, wildflowers swaying in the breeze. Golden hour lighting creates warm, 
dreamy atmosphere.
```

### Structure B: Character-First
```
Main Character + Environment + Changes to character/scene + Camera Movement + Video Style
```

**Example:**
```
A detective in a trench coat stands in a rain-soaked alley at night, examining 
evidence under a flickering streetlight. He kneels down, then stands with renewed 
purpose. [Handheld tracking shot]. Film noir aesthetic with high contrast.
```

**Both work equally well - choose based on whether camera or character is primary focus.**

---

## Camera Movement: Bracket Notation

### Single Movement:
```
The dancer spins gracefully across the stage [Pan right following movement].
```

### Combined Movements:
```
A chef prepares a gourmet dish [Pan right, Zoom in slowly on the plating].
```

### Sequential Movements:
```
She enters the room confidently [Dolly forward], pauses to survey the space, 
then walks to the window [Pan left].
```

### Available Camera Movements

**Basic Movements:**
- **Pan left/right**: Horizontal camera rotation
- **Tilt up/down**: Vertical camera rotation
- **Zoom in/out**: Push in/pull out effect
- **Truck left/right**: Lateral horizontal movement
- **Dolly in/out**: Forward/backward camera movement
- **Crane up/down**: Vertical camera position change

**Special Combinations:**
- **Left/Right circling**: Camera moves in circular pattern around subject
- **Walking shot**: Follows subject walking with sideways movement
- **Stage shot**: Combines panning with zoom for dramatic effect
- **Upward/Downward tilt**: Combines vertical movement with tilt

### Motion Adjectives Matter

❌ **Don't use:** "Fast zoom"
✅ **Do use:** "Slow push-in", "Gentle dolly forward", "Subtle zoom"

Hailuo responds better to controlled, cinematic language.

---

## Subject Reference Feature

### How It Works

1. **Upload single reference image** of character
2. **AI auto-detects facial features**
3. **Features maintained** across all generated scenes
4. **Consistent face** throughout all videos

### Best Practices

**Image Requirements:**
- ✅ High-quality portrait images
- ✅ Front-facing works best
- ✅ Realistic human images
- ✅ Clear facial features, good lighting
- ❌ Stylized art, anime, 3D renders (less reliable)

**Prompting with Subject Reference:**
Since AI already knows the face, focus on:
- Emotions and expressions
- Body language and pose
- Actions and movements
- Scene context and mood

**Example:**
```
[Subject Reference uploaded: front-facing portrait of woman in her 30s]

Prompt: The woman walks through a misty forest at dawn, expression thoughtful 
and peaceful. Soft morning light filters through trees. [Slow tracking shot 
following from side]. Serene, contemplative atmosphere.
```

### Limitations to Know

- **Hands**: Can still have issues when holding objects
- **Single entity**: Multi-character support in development
- **Lighting artifacts**: Occasional inconsistencies
- **Style-dependent**: Works best with realistic human images

---

## Image-to-Video Best Practices

### When Using Reference Image as First Frame

**The AI already knows:**
- What the subject looks like
- The scene composition
- The lighting setup

**Your prompt should focus on:**
- Camera movement
- Action/motion changes
- Mood shifts
- Atmospheric evolution

### ✅ Good Image-to-Video Prompt:
```
[Reference image: Woman standing at beach at sunset]

Prompt: The woman turns slowly to face the camera, hair blowing in the sea breeze, 
a gentle smile forming. [Slow dolly-in on her face]. Warm golden hour light, 
peaceful and nostalgic mood.
```

### ❌ Bad Image-to-Video Prompt:
```
[Reference image: Woman standing still at beach]

Prompt: The woman suddenly sprints down the beach, dives into the water, swims 
out 50 meters, and climbs onto a surfboard. [Fast tracking shot].
```

**Problem:** Too dramatic a change from static starting pose. Match actions to what's physically feasible.

---

## Emotion Rendering (Hailuo's Strength)

**Hailuo excels at emotional nuance.** Leverage this strength.

### Emotion Keywords That Work:

**Subtle emotions:**
- Contemplative, pensive, wistful
- Cautious, uncertain, hesitant
- Hopeful, optimistic, determined
- Melancholic, nostalgic, bittersweet

**Strong emotions:**
- Joyful, elated, triumphant
- Anxious, worried, fearful
- Angry, frustrated, intense
- Surprised, shocked, amazed

### ✅ Example with Emotion Focus:
```
An elderly man sits on a park bench, watching children play in the distance. 
His expression shifts from wistful nostalgia to a gentle, bittersweet smile. 
[Close-up, shallow depth of field]. Soft afternoon light, warm and peaceful.
```

**The emotion detail helps Hailuo render nuanced facial expressions.**

---

## Common Mistakes & Solutions

### Mistake 1: Clips Too Long

**Problem:** Generate 10-second clips, character features drift  
**Solution:** Stick to 4-6 seconds, chain clips in post-production

### Mistake 2: Vague Subject Motion

**Problem:** Prompt says "a person moves through the scene"  
**Solution:** Be specific: "walks purposefully", "drifts slowly", "rushes frantically"

### Mistake 3: Complex Hand Interactions

**Problem:** "Character picks up mug, drinks coffee, sets it down"  
**Solution:** Avoid detailed hand/object interactions - Hailuo struggles with these

### Mistake 4: Expecting Text Rendering

**Problem:** Include signs, labels, text in scene  
**Solution:** Avoid text entirely or add it in post-production

### Mistake 5: Low-Quality Reference Images

**Problem:** Blurry, low-res source images  
**Solution:** Use high-quality images, minimum 300px on short side

### Mistake 6: Overly Long Prompts

**Problem:** 500+ word prompts with conflicting details  
**Solution:** 3-4 clear sentences covering the 5-part formula

### Mistake 7: Conflicting Instructions

**Problem:** "Bright sunny day with dark moody lighting"  
**Solution:** Keep descriptions internally consistent

---

## Motion Realism Techniques

### Hailuo's Physics Accuracy

**What works well:**
- Natural walking/running
- Fluid fabric motion
- Water/liquid physics
- Smoke and particle effects
- Wind effects on hair/clothing
- Organic camera movements

**What to avoid:**
- Complex object manipulation
- Precise hand gestures
- Rapid action changes
- Unnatural physics (flying, morphing)

### Motion Descriptors

**Instead of:** "moves"  
**Use:** glides, drifts, strides, shuffles, surges, retreats

**Instead of:** "camera follows"  
**Use:** tracking shot, handheld following, smooth dolly alongside

---

## Lighting & Atmosphere

### Lighting Keywords That Work

**Natural Light:**
- Golden hour glow
- Soft morning light
- Harsh midday sun
- Blue hour twilight
- Overcast diffused light

**Artificial Light:**
- Neon reflections
- Warm candlelight
- Harsh fluorescent
- Soft lamp glow
- Streetlight pools

**Mood Descriptors:**
- Hazy, dreamlike
- Crisp, clear
- Moody, atmospheric
- Electric, vibrant
- Meditative, calm

---

## Multi-Shot Workflow

### Building Longer Sequences

Since Hailuo works best at 4-6 seconds:

**Step 1:** Plan shot sequence
- Shot 1 (6s): Wide establishing
- Shot 2 (6s): Medium action
- Shot 3 (6s): Close-up reaction
- Total: 18 seconds of footage

**Step 2:** Generate each shot separately
- Use same Subject Reference across all shots
- Maintain consistent lighting/mood descriptions
- Keep environmental details consistent

**Step 3:** Chain in post-production
- Edit clips together
- Add transitions as needed
- Result: Seamless longer sequence

**Step 4:** Optional temporal trimming
- Use middle 2 seconds of each 4-second clip
- Results in highest-quality stable footage

---

## Enhance Prompt Parameter

### When to Keep It Enabled (Default):
- General creative work
- Want AI optimization
- Exploring ideas
- Don't need precise technical control

### When to Disable It:
- Need exact camera movements
- Technical specifications required
- Precise control over all elements
- Commercial/client work with specific requirements

**Example where you'd disable:**
```
enhance_prompt: false

Prompt: Product demonstration. Static medium shot, no camera movement. 
The bottle rotates exactly 180 degrees clockwise over 4 seconds on white 
seamless background. Bright, even studio lighting.
```

---

## Scene Complexity Guidelines

### Keep It Focused

**Maximum elements per scene:**
- 1 primary subject
- 2-3 secondary elements
- Clear action/movement
- Single environment
- Consistent lighting

### ✅ Focused Scene:
```
A barista pours steamed milk into a latte, creating a leaf pattern. Steam rises 
as she works with concentration. [Close-up, slow dolly-in on the pour]. 
Warm coffee shop lighting, cozy atmosphere.
```

**Elements:** Barista (1), latte (2), steam (3), coffee shop context (environment)

### ❌ Overcomplicated Scene:
```
A barista makes a latte while a customer reads a newspaper, another customer 
works on laptop, delivery person enters with boxes, phone rings, manager counts 
register, espresso machine steams, music plays, sunlight through window changes, 
dog walks by outside...
```

**Too many elements competing for attention.**

---

## Quick Reference Checklist

Before submitting a Hailuo 2.3 prompt:

- [ ] **Duration**: 4-6 seconds for stability
- [ ] **Subject defined**: Clear who/what is in scene
- [ ] **Action specified**: What subject does
- [ ] **Camera movement**: Bracketed if needed
- [ ] **Lighting described**: Environmental light quality
- [ ] **Mood set**: Atmosphere and style
- [ ] **Subject Reference**: Uploaded if character consistency needed
- [ ] **Length check**: 3-4 clear sentences, not overly long
- [ ] **Conflict check**: No contradictory instructions

---

## Template Examples

### Basic Template:
```
[Camera movement], [subject description] [action] in [environment]. 
[Lighting and atmosphere].
```

### Emotion-Focused Template:
```
[Subject with emotional state] [action with emotion progression] in [environment]. 
[Camera movement]. [Lighting that supports mood].
```

### Image-to-Video Template:
```
[Reference image uploaded]

[Subject] [action from pose], [emotional change]. [Camera movement]. 
[Atmospheric evolution].
```

---

**Pro Tip:** Hailuo 2.3's strength is motion realism and emotion rendering in short clips. Play to these strengths: 4-6 seconds, natural movement, emotional nuance, realistic physics. Chain clips together in post for longer sequences.
