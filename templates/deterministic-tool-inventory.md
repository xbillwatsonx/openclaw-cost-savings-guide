# Inventory: Deterministic Tools

**Purpose:** record the commands that have been verified once so the agent never has to re-derive them. A deterministic tool produces the same result every run without model judgment: a task-runner recipe, a script, or a validator.

The names below are placeholders. Fill them with your own tools. Nothing here requires a specific task runner; `just`, `make`, `Task`, or documented shell scripts all work.

## Task runners present

| Task runner | Where its file lives | How to list its recipes |
| --- | --- | --- |
|  |  |  |

## Recipes that exist and are verified

| Recipe name | What it does | How it was verified | When the agent should use it |
| --- | --- | --- | --- |
|  |  |  |  |

## Scripts and validators

| Script or validator | What it checks | Where it lives | How to run it safely |
| --- | --- | --- | --- |
|  |  |  |  |

## Candidates worth converting

Repeated operations the agent keeps re-deriving. Each one is a recurring inference cost.

| Repeated operation | How often it runs | Current cost signal (turns, retries, rework) | Recipe or script idea |
| --- | --- | --- | --- |
|  |  |  |  |

## Teaching the agent

Where the agent is told to prefer these tools (instruction file and section):

Rules worth writing there:

- Check the task runner's recipe list before inventing a command.
- Verify any new command against installed help or docs, then verify the recipe with a small safe test.
- If a decision or format can be checked deterministically, use the validator instead of judging by eye.