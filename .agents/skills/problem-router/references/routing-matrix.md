# 路由矩阵 / Routing matrix

无论输入是中文、英文还是混合语言，都按意图而非输入语言路由。Route by intent, not by the language of the request.

| 需求 / Need | 推荐 Skill / Recommended skill | 不应替代的情况 / Do not substitute when |
|---|---|---|
| 找到真正需要回答的问题 / Find the real question | `socratic-questioning` | 用户已给出边界清晰的请求并要直接答案 / The request is already well-bounded and needs a direct answer. |
| 解释一个概念 / Explain a concept | `dual-layer-explanation` | 核心任务是评估现实世界主张 / The main task is evaluating a real-world claim. |
| 从给定样本中学习 / Learn from a supplied exemplar | `reverse-engineering` | 用户要做宽泛的市场或历史研究 / The user requests broad market or history research. |
| 研究产品、公司、技术、人物、行业或事件的演变 / Investigate development over time | `deep-research` | 用户只想核验单一断言 / The user wants one claim checked. |
| 核验陈述、数字、来源或因果主张 / Check a bounded claim | `fact-check` | 输入本质上是选项间的决策 / The input is mainly a decision between options. |
| 从事实、目标和约束重建路径 / Rebuild a path from fundamentals | `first-principles` | 问题是未经核验的事实主张 / The issue is an unverified factual claim. |
| 借用另一领域的机制 / Transfer a mechanism across domains | `cross-domain-transfer` | 期望用类比作为真实性证据 / The desired output is proof that an analogy is true. |
| 用互补模拟视角审视问题 / Use complementary simulated lenses | `expert-panel` | 单一明确方法已经足够 / A single clear method is sufficient. |
| 公平比较两个及以上明确立场 / Compare explicit positions fairly | `steelman-debate` | 选项尚未定义 / The options have not been defined. |
| 低成本检验一个不确定假设 / Test one uncertain assumption cheaply | `minimum-experiment` | 先需要完整研究报告 / A full research report is needed first. |
| 梳理优势、能量与可迁移模式 / Map strengths, energy, and transferable patterns | `talent-discovery` | 用户寻求诊断、治疗或定论式评估 / The user seeks diagnosis, therapy, or a definitive assessment. |
| 探索人生方向与原型行动 / Explore life directions and prototypes | `life-design` | 用户需要紧急危机响应或专业治疗 / The user needs immediate crisis response or professional treatment. |
