# Template: My Model Routing Policy

**Purpose:** decide model placement once, in writing, instead of in every prompt. Adapt this template to your setup, keep it short enough that you will actually follow it, and save it where your agent reads it.

The example rows below are examples. Replace them with your own providers and classes. Do not copy another setup's routing; your cost paths and quality bars are your own.

## Models by task class

| Task class | Model or tier | Why this placement | Attempt limit |
| --- | --- | --- | --- |
| (example) Hard judgment, architecture, final review of risky changes | premium tier | needs the quality | 2 |
| (example) Extraction, formatting, bounded routine coding | frugal tier | wrong answers are cheap to catch | 2 |
| (example) Health checks, backups, cleanup | no model, deterministic tool or command job | no judgment needed | fixed by the tool |

## What requires my approval

- Model routing changes:
- Provider or plugin installs:
- Automation edits:
- Configuration changes:
- Anything else:

## Delegation rules

- Spawn a sub-agent only when isolation, parallelism, or specialist work adds real value.
- One agent, one narrow slice, one deliverable, one acceptance target.
- Pass a briefing pack, not raw conversation history.
- Default worker budget: children per task, concurrency, and a per-run timeout.
- Stop weak or looping workers early instead of letting them grind.

## Retry and fan-out limits

- Maximum retries per task class before stopping and reporting:
- Maximum parallel workers per task:
- Never duplicate the same research across workers without a reason.

## Verification requirements

- Commands verified against installed docs or `--help` before use.
- Recipes verified with a small safe test before trust.
- Quality checked against success criteria, not just token counts.
- Matched task rerun after any change, recorded on the measurement worksheet.

## Where my tools live

- Task runner and its recipe file:
- Scripts and validators:
- Prompting guidance for the models I use:
- Cost worksheets and this policy:

## Usage review

- Next review date:
- What to check: provider dashboards (authoritative), the worksheets, whether this policy is still being followed, and whether any rule should change based on evidence.

## Limitations of this policy

- (anything unverified, unknown, or worth rechecking)