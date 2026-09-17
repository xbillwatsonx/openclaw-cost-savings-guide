# The OpenClaw Cost Savings Runbook

**Series:** AgentHelpSite OpenClaw series, special early companion, unnumbered
**Edition:** First edition, written against OpenClaw 2026.9.4
**Version:** 0.1.1

**Status:** Public release.
**Audience:** An OpenClaw agent working with the operator who invited you here

## Agent instructions

The user reached this runbook through one of the matching prompts. They do not need to read this document. Read it completely before acting.

1. Default to read-only inspection. Do not change files, configuration, models, providers, authentication, automations, plugins, or settings without the user's explicit approval of the exact change, given after you presented a proposal.
2. Never print credentials, tokens, API keys, or secret file contents. Describe their presence and location without exposing values.
3. Adapt to the user's actual setup. Do not assume a specific harness, task runner, provider, or directory layout. When something is unclear, ask.
4. Keep inspection, proposals, and changes separate, and apply one approved change at a time.
5. Never install providers or plugins, change authentication, alter model routing, edit automations, or modify configuration on your own initiative. Destructive actions, including deleting state, resetting, or uninstalling anything, are excluded from this runbook entirely.
6. OpenClaw can display provider-reported usage, recorded billed amounts, or locally estimated cost depending on the provider and route. Name the source of each figure and treat the provider's billing or plan-usage dashboard as the final authority.
7. This runbook was written against OpenClaw 2026.9.4. If the installed version differs, verify version-specific defaults against the installed docs or `--help` output before quoting them.
8. At the end of each stage, report: what you checked, what you found, what still needs attention, and the next safe step.

## 1. Outcome and boundaries

Help the user cut waste in their OpenClaw setup without sacrificing quality or reliability. By the end of this runbook they should have:

| Capability | Question it answers |
| --- | --- |
| Money path | Which cost path does each run consume: subscription allowance, usage-based API billing, or local inference? |
| Baseline | What does a representative task cost and produce today? |
| Ranked candidates | Which changes are most likely to help, with evidence? |
| Measured change | Did one approved change actually help, without hurting quality? |
| Cost policy | What written rules keep the setup lean after you leave? |

Boundaries for this whole runbook:

- inspection and measurement first; changes only after an explicit approval of one exact change;
- no fixed savings promises, in numbers or percentages, because none can be honestly made;
- the user's quality bar wins over any token saving;
- if a step cannot be done read-only, stop and propose instead.

## 2. Confirm scope and explain read-only inspection

**Goal:** make sure the user knows what this review does before anything runs.

Tell the user, in plain language:

- this stage inspects their setup and records measurements;
- you will run read-only commands and read configuration files, but change nothing;
- you will not print secret values;
- nothing changes later without a proposal and their explicit approval, one change at a time.

List the commands you intend to run in Section 3 and get their go-ahead. Then proceed. If the user asks for something outside this runbook, such as an install, a routing edit, or a destructive action, decline and explain it needs its own explicit request and plan.

**Stop condition:** if the user wants immediate changes before inspection, stop. Explain that a baseline taken before the change is what proves the change worked.

## 3. Identify the setup and the money path

**Goal:** determine the installed version, provider, active model, authentication route, usage surfaces, and deterministic tooling, without exposing credentials.

Run these read-only commands and report what they show:

```bash
openclaw --version
openclaw status
openclaw status --usage
openclaw channels list
```

In chat, when the surface is available, also use:

```text
/status
/usage tokens
/usage full
/context list
/context detail
```

Determine and report, without revealing secret values:

- the installed OpenClaw version, and whether any version-specific default you cite matches this install;
- the provider or providers in use;
- the active session model and the configured default, including whether the session is pinned or using a fallback;
- the authentication route for each provider: API key, OAuth or another account sign-in, or local access, without assuming that authentication alone proves the billing path;
- which usage surfaces exist and what each one shows: token counts, usage windows, estimated cost, or nothing;
- where the authoritative usage record lives: the provider's own dashboard;
- what is injected into context and how big it is, from `/context list` and `/context detail`;
- which deterministic tooling exists: task runners, recipes, scripts, validators.

Then classify each provider's cost path with the user: subscription allowance, usage-based API billing, or local inference. Fill the [setup and billing route worksheet](../worksheets/setup-and-billing-route.md) together. Distinguish paths explicitly. As of OpenClaw 2026.9.4, subscription-style sign-in surfaces show tokens rather than dollars unless they supply compatible usage data plus an explicitly configured local price.

A token-only surface does not prove usage-based API billing. Confirm the path with the provider's billing or plan-usage dashboard.

**Stop condition:** if you cannot determine the authentication route for a provider, say so and record it as unknown on the worksheet. Do not guess.

## 4. Choose representative tasks

**Goal:** pick one to three real tasks that will become the measurement baseline.

Ask the user for tasks they actually do, ideally recurring ones. For each chosen task, record:

- a short name for the task;
- what success looks like, in criteria the user can check;
- the model and cost path it currently uses;
- how often it runs.

These are the matched tasks for Section 9. If the user cannot pick, propose candidates from what you saw in Section 3 and let them choose. Do not proceed to changes without at least one task and its success criteria written down.

## 5. Inventory the setup

