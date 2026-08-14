# 三档精选指南

三档仍然保留，但它们现在表达的是**安装范围建议**，不是某个脚本的安装参数。先选择要采用的范围，再按你的 Agent 支持的原生方式安装各项内容。

| 档位 | 包含什么 | 适合谁 | 安装责任 |
| --- | --- | --- | --- |
| `own` | Mo.s-Skill 自有的 8 个原创 Skill | 只需要自有内容的局部工作流，或已有等价的方案收敛与实际调研能力 | 未指定时从本仓库 `skills/` 复制使用版文件；维护时才复制完整目录 |
| `recommended` | `own` 加 31 个日常工程上游 Skill | 想直接采用作者推荐的 Mo 工作流组合，并补齐通用工程能力 | 自有 Skill 从本仓库复制；上游 Skill 从官方渠道单独安装 |
| `all` | `own` 加 47 个上游 Skill，共 55 个当前筛选后的可用 Skill | 想与作者当前筛选后的可用集合对齐 | 按每个上游项目和 Agent 的官方方式逐项安装 |

## `own`：Mo.s-Skill 核心集

此档只分发本仓库以 MIT 发布的内容，但它不是完整工作流的无依赖模式。`own` 适合只使用不需要外部执行的局部能力，或你的 Agent 已经提供等价的方案收敛和实际调研流程。

| Skill | 用途 |
| --- | --- |
| `changelog-writer` | 根据 Git 事实起草双格式更新日志；提交或推送前等待确认。 |
| `decision-to-spec` | 将已确认决定同步到正式项目文档。 |
| `docs-integrity-audit` | 审计文档入口、链接、状态和术语的一致性。 |
| `evidence-based-validation` | 为单项改动选择最小、可复核的验证。 |
| `interaction-prototype-to-spec` | 先通过可体验原型收敛复杂交互，再形成规格。 |
| `phase-acceptance` | 按阶段、版本或里程碑执行验收。 |
| `research-brief` | 为独立 Agent 编写范围与证据标准明确的调研任务书。 |
| `skill-workflow-visualizer` | 基于真实 Skill 正文核对触发关系并绘制工作流。 |

### `own` 的推荐搭配

以下 Skill 不被复制进本仓库。它们是默认推荐搭配，不是硬依赖：使用者可以采用职责等价、且已在项目规则中明确的替代工作流。

| Mo Skill | 何时推荐上游 Skill | 默认推荐 Skill | 原因 |
| --- | --- | --- | --- |
| `decision-to-spec` | 讨论还没有形成可同步的明确决定 | `grill-with-docs` | 先追问、挑战取舍并收敛术语与决定，再同步文档。 |
| `docs-integrity-audit` | 发现的是方案或术语分歧，而不是机械文档问题 | `grill-with-docs` | 审计不能替用户裁决产品决定。 |
| `interaction-prototype-to-spec` | 原型体验后仍有产品取舍未定 | `grill-with-docs` | 在形成交互契约前收敛未决规则。 |
| `research-brief` | 已确认需要实际调查并准备派发 | `research` | 本 Skill 只产出任务书；`research` 负责查证并写出研究发现。 |
| `skill-workflow-visualizer` | 指定的本地正文或上游来源无法直接访问 | `research` | 常规情况可直接读取本地正文或指定来源；只有缺少可读证据时，才需要额外调查。 |

因此，`own` 可以安装和使用。需要上述能力而项目没有等价流程时，建议安装 `grill-with-docs` 和 `research`，即采用 `recommended`。

## `recommended`：日常工程补充集

此档包含 `own`，并参考 [manifests/recommended.json](../manifests/recommended.json) 中记录的 31 个上游选择。`grill-with-docs` 与 `research` 是 Mo 工作流的**默认推荐搭档**；其余条目构成日常工程的完整组合：

| 方向 | Skill |
| --- | --- |
| 规划、架构与任务拆解 | `ask-matt`、`think`、`codebase-design`、`domain-modeling`、`implement`、`improve-codebase-architecture`、`to-spec`、`to-tickets`、`triage`、`wayfinder` |
| 排错、评审与质量 | `check`、`code-review`、`health`、`hunt`、`tdd`、`teach` |
| 调研、阅读与表达 | `learn`、`read`、`research`、`write` |
| 讨论、原型与交接 | `grill-me`、`grilling`、`grill-with-docs`、`handoff`、`prototype` |
| 界面与浏览器验证 | `ui`、`webapp-testing`、`kill-ai-slop` |
| 文档与 Git 操作 | `doc-coauthoring`、`git-guardrails-claude-code`、`resolving-merge-conflicts` |

