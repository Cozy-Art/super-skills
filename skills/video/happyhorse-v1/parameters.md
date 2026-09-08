# HappyHorse 1.0 — Parameters Reference

Complete API parameter specifications for all HappyHorse 1.0 endpoints.

---

## Text-to-Video & Image-to-Video Parameters

| Parameter | Type | Range / Options | Default | Notes |
|-----------|------|-----------------|---------|-------|
| `prompt` (`positivePrompt`) | string | 1–2,500 chars | — | Required |
| `negative_prompt` | string | — | — | Optional; supported on I2V |
| `resolution` | enum | `720p`, `1080p` | `1080p` | Also accepts explicit `width` + `height` |
| `duration` | integer | 3–15 seconds | 5 | Step of 1 second |
| `aspect_ratio` | enum | `16:9`, `9:16`, `1:1`, `4:3`, `3:4` | `16:9` | T2V only |
| `seed` | integer | 0–2,147,483,647 | random | Set for reproducibility |
| `watermark` | boolean | true / false | false | I2V endpoint |

---

## Video Edit Endpoint Parameters

| Parameter | Type | Range / Options | Default | Notes |
|-----------|------|-----------------|---------|-------|
| `video_url` | string | MP4/MOV, ≤100 MB, 3–60s, >8 fps | required | Source clip |
| `prompt` | string | ≤2,500 chars | required | Edit instruction; use `[Image 1]`–`[Image 9]` for refs |
| `reference_image_urls` | list | Up to 5, ≥300px, ≤10 MB each | optional | JPEG, PNG, or WEBP |
| `resolution` | enum | `720p`, `1080p` | `1080p` | Aspect ratio preserved from source |
| `audio_setting` | enum | `auto`, `origin` | `auto` | `origin` = preserve original audio |
| `seed` | integer | 0–2,147,483,647 | random | Reproducibility |

### Video Edit Input Constraints

- Input formats: MP4, MOV (H.264 recommended)
- Max input file size: 100 MB
- Input duration: 3–60 seconds
- Output duration: matches input, capped at 15 seconds (inputs >15s truncated to first 15s)
- Input resolution: longer side ≤ 2160px, shorter side ≥ 320px
- Input aspect ratio: between 1:2.5 and 2.5:1
- Input frame rate: > 8 fps
- Reference images: ≥ 300px, ≤ 10 MB each

---

## Runware API — Output Format Options

| Parameter | Options | Default | Notes |
|-----------|---------|---------|-------|
| `outputFormat` | `MP4`, `WEBM`, `MOV` | `MP4` | H.264 MP4 recommended for general use |
| `outputQuality` | 20–99 | 95 | Higher = larger file size |
| `numberResults` | 1–4 | 1 | Each result uses a different seed |

### frameImages (Runware API)

Pins images to specific frame positions:

| Value | Behavior |
|-------|----------|
| Single image | Defaults to first frame |
| `frame: "first"` | Named first frame |
| `frame: "last"` | Named last frame |
| `frame: -1` | Last frame (zero-based) |
| `frame: N` (integer) | Specific frame position |

Use "first frame + last frame" to bookend a generation — model fills motion between two fixed visual states.

---

## Generation Endpoints

| Endpoint | Input | Max inputs | Max duration |
|----------|-------|-----------|--------------|
| `alibaba/happy-horse/text-to-video` | Text prompt | N/A | 15s |
| `alibaba/happy-horse/image-to-video` | Image + prompt | 1 image | 15s |
| `alibaba/happy-horse/reference-to-video` | 1–9 reference images + prompt | 9 images | 15s |
| `alibaba/happy-horse/video-edit` | Video (≤60s) + up to 5 refs + prompt | 5 images | 15s output |

---

## Recommended Parameter Combinations by Use Case

| Use case | Resolution | Duration | Aspect | Audio | Mode |
|----------|------------|----------|--------|-------|------|
| Ideation / batch drafts | 720p | 5s | 16:9 or 9:16 | Off | Std |
| English talking head | 1080p | 5–8s | 16:9 | On | Pro |
| Multilingual lip-sync (CJK, DE, FR) | 1080p | 5–8s | 16:9 | On | Pro |
| Cinematic product spot | 1080p | 8–15s | 16:9 | On | Pro |
| Image-to-video animation | 1080p | 5–8s | Match input | On | Pro |
| Vertical TikTok / Reels | 1080p | 5–8s | 9:16 | On | Std |
| Multi-shot scene (up to 5 shots) | 1080p | Up to 15s total | 16:9 | On | Pro |
| Element compositing (@elements) | 1080p | 5–8s | 16:9 | On | Pro |
| Natural-language video edit | Match input | Match input | Match input | origin | Pro |

**Key insight:** Audio generation is **on by default** and adds approximately **50% to credit usage**. Turn it off (`audio: off`) for ideation runs to cut costs significantly.

---

## Pricing (fal.ai)

| Resolution | Price per second |
|------------|-----------------|
| 720p | $0.14 / second |
| 1080p | $0.28 / second |

**Example costs:**
- 720p / 5s (no audio): $0.70
- 1080p / 8s (with audio, ~50% surcharge): ~$3.36
- 1080p / 15s max: $4.20 base (+ audio surcharge)

---

## Technical Specifications

### Model Architecture

| Specification | Value |
|---------------|-------|
| Developer | Alibaba Taotian Future Life Lab (ATH AI Unit) |
| Architecture | Unified 40-layer single-stream Transformer, no cross-attention modules |
| Parameters | 15 billion |
| Inference steps | 8 (DMD-2 distilled; "Std" mode) |
| Generation time | ~38 seconds for 1080p on single NVIDIA H100 |
| Open source | No — closed source, API access only |

### Output Specifications

| Specification | Value |
|---------------|-------|
| Max resolution | 1080p (1920×1080 for 16:9) |
| Base resolution | 720p (1280×720) |
| Frame rate | 24 fps |
| Duration range | 3–15 seconds (T2V, I2V, R2V) |
| Aspect ratios | 16:9, 9:16, 1:1, 4:3, 3:4 |
| Output format | MP4 (H.264), WEBM, MOV |
| Audio | Native joint generation (dialogue, foley, ambient, music) |
| Lip-sync languages | English, Mandarin, Cantonese, Japanese, Korean, German, French |

### Prompt Limits

| Limit | Value |
|-------|-------|
| Maximum prompt length | 2,500 characters (hard API limit) |
| Optimal single-shot length | ~20 words for most T2V shots |
| Multi-shot format | Use labeled timecodes instead of long paragraphs |

---

## @element Token Compositing (fal API)

The fal text-to-video endpoint exposes a `happyhorse_elements` field:

```json
{
  "happyhorse_elements": [
    {
      "name": "product_bag",
      "description": "A tan leather tote bag with brass hardware",
      "images": ["url1", "url2", "url3"]
    }
  ]
}
```

- Maximum **3 elements** per task
- Each element: a `name`, `description`, and 2–4 input images
- Reference in prompt with `@element_name` token
- Model treats each as a distinct asset, not a blended composite

**Prompt pattern:**
```
The @product_bag sits on a marble café table, soft window light from the left,
close-up product shot, slight dolly-in. Ambient café sounds, no music.
```
