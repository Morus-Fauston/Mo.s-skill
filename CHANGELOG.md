# Changelog

## v0.9.0 (2026-10-20 23:36)

### 新增

- **SAT 提交员专版**：新增 sat-changelog-writer，独立于个人版维护。
  - 主管确定版本、批次与写入范围；Changelog 和具体提交差异仅交主管审阅，不增加独立审阅员。
  - 明确批准后内容变化、混杂暂存、同仓库串行、本地核对后解冻及原 commit 推送跟踪。
  - 项目规范优先；无对应规范时沿用双日志及 TXT 完整区块提交信息。
- **评测场景**：新增 11 个场景、46 条期望，覆盖授权、审阅、索引污染和推送结果不明等边界。

### 文档

- **入口说明**：README 更新为十个个人版和一个 SAT 专版，区分角色限定、确认门与分发边界。

### 文件变更表

| 文件 | 变更 |
|:-----|:-----|
| skills/sat-changelog-writer/SKILL.md | 新增提交员行为契约 |
| skills/sat-changelog-writer/references/changelog-format.md | 新增独立默认格式 |
| skills/sat-changelog-writer/evals/evals.json | 新增评测场景库 |
| README.md | 更新数量、入口和适用边界 |

### 已知问题

- 场景库尚无可执行 runner，未取得模型行为评测结果。

### 待完成

- SAT 定向加载、业务入口和隔离环境验证尚未实施，需后续授权。

### 刻意不做

- 不修改个人版，不安装 Skill，不实现 SAT 工具或预设。
- 本轮只完成正文、契约和场景；静态检查不作为端到端通过证据。

---

## v0.8.0 (2026-10-20 22:53)

### 破坏性变更

- **四个 Skill 改为仅用户可调用**：`repository-docs-bootstrap`、`skill-workflow-orchestrator`、`interaction-prototype-to-spec`、`skill-workflow-visualizer` 现在只在你点名或运行斜杠命令时启动，模型不再按意图自动触发。
  - 迁移：需要这些能力时显式点名 Skill 或运行对应斜杠命令；原来依赖自动转交的用法，改由你手动发起。
  - 原因：它们会一次创建几十个文件、产生「删哪个 Skill」这类元决策、需要你先体验原型，或者本身就是给人看的分析工具。

### 新增

- **调用分档**：每个 Skill 增加 `agents/openai.yaml`，写入 `interface.display_name` 与 `interface.short_description`；四个仅手动 Skill 同时写入 `policy.allow_implicit_invocation: false`，并在 frontmatter 加 `disable-model-invocation: true`，让 Claude Code 与 Codex 表现一致。
- **画图判据**：`skill-workflow-visualizer` 增加「画图时机与分层」，明确什么情况值得画图、不值得画图，总览层与单 Skill 层如何分开，以及单张图节点上限 7 个。
- **状态复杂度判据**：`interaction-prototype-to-spec` 增加「什么算复杂状态」四条判据（状态数 ≥4、有权限分支、有异步过程、有并发冲突）；四条都不成立时只用 `ui`，不引入 `prototype`。

### 调整

- **报告默认不落盘**：六个 Skill 的报告改为默认在对话中交付结论，只有用户明确要求，或项目已有记录目录时才写文件；路径固定为 `.scratch/reports/<skill>/<YYYY-MM-DD>-<主题>.md`。六处模板正文合计从 211 行压缩到 103 行。
- **转交句改写**：12 处指向仅手动 Skill 的转交改为「提醒用户自行运行」，避免在正文里画出不存在的自动链路。
- **描述改写**：四个仅手动 Skill 的 `description` 改为面向人的一句话说明，去掉触发词列表；保持自动触发的六个 Skill 保留原触发描述。

### 技术

- `README.md` 增加「调用」列和「调用方式」一节，说明哪些 Skill 需要手动启动及原因。

### 文件变更

