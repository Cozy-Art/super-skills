# Nano Banana 2.1 — Parameters

Native endpoint (Gemini API, Interactions API): `POST https://generativelanguage.googleapis.com/v1beta/interactions` · header `x-goog-api-key: <key>` · model `gemini-nano-banana-2.1`. Also available on Google Cloud (Gemini Enterprise Agent Platform, formerly Vertex AI) and through wrappers.

*Verified against the Gemini API model card, image-generation guide, changelog and pricing pages (ai.google.dev), October 2026. Items marked (unverified) could not be confirmed first-party.*

## Model Lineup

| Model | ID | Status | Sizes | Thinking | References |
|---|---|---|---|---|---|
| **Nano Banana 2.1** | `gemini-nano-banana-2.1` | GA, 2026-10-06 | 1K (default), 2K, 4K | minimal · **medium** (default) · high | ≤14 total: ≤10 object, ≤4 character |
| Nano Banana 2 | `gemini-3.1-flash-image` | Deprecated (no shutdown date) | 512px, 1K, 2K, 4K | minimal (default) · high | ≤10 object, ≤4 character |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | GA | 1K only | minimal (default) · high | ≤14 object, no character |
| Nano Banana Pro | `gemini-3-pro-image` | GA | 1K, 2K, 4K | always on | ≤6 object, ≤5 character, ≤3 style |

## Request Fields (Interactions API)

| Field | Values | Default | Notes |
|---|---|---|---|
| `model` | `gemini-nano-banana-2.1` | — | Pin it; don't send the deprecated v2 string. |
| `input` | string, or ordered content blocks (text, image, video, PDF) | — | Put the text block and the reference images in one ordered list; order is how "the second image" resolves. |
| `response_format.type` | `image` | — | Request image output. The model can also return text. |
| `response_format.aspect_ratio` | see table below | (unverified: 1:1 for text-only; edits tend to follow the source) | Set explicitly. |
| `response_format.image_size` | `1K` `2K` `4K` | `1K` | **Uppercase K** — lowercase is rejected. No 512px on 2.1. |
| `response_format.mime_type` | `image/jpeg` (documented example); `image/png` (unverified) | — | PNG suits text/UI/graphics if your client offers it. |
| `generation_config.thinking_level` | `minimal` `medium` `high` | `medium` | Thinking can't be turned off. Set it explicitly for reproducible latency/cost. |
| `tools` | `[{"type": "google_search"}]` | off | Search grounding (Google Web + Image Search). Image-search sub-option field name: unverified. |
| `previous_interaction_id` | ID from the prior turn | — | Conversational editing / continuation. |
| `system_instruction` | string | — | (unverified for image models) Persistent art-direction rules. |

**Not available:** negative prompt, seed, guidance/steps, width/height, mask upload. Sampling params (`seed`, `temperature`, `topP`, `topK`, `logprobs`) are reported to return an API error on Cloud (unverified — secondary source). Structured outputs, function calling, caching, code execution, URL context, Maps grounding and Live API are listed as unsupported.

## Aspect Ratios

First-party confirmed for 2.1: `1:4` `4:1` `1:8` `8:1` (changelog — "wide and panoramic aspect ratio generation … across 1K, 2K, and 4K"), plus `1:1` `5:4` `16:9` `3:2` in documented examples.

Standard Gemini image set, expected but not individually confirmed for 2.1 (confirm on your platform): `1:1` `2:3` `3:2` `3:4` `4:3` `4:5` `5:4` `9:16` `16:9` `21:9`.

Each ratio × tier maps to fixed pixel dimensions (e.g. `1:1` = 1024² at 1K). Read the official table rather than hard-coding sizes. 2.1 fixes the tiling artifacts Nano Banana 2 showed on 1:4 / 4:1 / 1:8 / 8:1 at 2K and 4K.

## Limits

| Spec | Value |
|---|---|
| Inputs | text, image, video, PDF |
| Outputs | image, text |
| Input tokens | 131,072 |
| Output tokens | 32,768 |
| References per request | ≤14 (≤10 object, ≤4 character) |
| Batch API | supported (half price) |
| Flex / priority inference | not supported |
| Watermark | SynthID on every generated image |

No documented maximum prompt length beyond the token window. Wrappers impose their own (fal documents a prompt range of 3–50,000 characters — unverified, wrapper-specific).

## Pricing (Gemini API, paid tier, USD)

| | Standard | Batch |
|---|---|---|
| Input (text/image/video) | $1.50 / 1M tokens | $0.75 / 1M |
| Output text + thinking | $7.50 / 1M | $3.75 / 1M |
| Output image | $30 / 1M tokens ≈ **1K $0.0336 · 2K $0.0504 · 4K $0.113** | ≈ 1K $0.0168 · 2K $0.0252 · 4K $0.0567 |

No free tier for this model. Thinking tokens are billed; interim "thought images" are not.

## Recommended Combinations

| Workflow | Ratio | Size | Thinking | Grounding |
|---|---|---|---|---|
| Ideation / contact sheets | target | `1K` | `minimal` | off |
| Routine scene or edit | target | `1K`–`2K` | `medium` | off |
| Typography, infographic, menu | `16:9` `4:5` `2:3` | `2K` | `high` | off |
| Multi-reference composite / groups | target | `2K` | `high` | off |
| Panorama / banner | `4:1` `8:1` `1:4` `1:8` | `2K`–`4K` | `medium`–`high` | off |
| Current data visual | `16:9` | `2K` | `medium`–`high` | **on** |
| Final hero / print | target | `4K` (if your plan offers it) | `high` | as needed |

## Example Body

```json
{
  "model": "gemini-nano-banana-2.1",
  "input": [
    {"type": "text", "text": "Using the attached portrait as the woman's identity and the attached bottle photo as the product..."},
    {"type": "image", "mime_type": "image/png", "data": "<BASE64_1>"},
    {"type": "image", "mime_type": "image/png", "data": "<BASE64_2>"}
  ],
  "response_format": {"type": "image", "mime_type": "image/jpeg", "aspect_ratio": "4:5", "image_size": "2K"},
  "generation_config": {"thinking_level": "high"}
}
```

Follow-up edit: same shape with `"input": "Change only…"` and `"previous_interaction_id": "<ID>"`.

## Nano Banana 2 → 2.1 Migration

| v2 habit | 2.1 |
|---|---|
| `gemini-3.1-flash-image` | `gemini-nano-banana-2.1` |
| `512px` tier | Gone — use `1K`, downsample client-side |
| Thinking default `minimal` | Default `medium` — set `minimal` explicitly for throughput jobs |
| Panoramas with seams at 2K/4K | Fixed — re-render old panoramic work |
| Vague edit prompts | Change + keep-list |
| Anonymous multi-image prompts | Role per reference, by content |

## Wrappers

fal (`image_urls`, `num_images`, `output_format`, `enable_web_search`, `safety_tolerance`…) and Runware (`positivePrompt`, `width`/`height`, `inputs.referenceImages`…) expose their own fields. Document those as platform features; never mix them into a native Gemini request.
