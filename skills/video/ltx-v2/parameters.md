# LTX-2 — Parameters Reference

---

## Fast vs. Pro Mode Comparison

| Specification | Fast | Pro |
|--------------|------|-----|
| **Max duration** | **20 seconds** (v2.3) | 10 seconds |
| **Resolution** | 1080p, 1440p, 4K | 1080p, 1440p, 4K |
| **Inference speed** | 2× faster than Pro | Baseline |
| **Compute cost** | 1/10 of baseline | 1/5 of baseline |
| **Visual fidelity** | Good — production-ready | Higher — finer detail, truer color, smoother motion |
| **First/last frame interp.** | ✅ Yes (v2.3) | ❌ No |
| **I2V max duration** | 20 seconds | 10 seconds |
| **Best use** | Drafts, iteration, batch, social content, extended duration | Hero shots, client deliverables, portfolio, character close-ups |

> **Key insight from independent benchmarking:** "There is a much bigger disparity between LTX-2 Pro and LTX-2 Fast compared to the difference between competing models' standard and fast variants." Fast is efficient and good — Pro is noticeably better.

---

## Core API Parameters

| Parameter | Type | Required | Default | Valid Values | Notes |
|-----------|------|----------|---------|-------------|-------|
| `positivePrompt` | string | Yes | — | 2–10,000 chars | Single flowing paragraph; present tense |
| `duration` | enum | No | `6` | 6, 8, 10 (Pro); 6, 8, 10, 12, 14, 16, 18, 20 (Fast) | Seconds |
| `fps` | integer | No | `25` | 24, 25, 48, 50 | Higher = smoother motion, more VRAM |
| `width` | integer | No | — | Supported values (see resolution table) | Must pair with height |
| `height` | integer | No | — | Supported values | Must pair with width |
| `generate_audio` | boolean | No | `true` (WaveSpeed) / `false` (Runware) | true / false | Ambient + SFX + dialogue sync; not music |
| `seed` | integer | No | random | Any integer | Lock for reproducibility and cross-shot consistency |
| `numberResults` | integer | No | `1` | 1–20 | Batch with different seeds per result |
| `outputFormat` | enum | No | `MP4` | MP4, WEBM, MOV | MOV for Apple ecosystem workflows |
| `outputQuality` | integer | No | `95` | 20–99 | Higher = larger file size |

---

## Resolution and Aspect Ratio Options

| Aspect Ratio | Resolution Options | Notes |
|-------------|------------------|-------|
| **16:9** | 1920×1080, 2560×1440, 3840×2160 (4K) | Default; standard cinematic |
| **9:16** | 1080×1920 | Supported in LTX-2.3 Fast; vertical social content |
| Custom | Any supported width/height pair | Unconventional ratios may reduce temporal stability |

**fal.ai endpoint note:** Output is fixed at 16:9 regardless of input image dimensions. Prepare I2V source images in 16:9 or expect automatic cropping.

---

## FPS Options and Trade-offs

| FPS | Effect | VRAM Impact |
|-----|--------|------------|
| 24 | Standard cinematic cadence | Lower |
| 25 | Default; slightly smoother than 24 | Lower |
| 48 | High frame rate — smooth, modern look | Higher |
| 50 | Maximum available; very smooth motion | Highest |

**Note:** 48/50 FPS available only at 1080p and 1440p. 4K is limited to 24/25 FPS.

---

## Duration Selection

| Duration | Best For |
|----------|---------|
| 6s | Single action beat; minimal camera movement; social clips; baseline iteration |
| 8s | Two to three beats; moderate camera choreography |
| 10s | Complex sequences; multi-beat with phase prompting; Pro max |
| 12–20s | Extended narrative; multi-phase workflows; **Fast mode only** |

**Default baseline:** 6 seconds, 1080p, 25 FPS — minimum cost and time for draft iteration.

---

## Audio Generation Behavior

`generate_audio: true` produces **synchronized ambient soundscapes and effects** that match on-screen motion. This is not a music generation feature.

### What Audio Generation Produces

| Scene content | Generated audio |
|--------------|----------------|
| Rain visible in scene | Rain ambience |
| Footsteps on stone | Stone impact sounds |
| Market scene | Crowd murmur, fabric rustling |
| Dialogue in prompt quotes | Synchronized voice/lip-sync |
| Cabin interior with wind outside | Faint wind, wood creak |
| Studio product shot | Ambient studio hum |

### Audio Platform Defaults

- **WaveSpeed AI:** `generate_audio: true` by default
- **Runware:** `generate_audio: false` by default — must explicitly enable

### Spoken Dialogue Syntax

Place dialogue in quotation marks in the prompt, with a speaker attribution:

```
Reporter (live): "Thank you, Sylvia. And yes — this morning, here in the quiet town of New Castle, Vermont… black gold has been found!"
```

Characters can speak and sing in multiple languages. Specify language or accent if needed.

---

## Output Formats

| Format | Best For |
|--------|---------|
| MP4 | Universal; web delivery; default |
| WEBM | Web-optimized; open format |
| MOV | Apple ecosystem; Final Cut Pro; ProRes workflows |

---

## Fast vs. Pro Decision Framework

| Scenario | Recommended Mode |
|---------|-----------------|
| First draft of any concept | **Fast** |
| Batch-testing 3–5 prompt variations | **Fast** |
| Social media posts, short-form content | **Fast** |
| Duration > 10 seconds required | **Fast** (only option) |
| First/last frame interpolation needed | **Fast** (only option) |
| Hero shot for client deliverable | **Pro** |
| Final frame for portfolio | **Pro** |
| Character close-up with facial nuance | **Pro** |
| Product demo for marketing material | **Pro** |
| Iterating to find creative direction | **Fast → Pro for winner** |

---

## Version History

| Version | Release | Key additions |
|---------|---------|--------------|
| LTX-2.0 | January 2026 | Initial release; 14B video + 5B audio; 18× faster than Wan 2.2 |
| LTX-2.1 | — | Architecture refinements; same prompting |
| LTX-2.3 | March 2026 | New VAE reducing oversaturation; improved Fast-mode detail; extended Fast to 20s; added 9:16 aspect ratio |

**All versions share identical prompting principles.**

---

## Local Deployment

LTX-2 runs locally on consumer GPUs via **LTX Desktop**. Hardware requirements vary by resolution and duration. API access via ltx.io, fal.ai, WaveSpeed AI, and Runware.