`grill-with-docs` 和 `research` 代表作者推荐的默认组合。项目已有职责等价流程时，可不安装并在项目规则中说明替代关系。表中除 `kill-ai-slop` 外的项目分别来自 Matt Pocock Skills 和 Agentic Plugin Marketplace；各项的正确安装方式以各上游官方说明为准。

## `all`：完整精选来源索引

此档包含 `own`，并扩展到 [manifests/all-used.json](../manifests/all-used.json) 中记录的 47 个上游 Skill。基线是作者在 2026-08-14 已筛选的 Copilot 用户级可加载集合，再加已安装在共享 Agent Skill 目录中的 `ppt-master`：8 个自有 Skill 加 47 个上游 Skill，共 55 个。它不是扫描所有目录后得到的机械并集，已删除或占位的低价值 Skill 不会因为仍留在其他目录而重新进入清单。

| 来源 | 覆盖方向 | 注意事项 |
| --- | --- | --- |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | 规划、工程实现、领域建模、调研、学习与交接 | 某些工作流依赖 issue tracker 或项目初始化约定，不应默认启用。 |
| [Anthropic Skills](https://github.com/anthropics/skills) | 文档、表格、PPT、设计、创意与 MCP 示例 | 各目录的许可证并不完全相同，文档类内容可能是 source-available。 |
| [Agentic Plugin Marketplace](https://github.com/wshobson/agents) | 疑难诊断、长文协作、Git 防护与冲突解决 | 各 Agent 的原生安装入口不同，应按其 harness 文档操作。 |
| [Kill AI Slop](https://github.com/yetone/kill-ai-slop) | Web 项目的视觉与文案默认模式扫描、审阅和小范围修正 | Apache-2.0；安装完整 `skill/` 目录，包含扫描脚本和参考资料。 |
| [PPT Master](https://github.com/hugohe3/ppt-master) | 原生可编辑 PowerPoint 工作流 | 已安装在作者的共享 Agent Skill 目录；部分能力需要 Python 运行时依赖。 |

### `all` 的完整上游清单

| 来源 | Skill |
| --- | --- |
| Matt Pocock Skills | `ask-matt`、`check`、`code-review`、`codebase-design`、`domain-modeling`、`grill-me`、`grill-with-docs`、`grilling`、`handoff`、`health`、`hunt`、`implement`、`improve-codebase-architecture`、`learn`、`prototype`、`read`、`research`、`setup-matt-pocock-skills`、`tdd`、`teach`、`think`、`to-spec`、`to-tickets`、`triage`、`ui`、`wayfinder`、`webapp-testing`、`write`、`writing-great-skills` |
| Anthropic Skills | `algorithmic-art`、`brand-guidelines`、`canvas-design`、`docx`、`frontend-design`、`mcp-builder`、`pdf`、`pptx`、`skill-creator`、`theme-factory`、`web-artifacts-builder`、`xlsx` |
| Agentic Plugin Marketplace | `diagnosing-bugs`、`doc-coauthoring`、`git-guardrails-claude-code`、`resolving-merge-conflicts` |
| Kill AI Slop | `kill-ai-slop` |
| PPT Master | `ppt-master` |

以下目录或模板被明确排除，不计入 55 个可加载 Skill：

| 名称 | 排除原因 |
| --- | --- |
| `decision-to-spec-workspace` | 本机工作区辅助目录，不含 `SKILL.md`，不是独立可加载 Skill。 |
| `phase-acceptance-workspace` | 本机工作区辅助目录，不含 `SKILL.md`，不是独立可加载 Skill。 |
| `template-skill` | 上游占位模板，正文仍是“Replace with description...”，不属于作者保留的可用 Skill。 |

`all` 不是“建议所有人安装全部”，而是“与作者当前筛选后的可用集合对齐”。安装前仍应逐项检查：是否已被当前 Agent 内其他 Skill 覆盖、是否需要额外运行时、是否符合项目的权限和文档规则。

## 如何使用三档

1. 只要自有工作流时选择 `own`；需要完整日常工程组合时选择 `recommended`。
2. 要复现作者当前筛选后的可用 Skill 集合时选择 `all`，并跳过上表列出的排除项。
3. 任何上游 Skill 都从其官方渠道安装；本仓库只记录选择、来源和边界。

安装方法和更新原则见 [installation.md](installation.md)，来源与许可边界见 [source-attribution.md](source-attribution.md)。