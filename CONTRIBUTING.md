# 新增与维护 Skills / Adding and Maintaining Skills

## 中文

本仓库的技能核心遵循开放的 Agent Skills 格式。`SKILL.md` 与 Markdown 参考文件承载可跨 Agent 复用的内容；本仓库将它们放在 `.agents/skills/`，这是目录布局选择，不代表每种 Agent 都会从该路径自动发现技能。分享或安装时，按目标 Agent 支持的目录和加载方式适配。

```text
.agents/skills/<skill-name>/
```

每个 Skill 至少包含一个 `SKILL.md`，建议结构如下：

```text
<skill-name>/
├── SKILL.md
├── agents/openai.yaml       # 可选：Codex UI 名称、描述和默认提示
├── references/              # 可选：仅在特定流程需要的长文档/模板
├── scripts/                 # 可选：可重复执行且确有必要的工具
└── assets/                  # 可选：生成结果要用到的素材
```

维护约定：

1. Skill 文件夹名使用小写英文、数字和连字符，保持稳定；目录名和 frontmatter 中的 `name` 是稳定标识。调用命令或语法由具体 Agent 决定。给用户展示的 `display_name` 可以中英双语。
2. `SKILL.md` 的 YAML frontmatter 至少包含 `name` 和 `description`。描述中同时写入中文和英文的用途/触发场景，帮助两种语言的请求匹配。
3. 正文说明适用条件、主要流程、输出要求与真实边界；默认跟随用户语言回应。避免依赖单一 Agent 专属的调用语法、工具或能力；确需使用时，注明前提并提供可行的降级路径。仅在必要时才新增脚本、参考资料或模板。
4. `agents/openai.yaml` 是可选的 OpenAI/Codex 界面元数据，不属于跨 Agent 核心。若添加，确保 `display_name`、`short_description` 和 `default_prompt` 与 Skill 一致；提示内容可使用 OpenAI/Codex 的调用方式。隐式调用策略也只对支持该元数据的环境生效。
5. 参考文件应从 `SKILL.md` 链接；避免孤立文件、重复规则和未完成的 TODO 占位符。
6. 新增/修改后，从仓库根目录运行 `python3 scripts/validate_skills.py`，并按需补充 `docs/evals/` 中可观察的验收场景。新增技能时同步更新校验器中的 `EXPECTED_SKILLS`。若要宣称支持某个 Agent，还应在该 Agent 上核实目录发现、元数据处理和调用行为。
7. 公开上传前检查所有文件，不要提交密钥、个人信息、机器生成的杂项或未审阅的第三方指令。公开发布时需自行确认合适的许可证；本仓库目前不预设许可证。

技能名称作为稳定标识，应保持一致，因为 README、路由矩阵、评测和用户提示可能都会引用它。需要调整目录名时，同步更新 `SKILL.md`、路由矩阵、验收用例和所有引用；具体调用语法按目标 Agent 适配。

## English

The skill core in this repository follows the open Agent Skills format. `SKILL.md` and Markdown references carry the reusable content. This repository stores them under `.agents/skills/`; that is a layout choice and does not mean every agent discovers skills from this path automatically. Adapt installation and loading to the target agent.

```text
.agents/skills/<skill-name>/
```

Every Skill needs a `SKILL.md`. A useful layout is:

```text
<skill-name>/
├── SKILL.md
├── agents/openai.yaml       # Optional: Codex UI name, description, and prompt
├── references/              # Optional: longer material needed for specific workflows
├── scripts/                 # Optional: necessary repeatable utilities
└── assets/                  # Optional: files used in generated outputs
```

Conventions:

1. Use a stable lowercase folder name with English letters, digits, and hyphens. The folder name and frontmatter `name` are stable identifiers; invocation syntax depends on the agent. A user-facing `display_name` may be bilingual.
2. The `SKILL.md` YAML frontmatter must include at least `name` and `description`. Include Chinese and English use cases or trigger terms in the description to support requests in either language.
3. Describe when the Skill applies, its core workflow, output expectations, and real boundaries. Responses should follow the user's language. Avoid relying on one agent's invocation syntax, tools, or capabilities; when such a dependency is necessary, state the prerequisite and provide a fallback. Add scripts, references, or templates only when they serve a concrete need.
4. `agents/openai.yaml` is optional OpenAI/Codex interface metadata, not part of the cross-agent core. If present, keep `display_name`, `short_description`, and `default_prompt` consistent with the Skill; the prompt may use OpenAI/Codex invocation syntax. Implicit-invocation policy applies only in environments that support this metadata.
5. Link reference files from `SKILL.md`. Avoid orphaned files, duplicated rules, and unfinished TODO scaffolding.
6. After additions or edits, run `python3 scripts/validate_skills.py` from the repository root, update `EXPECTED_SKILLS` in the validator when adding a skill, and add observable acceptance scenarios under `docs/evals/` when useful. To claim support for an agent, verify discovery paths, metadata handling, and invocation behavior in that agent.
7. Review all files before public upload. Do not commit secrets, personal information, machine-generated clutter, or unreviewed third-party instructions. Choose an appropriate license before public distribution; this repository does not currently assume one.

Keep skill names stable because the README, routing matrix, evaluations, and user prompts may refer to them. If a folder name changes, update its manifest, the routing matrix, acceptance cases, and all links; adapt invocation syntax for each target agent.
