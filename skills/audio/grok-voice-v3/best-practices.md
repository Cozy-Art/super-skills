# Grok Voice 3.0 — Best Practices

Craft guidance for the `instructions` string. Section order and core rules follow xAI's Speech to Speech Prompting Guide; the rest is working practice for live voice agents.

## 1. Core Rules (from xAI's guide)

- Second person ("You are…"), Markdown headings, **short bullets** over paragraphs.
- Give **sample phrases** — the model follows them closely. Give 2–3 variants so it doesn't sound canned.
- Remove ambiguity and conflicts; one rule per bullet.
- Capitalised **ALWAYS / NEVER / EVERY** for the few rules that must hold.
- Write non-text rules in plain English ("If the caller goes quiet…"), not pseudo-code.
- Reference only tools that are attached; never script steps for capabilities the agent lacks.
- Bake key facts into the prompt (name, hours, prices, policies, full URL); answer only from them or the knowledge base; say "I don't know" otherwise.
- Don't script the greeting inside Conversation Flow — trigger the opener separately.
- **Iterate often** — small wording changes cause large behaviour shifts.

## 2. Writing Each Section

### Role & Persona
Identity + brand + disposition in 2–4 bullets. Say it's an AI and when to disclose it.

| Vague | Usable |
|---|---|
| "You are friendly." | "You are Mira, the front-desk assistant for Harbor Dental. Warm, unhurried, a little dry. You are an AI and say so if asked." |
| "Be a pirate." | "You are Captain Rook, a weathered smuggler in a tabletop game. Gruff, suspicious of strangers, softens when someone mentions the sea." |

Persona describes **behaviour and word choice**. Timbre, accent and age belong to the `voice` ID — don't write "deep British voice" and expect the sound to change.

### Objective
One or two sentences: the outcome and the fallback. "Book the caller into an available cleaning slot. If nothing fits, take a callback number and preferred times."

### Conversation Flow
- Simple agents: a short prose paragraph.
- Complex agents: numbered phases, each with **Goal / How to respond / Exit when**.
- Name the tool at the step where it's used, with its exact schema name.
- Don't front-load every branch; cover the main path plus the 2–3 most common detours.

### Guardrails & Escalation
- Scope: what it handles, what it declines ("I can't advise on medication — I can book you with the nurse line.").
- No medical, legal or financial advice unless that is explicitly the product and approved.
- Escalation triggers, concrete: caller asks for a human; two failed tool attempts; three no-match or no-input turns in a row; out-of-scope topic.
- **Pair every transfer with a spoken line** before the tool call: "Thanks for your patience — I'm connecting you now."
- Crisis-capable contexts (health, wellness, finance distress, youth): an empathetic safety path that names emergency services or a crisis line and transfers to a human. xAI calls this mandatory there.

### Voice & Communication Style
How it sounds *in words*:
- Spoken words only — no markdown, lists, emojis, stage directions or `*laughs*`.
- One or two short sentences per turn unless the caller asks for more.
- Calm tone; brief pause after questions; one question at a time.
- Silence or interruption → a short check-in ("Still with me?").
- Asked to repeat → restate the last point more simply, don't replay it verbatim.
- Vary phrasing; never repeat the same sentence twice in a call.
- **Language lock:** "Speak only English. If the caller uses another language, say in English that you support English and continue." (Or list the supported set.)

### CRITICAL INSTRUCTIONS (optional)
3–5 bullets max. Only things whose violation is a failure: disclosure, no payments over voice, confirm before booking. If everything is critical, nothing is.

## 3. Pace, Rhythm and Delivery

| Want | Lever |
|---|---|
| Slower / faster overall | `audio.output.speed` (0.7–1.5) |
| Shorter, punchier turns | "One sentence per turn; lead with the answer." |
| Warmer | Sample phrases with contractions and acknowledgements ("Got it — let's fix that.") |
| More formal | "Use full sentences, no slang, address the caller by surname." |
| Different timbre / accent | Change `voice` |
| A word said correctly | `replace` entry |
| A name heard correctly | `keyterms` entry |

