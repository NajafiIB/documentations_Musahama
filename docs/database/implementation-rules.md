# Database Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers strict rules for working with the database.

---

## 2. Service Boundary Rule

Pages must not scatter direct Supabase queries.

Use:
- services/ for reads and writes
- feature-system/ for capability access/runtime truth
- server-side reads for sensitive data, org bootstrap, and runtime resolution

---

## 3. Supabase Client Rule

Use centralized clients only:
- services/supabase/client.ts
- services/supabase/server.ts
- services/supabase/middleware.ts

Do not initialize random clients throughout page components.

---

## 4. Mutation Rule

Every write helper must automatically apply required ownership/audit fields where appropriate:
- organization_id
- created_by_user_id
- updated_by_user_id

This logic must not depend on forms remembering to pass everything correctly.

---

## 5. Sensitive Data Rule

These must stay server-only or sanitized:
- organization_integrations.secret_ref
- provider auth config
- secret-like values in global_config
- billing/provider internals

---

## 6. Transitional Data Rule

Do not build final UI around transitional JSON analysis fields in `research_results`.

Use normalized analysis tables instead.

---

## 7. Naming Rule

Keep these distinct:
- module keys: snake_case
- routes: kebab-case
- features: dot-separated capability names
- database table names: existing canonical table names

Example:
- module = results
- route = /results
- workflow table = research_results

They do not need to match exactly.

---

## 8. Change Rule

Any schema change must update:
- migration SQL
- docs/database/*
- related docs/auth or docs/authorization if affected
- service contracts if affected

No schema change is complete without documentation update.

---

## 9. Final Rule

If a developer asks where logic belongs:
- data fetch/mutation -> services/
- capability decision -> feature-system/
- security enforcement -> RLS + services
- final canonical data display -> canonical entity/analysis tables
