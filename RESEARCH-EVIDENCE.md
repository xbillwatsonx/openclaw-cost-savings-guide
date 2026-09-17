# Research Evidence

**Purpose:** record where each claim in this package comes from, and what could not be verified. This draft was written against the installed OpenClaw 2026.9.4 documentation, with commands and defaults checked against the installed docs during drafting.

Status labels:

- **Verified, installed docs:** confirmed in the installed OpenClaw 2026.9.4 documentation during drafting.
- **Verified, provider docs:** confirmed in official provider documentation cited by the series research records.
- **Local example:** real, but specific to one workspace. Presented as an example only, never as a standard OpenClaw feature.
- **Creator-reported:** a content creator's own measurement. Not independently verified. Never used as a product claim.
- **Not verified, excluded:** could not be confirmed in the installed docs. Left out of reader-facing content.

## Verified, installed docs (OpenClaw 2026.9.4)

| Claim | Where it is used |
| --- | --- |
| Per-file bootstrap injection cap default 20,000 characters; total across files default 60,000 characters. | Guide Section 7 |
| Skills list cost: a fixed base block plus about 97 characters per eligible skill before the name, description, and location fields, roughly 24 tokens per skill at about four characters per token, bounded by the configured skills prompt budget. | Guide Section 7 |
| Sub-agent defaults: 8 concurrent child runs, 5 active children per session (range 1 to 20), nesting depth 5 (range 1 to 5), no run timeout unless configured, completed child state archived after 60 minutes. | Guide Section 8 |
| Sub-agent model and thinking settings inherit the caller unless configured otherwise. | Guide Section 8 |
| Rolling-history tool-loop detection is disabled by default; a separate post-compaction guard remains active unless the whole setting is explicitly disabled. | Guide Section 8 |
| `/stop` sent in the requester chat aborts session work and cancels its active child tree, reporting stopped and failed counts. | Guide Section 8, checklist |
| `/status` shows the session model and context usage; `/usage tokens` shows token counts; `/usage full` shows a compact footer with estimated cost only when local pricing is configured and the provider supplies usage data; `openclaw status --usage` and `openclaw channels list` show provider usage windows as a percentage left. | Guide Section 2, runbook Section 3 |
| Subscription-style sign-in surfaces show tokens rather than dollars unless they supply compatible usage data plus an explicitly configured local price. | Guide Section 2, runbook Section 3 |
| `/context list` shows injected content and rough sizes; `/context detail` adds per-file, per-tool schema, per-skill entry, and system prompt sizes plus compactable transcript counts. | Guide Section 7, runbook Sections 3 and 5 |
| Cron `--light-context` applies to isolated agent-turn jobs and keeps bootstrap context empty. | Guide Section 9 |
| Cron `--no-deliver` disables runner fallback delivery; it does not remove the agent's message tool when a chat route is available. | Verified background evidence, not stated in reader-facing guidance |
| Recurring jobs use exponential retry backoff after consecutive errors: 30 seconds, then 1, 5, 15, and 60 minutes, returning to normal after the next successful run. | Guide Section 9 |
| Completed isolated run sessions are pruned by default after 24 hours. | Verified background evidence, not stated in reader-facing guidance |
| A cron job pinned to a model is a job primary; when no fallback list is configured, the agent default is not silently added as a hidden retry target. | Guide Section 9 |
| For local model providers, the scheduler probes the endpoint first and records the run as skipped when unreachable, so failed runs do not spend model calls. | Guide Section 9 |
| OpenClaw can run a cron command job that executes a shell command and records the result without starting a model run; output consisting only of the silent reply token is suppressed. | Guide Section 9 |
| The silent reply token `NO_REPLY` / `no_reply` tells the delivery layer not to post anything. | Guide Section 9 |
| A configured default model can walk a configured fallback chain; an explicit session selection is strict and reports failure instead of silently answering from an unrelated model. | Guide Section 4 |
| Auth profiles rotate on auth failures, rate limits, billing limits, and timeouts; billing failures mark the credential disabled initially for ten minutes. | Verified background evidence, not stated in reader-facing guidance |
| Default image cap 1200 pixels on the longest side; lower values usually reduce vision-token usage on screenshot-heavy runs. | Guide Section 7 |
| tokenjuice is an optional external plugin (installable package), documented by OpenClaw, that compacts exec and bash tool results after the command runs without changing the command or its exit code. | Guide Section 5 |

## Verified, provider docs

| Claim | Where it is used |
| --- | --- |
| ChatGPT Work and Codex share one usage allowance with two windows, a 5-hour window and a weekly window. | Guide Section 12, bonus |
| A new 5-hour window starts at the first message after the previous window ends. | Guide Section 12, bonus |
| The Dubibubi video is about subscription allowance on a paid ChatGPT plan, not usage-based API billing. | Guide Section 12, bonus |

## Local examples (examples only, not standard OpenClaw features)

| Claim | How it is presented |
| --- | --- |
| Task-runner recipes for repeated operations. | The guide teaches the pattern with generic examples; no specific private recipes, paths, or validators are named. |
| Validators checking rules deterministically. | Same: the principle is taught, private implementations are not exposed. |

## Creator-reported, unverified

| Claim | Treatment |
| --- | --- |
| The creator's reported usage reduction percentages. | Not repeated anywhere in this package as numbers or promises. |
| The claim that models can see their own usage limits. | Explicitly labeled unverified in the bonus section. |
| The window-start scheduling trick from the video. | Not included; it only repositions a reset and is irrelevant to usage-based API billing. |

## Not verified, excluded from reader-facing content

| Claim | Why excluded |
| --- | --- |
| A default of 1 for maximum concurrent cron runs. | Could not be confirmed in the installed 2026.9.4 docs during drafting. |
| A default of 3 for cron retry attempts. | Could not be confirmed; only the backoff schedule (30 seconds through 60 minutes) is verified, so only that is stated. |
| A `/subagents kill <id>` slash command. | Could not be confirmed as an exact command surface in the installed docs. The verified `/stop` behavior is used instead. |

## Portability limits

- OpenClaw changes between versions. Every "as of OpenClaw 2026.9.4" default must be rechecked against installed docs and `--help` before release, and again after any OpenClaw update.
- Provider behavior (pricing, allowances, windows, model availability) changes without notice.
- What works for one provider's subscription does not necessarily apply to another provider or to usage-based API billing.
- Local inference shifts cost to hardware, power, and time; it is not automatically cheaper overall.
- Workspace conventions shown as examples are one setup's choices. Readers should adapt, not copy.

## Sources

- Installed OpenClaw 2026.9.4 documentation, checked directly during drafting, for every claim labeled "Verified, installed docs" above.
- OpenAI Help Center documentation on ChatGPT Work and Codex usage, for the subscription allowance claims.
- Dubibubi, "Never Hit Codex Usage Limits Again," published 2026-09-16, for the two adapted ideas in the bonus section, with unverified claims labeled as such.
- The series research records for this guide, including the corrected research packet and usage-optimization notes, which are themselves the source of the provider-doc verifications above.