| 文件 | 变更 |
|:-----|:------|
| `README.md` | **调整** — 增加调用分档与报告默认行为说明 |
| `skills/*/SKILL.md` | **调整** — 调用分档、报告精简、判据补充与转交句改写 |
| `skills/*/agents/openai.yaml` | **新增** — 十个 Skill 的 Codex 界面元数据；四个含 `policy` 块 |
| `CHANGELOG.md`、`CHANGELOG.txt` | **调整** — 记录 v0.8.0 |

### 已知问题

- 无。

### 待完成

- **报告骨架仍偏长**：六处模板合计 103 行（每处 15 至 19 行），其中约一半是表格结构。若要进一步压到每处 8 至 10 行，需要把表格改成字段列表，尚未决定。
- `evals/` 仍无可执行 runner：它是评测场景库，执行方式为人工或 Agent 复核。

### 刻意不做

- **不为四个仅手动 Skill 提供自动降级**：如果某个 Agent 不支持 `disable-model-invocation`，它仍可能被自动触发；这是 harness 能力差异，不通过改 Skill 正文来兜底。
- **不引入第三方文档审计脚本**：依赖未在本机验证的运行时，且上游逐 Skill 许可未核实。
- **不新增 Skill**：本轮只做调用分档、正文减负与判据补齐。

---

## v0.7.0 (2026-10-20 22:29)

### 调整

- **仓库结构收敛**：删除 `docs/`、`scripts/`、`manifests/`、`.github/`、`CONTRIBUTING.md`、`CONTEXT.md`，仓库只保留 `README.md`、`LICENSE`、双格式更新日志和 `skills/`。README 重写为单页入口，保留十个 Skill 的选择表、共同原则和安装方式。
- **共享维护契约移除**：删除 `skills/_shared/references/` 下的工作上下文、证据状态和确认门三份参考；九个 `SKILL.md` 的维护参考行改为自包含声明，`repository-docs-bootstrap` 补齐 `## 完成条件与上下文摘要` 结构。

### 修复

- **悬空转交**：`phase-acceptance` 与 `evidence-based-validation` 中对不存在的 `qa` Skill 的转交，改为项目既有的 issue、待办或缺陷登记流程。
- **状态档位缺失**：`decision-to-spec` 的同步状态从「完成 / 部分完成 / 阻塞」三档补齐为四档，增加「不通过」。
- **内容重复**：`changelog-writer` 正文与 `references/changelog-format.md` 重复的两份日志模板和写作规则删除，改为指向参考文件；`repository-docs-bootstrap` 中复述 references 的九条目录角色压缩为三条原则。
- **主入口竞争**：`docs-integrity-audit` 与 `repository-docs-bootstrap` 补齐双向排除句，明确 `adopt-existing` 只补缺失主来源与入口，不做全面审计。

### 新增

- **内容三分判据**：`skill-workflow-orchestrator` 增加 Expert / Activation / Redundant 三分检查表和四条判定要求，精简候选必须逐段给出 Skill 名、行号和归类。
- **决策记录质量条件**：`decision-to-spec` 增加三条最低质量条件，即负向后果不可为空、被否决方案必须写出最强支持理由、记录先于引用。
- **更新日志诚实惯例**：`references/changelog-format.md` 增加「已知问题」「待完成」「刻意不做」三段及其纯文本压缩形式；`changelog-writer` 要求破坏性变更置于版本条目首位并写明迁移动作。
- **审计退出码语义**：`docs-integrity-audit` 增加项目已有检查命令时 0、1、2 三种退出码的解读规则，并规定未运行机械检查时不能写「通过」。

### 技术

- **评测用例规范化**：`evals.json` 的 id 统一为 kebab-case 字符串；`repository-docs-bootstrap` 的七条用例补齐 `files` 字段。
- **元数据清理**：删除 `repository-docs-bootstrap/agents/openai.yaml`。它是十个 Skill 中唯一的 Codex 界面元数据，其余九个没有，保留会造成结构不一致。

### 文件变更

