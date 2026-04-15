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
- `/supplier-development-program/cases/new`
- `/supplier-development-program/cases/[caseId]`
- `/supplier-development-program/cases/[caseId]/preview`
- `/supplier-development-program/catalog`
- `/supplier-development-program/settings`
- `/supplier-development-program/owner`
- `/musahama-strategy-management`
- `/musahama-strategy-management/owner`
- `/musahama-strategy-management/launch`
- `/musahama-strategy-management/plan/[planId]`
- `/negotiator`
- `/compliance-guardian`
- `/funding-orchestrator`
- `/companies`
- `/companies/[id]`
- `/contacts`
- `/contacts/[id]`
- `/settings/integrations`
- `/settings/integrations/[providerKey]`
- `/settings/automations`
- `/settings/automations/[automationId]`
- `/settings/data-sources`
- `/settings/plan-billing`
- `/settings`
- `/settings/workspace`
- `/settings/solutions`
- `/settings/usage`
- `/settings/account`
- `/settings/credit-admin`
- `/settings/delivery-orchestrator`
- `/onboarding`
- `/select-organization`

GOD-only platform-admin routes:

- `/platform-admin/view-standard`

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
