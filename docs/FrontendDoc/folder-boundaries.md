```md
# Folder Boundaries

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define what each major frontend folder is allowed to own.

This exists to stop the codebase from turning into a pile of mixed responsibilities.

---

## 2. Canonical High-Level Structure

```text
src/
  app/
  components/
  design-system/
  feature-system/
  features/
  views/
  entities/
  services/
  providers/
  hooks/
  store/
  lib/
  types/
  tests/
3. Folder Intent
app/

Route groups, layouts, page entry points, route handlers.

components/

Shared generic components only.

Recommended subfolders:

ui/

shell/

charts/

feedback/

navigation/

design-system/

Design tokens, themes, and UI guidelines.

feature-system/

Runtime capability layer.
This folder is mandatory.

Recommended subfolders:

catalog/

permissions/

resolver/

runtime/

features/

Module/domain UI implementation.

Recommended folders:

auth/

organizations/

crm-opportunities/

mandates/

research/

results/

companies/

contacts/

integrations/

billing/

settings/

views/

Reusable view primitives.

Recommended subfolders:

framework/

inline/

detail/

form/

entities/

Reusable entity-focused rendering or mapping helpers.
This is not where pages are owned.

services/

Data access, mutations, DTO shaping, secure server reads.

providers/

Top-level app providers and context composition.

hooks/

Thin reusable hooks for:

auth

organization

permissions

queries

UI

store/

Local app-shell and UI state only.

lib/

General utilities, constants, formatting, validation, helpers.

types/

Shared application and database-facing types.

tests/

unit/

integration/

e2e/

4. Hard Rules

feature-system/ is mandatory

features/ owns domain UI, not entitlement truth

views/ owns reusable inline/detail/form structure

services/ owns Supabase/backend access

components/ must stay generic

store/ must not become the security or capability source of truth

5. “Where does this go?” Rule

decides whether something is allowed -> feature-system/

fetches or mutates domain data -> services/

renders module-specific UI -> features/

renders reusable page/view patterns -> views/

renders generic shared UI -> components/

coordinates route/layout composition -> app/
