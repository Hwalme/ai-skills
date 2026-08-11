# luopan(罗盘)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/tag/saudademjj/luopan?label=version)](https://github.com/saudademjj/luopan)
[![Docs](https://img.shields.io/badge/docs-online-8A2BE2)](https://saudade.me/luopan/)

A travel itinerary planning skill. Nothing gets scheduled until budget and scope are confirmed. Factual data carries its source and query date, and a self-check runs before delivery.

## Features

- Budget gate: no itinerary draft is produced until the budget is confirmed. Until then, the skill only asks clarifying questions
- Scope red line: the itinerary covers only the stated destination. If a ring route crosses the boundary, the reason is stated and a strict alternative is offered
- Source hierarchy: tickets, opening hours and similar factual data prefer official channels. Self-media and informal rankings count only as leads and are labeled "needs official confirmation". Every data point carries its source and query date
- Workload by scale: beyond viewing time, buffer is added for queues, transit, meals and photos; top-tier parks get a full day; self-drive hours count into the day's load
- Self-check before delivery: rules are re-read before final writing and each one is filled into a self-check table with evidence, because long itineraries drift
- Output includes: day-by-day schedule, budget estimate (economy and comfort tiers), transport and accommodation suggestions, attractions and food lists (with pitfalls), a pre-trip confirmation checklist, and a data source index

## Install

### Option 1: plugin marketplace

In a plugin-capable client terminal, run two commands:

```bash
plugin marketplace add saudademjj/luopan
plugin install travel-planner
```

For local development, use a local path: `plugin marketplace add /path/to/luopan`, then `plugin install travel-planner`.

### Option 2: manual copy

Copy the whole `skills/travel-planner` directory into your skills directory.

## Usage

Describe your trip in plain language and the skill triggers automatically:

> "帮我规划去苏州 5 天,带爸妈"
> "北京 7 天 6 晚,情侣,预算中等"
> "伊犁自驾 9 天,5 人,从乌鲁木齐出发"

The first step is requirement gathering (budget is mandatory). Research and scheduling start only after confirmation. Explicit invocation also works.

## Iteration log

The rules were written by hand, not auto-summarized. After each itinerary round, the author compared the output against real needs and wrote the mismatches back into the rules. Full record: [ITERATIONS.md](ITERATIONS.md).

## Data freshness

Prices, opening hours and travel policies in itineraries carry their query date, and every output ends with a pre-trip confirmation checklist. Verify against official channels before departure.

## Example output

- [10-day Xinjiang self-drive loop (including the north section of the Duku Highway)](examples/ili-10day-itinerary.md), with the rule self-check table and data source index

## Languages

- [中文 README](README.zh-CN.md)

## License

[MIT](LICENSE)
