# Services Foundation

## Purpose

The `src/services/` layer is the backend-facing application layer for Musahama.

It exists so pages and UI components do not scatter direct Supabase access across the codebase.

## Core Rule

If code assembles or mutates domain data, it belongs in `src/services/` or a clearly platform-scoped server helper.

Use:

- `src/services/` for data access and mutations
- `src/platform/` for shared platform orchestration
- `src/platform/modules/` for module registry and summaries
- `src/modules/` for module manifests and module-owned UI composition

## What Services Own

Services own:

- Supabase queries and writes
- DTO shaping
- server-only data assembly
- normalized read models
- mutation helpers
- shared domain helpers

## What Services Do Not Own

Services do not own:

- sidebar rendering
- active-nav decisions
- entitlement presentation rules
- page composition
- final database enforcement

Those belong to:

- module registry and shell code
- UI components
- feature-system or platform orchestration
- RLS

## Current Service Domains

Major current domains include:

- `auth`
- `billing`
- `companies`
- `contacts`
- `integrations`
- `notifications`
- `organizations`
- `research`
- `results`
- `supabase`

Cross-module orchestration that is not tied to one domain increasingly lives under:

- `src/platform/`

## Developer Rule

When adding new functionality:

1. place raw reads and writes in a service or platform server helper
2. shape a stable return object for UI consumers
3. keep page components focused on composition, not data plumbing
4. avoid `as any` query shortcuts when the contract can be typed cleanly
