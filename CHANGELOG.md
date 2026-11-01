# Changelog

## v0.11.0 (2026-11-02 00:57)

### 调整

- **推荐研究入口迁移**：recommended 使用本仓库 research-mos 替换原 research，总数保持 44 项，由 11 个本仓库来源和 33 个上游来源组成。
  - 读取推荐清单时需同时处理 localSkills 与 packages，不能再只枚举上游包
  - 研究默认由当前会话负责，不强制先派子代理；有资格的主负责人可按需使用辅助，仍负责关键证据核验与最终结论
- **提交员规则对齐**：mat-changelog-writer 改为全项目唯一提交员跨仓顺序办理正式批次，补清角色／会话、合法空规范、冻结协调与未知结果处理；日志和具体差异仍只交主管审阅。
- **个人与 MAT 方法分开**：MAT 专版不替换个人代码审阅、实施、拆票、交接或 Waza hunt；四个原有手动入口保持调用策略。

### 新增

- **Mo’s 通用改写**：新增 research-mos 和 discernment-nudge-mos，分别用于可追溯调查与按对话语言表达的判断提醒。
  - 标题及显示名采用 Research、Discernment Nudge；提醒不固定英文结尾，保留按需触发、排除条件和同一对话最多一次的限制
- **MAT 工作方法**：新增 to-tickets-mat、implement-mat、review-mat、handoff-for-mat 和 MAT 专用 hunt。
  - 拆票覆盖开发、调查、文档和验证；实施完成交回而非自行提交
  - 审阅统一处理代码、报告及混合成果，当前会话直接审，作者自查不等于正式独审
  - 交接通过专用工具保存到受管项目 .TEAM/handoff/，不自动发送、创建接手会话或改变执行状态
- **For MAT 完整配套**：新增明确来源清单和五类型分配，包含 27 项基础方法与 5 项手动专题，共 32 项；本仓库提供 17 项，上游提供 15 项，不自动跟随推荐档更新。
- **评测与来源资料**：七个新目录附带 48 项场景，加上现有提交员 11 项，八项方法合计 59 项场景；补齐来源、修改说明、MIT／Apache-2.0 许可及两份通用方法的调用元数据。

### 文档

- **配套导航同步**：README、分层清单、安装与来源说明覆盖当前 18 份正文，区分源码数量、档位选择、实际安装和运行验证。
- **安装资源补齐**：明确初始化方法的四份参考文件、工作流可视化与编排的参考文件，以及派生包的来源／许可文件，避免只复制正文导致缺件。
- **范围差异说明**：own 保留原 10 项，all 保留原 63 项；all 暂不是新版 recommended 的严格超集。提醒本地化版的日常推荐替换尚未决定，For MAT 中仅提供给主管。

### 技术

- **有界静态核查**：八项正文与 59 项场景完成结构和本地引用检查；配套清单的 30 项一致性断言通过，78 个本地链接与锚点可定位。
- **契约复核**：完成独立契约审阅和纸面场景推演，补清研究协作资格及审阅缺证据的处理边界；上述结果不代表场景已全量运行或 MAT 接入通过。

### 文件变更表

| 文件／目录 | 变更 |
|:-----|:-----|
| README.md、docs/分层清单.md | 新方法导航、四种范围和五类型矩阵 |
| docs/安装与更新.md、docs/来源与许可.md | 必需资源、调用策略、来源和许可边界 |
| manifests/recommended.json | 研究入口替换，明确本仓库来源与上游来源 |
| manifests/for-mat.json | 新增完整 MAT 配套清单 |
| skills/research-mos/、skills/discernment-nudge-mos/ | 新增通用改写正文、元数据、许可、来源及场景 |
| skills/to-tickets-mat/、skills/implement-mat/、skills/review-mat/ | 新增 MAT 拆票、实施与统一审阅方法及配套 |
| skills/handoff-for-mat/、skills/hunt/ | 新增 MAT 交接与排错方法及配套 |
| skills/mat-changelog-writer/SKILL.md、skills/mat-changelog-writer/evals/evals.json | 对齐角色、跨仓串行及办理边界 |
| evals/activation.json | 直接调查请求改为选择 research-mos |
| CHANGELOG.md、CHANGELOG.txt | 同源记录本版本 |

