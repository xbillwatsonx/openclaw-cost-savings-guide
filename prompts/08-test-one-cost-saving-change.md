# Prompt: Test One Cost-Saving Change

Copy this into your OpenClaw chat. It helps you propose, approve, apply, and fairly measure exactly one change.

---

**For my agent:** Read **The OpenClaw Cost Savings Runbook** at `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, especially **Sections 8, 9, and 10, Propose one change and wait for explicit approval, Apply the change and run the matched task, and Keep, revise, or roll back**, before acting. If the address still says `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/main/runbook/the-openclaw-cost-savings-runbook.md`, read the included local runbook at `../runbook/the-openclaw-cost-savings-runbook.md`; if that file is unavailable in your environment, ask me to provide it.

I want to test exactly one low-risk change and measure it fairly. Pick the top-ranked candidate from our review, or confirm the one I name, and present a proposal containing: the exact change, the evidence behind it, the expected effect and how it will be verified, what could go wrong, the exact rollback steps, and the matched task that will measure it. Then stop and wait.

After I explicitly approve that exact proposal, apply only that change, rerun the matched task with the same input, and record the before and after: tokens or allowance change, retries, tool calls, quality against the success criteria, elapsed time, and any cleanup. Use the measurement worksheet (worksheets/before-and-after-measurement.md), name whether each number is provider-reported usage, a recorded billed amount, or a local estimate, and treat the provider billing or plan-usage dashboard as the final authority. Then recommend keep, revise, or roll back based on the evidence.

This prompt authorizes no change yet. Nothing changes until I explicitly approve one exact proposal. Do not batch multiple changes, and do not prepare or pre-apply anything while waiting. If I reject the proposal, present the next candidate the same way. Destructive actions are out of scope entirely.