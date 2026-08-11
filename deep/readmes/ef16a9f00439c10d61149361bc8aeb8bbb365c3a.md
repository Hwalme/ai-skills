# Feature Track

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)

Lightweight, repo-native shared memory for AI coding agents.

Feature Track keeps Codex, Claude Code, and other AI coding tools aligned on each long-lived feature: its status, source-of-truth docs, decisions, risks, and recent changes.

> Spec frameworks help agents plan the next change. Feature Track helps agents remember the feature.

It is not chat-history search, an opaque memory database, or a full spec-driven development framework. It is a portable, low-friction Markdown memory layer that lives inside your repo through `docs/features/`.

## Why

AI coding agents are good at making changes, but they lose project context easily:

- feature knowledge is scattered across PRDs, API notes, plans, chats, and old commits
- agents repeat discovery because there is no current feature index
- stale plans can look authoritative after reality has changed
- switching tools, sessions, or agents often resets project memory
- small teams and solo developers usually do not want heavyweight process

Feature Track gives every important feature a small living track file plus a global index. The track does not replace your docs. It points to the docs that still matter and records the current truth.

## Who It Is For

Feature Track is designed for:

- teams that want shared project memory without heavyweight process
- solo developers and indie hackers using AI coding tools
- brownfield projects with useful but scattered docs
- teams using Codex, Claude Code, or multiple agent tools
- projects that need traceable feature context across sessions

## Core Idea

```text
docs/features/
├── README.md              # global feature index
└── <feature-id>/
    ├── README.md          # current feature memory
    ├── prd/
    ├── api/
    ├── plans/
    └── archive/
```

Each feature track answers:

- What is true now?
- Which docs are the current source of truth?
- What decisions should future agents preserve?
- What risks, migrations, or rollout constraints matter?
- What changed recently?

## Philosophy

- Memory, not ceremony.
- Current truth over stale specs.
- Link first, migrate later.
- Adopt in minutes, improve over time.
- Works with your docs, not around them.

Feature Track is built for brownfield projects first. You can start by linking existing PRDs, API docs, plans, and design notes instead of moving everything into a new system.

## Quick Start

```bash
npx skills add JunsW/feature-track
```

Re-run the command any time to update. Or copy [SKILL.md](skills/feature-tracking/SKILL.md) and [references/](skills/feature-tracking/references/) into:

- **Claude Code:** `~/.claude/skills/feature-tracking/`
- **Cursor:** `.cursor/rules/feature-tracking.mdc` (use the body of `SKILL.md`, without frontmatter)
- **Codex:** `~/.codex/skills/feature-tracking/` for personal use or `.codex/skills/feature-tracking/` for a project

The complete portable rule set lives in [skills/feature-tracking/](skills/feature-tracking/).

## What Feature Memory Looks Like

This repository uses Feature Track on itself. The global index lives at [docs/features/README.md](docs/features/README.md):

```md
| Feature | Status | Track | Source Of Truth | Updated | Notes |
|---|---|---|---|---|---|
| Codex Plugin | active | [README](codex-plugin/README.md) | [README](../../README.md), [plugin manifest](../../plugins/feature-track/.codex-plugin/plugin.json) | 2026-07-06 | Publish-ready Codex plugin wrapper for the existing Feature Tracking skill |
| Claude Code Plugin | active | [README](claude-code-plugin/README.md) | [README](../../README.md), [plugin manifest](../../plugins/feature-track-claude/.claude-plugin/plugin.json), [marketplace](../../.claude-plugin/marketplace.json) | 2026-07-06 | Marketplace-ready Claude Code plugin wrapper for the Feature Tracking skill |
```

A feature track keeps the current operational memory close to the docs and files that prove it:

```md
## Current Status

Feature Track now targets a mature Codex plugin path for Codex users.

## Source Of Truth

- Product intro and install path: [README](../../../README.md)
- Plugin manifest: [plugin.json](../../../plugins/feature-track/.codex-plugin/plugin.json)

## Decisions

- Package the Codex path as a single-skill plugin first.
- Keep MCP servers, apps, and hooks out of v0.1.
```

See [docs/features/codex-plugin/README.md](docs/features/codex-plugin/README.md) and [docs/features/claude-code-plugin/README.md](docs/features/claude-code-plugin/README.md) for the full real tracks.

## How Agents Use It

At the start of work, an agent reads `docs/features/README.md`, opens the relevant feature track, and follows the current source-of-truth links instead of rediscovering context from scratch. After changes, the agent updates the feature track with the actual outcome: changed behavior, decisions, risks, tests, and recent changes.

`validate` turns this from loose Markdown into checkable memory. It catches index drift, missing required sections, feature tracks missing from the global index, and broken local links before stale context spreads into future sessions.

## How It Compares

Full spec-driven tools are useful when you want every change to move through proposals, spec deltas, task lists, and archive steps.

Feature Track is lighter. It focuses on long-term feature context rather than controlling every change. It is a good fit when you want AI agents to stop forgetting what a feature is, without forcing a new development lifecycle.

See [docs/comparison.md](docs/comparison.md) for more detail.

<details>
<summary><strong>Other Installation Options</strong></summary>

<br>

**Codex plugin:**

```bash
codex plugin marketplace add JunsW/feature-track
```

Then open `/plugins` and install **Feature Track**.

**Claude Code plugin:**

```text
/plugin marketplace add JunsW/feature-track
/plugin install feature-track@feature-track
```

**Local Python adapters:**

```bash
python3 cli/feature_track.py install codex
python3 cli/feature_track.py install claude-code --root .
```

All installation paths expose the same `feature-tracking` workflow. Avoid installing both the Codex plugin and standalone Codex skill unless you are testing adapter behavior.

</details>

## What The CLI Does

- `init`: create `docs/features/README.md`
- `add`: create a feature track and add it to the index
- `validate`: check index drift, required sections, and broken local links
- `install codex`: install the local Codex skill adapter
- `install claude-code`: generate Claude Code project instructions and commands

Validation is intentionally permissive by default so brownfield projects can adopt Feature Track gradually. Use `--ci` when you want stricter drift checks in automation.

## Repository Layout

- `.github/workflows/ci.yml`: basic CI for CLI syntax and feature memory validation
- `.claude-plugin/marketplace.json`: repo marketplace for the Claude Code plugin
- `.agents/plugins/marketplace.json`: repo marketplace for the Codex plugin
- `spec/feature-track-spec.md`: neutral Feature Track spec
- `cli/feature_track.py`: lightweight no-dependency CLI
- `plugins/feature-track/`: Codex plugin package
- `plugins/feature-track-claude/`: Claude Code plugin package
- `skills/feature-tracking/`: canonical portable Agent Skills package
- `skills/claude-code/`: Claude Code adapter snippets and commands
- `templates/`: reusable Markdown templates

## Status

`v0.1.0` is the first public release of Feature Track. The core format is intentionally simple: a global feature index plus one Markdown track per feature under `docs/features/`.

Today, Feature Track is best used as a lightweight documentation layer for Codex, Claude Code, or any agent workflow that can read and update files in your repo. The included plugins and CLI help create and validate that structure; the Markdown files remain the source of truth.

The document structure is designed to stay stable as the project grows.

## Contributing

Contributions are welcome. Please keep the spec portable, adapters lightweight, and validation friendly to existing projects. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Feature Track is released under the [MIT License](LICENSE).
