# Glossary

Plain definitions shared across this package. This file mirrors the glossary section in [the guide](guide/the-openclaw-cost-savings-guide.md) so the runbook, prompts, and worksheets use one term and one definition per concept.

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