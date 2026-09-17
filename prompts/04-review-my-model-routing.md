# Prompt: Review My Model Routing

Copy this into your OpenClaw chat. It helps you check which work runs on premium models that does not need them.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, especially **Section 6, Identify candidate waste**, before acting. If the address still says `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, read the included local runbook at `../runbook/the-openclaw-cost-savings-runbook.md`; if that file is unavailable in your environment, ask me to provide it.

I want to know which of my work runs on premium models without needing that quality, what my fallback behavior is, and where attempt limits should stop weak workers from looping. Review my configured models and fallbacks, my active session selections, and the tasks that actually run against them, using read-only inspection.

For each candidate change, give me the evidence, the expected leverage, when it helps, when it may not (including tasks that genuinely need the premium tier), the effort and reversibility, and how I could verify it with a matched task. Label anything inferred as a hypothesis. Do not attach savings numbers or percentages.

Report what you checked, what you found, what still needs attention, and the next safe step.

Do not print credentials or secret values. Do not change models, fallbacks, routing, or configuration without my explicit approval of an exact proposal. This prompt authorizes read-only inspection only.