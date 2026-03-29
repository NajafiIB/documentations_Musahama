# Frontend Foundation

## Purpose

This document defines the current frontend architecture of the Musahama platform.

It is centered on the live unified workspace model, not the older workflow-first navigation.

## Core Rules

The frontend is built around:

- one permanent workspace shell
- one canonical module registry
- one grouped navigation model
- one shared UI primitive system
- one disciplined service boundary

## Current Workspace Areas

The official top-level areas are:

- `dashboard`
- `approvals`
- `activity`
- `origination_match`
- `partner_match`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`
- `companies`
- `contacts`
- `integrations`
- `data_packs`
- `billing`
- `settings`

Legacy visible routes still exist for compatibility:

- `/mandates`
- `/research`
- `/results`

The older `crm_opportunities` concept remains in the legacy catalog, but it is not currently an active workspace route.

## Ownership Boundaries

### `app/`

Owns:

- route groups
- layouts
- page entrypoints
- route params

### `src/components/`

Owns:

- shared UI primitives
- shell components
- table/list primitives
- cross-module presentation pieces

### `src/platform/`

Owns:

- module registry
- platform-level dashboards
- approvals
- activity
- data-pack summaries
- cross-module shell helpers

### `src/modules/`

Owns:

- solution-module manifests
- module-specific pages
- module-specific summary logic

### `src/services/`

Owns:

- data reads and writes
- DTO shaping
- Supabase access
- server-only query assembly

### `src/hooks/`

Owns:

- thin reusable state helpers
- persistent UI preferences
- composable client hooks

## Security Rule

The frontend is not the security boundary.

It may hide, disable, or group UI, but real enforcement must still come from:

- auth/session resolution
- organization context
- module enablement
- entitlement checks
- RLS

## Data Rule

Final UI should prefer normalized shared entities and runtime tables over ad hoc JSON blobs.

Examples:

- companies and contacts pages should read shared entity shapes
- approvals should read `module_action_requests`
- module summaries should read shared runtime state when available

## Developer Rule

When building new frontend functionality:

- add or update a module manifest first if navigation changes
- keep shared primitives in `src/components/ui`
- keep cross-module logic in `src/platform`
- keep module-specific UI in `src/modules` or the route area that owns it
- do not create a second manual navigation or entitlement system
