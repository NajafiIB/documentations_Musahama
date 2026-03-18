```md
# Organization Context Services

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how organization context is loaded and maintained through the service layer.

The platform is organization-first.
No protected workspace should load without current organization resolution.

---

## 2. Required Reads

The services layer must support:

- get current authenticated user
- list active memberships for current user
- resolve current organization
- read current organization settings
- read organization membership role
- read organization status

---

## 3. Required Service Contracts

Recommended service functions:

- `getActiveMemberships(userId)`
- `resolveCurrentOrganization(userId)`
- `getOrganizationById(organizationId)`
- `getOrganizationSettings(organizationId)`
- `listOrganizationMembers(organizationId)`
- `inviteOrganizationMember(organizationId, payload)`
- `acceptOrganizationInvitation(token)`

---

## 4. Resolution Rule

Current organization resolution should follow:

1. resolve authenticated user
2. load active memberships
3. if zero memberships -> onboarding path
4. if one membership -> use that organization
5. if multiple memberships -> use selected organization or require selector
6. confirm organization status is active

---

## 5. Required Output Shape

A current-organization resolver should return a stable shape like:

```ts
type CurrentOrganizationResolution =
  | { kind: "no_session" }
  | { kind: "no_membership" }
  | { kind: "single"; organizationId: string; role: string }
  | {
      kind: "multi";
      organizations: Array<{
        organizationId: string;
        name: string;
        role: string;
      }>;
    }
6. Hard Rules

Never guess organization from route alone

Never treat profile as membership

Never render workspace before membership/org resolution

Never allow inactive membership to act as active context

Never let page components recreate organization resolution logic ad hoc

7. Final Rule

Organization context is a service responsibility first, then consumed by layout/providers/hooks.
