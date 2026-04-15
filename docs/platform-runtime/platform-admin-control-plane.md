# Platform Admin Control Plane

## Purpose

The platform admin area is an internal operator surface for global support, audit, billing-credit control, data inspection, and rollout management.

It is not a workspace module. It is protected by platform roles and should remain separate from organization-scoped workspace settings.

## Canonical Route Family

Platform admin routes live under:

- `/platform-admin`

Current areas include:

- organizations
- new organization creation
- users
- entitlements
- solutions
- integrations
- data sources
- billing credits
- operations
- monitoring
- audit support
- audit recovery
- delivery QA
- data explorer

## Access Model

Platform admin access depends on platform role, not workspace membership alone.

Support preview and impersonation are read-only support tools. They must record a reason and must be clear in the workspace shell when active.

## Audit Model

Global mutations and support actions must be auditable.

Current audit and control concepts include:

- `god_audit.mutation_events`
- global platform solution/provider/dataset policies
- rollout batches
- shared integrations
- support preview sessions

## Implementation References

Primary implementation files:

- `app/(platform-admin)/platform-admin`
- `src/services/platform-admin/god-mode.ts`
- `src/services/platform-admin/god-global-control.ts`
- `src/services/platform-admin/impersonation.ts`
- `src/services/platform-admin/delivery-ops.ts`

Database setup:

- `supabase/migrations/20260407103000_add_god_mode_control_plane.sql`
- `supabase/migrations/20260407143000_expand_god_global_control.sql`