### 已知问题

- 部分保留方法仍含旧研究入口、原生委派或显式依赖接缝，尚未全部完成 MAT 定向适配；完整清单不等于调用链已验证。

### 待完成

- 新场景的实际模型行为测试，以及目标 Harness 的发现、加载与替代入口验证。
- MAT 真实身份、业务工具、交接保存、读取权限和端到端执行验证。

### 刻意不做

- 不安装或覆盖个人 Skill，不修改上游缓存、历史版本条目及历史评测。
- 不扩充 own／all，不自动替换日常提醒方法，不替用户建立 UI 制作流程。
- 不实现 MAT 产品工具、权限平台或统一安装器。

---

## v0.10.2 (2026-11-01 15:54)

### 调整

- **专版 Skill 更名为 MAT**：`sat-changelog-writer` 更名为 `mat-changelog-writer`，目录、`SKILL.md` 的 `name` 字段与全部现行引用同步更新；用途、审阅契约和分发边界未变。
  - 目录由 `skills/sat-changelog-writer/` 迁移到 `skills/mat-changelog-writer/`，Git 以重命名记录，历史可追溯
  - 正文中的「SAT 提交员」「SAT 业务入口」「SAT 隔离环境」「SAT 真实身份」等术语统一改为 MAT
  - 场景库 `evals.json` 的 `skill_name` 与场景文本同步；入口选择场景 `activation.json` 中的 `sat-not-a-batch` 改为 `mat-not-a-batch`
- **已发布条目保持原文**：`CHANGELOG.md`、`CHANGELOG.txt` 的 v0.9.0、v0.10.0、v0.10.1 条目和 `evals/results/` 的历史评测记录仍写 SAT 与 `sat-changelog-writer`，按「不改写已发布条目」原则保留；本次条目即 SAT→MAT 迁移的追溯依据。

### 文档

- **现行文档术语同步**：README 的专版描述、调用表与安装边界，以及三份 docs 的专版归属说明统一改为 MAT。

### 技术

- **Windows 文件权限修复（环境侧，非仓库产物）**：本次操作中 `skills/` 与 `.git/` 无法创建条目，判断为 Windows 文件权限缺项；按 ACL 诊断流程修复并复测通过，权限备份与回滚脚本留在 `D:\Device\dsh-acl-recovery`，不进入版本控制。

### 文件变更表

| 文件 | 变更 |
|:-----|:-----|
| `README.md` | 专版描述、调用表、安装边界共 8 处改为 MAT |
| `docs/分层清单.md` | `own` 档说明与专版归属改为 MAT |
| `docs/安装与更新.md` | 专版分发边界改为 MAT |
| `docs/来源与许可.md` | 专版许可说明改为 MAT |
| `evals/activation.json` | 场景 id `sat-not-a-batch` → `mat-not-a-batch` |
| `skills/mat-changelog-writer/SKILL.md` | 由 `skills/sat-changelog-writer/` 重命名；`name`、标题与正文改为 MAT |
| `skills/mat-changelog-writer/references/changelog-format.md` | 默认格式标题改为 MAT |
| `skills/mat-changelog-writer/evals/evals.json` | `skill_name` 与场景文本改为 MAT |

### 已知问题
- 无

### 待完成
- 无

### 刻意不做
- 不改写已发布版本条目与历史评测记录，保留原始表述
- 不修改第三方上游缓存 `.skills/upstream/` 中出现的 SAT 字样

---

## v0.10.1 (2026-10-25 23:55)

### 修复

- **上游表与来源索引的恢复**：`manifests/` 与 `docs/` 在 v0.9.0 的仓库收拢中被整体删除，上游来源索引和三档说明因此不在版本控制里；本次按收拢前的最后版本恢复与上游表直接相关的 5 个文件。
  - `manifests/all-used.json`（53 个上游 Skill 来源索引与 4 条排除项）与 `manifests/recommended.json`（34 个推荐上游选择）与删除前逐字节一致，本次未做任何改动
  - `docs/分层清单.md`、`docs/安装与更新.md`、`docs/来源与许可.md` 恢复后再修正口径，见下三条
  - v0.9.0 实际删除 16 个文件，本次恢复 5 个，其余 11 个仍处于删除状态
