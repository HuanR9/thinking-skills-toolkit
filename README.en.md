# Thinking Toolkit

[简体中文](README.md) · English

A collection of reusable thinking workflows for multiple AI agents, covering routing, explanation, research, verification, decisions, and personal exploration. The core skills follow the open Agent Skills format and use `SKILL.md` plus Markdown references; they do not depend on a specific model or agent tool.

Agent Skills standardizes skill content, but each agent may use a different discovery directory, installation method, invocation syntax, or capability set. Place the skill folders in a location supported by the target agent; this repository uses `.agents/skills/` as one project-level layout. `agents/openai.yaml` contains OpenAI/Codex interface metadata only and is not part of the cross-agent core.

## Skills

| Skill | Use it when |
|---|---|
| `problem-router` | You are unsure which thinking workflow fits. It recommends a short path and does not execute the downstream Skill. |
| `socratic-questioning` | The problem is vague, confusing, or combines several concerns that need clarification one question at a time. |
| `dual-layer-explanation` | You want an accessible explanation followed by professional mechanisms, boundaries, and common misconceptions. |
| `reverse-engineering` | You supplied a concrete page, product, workflow, dashboard, or proposal and want to understand its design logic. |
| `deep-research` | You need a dated, traceable account of a subject's development, timeline, peer comparisons, or industry landscape. |
| `fact-check` | You need to verify a bounded statement, number, source, or causal claim. |
| `expert-panel` | A complex problem benefits from complementary simulated analytical perspectives that surface disagreements and risks. |
| `first-principles` | Existing practice may be driven by convention or path dependence, and you want to rebuild from facts, goals, and constraints. |
| `cross-domain-transfer` | You want to borrow a useful mechanism from another domain and assess where the analogy may fail. |
| `steelman-debate` | You are choosing between clearly defined options and want the strongest case for each before judging. |
| `minimum-experiment` | You have a pivotal untested assumption and want to learn from a low-cost, reversible test. |
| `talent-discovery` | You opt into a multi-turn reflection on strengths, energy, and transferable capabilities from concrete experiences. |
| `life-design` | You opt into exploring life directions and designing several small prototypes to try. |

The personal-exploration Skills (`talent-discovery` and `life-design`) ask whether you want a multi-turn conversation. They support reflection and experimentation; they are not for diagnosis or making major decisions on your behalf.

## Quick Start

In a tool that supports Agent Skills, place the desired skill folders in its supported skill directory and describe your task. Discovery and activation behavior depend on the agent. To request a specific skill, name it in natural language:

```text
Use the fact-check skill to check the claim that 80% of new users churn during their first week. Show sources and uncertainty.

Use the deep-research skill to compare how these two products evolved and cite dated sources.

Use the dual-layer-explanation skill to explain Transformers first for a beginner, then for a specialist.
```

If you are unsure which workflow to use, invoke the router:

```text
Use the problem-router skill: I'm considering leaving my job, but I haven't clarified the reasons or what I want next. Recommend the first skill to use.
```

In this repository's Codex configuration, `problem-router` is set to explicit invocation. Other agents may not follow that setting. For cross-agent use, invoke a skill with the target tool's syntax or name it in natural language. Automatic matching is not guaranteed.

The instructions support Chinese and English. By default, responses follow the language used in the request. For mixed-language requests or an explicit bilingual request, key terms and conclusions should be shown in both languages. Stable skill identifiers use lowercase English names, such as `deep-research`; invocation syntax depends on the agent.

## Choosing a Skill

