# Service Directory Map

## Purpose

This page defines the current recommended shape of the application service layer.

It reflects the platform transition from one workflow-heavy product into:

- shared platform services
- shared entity services
- retained origination workflow services

## Recommended Structure

```text
src/
  platform/
    approvals/
    dashboard/
    data-packs/
    modules/

  services/
    activity/
    auth/
    automations/
    billing/
    companies/
    contacts/
    credits/
    enrichment/
    integrations/
    msm/
    notifications/
    organizations/
    platform-admin/
    research/
    results/
    sdp/
    supabase/
    support/
```

## Folder Responsibility

### `src/platform/`

Use for cross-module platform concerns such as:

- module registry
- platform dashboards
- approvals
- data-pack summaries
- cross-module runtime views

### `src/services/`

Use for domain-level data access and mutations such as:

- auth/session helpers
- recent work and activity surfaces
- workspace automation runtime
- companies and contacts
- enrichment jobs and enrichment audit records
- organization membership
- integrations
- billing
- credit wallet, ledger, quotes, and operation costs
- platform admin controls and support preview
- Supplier Development Program
- Musahama Strategy Management
- support bug-report intake
- retained origination workflow reads and writes

## Naming Rule

Use:

- kebab-case files
- verb-first names for loaders and mutations
- one clear responsibility per file

Examples:

- `list-companies.ts`
- `get-workspace-bootstrap.ts`
- `list-approval-requests.ts`
- `get-data-packs-overview.ts`

Avoid:

- `helpers.ts`
- `misc.ts`
- `doEverything.ts`

## Current Transition Rule

The origination flow still has operational services under the legacy workflow domain folders.

That is acceptable during the bridge, but new cross-module runtime logic should prefer the shared platform/runtime model instead of inventing another workflow-specific service tree.
