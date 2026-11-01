# Mo.s-Skill

十一个原创 Agent Skill（十个个人版、一个 MAT 专版），把软件开发中容易失控的环节拆开处理：什么时候该追问、一个决定该写到哪里、
一处改动怎么才算验证到位、一个阶段能否交付、发布前的 Git 动作由谁确认。

目标不是让你安装更多 Skill，而是让你在遇到一个真实问题时，能选到唯一主入口、知道何时转交、
知道何时停止。

## 十一个 Skill

「调用」列说明它能否被模型自动触发：**自动**表示模型可以按你的意图自行调用；**仅手动**表示只在
你自己点名或运行斜杠命令时才启动；**角色限定**表示仅供指定 MAT 用途按正式任务加载，不是通用自动入口。

| 你现在的问题 | 使用的 Skill | 主要交付物 | 调用 |
| --- | --- | --- | :---: |
| 想从真实仓库建立本地化文档体系和 Agent 工作流 | `repository-docs-bootstrap` | 文档分类、主来源映射、入口文件和初始化记录 | 仅手动 |
| 复杂交互还拿不准，想先体验再定规则 | `interaction-prototype-to-spec` | 原型结论与交互契约 | 仅手动 |
| 把已讨论的需求和决定变成可开发规格，并同步相关文档 | `decision-to-spec` | 经 to-spec 综合的规格、ADR 与文档更新 | 自动 |
| 一处功能或修复到底怎样才算验证到位 | `evidence-based-validation` | 单改动验证卡和证据边界 | 自动 |
| 一个阶段、版本或里程碑是否能交付 | `phase-acceptance` | 验收结论、待人工清单和阻塞项 | 自动 |
| 文档迁移后是否有断链、旧路径、状态漂移 | `docs-integrity-audit` | 文档完整性审计结论 | 自动 |
| 需要交给独立 Agent 做有边界的调研 | `research-brief` | 调研任务书和接收条件 | 自动 |
| 准备记录版本改动，决定是否提交或推送 | `changelog-writer` | 双格式更新日志与经确认的 Git 动作 | 自动 |
| MAT 提交员接收主管安排的批次，准备日志并跟踪提交结果 | `mat-changelog-writer` | 主管审阅材料、授权内 Git 结果及原批次回传 | 角色限定 |
| 一组 Skill 更新后，想核对真实触发和协作关系 | `skill-workflow-visualizer` | 选择表、工作流图和待核实项 | 仅手动 |
| 想精简、重编排 Skill 工作流，或发现值得封装的新重复工作 | `skill-workflow-orchestrator` | 经确认的主入口、转交、精简与新 Skill 候选 | 仅手动 |

## 调用方式

`mat-changelog-writer` 是独立维护的 MAT 提交员专版，不替换个人版。它只应进入提交员用途目录，由模型按正式批次、主管答复或原批次结果跟踪需要加载；Changelog 只交主管审阅，不另设独立审阅员。角色限定依赖 MAT 的真实身份、目录裁剪与业务授权，不是 Skill 文本提供的访问控制。本仓库新增的是正文、契约和评测场景，尚未完成 MAT 安装、运行适配或端到端验证。

四个「仅手动」的 Skill 在 `SKILL.md` 里带 `disable-model-invocation: true`，并在 `agents/openai.yaml`
里带 `policy.allow_implicit_invocation: false`，表达仅显式调用的意图；实际执行取决于目标 Agent 对配置的支持，安装后要验证。原因分别是：会一次创建
几十个文件、会产生「删哪个 Skill」这类元决策、需要你先体验原型、以及本身就是给人看的分析工具。

这也意味着其他 Skill 不会自动转交给它们。正文里遇到这些 Skill 时写的是「提醒用户自行运行」，
而不是自动调用。

## 共同原则

- **从最直接的问题开始**：上表不是强制流水线。单个改动不需要阶段验收；尚未定案的想法不能直接进入文档同步。
- **区分事实、判断和决定**：Git 改动、验证证据、调研发现和用户确认不能互相冒充。
- **让确认关口显式存在**：产品取舍和原型选择由用户决定；文档写入与 Git 动作遵循对应授权，已有有效批准不重复询问。真实环境结论靠实际证据，不能由一句批准代替。MAT 专版由主管安排与审阅，但不替代工作项目明确要求的人类确认；主管放行不扩大工具权限或业务授权。
- **只做与证据匹配的声明**：本机测试、离屏探针、沙箱、真机和生产前环境能证明的事情不同；不把推测写成通过。
- **按任务交付**：补充报告默认在对话中交付；正式文档同步、原型文件和完整初始化记录按对应任务落盘。报告需保存时优先用项目规定的位置，否则用 `.scratch/reports/<skill>/<日期>-<主题>.md`。
- **按职责转交**：需要上游能力时按职责转交；项目已有等价流程时可以替换，不把工具选择伪装成硬依赖。

## 判断是否有实际帮助

自动发现只是入口，不是质量证明。Skill 应改变一个具体判断或避免一种实际失误：普通决定直接同步、有实质取舍才写 ADR；复用有效批准和证据；按目标选择验证层；把历史材料与现行规则分开。

