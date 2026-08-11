# AI Skills 分类总览（深度细分 · 便于检索）

> 更新：2026-08-11 · PD
> 用途：把全网 AI Skills 按**多层级分类**整理，越细分越好找。本表是"目录的目录"——
> 每个叶子给**代表 skill + 源头仓库**，全量 85,000+ 去源头抓（见末尾附录）。
> 交叉标签：🎬 电影 / 📱 漫剧 / 💼 商单 —— 表示该 skill 适用的生产形态（你的三形态准绳）。

---

## 0. 顶层板块索引（11 大板块）

| # | 板块 | 细分深度 | 代表子方向 |
|---|---|---|---|
| 1 | **AIGC 生成式 AI** | ★★★★★ 最深 | 生视频/生图/生音频/3D/商单专项 |
| 2 | 开发工程 Dev & Engineering | ★★★ | 前端/后端/质量/运维/数据层/集成/安全 |
| 3 | 文档与办公 Documents & Office | ★★ | PDF/Word/Excel/PPT/写作 |
| 4 | 数据 & AI/ML | ★★★ | 分析/可视化/ML/上下文工程 |
| 5 | 营销与增长 Marketing | ★★ | SEO/GEO/Ads/社媒 |
| 6 | 商业与办公 Business | ★★★ | 财务/销售/客户成功/法务/HR |
| 7 | Agent 工程 Agent Engineering | ★★★ | 编排/评测/安全/红队 |
| 8 | 设计与 UI/UX | ★★ | 前端设计/规范/无障碍/线框 |
| 9 | 研究与知识 Research | ★★ | 文献/学术/知识图谱 |
| 10 | 垂直行业 Vertical | ★★★ | 电商/教育/医疗/汽车机器人/交易/旅行 |
| 11 | 生产力 & 通信 Productivity | ★★ | 任务/会议/邮件/演示 |

---

## 1. AIGC 生成式 AI（顶级深分）

### 1.1 生视频 Video Generation
#### 1.1.1 文生视频 T2V
- **ComfyUI 工作流（文生视频）** 🎬📱💼
  - 代表：WAN2.1 / WAN2.2 文生视频、HunyuanVideo 文生视频、LTX-Video、CogVideoX ComfyUI 流程、Step-Video
  - 源头：ComfyUI 官方 examples、社区 workflow JSON 合集、各模型官方 ComfyUI 节点包
- **云平台 API 生视频** 🎬📱💼
  - Seedance（即梦）、Kling（可灵）、Sora、Runway Gen、Pika、Luma Dream Machine、Hailuo（海螺）、Vidu
  - 形态：🎬📱💼
- **程序化视频（代码驱动）** 💼🎬
  - Remotion 最佳实践、Remotion 工具包（动画/字幕/3D/图表/转场/媒体处理）
  - 源头：remotion-dev/skills、calesthio/OpenMontage（500+ 视频类 skill）

#### 1.1.2 图生视频 I2V
- **ComfyUI 图生视频工作流（首帧图 → 视频）** 🎬📱💼
- **首尾帧控制 / 关键帧插值**
- **运动笔刷 / 运动控制**（DragNUWA、MotionCtrl 思路的 ComfyUI 实现）
- 形态：🎬📱💼

#### 1.1.3 视频转绘 / 风格化 V2V
- **ComfyUI AnimateDiff / 转绘链**（图转视频再风格化）
- **风格迁移 / 动漫化 / 实拍转二次元**
- 形态：📱💼

#### 1.1.4 视频后期自动化
- **自动剪辑 / 转场 / 节奏对齐**（ffmpeg 抽帧/片段 skill）
- **字幕生成 / 多语言配音 / TTS 对齐**
- **特效 / 抠像 / 超分 / 降噪**（视频帧级处理）
- 形态：🎬📱💼

#### 1.1.5 数字人 / 口播
- **Lip-sync 对口型**（Wav2Lip、MuseTalk 流程）
- **数字人驱动 / 虚拟主播 / 商单口播**
- 形态：💼📱

### 1.2 生图 Image Generation
#### 1.2.1 文生图 T2I
- **ComfyUI 生图工作流（基础文生图）** 🎬📱💼
- **模型**：Flux / SDXL / SD1.5 / PixArt / 通义万相
- **云平台**：Midjourney / DALL·E / 即梦 / 可灵生图
- 形态：🎬📱💼

#### 1.2.2 图生图 / 重绘 I2I
- **ComfyUI img2img / inpaint / 局部重绘**
- **放大 / 重绘放大（Upscale）**
- 形态：🎬📱💼

#### 1.2.3 控制类 Control
- **ControlNet / IP-Adapter / LoRA 加载与管理**
- **姿态 / 深度 / 线稿 / 语义控制**
- **一致性（角色 / 场景保持）** —— 电影/漫剧关键
- 形态：🎬📱💼

