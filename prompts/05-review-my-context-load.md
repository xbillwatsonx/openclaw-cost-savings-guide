# Prompt: Review My Context Load

Copy this into your OpenClaw chat. It helps you see what is always loaded into your context and what is worth leaning out.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/v0.1.1/runbook/the-openclaw-cost-savings-runbook.md`, especially **Section 6, Identify candidate waste**, before acting. If you cannot access that address, ask me to provide the included local runbook file at `../runbook/the-openclaw-cost-savings-runbook.md`.

I want to see what is always loaded into my context on every run, and what is worth trimming. Use `/context list` and `/context detail`, and read-only inspection of my instruction files and skills, to report: injected file sizes and any truncation, the skills list and its description lengths, heavy history or images, and tool schema sizes.

For each candidate reduction, give me the evidence, the expected leverage, when it helps, when it may not (including rules I actually rely on), and how I could verify quality does not drop with a matched task. Label anything inferred as a hypothesis. Do not attach savings numbers or percentages.

Report what you checked, what you found, what still needs attention, and the next safe step.

Do not print credentials or secret values. Do not edit instruction files, skills, or configuration without my explicit approval of an exact proposal. This prompt authorizes read-only inspection only.