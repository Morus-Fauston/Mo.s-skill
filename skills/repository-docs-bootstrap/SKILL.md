---
name: repository-docs-bootstrap
description: "为一个仓库建立本地化的文档治理骨架：分类、主来源、入口文件和 Agent 工作流。只在你主动调用时运行；不负责后续审计、决策同步或实际调研。"
disable-model-invocation: true
---

# 仓库文档初始化

这个 Skill 负责在新仓库快速复现一套以 MTP 文档治理为默认范式的完整骨架，再把它变成目标仓库自己的文档入口、分类命名、唯一主来源关系和 Agent 协作规则。它复现的是文件角色和维护关系，不是把 MTP、MoMA 或其他私有项目的产品内容、研究前缀、历史文件和个人信息复制过去。

## 模式

默认使用 `full-governance`：补齐根目录关键文件、`Docs` 治理目录、`ADR`、`Research`、工作流、Agent 约定、验证/历史/迁移入口和 `.scratch` 工作台；已有文件只补强或接管，不覆盖。只有用户明确说“只盘点/只提案/只审计”时才使用 `plan-only` 或 `adopt-existing`。完整骨架和每个入口的最低内容见 [governance-baseline.md](references/governance-baseline.md)，可落盘的必选/按需文件清单见 [reproduction-manifest.md](references/reproduction-manifest.md)。

## 完成条件与上下文摘要

- 本 Skill 自包含：目标仓库通常没有本仓库其它目录，触发、边界、完成条件和最小交接摘要都在本文件与 `references/` 内。
- 已读取仓库指令、根 README、领域/术语材料、构建测试入口和现有文档目录；无法访问的材料已标明。
- 已明确初始化模式，并按基线清单记录每个文件是“已存在并保留”“已补强”“新建”“不适用”还是“等待负责人补充”。
- `full-governance` 已创建有实际入口内容的治理骨架，不留下只有目录名的空目录。
- 已根据仓库实际内容建立材料清单，并区分现行、提案、研究、执行证据、历史和私有材料。
- 已为每类现行信息指定唯一主要来源，其他文档只链接或摘要。
- 研究分类和命名来自仓库自己的稳定领域词汇；主题名、ADR 名和普通文件名使用中文，只有类别代号、编号、协议名、库名、产品名、API 名等专有名词保留原文。
- `AGENTS.md` 中的工作流只引用当前可发现、职责清楚的推荐 Skill，并保留人工确认、真实环境和权限边界。
- 索引、相对链接、状态字段和当前入口已经静态检查；未检查的范围没有被写成“通过”。
- 交付了变更清单、未决问题、证据边界和后续维护责任。

## 操作边界

- 默认先盘点再按 `full-governance` 创建骨架；用户明确要求初始化时，可以编辑或新建文档，但不修改业务代码、不部署、不提交或推送 Git。
- 保留用户已有未提交改动。不要删除、覆盖、批量重命名历史文档或移动私有材料；这类动作必须单独得到明确授权，并先建立旧新路径映射。
- 默认按 MTP 的 `Docs`、`AGENTS.md`、`CONTEXT.md`、Research 索引、ADR、工作流、验证反馈和 `.scratch` 期次票据骨架初始化；分类仍必须按目标仓库本地事实建立。
- 不把 MoMA 的 `ENG/CODE/ECO/ARC/UX`、MTP 的 `SYS/CODE/ECO/ARC/UX` 或任何外部模板当成目标仓库的固定分类。
- 不把英文主题、`report`、`task`、`research`、`decision` 等通用词混入中文文件名；类别代号是结构化标识，可以使用稳定短码，但必须在 Research 入口定义含义。
- 不把研究建议、聊天讨论、原型尝试或测试输出写成已确认的产品/架构决定；不确定时写“待确认/待调研”。
- 不创建没有 README/入口责任的空目录、占位研究报告、重复汇总报告或第二份权威规格。完整骨架中的暂未启用目录必须有 README，明确“当前未启用”和启用条件。
- 用户没有指定公开范围时，先检查 `.gitignore`、仓库规则和已有私有边界；不要擅自改变公开/私有状态。
- ES、LICO 等私有项目只可作为治理机制的来源标签；不得复制其正文、个人姓名、联系方式、账户、设备信息、密钥、私有业务数据或本机绝对路径。初始化报告只写抽象机制和目标仓库的公开事实。