#### 1.2.4 电商 / 商单图
- **商品图 / 虚拟模特 / 场景图**
- **海报 / 封面 / Banner / 电商详情页**
- 形态：💼

### 1.3 生音频 / 语音 Audio & Voice
#### 1.3.1 TTS 语音合成
- **edge-tts**（免费多语种，你的 Cinema 在用）
- **CosyVoice / GPT-SoVITS / Fish-Speech**（克隆 / 角色音色）
- 形态：🎬📱💼

#### 1.3.2 音乐生成
- **Suno / Udio / 开源替代**
- 形态：💼🎬

#### 1.3.3 音效 / 处理
- **音效生成 / 降噪 / 人声分离**
- 形态：🎬💼

### 1.4 3D / 模型生成
- **文生 3D / 图生 3D**（Tripo、Hyper3D 思路的 ComfyUI / API 流程）
- 形态：🎬💼

### 1.5 商单广告专项（跨形态）💼
- **商单视频流水线 / 批量生成 / 多尺寸适配（竖屏+横屏+方形）**
- **品牌一致性 / 文案-画面对齐**
- 形态：💼

---

## 2. 开发工程 Dev & Engineering
### 2.1 语言 / 栈
- 前端（React/Next/Vue）：`vercel-react-best-practices`、`frontend-design`、`web-design-guidelines`
- 后端（Node/Python/Go）：`api-design`、`security-best-practices`
- 全栈：`code-to-prd`（代码反向生成 PRD）
### 2.2 代码质量
- `code-review`、`debugging`（根因分析）、`refactoring`、`testing`（单元/集成/E2E）
### 2.3 运维 DevOps
- `ci-cd`、`cloud-monitoring`、`docker-compose-setup`、`infrastructure-as-code`（Terraform/Pulumi）、`kubernetes-*`
### 2.4 数据层
- `database-backup` / `database-migration` / `database-schema-design` / `database-seeding` / `query-optimization`
### 2.5 集成 Integration
- `api-integration`、`graphql-api-design`、`oauth-2-0-setup`、`webhook-setup`、`mcp-builder`（MCP 服务构建）
### 2.6 安全 Security
- `security-best-practices`（Go/Express/FastAPI/React）、`security-threat-model`、`security-ownership-map`、`web-security`

---

## 3. 文档与办公 Documents & Office
- **PDF**：读取/提取/拆分合并/表单/OCR/加解密 —— `anthropics/skills` 的 `pdf`
- **Excel**：公式/图表/清洗/校验 —— `xlsx`
- **PPT**：演示/模板/缩略图 —— `pptx`
- **Word**：批注/修订/转换 —— `docx`
- **文档共创**：`doc-coauthoring`
- **写作 / 技术文档 / 报告生成**：`report-generation`、`technical-writing`

---

## 4. 数据 & AI/ML
### 4.1 数据分析
- `data-analysis`、`data-cleaning`、`data-visualization`、`exploratory-data-analysis`、`sql-query-generation`
### 4.2 机器学习
- `data-labeling`、`hyperparameter-tuning`、`ml-pipeline-creation`、`model-deployment`、`model-training`
- 源头：`K-Dense-AI/scientific-agent-skills`（125+ 科研类）
### 4.3 上下文工程
- `context-compression`、`context-injection`、`context-optimization`、`context-ranking`、`context-retrieval`

---

## 5. 营销与增长 Marketing
- `seo-audit`（页面/关键词/技术 SEO）、`audit-website`（性能+安全+SEO+A11Y 全身体检）
- `geo`（生成式引擎优化）、`ads`
- 社媒内容 / 文案 / 邮件营销
- 源头：`coreyhaines31/marketingskills`、`nowork-studio/NotFair`（SEO/GEO/Ads）

---

## 6. 商业与办公 Business
### 6.1 财务与会计
- `budget-planning`（方差分析）、`expense-categorization`、`financial-modeling`（P&L/DCF）、`financial-report-generation`、`invoice-processing`
### 6.2 销售
- `sales-playbook`、`lead-qualification`、`crm`
### 6.3 客户成功
- `churn-analysis`、`customer-feedback-analysis`（NPS/CSAT）、`knowledge-base-article-writing`、`onboarding-playbook-creation`、`ticket-triage`
### 6.4 法务合规
- `contract-review`、`compliance-checks`、`gdpr/pipl` 合规巡检
### 6.5 人力资源
- 招聘 / 入职 / 绩效

---

## 7. Agent 工程 Agent Engineering
### 7.1 编排与质量
- `agent-evaluation`（评测/grader/发布门禁）、`agent-observability`（trace/metrics/成本归因）、`human-in-the-loop`（审批门/升级）
- `multi-agent-orchestration`（多智能体编排/交接/恢复）、`mcp-server-building`、`tool-schema-design`
### 7.2 安全（高价值）
- `agent-red-teaming`（授权对抗测试）、`prompt-injection-defense`、`skill-supply-chain-audit`（技能包恶意指令/权限/来源审计）
- 注：2026 研究在开放 hub 少数 skill 检出指令级攻击，供应链审计类是刚需。

