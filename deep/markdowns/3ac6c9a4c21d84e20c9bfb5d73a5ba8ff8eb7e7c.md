# infrasity-labs/dev-gtm-claude-skills

> : GTM-focused skill collection for developer go-to-market workflows including launch planning, positioning, and outbound sequences.

## 基本信息

| 字段 | 内容 |
|---|---|
| 名称 | infrasity-labs/dev-gtm-claude-skills |
| 链接 | https://github.com/infrasity-labs/dev-gtm-claude-skills |
| 来源聚合 | Marketing |
| 分类路径 | 运维DevOps / IaC基础设施 / Terraform |
| 类型 | AI Skill / Agent Tool |

## 简介

: GTM-focused skill collection for developer go-to-market workflows including launch planning, positioning, and outbound sequences.

## README / Skill 文档

<div align="center">

<img src="assets/infrasity_logo.avif" alt="Infrasity" height="64" />

# Claude Code Skills for SEO, GEO & Developer Marketing

**Free, open-source Claude skills that audit your docs, score your AI discoverability, and run developer-marketing workflows — so your product gets found, parsed, and cited by AI systems.**

[![Claude Compatible](https://img.shields.io/badge/Claude-Compatible-FF4A1C)](https://claude.ai/) [![GEO Optimized](https://img.shields.io/badge/GEO-Optimized-7F77DD)](https://www.infrasity.com/services/ai-geo-optimization-agency) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/Infrasity-Labs/dev-gtm-claude-skills?style=social)](https://github.com/Infrasity-Labs/dev-gtm-claude-skills/stargazers) [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/) [![skills.sh](https://skills.sh/b/Infrasity-Labs/dev-gtm-claude-skills)](https://skills.sh/Infrasity-Labs/dev-gtm-claude-skills)

[Skills](#skills) · [Install](#installation) · [Commands](#commands) · [Who it's for](#who-its-for) · [FAQ](#faq) · [Website](https://www.infrasity.com/claude-skills)

**Works with:** Claude Code · OpenAI Codex · OpenClaw · Hermes Agent[^hermes] · Mistral Vibe[^vibe] · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

<p align="center">
  <img src="./assets/dev-gtm-claude-skills.png" width="100%" alt="dev-gtm-claude-skills"/>
</p>

</div>

---

`dev-gtm-claude-skills` is a collection of open-source **Claude Code skills** for **SEO**, **GEO (Generative Engine Optimization)**, **AI discoverability**, and **developer marketing**. Each skill is a self-contained package — a `SKILL.md` that tells Claude when and how to use it, optional Python tooling, and a README with full usage docs. Install once, then run from Claude Code, Claude Desktop, or Claude.ai with a plain-language prompt.

These skills are built for **developer-focused companies** — DevTools, AI-agent platforms, observability, and B2B SaaS — that need their documentation and content to be **cited by AI systems like ChatGPT, Claude, Perplexity, and Gemini**, not just indexed by Google.

> **What is GEO?** Generative Engine Optimization is the practice of optimizing content so it gets surfaced and cited by AI answer engines. Traditional SEO tools optimize for search crawlers; these skills audit the signals — structured content, `llms.txt`, internal linking, and documentation completeness — that LLMs use when deciding what to recommend.

### What you can do in one prompt

- **Audit developer docs** for SEO and AI discoverability — 33 checks, scored 0–100
- **Score API & SDK documentation** quality, endpoint by endpoint
- **Check AI-readiness** — `robots.txt`, `llms.txt`, and `llms-full.txt` in one pass
- **Generate 3-month SEO performance reports** vs competitors
- **Fix internal linking** — find orphan pages and dead-ends, get paste-ready suggestions
- **Produce SEO content briefs** as formatted `.docx` outlines

---

## What Are Claude Code Skills & Agent Plugins?

Claude Code skills (also called agent skills or coding-agent plugins) are modular instruction packages that give AI coding agents domain expertise they don't have out of the box. Each skill in this repo includes:

- **`SKILL.md`** — structured instructions, workflows, and decision frameworks that tell the agent when and how to act
- **Python tools** — optional stdlib-only CLI scripts for the skills that crawl, score, or render reports
- **Reference docs** — templates, scoring guides, and checklists the skill loads on demand

Because every skill follows the open `SKILL.md` standard, it isn't locked to a single product. The same package runs in Claude Code, Claude Desktop, Claude.ai, and any other agent that reads the standard (see [Multi-Tool Support](#multi-tool-support)).

### Skills vs Agents

|  | Skills | Agents |
| --- | --- | --- |
| **Purpose** | _How_ to execute a task | _What_ task to do |
| **Scope** | A single, well-defined workflow | An end-to-end job, often composing skills |
| **Example** | "Follow these 33 checks to audit docs" | "Research, write, and review this blog post" |

This repo ships several bundles: the SEO/GEO/docs **skills** under [`skills/`](skills/), the full-funnel marketing **skills** under [`marketing-skills/`](marketing-skills/), the blog content engine under [`writing-skills/`](writing-skills/), a comprehensive **SEO suite** under [`seo-skills/`](seo-skills/), and blog-production **agents** under [`agents/`](agents/).

---

## Table of contents

- [What Are Claude Code Skills & Agent Plugins?](#what-are-claude-code-skills--agent-plugins)
- [Multi-Tool Support](#multi-tool-support)
- [Installation](#installation)
- [Skills](#skills)
- [Marketing skills](#marketing-skills)
- [Writing skills](#writing-skills)
- [SEO skills](#seo-skills)
- [Notion skills](#notion-skills)
- [Coding skills](#coding-skills)
- [Job search skills](#job-search-skills)
- [Product designer skills](#product-designer-skills)
- [Commands](#commands)
- [Who it's for](#who-its-for)
- [Requirements](#requirements)
- [Sample outputs](#sample-outputs)
- [Repository structure](#repository-structure)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## Multi-Tool Support

Every skill here is written to the open `SKILL.md` standard, so it isn't tied to a single agent. **Claude Code**, **Claude Desktop**, and **Claude.ai** read the skills natively (see [Installation](#installation)). For every other tool, the repo ships converter and installer scripts under [`scripts/`](scripts/) — clone the repo, then run the one-liner for your tool.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
```

Each script discovers all skills under `skills/`, `marketing-skills/`, `writing-skills/`, `notion-skills/`, and `seo-skills/` and installs them in the format that tool expects.

| Tool | Tested | Skills land in |
| --- | --- | --- |
| **Claude Code** | ✅ | `~/.claude/skills/` |
| **Claude Desktop / Claude.ai** | ✅ | ZIP upload |
| **Hermes Agent** | ✅ | `~/.hermes/skills/` |
| **Kilo Code** | ✅ | `~/.claude/skills/` (via `claudeCodeCompat`) |
| **Mistral Vibe** | ✅ | `~/.vibe/skills/` |
| **OpenAI Codex** | ✅ | `~/.codex/skills/` |
| **OpenClaw** | ✅ | `~/.openclaw/skills/` |
| **Augment** | ✅ | `.augment/skills/` (project-local) |
| **Antigravity** | ✅ | `~/.gemini/antigravity/skills/` |
| **Cursor** | 🔜 | `.cursor/rules/` (project-local) |
| **Aider** | 🔜 | `CONVENTIONS.md` (project-local) |
| **Windsurf** | 🔜 | `.windsurf/skills/` (project-local) |
| **OpenCode** | 🔜 | `.opencode/skills/` (project-local) |

See [full install steps per tool](#per-tool-install-steps) below.

---

## Installation

Most skills need **no API keys**; the SEO skills that pull live search data use a DataForSEO MCP server (setup below).

### Quick install (recommended)

Install every skill in this repo with one command — no cloning, no copying:

```bash
npx skills add Infrasity-Labs/dev-gtm-claude-skills
```

This pulls the latest skills straight into your Claude Code skills directory. Re-run it any time to update. Prefer to install manually or use Claude Desktop / Claude.ai? Use one of the methods below.

### Blog skills runtime (agents + scripts)

The [writing skills](#writing-skills) add a `/blog` content engine built from 30 sub-skills, **5 subagents**, and **shared Python scripts**. `npx skills add` installs the skill instructions, but the subagents and shared scripts need one extra step so the `/blog write` pipeline (research → write → SEO → review) runs end-to-end:

```bash
# Clone the repository to access the installer
git clone https://github.com/Infrasity-Labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
./scripts/claude-blog-install.sh                  # agents → ~/.claude/agents, scripts → ~/.claude/scripts
pip install -r writing-skills/requirements.txt    # textstat + beautifulsoup4
```

Use `--project` to install into the current project's `./.claude/` instead of `~/.claude/` (make sure to run the script from your project's root directory, e.g., `path/to/cloned-repo/scripts/claude-blog-install.sh --project`), and `--dry-run` to preview. A few sub-skills need their own credentials — `blog-google` (Google API OAuth), `blog-audio` / `blog-image` (`GOOGLE_AI_API_KEY` + nanobanana MCP), `blog-notebooklm` (browser login) — and all degrade gracefully when unconfigured.

### Claude Code (manual)

Clone the repo and copy the skill into your Claude Code skills directory.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
```

**Project-level** (available only in the current project):

```bash
mkdir -p .claude/skills
cp -r dev-gtm-claude-skills/skills/<skill-name> .claude/skills/
```

**User-level** (available across all projects):

```bash
mkdir -p ~/.claude/skills
cp -r dev-gtm-claude-skills/skills/<skill-name> ~/.claude/skills/
```

Skills activate automatically — Claude reads every `SKILL.md` in `.claude/skills/` at the start of each session. Trigger them by describing the task in plain language, or type `/<skill-name>` directly.

<p align="center">
  <img src="./assets/clone-repo.png" width="100%" alt="clone repo"/>
</p>

<p align="center">
  <img src="./assets/activate-skills.gif" width="100%" alt="Activate skills GIF"/>
</p>

### Claude Desktop / Claude.ai

Skills upload as ZIP files via **Settings → Customize → Skills → Create skill → Upload a skill**.

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills/skills

# Zip the skill you want to install
zip -r docs-auditor.zip docs-auditor/
```

Upload the `.zip`, toggle the skill on, and it's active across all your chats. Uploaded skills stay private to your account; Claude installs any required packages the first time it runs them.

<p align="center">
  <img src="./assets/converting-to-zip.gif" width="100%" alt="Converting to zip GIF"/>
</p>

<p align="center">
  <img src="./assets/add-to-claude.gif" width="100%" alt="Add to Claude GIF"/>
</p>

### DataForSEO MCP (for the live-search skills)

`growth-report`, `blog-post-counter`, and `api-docs-quality-report` pull live search data via a DataForSEO MCP server.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "dataforseo": {
      "command": "npx",
      "args": ["-y", "@dataforseo/mcp-server"],
      "env": {
        "DATAFORSEO_USERNAME": "your@email.com",
        "DATAFORSEO_PASSWORD": "your_api_password"
      }
    }
  }
}
```

**Claude Desktop** — Customize → Connectors → Add Custom Connector:

```
https://your_email:your_api_password@mcp.dataforseo.com/http
```

Get credentials at [dataforseo.com](https://dataforseo.com).

### Clay connector (for prospect enrichment and cold-email)

`dev-marketing-prospector` and `cold-email` use Clay's data enrichment tools to look up company funding, headcount, tech stack, and verified contact information — replacing manual research across Crunchbase, LinkedIn, and Apollo.

**Claude.ai / Claude Desktop** — Settings → Customize → Connectors → Connect Clay. Sign in with your Clay account. Once connected, the `find-and-enrich-company`, `ask-question-about-accounts`, and `find-and-enrich-contacts-at-company` tools become available automatically.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "clay": {
      "command": "npx",
      "args": ["-y", "@clay-hq/mcp-server"],
      "env": {
        "CLAY_API_KEY": "your_clay_api_key"
      }
    }
  }
}
```

Get your API key at [clay.com](https://clay.com). Both skills degrade gracefully when Clay is not connected — `dev-marketing-prospector` falls back to manual web search across all source categories, and `cold-email` prompts the user for research signals instead.

### Notion connector (for saving outputs to your workspace)

`competitor-profiling`, `customer-research`, and `content-brief` save their outputs to Notion as structured databases — competitor profiles become queryable competitive intelligence records, VOC research becomes a searchable quote bank, and content briefs sync to a living Notion database your whole team can filter and reference.

**Claude.ai / Claude Desktop** — Settings → Customize → Connectors → Connect Notion. Sign in with your Notion account and grant access to the workspaces you want skills to write to. Once connected, the `notion-search`, `notion-create-database`, `notion-create-pages`, and `notion-update-page` tools become available automatically.

**Claude Code** — add to `.claude/settings.json` or `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "your_notion_integration_secret"
      }
    }
  }
}
```

Get your integration secret at [notion.so/my-integrations](https://www.notion.so/my-integrations). All skills degrade gracefully when Notion is not connected — outputs are returned in chat or saved locally, and each skill appends a 💡 note with setup instructions.

### Apify connector (for web scraping — reviews, Reddit, Google Maps)

`reddit-comments`, `competitor-profiling`, `customer-research`, `seo-maps`, and `programmatic-seo` use Apify actors to scrape data that WebFetch and Firecrawl can't reliably reach — Reddit threads blocked by rate limits, G2/Capterra/Trustpilot review pages with anti-bot protection, and live Google Maps business listings.

> **Note:** Apify is an **official Anthropic connector** and is available on **Claude Desktop only**. It cannot be configured as a Claude Code MCP server.

**Claude Desktop** — Settings → Customize → Connectors → Connect Apify. Sign in with your Apify account. Once connected, the following actors are available across skills:

| Actor | Used by |
|---|---|
| `apify/reddit-scraper` | `reddit-comments`, `customer-research` |
| `apify/g2-scraper`, `apify/capterra-scraper`, `apify/trustpilot-scraper` | `competitor-profiling`, `customer-research` |
| `apify/google-maps-scraper`, `apify/google-maps-reviews-scraper`, `apify/yelp-scraper` | `seo-maps` |
| `apify/youtube-scraper`, `apify/amazon-reviews-scraper` | `customer-research` |
| `apify/google-maps-scraper`, `apify/g2-scraper`, `apify/capterra-scraper` | `programmatic-seo` |

All skills degrade gracefully when Apify is not connected — each falls back to WebFetch or Firecrawl and appends a 💡 note explaining what Apify would unlock.

### Klaviyo connector (for email template and campaign sync)

`emails`, `churn-prevention`, `lead-magnets`, and `onboarding` use Klaviyo's MCP tools to read your existing email setup and push new templates directly into your account — auditing existing flows, creating HTML and drag-and-drop templates, building campaigns, and pullin

> *（内容过长，已截断前 15000 字符。完整文档见原链接）*

## 参考链接

- https://github.com/infrasity-labs/dev-gtm-claude-skills