## 工作流程

### 0. 选择初始化模式

- `full-governance`：新仓库或治理骨架缺失时使用，按基线清单创建文件和入口。
- `adopt-existing`：已有 Docs 体系时使用，保留目录和命名，补缺失的主来源、索引、工作流和状态规则。
- `plan-only`：用户只要方案或暂不授权写入时使用，只交付文件映射和差距清单。

用户只说“初始化/复现治理结构”时默认 `full-governance`；不因目录已有少量 Markdown 就自动降级为只读。

### 1. 建立事实基线

先读取 `AGENTS.md`（含父目录指令）、根 README、`CONTEXT.md`/术语表、构建与测试配置、现有文档入口、`.gitignore` 和 `git status`。按需查看源码目录、测试目录、部署配置和票据入口，以确认仓库的领域、运行环境、交付节奏和私有材料边界。记录文件路径、状态、编号、版本线索和可验证的维护责任，不把所有 Markdown 视为同一层级。

### 2. 形成仓库本地分类

先按“信息用途”和“生命周期”归类，再为仓库命名。通常需要判断是否存在：

- 稳定术语、领域对象和边界；
- 当前产品/平台决策、需求、设计或技术规格；
- 难逆转的架构取舍（ADR 或等价记录）；
- 一次性事实研究、任务书、报告、审阅和采纳状态；
- 持续执行的开发、验证、发布和交接工作流；
- 版本计划、票据、原始证据、待办、预案、设计资产；
- 历史、迁移、归档和本地私有材料。

研究分类必须从仓库自己的稳定边界推导。例如平台仓库可能需要 `SYS`，数据工具可能需要 `DATA`，领域引擎仓库可能需要 `ENG`；只有在目录中实际存在该研究对象、能写出反例边界并能由维护者持续编号时才建立类别。类别定义、编号范围、任务书/报告配对、中文主题规则和“交付/审阅/采纳”状态写入本仓库的 Research 入口，不写进通用模板。详细命名制度和完整示例见 [governance-baseline.md](references/governance-baseline.md)，初始化时必须把它转化成目标仓库自己的规则。

### 3. 先给出映射，再写入

在大范围创建或重排前，形成一张简短映射：

```markdown
| 信息类型 | 目标主来源 | 需要新建/补强 | 只需链接的现有材料 | 未决点 |
| --- | --- | --- | --- | --- |
| 稳定术语 | [文件] | [文件] | [文件] | [问题] |
```

已有入口明确且不冲突时，直接在其结构内补强。若现有分类、公开边界、权威来源或迁移范围无法判断，停在映射阶段报告问题，不擅自选择。用户已经明确“初始化并采用本地化方案”时，映射本身可作为写入前的内部检查，不必重复询问已授权事项。

### 4. 复现治理骨架并本地化

读取 [governance-baseline.md](references/governance-baseline.md) 和 [reproduction-manifest.md](references/reproduction-manifest.md)，先按 MTP 默认文件角色建立骨架，再根据事实决定目录名称、语言和是否启用。完整模式的目标是让新 Agent 有稳定入口，而不是让每个目录马上拥有业务正文。

根目录至少处理以下角色：`README.md`、`AGENTS.md`、`CONTEXT.md`、`.gitignore`、许可证文件和版本记录；已有双格式 `CHANGELOG.md`/`CHANGELOG.txt` 时保持一致，只有项目确实需要版本记录时才新建。许可证文本和组织身份不能由 Agent 猜测，缺失时建立待负责人补充项，不写伪造许可证。

治理目录按三条原则处理：

1. **根文件先补**：`AGENTS.md` 只放硬约束、开始工作前的阅读顺序、Skill 路由和人工关口；`CONTEXT.md` 只放稳定术语与模块边界，不放临时计划。
2. **治理目录按事实启用**：每个目录都要有 `README.md`，写清用途、主要来源、状态词、命名与编号规则、更新责任、不属于本目录的材料和启用条件；没有实际材料时写明空状态，不为它创建空目录。
3. **执行材料与正式文档分层**：`.scratch` 保存票据、证据和工作文件，不替代正式 Docs；票据契约见 [ticket-governance.md](references/ticket-governance.md)。

