# Changelog

## 0.1.1, 2026-09-17

- Removed the stale draft banner from the approved CC BY 4.0 license.
- Removed stale draft wording from the published guide.
- Repaired the local-runbook fallback sentence in all eight prompts.
- Pinned prompt and guide runbook links to the immutable v0.1.1 release.

## 0.1.0, 2026-09-17

- Published the first public release of the OpenClaw Cost Savings Guide and companion runbook.
- Replaced every release placeholder with the fixed public runbook URL.
- Completed technical, factual, privacy, link, prompt, terminology, punctuation, and persona validation.
- Approved the CC BY 4.0 license.

## 2026-09-17, accuracy and validation refinement

- Refined OAuth and billing-path language so authentication is not treated as proof of billing.
- Distinguished provider-reported usage, recorded billed amounts, and local usage estimates.
- Strengthened all eight prompt boundaries to require explicit approval of an exact proposal before changes.
- Standardized cost-path terminology and added the `USER.md` bootstrap-cap exception.
- Corrected evidence attributions and refreshed the validation record.
- Added non-shipping deterministic package validation through the project justfile.
- Improved the draft prompts' direct local-runbook fallback and clarified the beginner prompt flow.
- Added measured-change guidance for optional tokenjuice use, a token-only billing warning, and Astra audience context after persona validation.

## 2026-09-17: First complete draft

- Created the full first-draft package defined by the frozen specification: guide, companion runbook, quick-start card, two worksheets, three templates, eight prompts, glossary, research evidence, validation plan, changelog, and license.
- The companion runbook is unnumbered. The existing five-runbook series numbering is unchanged.
- All version-specific OpenClaw facts were verified against the installed OpenClaw 2026.9.4 documentation during drafting.
- Three claims from the research packet could not be confirmed in the installed docs (a default of 1 for maximum concurrent cron runs, a default of 3 for cron retry attempts, and a `/subagents kill` command surface). They are excluded from reader-facing content and recorded in RESEARCH-EVIDENCE.md.
- Every prompt included the local runbook bridge (`../runbook/the-openclaw-cost-savings-runbook.md`), the relevant runbook section, a read-first instruction, purpose, expected behavior, a release URL placeholder, and the prohibition on changes without explicit approval.
- At this first-draft checkpoint, the package was ready for parent factual, structural, privacy, and mechanical review.