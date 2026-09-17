# The OpenClaw Cost Savings Guide

**A special early guide in the AgentHelpSite OpenClaw series**
**Edition:** Written against OpenClaw 2026.9.4. Version-specific details are labeled and should be rechecked against your installed docs before release.
**Version:** 0.1.1

**Status:** Public release.
**Companion runbook:** [The OpenClaw Cost Savings Runbook](../runbook/the-openclaw-cost-savings-runbook.md)

## 1. Start here

The fastest way to waste money on an AI agent setup is to optimize before you know how a run is billed. You can spend an evening shortening prompts, switching models, and trimming settings, then open your invoice and see the same number, because you never learned which runs create which cost, or whether the numbers you were watching were the numbers that mattered.

By the end of this guide you will be able to:

- identify your active provider, model, authentication route, and the authoritative usage record;
- tell the difference between subscription allowance, usage-based API billing, and local inference;
- record a small baseline with representative tasks before changing anything;
- route work by difficulty and value instead of sending everything to one premium model;
- replace repeated model reasoning with verified deterministic tools;
- teach your agent to prefer those tools and current prompting guidance;
- cut unnecessary context, output, retries, search, and fan-out;
- control sub-agents and recurring automations;
- make one low-risk change at a time and measure cost, quality, reliability, and cleanup;
- keep or roll back each change based on evidence.

