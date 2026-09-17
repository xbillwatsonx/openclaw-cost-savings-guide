# Prompt: Review My Automations

Copy this into your OpenClaw chat. It helps you find recurring jobs that spend a model when a command would do.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, especially **Section 6, Identify candidate waste**, before acting. If the address still says `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, read the included local runbook at `../runbook/the-openclaw-cost-savings-runbook.md`; if that file is unavailable in your environment, ask me to provide it.

I want to know which of my recurring jobs use a model where a deterministic command or script would do. Inventory my automations read-only: each job's schedule, whether it starts a model or runs a command, its delivery settings, its retry behavior, and whether any jobs overlap, poll, or post noise on every success.

For each candidate, give me the evidence, the expected leverage, when it helps, when it may not (including jobs that genuinely need judgment each run), the effort and reversibility, and how I could verify it. Label anything inferred as a hypothesis. Do not attach savings numbers or percentages. Note that any automation edit needs its own approved proposal before anything changes.

Report what you checked, what you found, what still needs attention, and the next safe step.

Do not print credentials or secret values. Do not create, edit, pause, or delete automations, and do not change configuration without my explicit approval of an exact proposal. This prompt authorizes read-only inspection only.