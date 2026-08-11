# Claude Code Resources — A visual field guide

> One stop. Every command, every agent, every skill — organized by what you're trying to do, not by where they live in the docs.

**🔗 [vexilo.app/?lang=en](https://vexilo.app/?lang=en)** — the live interactive guide.

---

## What this is

An interactive field guide for [Claude Code](https://github.com/anthropics/claude-code). Built because scrolling through `/help`, the docs, and 40 GitHub repos to find the right slash command is a 20-minute context switch nobody should pay twice.

```
31  agents       pre-built specialist subagents
99  commands     slash-command workflows
123 skills       on-demand capability packs
13  rules        project-level conventions
```

All four are organized around a single **5-step workflow** — *Research → Plan → Test-first → Security → Commit* — which is the core method behind the whole guide.

## Why it exists

Three companion toolkits (gstack, ECC, Auto Agent) ship hundreds of agents and commands between them. Anthropic Skills adds another layer. Great power, but you only discover them after you already needed one. This guide fixes that.

The killer move: every node in the 5-step flow links directly to the agents / commands / skills that pull weight at that step. Click once, see the stack, copy the snippet.

## The 30-second killer feature

Click **"Teach Claude this handbook"** at the top of the page. In 30 seconds it primes your local Claude with the entire guide, so when you say *"fix the auth bug"*, Claude already knows which agents and commands to chain.

No install. No npm. No API key. Just open the page, click once, paste back into your Claude session.

## Coverage

| Resource type | Count | Example usage |
| --- | --- | --- |
| **Agents** | 31 | `tdd-guide`, `build-error-resolver`, `security-reviewer`, `code-reviewer` |
| **Commands** | 99 | `/plan`, `/tdd`, `/security-scan`, `/quality-gate`, `/orchestrate` |
| **Skills** | 123 | UX review, prompt tuning, schema design, regex explainer |
| **Rules** | 13 | repo conventions, naming, file layout |
| **Deep guides** | 7 | project flow · best practices · deploy · UI/UX Pro Max · email-verification deploy · daily-use manual |

## How to use it

1. Open **[vexilo.app/?lang=en](https://vexilo.app/?lang=en)**
2. Press `⌘ K` to search anything (every agent, command, skill is one keystroke away)
3. Pick your scenario card — bug fix, new feature, code review, pre-launch security, automation, or "I'm new, where do I start?"
4. Click into the 5-step flow to see which agents and commands chain together
5. (Optional) Click **Teach Claude this handbook** to feed the whole guide into your local Claude session

## Built around three companion toolkits

- **[gstack](https://github.com/garrytan/gstack)** — the original spec-driven development workflow
- **[ECC](https://github.com/ezyang/codemirror)** — engineering coding conventions (note: actually **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)**)
- **[Auto Agent](https://github.com/coleam00/ai-agents)** — autonomous task execution
- **[Anthropic Skills](https://github.com/anthropics/skills)** — official capability packs

## Related tools this guide respects

- [anthropics/claude-code](https://github.com/anthropics/claude-code) — the official CLI (obviously)
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — Boris Cherny's patterns distilled into a 60k-star repo
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — the canonical curated list

## Contributing

Spotted an outdated command count? A new agent missing from the index? Open an issue — the guide is versioned (currently v1.1.9) and updates ship weekly.

## License

MIT. The guide is free, the data is open, and the index improves when people point at gaps.

---

<p align="center">
  <a href="https://vexilo.app/?lang=en"><strong>Open the field guide →</strong></a>
</p>