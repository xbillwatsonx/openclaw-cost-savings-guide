# Quick Start Card

Use this when you want to cut OpenClaw waste without breaking anything.

## The Simple Setup

Work through these three things:

1. Know your money path. Learn which cost path each run consumes: subscription allowance, usage-based API billing, or local inference.
2. Find waste with evidence. Inventory your setup and identify candidate waste, with evidence, before changing anything.
3. Change one thing at a time and measure. Apply one approved low-risk change, rerun a matched task with the same input, then keep, revise, or roll back based on evidence.

## Prompt Order

### Do Today

1. `prompts/01-explain-my-cost-path.md`: learn which cost path your runs consume
2. `prompts/02-audit-my-openclaw-cost-patterns.md`: get an evidence-based audit of cost patterns
3. `prompts/03-find-deterministic-tool-opportunities.md`: find repeated reasoning a deterministic tool could replace
4. `prompts/04-review-my-model-routing.md`: check which work runs on premium models
5. `prompts/05-review-my-context-load.md`: see what is always loaded into context
6. `prompts/06-review-my-sub-agent-controls.md`: review sub-agent limits and fan-out
7. `prompts/07-review-my-automations.md`: review recurring jobs for waste
8. `prompts/08-test-one-cost-saving-change.md`: propose, approve, apply, and measure one change

Complete all eight prompts before calling the cost review finished. Prompts 1 through 7 are read-only. Prompt 8 still requires your explicit approval before anything changes.

For prompts 1 through 7, your agent performs read-only inspection and reports what it found. Prompt 8 is where it proposes one exact change for you to approve or reject.

## What To Tell The Agent First

```text
Please use the included runbook at `runbook/the-openclaw-cost-savings-runbook.md` to help me cut OpenClaw cost and waste. Start by explaining my money path: my installed version, my provider or providers, my active model, my authentication route, and where my usage is actually recorded. Do not change anything yet. Everything is read-only until I approve one specific change.
```

## What Good Looks Like

- you know which cost path each run consumes
- you have a recorded baseline for at least one representative task
- candidate waste comes with evidence, not guesses
- one change at a time, measured with a matched task
- you keep, revise, or roll back based on evidence
- you have a saved cost policy and a next review date

## Safety Boundary

Do not approve plugin or provider installs, authentication changes, model routing edits, automation edits, or configuration changes unless the agent first proposed the exact change, its rollback path, and its verification plan. Never paste credentials into chat. Destructive actions are out of scope for this runbook.