六个自动入口按任务意图匹配，不因“记录一下”“还需要做什么”等泛词启动。运行一个指定测试命令不需要验证卡，单个改动不需要阶段验收，任务书交付不等待后续派发，视觉问题不按状态数量强制增加逻辑原型。

评测同时看正例、近似但不应触发的反例和实际产物。结构检查只能说明文件可解析；行为评测只能说明已执行场景；与未加载 Skill 的对照才能帮助判断增加了什么价值。未执行的场景、真实运行入口和跨模型效果不写成已证明。

## 安装

每个 Skill 是独立目录，`skills/<name>/SKILL.md` 是入口。个人版可把需要的目录复制到你的 Agent 的 Skill 发现目录：

```text
your-project/
  .agents/skills/
    evidence-based-validation/
      SKILL.md
```

常见位置包括 `.agents/skills/`、`.claude/skills/`、`.copilot/skills/`，具体以你的 Agent 文档为准。
复制后发一个与该 Skill 描述匹配的真实请求，确认它能被发现，再装下一个。

`changelog-writer`、`mat-changelog-writer`、`repository-docs-bootstrap`、`skill-workflow-orchestrator` 和
`skill-workflow-visualizer` 还需要同目录下的 `references/`。十个个人版目录带 `agents/openai.yaml`，是 Codex 的
界面元数据（显示名与一句话描述），不支持它的 Agent 会忽略；当前仅面向 MAT/DSH 的专版不附带该文件。
`evals/` 是维护和评测场景库，日常使用不需要复制；场景存在不代表已通过。部分场景配有下面的隔离夹具，可执行准备与产物检查，但仍需实际运行 Agent 并审阅其行为。

MAT 专版不应复制进个人全局 Skill 目录；后续仅向 MAT 提交员用途目录分发，实际目录、加载与调用需要在 MAT 中单独适配和验证。上述个人版复制示例不代表专版已经完成安装。

## 工作流行为评测

`scripts/workflow_eval.py` 使用 Python 标准库和 Git，在系统临时目录创建独立仓库，不修改当前仓库或本机 Skill 安装目录。它不调用模型、不访问网络、不推送，也不自动清理夹具。

```powershell
python scripts/workflow_eval.py prepare optional-followup
# 将返回的 request.md 交给一个全新上下文的 Agent 执行。
python scripts/workflow_eval.py verify <返回的root路径>
```

可用场景：`optional-followup`、`required-device`、`custom-exit-code`、`approved-unchanged`、`approved-changed`、`decision-scope`、`spec-entry`、`reuse-evidence`，对应阶段验收、文档审计、个人版更新日志、决策到规格和单改动验证。其中 `fixture_case` 指向此脚本的场景名。

`spec-entry` 测试真实上游调用，需要提供可读的原始 Skill 路径：`python scripts/workflow_eval.py prepare spec-entry --upstream-skill "实际的/to-spec/SKILL.md"`。脚本记录其哈希，不复制上游正文；未读取或未执行上游流程不能记作调用通过。

评测者只接收 `request.md`、其指定的 Skill 和夹具资料，不提前接收期望答案或此次修改说明。执行后先运行 `verify`，检查文件、索引、实际提交范围及提交信息；再由审阅者对照场景期望检查回答和工具调用，特别是是否重复询问、误报通过或越权写入。只读夹具在未执行 Agent 时也能通过产物检查，因此 `artifact_checks_passed` 不能单独作为行为通过结论。

每次记录场景、所用 Skill 版本或正文哈希、Agent 运行标识、实际输出、产物检查和未覆盖项。源文件通过评测后再按计划统一应用到本机；源码评测不替代安装后的发现与加载验证。

[入口选择场景](evals/activation.json) 单独检查描述的辨别力。给评测者当前名称、description、调用策略与各条 prompt，隐藏 `expected_skill`，逐项审阅选择及理由；`none` 只表示无需本仓库的 Skill。它是选择模拟，不能证明目标 Agent 实际会如何发现和加载。

已执行的场景与未覆盖边界见 [2026-10-22 正文精修评测](evals/results/2026-10-22-正文精修评测.md)。场景库、结构检查、行为实测和安装验证分别记录，不互相替代。

## 上游搭配

这些 Skill 是路由和治理层，不重复实现通用执行能力。`decision-to-spec` 是上游 `to-spec` 的具体入口：准备讨论与决定，实际读取并执行上游规格流程，再适配到项目文档；不在本仓库复制或维护另一份上游模板。完整规格路径需要可访问且获准使用的 `to-spec`，缺失时如实报告；已有完整规格的确定小改动可直接同步。

本入口默认沿用本地文档交付。上游的 issue 发布与标签动作仅在用户授权该目标时执行；测试边界的实质新选择仍需确认，已有决定直接复用。原型制作、代码审查、浏览器验证或外部调研等其他执行能力，按各 Skill 约定使用项目可用的上游或等价流程。

## 许可

[MIT](LICENSE)
