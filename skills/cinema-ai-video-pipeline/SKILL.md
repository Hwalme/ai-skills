---
name: cinema-ai-video-pipeline
description: >-
  Use when the user wants to build or run an end-to-end AI video production
  pipeline (script -> image -> voice -> video) with a ZERO-COST stack:
  DeepSeek V3 for scriptwriting, Pollinations.ai Flux for image generation,
  edge-tts for narration, and Remotion for programmatic rendering. Covers
  provider routing, the three-form factor strategy (film / web-comic /
  commercial ad), and how to keep the pipeline free while remaining
  production-grade. Use for "make a video with AI", "AI short film
  pipeline", "zero-cost video generation", or "ComfyUI alternative".
license: MIT
compatibility: >-
  Node.js 18+ (Remotion), Python 3.8+ (edge-tts). Free/public APIs only —
  no paid keys required. Designed to be portable across film, web-comic
  (漫剧), and commercial-ad (商单) outputs from one codebase.
metadata:
  author: hwalme
  version: "1.0"
  tags:
    - video
    - ai-pipeline
    - remotion
    - tts
    - content-production
---

# Cinema AI Video Pipeline (Zero-Cost Stack)

A repeatable, production-grade AI video pipeline that costs **$0** in API
fees and runs entirely on free/public providers. Built so one codebase
serves three forms: **film** (ep01/ep02), **web-comic / 漫剧**, and
**commercial ad / 商单**.

## Pipeline stages
1. **Script** — DeepSeek V3 (free chat endpoint) writes scene scripts,
   beat sheets, and shot lists. Keep a single source-of-truth rules file
   (AGENTS.md) so scripting stays consistent across episodes.
2. **Image** — Pollinations.ai Flux (`https://image.pollinations.ai/...)
   generates keyframes / concept art from prompts. No API key.
3. **Voice** — `edge-tts` (Python) synthesizes narration per line; pick
   voice by character. Outputs `.mp3` per shot.
4. **Video** — Remotion (React) composes images + voice + timing into a
   30s / 1080p / 30fps MP4. Provider routing layer lets you swap a stage
   (e.g. ComfyUI when a key is available) without rewriting the pipeline.

## When to use
- "Make an AI short film / 漫剧 / 商单 ad with no budget."
- "Set up a reusable video generation pipeline."
- "What's the free alternative to ComfyUI for image gen?"

## Procedure
1. Author script via DeepSeek V3; store as structured JSON (shot id,
   prompt, voice line, duration).
2. For each shot, call Pollinations Flux with the shot prompt → save image.
3. For each voice line, `edge-tts --voice <char> -t "<line>" -o shot.mp3`.
4. Feed assets into a Remotion `composition`; render `npx remotion render`.
5. Route: if `COMFYUI_H3_URL` (or similar) is set, use ComfyUI for that
   stage instead of Pollinations — keep the orchestration identical.

## Hard rules
- **Never claim "done" on a stage that only emitted a placeholder.** Verify
  each artifact (image non-empty, mp3 non-silent, mp3 duration > 0).
- Keep the **three-form-factor test**: any pipeline change must still serve
  film + 漫剧 + 商单. A fix that only helps one form is a temp patch — label it.
- Free APIs rate-limit: build retry/backoff, don't hammer.
- This skill does NOT contain paid keys; it describes free endpoints only.

## References
See `references/free-stack.md` for exact endpoint URLs, Remotion composition
skeleton, and the provider-routing interface.