- **上游表复核结论**：对照本地 `.skills/upstream/` 五个上游缓存逐条核对，表内 53 条没有失效项。
  - Matt Pocock 28/28、Anthropic 15/15、Waza 8/8、Huashu Design 1/1、Kill AI Slop 1/1 全部存在，未发现改名或下线
  - 五个缓存最后一次 fetch 为 2026-10-01，`HEAD` 与 `origin/main` 一致、0 commits 落后，因此下面「未选入」的 11 条在建表时已存在，属策展取舍而非上游新增
- **三档数量口径与 SAT 专版归属**：恢复的文档按 v0.6.0 快照写作，早于 v0.9.0 新增的 `sat-changelog-writer`，会让读者以为自有 Skill 只有十个通用入口。
  - 明确 `sat-changelog-writer` 是角色限定的 SAT 专版、不复制进个人全局目录，因此不计入三档
  - 数量保持 `own=10`、`recommended=44`、`all=63`，与 `manifests` 的「53 upstream + 10 owned」自洽
  - 「十个自有 Skill」一类表述改为「十个个人版 Skill」
- **过时引用与断链**：`docs/安装与更新.md` 仍在描述 v0.9.0 已删除的 `skills/_shared/references/` 共享契约目录和被删除的校验脚本，并链接到未恢复的 `技能选择.md`。
  - 改为「每个 `SKILL.md` 自带可独立运行的最小摘要，仓库不维护共享契约目录」，并删去校验脚本提法
  - 断链改指 `README.md` 的 Skill 选择表；三份恢复文档的相对链接现为 0 断链
- **漏记的上游来源**：`docs/来源与许可.md` 的上游项目表缺 `Huashu Design`，而 `manifests` 与分层清单都记录了它；补回该来源的覆盖方向、MIT 许可与安装边界。

### 新增

- **未选入上游 Skill 的事实记录**：`docs/分层清单.md` 的排除表只列 4 项，但本地缓存中另有 11 个上游 Skill 既未选入、也不在排除项内，读者无法从表里区分「未选入」与「失效」。
  - Matt Pocock Skills 7 个：`claude-handoff`、`setup-ts-deep-modules`、`to-questionnaire`、`wait-what`、`writing-for-agents`、`migrate-to-shoehorn`、`scaffold-exercises`
  - Anthropic Skills 4 个：`academy-guide`、`claude-api`、`internal-comms`、`slack-gif-creator`
  - 写明它们不是失效条目，选入其中任何一项都需要单独决定并同步 `manifests/` 与清单

### 文件变更

| 文件 | 变更 |
|:-----|:------|
| `manifests/all-used.json` | **恢复** — 与删除前逐字节一致，53 条上游索引与 4 条排除项 |
| `manifests/recommended.json` | **恢复** — 与删除前逐字节一致，34 条推荐上游选择 |
| `docs/分层清单.md` | **恢复并修正** — 补 SAT 专版归属与 11 条未选入记录，口径改为「个人版」 |
| `docs/安装与更新.md` | **恢复并修正** — 删除 `_shared` 与校验脚本的过时描述，修断链 |
| `docs/来源与许可.md` | **恢复并修正** — 补 Huashu Design 来源行，标注 SAT 专版分发边界 |

### 已知问题

- v0.9.0 的既有条目仍写着 `docs/`、`scripts/`、`manifests/`、`.github/`「不再随仓库分发」，与本版本恢复后的状态冲突；已发布条目按规则不改写，以本条目为准。
- `docs/` 目前只有 3 篇文档，恢复后仍缺 `技能选择.md`、`工作流协作.md`、`工作流设计哲学.md` 与 ADR，导航不完整。
- 仓库没有校验入口：`scripts/validate.ps1` 仍处于删除状态，本轮 JSON 与清单一致性靠临时检查完成，不能复跑。

### 待完成

- 11 个未选入的上游 Skill 的取舍决定；触发条件是作者要调整 `all` 档范围。
- 其余 11 个被删文件（`CONTEXT.md`、`CONTRIBUTING.md`、`.github/copilot-instructions.md`、`scripts/validate.ps1`、`skills/_shared/references/` 3 份、4 篇 docs 与 ADR）是否恢复；触发条件是决定为 `docs/` 重建导航。
- 仓库仍无自动回归 runner，`evals/` 场景库没有可执行入口。