具体目录树、每个入口的最低内容和必选/按需文件清单见 [governance-baseline.md](references/governance-baseline.md) 与 [reproduction-manifest.md](references/reproduction-manifest.md)。

如果仓库有多个独立产品域或维护域，在 `Docs/` 或 `docs/` 下按领域建立 `README.md`、`规格/`、`ADR/`、`架构与设计/`、`问题与记录/`、`验收与发布/` 等子入口；根入口必须说明领域文档与全局决策、Research、票据的关系。

每个新增 README 至少说明：用途、主要来源、状态词、命名/编号规则、更新责任、不属于本目录的材料、当前空状态和下一步启用条件。

`AGENTS.md` 的 Skill 路由应按问题选择主入口。可复用的通用路线包括：方向未定用 `grilling`/`think`，关键事实用 `research-brief`/`research`，结论确认后用 `decision-to-spec`，实现用项目实际的 `tdd` 或等价流程，单改动用 `evidence-based-validation`，阶段/版本用 `phase-acceptance`，文档一致性用 `docs-integrity-audit`，合并/发布用 `check`/`code-review`，版本记录用 `changelog-writer`，Skill 治理用 `skill-creator`/`health`。先检查这些 Skill 是否可发现；不可用时写职责而不是虚构安装依赖。

`AGENTS.md` 应直接包含个人惯用的 Skill 工作流参考段落，见 [governance-baseline.md](references/governance-baseline.md#agentsmd-skill-工作流参考段落)。初始化新仓库时优先复制这套路由，再只补项目自己的测试、平台和人工验收规则；不要重新发明一套互相冲突的流程。

### 5. 检查并交付

检查当前入口和新增索引的相对链接、目录与文件名、编号配对、状态词、主来源关系、`.gitignore` 边界和 AGENTS 工作流引用。对历史路径与现行路径分开报告。若项目有文档完整性检查或仓库验证命令，运行最小相关检查；否则说明仅做了静态检查。

`full-governance` 还要写入一份初始化记录。这是本 Skill 的产物，不是可选报告：

- 优先放入目标仓库已有的迁移/记录入口。
- 该目录尚未启用时，在 `Docs/README.md` 中登记报告位置。
- 目标仓库连 `Docs/` 都还没有时，写到 `.scratch/reports/repository-docs-bootstrap/<YYYY-MM-DD>-<仓库名>.md`，不再询问路径。

记录只保留最小结构，不复制正文、私有项目内容或个人信息：

```markdown
# 仓库文档初始化报告
- 基线版本与生成日期：
- 仓库类型、领域、现有入口、私有边界：

## 本地分类与主来源
| 类别/材料 | 主来源 | 状态 | 依据 |

## 文件动作
| 文件 | 新建 / 补强 / 保留 / 不适用 | 原因 |

## 未启用目录与未决责任
- 启用条件 / 负责人待补项 / 静态检查未覆盖范围
```

## 按需参考

- 需要逐项检查和模板时，读取 [bootstrap-checklist.md](references/bootstrap-checklist.md)。
- 需要复现完整治理骨架、文件角色和各 README 最低内容时，读取 [governance-baseline.md](references/governance-baseline.md)。
- 需要把根文件、全局 Docs、产品域和 `.scratch` 组合成明确落盘清单时，读取 [reproduction-manifest.md](references/reproduction-manifest.md)。
- 需要建立或复现票据、期次、依赖、证据和状态管理时，读取 [ticket-governance.md](references/ticket-governance.md)。
- 文档系统已经存在、目标是查断链/状态漂移/重复权威来源时，转交 `docs-integrity-audit`。
- 已有体系且只需查断链、状态漂移和重复权威来源时，不要进入本 Skill 的 `full-governance`；`adopt-existing` 只用于补缺失的主来源、索引和入口，不做全面审计。
- 已确认的产品或架构结论需要落到正式文档时，转交 `decision-to-spec`。
- 需要实际查证事实或外包调查时，转交 `research-brief`/`research`；本 Skill 不把参考项目经验当作事实。