You do not have to do any of this from memory. The companion runbook, [The OpenClaw Cost Savings Runbook](../runbook/the-openclaw-cost-savings-runbook.md), walks your agent through a safe, adaptive review of your actual setup. The [quick-start card](../runbook/quick-start-card.md) has the short version. The [prompts](#13-how-to-use-the-prompts) hand the runbook to your agent one step at a time.

Two promises up front. First, this guide never claims a fixed savings percentage. When something helps, it says when it helps, when it may not, and how to verify it. Second, nothing here asks you or your agent to change your live setup without your explicit approval. The review stays read-only until you approve one specific change.

## 2. Follow the money path

Every recommendation in this guide depends on one question: which cost path does this run consume? Answer that before anything else.

A provider is the company or service that supplies the model, for example OpenAI, Anthropic, or a local Ollama installation. The model name alone does not tell you what a run costs. The same model reference can consume three different cost paths depending on how the session is authenticated and where it runs.

### The three cost paths

| Path | How it works | What a cheaper run means here |
| --- | --- | --- |
| Subscription allowance | You connect an account whose provider allows plan-backed access. The connection may use OAuth, an authorization flow that avoids copying an API key, but OAuth alone does not prove the billing path. The provider decides whether the run uses a plan allowance. | The allowance lasts longer. The flat monthly price does not move. |
| Usage-based API billing | A provider charges for API use, commonly by tokens, the chunks of text a model reads or writes. An API key often selects this path, but the provider's pricing and account terms decide the charge. | Lower usage can lower the next bill. |
| Local inference | The model runs on your own hardware or a self-hosted server. There are no per-token charges, but you pay in hardware, electricity, time, and reliability instead. | Less load on your host, not a smaller invoice. |

Many setups mix these. A premium subscription model for hard work, a cheap API key for volume tasks, and a local model for private or offline jobs can all be live at once. That is fine. The trap is measuring one path while spending on another.

### How to see your route

Run these on a normal day, before changing anything. They are read-only.

| Command | What it shows |
| --- | --- |
| `openclaw status` | Gateway and session overview, including the active model and how the session is configured. |
| `/status` in chat | The session model, context usage, and the last response's usage details. |
| `/usage tokens` in chat | Token counts for a turn. |
| `/usage full` in chat | A compact usage footer with model and context details, and an estimated cost when local pricing is configured and the provider supplies usage data. |
| `openclaw status --usage` | Per-provider usage windows, shown as a percentage left. `openclaw channels list` shows the same windows in its output. |
| `/context list` and `/context detail` in chat | What is being injected into your prompt and how big it is. Covered in Section 7. |

Two cautions as of OpenClaw 2026.9.4. Subscription-style sign-in surfaces show tokens, not dollars, unless they supply compatible usage data plus an explicitly configured local price. OpenClaw can display provider-reported usage, recorded billed amounts, or a usage estimate, meaning cost calculated from available usage and pricing metadata. Treat the provider's own billing or plan-usage dashboard as the final authority.

A model can also be reachable through more than one authentication route. A subscription sign-in and an API key for the same provider are different cost paths even when the model name is identical. When you record a baseline, record the route, not just the model. The [setup and billing route worksheet](../worksheets/setup-and-billing-route.md) gives you a place to write it down.

**When this section helps:** always. **When it may not:** never, in the sense that skipping it invalidates everything after it. **How to verify:** run the commands above and compare them against your provider dashboard.

## 3. Measure before changing

Pick one to three representative tasks, real work you actually do, and define what success means for each before you touch anything. Then run each task once and record a baseline, the "before" measurement you will compare against later.

Record for each task:

- the task and its success criteria;
- the model and the cost path it consumed;
- tokens in and out, or the allowance change, when the surface shows them;
- retries and tool calls;
- completion quality against the criteria;
- elapsed time;
- any failure, repeated work, or cleanup you had to do.

The last two matter as much as the tokens. A change that saves tokens but produces work you have to redo has not saved anything. Quality loss, extra retries, and human cleanup are costs.

A matched task is the same task run before and after one change, with the same input, so the comparison is fair. Change one meaningful variable at a time. If you change the model, the prompt, and the schedule together and usage drops, you will not know which change did it, or whether one of them quietly made things worse.

The [before-and-after measurement worksheet](../worksheets/before-and-after-measurement.md) holds the fields. The runbook walks your agent through filling it.

**When this helps:** any time you plan to keep or roll back a change. **When it may not:** one-off tasks you will never repeat, where a baseline costs more than it returns. **How to verify:** rerun the matched task and compare the two records.

## 4. Route work by difficulty and value

Model routing is deciding in advance which class of model handles which class of work. It is usually the single highest-leverage cost change available, and OpenClaw makes it practical. The principle is simple: pay for premium judgment where judgment is needed, and stop paying for it everywhere else.

- Reserve premium models for hard judgment: architecture, final review of important work, high-risk changes, decisions with real consequences.
- Send bounded work to frugal models: extraction, formatting, summarizing, routine coding with clear acceptance criteria, repetitive operations where a wrong answer is cheap to catch.

"Bounded" is the load-bearing word. If a cheap model loops, retries, or produces work you must redo, the cheapest model becomes the most expensive one. So routing has a second half: a fallback, the next model OpenClaw tries when the current one fails, for example a rate limit, and explicit attempt limits so weak workers stop instead of grinding.

As of OpenClaw 2026.9.4, fallback behavior depends on where the model selection came from. A configured default can walk a configured fallback chain. An explicit session selection you made is strict: if it fails, OpenClaw reports the failure rather than silently answering from an unrelated model. Knowing which one you are using is part of routing.

When in doubt, compare the total cost of a run: model price, retries, and your cleanup time. A mid-priced model that finishes once often beats a cheap model that tries three times. And sometimes the cheapest option is no model at all. A script or a task-runner recipe (Section 5) or just doing it yourself can beat any delegation.

The [model routing policy template](../templates/model-routing-policy.md) turns this into a short written policy you can save and reuse.

**When this helps:** setups that lean on one premium model for everything, which is the most common waste pattern. **When it may not:** setups already routed deliberately, or single-model local installations where routing adds complexity without a cost difference. **How to verify:** record a baseline for a routed task, then the matched task after the change, including retries and quality.

## 5. Replace repeated reasoning with deterministic tools

Every time your agent re-derives a command from scratch, it spends tokens reasoning, searching, and possibly inventing flags that do not exist. A deterministic tool produces the same result every run without model judgment: a script, a validator, or a task-runner recipe. A task runner is a command tool such as `just`, `make`, or `Task` that stores named, verified commands in a file. A recipe is one of those named commands. A validator is a small program that checks a rule or format deterministically instead of asking a model to eyeball it.

The economy is simple. Creating and verifying a recipe costs one session of work. Every later session reads the recipe name and runs it. The reasoning is never paid for again, and the command is correct because you tested it.

`just` is the worked example in this guide because it is a small, widely available task runner with a readable file format. The principle is portable to `make`, `Task`, or documented shell scripts.

Turn a repeated operation into a recipe:

1. Check whether a working recipe already exists (`just --list` if you use just, or your runner's equivalent).
2. Verify the command's behavior from installed help or authoritative docs before trusting anything, including anything in this guide.
3. Name the recipe, give it a short description, and keep its parameters clear.
4. Tell your agent where the task runner lives and when to prefer it, in your instruction file, not in every prompt.
5. Verify the recipe with a small safe test before relying on it.

If a decision or format can be checked deterministically, use or write a validator instead of asking a model to judge it. Validation by model is a recurring cost. Validation by script is a one-time cost.

One optional extra: OpenClaw documents an external plugin called tokenjuice that compacts noisy command output after the command runs, without changing the command or its exit code. It is optional, it must be installed before it does anything, and installing it is a change to your setup. Treat installation as its own measured change using the same before-and-after method, after higher-leverage routing and deterministic-tool opportunities have been tested. Nothing in this guide or the runbook installs it for you.

The [deterministic tool inventory](../templates/deterministic-tool-inventory.md) helps you record what exists and what is worth converting.

**When this helps:** any operation you have watched the agent re-discover or re-reason more than twice. **When it may not:** one-off commands, or setups where the agent already has verified recipes for everything it repeats. **How to verify:** count how often the operation occurs in a week, then confirm the recipe produces the same result the raw command did.

## 6. Teach the agent how to use the setup

Deterministic tools do not save anything if the agent does not know they exist. Cheap runs also get expensive when instructions are vague and the agent must search to figure out what you want. Instruction design is cost control.

- Put stable rules where the agent always reads them, in your workspace instruction files, and supply task-specific details only with the task. A skill, a packaged instruction file the agent reads on demand when a task matches its description, is the natural home for procedure-sized guidance.
- Give exact paths and precise starting points. "Look at my backup script" is a search. "The script is at [exact path], it should exit 0, here is what it actually prints" is a task.
- Keep tool descriptions short and schemas strict when you configure custom tools. A tool's name tells the model what domain it is in, its description tells it when to use it, and a strict schema prevents malformed arguments that cost retries.
- Follow current model-specific prompting guidance for the models you actually run. Extract the durable rules into your instruction files. Do not paste a giant prompting manual into every request; that loads thousands of tokens to answer one question.
- Remove stale and duplicate instructions. Every rule you delete from an always-loaded file is saved on every future run, but test after deleting rules you relied on.

**When this helps:** immediately after you add a recipe, script, or policy. An undocumented tool is a tool the agent will not use. **When it may not:** over-instructing simple tasks. If the agent already does it right, leave it alone. **How to verify:** ask the agent to do a task that should use the recipe or rule, and watch whether it does.

## 7. Control context

A context window is the total text the model considers in one run: the system prompt, the skills list, conversation history, tool calls, and their results. A system prompt is the instruction block the model sees at the start of every run, including tool schemas, the skills list, and injected workspace files.

Context is not free. What loads on every run is what you pay for on every run. OpenClaw injects workspace bootstrap files, your always-loaded instruction files such as the agent and user instruction files, into the session at startup. As of OpenClaw 2026.9.4, each bootstrap file is capped at 20,000 characters, `USER.md` has its own smaller 4,000-character cap, and all bootstrap files together are capped at 60,000 characters. Content beyond a cap is truncated, not billed in full, but a large always-loaded file still crowds out useful context and pushes compaction sooner.

Start by looking instead of guessing. `/context list` shows what is injected and rough sizes. `/context detail` goes deeper: per-file sizes, per-tool schema sizes, per-skill entry sizes, system prompt size, and how much of the transcript is compactable. These two commands turn "my context feels heavy" into a ranked list of what to cut.

Practical reductions:

- Keep always-loaded files lean. Move reference material out of bootstrap files and into skills or docs the agent retrieves on demand.
- Keep skill descriptions short. As of OpenClaw 2026.9.4, the skills list costs a fixed base block plus about 97 characters per eligible skill before the name, description, and location fields are even counted, roughly 24 tokens per skill at about four characters per token. The list is also bounded by a configured skills prompt budget. Bulky descriptions add up on every single run.
- Retrieve targeted excerpts instead of pasting whole references, and externalize large logs and progress records to files instead of leaving them in history.
- Ask for concise reports by default and request depth only when needed. Cutting detail too far can hide failure signals, so keep the failure paths verbose.
- Treat compaction, summarizing older history so it takes less context space, as a measured tool, not free work. It uses model effort too. Check whether it actually reduces later usage enough to justify it.
- Lower image sizes if your runs attach many screenshots. As of OpenClaw 2026.9.4 the default image cap is 1200 pixels on the longest side; lowering it usually reduces vision-token usage on screenshot-heavy runs.
- Start a fresh session when history is stale instead of paying for irrelevant conversation on every turn.

**When this helps:** runs where `/context detail` shows large always-loaded files, a long skills list, or heavy history. **When it may not:** lean setups that already pass these checks. **How to verify:** rerun `/context list` after the change and rerun a matched task to confirm quality did not drop.

## 8. Regulate sub-agents

A sub-agent is a child session your agent can spawn for a slice of work. Each sub-agent has its own context and token usage by default, so fan-out, spawning many sub-agents at once, multiplies cost in a very direct way: each child loads instructions, reasons, calls tools, and writes output, and then you pay again to review what came back.

Fan-out is a budget decision, not a default. Use a sub-agent when isolation, parallelism, or specialist work adds real value:

- one agent, one narrow task slice, one deliverable, one acceptance target;
- pass a small briefing pack, not your whole conversation history;
- require a structured hand-off: summary, deliverable path, what changed, validation steps, risks, next step;
- do not assign several agents to duplicate the same research without a reason;
- stop weak or looping workers early. Sending `/stop` in the requester chat aborts your session's work and cancels its active child tree, and reports how many children actually stopped.

OpenClaw ships limits you can inspect and, with approval, tune. As of OpenClaw 2026.9.4, sub-agent defaults are: 8 concurrent child runs across the gateway, 5 active children per session (range 1 to 20), nesting depth of 5 (range 1 to 5), no run timeout unless you configure one, and completed child state archived after 60 minutes. You can also set a cheaper default model for sub-agents so routine child work does not inherit the premium parent model.

Two behaviors worth knowing, both as of 2026.9.4. Rolling-history tool-loop detection, a guard that watches for repetitive tool-call patterns, is disabled by default; a separate post-compaction guard stays active unless you explicitly disable the whole setting. Do not change either merely because it exists. And an accepted child keeps running after its parent finishes, so "the parent replied" does not mean "the fan-out is over."

The [sub-agent budget checklist](../templates/sub-agent-budget-checklist.md) turns this into a per-spawn decision.

**When this helps:** orchestrations that spawn workers by habit, duplicate research, or lose track of running children. **When it may not:** genuinely parallel work with narrow slices and clear deliverables, where fan-out is the right tool. **How to verify:** compare the total cost of an orchestration against doing the same job directly or deterministically.

## 9. Make recurring work cheaper

An automation, called a cron job in OpenClaw, is a scheduled or event-driven job that can start an agent turn or run a command without you present. Recurring jobs are where silent waste compounds: a job that runs a model when a script would do, every hour, costs you every hour.

The biggest lever is determinism. If a recurring job needs no model judgment, it should not use a model. OpenClaw can run a command job that executes a shell command and records the result without starting a model run at all. Health checks, backups, cleanups, and data pulls usually belong here. The agent gets involved only when a check fails and the output needs interpretation.

When a job does need an agent turn, keep it small:

- Use a thin launcher: a short scheduled prompt that hands off to a maintained skill or script, instead of carrying the full instructions in the schedule itself.
- Keep bootstrap context empty for isolated recurring jobs with `--light-context` so each run does not reload your whole workspace. As of 2026.9.4 this applies to isolated agent-turn jobs.
- Prefer an event-driven trigger, a job that runs because something happened instead of on a fixed schedule, when the underlying event is detectable. Polling on a timer to detect a change is the expensive way.
- Do not poll the agent in a loop to wait for background work. Check status on demand when you actually want it.
- Keep retries bounded. As of OpenClaw 2026.9.4, recurring jobs back off after consecutive errors at 30 seconds, then 1, 5, 15, and 60 minutes, and return to normal after the next successful run. Do not widen that into a retry storm.
- Use quiet success. OpenClaw supports a silent reply token, `NO_REPLY` or `no_reply`, that tells the delivery layer not to post anything. A maintenance job that only speaks when it finds a problem is cheaper to run and easier to live with.
- Know that a pinned cron model is strict. As of OpenClaw 2026.9.4, a job pinned to a model uses that model, and when no fallback list is configured, your agent's default model is not silently added as a hidden retry target. A pinned job fails loudly rather than quietly spending elsewhere.
- Local models get a preflight probe. For local providers, the scheduler checks whether the endpoint is reachable first and records the run as skipped when it is not, so you do not pay for model calls into a dead server.

A cron model pin, a delivery flag, or a schedule change is still a change to your live setup. The runbook inspects first and proposes; you approve.

**When this helps:** any schedule that fires a model when a command would do, or fires often into an empty result. **When it may not:** jobs that genuinely need judgment each run. **How to verify:** list your automations with their delivery settings and ask which ones could be command jobs.

## 10. Reliability is cost control

Everything in this section is also a cost practice, because failures are billed too: retries, repeated discovery, and your cleanup time all show up in usage.

- Verify commands before instructing. If you or your agent has not run a command or checked its `--help` in your installed version, it is not verified yet, including commands from this guide.
- Define success before execution, for every task you baseline and every recipe you trust.
- Capture evidence once, in a file the agent can find later, so future sessions do not re-derive what you already learned.
- Checkpoint long jobs so a late failure does not restart the whole run.
- Stop after the first sufficient result unless validation explicitly requires more.
- Prefer preflight checks, validators, and tests over model judgment for anything deterministic (Section 5).

**When this helps:** always, slowly, compounding. **When it may not:** never. **How to verify:** track how often you re-solve the same problem; each repeat is unpriced waste you just found.

## 11. Build a personal cost policy

Decisions made once, in writing, are cheaper than decisions made in every prompt. End your review by writing a short policy and saving it where your agent reads it:

- which model classes handle which work, and what requires the premium tier;
- what your agent must ask approval for;
- when to delegate, and the per-spawn budget (Section 8);
- maximum retries and fan-out per task class;
- required verification for each class of change;
- where your task runner, recipes, scripts, validators, and prompting guidance live;
- when you will review usage again, a date you actually keep.

The [model routing policy template](../templates/model-routing-policy.md) is the starting point. Keep the policy short enough that you will follow it. A policy you ignore is context you pay to load and never use.

## 12. Bonus for Astra Users: Two Ideas You Can Use Right Away

This guide owes a debt to the creator Dubibubi, whose video ["Never Hit Codex Usage Limits Again"](https://youtu.be/u_yvc7NTYvI?si=k5YD5azJEC9TS98K) (published 2026-09-16) inspired two of the practices above. Thank you for the concrete, practical breakdown.

Here, Astra refers to the model and audience discussed in that ChatGPT Work and Codex subscription video. If you use a different provider or cost path, adapt the principles and skip the subscription-specific details.

Get the framing right before borrowing anything: the video is about making a ChatGPT Work and Codex subscription allowance last longer. OpenAI's own documentation confirms that Work and Codex share one usage allowance with two windows, a 5-hour window and a weekly window, and that a new 5-hour window starts at your first message after the previous one ends. Shorter, better-targeted runs make that allowance last longer. This has nothing to do with usage-based API billing, where the same techniques lower a token bill instead. The creator's reported savings percentages are his own measurements, not verified claims, so this guide repeats none of them as promises.

The two ideas below are adapted from the video's approach. The on-screen prompt text was not available to this project, so the prompts here are original wording built on the ideas, not copies.

### Idea 1: Give the exact starting point, not a search

The cheapest run is one that does not have to find anything. Instead of describing a problem and letting the model search your setup for a cause, hand it the precise component, the expected behavior, the actual behavior, and the likely file. You pay for the fix, not the hunt.

Adapted prompt (original wording):

> Component: [what you are working on]. Expected: [what should happen]. Actual: [what happens instead]. Likely file: [exact path, if you know it]. Fix [this one thing] and leave everything else unchanged.

This is verified in the sense that it removes search and retry work from the run. Whether it helps you depends on how much of your current usage is discovery. Check your last few "fix this" conversations for how many turns happened before the agent even reached the right file.

### Idea 2: Ask for the shortest sufficient result, and route bounded routine work down

Two habits in one idea. First, tell the agent to stop at the first sufficient result. Second, send bounded routine work to a cheaper model or a narrowly scoped sub-agent instead of a premium one. This is Sections 4 and 8 in practice, and it pairs with the claim in the video that the model can see its own usage limits, a claim this project could not verify in official documentation, so treat it as unverified.

Adapted prompt (original wording):

> Use at most one retrieval step unless it is insufficient. Stop after the first sufficient result. Report a short summary: what changed, deliverable path, validation steps, risks, next step. Do not redo work outside your slice.

Both ideas are cheap to try and easy to measure with the [before-and-after worksheet](../worksheets/before-and-after-measurement.md): record a real task done your current way, then the same task with the adapted prompt, and compare turns, tokens, and quality.

## 13. How to use the prompts

Open the [companion runbook](../runbook/the-openclaw-cost-savings-runbook.md) first, then copy one prompt at a time into your OpenClaw chat. Each prompt tells your agent which runbook section to read before it acts, states what the step is for, and keeps the work read-only until you approve a specific change. Let the agent finish and report before moving to the next prompt.

**Runbook address:** `https://raw.githubusercontent.com/xbillwatsonx/openclaw-cost-savings-guide/v0.1.1/runbook/the-openclaw-cost-savings-runbook.md`

| Prompt | What it helps you do | Runbook section |
| --- | --- | --- |
| [Explain my cost path](../prompts/01-explain-my-cost-path.md) | Learn which cost path your runs consume. | Section 3, Identify the setup and the money path |
| [Audit my cost patterns](../prompts/02-audit-my-openclaw-cost-patterns.md) | Get an evidence-based inventory and waste candidates. | Sections 5 and 6 |
| [Find deterministic tool opportunities](../prompts/03-find-deterministic-tool-opportunities.md) | Find repeated reasoning a tool could replace. | Sections 5 and 6 |
| [Review my model routing](../prompts/04-review-my-model-routing.md) | Check premium use, fallbacks, and attempt limits. | Section 6 |
| [Review my context load](../prompts/05-review-my-context-load.md) | See what is always loaded and what to lean out. | Section 6 |
| [Review my sub-agent controls](../prompts/06-review-my-sub-agent-controls.md) | Check limits, fan-out, and hand-offs. | Section 6 |
| [Review my automations](../prompts/07-review-my-automations.md) | Find model work that should be deterministic. | Section 6 |
| [Test one cost-saving change](../prompts/08-test-one-cost-saving-change.md) | Propose, approve, apply, and measure one change. | Sections 8, 9, and 10 |

## 14. Glossary

The same glossary lives at [glossary.md](../glossary.md) so the runbook, prompts, and worksheets share it.

| Term | What it means |
| --- | --- |
| Agent | The OpenClaw assistant that can inspect your setup and, with your approval, work on it. |
| Usage-based API billing | A cost path where a provider charges API activity, often by tokens and commonly through an API key. The provider's pricing terms are authoritative. |
| Automation | A scheduled or event-driven OpenClaw job that can start an agent turn or run a command without you present. Also called a cron job. |
| Baseline | A recorded "before" measurement of a representative task, taken before any change. |
| Bootstrap files | Workspace instruction files OpenClaw injects into the session prompt at startup, such as the agent and user instruction files. |
| Compaction | Summarizing older conversation history so it takes less context space. It uses model effort itself, so it is not free. |
| Context window | The total text the model considers in one run: system prompt, skills list, history, tool calls, and results. |
| Deterministic tool | A script, validator, or task-runner recipe that produces the same result every run without model judgment. |
| Event-driven trigger | A job that runs because something happened, such as a webhook, instead of on a fixed schedule. |
| Fallback | The next model OpenClaw tries when the current model fails, for example a rate limit. |
| Fan-out | Spawning many sub-agents at once for the same job. |
| Gateway | The OpenClaw process that runs the agent, manages sessions, and connects channels. |
| Local inference | Running models on your own hardware or a self-hosted server instead of a paid cloud API. Cost shifts to hardware, power, and time. |
| Matched task | The same task run before and after one change, with the same input, so the comparison is fair. |
| Model routing | Deciding in advance which class of model handles which class of work. |
| OAuth | An authorization flow that lets OpenClaw connect to a provider account without copying an API key. Whether that connection uses a subscription allowance depends on the provider and plan. |
| Provider | The company or service that supplies the model, such as OpenAI, Anthropic, or a local Ollama installation. |
| Quiet success | A job that finishes without posting a message unless it finds a problem. |
| Recipe | One named, verified command in a task-runner file. |
| Skill | A packaged instruction file the agent reads on demand when a task matches its description. |
| Subscription allowance | A provider plan's usage budget, often measured in windows or other limits rather than per-token dollars. |
| System prompt | The instruction block the model sees at the start of every run, including tool schemas, the skills list, and injected workspace files. |
| Task runner | A command tool such as `just`, `make`, or `Task` that stores named, verified commands in a file. |
| Thin launcher | A short scheduled prompt that hands off to a maintained skill or script instead of carrying the full instructions itself. |
| Token | The chunk of text a model reads or writes. Usage is measured in tokens. |
| Tokenjuice | An optional external OpenClaw plugin that compacts large command output after the command runs, without changing the command or its exit code. |
| Usage estimate | A cost figure OpenClaw calculates from available usage and pricing metadata. It may differ from the provider's final bill. |
| Usage window | The period a subscription allowance covers before it resets. |
| Validator | A small program that checks a rule or format deterministically instead of asking a model to judge it. |

## 15. Sources and version note

- Installed OpenClaw documentation, version 2026.9.4, for every command, default, and behavior labeled "as of" in this guide. OpenClaw changes between versions, so recheck these against your installed docs and `--help` output before relying on them.
- OpenAI Help Center documentation on ChatGPT Work and Codex usage, for the subscription allowance windows described in the bonus section.
- Dubibubi, ["Never Hit Codex Usage Limits Again"](https://youtu.be/u_yvc7NTYvI?si=k5YD5azJEC9TS98K), for the two adapted ideas, clearly labeled where creator-reported claims are unverified.
- The series research records behind this package, summarized in [RESEARCH-EVIDENCE.md](../RESEARCH-EVIDENCE.md).

This package never promises a fixed savings percentage. Provider pricing, plan allowances, model availability, and OpenClaw defaults all change without notice. Measure your own setup, make one change at a time, and keep what the evidence supports.