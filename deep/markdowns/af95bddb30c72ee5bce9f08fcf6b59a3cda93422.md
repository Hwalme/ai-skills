# hafiz-actyte/idea-autopsy

> 暂无描述。

## 基本信息

| 字段 | 内容 |
|---|---|
| 名称 | hafiz-actyte/idea-autopsy |
| 链接 | https://github.com/hafiz-actyte/idea-autopsy |
| 来源聚合 | sickn33/agentic-awesome-skills |
| 分类路径 | 开发工程 / 工程方法 / 通用工程 |
| 类型 | AI Skill / Agent Tool |

## 简介

暂无简介。

## README / Skill 文档

# 🪦 Idea Autopsy — a Claude Code skill that kills bad business ideas before you build them

Most business ideas deserve to die **before** you spend a dollar on them.
This skill turns Claude Code into a ruthless idea pathologist: kill-list check →
five hard filters → the free-AI one-prompt test → live-market verification with
your own eyes → a verdict with a named kill-pattern.

Built from a real system that killed **42 business ideas** (including a 9/10-scored
idea and one that turned out to be federally illegal) before a single one was built.
I post the autopsies here: **[YouTube @actyte](https://www.youtube.com/@actyte)** · **[Instagram @hafiz.actyte](https://www.instagram.com/hafiz.actyte/)** · **[LinkedIn](https://www.linkedin.com/in/hafizsiddiq15/)**.

## Install

**As a Claude Code plugin (recommended):**

```
/plugin marketplace add hafiz-actyte/idea-autopsy
/plugin install idea-autopsy@idea-autopsy
```

**Or plain clone (works for any harness that reads skills folders):**

```bash
git clone https://github.com/hafiz-actyte/idea-autopsy /tmp/idea-autopsy \
  && cp -r /tmp/idea-autopsy/skills/idea-autopsy ~/.claude/skills/
```

Then, in any project:

```
autopsy my idea: <describe the idea>
```

## What it does

1. **Kill-list check** — matches the idea against your own `REJECTION.md` graveyard
   (starter template included). Dead ideas stay dead; no re-research.
2. **Five filters** — real pain? buyer has money *now*? proven demand? legal to
   charge for? a moat? One hard NO = dead.
3. **Free-AI test** — if one prompt produces your whole deliverable, you don't have
   a product. You have a prompt.
4. **Own-eyes verification** — a Meta Ad Library checklist that catches the traps
   desk research misses: zero-ads categories, incumbent-owned lanes, and the
   "1,100 advertisers means demand" trap (it also means everyone could build it —
   so everyone did).
5. **Verdict** — DEAD with a named kill-pattern (14 documented in
   `references/kill-patterns.md`), or SURVIVED with the one cheapest test that
   could still kill it. Every autopsy writes a row to your kill-list.

## Why kill ideas?

Building was never the problem — AI builds anything in a weekend now. Picking is
the problem. A fast, honest kill is a win: it costs 20 minutes instead of 3 months.
The kill-list compounds — every dead idea makes the next autopsy faster.

## Files

- `skills/idea-autopsy/SKILL.md` — the autopsy procedure Claude follows
- `skills/idea-autopsy/references/kill-patterns.md` — the 14 named ways ideas die
- `skills/idea-autopsy/templates/REJECTION-template.md` — your starter kill-list

## Watch ideas die

Real autopsies from the 42-idea graveyard, one per week — comment your idea; the
most-liked one gets autopsied on camera:

- YouTube: [@actyte](https://www.youtube.com/@actyte)
- Instagram: [@hafiz.actyte](https://www.instagram.com/hafiz.actyte/)
- LinkedIn: [Hafiz Siddiq](https://www.linkedin.com/in/hafizsiddiq15/)

MIT license. PRs welcome — especially new kill-patterns with receipts.


## 参考链接

- https://github.com/hafiz-actyte/idea-autopsy
