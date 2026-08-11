<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>Self-developed Skills and MCP services for platforms and enterprises in the agent era.</p>
  <p>
    <a href="README_zh.md">中文</a> ·
    <a href="#install-skills">Skills</a> ·
    <a href="#install-mcp">MCP</a> ·
    <a href="#install-rest-api">REST API</a>
  </p>
  <p>
    <a href="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml"><img src="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  </p>
</div>

All capabilities are built, tested, and operated by Agent Body, so platforms do not have to evaluate and maintain inconsistent community services.

## Why Agent Body

- **Built in-house:** We develop every Skill and its backend service.
- **Reliable:** Thoroughly tested and continuously maintained.
- **One integration:** Add multiple capabilities through one connection.
- **Dedicated support:** One-on-one integration support for enterprise customers.

## Install

Choose one or more integration methods. Skills teach an AI agent how to use a capability, MCP connects an agent client directly, and REST integrates the same Tools into application code.

### Install Skills

#### Install all Skills

Tell your AI agent:

> Install all Agent Body Skills. Skill source: [https://github.com/agentbody/skills](https://github.com/agentbody/skills). Verify they work after installation.

#### Install one Skill

Use the source link in the table, for example:

> Install the Agent Body document-parsing Skill. Skill source: [https://github.com/agentbody/skills/tree/main/skills/document-parsing](https://github.com/agentbody/skills/tree/main/skills/document-parsing). Verify it works after installation.

#### Skill catalog and usage examples

Installed Skills use the listed MCP endpoint on `api.agentbody.io` over HTTPS port `443`.

| Skill source | MCP endpoint | Example request after installation |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp/account` | “Show my current balance and API key quota.” |
| [people-data](skills/people-data/SKILL.md) | `/mcp/people-data` | “Find the public business email for this LinkedIn profile.” |
| [find-leads](skills/find-leads/SKILL.md) | `/mcp/find-leads` | “Find recent Reddit posts from founders looking for CRM alternatives.” |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/mcp/competitor-monitoring` | “Research recent customer reactions to this competitor.” |
| [demand-research](skills/demand-research/SKILL.md) | `/mcp/demand-research` | “Research budget and buying-intent signals for accounting automation.” |
| [document-parsing](skills/document-parsing/SKILL.md) | `/mcp/document-parsing` | “Parse the PDF at this HTTPS link and return pages 1 through 5 as Markdown.” |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/mcp/humanizer` | “Rewrite this text naturally while preserving all facts.” |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | `/mcp/youtube-transcript` | “Extract the English transcript from this YouTube video.” |
| [tiktok-transcript](skills/tiktok-transcript/SKILL.md) | `/mcp/tiktok-transcript` | “Extract the existing captions from this TikTok video.” |

One MCP endpoint corresponds to one Skill. A Skill supplies the workflow; the Tools execute it.

### Install MCP

Access to Agent Body MCP services is provided through the [Agent Body community on Discord](https://discord.gg/TxuDBzAYJr). Obtain an API key, then add the required services to a client that supports Streamable HTTP MCP. To install all services, use:

Production host: `api.agentbody.io`; transport: HTTPS; port: `443`.

```json
{
  "mcpServers": {
    "account": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/account",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "people-data": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/people-data",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "find-leads": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/find-leads",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "competitor-monitoring": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/competitor-monitoring",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "demand-research": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/demand-research",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "document-parsing": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/document-parsing",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "humanizer": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/humanizer",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "youtube-transcript": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/youtube-transcript",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "tiktok-transcript": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/tiktok-transcript",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    }
  }
}
```

Replace `<AGENT_BODY_API_KEY>` with the credential provided by the community. Keep only the services you need. Store the credential in your platform's secret store and never commit it to a Skill or repository. Legacy paths such as `/mcp`, `/people-data/mcp`, and `/humanizer/mcp` are not supported.

#### MCP endpoints and call examples

MCP clients invoke Tools with `tools/call`. The protocol request has this shape:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "account_quota",
    "arguments": {}
  }
}
```

| MCP endpoint | All available Tools | Example Tool call |
|---|---|---|
| `/mcp/account` | `account_quota`, `usage_summary`, `usage_history` | `account_quota {}` |
| `/mcp/people-data` | `linkedin_email_lookup`, `linkedin_phone_lookup`, `linkedin_person_profile`, `linkedin_people_search`, `youtube_email_finder` | `linkedin_email_lookup {"profileUrl":"https://www.linkedin.com/in/example"}` |
| `/mcp/find-leads` | `find_leads_create_monitor`, `find_leads_get_signals`, `find_leads_review_signals` | `find_leads_create_monitor {"objective":"Find founders seeking CRM alternatives","until":"Collect 5 relevant signals","source":"reddit"}` |
| `/mcp/competitor-monitoring` | `competitor_monitoring_create_monitor`, `competitor_monitoring_get_signals`, `competitor_monitoring_review_signals` | `competitor_monitoring_create_monitor {"objective":"Research reactions to Acme CRM","until":"Collect 5 relevant signals","source":"reddit"}` |
| `/mcp/demand-research` | `demand_research_create_monitor`, `demand_research_get_signals`, `demand_research_review_signals` | `demand_research_create_monitor {"objective":"Research demand for accounting automation","until":"Collect 5 budget or intent signals","source":"reddit"}` |
| `/mcp/document-parsing` | `document_parsing`, `document_result_get` | `document_parsing {"fileUrl":"https://files.example.com/report.pdf","fileName":"report.pdf"}` |
| `/mcp/humanizer` | `humanizer_text` | `humanizer_text {"text":"This is the text to rewrite.","mode":"balanced"}` |
| `/mcp/youtube-transcript` | `youtube_transcript` | `youtube_transcript {"url":"https://www.youtube.com/watch?v=VIDEO_ID","language":"en"}` |
| `/mcp/tiktok-transcript` | `tiktok_transcript`, `tiktok_audio_to_transcript` | `tiktok_transcript {"url":"https://www.tiktok.com/@example/video/VIDEO_ID","language":"en"}` |

The Tool Reference inside each Skill contains every Tool's exact inputs and outputs. MCP uses `X-Idempotency-Key` for optional request idempotency. Successful calls return business data in `structuredContent.data`; business failures set `isError: true` and return a stable `code`.

### Install REST API

REST and MCP expose the same Tools through the same authorization, validation, billing, and usage pipeline. List the Tools visible to the current API key:

Production base URL: `https://api.agentbody.io` (HTTPS port `443`).

```bash
curl https://api.agentbody.io/v1/tools \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}"
```

Call a Tool by its dotted Tool ID:

```bash
curl -X POST https://api.agentbody.io/v1/tools/linkedin.email_lookup/call \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: lookup-001" \
  --data '{"profileUrl":"https://www.linkedin.com/in/example"}'
```

There is one discovery endpoint and 23 concrete Tool call endpoints. Use the JSON body shown below with the same Bearer and `Content-Type` headers as the example.

| REST endpoint | Example JSON body |
|---|---|
| `GET /v1/tools` | No body |
| `POST /v1/tools/account.quota/call` | `{}` |
| `POST /v1/tools/usage.summary/call` | `{"from":"2026-08-01T00:00:00Z","to":"2026-08-05T00:00:00Z"}` |
| `POST /v1/tools/usage.history/call` | `{"limit":20,"status":"success"}` |
| `POST /v1/tools/linkedin.email_lookup/call` | `{"profileUrl":"https://www.linkedin.com/in/example"}` |
| `POST /v1/tools/linkedin.phone_lookup/call` | `{"profileUrl":"https://www.linkedin.com/in/example"}` |
| `POST /v1/tools/linkedin.person_profile/call` | `{"linkedin_url":"https://www.linkedin.com/in/example"}` |
| `POST /v1/tools/linkedin.people_search/call` | `{"jobTitle":["Founder"],"location":["Singapore"],"companyFilter":"current"}` |
| `POST /v1/tools/youtube.email_finder/call` | `{"channels":["https://www.youtube.com/@example"],"scrape_fresh_emails":false}` |
| `POST /v1/tools/find_leads.create_monitor/call` | `{"objective":"Find founders seeking CRM alternatives","until":"Collect 5 relevant signals","source":"reddit","limits":{"target":5}}` |
| `POST /v1/tools/find_leads.get_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","search_queries":[{"source":"reddit","query":"CRM alternative for startup","strategy":"recent","time_window":"month"}],"limit":5}` |
| `POST /v1/tools/find_leads.review_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","reviews":[{"lead_id":"LEAD_ID","verdict":"relevant","reason":"Explicit buying intent"}]}` |
| `POST /v1/tools/competitor_monitoring.create_monitor/call` | `{"objective":"Research reactions to Acme CRM","until":"Collect 5 relevant signals","source":"reddit","limits":{"target":5}}` |
| `POST /v1/tools/competitor_monitoring.get_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","search_queries":[{"source":"reddit","query":"Acme CRM review","strategy":"recent","time_window":"month"}],"limit":5}` |
| `POST /v1/tools/competitor_monitoring.review_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","reviews":[{"lead_id":"LEAD_ID","verdict":"relevant","reason":"Specific product feedback"}]}` |
| `POST /v1/tools/demand_research.create_monitor/call` | `{"objective":"Research demand for accounting automation","until":"Collect 5 budget or intent signals","source":"reddit","limits":{"target":5}}` |
| `POST /v1/tools/demand_research.get_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","search_queries":[{"source":"reddit","query":"accounting automation budget","strategy":"relevance","time_window":"quarter"}],"limit":5}` |
| `POST /v1/tools/demand_research.review_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","reviews":[{"lead_id":"LEAD_ID","verdict":"relevant","reason":"Contains a budget statement"}]}` |
| `POST /v1/tools/document.parsing/call` | `{"fileUrl":"https://files.example.com/report.pdf","fileName":"report.pdf"}` |
| `POST /v1/tools/document.result.get/call` | `{"documentId":"550e8400-e29b-41d4-a716-446655440000","pageStart":1,"pageEnd":10}` |
| `POST /v1/tools/humanizer.text/call` | `{"text":"This is the text to rewrite.","language":"en","mode":"balanced"}` |
| `POST /v1/tools/youtube.transcript/call` | `{"url":"https://www.youtube.com/watch?v=VIDEO_ID","language":"en"}` |
| `POST /v1/tools/tiktok.transcript/call` | `{"url":"https://www.tiktok.com/@example/video/VIDEO_ID","language":"en"}` |
| `POST /v1/tools/tiktok.audio_to_transcript/call` | `{"url":"https://www.tiktok.com/@example/video/VIDEO_ID"}` |

Successful calls return `{"data": {...}}`. Errors return `{"error":{"code":"...","message":"..."}}`. `Idempotency-Key` is optional but recommended for retryable calls. API key permissions and runtime enablement determine which Tools appear in `GET /v1/tools`.

`GET /v1/tools` returns one entry per visible Tool. `input_schema` and `output_schema` are complete JSON Schemas; the output schema below is abbreviated for readability.

```json
{
  "data": [
    {
      "id": "linkedin.email_lookup",
      "name": "linkedin_email_lookup",
      "description": "Look up an email address from a LinkedIn profile URL.",
      "input_schema": {
        "type": "object",
        "properties": {"profileUrl": {"type": "string", "format": "uri"}},
        "required": ["profileUrl"],
        "additionalProperties": false
      },
      "output_schema": {"type": "object"},
      "annotations": {
        "readOnlyHint": true,
        "destructiveHint": false,
        "idempotentHint": false,
        "openWorldHint": true
      }
    }
  ]
}
```

`name` is always the Tool ID with dots replaced by underscores, which is exactly the MCP Tool name. Prices, provider names, provider URLs, and credentials are never part of a response.

## Contributing

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [MIT License](LICENSE)
