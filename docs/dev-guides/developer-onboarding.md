# Developer Onboarding

## First-Day Objective

Understand the current platform architecture before touching implementation.

Musahama is now:

- a unified workspace shell
- a shared platform kernel
- shared entity graphs for companies and contacts
- reusable capabilities
- solution modules
- paid data packs
- approval-gated external execution

It is not primarily a set of standalone `crm_opportunities`, `mandates`, `research`, and `results` top-level apps anymore.

## Required Read Order

1. `docs/architecture/overview.md`
2. `docs/authorization/authorization-foundation.md`
3. `docs/feature-system/module-catalog.md`
4. `docs/platform-runtime/runtime-plane.md`
5. `docs/database/source-of-truth-rules.md`
6. `docs/frontend/workspace-shell.md`
7. `docs/services/services-foundation.md`
8. `docs/dev-guides/documentation-discipline.md`

## First Implementation Checks

Before starting work:

1. confirm which module or platform area owns the change
2. confirm whether the change affects shared entities, runtime tables, or data packs
3. confirm whether the navigation model or module registry must change
4. confirm whether docs/specs must be updated in the same change

## Supabase Contract Discipline

If you change the database:

1. add a migration
2. apply it to the linked remote
3. sync `supabase/schema.sql`
4. regenerate `src/types/database.types.ts`
5. re-run validation

See:

- `database/CONTRACT.md`

## Rule of Thumb

If you are unsure where something belongs:

- platform-wide shell/runtime concern -> `src/platform/`
- data read/write concern -> `src/services/`
- solution-specific UI or manifest -> `src/modules/`
- shared data catalog concern -> `src/platform/data-packs/` plus DB catalog tables