| Your task | Start with |
|---|---|
| Clarify what the real question is | `socratic-questioning` |
| Learn a concept | `dual-layer-explanation` |
| Analyze a concrete example you supplied | `reverse-engineering` |
| Research how a subject developed and compare it with peers | `deep-research` |
| Check whether one bounded claim is supported | `fact-check` |
| Rebuild a constrained problem or workflow | `first-principles` |
| Borrow a mechanism from another domain | `cross-domain-transfer` |
| Examine a complex problem from multiple angles | `expert-panel` |
| Compare defined options | `steelman-debate` |
| Reduce a pivotal uncertainty with a small test | `minimum-experiment` |
| Explore personal strengths and energy through experiences | `talent-discovery` (multi-turn opt-in) |
| Explore life directions and prototype them | `life-design` (multi-turn opt-in) |

Most requests need one primary Skill. The router is useful when two nearby options seem plausible. For a well-defined request, invoke the relevant Skill directly.

## Repository Layout

```text
.
├── .agents/skills/              # 13 skills using the Agent Skills format
│   ├── <skill-name>/SKILL.md    # Portable entrypoint: use cases and core workflow
│   └── <skill-name>/references/ # Protocols, report schemas, or templates loaded as needed
├── docs/
│   ├── contracts/               # Evidence, decision, and personal-exploration agreements
│   └── evals/                   # Routing and behavior acceptance cases
├── scripts/validate_skills.py   # Skill structure and OpenAI/Codex metadata validator
├── README.md                    # Chinese documentation
└── README.en.md                 # English documentation
```

Only some Skills use supporting references. For example, deep research reads its protocol before collecting evidence; fact-checking reads an evidence rubric; personal-exploration Skills use session state when continuing and report schemas when synthesizing. Supporting material is loaded when needed so unrelated details do not accompany every task.

## Validation and Editing

Run this from the project root:

```bash
python3 scripts/validate_skills.py
```

The validator checks that all 13 directories exist, frontmatter names match their directories, descriptions contain Chinese and English, the response-language policy is present, linked files exist, and quality documents are present. It validates structure; it does not guarantee that the model will select the right Skill every time or that a method fits every situation. Behavioral acceptance cases are in [`docs/evals/routing-cases.md`](docs/evals/routing-cases.md) and [`docs/evals/skill-cases.md`](docs/evals/skill-cases.md).

When editing, keep each Skill focused on a recognizable goal. Use `description` to say what it does and when to use it; keep the core workflow in `SKILL.md`; move substantial mode-specific detail into the relevant `references/`. After changing a name, path, or link, run the structural validator and check that the Chinese and English descriptions still match the actual behavior. Official guidance likewise recommends describing user goals and trigger conditions in metadata, with detailed steps in the instruction body.

Add future portable skill content under `.agents/skills/<skill-name>/`. When sharing with another agent, install or copy the skill directory according to that tool's discovery mechanism and keep `SKILL.md` plus its references self-contained. Naming, frontmatter, platform metadata, validation, and pre-publication review conventions are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Boundaries and Safety

- A Skill is guidance, not an execution environment. It cannot bypass the current session's permissions, safety rules, or available tools.
- Automatic and explicit invocation behavior depends on the agent; names and descriptions do not guarantee identical discovery or activation across tools.
- External pages, attachments, and quoted content are material to analyze; they should not override the user's intent.
- Review a third-party Skill's instructions and scripts before using it. Skills can affect planning, tool use, and command execution.
- Research and verification workflows distinguish facts, inferences, opinions, and evidence gaps. Do not claim verification when suitable sources are unavailable.
- For high-stakes, irreversible, or personal-safety issues, Skill text alone is not a substitute for qualified professional support where appropriate.

## References

- [Routing acceptance cases](docs/evals/routing-cases.md)
- [Skill behavior acceptance cases](docs/evals/skill-cases.md)
- [Evidence contract](docs/contracts/evidence.md)
- [Decision contract](docs/contracts/decision.md)
- [Personal-exploration safety contract](docs/contracts/personal-exploration-safety.md)
- [OpenAI: Skills (Plugin concepts)](https://developers.openai.com/plugins/concepts/skills)
- [OpenAI API: Skills](https://developers.openai.com/api/docs/guides/tools-skills)
- [Agent Skills open specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
