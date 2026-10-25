---
name: problem-router
description: "为模糊问题、学习任务、研究请求、决策或自我探索选择合适的思维方法 / Recommend a thinking method for a vague problem, learning, research, decisions, or self-exploration. 只给出短路径，不执行后续任务 / Recommend a short path; do not solve the downstream task."
---

# 问题路由器 / Problem Router

## 语言 / Language

默认以用户当前使用的语言路由与说明：中文请求用中文，English requests use English。混合语言或要求双语时，用中英对照列出推荐路径和所需输入；技能标识保持英文连字符形式，例如 `deep-research`；具体调用语法由当前 Agent 决定。Match the user's language; preserve canonical hyphenated skill identifiers, while invocation syntax depends on the host agent.

## 目标 / Goal

分类用户请求，找出会改变路线的那个关键不确定性，并推荐审慎的下一项 Skill。本 Skill 是导航器，不是执行器：不得声称已经运行了其他 Skill。Classify the request, reveal the route-changing uncertainty, and recommend a next Skill; this is a navigator, not an executor.

## 流程 / Process

1. 识别主导意图：澄清、解释、逆向拆解样本、研究、核验主张、解决复杂问题、比较选择、做实验或探索个人方向。Identify the dominant intent among clarification, explanation, research, verification, decision, experiment, and personal exploration.
2. 评估请求是否需要外部证据、用户提供的样本、多轮对话，或不确定性下的决策。Assess whether it needs evidence, an exemplar, multi-turn dialogue, or a decision under uncertainty.
3. 若一个缺失事实会改变路线，只问这一问；否则输出一至三步路线。If one missing fact changes the route, ask only that question; otherwise output one to three steps.
4. 说明路线、适配原因、第一步所需输入，以及为什么不选最接近的替代方案。State route, fit, required input, and why the nearest alternative is not preferred.
5. 停止并让用户明确选择或调用第一项 Skill。Stop and let the user explicitly choose or invoke the first Skill.

## 路由边界 / Routing boundaries

- 真正不清晰的问题路由至 `socratic-questioning`，但不应强制每个请求都先澄清。Route genuinely unclear problems to `socratic-questioning`, not every request.
- 可界定事实主张路由至 `fact-check`；实体、行业或历史研究路由至 `deep-research`。Route bounded claims to fact-check and longitudinal investigations to deep research.
- 用户提供的页面、产品、仪表盘或流程路由至 `reverse-engineering`。Route supplied exemplars to `reverse-engineering`.
- 离散选择路由至 `steelman-debate`；未经检验的关键假设路由至 `minimum-experiment`。Route choices and pivotal assumptions appropriately.
- 只有用户同意多轮个人探索后，才把职业/人生材料路由至 `talent-discovery` 或 `life-design`。Require opt-in before personal-exploration Skills.
- 本次回复不得激活或开始执行下游 Skill。Do not activate or begin a downstream Skill in this response.

只有两个相近 Skill 都合理时，才阅读[路由矩阵 / routing matrix](references/routing-matrix.md)。Read the routing matrix only when two nearby Skills appear plausible.
