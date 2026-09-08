# Luma Uni-1.1 — Parameters Reference

Complete API parameter specifications for the Luma Agents API.

---

## API Endpoint

```
Base URL:  https://agents.lumalabs.ai
Generate:  POST /v1/generations
Poll:      GET  /v1/generations/{id}
List:      GET  /v1/generations?limit=N&offset=N
Delete:    DELETE /v1/generations/{id}

Authentication: Authorization: Bearer <LUMA_AGENTS_API_KEY>
```

**Important:** Uni-1 / Uni-1.1 models are only available via the Agents API (`agents.lumalabs.ai`). The legacy Dream Machine API (`api.lumalabs.ai`) only supports Photon/Photon Flash models.

---

## Complete Parameter Reference

All parameters passed via `POST /v1/generations`:

| Parameter | Type | Default | Valid Values | Notes |
|-----------|------|---------|-------------|-------|
| `prompt` | string | **required** | 1–6,000 chars | Primary creative control |
| `type` | string | `"image"` | `"image"`, `"image_edit"` | Generation vs. editing mode |
| `model` | string | `"uni-1"` | `"uni-1"`, `"uni-1-max"` | Same wire format; `-max` gives higher quality |
| `aspect_ratio` | string | `null` | 9 values (see table) | `null` lets model infer from prompt content |
| `style` | string | `"auto"` | `"auto"`, `"manga"` | `manga` requires portrait ratio |
| `output_format` | string | `null` | `"png"`, `"jpeg"` | `null` lets model pick based on content |
| `web_search` | boolean | `false` | `true`, `false` | Searches web for visual references before generating |
| `image_ref` | array | `[]` | Up to 9 (`image`); up to 8 (`image_edit`) | URL or base64 with `media_type` |
| `source` | object | — | URL or base64 | **Required** for `image_edit`; **forbidden** for `image` |
| `user_id` | string | — | Max 256 chars | Stable opaque end-user ID; recommended for partners |
| `callback_url` | string | — | Public HTTPS endpoint | Receives generation status updates via POST |

---

## Aspect Ratios (All 9)

| Value | Orientation | Typical Use Case |
|-------|------------|-----------------|
| `3:1` | Ultra-wide landscape | Panoramic banners |
| `2:1` | Wide landscape | Website headers |
| `16:9` | Standard widescreen | Hero images, desktop wallpapers |
| `3:2` | Classic landscape | Traditional photography |
| `1:1` | Square | Social media, profile pictures |
| `2:3` | Classic portrait | Book covers, posters |
| `9:16` | Standard portrait | Mobile wallpapers, Stories |
| `1:2` | Tall portrait | Vertical banners |
| `1:3` | Ultra-tall portrait | Tall signage |

**Default behavior:** When `aspect_ratio` is `null`, the model infers the appropriate ratio from the prompt content. Set explicitly when the ratio is critical to the design.

---

## Style Presets

| Value | Description | Aspect Ratio Constraint |
|-------|------------|------------------------|
| `"auto"` | Model selects best style for the prompt | All 9 ratios supported (or omit) |
| `"manga"` | Manga/anime with ink outlines and screentone shading | **Portrait only** (`2:3`, `9:16`, `1:2`, `1:3`) |

⚠️ **Critical:** `style: "manga"` with `type: "image"` and a landscape or square ratio returns **HTTP 422**. Always use a portrait ratio with manga style.

---

## Model Tier Comparison and Pricing

| Model | T2I (2K) | Image Edit | Quality | Generation Time |
|-------|---------|-----------|---------|----------------|
| `uni-1` | $0.0404 | $0.0434 | Standard | ~31 seconds |
| `uni-1-max` | $0.1000 | ~$0.1030 | Higher | Longer |

`uni-1-max` is a drop-in replacement — same prompts, same parameters, better output quality.

### Reference Image Pricing (`uni-1`)

Each `image_ref` beyond zero adds **$0.0030** per image:

| `image_ref` count | `uni-1` price |
|-------------------|--------------|
| 0 (T2I only) | $0.0404 |
| 1 | $0.0434 |
| 2 | $0.0464 |
| 3 | $0.0494 |
| 4 | $0.0524 |
| 5 | $0.0554 |
| 6 | $0.0584 |
| 7 | $0.0614 |
| 8 | $0.0644 |
| 9 | $0.0674 (image type only) |

