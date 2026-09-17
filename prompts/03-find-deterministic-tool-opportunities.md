# Prompt: Find Deterministic Tool Opportunities

Copy this into your OpenClaw chat. It helps you find repeated model reasoning that a recipe, script, or validator could own instead.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/v0.1.1/runbook/the-openclaw-cost-savings-runbook.md`, especially **Sections 5 and 6, Inventory the setup and Identify candidate waste**, before acting. If you cannot access that address, ask me to provide the included local runbook file at `../runbook/the-openclaw-cost-savings-runbook.md`.

I want to find operations my agent keeps re-deriving, where a task-runner recipe, script, or validator could do the same job deterministically. List the task runners, recipes, scripts, and validators I already have, then list repeated operations worth converting, how often each runs, and the cost signal for each, such as turns spent rediscovering, retries, or rework.

For each candidate, give me the evidence, when a deterministic tool helps, when it may not (including one-off commands that are not worth it), and how to verify the recipe reproduces the verified command's result. Label anything inferred as a hypothesis.

Report what you checked, what you found, what still needs attention, and the next safe step.

Do not print credentials or secret values. Do not create, edit, or run new recipes or scripts yet, and do not install anything without my explicit approval of an exact proposal. This prompt authorizes read-only inspection only. Creating a tool later needs its own approved proposal.