| 文件 | 变更 |
|:-----|:------|
| `README.md` | **重写** — 单页入口，含十个 Skill 选择表、共同原则与安装方式 |
| `.gitignore` | **调整** — 移除已删除路径的忽略规则 |
| `CONTEXT.md` | **删除** — 术语表随仓库结构收敛移除 |
| `CONTRIBUTING.md` | **删除** — 贡献规则由 README 与各 `SKILL.md` 承接 |
| `docs/`（7 个文档与 ADR） | **删除** — 不再随仓库分发 |
| `scripts/validate.ps1` | **删除** — 校验脚本不再随仓库分发 |
| `manifests/recommended.json`、`manifests/all-used.json` | **删除** — 上游来源索引不再随仓库分发 |
| `.github/copilot-instructions.md` | **删除** — 引用已删除的校验脚本 |
| `skills/_shared/references/`（3 个文件） | **删除** — 共享契约改为各 Skill 自包含 |
| `skills/repository-docs-bootstrap/agents/openai.yaml` | **删除** — 唯一的 Codex 界面元数据 |
| `skills/*/SKILL.md` | **调整** — 自包含声明、判定判据、边界句与转交修正 |
| `skills/changelog-writer/references/changelog-format.md` | **调整** — 三段诚实惯例与纯文本压缩形式 |
| `skills/*/evals/evals.json` | **调整** — id 规范与字段补齐 |

### 已知问题

- 无。

### 待完成

- 仍无可执行评测 runner：`evals/` 是评测场景库，执行方式为人工或 Agent 复核，尚无自动回归。

### 刻意不做

- **不引入第三方文档审计脚本**：依赖未在本机验证的运行时，且上游逐 Skill 许可未核实。
- **不把四个 Skill 的报告模板外移到 `references/`**：会改变使用版安装边界，留待结构稳定后单独评估。
- **不新增 Skill**：本次只做收敛与判据补齐，不扩大集合。
- **不删除 `evals/`**：它是每个 Skill 的质量证据，不属于介绍性文档。

---

## v0.6.0 (2026-10-10 12:33)

### 新增

- **仓库文档初始化 Skill**：新增 `repository-docs-bootstrap`，从目标仓库现有文档、目录、配置和 Agent 约定提取事实，生成本地化的文档治理初始化方案与检查清单。
- **MTP 默认治理骨架**：提供 `README.md`、`AGENTS.md`、`CONTEXT.md`、`Docs/当前决策/`、`Docs/ADR/`、`Docs/Research/`、`Docs/工作流/`、`Docs/验证反馈/`、`agents/` 和 `.scratch/` 的建立规则，并把 `records/`、`plans/`、`meetings/`、产品域和证据目录作为按事实启用的扩展。
- **Research 本地命名机制**：要求先从目标仓库建立类别表和主来源映射，再使用稳定类别代号、三位序号和中文主题命名；普通主题与文件名使用中文，产品名、平台名、库名、协议名、API 名和代码符号等专有名词保留原文，并提供 `SYS-001-WinUI窗口透明合成与透明度丢失机制调研.md` 等示例。
- **ADR 与 Agent 工作流参考**：补充中文 ADR 命名、决策边界、`AGENTS.md` 中个人惯用 Skill 路由，以及事实、决定、规格、执行和验收之间的转交规则。
- **票据与证据治理**：提供 `.scratch` 期次/功能目录、中文票据契约、`ready-for-agent` 到 `archived` 的状态机、失败返工、范围调整、封存重启、连续执行授权和跨 Agent 交接规则，并区分自动化、进程/端到端、真实环境和人工证据。
- **隐私边界与初始化评测**：增加私有仓库初始化的脱敏约束，禁止把个人信息、凭据、设备信息、私有业务内容和本机绝对路径写入可发布文档；新增治理骨架、Research 分类和隐私边界评测用例。

### 调整

