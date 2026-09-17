# The OpenClaw Cost Savings Guide

**Series position:** A special early guide. It releases after Runbook 1 and before the currently planned Runbook 2. It is not part of the numbered runbook sequence, and its companion runbook stays unnumbered.

**Edition:** Written against OpenClaw 2026.9.4. Recheck version-specific details against your installed docs before release.

**Version:** 0.1.0

**Status:** Public release.

**Runbook address:** `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`

## What this package is

The guide explains the ideas and decisions behind spending less on OpenClaw runs. The companion runbook turns those ideas into a safe, adaptive, approval-gated review of your actual setup. The guide teaches. The runbook does the work with your agent, one approved change at a time.

No file in this package promises a fixed savings percentage. Every recommendation states when it helps, when it may not, and how to verify it.

## How to use this package

1. Read the [guide](guide/the-openclaw-cost-savings-guide.md) to understand the ideas.
2. Open the [quick-start card](runbook/quick-start-card.md) when you are ready to start.
3. Copy the [prompts](prompts/01-explain-my-cost-path.md) into your OpenClaw chat one at a time. Each prompt tells your agent which runbook section to read first and keeps the work read-only until you approve a specific change.

## Contents

| File | What it is |
| --- | --- |
| [guide/the-openclaw-cost-savings-guide.md](guide/the-openclaw-cost-savings-guide.md) | The main guide. Explains the money path, measurement, routing, deterministic tools, context, sub-agents, automations, and a personal cost policy. |
| [runbook/the-openclaw-cost-savings-runbook.md](runbook/the-openclaw-cost-savings-runbook.md) | The companion runbook your agent executes. Adaptive and approval-gated. |
| [runbook/quick-start-card.md](runbook/quick-start-card.md) | The short card: what to do, in what order, and the safety boundary. |
| [worksheets/setup-and-billing-route.md](worksheets/setup-and-billing-route.md) | Record your providers, models, authentication routes, and cost paths. |
| [worksheets/before-and-after-measurement.md](worksheets/before-and-after-measurement.md) | Record a matched before-and-after comparison for one change. |
| [templates/model-routing-policy.md](templates/model-routing-policy.md) | A template for your personal cost policy. |
| [templates/sub-agent-budget-checklist.md](templates/sub-agent-budget-checklist.md) | A checklist for spawning sub-agents deliberately instead of by habit. |
| [templates/deterministic-tool-inventory.md](templates/deterministic-tool-inventory.md) | An inventory for task-runner recipes, scripts, and validators. |
| [prompts/01-explain-my-cost-path.md](prompts/01-explain-my-cost-path.md) | Learn which cost path your runs consume. |
| [prompts/02-audit-my-openclaw-cost-patterns.md](prompts/02-audit-my-openclaw-cost-patterns.md) | Get an evidence-based audit of your cost patterns. |
| [prompts/03-find-deterministic-tool-opportunities.md](prompts/03-find-deterministic-tool-opportunities.md) | Find repeated reasoning that a deterministic tool could replace. |
| [prompts/04-review-my-model-routing.md](prompts/04-review-my-model-routing.md) | Check which work runs on premium models. |
| [prompts/05-review-my-context-load.md](prompts/05-review-my-context-load.md) | See what is always loaded into context. |
| [prompts/06-review-my-sub-agent-controls.md](prompts/06-review-my-sub-agent-controls.md) | Review sub-agent limits and fan-out. |
| [prompts/07-review-my-automations.md](prompts/07-review-my-automations.md) | Review recurring jobs for waste. |
| [prompts/08-test-one-cost-saving-change.md](prompts/08-test-one-cost-saving-change.md) | Propose, approve, apply, and measure one change. |
| [glossary.md](glossary.md) | Plain definitions shared across the package. |
| [RESEARCH-EVIDENCE.md](RESEARCH-EVIDENCE.md) | The evidence record behind the claims in this package. |
| [VALIDATION-PLAN.md](VALIDATION-PLAN.md) | What must pass before release. |
| [CHANGELOG.md](CHANGELOG.md) | What changed and when. |
| [LICENSE](LICENSE) | CC BY 4.0 license. |

## Safety

The runbook defaults to read-only inspection. Your agent must not install providers or plugins, change authentication, alter model routing, edit automations, or modify configuration without your explicit approval of the exact change. Destructive actions are out of scope. Never paste credentials into chat.