# idea-os

An **operating system for turning raw ideas into build-ready plans** — as a Claude Code / Claude-compatible skill.

You drop in a rough problem statement or idea. It runs a five-phase pipeline (clarify → research → PRD → plan) and writes four files you can take straight to building:

1. `questions.md` — sharp, tier-adapted clarifying questions
2. `research.md` — market, competitors, SWOT, JTBD, distribution, trends, insights
3. `PRD.md` — problem, users, scope, non-goals, metrics
4. `plan.md` — user journey (mermaid), platform/stack recommendations, phased build with kill criteria

## Why this exists

Coding is having a moment. Non-developers are opening terminals. Experienced PMs are shipping side projects. The hard part isn't the code anymore — it's the gap between "I have an idea" and "I know exactly what to build, for whom, how, and how I'll know it's working."

Most PRD tools stop at the document. `idea-os` goes further — it ties research to PRD to phased plan, with opinionated platform/stack recommendations, a mermaid user-journey diagram, kill criteria per phase, and first-100-users distribution. It adapts depth to the idea's complexity and the builder's experience so a first-time builder isn't buried in jargon and a founder gets full rigor.

## What you get

- **Clarifying questions** (4–18, complexity-adjusted) that actually change the answer
- **Deep research** — TAM/SAM/SOM (top-down + bottom-up), segmentation, competitor matrix with positioning map, SWOT, JTBD, distribution strategy, why-now, 3–7 non-obvious insights
- **PRD** — falsifiable problem statement, named personas, ranked JTBD, leading/lagging metrics, explicit non-goals
- **Execution plan** with:
  - User journey (text walkthrough + mermaid diagram that renders on GitHub)
  - Platform recommendation (web / mobile / desktop / CLI / extension / hybrid) tied to research findings
  - Stack recommendation (conservative / modern / cutting-edge matrix)
  - Phased build (MVP → v1 → target state) with kill criteria and per-phase distribution
  - Concrete next steps for the next 1–2 weeks

## Installation

### Claude Code

Clone into your skills directory:

```bash
git clone https://github.com/Slashworks-biz/idea-os.git ~/.claude/skills/idea-os
```

The skill activates automatically when you describe an idea or problem that needs the full pipeline.

### Claude.ai

Zip the repo contents and upload as a project-level skill, or paste `SKILL.md` into a project description.

### Trigger phrases

- "I have an idea for…"
- "Help me build X"
- "Validate and plan this concept…"
- "What should I build?"
- Any problem statement where the user wants the full multi-phase artifact output (not a quick one-shot answer)

## How it works

Five phases, in order:

1. **Triage** — classify idea complexity (C1 simple / C2 moderate / C3 complex) and jargon level (plain / standard / full). Depth and vocabulary scale accordingly.
2. **Clarify** — write `questions.md`, wait for answers. Skip if the brief is already dense or in autonomous mode.
3. **Research** — write `research.md` using real signal (WebSearch + WebFetch). No hallucinated stats; sources or `[assumption]` flags.
4. **PRD** — write `PRD.md`.
5. **Plan** — write `plan.md` with user journey, platform/stack picks, phased build, metrics, kill criteria, distribution, next steps.

See [`SKILL.md`](SKILL.md) for the full spec.

## Repo layout

```
idea-os/
├── SKILL.md                          # skill entry point (trigger + workflow)
├── references/
│   ├── clarifying-questions.md       # tiered question bank by idea type
│   ├── research-frameworks.md        # JTBD, SWOT, Porter 5, PESTEL, Blue Ocean, Wardley
│   ├── market-analysis.md            # TAM/SAM/SOM, segmentation, WTP
│   ├── competitor-analysis.md        # direct/indirect/substitute, positioning map
│   ├── distribution.md               # first-100-users channel-fit patterns
│   ├── prd-structure.md              # PRD anatomy and anti-patterns
│   ├── mvp-slicing.md                # vertical slice, walking skeleton, concierge MVP, RICE/ICE/Kano
│   ├── metrics-framework.md          # North Star, AARRR, HEART, counter-metrics
│   ├── platform-recommendation.md    # web/mobile/desktop/CLI/ext decision framework
│   ├── stack-recommendation.md       # conservative/modern/cutting-edge defaults
│   └── user-journey.md               # text + mermaid guidance
├── assets/
│   ├── questions-template.md
│   ├── research-template.md
│   ├── PRD-template.md
│   └── plan-template.md
├── examples/
│   └── example-notion-for-dog-trainers.md  # reference-only T2/S2 walkthrough
└── README.md
```

## Philosophy

- **Specifics beat generics.** A SWOT bullet that could apply to any product in the category is dead weight.
- **Non-goals are diamonds.** The PRD lives or dies by what you refuse to build in v1.
- **Kill criteria up front.** Every phase has a "stop here" threshold set before hope distorts judgment.
- **Evidence over confidence.** Every factual claim is sourced or flagged `[assumption]`.
- **Distribution deserves product-level rigor.** Where the first 100 users come from is a product decision, not a marketing afterthought.
- **Jargon only where earned.** Plain-level readers never see "Kano model" without an explanation. Full-level readers get the full vocabulary.
- **MVP is a vertical slice, not a feature list.** One user, one job, end-to-end.

## Example

See [`examples/example-notion-for-dog-trainers.md`](examples/example-notion-for-dog-trainers.md) for a complete mid-complexity walkthrough — original brief → questions → research → PRD → plan. It's a reference-only file showing the quality bar; you don't need to read it unless you're calibrating the skill.

## Contributing

Issues and PRs welcome. Especially useful:
- Additional domain-specific question banks (healthtech, fintech, climate, etc.)
- Example walkthroughs at different complexity levels
- Sharper competitor-analysis templates for specific categories

## Related skills

`idea-os` sits alongside (does not replace):
- **`idea-refine`** — quick feedback on a single idea; use this when you *don't* want four files
- **`product-management`** — PRD editing and ongoing product work for an already-scoped product
- **`design-thinking`** — methodology, complementary to `idea-os`'s artifact pipeline
- **`senior-software-engineer`** — downstream of `idea-os`; once you have the plan, this helps you build it

## License

MIT — see [LICENSE](LICENSE).

## Credit

Built under [Slashworks](https://github.com/Slashworks-biz) with the Claude Agent SDK.
