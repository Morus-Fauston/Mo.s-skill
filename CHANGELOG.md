# Changelog

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
| `docs/workflow-philosophy.md` | **新增** 工作流设计哲学、原创 Skill 分工与上游角色说明 |
| `README.md`、`CONTRIBUTING.md` | 明确仓库定位、安装入口与维护边界 |
| `docs/installation.md`、`docs/curated-tiers.md` | 更新三档数量、完整 Skill 清单和排除规则 |
| `docs/source-attribution.md` | 调整上游来源定位与许可说明 |
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