- **自有 Skill 清单**：纳入 `repository-docs-bootstrap` 后，自有 Skill 从 9 个更新为 10 个，`recommended` 从 43 个更新为 44 个，`all` 从 62 个更新为 63 个。
- **仓库导航与工作流说明**：同步 README、分层清单、安装与更新、Skill 选择、工作流协作、工作流设计哲学、来源与许可及共享维护契约中的 Skill 数量、入口和协作关系。
- **许可证署名**：将版权主体从 `Mo` 更正为 `Morus-Fauston`。

### 文件变更

| 文件 | 变更 |
|:-----|:------|
| `skills/repository-docs-bootstrap/SKILL.md` | **新增** — 仓库文档治理初始化入口 |
| `skills/repository-docs-bootstrap/references/governance-baseline.md` | **新增** — MTP 默认骨架、Research 命名、ADR 和 Agent 工作流参考 |
| `skills/repository-docs-bootstrap/references/reproduction-manifest.md` | **新增** — 文档、票据、证据和扩展模块复现清单 |
| `skills/repository-docs-bootstrap/references/ticket-governance.md` | **新增** — 票据状态、证据和交接基线 |
| `skills/repository-docs-bootstrap/references/bootstrap-checklist.md` | **新增** — 初始化检查清单 |
| `skills/repository-docs-bootstrap/agents/openai.yaml` | **新增** — Skill 入口元数据 |
| `skills/repository-docs-bootstrap/evals/evals.json` | **新增** — Skill 评测用例 |
| `README.md` | **调整** — 纳入第十个自有 Skill 及入口说明 |
| `docs/adr/0001-共享契约与独立Skill.md` | **调整** — 同步自有 Skill 数量 |
| `docs/分层清单.md` | **调整** — 同步三档清单和新增 Skill |
| `docs/安装与更新.md` | **调整** — 同步安装数量和组合说明 |
| `docs/工作流协作.md` | **调整** — 增加文档初始化入口 |
| `docs/工作流设计哲学.md` | **调整** — 同步自有 Skill 总数 |
| `docs/技能选择.md` | **调整** — 增加 `repository-docs-bootstrap` 选择项 |
| `docs/来源与许可.md` | **调整** — 同步自有 Skill 数量 |
| `manifests/all-used.json` | **调整** — 更新可加载 Skill 清单 |
| `LICENSE` | **调整** — 更新版权主体署名 |

---
## v0.5.1 (2026-08-23 04:48)

### 新增

- **上游写作与操作能力**：将 Matt Pocock Skills 的 `loop-me`、`setup-pre-commit`、`wizard`、`writing-beats`、`writing-fragments` 和 `writing-shape` 纳入 `all` 精选来源索引，补齐人工操作向导、提交前检查和写作工作流能力。

### 调整

- **精选集合扩展**：将 `all` 从 56 个可加载 Skill 更新为 62 个，其中上游 Skill 从 47 个增加到 53 个。
- **安装说明同步**：同步三档安装范围中的 `all` 数量，避免安装说明与精选清单不一致。
- **来源说明同步**：扩展 Matt Pocock Skills 的职责描述，覆盖人工操作向导和写作工作流。

### 文件变更表

| 文件 | 变更 |
|:-----|:------|
| `manifests/all-used.json` | 将 6 个 Matt Pocock Skills 纳入 `all` 精选来源索引，并更新上游数量说明 |
| `docs/分层清单.md` | 同步 `all` 的 Skill 数量、明细和排除说明 |
| `docs/安装与更新.md` | 将 `all` 的可加载 Skill 数量从 56 更新为 62 |
| `docs/来源与许可.md` | 补充 Matt Pocock Skills 覆盖人工操作向导和写作工作流 |

---

## v0.5.0 (2026-08-23 03:55)

### 调整

