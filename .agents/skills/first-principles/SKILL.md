---
name: first-principles
description: "当既有做法可能受路径依赖影响时，从已确认事实、目标、约束和假设重建方案 / Rebuild a solution from confirmed facts, goals, constraints, and assumptions. 不用于简单查询或未经核验的事实主张 / Do not use for a simple lookup or unverified factual claim."
---

# 第一性原理 / First Principles

## 语言 / Language

默认以用户当前使用的语言回答：中文请求用中文，English requests use English。用户混用语言或要求双语时，为核心概念和前提提供中英对照；不要翻译代码标识符、法律名称、标准名称或用户原文，除非被要求。Match the user's language and preserve exact identifiers unless asked to translate.

## 目标 / Goal

找出既有方案只是修补症状的地方，再从问题最底层仍有用的事实推导替代方案。Expose symptom-patching approaches and derive alternatives from the lowest useful-level facts.

## 流程 / Process

1. 重述问题与预期结果；若缺失目标或约束会实质改变分析，只问一个问题。Restate problem and outcome; ask one question only if material.
2. 列出不可妥协事实、未检验假设、目标、资源和约束。Inventory facts, assumptions, outcomes, resources, and constraints.
3. 识别当前方法中哪些只是惯例或局部优化，而非必要条件。Identify convention or local optimization versus necessity.
4. 从事实、目标和约束重建一个或多个可行路径。Rebuild feasible paths from facts, goals, and constraints.
5. 输出表层补丁、重建路径、成立假设、风险和第一步验证。Output surface patches, reconstructed path, assumptions, risks, and first validation.

## 质量规则 / Quality rules

- 不因一项断言熟悉或在行业常见，就把它叫作基本事实。Do not call familiarity a basic fact.
- 保留真实的法律、安全、预算、时间和人际约束；第一性原理不等于可以无视它们。Preserve genuine constraints.
- 分析依赖争议证据时推荐 `fact-check`；一个假设主导选择时推荐 `minimum-experiment`。Use the indicated Skills for disputed evidence or pivotal assumptions.
