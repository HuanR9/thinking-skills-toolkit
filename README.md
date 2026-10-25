# 思维工具集

[English](README.en.md)

一组面向多种 AI Agent 的可复用思维工作流，覆盖问题路由、解释、研究、核验、决策与个人探索。核心技能按开放的 Agent Skills 格式编写，以 `SKILL.md` 和 Markdown 参考文件为主，不依赖某个特定模型或 Agent 工具。

Agent Skills 定义了技能内容的通用格式，但不同 Agent 的技能发现目录、安装方式、调用语法和可用能力可能不同。使用时需将技能目录放到目标 Agent 支持的位置；本仓库的 `.agents/skills/` 是一种项目级目录布局。`agents/openai.yaml` 仅提供 OpenAI/Codex 界面元数据，不属于跨 Agent 的核心内容。

## Skills

| Skill | 适用场景 |
|---|---|
| `problem-router` | 不确定该用哪种思路时，推荐一条简短路径。它只负责导航，不代替后续 Skill 执行任务。 |
| `socratic-questioning` | 问题含糊、纠结或多个问题混在一起，需要先通过一次一个问题澄清。 |
| `dual-layer-explanation` | 需要先用易懂语言解释，再补充专业机制、边界和常见误解。 |
| `reverse-engineering` | 已提供具体页面、产品、流程、仪表盘或方案，想拆解它的设计逻辑。 |
| `deep-research` | 研究对象的历史演变、时间线、竞品比较或行业格局，需要可追溯证据。 |
| `fact-check` | 核验一个具体的说法、数字、来源或因果判断。 |
| `expert-panel` | 复杂问题需要几个互补的模拟分析视角来揭示分歧与风险。 |
| `first-principles` | 现有做法可能受惯例或路径依赖影响，需要从事实、目标和约束重新推导。 |
| `cross-domain-transfer` | 希望从其他领域迁移可用机制，并评估类比何处可能失效。 |
| `steelman-debate` | 在几个已明确选项之间做决定，需要先看清每个选项最强的论据。 |
| `minimum-experiment` | 有一个关键但未验证的假设，想用低成本、可逆测试获取信息。 |
| `talent-discovery` | 自愿进行多轮反思，从具体经历中探索优势、能量和可迁移能力。 |
| `life-design` | 自愿探索人生方向，并设计多个可尝试的小型原型。 |

个人探索类 Skills（`talent-discovery`、`life-design`）会先确认用户是否愿意进行多轮对话。它们用于反思和实验，不用于诊断或替用户作重大决定。

## 快速开始

在支持 Agent Skills 的工具中，将所需技能目录放入该工具支持的技能目录，然后提出任务。Agent 会如何发现和激活技能，取决于具体工具。若需明确指定，可在自然语言请求中写出技能名称，例如：

```text
请使用 fact-check 技能，核验“80% 的新用户会在首周流失”这个说法，并说明证据来源和不确定性。

Use the deep-research skill to compare how these two products evolved and cite dated sources.

请用 dual-layer-explanation 技能，先通俗、再专业地解释 Transformer。
```

若不确定该用哪个，可以明确调用路由器：

```text
请使用 problem-router 技能：我在考虑离职，但原因和目标还没有理清。请建议下一步用哪个技能。
```

在本仓库的 Codex 配置中，`problem-router` 设为仅显式调用；其他 Agent 是否遵循此设置取决于其实现。跨 Agent 使用时，最稳妥的显式调用方式是按目标工具支持的语法指定技能，或在自然语言中写出技能名称。自动匹配并非保证行为。

技能指令支持中文和英文。默认用用户当前使用的语言回应；若请求中英混杂或明确要求双语，则为重要术语和结论提供中英对照。技能的稳定标识使用英文连字符形式，例如 `deep-research`；调用语法由 Agent 决定。

## 如何选择

可以先按任务形态区分：