- **上游来源重索引**：重新核对本地上游缓存与两个 manifest 的 Skill 来源，修正 `webapp-testing`、`doc-coauthoring`、`diagnosing-bugs`、`git-guardrails-claude-code` 和 `resolving-merge-conflicts` 的归属，并移除无法核验的 `writing-great-skills` 与未采用的 `wshobson/agents` 来源。
- **Waza 重索引**：将现有 Waza Skill 重新登记为 `check`、`health`、`hunt`、`learn`、`read`、`think`、`ui`、`write`，不新增 Skill 内容。

### 文档

- **文档路径汉化**：将 `docs/` 下现行文档、ADR 和研究文件改为中文文件名，并修复改名后遗留的相对链接。
- **清单同步**：同步 `recommended` 和 `all` 的数量、上游来源、Skill 明细、排除项及安装说明，加入 Huashu Design 和 Waza 的来源说明。
- **本机盘点隔离**：将本机 Agent Skill 盘点文件加入 `.gitignore`，避免机器状态进入版本控制。

### 技术

- **校验增强**：扩展 `validate.ps1` 对本地 Skill、评测文档、manifest JSON、数量和重复来源的检查。
- **评测覆盖**：增加上游路由、证据复用、用户确认和工作流编排场景的评测用例。

### 文件变更表

| 文件 | 变更 |
|:-----|:------|
| `.gitignore` | 更新本机盘点和上游参考文件的忽略规则 |
| `manifests/recommended.json`、`manifests/all-used.json` | 修正上游来源并同步精选清单 |
| `scripts/validate.ps1` | 增强 Skill、评测和 manifest 校验 |
| `docs/` | 汉化文件名、修复链接并同步来源和数量说明 |
| `skills/_shared/references/evidence-status.md` | 增加共享证据状态参考 |
| `skills/*/SKILL.md`、`skills/*/evals/evals.json` | 更新路由、确认规则和评测覆盖 |

---

## v0.4.0 (2026-08-23 01:39)

### 新增

- **上游优先路由**：将本地 Skill 收敛为路由、治理、证据边界和人工确认层，优先调用上游 Skill 执行规格生成、原型制作、代码审查、浏览器验证和实际调研。
  - `decision-to-spec` 在缺少完整功能规格时转交 `to-spec`。
  - `interaction-prototype-to-spec` 默认调用 `ui` 制作视觉原型，复杂状态时补充 `prototype`。
  - `evidence-based-validation` 和 `phase-acceptance` 优先消费 `check`、`code-review`、`webapp-testing` 和项目测试结果。
  - `research-brief` 在用户确认任务书后转交 `research`。
- **上游参考缓存**：增加 `.skills/upstream/` 本机参考目录约定，用于保存官方上游仓库副本；该目录被 Git 忽略，不参与发布和运行时安装。
- **共享工作流契约**：新增工作上下文、证据状态和人工确认门参考文件。
  - 同一 Agent、同一上下文连续调用 Skill 时不要求填写表单。
  - 只有跨 Agent、跨会话或长期复用时，才按需摘要工作背景。
  - 默认不因上下文摘要创建独立过程文件。
- **领域术语和架构记录**：新增工作流领域术语说明和共享契约架构决策记录。

### 架构改进

- **职责分层**：将本地 Skill 与上游执行器明确分层，减少本地 Skill 对通用测试、原型、研究和规格流程的重复实现。
- **验证边界**：压缩 `evidence-based-validation` 和 `phase-acceptance` 中的执行教程，保留验证层选择、证据边界、阶段契约和人工验收判断。
- **交互原型路由**：压缩 `interaction-prototype-to-spec` 的原型实现说明，改为负责交互问题定义、方案比较、用户体验确认和交互契约整理。
- **状态分层**：区分工作项状态、验证项状态和阶段结论，避免将“待人工”“阻塞”和“部分通过”混为同一层级。
- **独立分发**：共享参考文件仅用于维护，不成为单个 Skill 的运行时硬依赖；每个 `SKILL.md` 保留独立运行所需的最小摘要。

### 调整

