# GPT Image 2 — Parameters Reference

Complete API specifications for `gpt-image-2`.

---

## Generation Endpoint

**`POST https://api.openai.com/v1/images/generations`**

| Parameter | Type | Values | Default | Notes |
|-----------|------|--------|---------|-------|
| `model` | string | `gpt-image-2` | — | Required |
| `prompt` | string | Up to 32,000 chars | — | Required |
| `size` | string | Any WxH within constraints, or `auto` | `auto` | Both edges multiples of 16; max edge < 3840px; ratio ≤ 3:1; total pixels 655,360–8,294,400 |
| `quality` | string | `low`, `medium`, `high`, `auto` | `auto` | Drives cost and rendering fidelity |
| `thinking` | string | `off`, `low`, `medium`, `high` | `off` | Reasoning budget before rendering — key differentiator of this model |
| `n` | integer | 1–10 | 1 | Batched images share style coherence (different from calling endpoint N times) |
| `output_format` | string | `png`, `jpeg`, `webp` | `png` | GPT image models only |
| `output_compression` | integer | 0–100 | 100 | JPEG and WebP only |
| `background` | string | `transparent`, `opaque`, `auto` | `auto` | ⚠️ `transparent` is **NOT supported** on `gpt-image-2` — use `opaque` or `auto` |
| `moderation` | string | `auto`, `low` | `auto` | Content-filtering strictness |
| `seed` | integer | Any int32 | random | Reduces variance; does NOT guarantee identical output |
| `partial_images` | integer | 0–3 | 0 | For streaming responses |
| `user` | string | Free-form | — | Hashed user ID for abuse detection |

---

## Edit Endpoint

**`POST https://api.openai.com/v1/images/edits`**

Accepts: `prompt`, `image_urls` (1–16 images), `quality`, `size`, `output_format`, `output_compression`

**Note:** The `input_fidelity` parameter present on `gpt-image-1.5` is **disabled** for `gpt-image-2` — always processes image inputs at maximum fidelity automatically. Passing it will cause an error.

| Parameter | Notes |
|-----------|-------|
| `image_urls` | 1–16 reference images; JPEG, PNG, WebP |
| `quality` | Same tiers as generation; use `high` for identity-preserving edits |
| `size` | Output size; aspect ratio from source is preserved when not specified |
| `input_fidelity` | ⛔ Disabled — do not pass this parameter |

---

## Size Values

| Label | Resolution | Notes |
|-------|-----------|-------|
| Square | `1024x1024` | Fastest to generate; good general default |
| HD Landscape | `1536x1024` | Standard landscape |
| HD Portrait | `1024x1536` | Standard portrait |
| 2K / QHD | `2560x1440` | Recommended upper reliability boundary |
| Near-4K | `3824x2144` | Experimental — use instead of `3840x2160` to avoid edge constraint |
| 4K / UHD | `3840x2160` | Documented target; enforce `< 3840` max edge rule strictly |
| Ultra-wide panoramic | `3072x1024` | More token-efficient than square at same pixel count |

**Supported aspect ratios:** 1:1, 4:3, 3:4, 3:2, 2:3, 16:9, 9:16, 2:1, 1:2, 21:9, 9:21, 3:1, 1:3

**Token efficiency:** Rectangular aspect ratios use fewer output tokens than square at equivalent pixel counts. A 3:1 ratio is significantly cheaper than 1:1 at the same pixel budget — use wide/tall formats when appropriate.

### Resolution Constraints (Hard)
- Maximum edge length: < 3840px
- Both edges must be multiples of 16px
- Long-to-short edge ratio: must not exceed 3:1
- Total pixels: minimum 655,360 — maximum 8,294,400
- Outputs above 2560×1440 (2K) are **experimental**
- 4K is documented but treat as experimental; use 2K as reliable ceiling and upscale externally if needed

---

## Quality vs. Cost

| Quality | 1024×1024 | 1024×1536 | 1536×1024 | Best For |
|---------|-----------|-----------|-----------|---------|
| `low` | $0.006 | $0.005 | $0.005 | Ideation, drafts, high-volume pipelines |
| `medium` | $0.053 | $0.041 | $0.041 | Most production work |
| `high` | $0.211 | $0.165 | $0.165 | Dense text, UI elements, close-up portraits |

**Token pricing:**
- Text input: $5.00 / 1M tokens
- Image input: $8.00 / 1M tokens
- Cached image input: $2.00 / 1M tokens
- Image output: $30.00 / 1M tokens

---

## Thinking Mode: Full Decision Matrix

| Level | Planning Depth | Best Use Case | Cost Multiplier |
|-------|---------------|---------------|-----------------|
| `off` | None | Creative/loose prompts, landscapes, abstract art | 1× baseline |
| `low` | Light planning | Product shots, hero images, standard portraits | ~1.2× |
| `medium` | Heavier planning | Infographics, diagrams, slides, scenes with counted elements | ~1.5–2× |
| `high` | Maximum reasoning | Complex multilingual layouts, strict technical diagrams | ~2–4× |

**Practical rule:** If the prompt contains a number, a label, or a positional constraint ("three arrows pointing right"), move up one tier. If purely atmospheric ("a cozy forest at dusk"), drop a tier.

---

## Output Formats

| Format | Supports Transparency | Supports Compression | Notes |
|--------|----------------------|---------------------|-------|
| PNG | ⛔ No (on `gpt-image-2`) | No | Default; best for lossless output |
| JPEG | No | Yes (0–100%) | Best for photos when file size matters |
| WebP | No | Yes (0–100%) | Best for web delivery |

