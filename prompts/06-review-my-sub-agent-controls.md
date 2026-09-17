# Prompt: Review My Sub-Agent Controls

Copy this into your OpenClaw chat. It helps you check whether your sub-agent use is deliberate or habit.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, especially **Section 6, Identify candidate waste**, before acting. If the address still says `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, read the included local runbook at `../runbook/the-openclaw-cost-savings-runbook.md`; if that file is unavailable in your environment, ask me to provide it.

I want to know whether my sub-agent use is a deliberate budget decision or an expensive habit. Review my sub-agent patterns read-only: what gets spawned and why, how narrow the slices are, whether hand-offs are structured, how far fan-out goes, and which limits are configured. Check the defaults I rely on against my installed version's documentation before quoting them.

For each candidate change, give me the evidence, the expected leverage, when it helps, when it may not (including genuinely parallel work with clear deliverables), the effort and reversibility, and how I could verify it. Label anything inferred as a hypothesis. Do not attach savings numbers or percentages.

Report what you checked, what you found, what still needs attention, and the next safe step.

Do not print credentials or secret values. Do not spawn, cancel, or reconfigure agents or sessions as part of this review, and do not change configuration without my explicit approval of an exact proposal. This prompt authorizes read-only inspection only.