- **跨 Agent/跨会话上下文**：将原先容易误解为“跨 Skill 交接”的概念改为按需工作上下文摘要。
- **工作编号**：不再要求每个请求生成编号；只有跨 Agent、跨会话或已有 Issue/阶段编号时才使用。
- **评测覆盖**：增加并更新规格生成、验证、原型和阶段验收的跨 Skill 路由与上下文复用场景。
- **安装说明**：补充共享维护参考、上游参考缓存和独立 Skill 安装边界。
- **忽略规则**：忽略本轮生成的研究报告，不忽略整个 `docs/research/` 目录。

### 文件变更表

| 文件 | 变更 |
|:-----|:------|
| `skills/_shared/references/` | **新增** 工作上下文、证据状态和确认门参考 |
| `CONTEXT.md` | **新增** 工作流领域术语说明 |
| `docs/adr/0001-共享契约与独立Skill.md` | **新增** 共享契约与独立分发架构决策 |
| `skills/*/SKILL.md` | 更新上游路由、完成条件、上下文摘要和职责边界 |
| `skills/*/evals/evals.json` | 增加跨 Skill 路由、证据复用和用户确认场景 |
| `docs/工作流设计哲学.md`、`docs/技能选择.md`、`docs/工作流协作.md` | 更新工作流原则、入口选择和协作关系 |
| `docs/安装与更新.md`、`CONTRIBUTING.md` | 更新安装、维护和共享参考规则 |
| `manifests/*.json` | 同步上游来源和精选清单 |
| `.gitignore` | 忽略上游参考缓存和本轮研究报告 |

---

## v0.3.0 (2026-08-15 16:27)

### 新增

- **Skill 工作流重编排**：新增 `skill-workflow-orchestrator`，将已有 Skill 的事实基线转为可确认的主入口、转交、精简与新 Skill 候选方案。
  - 先要求 `skill-workflow-visualizer` 的真实正文分析结果，区分当前事实、历史观察和用户尚未确认的建议。
  - 新 Skill 仅在重复稳定、边界清楚、现有能力无法承接、封装有收益且可评测时进入候选；确认后转交 `skill-creator`。

### 架构改进

- **三层职责分离**：收敛 `skill-workflow-visualizer` 为事实提取、协作图与可选历史聚合信号层；重编排决策由 `skill-workflow-orchestrator` 负责，创建和评测由 `skill-creator` 负责。
- **人工确认边界**：允许基于事实基线直接分析重编排方案；只有更新工作流、安装范围、清单或创建、改造、删除 Skill 时才等待用户确认。

### 调整

- **安装范围一致性**：统一公开安装口径为 9 个自有 Skill、31 个推荐上游 Skill、47 个完整精选上游 Skill，即 `own = 9`、`recommended = 40`、`all = 56`。
- **可移植发布说明**：移除作者本机、共享目录和用户级安装状态描述，将 `all` 明确为可复现的精选来源索引。
- **维护约束**：仓库指令不再写死本地 Skill 数量；验证脚本从实际目录和 manifest 计算并报告三档总数。

### 文件变更表

| 文件 | 变更 |
|:-----|:------|
| `skills/skill-workflow-orchestrator/` | **新增** 重编排 Skill 与三组行为评测 |
| `skills/skill-workflow-visualizer/` | 收敛为事实可视化和历史聚合信号输入层 |
| `README.md`、`CONTRIBUTING.md`、`docs/*.md` | 更新仓库定位、协作边界、安装范围与来源说明 |
| `manifests/all-used.json` | 统一完整精选清单口径并移除机器状态描述 |
| `scripts/validate.ps1`、`.github/copilot-instructions.md` | 从实际数据计算数量，并移除写死的 Skill 数量 |

---

## v0.2.0 (2026-08-14 23:21)

### 新增

- **工作流设计哲学**：新增仓库定位文档，明确八个原创 Skill 的共同原则：从直接问题开始、区分事实/判断/决定、保留人工关口、按证据交付结果，并按职责组合可替换能力。
- **完整安装范围**：将 `all` 从仅列来源升级为可核对的完整上游 Skill 清单，明确 8 个自有加 47 个上游、共 55 个筛选后的可用 Skill。

