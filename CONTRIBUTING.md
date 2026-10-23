# 新增与维护 Skills / Adding and Maintaining Skills

## 中文

本仓库统一采用 Codex 项目级 Skills 目录。以后新建的 Skill 放在：

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

1. Skill 文件夹名使用小写英文、数字和连字符，保持稳定；目录名同时是 `$skill-name` 的调用名。给用户展示的 `display_name` 可以中英双语。
2. `SKILL.md` 的 YAML frontmatter 至少包含 `name` 和 `description`。描述中同时写入中文和英文的用途/触发场景，帮助两种语言的请求匹配。
3. 正文说明适用条件、主要流程、输出要求与真实边界；默认跟随用户语言回应。仅在必要时才新增脚本、参考资料或模板。
4. `agents/openai.yaml` 是可选的产品界面元数据。若添加，确保 `display_name`、25–64 字符的 `short_description` 和 `default_prompt` 与 Skill 一致；默认提示需包含 `$skill-name`。只有明确需要时才关闭隐式调用。
5. 参考文件应从 `SKILL.md` 链接；避免孤立文件、重复规则和未完成的 TODO 占位符。
6. 新增/修改后，从仓库根目录运行 `python3 scripts/validate_skills.py`，并按需补充 `docs/evals/` 中可观察的验收场景。
7. 公开上传前检查所有文件，不要提交密钥、个人信息、机器生成的杂项或未审阅的第三方指令。公开发布时需自行确认合适的许可证；本仓库目前不预设许可证。

命名和调用名要稳定，因为 README、路由矩阵、评测和用户提示可能都会引用它。需要调整目录名时，同步更新 `SKILL.md`、路由矩阵、验收用例和所有引用。

## English

Add future Skills to the repository's Codex project-level directory:

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

1. Use a stable lowercase folder name with English letters, digits, and hyphens. The folder name is also the `$skill-name` invocation. A user-facing `display_name` may be bilingual.
2. The `SKILL.md` YAML frontmatter must include at least `name` and `description`. Include Chinese and English use cases or trigger terms in the description to support requests in either language.
3. Describe when the Skill applies, its core workflow, output expectations, and real boundaries. Responses should follow the user's language. Add scripts, references, or templates only when they serve a concrete need.
4. `agents/openai.yaml` is optional UI metadata. If present, keep `display_name`, a 25–64 character `short_description`, and `default_prompt` consistent with the Skill; the default prompt must include `$skill-name`. Disable implicit invocation only when explicitly needed.
5. Link reference files from `SKILL.md`. Avoid orphaned files, duplicated rules, and unfinished TODO scaffolding.
6. After additions or edits, run `python3 scripts/validate_skills.py` from the repository root and add observable acceptance scenarios under `docs/evals/` when useful.
7. Review all files before public upload. Do not commit secrets, personal information, machine-generated clutter, or unreviewed third-party instructions. Choose an appropriate license before public distribution; this repository does not currently assume one.

Keep names and invocation identifiers stable because the README, routing matrix, evaluations, and user prompts may refer to them. If a folder name changes, update its manifest, the routing matrix, acceptance cases, and all links.
