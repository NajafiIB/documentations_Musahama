
---

## `docs/authorization/route-guarding.md`

```md
# Route Guarding

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how route access must be guarded.

Routes must not rely on static navigation visibility.
Every protected route must validate access again.

---

## 2. Coarse Route Guarding

### Public routes
- /login
- /register
- /forgot-password
- /invite/[token]

### Protected routes
- /dashboard
- /crm-opportunities
- /mandates
- /research
- /results
- /companies
- /contacts
- /integrations
- /billing
- /settings

---

## 3. Route Guard Sequence

For every protected route:

1. verify session
2. resolve current organization
3. resolve active membership
4. resolve current role
5. resolve enabled module state
6. allow or deny route
7. resolve feature states inside the page

---

## 4. Correct Rule

### Middleware
May do:
- coarse auth/session protection
- public vs protected route segregation

### Server-side layout/page gate
Must do:
- organization resolution
- role resolution
- module visibility check

### Page internals
Must do:
- feature-level checks through runtime hooks/resolvers

---

## 5. Examples

### /integrations
Requires platform operator visibility.

### /billing
Requires platform operator visibility.

### /crm-opportunities
Requires workflow role + enabled module.

### /results
Requires workflow role + enabled module.

### /settings
Requires subsection-specific access.

---

## 6. Failure Behavior

### no session
Redirect to /login

### no active organization
Redirect to /onboarding or org selector

### no membership
Block workspace access

### module disabled
Redirect to allowed landing page or access denied page

### role not allowed
Show access denied

---

## 7. Hard Rule

Do not rely on hidden sidebar items as authorization.
Routes must be guarded independently.
