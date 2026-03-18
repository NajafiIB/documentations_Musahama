# App Router Structure

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official Next.js App Router structure.

---

## 2. Route Groups

Use these route groups:

### (auth)
Contains authentication routes.
Exact auth route names must follow `docs/auth/*`.

Typical routes:
- /login
- /register
- /forgot-password
- /invite/[token]
- /auth/callback

### (workspace)
Contains the protected application workspace.

### api
Contains route handlers and server endpoints.

---

## 3. Official Workspace Routes

Use these route groups:

- /dashboard
- /crm-opportunities
- /mandates
- /mandates/[id]
- /research
- /research/[id]
- /results
- /results/[id]
- /companies
- /companies/[id]
- /contacts
- /contacts/[id]
- /integrations
- /billing
- /settings

---

## 4. Naming Rules

### Routes
Use kebab-case.
Examples:
- /crm-opportunities
- /results

### Module keys
Use snake_case.
Examples:
- crm_opportunities
- results

### Database names
Keep canonical DB table names as they are.
Example:
- workflow table = research_results

The route name and table name do not need to match exactly.

---

## 5. Recommended App Tree

```text
src/app/
  (auth)/
    login/
    register/
    forgot-password/
    invite/[token]/
    auth/callback/

  (workspace)/
    layout.tsx
    page.tsx
    dashboard/
    crm-opportunities/
    mandates/
    mandates/[id]/
    research/
    research/[id]/
    results/
    results/[id]/
    companies/
    companies/[id]/
    contacts/
    contacts/[id]/
    integrations/
    billing/
    settings/
6. Layout Responsibilities
root layout

Owns:

global CSS

theme provider

query provider

app-level wrappers

auth layout

Owns:

auth page chrome only

no workspace shell

workspace layout

Owns:

session check

current organization resolution

role/context bootstrap

shell composition

protected route entry

pages

Own:

asking for DTOs

rendering feature views

composing page content

not direct capability truth

7. Protected Route Rule

No protected workspace route should render before:

session is resolved

current organization is resolved

active membership is known

8. Special States

The frontend must support dedicated handling for:

unauthorized / no session

no active organization

multi-organization selector

access denied

not found


---

  api/
  globals.css
  layout.tsx
