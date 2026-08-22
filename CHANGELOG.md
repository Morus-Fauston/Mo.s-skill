# Changelog

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