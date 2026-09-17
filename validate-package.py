#!/usr/bin/env python3
"""Validate the OpenClaw Cost Savings Guide package."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = [
    "README.md",
    "guide/the-openclaw-cost-savings-guide.md",
    "runbook/the-openclaw-cost-savings-runbook.md",
    "runbook/quick-start-card.md",
    "worksheets/setup-and-billing-route.md",
    "worksheets/before-and-after-measurement.md",
    "templates/model-routing-policy.md",
    "templates/sub-agent-budget-checklist.md",
    "templates/deterministic-tool-inventory.md",
    "prompts/01-explain-my-cost-path.md",
    "prompts/02-audit-my-openclaw-cost-patterns.md",
    "prompts/03-find-deterministic-tool-opportunities.md",
    "prompts/04-review-my-model-routing.md",
    "prompts/05-review-my-context-load.md",
    "prompts/06-review-my-sub-agent-controls.md",
    "prompts/07-review-my-automations.md",
    "prompts/08-test-one-cost-saving-change.md",
    "glossary.md",
    "RESEARCH-EVIDENCE.md",
    "VALIDATION-PLAN.md",
    "CHANGELOG.md",
    "LICENSE",
]

PRIVATE_PATTERNS = [
    r"/home/[^/\s]+",
    r"\.openclaw/workspace",
    r"\b\d{17,20}\b",
    r"\b\d{10,15}\b",
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    r"COO_POLICY",
    r"model-routing-manifest",
]

STALE_OR_UNSAFE_PATTERNS = [
    r"default per-file bootstrap cap is 12,000",
    r"maxSpawnDepth.{0,40}default.{0,10}1",
    r"ships an opt-in `tokenjuice`",
    r"built-in `tokenjuice`",
    r"\b[0-9]{1,3}(?:\.[0-9]+)?%",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for path in ROOT.rglob("*.md"):
        if "RUNBOOK_RELEASE_URL_PENDING" in path.read_text(encoding="utf-8"):
            fail(errors, f"unresolved release URL placeholder: {path.relative_to(ROOT)}")

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(errors, f"missing required file: {relative}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        if re.search(r"[—–]", text):
            fail(errors, f"em or en dash: {relative}")

        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                fail(errors, f"private surface match `{pattern}`: {relative}")

        for pattern in STALE_OR_UNSAFE_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE | re.DOTALL):
                fail(errors, f"stale or unsupported claim `{pattern}`: {relative}")

        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).resolve().exists():
                fail(errors, f"broken link `{match.group(1)}`: {relative}")

    prompts = sorted((ROOT / "prompts").glob("*.md"))
    if len(prompts) != 8:
        fail(errors, f"expected 8 prompts, found {len(prompts)}")

    for path in prompts:
        text = path.read_text(encoding="utf-8")
        required_fragments = [
            "../runbook/the-openclaw-cost-savings-runbook.md",
            "https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md",
            "explicit approval",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                fail(errors, f"prompt bridge missing `{fragment}`: {path.name}")
        if not re.search(r"read.+runbook", text, re.IGNORECASE | re.DOTALL):
            fail(errors, f"prompt does not instruct agent to read runbook: {path.name}")
        if not re.search(r"section", text, re.IGNORECASE):
            fail(errors, f"prompt does not name a runbook section: {path.name}")

    if errors:
        print(f"Cost savings package validation: FAIL ({len(errors)} finding(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Cost savings package validation: PASS")
    print(f"Required files: {len(REQUIRED)}/{len(REQUIRED)}")
    print(f"Prompts: {len(prompts)}/8")
    print(f"Markdown files checked: {len(markdown_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
