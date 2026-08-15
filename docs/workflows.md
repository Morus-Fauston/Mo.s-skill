# Skill 协作与人工关口

本页描述的是基于当前九个 `SKILL.md` 的协作边界。它不要求 Agent 自动串联所有步骤，而是说明一个工作流完成后，下一步何时应由用户选择，何时只是一条建议。

## 总览

```mermaid
flowchart TD
    Start[用户描述当前问题] --> Choose{最直接的目标}
    Choose -->|阶段或版本是否交付| Acceptance[phase-acceptance]
    Choose -->|一个改动如何证明| Validation[evidence-based-validation]
    Choose -->|已确认决定需要写入文档| Spec[decision-to-spec]
    Choose -->|迁移、索引或状态一致性| Audit[docs-integrity-audit]
    Choose -->|交互尚未定案| Prototype[interaction-prototype-to-spec]
    Choose -->|需要外包调研| Brief[research-brief]
    Choose -->|准备记录版本| Changelog[changelog-writer]
    Choose -->|Skill 关系需要核对| Visualizer[skill-workflow-visualizer]
    Choose -->|想重编排或精简 Skill 系统| Orchestrator[skill-workflow-orchestrator]

    Prototype -->|用户确认交互规则| Spec
    Brief -->|用户自行派发并决定是否采纳结论| Spec
    Audit -->|发现已确认决定没有落点| Spec
    Validation -->|多个承诺需要统一验收| Acceptance
    Acceptance -->|准备记录已验收变更| Changelog
    Visualizer -->|事实基线| Orchestrator
    Orchestrator -->|确认创建或改造 Skill| Creator[skill-creator]
```

箭头表示可能的后续选择，不代表自动调用。任何需要新的项目决定、外部授权或 Git 操作的箭头都应停在用户确认处。

## 决定同步

```mermaid
flowchart TD
    A[已确认的讨论] --> B[区分已确认、未决和待调研事项]
    B --> C{是否存在可列举的已确认决定}
    C -->|否| D[停止或转文档审计]
    C -->|是| E[决定映射到主要来源与派生文档]
    E --> F{权威来源或结论是否不明确}
    F -->|是| G[等待用户确认]
    G --> E
    F -->|否| H[更新文档并检查术语、状态和链接]
    H --> I[文档同步报告]
```

`decision-to-spec` 的关键约束是只同步已经确认的决定。它不是用来逼用户马上作出决定，也不会把调研报告自动变成规格。

## 单改动验证与阶段验收

```mermaid
flowchart LR
    A[一个具体改动] --> B[evidence-based-validation]
    B --> C[验证卡：已执行证据、待人工、阻塞]
    C --> D{多个承诺组成阶段或版本}
    D -->|是| E[phase-acceptance]
    D -->|否| F[结束]
    E --> G[验收报告：通过、部分通过、不通过或阻塞]
```

两者不应混用。前者回答“这一处被证明了吗”，后者回答“这次交付承诺是否兑现”。真实浏览器、设备、权限和预发布环境无法由 Agent 直接验证时，报告必须保留待人工步骤和预期证据。

## 发布记录与 Git 确认

```mermaid
flowchart TD
    A[用户要求记录版本] --> B[读取版本基线、Git 历史、差异和工作区]
    B --> C[起草版本建议和更新日志，不写入]
    C --> D[展示拟写入内容和拟暂存范围]
    D --> E[等待用户一次确认]
    E --> F{确认的动作}
    F -->|只写日志| G[写入更新日志]
    F -->|提交| H[仅暂存确认路径并提交]
    F -->|提交并推送| I[提交后推送]
```

`changelog-writer` 不会因为发现改动就自行提交。确认必须覆盖版本号、日志内容、Git 动作和暂存范围。

## 原型与调研的边界

| 场景 | 正确入口 | 人工关口 | 不应发生的事 |
| --- | --- | --- | --- |
| 复杂交互需要先体验 | `interaction-prototype-to-spec` | 用户确认入口、状态、数据和权限取舍 | 把原型当作生产实现或正式规格 |
| 需要把重要问题交给独立 Agent 研究 | `research-brief` | 用户确认范围、版本和证据标准；之后自行决定是否派发和采纳 | 自动派发、自动采纳研究建议 |
| 文档迁移后链接和状态可能出错 | `docs-integrity-audit` | 用户确认已证实机械修复的范围 | 擅自改写业务决策或删除历史资料 |

## 维护工作流说明

当本仓库中的某个 Skill 修改时，`skill-workflow-visualizer` 可从现行 `SKILL.md` 重新提取事实，再检查本页和 [skill-selection.md](skill-selection.md) 是否过期。流程图的依据应始终是实际 Skill 正文，而不是 Skill 名称、旧图或使用习惯。