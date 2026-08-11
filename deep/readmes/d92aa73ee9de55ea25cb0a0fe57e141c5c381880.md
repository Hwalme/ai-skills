

<p align="center">
  <img src="assets/banner.png" alt="Claude Ecom" width="100%">
</p>

# claude-ecom

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/claude-ecom?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/claude-ecom)

Turn order/sales CSV into a business review — KPI decomposition, prioritized findings, and concrete next actions. One command.

<p align="center">
  <img src="assets/claude_ecom_demo.gif" alt="claude-ecom demo" width="100%">
</p>

---

## Who This Is For

- Data Analysts / Marketers who write monthly business reviews from scratch every time
- D2C brand owners, retail managers, or ecommerce managers without an analyst on staff
- Anyone who knows revenue dropped but can't explain why

## Quick Start

Install as a Claude Code plugin:

```
/plugin marketplace add takechanman1228/claude-ecom
/plugin install claude-ecom@claude-ecom
```

Then drop your orders CSV into the project and run:

```
/claude-ecom:ecom review
```

The Python backend installs itself into a private venv
(`~/.local/share/claude-ecom/`) on session start and survives plugin
updates. Requires: Claude Code, Python 3.10+

### CLI only (no Claude Code)

The compute engine works standalone — it generates `review.json` and a
basic report, without the narrative layer:

```bash
pip install claude-ecom
ecom review orders.csv
```

### Migrating from v0.1.x (curl installer)

Versions up to 0.1.3 installed via `install.sh` into `~/.claude/skills/ecom`.
That copy will conflict with the plugin (duplicate skills). Remove it:

```bash
rm -rf ~/.claude/skills/ecom
```

## What You Get

A single `REVIEW.md` that reads like a consultant wrote it:


```
# Business Review
> Revenue reached $9.37M for the year, essentially flat YoY (-1.7%), despite strong
> short-term momentum — the last 90 days surged 84% and November posted +28.5%,
> both driven by Q4 seasonal demand rather than structural growth. The flat annual...
```

```
           30d Pulse       90d Momentum     365d Structure
Revenue    $1.47M (+ 28%)  $3.73M (+ 84%)   $9.37M (= -2%)
Orders     3,499 (+ 26%)   8,814 (+ 60%)    24,812 (- 11%)
AOV        $419 (+ 2%)     $424 (+ 15%)     $378 (+ 10%)
Customers  1,676 (+ 11%)   2,918 (+ 51%)    4,296 (= flat)
...
```
```
Revenue $9.37M (YoY: -1.7%)
├── 🔴 New Customer Revenue $1.45M (15.5%)
│   ├── New Customers: 1,559 (-57.8%)
│   └── New Customer AOV: $305
└── 🟢 Existing Customer Revenue $7.92M (84.5%)
    ├── Returning Customers: 2,737 (+345%)
    ├── Returning AOV: $395
    └── Repeat Purchase Rate: 75.4%
```
Executive summary → Multi-horizon dashboard → KPI trees with 🔴/🟢 signals → Findings with "what / why / what to do" → Prioritized action plan with deadlines, success metrics, and guardrails.
[See a full example output →](examples/online-retail-ii/REVIEW.md)


## Commands

| Command | Description |
|---------|-------------|
| `/claude-ecom:ecom review` | Full business review — auto-selects 30d / 90d / 365d |
| `/claude-ecom:ecom review 30d` / `90d` / `365d` | Focus on a specific period |
| `/claude-ecom:ecom review How's retention?` | Ask a question instead of a full report |

You can also just ask in plain language — "review my store", "how was
last month?" — and Claude invokes the skill automatically.

## Input

Any e-commerce/retail orders CSV works. 

Required columns: order ID, order date, customer ID or email, revenue (after discounts, before tax/shipping).
Optional (enables deeper analysis): quantity, SKU or product name, discount amount. In many cases, column names don't need to match exactly.


## How It Works

```
Orders CSV → Python engine → review.json → Claude → REVIEW.md
```

Python computes every KPI and runs health checks. Claude reads the structured output and writes the business narrative. Numbers are precise because Python owns them. Interpretation is sharp because Claude owns that.



## Example

Tested on [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) (UCI, CC BY 4.0) — a real UK retailer with ~1M transactions over 2 years.

[See the full report →](examples/online-retail-ii/REVIEW.md) | [Try it yourself →](examples/online-retail-ii/)

## Roadmap

- [ ] Shopify API integration (skip CSV export)
- [ ] Weekly digest mode
- [ ] Multi-store comparison

## Acknowledgements

Inspired by [claude-ads](https://github.com/AgriciDaniel/claude-ads) by [@AgriciDaniel](https://github.com/AgriciDaniel).

## License

MIT
