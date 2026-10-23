# 思维 Skills 工具集 / Thinking Skills Toolkit

一组面向 Codex 的可复用思维工作流，包含问题路由、解释、研究、核验、决策和个人探索。适合直接使用，也可按项目需要修改。  
A collection of reusable thinking workflows for Codex, covering routing, explanation, research, verification, decisions, and personal exploration. Use them as-is or adapt them to your needs.

> 中文用户可从[中文版](#中文版)开始；English readers can jump to the [English version](#english-version).

---

## 中文版

### Skills 是什么

Skill 是一个包含 `SKILL.md` 的目录。它将某类任务的适用场景、操作步骤、边界和交付要求整理为可复用的工作流；需要时还可以附带 `references/` 参考文件、`scripts/` 脚本或模板资源。

在 Codex 中，Skill 不会给模型增加新的工具或权限。它提供的是“何时使用某种方法、如何完成、结果应达到什么标准”的指导；实际能访问哪些文件或工具，仍由当前 Codex 环境决定。官方文档说明，模型会先看到 Skill 的名称和描述，在请求匹配或用户明确调用时再读取完整指令。因此，自动选择是模型判断，不是每次都能保证触发。参见 [OpenAI：Skills](https://developers.openai.com/plugins/concepts/skills) 与 [OpenAI API：Skills](https://developers.openai.com/api/docs/guides/tools-skills)。

### 这套工具包含什么

| Skill | 适用场景 |
|---|---|
| `$problem-router` | 不确定该用哪种思路时，推荐一条简短路径。它只负责导航，不代替后续 Skill 执行任务。 |
| `$socratic-questioning` | 问题含糊、纠结或多个问题混在一起，需要先通过一次一个问题澄清。 |
| `$dual-layer-explanation` | 需要先用易懂语言解释，再补充专业机制、边界和常见误解。 |
| `$reverse-engineering` | 已提供具体页面、产品、流程、仪表盘或方案，想拆解它的设计逻辑。 |
| `$deep-research` | 研究对象的历史演变、时间线、竞品比较或行业格局，需要可追溯证据。 |
| `$fact-check` | 核验一个具体的说法、数字、来源或因果判断。 |
| `$expert-panel` | 复杂问题需要几个互补的模拟分析视角来揭示分歧与风险。 |
| `$first-principles` | 现有做法可能受惯例或路径依赖影响，需要从事实、目标和约束重新推导。 |
| `$cross-domain-transfer` | 希望从其他领域迁移可用机制，并评估类比何处可能失效。 |
| `$steelman-debate` | 在几个已明确选项之间做决定，需要先看清每个选项最强的论据。 |
| `$minimum-experiment` | 有一个关键但未验证的假设，想用低成本、可逆测试获取信息。 |
| `$talent-discovery` | 自愿进行多轮反思，从具体经历中探索优势、能量和可迁移能力。 |
| `$life-design` | 自愿探索人生方向，并设计多个可尝试的小型原型。 |

个人探索类 Skills（`talent-discovery`、`life-design`）会先确认用户是否愿意进行多轮对话。它们用于反思和实验，不用于诊断或替用户作重大决定。

### 如何使用

在 Codex 中打开本项目后，可以直接提出任务；对较明确的任务，也可以在请求中显式指定 Skill。常见写法：

```text
$fact-check 核验“80% 的新用户会在首周流失”这个说法，说明证据来源和不确定性。

Use $deep-research to compare how these two products evolved and cite dated sources.

请用 $dual-layer-explanation 先通俗、再专业地解释 Transformer。
```

若不确定该用哪个，可以明确调用路由器：

```text
$problem-router 我在考虑离职，但原因和目标还没有理清。请建议下一步用哪个 Skill。
```

`problem-router` 配置为显式调用，因此应输入 `$problem-router` 或清楚地说“使用 problem-router”；它不会作为隐式自动匹配的 Skill 启用。其他 12 个 Skills 可根据双语名称描述自动匹配，也可像上面一样显式调用。若自动匹配没发生，直接写出 `$skill-name` 即可。

Skills 的指令支持中文和英文。默认用用户当前使用的语言回应；若请求中英混杂或明确要求双语，则为重要术语和结论提供中英对照。Skill 的规范调用名保留英文连字符形式，例如 `$deep-research`。

### 如何选择

可以先按任务形态区分：

| 你现在要做的事 | 可先用 |
|---|---|
| 还没弄清真正的问题 | `$socratic-questioning` |
| 学会一个概念 | `$dual-layer-explanation` |
| 分析你给出的具体范例 | `$reverse-engineering` |
| 研究一个主题如何发展、如何与同行比较 | `$deep-research` |
| 判断一条可核验的具体说法是否成立 | `$fact-check` |
| 重新设计一个受约束的问题或流程 | `$first-principles` |
| 借用其他领域的做法 | `$cross-domain-transfer` |
| 审视复杂问题的不同角度 | `$expert-panel` |
| 比较已定义的选项 | `$steelman-debate` |
| 用小测试降低关键不确定性 | `$minimum-experiment` |
| 通过经历探索个人优势和能量 | `$talent-discovery`（需同意多轮探索） |
| 探索人生方向并设计原型 | `$life-design`（需同意多轮探索） |

一次请求通常只需一个主 Skill。路由器在两个相近选项都合理时才有帮助；对于已经明确的请求，可直接调用对应 Skill，不必先经过路由。

### 项目结构

```text
.
├── .agents/skills/             # 13 个 Codex Skills
│   ├── <skill-name>/SKILL.md   # 必需入口：适用条件与核心流程
│   └── <skill-name>/references/ # 按需读取的协议、报告结构或模板
├── docs/
│   ├── contracts/              # 证据、决策与个人探索安全约定
│   └── evals/                  # 路由和行为验收用例
├── scripts/validate_skills.py  # 结构与双语入口校验
└── README.md
```

只有部分 Skills 使用 `references/`。例如，深度研究在检索前读取研究协议，事实核验读取证据量表，个人探索在续谈或汇总时读取会话状态和报告结构。额外资料按需加载，以免每次任务都带入不相关内容。

### 校验与修改

在项目根目录运行：

```bash
python3 scripts/validate_skills.py
```

校验器会检查 13 个目录是否齐全、每个入口的 frontmatter 与名称、中文和英文描述、语言策略标记、已引用文件是否存在，以及质量文档是否齐备。它检查的是结构，不代表模型每次都能选中正确的 Skill，也不证明方法本身一定适合所有情境。行为验收用例见 [`docs/evals/routing-cases.md`](docs/evals/routing-cases.md) 和 [`docs/evals/skill-cases.md`](docs/evals/skill-cases.md)。

修改时，优先保持每个 Skill 专注于一个可辨识的目标；`description` 说明“做什么、何时使用”，`SKILL.md` 保留核心工作流，较长的专项细节放在相关 `references/`。修改目录、名称或链接后，运行结构校验并复核中英文入口描述与实际行为一致。官方建议也强调应让描述清楚说明触发条件，并将详细流程放在指令正文中。

后续新建 Skills 统一放在 `.agents/skills/<skill-name>/`，命名、frontmatter、UI 元数据、校验和公开前检查规范见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。建议未来 GitHub 仓库使用名称 `thinking-skills-toolkit`；当前文件夹仍为 `MySkills`，仓库尚未配置 GitHub remote。

### 边界与安全

- Skill 是指导，不是独立执行环境；它不能绕过当前会话的权限、安全规则或工具可用性。
- 自动调用是依据名称和描述进行的模型选择。需要明确时，在请求里指定 `$skill-name`。
- 外部网页、用户附件和引用内容是分析对象，不应被当作覆盖用户意图的更高优先级指令。
- 使用第三方 Skill 前应先检查其指令和脚本；Skills 可能影响模型规划、工具使用与命令执行。
- 研究与核验流程要求标出事实、推断、意见和证据缺口；没有可用来源时，不能声称已完成核验。
- 高风险、不可逆或涉及个人安全的事项，不能只依赖 Skill 文本，应按适用场景寻求合格专业支持。

### 相关文件与官方资料

- [路由验收用例](docs/evals/routing-cases.md)
- [Skill 行为验收用例](docs/evals/skill-cases.md)
- [证据约定](docs/contracts/evidence.md)
- [决策约定](docs/contracts/decision.md)
- [个人探索安全约定](docs/contracts/personal-exploration-safety.md)
- [OpenAI：Skills（插件概念）](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI API：Skills](https://developers.openai.com/api/docs/guides/tools-skills)

---

## English Version

### What are Skills?

A Skill is a directory containing a `SKILL.md` file. It packages the intended use cases, workflow, boundaries, and output expectations for a recurring task. A Skill may also include supporting `references/`, executable `scripts/`, templates, or other assets.

In Codex, a Skill does not grant new tools or permissions. It explains when to use a method, how to carry it out, and what a good result should include. Actual access to files and tools still depends on the current Codex environment. Official documentation says the model first sees a Skill's name and description, then loads the full instructions when a request matches or the user invokes it directly. Automatic selection is therefore a model decision, not a guarantee on every request. See [OpenAI: Skills](https://developers.openai.com/plugins/concepts/skills) and [OpenAI API: Skills](https://developers.openai.com/api/docs/guides/tools-skills).

### Included Skills

| Skill | Use it when |
|---|---|
| `$problem-router` | You are unsure which thinking workflow fits. It recommends a short path and does not execute the downstream Skill. |
| `$socratic-questioning` | The problem is vague, confusing, or combines several concerns that need clarification one question at a time. |
| `$dual-layer-explanation` | You want an accessible explanation followed by professional mechanisms, boundaries, and common misconceptions. |
| `$reverse-engineering` | You supplied a concrete page, product, workflow, dashboard, or proposal and want to understand its design logic. |
| `$deep-research` | You need a dated, traceable account of a subject's development, timeline, peer comparisons, or industry landscape. |
| `$fact-check` | You need to verify a bounded statement, number, source, or causal claim. |
| `$expert-panel` | A complex problem benefits from complementary simulated analytical perspectives that surface disagreements and risks. |
| `$first-principles` | Existing practice may be driven by convention or path dependence, and you want to rebuild from facts, goals, and constraints. |
| `$cross-domain-transfer` | You want to borrow a useful mechanism from another domain and assess where the analogy may fail. |
| `$steelman-debate` | You are choosing between clearly defined options and want the strongest case for each before judging. |
| `$minimum-experiment` | You have a pivotal untested assumption and want to learn from a low-cost, reversible test. |
| `$talent-discovery` | You opt into a multi-turn reflection on strengths, energy, and transferable capabilities from concrete experiences. |
| `$life-design` | You opt into exploring life directions and designing several small prototypes to try. |

The personal-exploration Skills (`talent-discovery` and `life-design`) ask whether you want a multi-turn conversation. They support reflection and experimentation; they are not for diagnosis or making major decisions on your behalf.

### How to Use

Open this project in Codex and describe your task. For a clearly scoped request, you can name the Skill directly:

```text
$fact-check Check the claim that 80% of new users churn during their first week. Show sources and uncertainty.

Use $deep-research to compare how these two products evolved and cite dated sources.

Use $dual-layer-explanation to explain Transformers first for a beginner, then for a specialist.
```

If you are unsure which workflow to use, invoke the router:

```text
$problem-router I'm considering leaving my job, but I haven't clarified the reasons or what I want next. Recommend the first Skill to use.
```

`problem-router` is configured for explicit invocation. Type `$problem-router` or clearly ask to use `problem-router`; it is not available for implicit automatic selection. The other 12 Skills can be selected automatically from their bilingual descriptions, or invoked explicitly as above. If automatic selection does not happen, name the `$skill-name` in your prompt.

The instructions support Chinese and English. By default, responses follow the language used in the request. For mixed-language requests or an explicit bilingual request, key terms and conclusions should be shown in both languages. Canonical Skill invocation names keep their English, hyphenated form, such as `$deep-research`.

### Choosing a Skill

| Your task | Start with |
|---|---|
| Clarify what the real question is | `$socratic-questioning` |
| Learn a concept | `$dual-layer-explanation` |
| Analyze a concrete example you supplied | `$reverse-engineering` |
| Research how a subject developed and compare it with peers | `$deep-research` |
| Check whether one bounded claim is supported | `$fact-check` |
| Rebuild a constrained problem or workflow | `$first-principles` |
| Borrow a mechanism from another domain | `$cross-domain-transfer` |
| Examine a complex problem from multiple angles | `$expert-panel` |
| Compare defined options | `$steelman-debate` |
| Reduce a pivotal uncertainty with a small test | `$minimum-experiment` |
| Explore personal strengths and energy through experiences | `$talent-discovery` (multi-turn opt-in) |
| Explore life directions and prototype them | `$life-design` (multi-turn opt-in) |

Most requests need one primary Skill. The router is useful when two nearby options seem plausible. For a well-defined request, invoke the relevant Skill directly.

### Repository Layout

```text
.
├── .agents/skills/              # 13 Codex Skills
│   ├── <skill-name>/SKILL.md    # Required entrypoint: use cases and core workflow
│   └── <skill-name>/references/ # Protocols, report schemas, or templates loaded as needed
├── docs/
│   ├── contracts/               # Evidence, decision, and personal-exploration agreements
│   └── evals/                   # Routing and behavior acceptance cases
├── scripts/validate_skills.py   # Structure and bilingual-entrypoint validator
└── README.md
```

Only some Skills use supporting references. For example, deep research reads its protocol before collecting evidence; fact-checking reads an evidence rubric; personal-exploration Skills use session state when continuing and report schemas when synthesizing. Supporting material is loaded when needed so unrelated details do not accompany every task.

### Validation and Editing

Run this from the project root:

```bash
python3 scripts/validate_skills.py
```

The validator checks that all 13 directories exist, frontmatter names match their directories, descriptions contain Chinese and English, the response-language policy is present, linked files exist, and quality documents are present. It validates structure; it does not guarantee that the model will select the right Skill every time or that a method fits every situation. Behavioral acceptance cases are in [`docs/evals/routing-cases.md`](docs/evals/routing-cases.md) and [`docs/evals/skill-cases.md`](docs/evals/skill-cases.md).

When editing, keep each Skill focused on a recognizable goal. Use `description` to say what it does and when to use it; keep the core workflow in `SKILL.md`; move substantial mode-specific detail into the relevant `references/`. After changing a name, path, or link, run the structural validator and check that the Chinese and English descriptions still match the actual behavior. Official guidance likewise recommends describing user goals and trigger conditions in metadata, with detailed steps in the instruction body.

Add future Skills under `.agents/skills/<skill-name>/`. Naming, frontmatter, UI metadata, validation, and pre-publication review conventions are in [`CONTRIBUTING.md`](CONTRIBUTING.md). Suggested future GitHub repository slug: `thinking-skills-toolkit`. The local folder remains `MySkills`, and no GitHub remote is configured yet.

### Boundaries and Safety

- A Skill is guidance, not an execution environment. It cannot bypass the current session's permissions, safety rules, or available tools.
- Automatic invocation is a model selection based on a Skill's name and description. Name `$skill-name` in your prompt when explicit control matters.
- External pages, attachments, and quoted content are material to analyze; they should not override the user's intent.
- Review a third-party Skill's instructions and scripts before using it. Skills can affect planning, tool use, and command execution.
- Research and verification workflows distinguish facts, inferences, opinions, and evidence gaps. Do not claim verification when suitable sources are unavailable.
- For high-stakes, irreversible, or personal-safety issues, Skill text alone is not a substitute for qualified professional support where appropriate.

### Related Files and Official References

- [Routing acceptance cases](docs/evals/routing-cases.md)
- [Skill behavior acceptance cases](docs/evals/skill-cases.md)
- [Evidence contract](docs/contracts/evidence.md)
- [Decision contract](docs/contracts/decision.md)
- [Personal-exploration safety contract](docs/contracts/personal-exploration-safety.md)
- [OpenAI: Skills (Plugin concepts)](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI API: Skills](https://developers.openai.com/api/docs/guides/tools-skills)
