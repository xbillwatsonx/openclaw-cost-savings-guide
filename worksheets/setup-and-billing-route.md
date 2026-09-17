# Worksheet: Setup and Billing Route

**Purpose:** record which cost path each part of your setup consumes. Fill this in with your agent during Section 3 of the [companion runbook](../runbook/the-openclaw-cost-savings-runbook.md), then keep it with your cost policy.

**Never record secret values on this sheet.** For the authoritative usage record, write the name of the provider dashboard page (for example, "provider usage page"), not a link containing tokens or credentials.

## Basics

- Date:
- OpenClaw version: (from `openclaw --version`)
- Filled in with agent: yes / no

## Providers and routes

One row per provider in use. If you do not know a value, write "unknown" rather than guessing.

| Provider | Active model | Authentication route (API key, OAuth or account sign-in, or local) | Verified cost path (subscription allowance, usage-based API billing, or local inference) | Usage surface available | Authoritative record |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Notes per provider

For each provider above, answer briefly:

- Does the usage surface show tokens only, or tokens plus an estimated cost?
- Which numbers here are local estimates, and which come from the provider's own dashboard?
- Any known mismatch between what OpenClaw shows and what the provider reports? (worth rechecking at the next review)

## Mixed setups

If one model name is reachable through more than one authentication route, list each route separately:

| Model | Route 1 | Route 2 (if any) |
| --- | --- | --- |
|  |  |  |

## Unknowns and follow-ups

-