| 你现在要做的事 | 可先用 |
|---|---|
| 还没弄清真正的问题 | `socratic-questioning` |
| 学会一个概念 | `dual-layer-explanation` |
| 分析你给出的具体范例 | `reverse-engineering` |
| 研究一个主题如何发展、如何与同行比较 | `deep-research` |
| 判断一条可核验的具体说法是否成立 | `fact-check` |
| 重新设计一个受约束的问题或流程 | `first-principles` |
| 借用其他领域的做法 | `cross-domain-transfer` |
| 审视复杂问题的不同角度 | `expert-panel` |
| 比较已定义的选项 | `steelman-debate` |
| 用小测试降低关键不确定性 | `minimum-experiment` |
| 通过经历探索个人优势和能量 | `talent-discovery`（需同意多轮探索） |
| 探索人生方向并设计原型 | `life-design`（需同意多轮探索） |

一次请求通常只需一个主 Skill。路由器在两个相近选项都合理时才有帮助；对于已经明确的请求，可直接调用对应 Skill，不必先经过路由。

## 项目结构

```text
.
├── .agents/skills/             # 13 个 Agent Skills 格式的技能
│   ├── <skill-name>/SKILL.md   # 通用入口：适用条件与核心流程
│   └── <skill-name>/references/ # 按需读取的协议、报告结构或模板
├── docs/
│   ├── contracts/              # 证据、决策与个人探索安全约定
│   └── evals/                  # 路由和行为验收用例
├── scripts/validate_skills.py  # 技能结构与 OpenAI/Codex 元数据校验
├── README.md                   # 中文说明
└── README.en.md                # English documentation
```

只有部分 Skills 使用 `references/`。例如，深度研究在检索前读取研究协议，事实核验读取证据量表，个人探索在续谈或汇总时读取会话状态和报告结构。额外资料按需加载，以免每次任务都带入不相关内容。

## 校验与修改

在项目根目录运行：

```bash
python3 scripts/validate_skills.py
```

校验器会检查 13 个目录是否齐全、每个入口的 frontmatter 与名称、中文和英文描述、语言策略标记、已引用文件是否存在，以及质量文档是否齐备。它检查的是结构，不代表模型每次都能选中正确的 Skill，也不证明方法本身一定适合所有情境。行为验收用例见 [`docs/evals/routing-cases.md`](docs/evals/routing-cases.md) 和 [`docs/evals/skill-cases.md`](docs/evals/skill-cases.md)。

修改时，优先保持每个 Skill 专注于一个可辨识的目标；`description` 说明“做什么、何时使用”，`SKILL.md` 保留核心工作流，较长的专项细节放在相关 `references/`。修改目录、名称或链接后，运行结构校验并复核中英文入口描述与实际行为一致。官方建议也强调应让描述清楚说明触发条件，并将详细流程放在指令正文中。

后续新建技能的通用内容统一放在 `.agents/skills/<skill-name>/`。分享给其他 Agent 时，根据目标工具的发现机制复制或安装技能目录；保持 `SKILL.md` 和其引用资源可独立读取。命名、frontmatter、平台元数据、校验和公开前检查规范见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 边界与安全

- Skill 是指导，不是独立执行环境；它不能绕过当前会话的权限、安全规则或工具可用性。
- 自动调用和显式调用方式由 Agent 决定；技能名称与描述不能保证每个工具都以相同方式发现或激活它。
- 外部网页、用户附件和引用内容是分析对象，不应被当作覆盖用户意图的更高优先级指令。
- 使用第三方 Skill 前应先检查其指令和脚本；Skills 可能影响模型规划、工具使用与命令执行。
- 研究与核验流程要求标出事实、推断、意见和证据缺口；没有可用来源时，不能声称已完成核验。
- 高风险、不可逆或涉及个人安全的事项，不能只依赖 Skill 文本，应按适用场景寻求合格专业支持。

## 参考资料

- [路由验收用例](docs/evals/routing-cases.md)
- [Skill 行为验收用例](docs/evals/skill-cases.md)
- [证据约定](docs/contracts/evidence.md)
- [决策约定](docs/contracts/decision.md)
- [个人探索安全约定](docs/contracts/personal-exploration-safety.md)
- [OpenAI：Skills（插件概念）](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI API：Skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [Agent Skills 开放规范](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