### 调整

- **安装入口**：README 和安装说明改为先选择 `own`、`recommended` 或 `all`，避免独立 Agent 将复制本仓库 `skills/` 误解为完整安装。
- **推荐组合**：将 `recommended` 扩展为 31 个上游 Skill、共 39 个可加载 Skill，覆盖规划、架构、排错、测试、调研、文档、界面和 Git 操作。
- **筛选边界**：补充 `kill-ai-slop`，保留已安装的 `ppt-master`，并明确排除运行工作区产物和未填写的上游模板，避免残留目录进入安装基线。

### 架构改进

- **主体与参考分离**：明确 `skills/` 下八个原创 Skill 是发布主体；上游清单仅用于补齐、比较或替换相邻职责，不定义本仓库的产品主体或设计哲学。
- **维护约束**：贡献规则要求保持事实、判断与用户决定之间的边界，不能用自动化替代人工确认。

### 文件变更表

| 文件 | 变更 |
|:-----|:------|
| `docs/工作流设计哲学.md` | **新增** 工作流设计哲学、原创 Skill 分工与上游角色说明 |
| `README.md`、`CONTRIBUTING.md` | 明确仓库定位、安装入口与维护边界 |
| `docs/安装与更新.md`、`docs/分层清单.md` | 更新三档数量、完整 Skill 清单和排除规则 |
| `docs/来源与许可.md` | 调整上游来源定位与许可说明 |
| `manifests/recommended.json`、`manifests/all-used.json` | 扩展推荐清单，记录筛选后的 all 基线与排除项 |

---

## v0.1.0 (2026-08-14 22:05)

### 新增

- **原创 Skill 套件**：发布八个中文优先的 Agent Skills，分别覆盖决策同步、文档完整性、单改动验证、交互原型收敛、阶段验收、调研任务书、版本记录和工作流可视化。
- **双更新日志工作流**：提供 `changelog-writer`，同步起草详细 Markdown 与压缩纯文本记录，并把版本、文本、Git 动作与暂存范围收敛到一次人工确认。

### 架构改进

- **职责边界**：将 Skill 设计为可独立分发的最小工作流单元，明确已确认决定、未决方案、实际调研、验证证据和阶段交付之间的转交条件。
- **人工关口**：对正式文档写入、外部调研采纳和 Git 提交/推送保留用户确认，避免把推断自动升级为项目决定。
- **多 Agent 分发**：采用内容可移植的 Skill 目录，而非绑定特定 Agent 的安装脚本；默认安装使用版，维护和评测时才保留完整目录。

### 技术

- **版本规范**：更新日志采用双文件策略与标准 SemVer，支持 `alpha`、`beta`、`rc` 预发布标识，Git 标签可使用 `v` 前缀。
- **结构校验**：新增 PowerShell 验证脚本，校验八个 Skill 的 frontmatter、评测文档和上游来源索引，并以 UTF-8 读取中文 JSON。

### 文档

- **公开文档**：补充 Skill 选择、协作工作流、安装更新、三档精选及来源与许可边界说明。
- **上游搭配**：记录 Matt Pocock Skills 的 `grill-with-docs` 与 `research` 为推荐搭配，而非硬依赖；不再重新分发第三方 Skill 正文。

### 文件变更表

| 文件 | 变更 |
|:-----|:------|
| `skills/` | **新增** 八个原创 Skill、评测资料及更新日志格式参考 |
| `docs/` | **新增** 选择、工作流、安装、精选和来源边界文档 |
| `manifests/` | **新增** 推荐与历史上游来源索引 |
| `scripts/validate.ps1` | **新增** Skill、评测和索引结构校验 |
| `README.md`、`CONTRIBUTING.md`、`.github/copilot-instructions.md` | **新增** 入口、贡献与维护约束 |
