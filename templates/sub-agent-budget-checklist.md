# Checklist: Sub-Agent Budget

**Purpose:** make every spawn a deliberate budget decision instead of a habit. Each sub-agent has its own context and token usage, so fan-out multiplies cost: instructions, reasoning, tools, output, and your review time.

Use this checklist per spawn. It pairs with the [model routing policy](model-routing-policy.md).

## Before spawning

- [ ] Real value: does this need isolation, parallelism, or specialist work?
- [ ] A deterministic tool, an existing recipe, or direct work would not be cheaper.
- [ ] One narrow task slice, not "help me with this project."
- [ ] One deliverable named up front.
- [ ] One acceptance target I can check.
- [ ] Briefing pack prepared: the slice, the context it needs, the deliverable format. Not raw conversation history.
- [ ] Child model chosen: cheaper than the parent where quality allows.
- [ ] Limits decided: how many children, how many total attempts, and a run timeout.
- [ ] Not duplicating another worker's research without a reason.

## While running

- [ ] No polling loops. Check status on demand, when I actually want it.
- [ ] Weak or looping workers stopped early. `/stop` in the requester chat aborts session work and cancels the active child tree, and reports how many children actually stopped.

## Hand-off received

Every child report must contain all six:

- [ ] summary
- [ ] deliverable path
- [ ] what changed
- [ ] validation steps
- [ ] risks
- [ ] next step

## After

- [ ] Did the result justify the cost? Write the answer down, honestly, one line.
- [ ] If no: note what to do differently next time, or whether to stop spawning for this task class entirely.