# Free Zero-Cost AI Video Stack — reference

Exact endpoints and skeletons for the `cinema-ai-video-pipeline` skill.
All free / no-key. Swap any stage via the provider-routing layer.

## 1. Script — DeepSeek V3 (free chat endpoint)
POST to the public DeepSeek-compatible chat endpoint with a system prompt
that enforces your AGENTS.md rules (single source of truth, three-form
factor test). Parse the model output into structured JSON:

```json
{
  "shots": [
    { "id": "s01", "prompt": "<flux prompt>", "voice": "zh-CN-YunxiNeural", "line": "<narration>", "dur": 4 }
  ]
}
```

## 2. Image — Pollinations.ai Flux (no key)
```
https://image.pollinations.ai/prompt/<url-encoded-prompt>?width=1920&height=1080&nologo=true&model=flux
```
Save response bytes as `shots/s01.png`. Verify non-empty before proceeding.

## 3. Voice — edge-tts (Python)
```bash
pip install edge-tts
edge-tts --voice zh-CN-YunxiNeural --text "台词" --write-media shots/s01.mp3
```
Verify duration > 0 with `ffprobe` or a header check.

## 4. Video — Remotion composition skeleton
```tsx
// src/Video.tsx
import { AbsoluteFill, Sequence, useVideoConfig } from "remotion";
export const Main: React.FC = () => (
  <AbsoluteFill style={{ background: "#000" }}>
    {shots.map((s, i) => (
      <Sequence key={s.id} from={offsets[i]} durationInFrames={s.dur * fps}>
        <AbsoluteFill>
          <img src={s.img} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          <audio src={s.mp3} autoPlay />
        </AbsoluteFill>
      </Sequence>
    ))}
  </AbsoluteFill>
);
```
Render: `npx remotion render src/index.ts Main out/video.mp4`

## 5. Provider routing interface
```ts
type Stage = "image" | "voice" | "script";
type Provider = (input: any) => Promise<Buffer | string>;
const router: Record<Stage, Provider> = {
  image: process.env.COMFYUI_H3_URL ? comfyImage : pollinationsImage,
  voice: edgeTts,
  script: deepseekScript,
};
```
When `COMFYUI_H3_URL` is present, the image stage transparently switches to
ComfyUI; everything else stays free.