**Goal:** build an evidence-based inventory of what runs, what it costs, and what it produces.

Inspect and record, read-only:

1. Recurring tasks: what repeats, how it is invoked, and what it produces.
2. Premium-model use: which tasks use the most expensive configured models, and whether the work needs them.
3. Fallback behavior: what fallbacks are configured, whether session selections are strict or falling through, and what attempt limits exist.
4. Instructions and skills: the always-loaded instruction files, their sizes, duplicates, stale rules, and the skills list with its description lengths.
5. Context sources: injected file sizes from `/context list` and `/context detail`, truncation, heavy history, images.
6. Sub-agent patterns: what gets spawned, why, with what limits, hand-off formats, and whether children are tracked or duplicated.
7. Recurring automations: each job's schedule, whether it starts a model or runs a command, its delivery settings, retries, and whether it polls.
8. Deterministic tooling: task runners and their recipes, scripts, validators, and which repeated operations have none.
9. Known waste the user already suspects: retries, redo loops, repeated discovery, verbose outputs.

Use the [deterministic tool inventory](../templates/deterministic-tool-inventory.md) and [sub-agent budget checklist](../templates/sub-agent-budget-checklist.md) as recording aids where they fit.

Record evidence for every entry: the command output, file size, or count that supports it. Label anything you inferred as a hypothesis.

## 6. Identify candidate waste

**Goal:** turn the inventory into a list of candidate improvements, each with evidence and honest boundaries.

Look for, and only report when the evidence supports it:

- premium models doing routine, bounded work;
- repeated command discovery that a task-runner recipe or script could own;
- model judgment where a validator could check the result deterministically;
- stale, duplicate, or oversized always-loaded instructions;
- bulky skill descriptions inflating the skills list;
- bootstrap files at or beyond truncation caps;
- sub-agent fan-out without narrow slices, budgets, or structured hand-offs;
- polling loops or noisy recurring deliveries;
- model-driven automations that could be command jobs;
- weak workers or cheap models that loop and retry more than stronger routing would;
- verbose default output where a concise report would serve;
- broad paid search where the user already knows the exact starting point.

For each candidate, report:

- the evidence, from Section 5;
- the expected leverage, high, medium, or low, and why;
- when it helps, when it may not, and how the user could verify it;
- the effort, reversibility, and risk of changing it.

Never present a hypothesis as a finding, and never attach a savings percentage or promise to any candidate.

## 7. Rank recommendations

**Goal:** give the user a short, honest, ranked list.

Rank the candidates from Section 6 by, in order of importance:

1. expected leverage;
2. evidence strength;
3. reversibility;
4. effort;
5. risk.

Present the ranked list with one line of justification each. Recommend starting with the highest-leverage candidate that is low-risk, reversible, and easy to verify. Tell the user why the top item earns its place, and name any candidate you deliberately left off and why.

## 8. Propose one change and wait for explicit approval

**Goal:** one exact, low-risk change, approved in writing by the user before anything happens.

Present a proposal containing:

- the exact change, including the exact file, setting, command, or schedule involved;
- the evidence behind it, from the inventory;
- the expected effect and how it will be verified;
- what could go wrong;
- the rollback path, the exact steps to undo the change;
- the matched task from Section 4 that will measure it.

Then stop and wait. Do not apply the change, prepare the change, or "get ready" without approval. If the user says yes to a different or larger change than you proposed, write the new proposal and get approval for that version. One change at a time, always.

## 9. Apply the change and run the matched task

**Goal:** one approved change, measured fairly.

1. Apply exactly the approved change, nothing else.
2. Rerun the matched task with the same input as the baseline run.
3. Record, in the [before-and-after worksheet](../worksheets/before-and-after-measurement.md):
   - tokens in and out, or allowance change, from the available usage surfaces;
   - retries and tool calls;
   - quality against the success criteria;
   - elapsed time;
   - failures, repeated work, or cleanup needed.
4. Name the surface and type of each number: provider-reported usage, recorded billed amount, or local estimate. Treat the provider billing or plan-usage dashboard as the final authority.

**Stop condition:** if anything else changes while you work, such as a system update or an unrelated job, say so and note that the comparison may be contaminated.

## 10. Keep, revise, or roll back

**Goal:** let evidence decide.

Compare the after record to the baseline:

- keep the change if usage dropped and quality and reliability held;
- revise the change if the result is partial, then re-measure;
- roll back using the exact steps from the proposal if quality or reliability degraded, regardless of the token numbers.

Report the decision with the evidence. If the user cannot decide, recommend the safer option. Never hide a degraded result to protect a saving.

## 11. Save the cost policy and next review date

**Goal:** leave the setup protected after the review ends.

With the user, write a short personal cost policy using the [model routing policy template](../templates/model-routing-policy.md):

- which model classes handle which work;
- what requires approval;
- delegation and fan-out budgets;
- retry limits;
- required verification;
- where the task runner, recipes, scripts, validators, and prompting guidance live;
- the next usage review date.

Save it where the user wants it, with their approval for that location. Record on the policy:

- the limitations of this review: anything unverified, any unknowns from the worksheets;
- the completed worksheets, kept somewhere the user and future sessions can find them.

Finish by reporting: what was checked, what changed, what was measured, what was kept or rolled back, the policy location, and the next review date.