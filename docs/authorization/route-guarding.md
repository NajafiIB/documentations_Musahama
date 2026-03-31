# Route Guarding

## Current Protected Workspace Routes

Primary workspace routes:

- `/dashboard`
- `/approvals`
- `/activity`
- `/origination-match`
- `/origination-match/mandates`
- `/origination-match/research`
- `/origination-match/results`
- `/supplier-development-program`
- `/supplier-development-program/cases`
- `/supplier-development-program/cases/[caseId]`
- `/supplier-development-program/catalog`
- `/partner-match`
- `/negotiator`
- `/compliance-guardian`
- `/funding-orchestrator`
- `/companies`
- `/companies/[id]`
- `/contacts`
- `/contacts/[id]`
- `/settings/integrations`
- `/settings/integrations/[providerKey]`
- `/settings/data-sources`
- `/settings/plan-billing`
- `/settings`
- `/settings/workspace`
- `/settings/solutions`
- `/settings/usage`
- `/settings/account`
- `/settings/view-standard`
- `/settings/delivery-orchestrator`
- `/onboarding`
- `/select-organization`

Compatibility routes that still exist:

- `/mandates`
- `/mandates/[id]`
- `/mandates/[id]/strategies/[strategyId]`
- `/research`
- `/research/[id]`
- `/research/search`
- `/results`
- `/results/[id]`
- `/integrations`
- `/integrations/[providerKey]`
- `/data-packs`
- `/billing`

## Guarding Rule

A route is protected when it requires:

- session resolution
- current organization resolution
- active membership
- module availability where applicable

## Active-Navigation Rule

Compatibility routes should still resolve to the correct active module in the shell.

Most importantly:

- `/mandates`
- `/research`
- `/results`
- `/integrations`
- `/data-packs`
- `/billing`

should activate:

- `Origination Match`
- `Integrations`
- `Data Packs`
- `Billing`
