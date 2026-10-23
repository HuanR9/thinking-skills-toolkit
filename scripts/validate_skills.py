#!/usr/bin/env python3
"""Validate the repository's local Codex Skill structure without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
EXPECTED_SKILLS = (
    "problem-router",
    "socratic-questioning",
    "dual-layer-explanation",
    "reverse-engineering",
    "deep-research",
    "fact-check",
    "expert-panel",
    "first-principles",
    "cross-domain-transfer",
    "steelman-debate",
    "minimum-experiment",
    "talent-discovery",
    "life-design",
)
LANGUAGE_MARKER = "## 语言 / Language"


def frontmatter(content: str) -> str | None:
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    return match.group(1) if match else None


def scalar(block: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?(.+?)[\"']?\s*$", block, re.MULTILINE)
    return match.group(1).strip() if match else None


def validate() -> list[str]:
    errors: list[str] = []
    if not SKILLS_ROOT.is_dir():
        return [f"Missing skills root: {SKILLS_ROOT}"]

    actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    missing = set(EXPECTED_SKILLS) - actual
    unexpected = actual - set(EXPECTED_SKILLS)
    if missing:
        errors.append(f"Missing skill directories: {', '.join(sorted(missing))}")
    if unexpected:
        errors.append(f"Unexpected skill directories: {', '.join(sorted(unexpected))}")

    for name in EXPECTED_SKILLS:
        skill_dir = SKILLS_ROOT / name
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{name}: SKILL.md is missing")
            continue
        content = skill_file.read_text(encoding="utf-8")
        header = frontmatter(content)
        if header is None:
            errors.append(f"{name}: invalid or missing YAML frontmatter")
            continue
        if scalar(header, "name") != name:
            errors.append(f"{name}: frontmatter name does not match directory")
        description = scalar(header, "description")
        if not description or "TODO" in description:
            errors.append(f"{name}: missing or unfinished description")
        elif not re.search(r"[\u4e00-\u9fff]", description) or not re.search(r"[A-Za-z]", description):
            errors.append(f"{name}: description must include Chinese and English discovery terms")
        if LANGUAGE_MARKER not in content:
            errors.append(f"{name}: missing bilingual response-language policy")
        if "[TODO:" in content:
            errors.append(f"{name}: unfinished TODO marker")
        for relative in re.findall(r"\]\(([^)]+\.md)\)", content):
            target = (skill_dir / relative).resolve()
            if not target.is_file():
                errors.append(f"{name}: missing referenced file {relative}")

    router_config = SKILLS_ROOT / "problem-router" / "agents" / "openai.yaml"
    if not router_config.is_file():
        errors.append("problem-router: explicit invocation policy is missing")
    elif "allow_implicit_invocation: false" not in router_config.read_text(encoding="utf-8"):
        errors.append("problem-router: must remain explicit-only")

    for path in (
        ROOT / "docs" / "contracts" / "evidence.md",
        ROOT / "docs" / "contracts" / "decision.md",
        ROOT / "docs" / "contracts" / "personal-exploration-safety.md",
        ROOT / "docs" / "evals" / "routing-cases.md",
        ROOT / "docs" / "evals" / "skill-cases.md",
    ):
        if not path.is_file():
            errors.append(f"Missing quality artifact: {path.relative_to(ROOT)}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        sys.exit(1)
    print(f"Validated {len(EXPECTED_SKILLS)} Skills and supporting quality artifacts.")
