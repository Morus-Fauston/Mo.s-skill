# Contributing

## 自有 Skill

每个自有 Skill 放在 `skills/<skill-name>/`，至少包含 `SKILL.md`。它们是本仓库“理解并编排已有 Skill”方法的示范实现与关键能力。修改时保持触发条件、边界、人工确认点和最终产物清晰可核验；不得为了增加自动化程度而抹去事实、判断和用户决定之间的边界。新增或保留 Skill 前，说明它解决的直接问题、主入口关系和为何不与已有 Skill 重复；新建 Skill 候选应先由 `skill-workflow-orchestrator` 形成经确认的候选契约，再转交 `skill-creator` 设计、评测和迭代。需要行为评测的 Skill 同步更新 `evals/evals.json`。

发布给普通使用者时，默认只安装使用版：`SKILL.md` 加运行时需要的引用文件、脚本或资源，不包含 `evals/`。维护、修改或评测 Skill 时才保留完整目录；当前使用版文件清单见 [docs/installation.md](docs/installation.md)。

提交前运行：

```powershell
./scripts/validate.ps1
```

不要加入机器绝对路径、个人库存、密钥、会话转录或特定业务项目资料。

## 上游 Skill

不要把第三方 Skill 正文复制到 `skills/`。上游清单是职责参考和兼容性信息，不应削弱或取代原创 Skill 与工作流设计哲学。修改 `manifests/recommended.json` 或 `manifests/all-used.json` 时，先证明该项补齐明确需求、没有被当前主入口覆盖，或说明它为何仅保留为按需参考；再提供官方仓库 URL、精确 Skill 名称和许可证依据，并在 [docs/source-attribution.md](docs/source-attribution.md) 中说明它支持的 Agent 与官方安装路径。不得承诺某个自定义脚本能跨 Agent 自动安装。
