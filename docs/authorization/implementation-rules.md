# Authorization Implementation Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Give developers a strict implementation contract for authorization.

---

## 2. Folder Ownership

### `feature-system/`
Use for:
- role matrix
- module rules
- feature rules
- runtime resolvers
- capability hooks

### `features/`
Use for:
- page/module UI
- module-specific components
- forms
- views

### `services/`
Use for:
- Supabase access
- membership reads
- module reads
- feature entitlement reads
- provider/integration reads

### `views/`
Use for reusable presentation layouts only.

---

## 3. Required Frontend Structure

```text
src/
  feature-system/
    catalog/
    permissions/
    resolver/
    runtime/