Don't write "speak slowly" and also set speed 1.3 — config and prose should agree.

## 4. Numbers, Codes, Money, Dates

- Phone numbers, account IDs, confirmation codes: "Speak each character separately, joined by hyphens: 4-1-5-…". Read back exactly — no dropping, adding or reordering — then ask "Did I get that right?" If corrected, read the corrected version back.
- Money and dates: "Say amounts as words a person would say: 'forty-nine ninety-nine', 'Tuesday the fourteenth'."
- Spelling names: "Use 'A as in apple' only if the caller asks."

## 5. Unclear Input

"Respond only to clear speech. If audio is empty, garbled or cut off, ask a short clarifying question — never guess." This prevents hallucinated requests from noise.

## 6. Tool Phrasing

- Names short, `snake_case`, identical in prompt and schema: `lookup_order`, `book_slot`, `transfer_call`.
- **Preamble** before any tool call to mask latency: "One sentence before every tool call, e.g. 'Let me pull that up.'" Or put the phrase in each tool's `description`.
- **Read-only** (lookup, search, availability): call proactively, don't ask permission.
- **State-changing** (book, cancel, refund, transfer, send): restate what will happen and get a yes first.
- After a tool returns: give the gist in one sentence with at most three key details; offer more on request.
- Tool failure: one retry, then apologise briefly and use the fallback from Objective.
- Built-in server tools (`web_search`, `x_search`, `file_search`, `mcp`) need a usage rule too: "Use web_search only for current events; never for account questions."

## 7. Supervisor Pattern

When a stronger text model (or your backend) does the reasoning and Grok Voice speaks: open conversationally, one-sentence gist + ≤3 details, ≤2 sentences total, everything formatted for speech (numbers, money, phone, dates). Tell the voice agent to never read raw JSON or URLs character-by-character unless asked.

## 8. Reasoning Effort

`"high"` (default) for multi-step tasks, tool chains, policy judgement. `"none"` for simple, latency-sensitive flows (receptionist, IVR menu, game banter). Test both; xAI doesn't publish the latency difference.

## 9. Iteration Aids

- **Critique pass:** ask a strong text model to find ambiguity, missing definitions, conflicts and unstated assumptions in the prompt and return revised lines.
- **Targeted fix:** describe one observed failure ("agent books without confirming") and ask for 2–3 prompt variants addressing only that.
- Test script per release: interruption mid-sentence, 10 s silence, noisy line, off-topic ask, request for a human, a code to read back, an attempted prompt injection ("ignore your rules").

## 10. Common Mistakes

| Mistake | Why it fails | Fix |
|---|---|---|
| Paragraph-long persona essay | Diluted; rules lost | 2–4 bullets |
| "Use bullet points to list options" | Bullets get spoken or dropped | "Offer at most two options in one sentence." |
| Greeting scripted in Flow | Double or skipped greeting | Trigger opener with `response.create` |
| Mentioning `send_sms` that isn't attached | Agent promises impossible actions | Remove, or attach the tool |
| "Sound British" in instructions | Prose can't change timbre | Pick `eve` / `leo` or a custom voice |
| `*smiles*` / `[laughs]` in sample phrases | Read aloud or unpredictable | Express warmth in wording |
| Long answers | Callers interrupt; turn-taking suffers | 1–2 sentences per turn |
| Misheard brand name fixed in prose | Recognition isn't prompt-controlled | `keyterms` |
| Mispronounced name fixed in prose | Unreliable | `replace` |
| No escalation trigger | Loops forever | Concrete counts (2 tool fails, 3 no-match) |
| Facts left to the model | Hallucinated hours/prices | Put facts in the prompt or `file_search` |
| Confirm-everything | Slow, robotic | Confirm only state-changing actions |
| Conflicting tone rules ("brief" + "explain thoroughly") | Inconsistent behaviour | One rule per behaviour |
