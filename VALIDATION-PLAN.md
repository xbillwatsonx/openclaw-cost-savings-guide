# Validation Plan

**Purpose:** define what must pass before this package can be released, and record the results of the checks already run. Release gates passed on 2026-09-17: technical validation, beginner review, privacy review, complete package review, and owner approval.

## First-draft mechanical results (2026-09-17)

| Check | Result |
| --- | --- |
| All 22 required files exist | Pass. Every file in the frozen specification's package list exists, including this one. |
| Em and en dash scan | Pass. No em or en dashes in any file. |
| Privacy scan | Pass. No private home paths, usernames, hostnames, IDs, private model-routing details, or credentials in reader-facing files. |
| Prompt bridge check | Pass. All 8 prompts name `../runbook/the-openclaw-cost-savings-runbook.md`, identify the relevant runbook section, instruct the agent to read it first, state purpose and expected behavior, include `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/v0.1.1/runbook/the-openclaw-cost-savings-runbook.md`, and prohibit changes without explicit approval. |
| Internal link check | Pass. All relative markdown links resolve, including the README link to this file and the guide's internal prompt-table anchor. |
| Creator percentage scan | Pass. No creator-reported savings percentages appear in reader-facing files. |
| Version labels | Pass. Every version-specific statement carries an explicit OpenClaw 2026.9.4 label or appears inside a paragraph whose opening sentence carries that label. |
| Defaults verification | Pass. Every version-specific default was checked against the installed OpenClaw 2026.9.4 documentation during drafting (per-file bootstrap cap 20,000 characters; total 60,000; sub-agent concurrency 8, children per session 5 with range 1 to 20, spawn depth 5 with range 1 to 5, no run timeout by default, archive after 60 minutes; completed cron session retention 24 hours; image cap 1200 pixels; cron retry backoff 30 seconds through 60 minutes). |
| Excluded claims | Recorded. Three research-packet claims could not be confirmed in the installed docs and are excluded from reader-facing content; see RESEARCH-EVIDENCE.md. |

## Technical checks before release

| Check | Method | Status |
| --- | --- | --- |
| Commands and flags verified against installed docs or `--help` | Recheck every command in the guide and runbook against the installed version at release time | Pass, release recheck completed 2026-09-17 |
| Exact version-specific defaults sourced | Recheck the "as of 2026.9.4" items against installed docs after any OpenClaw update | Pass, release recheck completed 2026-09-17 |
| Subscription and API paths never conflated | Read Sections 2, 3, and 12 of the guide as a set | Pass, reviewed 2026-09-17 |
| Optional plugins correctly labeled | Confirm tokenjuice appears only as an optional external plugin with no install instruction | Pass, reviewed 2026-09-17 |
| Local workspace recipes clearly labeled as examples | Confirm no private recipe, path, or validator is named or implied as standard | Pass, reviewed 2026-09-17 |
| No credentials, private paths, or operator-specific data | Repeat the privacy scan; also review by a second reader | Pass, reviewed 2026-09-17 |
| No em or en dashes | Repeat the dash scan | Pass, release recheck completed 2026-09-17 |
| Internal links resolve | Repeat the link check | Pass, release recheck completed 2026-09-17 |
| Every prompt has the required runbook bridge | Repeat the prompt bridge check | Pass, release recheck completed 2026-09-17 |
| Glossary terms appear in content and use consistent definitions | Cross-check every glossary term against its first-use definition in the guide | Pass, reviewed 2026-09-17 |

## Evidence checks before release

| Check | Status |
| --- | --- |
| No fixed savings promise anywhere in the package | Pass, reviewed 2026-09-17 |
| Creator claims labeled | Pass, reviewed 2026-09-17 |
| Each recommendation states when it helps, when it may not, and how to verify it | Pass, reviewed 2026-09-17 |
| Matched before-and-after method measures quality and cleanup, not tokens alone | Pass, reviewed 2026-09-17 |

## Beginner simulations

Run each persona against the guide and quick-start card, revise only from evidence, then regress earlier passes:

1. A true non-technical beginner: pass, no blockers. They understood all three cost paths, the first action, and the approval boundary. The quick-start completion meaning and local-runbook fallback were clarified from their feedback.
2. A budget-conscious self-hosted operator: pass with minor feedback, no blockers. They confirmed that local inference is treated as a cost shift and that the runbook adapts to the actual setup. Astra audience context and the local-runbook fallback were clarified.
3. An API-billed operator: pass with minor feedback, no blockers. They understood the authoritative billing record and matched baseline. A token-only billing warning and measured-change guidance for optional tokenjuice use were added.
4. A subscription-backed operator: pass, no blockers. They understood allowance windows, the distinction from API billing, and that OAuth does not prove the billing path.
5. An operator with excessive agents and automations: pass, no blockers. They identified fan-out, polling, noisy delivery, and model-driven deterministic work as waste while preserving the approval boundary.

After these evidence-based revisions, repeatable package validation and the affected factual, privacy, terminology, prompt-bridge, link, and punctuation checks must pass again before owner review.

## Release gates, in order

1. Technical validation of commands and selected recommendations with controlled evidence.
2. Beginner validation simulations.
3. Privacy review.
4. Complete package review (factual, structural, privacy, mechanical).
5. Owner's bundled approval of the whole package.

The fixed runbook URL was inserted throughout the package before release. Link and prompt checks were repeated successfully.