# 来源、许可与上游精选

## Mo.s-Skill 自有内容

`skills/` 中的八个目录由本仓库维护，并以 [MIT License](../LICENSE) 发布。它们可独立复制，不依赖本仓库的安装脚本或某个专用插件系统；部分场景推荐转交给上游 Skill，推荐搭配见 [curated-tiers.md](curated-tiers.md)。

## 上游内容不在本仓库分发

本仓库不复制或重新发布第三方 Skill 正文。`manifests/` 是维护者使用的来源索引，记录曾被选入工作流参考的上游项目和 Skill 名称。它不等于锁定依赖、不保证所有名称仍存在，也不表示任何 Agent 都可以用同一条命令安装。

| 上游项目 | 为什么被记录 | 获取与许可原则 |
| --- | --- | --- |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | 工程规划、调研、测试、审查、界面和交接等通用工作流；其中 `grill-with-docs` 与 `research` 是 Mo 工作流的默认推荐搭档 | 使用其官方插件或 `skills.sh` 路径；以其仓库的许可证和发布说明为准。 |
| [Anthropic Skills](https://github.com/anthropics/skills) | 文档、表格、演示文稿、设计和技术示例 | Claude Code 可使用其官方市场；注意其中内容的许可并不完全相同，尤其文档类内容可能是 source-available。 |
| [Agentic Plugin Marketplace](https://github.com/wshobson/agents) | 面向 Claude Code、Codex、Cursor、OpenCode、Gemini CLI 与 Copilot 的原生适配参考 | 使用其对应 Agent 的官方市场或生成流程；以它的多 harness 文档为准。 |
| [PPT Master](https://github.com/hugohe3/ppt-master) | 原生可编辑 PowerPoint 的专门工作流 | 使用其仓库或 Claude Code 市场中的官方安装步骤；Python 依赖和功能边界以其文档为准。 |

## 维护上游索引

新增或修改 `manifests/` 条目之前，应完成以下核对：

1. 官方仓库或维护者发布页真实存在，且链接指向正确项目。
2. Skill 名称与上游当前目录或插件元数据一致。
3. 记录该来源的许可证，以及内容是否允许再分发。
4. 记录实际支持的 Agent 和官方安装路径，不把某一个工具的命令写成通用命令。
5. 不复制第三方 Skill 正文、运行时依赖、示例资产或密钥配置。

上游项目会改名、拆分、改变安装入口或删除 Skill。因此使用者应始终以官方说明为准；维护者需要定期复核来源索引，而不是把它当作长期稳定的包管理器。
