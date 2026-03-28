# Frontend Foundation

Owner: Platform Architect
Last Updated: 2026-03-28
Version: 1.1
Status: Approved

---

## 1. Purpose

Define the official frontend architecture for the Musahama platform.

This document is the source of truth for:
- frontend structure
- shell behavior
- route model
- UI ownership boundaries
- page composition rules
- view framework expectations

---

## 2. Core Rule

The frontend is a stable workspace system, not a collection of unrelated pages.

The frontend must be built around:
- one permanent shell
- one canonical module list
- one reusable view framework
- one runtime capability layer
- one disciplined service boundary

---

## 3. Approved Frontend Stack

Use:
- Next.js App Router
- shadcn/ui
- Tailwind CSS
- TanStack Table
- React Hook Form
- Zod
- Recharts
- Lucide Icons
- Zustand or React Context

shadcn/ui is the design system base.
A custom internal view framework sits on top.

---

## 4. Permanent Shell Rule

The workspace shell is always present once the user is inside the protected app.

The shell contains:
- Header
- Sidebar
- Footer

The shell must not disappear or change shape page by page.

---

## 5. Canonical Navigation Model

The only official top-level modules are:
- dashboard
- mandates
- research
- results
- companies
- contacts
- integrations
- billing
- settings

These are the only valid top-level sidebar areas.

The following are not top-level modules:
- discovery
- shortlist
- dossiers
- CRM sync
- CRM opportunities import
- analytics

CRM opportunity loading and linking must appear as a mandate-level action, drawer, or button.
It must not appear as a dedicated top-level tab.

These must appear as:
- embedded views
- actions
- result detail sections
- exports
- widgets
- secondary tabs

---

## 6. Ownership Boundary

### app/
Owns:
- route groups
- layouts
- route params
- page composition entry points

### components/
Owns:
- shared generic UI
- shell primitives
- navigation primitives
- chart wrappers
- feedback components

### design-system/
Owns:
- tokens
- themes
- guidelines

### feature-system/
Owns:
- runtime capability truth
- module visibility
- feature availability
- provider requirement resolution

### features/
Owns:
- domain/module UI
- module-specific forms
- domain-specific views
- module-specific components

### views/
Owns:
- reusable inline/detail/form view primitives

### services/
Owns:
- data fetching
- mutations
- DTO shaping
- Supabase/backend access

### providers/
Own:
- top-level context composition

### hooks/
Own:
- thin reusable hooks
- organization/session/query/UI hooks

### store/
Owns:
- local UI/app-shell state
- never final security or entitlement truth

---

## 7. Security and Access Rule

The frontend is not the security boundary.

The frontend must consume resolved runtime truth from:
- auth/session layer
- organization context services
- feature-system runtime APIs

The frontend must not:
- invent entitlement rules
- hardcode role logic throughout components
- treat hidden navigation as true access control

---

## 8. Source-of-Truth Rule for Final UI

Final UI must read normalized canonical data where applicable.

Use:
- companies
- company_domains
- contacts
- contact_emails
- contact_phones
- evidence
- psych_profiles
- lmc_fits
- dossiers

Do not build final UI around transitional `research_results` JSON blobs.

---

## 9. Final Mental Model

- shell = stable workspace frame
- modules = navigation and page areas
- features = actions and capabilities
- views = reusable inline/detail/form patterns
- services = data access
- feature-system = runtime capability truth
