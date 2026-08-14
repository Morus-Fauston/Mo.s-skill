# 三档精选指南

三档仍然保留，但它们现在表达的是**安装范围建议**，不是某个脚本的安装参数。先选择要采用的范围，再按你的 Agent 支持的原生方式安装各项内容。

| 档位 | 包含什么 | 适合谁 | 安装责任 |
| --- | --- | --- | --- |
| `own` | Mo.s-Skill 自有的 8 个原创 Skill | 只需要自有内容的局部工作流，或已有等价的方案收敛与实际调研能力 | 未指定时从本仓库 `skills/` 复制使用版文件；维护时才复制完整目录 |
| `recommended` | `own` 加默认推荐搭档和一组日常工程常用的上游 Skill | 想直接采用作者推荐的 Mo 工作流组合，并补齐通用工程能力 | 自有 Skill 从本仓库复制；上游 Skill 从官方渠道单独安装 |
| `all` | `recommended` 的范围之外，再加入完整的当前精选上游来源 | 已经了解自身 Agent 的插件、权限与维护方式，且需要更广覆盖 | 按每个上游项目和 Agent 的官方方式逐项安装 |

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

此档包含 `own`，并参考 [manifests/recommended.json](../manifests/recommended.json) 中记录的上游选择。当前上游来源为 [Matt Pocock Skills](https://github.com/mattpocock/skills)。其中 `grill-with-docs` 与 `research` 是 Mo 工作流的**默认推荐搭档**；其他 Skill 是按需补充：

| 方向 | Skill |
| --- | --- |
| 规划、排错与审查 | `think`、`hunt`、`check`、`code-review` |
| 调研与表达 | `research`、`read`、`write` |
| 实现与测试 | `tdd` |
| 讨论、原型与交接 | `grilling`、`grill-with-docs`、`prototype`、`handoff` |
| 界面与浏览器验证 | `ui`、`webapp-testing` |

`grill-with-docs` 和 `research` 代表作者推荐的默认组合。项目已有职责等价流程时，可不安装并在项目规则中说明替代关系。表内其余条目是常用补充；若与你的既有工作流重复，可不安装。各项的正确安装方式以 Matt Pocock Skills 的官方说明为准。

## `all`：完整精选来源索引

此档包含 `own`，并扩展到 [manifests/all-used.json](../manifests/all-used.json) 中记录的全部来源：

| 来源 | 覆盖方向 | 注意事项 |
| --- | --- | --- |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | 规划、工程实现、领域建模、调研、学习与交接 | 某些工作流依赖 issue tracker 或项目初始化约定，不应默认启用。 |
| [Anthropic Skills](https://github.com/anthropics/skills) | 文档、表格、PPT、设计、创意与 MCP 示例 | 各目录的许可证并不完全相同，文档类内容可能是 source-available。 |
| [Agentic Plugin Marketplace](https://github.com/wshobson/agents) | 疑难诊断、长文协作、Git 防护与冲突解决 | 各 Agent 的原生安装入口不同，应按其 harness 文档操作。 |
| [PPT Master](https://github.com/hugohe3/ppt-master) | 原生可编辑 PowerPoint 工作流 | 可选；部分能力需要 Python 运行时依赖。 |

`all` 不是“建议所有人安装全部”。它是维护者使用过、按来源保留的完整历史精选索引；在逐项核实当前名称、许可证、支持的 Agent 和官方安装方式前，不保证每项仍可安装。安装前应逐项检查：是否已被当前 Agent 内其他 Skill 覆盖、是否需要额外运行时、是否符合项目的权限和文档规则。

## 如何使用三档

1. 先从 `own` 开始，挑选一个正在解决的问题对应的 Skill。
2. 缺少通用工程能力时，按 `recommended` 表选择一个上游 Skill，并用该上游官方方法安装。
3. 只有在明确知道为什么需要某项额外能力时，才查阅 `all` 的来源索引。

安装方法和更新原则见 [installation.md](installation.md)，来源与许可边界见 [source-attribution.md](source-attribution.md)。