---

## 8. 设计与 UI/UX
- `frontend-design`（Anthropic 官方说明书）、`web-design-guidelines`（Vercel 100+ 规则）、`accessibility-testing`（WCAG）、`wireframing`、`logo-design`、`user-flow-mapping`

---

## 9. 研究与知识 Research
- `literature-review`、`citation`、`knowledge-graph`、`research-synthesis`

---

## 10. 垂直行业 Vertical
- **电商**：选品 / listing 优化 / 供应链 —— `ecommerce`
- **教育**：课件 / 题库 / 学术写作
- **医疗健康**：健康顾问 / 生活规划
- **汽车 / 机器人**：jherrodthomas 合集（100+ / 76 skills）
- **金融交易**：tradermonty 交易 / 量化
- **旅行 / 本地**：行程规划 / 本地检索

---

## 11. 生产力 & 通信 Productivity & Communication
### 11.1 生产力
- `task-management`、`meeting-notes`、`automation`
### 11.2 通信
- `email-drafting`、`chatbot-conversation-design`、`meeting-transcription`、`presentation-creation`、`report-generation`

---

## 附录 A：源头仓库（抓全量 85k）

| 仓库 / 合集 | 规模 | 说明 |
|---|---|---|
| ossfork/awesome-claude-skills | 精选 | 经典 awesome 列表 |
| VoltAgent/awesome-agent-skills | 1400+ | 官方+社区（Anthropic/Stripe/Vercel/Cloudflare…） |
| seb1n/awesome-ai-agent-skills | 103（完整 SKILL.md） | 本文主要骨架来源，非链接目录 |
| aiworkskills/skillranking | 17 场景 × Top8 | Clawhub 品类精选榜 |
| anthropics/skills | 官方 | docx/xlsx/pptx/pdf/frontend-design/mcp-builder |
| openai/skills | 官方 | playwright/security-* |
| vercel-labs/agent-skills | 官方 | react/web-design/agent-browser |
| alirezarezvani/claude-skills | 337 | 含 code-to-prd |
| K-Dense-AI/scientific-agent-skills | 125+ | 科研 |
| calesthio/OpenMontage | 500+ | **视频创作类（AIGC §1.1 主源）** |
| nowork-studio/NotFair | — | 营销 SEO/GEO/Ads |
| yzfly/awesome-claude-skills-zh / JackyST0 | 中文 | 中文友好 |

## 附录 B：可发布平台（仅免费，付费已剔除）

| 平台 | 流量/规模 | 提交方式 | 账号 |
|---|---|---|---|
| skills.sh（Vercel） | 90,000+ 安装 | `npx skills add owner/repo` 触发收录 | GitHub 公开仓库 |
| agentskills.io（官方/AAIF） | 标准/SDK | 符合 spec 的公开仓库 | GitHub |
| agentskill.sh | 47,000+ | 网页 submit 贴 URL + 安全扫描 | GitHub 登录 |
| skillsmp.com | 25,000–66,500+ | 站点提交/从 GitHub 聚合 | GitHub |
| mcpmarket.com | DR52/1.4M 月访 | 列表提交流程 | GitHub |
| claudemarketplaces.com | DR36/277K | **自动抓取**公开仓库 | GitHub |
| skillhub.club | DR33/119K | 手动上传 SKILL.md | GitHub |
| claude-plugins.dev | DR30/26K | GitHub 自动收录 | GitHub |
| claudeskills.info | DR26/100K | 社区提交表单 | GitHub |
| claudepluginhub.com | DR13/168K | 抓取公开仓库 | GitHub |
| mcp.directory | DR16/134K | 提交仓库 | GitHub |
| skillsdirectory.com | DR20/79K（36,109 skills） | 网页 /submit（人工+扫描审核） | GitHub 登录 |
| mcpservers.org/agent-skills | 官方型 | 提交/聚合 | GitHub |
| agentskillsrepo.com | — | 网页提交 | 公开提交 |
| skillsplayground.com | DR16/20K | README 加 badge | GitHub |
| agentskills.so | DR19/156K | 抓取 skills.sh | （随 skills.sh） |
| tonsofskills.com | DR20/2K | 抓取 GitHub / ccpi CLI | GitHub |
| allyourtech.ai | DR37 | 免费提交表单 | — |
| claudeskillsmarket.com | DR2/28K | 抓取收录 | （随 GitHub） |
| skill0.io/zh | 中文友好 | 站点提交 | GitHub |
| GitHub CLI `gh skill publish` | 原生 | spec 校验+建议不可变发布 | GitHub |
| anthropics/skills 插件市场 | 原生 | `/plugin marketplace add` | GitHub/Claude |

**结论**：你只需 1 个 GitHub 账号，本仓库推上去即可覆盖上表 19+ 免费平台。
