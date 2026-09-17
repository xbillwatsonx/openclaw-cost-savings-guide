# Prompt: Explain My Cost Path

Copy this into your OpenClaw chat. It helps you learn which cost path your runs consume before you change anything.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, especially **Section 3, Identify the setup and the money path**, before acting. If the address still says `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, read the included local runbook at `../runbook/the-openclaw-cost-savings-runbook.md`; if that file is unavailable in your environment, ask me to provide it.

I want to understand how my usage is actually billed before I try to save anything. Identify my installed version, my provider or providers, my active model, my authentication route for each provider (API key, OAuth or account sign-in, or local), and where my usage is recorded. Do not assume authentication alone proves billing. Verify which runs consume subscription allowance, which consume usage-based API billing, and which use local inference. Name whether each number is provider-reported usage, a recorded billed amount, or a local estimate, and identify the provider dashboard that is authoritative.

Report what you checked, what you found, what still needs attention, and the next safe step. Offer to fill in the setup and billing route worksheet (worksheets/setup-and-billing-route.md) with me.

Do not print credentials or secret values. Do not change files, configuration, models, providers, automations, plugins, or settings without my explicit approval of an exact proposal. This prompt authorizes read-only inspection only.