---

## Validation Rules

| Rule | Constraint |
|------|-----------|
| `prompt` | Required; 1–6,000 characters |
| `model` | `uni-1` or `uni-1-max`; defaults to `uni-1` |
| `type` | `image` or `image_edit`; defaults to `image` |
| `aspect_ratio` | One of 9 supported values or `null` |
| `style: "manga"` | Requires portrait ratio when `type: "image"` — 422 otherwise |
| `output_format` | `png`, `jpeg`, or `null` |
| `image_ref` | Max 9 entries for `image`; max 8 for `image_edit` |
| `image_ref[].url` | Publicly accessible; max 50 MB per image |
| `source` | Required for `image_edit`; forbidden for `image` — 422 if both present |

---

## Output Specifications

| Spec | Value | Notes |
|------|-------|-------|
| Resolution | 2048px (2K) on longest edge | All requests; no higher option via API |
| Formats | PNG, JPEG | PNG = lossless; JPEG = smaller, better for photos |
| Aspect ratios | 9 options | See table above |
| Output URL expiry | **1 hour** (presigned URL) | Download promptly or poll `GET /v1/generations/{id}` for fresh URL |
| Generation time | ~31 seconds (`uni-1`) | Per Luma benchmark data |

**Polling states:** `queued` → `processing` → `completed` / `failed`

---

## Failure Codes

| Code | Cause |
|------|-------|
| `content_moderated` | Prompt violated content policy |
| `generation_failed` | Internal generation error |
| `budget_exhausted` | Account credit limit reached |
| `output_not_found` | Output URL expired or not found |
| `image_too_large` | Input image exceeds 50 MB |
| `unsupported_format` | Input image format not supported |
| `corrupt_input` | Invalid base64 or unreadable file |
| `invalid_request` | Parameter validation failed (check aspect_ratio + style combo) |
| `rate_limited` | Too many concurrent requests |

---

## SDK Support

- Python SDK
- TypeScript / JavaScript SDK
- Go SDK
- CLI

---

## Web Platform Pricing (Luma App)

| Model | Action | Credits per image |
|-------|--------|-----------------|
| Uni-1 | Create or Modify | 30 credits |

Subscription plans:
- Plus: $30/month
- Pro: $90/month
- Ultra: $300/month

---

## Provisioned Throughput

For production workloads requiring guaranteed capacity. Includes a **no-train guarantee** — data processed through Provisioned Throughput is never used to train Luma models. Contact Luma sales for plan details.

---

## Version History and Migration

### Timeline

| Version | Release Date | Key Event |
|---------|-------------|---------|
| Uni-1 | March 22, 2026 | Initial launch |
| Uni-1.1 | May 4–5, 2026 | API launch; `uni-1.1-max` debuts at #1 Arena Elo |

### Uni-1 → Uni-1.1: Zero Code Changes Required

`uni-1` IS the Uni-1.1 standard tier. To upgrade to max quality:
```json
{ "model": "uni-1-max", "prompt": "..." }
```

### API URL Change

| Version | Base URL |
|---------|---------|
| Photon / Legacy | `https://api.lumalabs.ai/dream-machine/v1/` |
| Uni-1 / Uni-1.1 | `https://agents.lumalabs.ai/v1/` |

### Photon → Uni-1.1 Migration

| Photon parameter | Uni-1.1 equivalent |
|-----------------|-------------------|
| `character_ref.identity0.images[...]` | `image_ref` + `"Use IMAGE1 as a CHARACTER reference"` in prompt |
| `style_ref[].weight` | `image_ref` + `"Use IMAGE1 as a STYLE reference"` in prompt |
| `modify_image_ref.url + weight` | `source.url` + `type: "image_edit"` |
| `api.lumalabs.ai` endpoint | `agents.lumalabs.ai` endpoint |

Key differences from Photon:
- Architecture: Diffusion → Autoregressive reasoning transformer
- References: Up to 4 with `weight` → Up to 9 with explicit role labels
- Reasoning: None → Native chain-of-thought; state-of-the-art spatial logic
- Text rendering: Basic → Reliable on signs, labels, surfaces