### 刻意不做

- **不改写 v0.9.0 已发布条目**：已发布版本不得修改，用新条目记录恢复事实并保留历史。
- **不代替作者做选入决定**：11 条未选入的上游 Skill 只记事实与差异，不因复核就补进索引。
- **不为 SAT 专版虚构安装口径**：`sat-changelog-writer` 依赖 SAT 的真实身份、目录裁剪与业务授权，本次只标注「不计入三档」。
- **不整体改版文档**：只在恢复内容上修口径、断链与漏记项，不重写结构与章节。

---

## v0.10.0 (2026-10-22 22:43)

### 调整

- **触发与完成条件**：精修十个个人版 Skill 的正文，按明确任务意图选择入口，减少泛词误触发、重复确认、重复验证和不必要报告。
- **规格入口**：decision-to-spec 实际读取并执行上游 to-spec，负责上下文准备、本地文档适配和一致性复核；已有完整规格的小改动保留轻量同步路径，实质取舍进入 ADR。
- **证据与验收**：复用适用于当前改动的证据，区分必需检查与可选后续；文档审计遵循实际工具退出码和项目权威来源。
- **按需编排**：原型类型依据待验证问题选择，任务书交付不等待派发；无流程图时可直接分析正文，长模板改为按需参考。
- **批准复用**：更新日志流程复用仍有效的批准，只对实质变化重新确认；SAT 专版精简长句并保留主管审阅、身份与提交边界。
- **调用策略**：保留四个仅手动入口，明确配置声明与实际运行效果需要分别验证。

### 新增

- **隔离评测工具**：增加 workflow_eval.py，支持八类夹具的准备与文件、索引、提交范围检查；不自动调用模型，产物检查不等于行为通过。
- **评测资料**：场景库扩展至 66 个行为场景、261 条期望及 21 个入口选择案例，新增正文精修评测记录。
  - 已执行七项隔离任务、四项只读任务、20 条入口选择模拟及一个无 Skill 对照；to-spec 入口修正后另完成完整规格与轻量同步两项验证。
  - 无 Skill 对照也得到正确结果，不据此宣称 Skill 必然提升效果。

### 文件变更表

| 文件 | 变更 |
|:-----|:-----|
| README.md | 更新入口、调用边界、安装依赖与评测说明 |
| skills/*/SKILL.md | 精修十个个人版正文，小幅调整 SAT 专版 |
| skills/decision-to-spec/agents/openai.yaml | 更新规格入口简述 |
| skills/*/evals/evals.json | 补充行为边界与回归场景 |
| skills/repository-docs-bootstrap/references/*.md | 同步治理、ADR 与调用规则 |
| skills/skill-workflow-orchestrator/references/proposal-template.md | 新增按需方案模板 |
| skills/skill-workflow-visualizer/references/workflow-template.md | 新增按需工作流模板 |
| scripts/workflow_eval.py、scripts/.gitignore | 新增隔离评测工具与缓存忽略规则 |
| evals/activation.json | 新增入口选择案例 |
| evals/results/2026-10-22-正文精修评测.md | 记录执行结果、版本快照和未覆盖项 |
| CHANGELOG.md、CHANGELOG.txt | 记录 v0.10.0 |

### 已知问题

- 内置 quick_validate 的字段白名单不接受四个手动入口原有的 disable-model-invocation；保留调用策略，另行检查其余结构，不将临时副本验证视为运行兼容证明。
- 场景库尚未全量执行，当前结果不证明跨模型或长期收益。

### 待完成

- 补测上游缺失、新测试边界及实际运行环境中的发现与加载行为。
- SAT 定向加载、业务入口与隔离验证仍待后续授权。

### 刻意不做

- 不新增 Skill，不因正文相似删除各自必要的边界，不将工作流编排成强制流水线。
- 本机已另行安装十个个人版并核对 37 个文件；安装不属于 Git 产物，SAT 专版及其他 Agent 副本未同步。

---

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
