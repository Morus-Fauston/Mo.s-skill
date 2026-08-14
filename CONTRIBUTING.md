# Contributing

## 自有 Skill

每个自有 Skill 放在 `skills/<skill-name>/`，至少包含 `SKILL.md`。修改时保持触发条件、边界、人工确认点和最终产物清晰可核验。需要行为评测的 Skill 同步更新 `evals/evals.json`。

发布给普通使用者时，默认只安装使用版：`SKILL.md` 加运行时需要的引用文件、脚本或资源，不包含 `evals/`。维护、修改或评测 Skill 时才保留完整目录；当前使用版文件清单见 [docs/installation.md](docs/installation.md)。

提交前运行：

```powershell
./scripts/validate.ps1
```

不要加入机器绝对路径、个人库存、密钥、会话转录或特定业务项目资料。

## 上游 Skill

不要把第三方 Skill 正文复制到 `skills/`。修改 `manifests/recommended.json` 或 `manifests/all-used.json` 时，提供官方仓库 URL、精确 Skill 名称和许可证依据，并在 [docs/source-attribution.md](docs/source-attribution.md) 中说明它支持的 Agent 与官方安装路径。不得承诺某个自定义脚本能跨 Agent 自动安装。
