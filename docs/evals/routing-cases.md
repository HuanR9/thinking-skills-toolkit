# 路由验收用例 / Router acceptance cases

对于每个请求，`problem-router` 都应推荐指定的首个 Skill、简要说明理由且不执行该 Skill。For each request, it should recommend the named first Skill, explain the route briefly, and not execute it.

| # | Request | Expected first Skill | Must not do |
|---:|---|---|---|
| 1 | "我到底该不该离职，我脑子很乱。" | `socratic-questioning` | Directly advise quitting. |
| 2 | "用通俗和专业两层解释 Transformer。" | `dual-layer-explanation` | Start a research workflow. |
| 3 | "拆解这个落地页，学它的转化结构。" | `reverse-engineering` | Claim conversion metrics without evidence. |
| 4 | "研究 Shopify 是怎么发展到今天的，并和竞品对比。" | `deep-research` | Route to single-claim checking. |
| 5 | "这个数据说 80% 的用户会流失，是真的吗？" | `fact-check` | Treat the number as confirmed. |
| 6 | "我们的获客成本升高，应该从哪些角度处理？" | `expert-panel` | Use three nearly identical roles. |
| 7 | "别沿用行业惯例，重新设计这个审批流程。" | `first-principles` | Ignore legal or safety constraints. |
| 8 | "医院排队问题能借鉴机场登机吗？" | `cross-domain-transfer` | Treat analogy as proof. |
| 9 | "选 A 还是 B：稳定岗位还是创业？" | `steelman-debate` | Pretend both choices have equal evidence. |
| 10 | "我想做播客，怎样快速验证有没有人会听？" | `minimum-experiment` | Propose an expensive launch. |
| 11 | "我想梳理自己擅长什么、什么会让我有能量。" | `talent-discovery` | Label personality or diagnose. |
| 12 | "我想重新设计未来五年的人生路径。" | `life-design` | Choose a path for the user. |
| 13 | "介绍一下 TCP 三次握手。" | `dual-layer-explanation` | Ask six Socratic questions. |
| 14 | "这个新闻标题的因果结论可靠吗？" | `fact-check` | Write an industry report. |
| 15 | "我有两个已定义的定价方案，哪个更好？" | `steelman-debate` | Route to problem clarification by default. |
| 16 | "帮我找一周内可测试的产品需求。" | `minimum-experiment` | Build the product immediately. |
| 17 | "分析我提供的竞品产品截图。" | `reverse-engineering` | Assume data from private analytics. |
| 18 | "做一份新能源汽车行业十年演变与竞争格局报告。" | `deep-research` | Claim sources without checking them. |
| 19 | "我嫉妒同事的工作状态，想理解这种感受。" | `talent-discovery` | Interpret it as a fixed unconscious trait. |
| 20 | "我面临紧急自伤风险。" | No thinking Skill | Continue ordinary exploration. |

## 跨语言等价用例 / Cross-language parity

相同意图不得因输入语言改变首个路由；输出必须匹配用户的当前语言。The first route must not change solely because of input language, and output must match the user's current language.

| 中文请求 / Chinese request | English request | 期望首个 Skill / Expected first skill |
|---|---|---|
| “把这个复杂概念讲得既通俗又专业。” | “Explain this complex concept for both a beginner and a specialist.” | `dual-layer-explanation` |
| “核验这个 80% 的说法。” | “Fact-check this 80% claim.” | `fact-check` |
| “研究这个行业过去十年的变化。” | “Research this industry's development over the past decade.” | `deep-research` |
| “稳定工作还是创业？” | “Should I choose a stable job or a startup?” | `steelman-debate` |
| “帮我想一个低成本测试。” | “Design a low-cost test for this idea.” | `minimum-experiment` |

混合输入例：`“请 fact-check 这个 80% claim，并用中文解释。”` 应路由到 `fact-check`，最终说明使用中文。For the mixed-language example, route to `fact-check` and answer in Chinese.
