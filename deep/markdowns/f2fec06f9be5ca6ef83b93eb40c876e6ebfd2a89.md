# suraj1235/open-dynamic-workflows

> 暂无描述。

## 基本信息

| 字段 | 内容 |
|---|---|
| 名称 | suraj1235/open-dynamic-workflows |
| 链接 | https://github.com/Suraj1235/open-dynamic-workflows |
| 来源聚合 | sickn33/agentic-awesome-skills |
| 分类路径 | 开发工程 / 工程方法 / 通用工程 |
| 类型 | AI Skill / Agent Tool |

## 简介

暂无简介。

## README / Skill 文档

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner.svg" width="660" alt="open dynamic workflows — the script is the orchestrator, not the model">
</picture>

<br><br>

**The model plans the swarm. A local script runs it. Your chat only sees the answer.**

An open-source engine for dynamic, multi-agent workflows where a *script* is the orchestrator, not the model — the pattern behind Claude Code's dynamic workflows and ultracode, for **OpenCode, Cursor, OpenAI Codex, Google Antigravity, and VS Code**. Bring your own model, run a local daemon, keep everything on your machine.

[**Quick start**](#quick-start)&nbsp;·&nbsp;[**How it works**](#how-it-works)&nbsp;·&nbsp;[**Topologies**](#topologies)&nbsp;·&nbsp;[**Compare**](#how-it-compares)&nbsp;·&nbsp;[**FAQ**](#faq)

<br>

[![CI](https://github.com/Suraj1235/open-dynamic-workflows/actions/workflows/ci.yml/badge.svg)](https://github.com/Suraj1235/open-dynamic-workflows/actions/workflows/ci.yml)
![license MIT](https://img.shields.io/badge/license-MIT-6366f1?style=flat-square&labelColor=1a1b22)
![node ≥ 20](https://img.shields.io/badge/node-%E2%89%A5%2020-6366f1?style=flat-square&labelColor=1a1b22)
![runs on mac · linux · windows](https://img.shields.io/badge/runs%20on-mac%C2%B7linux%C2%B7windows-6366f1?style=flat-square&labelColor=1a1b22)
![hosting cost $0](https://img.shields.io/badge/hosting%20cost-%240-22c55e?style=flat-square&labelColor=1a1b22)
![telemetry none](https://img.shields.io/badge/telemetry-none-22c55e?style=flat-square&labelColor=1a1b22)
![sandbox quickjs wasm](https://img.shields.io/badge/sandbox-quickjs%C2%B7wasm-6366f1?style=flat-square&labelColor=1a1b22)

</div>

---

<div align="center">
<img src="assets/architecture.svg" width="920" alt="How it runs: you describe a workflow, a local script plans and fans out parallel agents, critics verify, you get one answer">
</div>

---

## What it is

When you ask one LLM to coordinate fifty agents, it spends its context window keeping track of the other forty-nine. The fix is to have the model write a plan **once** — a plain JavaScript `execute()` function — and then step out of the loop while a runtime executes it. The model is the author. The script is the orchestrator. That capability had been locked to one proprietary tool; this is the same idea, MIT-licensed, on your machine.

| Script-as-orchestrator | It verifies its own work | Runs on your machine |
| :--: | :--: | :--: |
| The model writes a plan once. A local daemon runs the swarm. | Adversarial critics catch false positives before you see them. | Bring your own model. No telemetry. Nothing leaves your box. |

```
you ──▶ "workflow: audit every endpoint for missing auth"
        │
        ├─ plan      25 agents · adversarial verification · ~$0.30 · ~4 min
        ├─ confirm   [run] [view script] [edit]
        └─ run       ▶ wf_9f3c2a  → 200 endpoints checked, 6 real issues, report written
```

---

## How it works

The model never babysits the swarm. It writes one `execute(context)` function and hands it to the daemon, which runs it inside a WASM-isolated QuickJS sandbox where the only things in scope are the workflow primitives — `agent`, `parallel`, `pipeline`, `verify`, `loop`, `checkpoint`. Every `agent()` call becomes one HTTP request to your model provider, scheduled through a concurrency queue. Your chat window only sees the final answer.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#6366f1','primaryTextColor':'#ffffff','lineColor':'#818cf8','primaryBorderColor':'#a5b4fc'}}}%%
flowchart LR
    you([you: a one-line workflow]) --> script[local daemon<br/>plans + schedules]
    script --> a1((agent)) & a2((agent)) & a3((agent))
    a1 & a2 & a3 --> critics{adversarial<br/>critics}
    critics --> answer([one verified answer])
    script -.checkpoint.-> db[(sqlite + WAL)]
```

- **It survives.** State lives in SQLite with write-ahead logging. Kill the daemon mid-run, start it with `--resume`, and completed agents come back from cache — only unfinished work re-runs. A failed agent is dropped, not fatal; the run keeps going. Node identity is `sha1(workflow | phase | role | prompt)`, so replay is exact.
- **It doesn't trust its own agents.** A finding isn't a finding until a panel of skeptics has tried to knock it down. The `verify` primitive runs critics that hunt false positives, challenge severity, and look for what's missing, then keeps only what survives a quorum.
- **It won't blow the context window.** Each agent gets a fresh window and only its distilled result crosses back — the same isolation big harnesses use to run huge tasks. On top of that, every call is measured against the model's real context window and, if it would overflow, the input is compacted by dropping *whole* structural elements (never a mid-JSON cut). A provider "context too long" error is caught and self-healed with a bounded compact-and-retry instead of crashing the run — so it holds up on small and free models, not just 200K-token ones.

---

## Quick start

> **Install from GitHub** — not on the npm registry yet, so install by cloning. (An unrelated package happens to sit at the name `open-dynamic-workflows` on npm — that isn't this project.) Same steps on macOS, Linux, and Windows.

```bash
git clone https://github.com/Suraj1235/open-dynamic-workflows
cd open-dynamic-workflows
npm install
npm run setup
```

<div align="center">
<img src="assets/demo.svg" width="680" alt="terminal: a real daemon run planning and verifying a workflow on a free model">
</div>

`npm run setup` writes `~/.odw/config.json`. Add one key and you're done:

```json
{
  "apiKeys": { "anthropic": "sk-ant-..." },
  "models": { "planning": "gpt-4o-mini", "default": "claude-sonnet-4-6" }
}
```

Then drive it from a shell — no editor required:

```bash
odw-daemon start
odw-daemon run --prompt "workflow: find every TODO that hides a real bug" --cwd ./my-project
```

Or wire it directly into your agentic coder from the clone:

```bash
odw-daemon integrate all          # one command for every supported adapter below
odw-daemon integrate mcp          # writes .mcp.json + AGENTS.md instructions
odw-daemon integrate codex        # Codex plugin + MCP + ODW/ultracode skills
odw-daemon integrate cursor       # writes MCP + rule + /odw + /ultracode skills + subagent + dashboard
odw-daemon integrate kimi         # writes ~/.kimi-code/mcp.json + /flow:odw + /flow:ultracode
odw-daemon integrate gemini       # writes ~/.gemini/settings.json + /odw + /ultracode
odw-daemon integrate zed          # writes .zed/settings.json + /odw + /ultracode Agent Skills
odw-daemon integrate zcode        # generic MCP + zcode guidance + Zed-compatible settings/skills
odw-daemon integrate opencode     # local OpenCode plugin wrapper + /odw + /ultracode + /workflows
odw-daemon integrate vscode       # installs the local VS Code dashboard extension
odw-daemon integrate antigravity  # Antigravity plugin bundles + MCP configs + ODW/ultracode skills + workflow
odw-daemon integrate openclaw     # OpenClaw skill folder
odw-daemon doctor all             # verify configs and daemon readiness
odw-daemon doctor all --json      # machine-readable readiness for agents/CI
npm run smoke:hosts               # temp install + live workflow + MCP bridge + host CLI probes
```

After that, open the target agent and say `workflow: ...`, `ultracode ...`, or `/deep-research ...`.

If a model has no key or route, `odw-daemon run` tells you up front — before planning — exactly which line of the config to fix. No silent first-run failures.

<details>
<summary><b>Run on a free local model, or any OpenAI-compatible endpoint</b></summary>

<br>

No cloud key? Run a local model with **Ollama** and pay nothing — point all three roles at it so planning and fallbacks stay free too:

```json
{ "models": { "planning": "ollama:llama3", "default": "ollama:llama3", "fallback": "ollama:llama3" } }
```

**Any OpenAI-compatible endpoint** works — OpenCode Zen, Azure OpenAI, vLLM, LM Studio, Together, Groq:

```json
{
  "baseURLs": { "default": "https://opencode.ai/zen/v1" },
  "apiKeys":  { "default": "your-key" },
  "models":   { "planning": "minimax-m3-free", "default": "minimax-m3-free", "fallback": "minimax-m3-free" }
}
```

Prefer not to install globally? Every command also runs from the repo: `npm start`, `npm run status`, `npm run odw -- run --prompt "..."`.

</details>

Model routing is automatic:

| Model id | Routes to |
| --- | --- |
| `claude-*` | Anthropic |
| `gpt-*`, `o*` | OpenAI |
| `ollama:*` | local Ollama (free) |
| `provider:model` | a named `baseURLs.<provider>` |
| anything else | `baseURLs.default` |

---

## Topologies

The planner picks the simplest shape that fits the task instead of throwing a swarm at everything.

<div align="center">
<img src="assets/topologies.svg" width="900" alt="six orchestration topologies: pipeline, map-reduce, adversarial, consensus, tree search, hybrid">
</div>

| Topology | Shape | Good for |
|----------|-------|----------|
| MapReduce | split → map in parallel → reduce | auditing 500 files, the same check across many items |
| Pipeline | stage → stage → stage, per item, no barrier | migrate → test → fix, where item A streams ahead of item B |
| Adversarial | propose → critique → fix → re-verify | anything that has to be *correct*, not just plausible |
| Consensus | many evaluators → weighted vote | uncertain facts, research, judgement calls |
| Tree search | expand → score → prune → backtrack | root-cause hunts, branching exploration |
| Hybrid | the above, composed | real features that have several phases |

---

## Inside your agent

For broad agent support, start with `odw-daemon integrate mcp`. It writes a project `.mcp.json` using the common `mcpServers` shape and adds a managed `AGENTS.md` block that tells MCP-capable agents when to use `odw_run`, `odw_plan`, `odw_status`, and `odw_result`. Host-specific installers sit beside it: `integrate codex` installs a local Codex plugin bundle under `~/.codex/plugins/odw`, registers it in the personal marketplace at `~/.agents/plugins/marketplace.json`, and keeps the fallback `~/.codex/config.toml` MCP block plus the `~/.agents/skills/odw` and `~/.agents/skills/ultracode` skills; `integrate cursor` adds Cursor MCP config, a project rule, project-local `.cursor/skills/odw` and `.cursor/skills/ultracode` skills invokable as `/odw` and `/ultracode`, a Cursor-native `.cursor/agents/odw-orchestrator.md` subagent, and the dashboard extension under `~/.cursor/extensions`; `integrate kimi` writes Kimi Code's `~/.kimi-code/mcp.json`, `AGENTS.md`, and project-local `.kimi/skills/odw` plus `.kimi/skills/ultracode` flow skills invokable as `/flow:odw`, `/skill:odw`, `/flow:ultracode`, or `/skill:ultracode`; `integrate gemini` writes Gemini CLI's `~/.gemini/settings.json`, `GEMINI.md`, and project-local `.gemini/commands/odw.toml` plus `ultracode.toml` slash commands; `integrate zed` writes Zed `context_servers`, `AGENTS.md`, and project-local `.agents/skills/odw` plus `.agents/skills/ultracode` Agent Skills invokable with `/`; `integrate zcode` writes generic MCP plus zcode-facing `AGENTS.md` guidance and retargeted `.agents/skills/odw` plus `.agents/skills/ultracode` skills over the same Zed-compatible context-server config; `integrate opencode` writes the local plugin wrapper plus `/odw`, `/ultracode`, and `/workflows` commands; `integrate vscode` installs the local dashboard extension into `~/.vscode/extensions`; and `integrate antigravity` installs official-layout Antigravity plugin bundles at `~/.gemini/config/plugins/odw`, `~/.gemini/antigravity-cli/plugins/odw`, and `.agents/plugins/odw` while preserving direct MCP configs at `~/.gemini/config/mcp_config.json`, `~/.gemini/antigravity-cli/mcp_config.json`, and `.agents/mcp_config.json`.

Run `odw-daemon doctor <agent>` after setup to check both sides of the handshake: the expected agent config files exist and point at this checkout, and the local daemon is reachable. It exits non-zero with a specific missing file or daemon-start hint when something is not ready.
Add `--json` to `integrate` or `doctor` when an agent, CI job, or installer UI needs stable machine-readable output instead of colored text.

For release and support checks, run `npm run smoke:hosts`. It creates a temporary full install, verifies the combined `AGENTS.md` guidance covers generic MCP hosts, Kimi Code, Zed, and zcode, starts a temporary daemon against a zero-cost mock provider, completes a real workflow, completes a real `odw_run` through the MCP bridge, parses `odw-daemon doctor all --json` so every named adapter is checked explicitly, and probes installed host CLIs. Missing proprietary hosts are reported as skipped instead of faking coverage.
Use `npm run smoke:hosts -- --require-host opencode` when a release machine is expected to prove a specific host is runnable.

The adapters are how your existing tool drives the engine. The easiest default is MCP: `odw-daemon integrate codex` and `odw-daemon integrate cursor` point the host at the local `odw-mcp` bridge, so the host gets `odw_plan`, `odw_run`, `odw_status`, `odw_result`, and `odw_control` tools without the compiled orchestration script entering chat context. Codex now also gets the official plugin packaging path, so the same skill and MCP server can be surfaced from Codex's plugin browser. Native adapters sit beside that where the host exposes better hooks. **On OpenCode the engine runs *inside* the plugin, on your already-configured model — no daemon and no second API key.** Everywhere else the engine runs in the local daemon (its own key) and the adapter is a thin client over its localhost API.

| Editor / agent | How it connects | No-key, no-daemon native mode? |
| --- | --- | --- |
| **Generic MCP hosts** | `odw-daemon integrate mcp` writes `.mcp.json` plus managed `AGENTS.md` instructions for clients that import the common `mcpServers` JSON shape | **No** - MCP is a tool bridge, not host-model execution |
| **Kimi Code CLI** | `odw-daemon integrate kimi` writes `~/.kimi-code/mcp.json`, managed `AGENTS.md`, and `.kimi/skills/odw` plus `.kimi/skills/ultracode` so `/flow:odw`, `/skill:odw`, `/flow:ultracode`, or `/skill:ultracode` opens the workflow playbook in Kimi | **No** - same MCP bridge |
| **Gemini CLI** | `odw-daemon integrate gemini` writes `~/.gemini/settings.json` `mcpServers.odw`, managed `GEMINI.md`, and `.gemini/commands/odw.toml` + `ultracode.toml` so `/odw` and `/ultracode` route through ODW | **No** - same MCP bridge |
| **Zed / zcode-style clients** | `odw-daemon integrate zed` writes `.zed/settings.json` `context_servers`, managed `AGENTS.md`, and `.agents/skills/odw` plus `.agents/skills/ultracode` so `/odw` or `/ultracode` opens the workflow playbook in Zed Agent; `integrate zcode` writes both generic `.mcp.json` and zcode-specific guidance/skills over the same Ze

> *（内容过长，已截断前 15000 字符。完整文档见原链接）*

## 参考链接

- https://github.com/Suraj1235/open-dynamic-workflows