**Transparency:** `gpt-image-2` does not support `background: "transparent"`. Use `opaque` or `auto`, then apply downstream background-removal if a transparent asset is needed.

---

## Rate Limits & API Access

- Available on Tier 1 and above (requires billing setup on Free tier)
- Tier 1 default: ~50 requests per minute
- Read `x-ratelimit-remaining-requests` and `x-ratelimit-remaining-tokens` headers and throttle before hitting limits
- Response images: base64-encoded data or URL format
- **URL responses expire after 1 hour** — copy to own S3/CDN immediately

---

## Recommended Parameter Combinations by Use Case

| Use Case | Quality | Size | Thinking | Notes |
|----------|---------|------|----------|-------|
| Ideation / batch drafts | `low` | `1024x1024` | `off` | Fastest, cheapest |
| Standard editorial portrait | `high` | `1024x1536` | `low` | Portrait orientation |
| Product photography | `high` | `1536x1024` | `low` | Landscape with detail |
| Dense text / signage | `high` | `1536x1024` | `medium` | Text accuracy critical |
| UI mockup | `high` | `1024x1536` | `medium` | Mobile portrait |
| Infographic / diagram | `high` | `1536x1024` | `medium` to `high` | Counted elements |
| Complex multilingual layout | `high` | `2560x1440` | `high` | Max reasoning needed |
| Multi-image compositing | `high` | Match source | `low` to `medium` | Edit endpoint |
| Virtual try-on | `high` | Match person image | `medium` | Preserve identity precisely |

---

## API Code Reference

### Python — Full-Featured Generation

```python
import base64
from pathlib import Path
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="gpt-image-2",
    prompt=(
        "A minimalist diagram of an OAuth 2.1 authorization code flow with PKCE. "
        "Five boxes labeled in English: User, Client, Auth Server, Resource Server, Token. "
        "Sharp sans-serif text, off-white background, teal accent arrows."
    ),
    size="1536x1024",
    quality="high",
    n=2,
    thinking="medium",
    response_format="b64_json",
)

out_dir = Path("out")
out_dir.mkdir(exist_ok=True)

for i, image in enumerate(response.data):
    png_bytes = base64.b64decode(image.b64_json)
    (out_dir / f"output_{i}.png").write_bytes(png_bytes)
```

### Python — Multi-Image Edit / Compositing

```python
response = client.images.edit(
    model="gpt-image-2",
    image=[
        open("base_scene.png", "rb"),
        open("style_reference.png", "rb"),
    ],
    prompt=(
        "Image 1: base scene to preserve. "
        "Image 2: style reference. "
        "Apply Image 2's watercolor brushwork and palette to Image 1. "
        "Preserve all subjects, composition, and proportions from Image 1. "
        "No watermark."
    ),
    quality="high",
)
```

### Python — Retry Wrapper (Production)

```python
import time
from openai import OpenAI, RateLimitError, APIStatusError

client = OpenAI()

def generate_with_retry(prompt: str, tries: int = 3):
    delay = 1.0
    for attempt in range(tries):
        try:
            return client.images.generate(
                model="gpt-image-2",
                prompt=prompt,
                size="1024x1024",
                quality="high",
                n=1,
            )
        except RateLimitError:
            time.sleep(delay)
            delay *= 2
        except APIStatusError as e:
            if 500 <= e.status_code < 600 and attempt < tries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
    raise RuntimeError("gpt-image-2 retries exhausted")
```

⚠️ **Do not retry 400s, 401s, or content-policy 429s** — these fail for a reason and retrying wastes credits.

### Batch for Coherent Variants

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="Four hero illustrations for an API documentation landing page, shared color palette, shared line weight.",
    size="1536x1024",
    quality="high",
    n=4,
    thinking="low",
)
```

`n > 1` returns images that share composition and style — different from calling the endpoint multiple times in parallel, which produces unrelated results.

---

## Version Context

| Model | Release | Key characteristics |
|-------|---------|-------------------|
| `gpt-image-1` | April 2025 | First API image model; no reasoning; unreliable text |
| `gpt-image-1-mini` | 2025 | Cost/throughput optimized; fixed sizes; for drafts and high-volume |
| `gpt-image-1.5` | December 2025 | Improved instruction following; supports `input_fidelity`; supports transparent background |
| `gpt-image-2` | April 21, 2026 | Current flagship; Thinking Mode; flexible resolutions to 4K; near-perfect text; web search; **no transparent support** |

### Migration from `gpt-image-1` or `gpt-image-1.5`

1. Swap model ID to `"gpt-image-2"` — existing SDK integrations continue working
2. Remove `input_fidelity` — disabled, causes errors if passed
3. Replace `background: "transparent"` with `"opaque"` + post-process
4. Add `thinking` for prompts with counted elements, labels, or spatial constraints
5. Drop generic quality boosters (`8K, masterpiece, ultra-detailed`) — replaced with specific lighting/material/composition language
6. Test at `quality: "low"` first; upgrade to `"high"` for production

### When to Keep Older Models

| Scenario | Recommended model |
|----------|------------------|
| Need transparent PNG output | `gpt-image-1.5` |
| Backward-compatible existing pipeline | Keep current while validating |
| Maximum cost efficiency at scale | `gpt-image-1-mini` |
| All new production work | `gpt-image-2` |
