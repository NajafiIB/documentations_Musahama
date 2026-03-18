```md
# Workspace Shell

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the permanent application shell used throughout the protected workspace.

---

## 2. Permanent Shell Rule

Once the user enters the protected workspace, the shell is always present.

The shell contains:
- Header
- Sidebar
- Footer

Do not redesign shell structure per page.

---

## 3. Header Contract

The header contains:
- organization switcher
- global search
- quick create
- notifications
- user menu

The header is global workspace UI, not module-specific UI.

---

## 4. Sidebar Contract

The sidebar is driven by canonical module keys only:

- dashboard
- crm_opportunities
- mandates
- research
- results
- companies
- contacts
- integrations
- billing
- settings

The sidebar must not use deprecated concepts as top-level items:
- discovery
- shortlist
- dossiers
- CRM sync
- analytics

Those belong deeper in the module UI.

---

## 5. Footer Contract

Keep the footer minimal:
- version
- support/docs
- status

---

## 6. Shell Boot Sequence

The shell should load in this order:

1. resolve session
2. resolve current user
3. resolve current organization
4. resolve active membership/role
5. resolve enabled modules
6. render shell
7. render active route content

The shell must not render a fake fully-active workspace before these checks complete.

---

## 7. Shell States

The workspace shell must gracefully handle:
- loading bootstrap state
- no session
- no active organization
- multiple organizations requiring selection
- access denied
- module unavailable

---

## 8. Shell Responsibility Boundary

The shell owns:
- consistent framing
- organization switcher placement
- module navigation placement
- global quick actions placement
- global feedback/status placement

The shell does not own:
- module-specific business logic
- feature entitlement decisions
- direct data queries scattered in shell components
