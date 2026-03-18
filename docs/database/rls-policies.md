# RLS Policies

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the security expectations for row-level security.

RLS is the final database enforcement layer.

---

## 2. Core Security Model

Supabase Auth handles authentication.
Supabase RLS enforces organization isolation and database-level authorization.

Runtime feature/module resolution sits above RLS, not instead of it.

---

## 3. Required Principles

1. Every organization-owned table must be tenant-filtered
2. Membership must be active to read/write organization-owned business data
3. Elevated org operations must require allowed org roles
4. Frontend visibility is never a replacement for RLS
5. Sensitive integration data must never be exposed directly to clients

---

## 4. Recommended Helper Functions

### is_org_member(organization_id)
Returns true when auth user has active membership in the organization.

### has_org_role(organization_id, roles[])
Returns true when auth user has active membership with one of the allowed roles.

These helper functions should be reused consistently across policy definitions.

---

## 5. Table Policy Groups

### profiles
Allow:
- self select
- self update
- self insert if needed during bootstrap/trigger model

### organizations
Allow:
- select for active members
- insert for authenticated onboarding/bootstrap flows
- update only for owner/admin/developer or stricter final policy if needed

### organization_members
Allow:
- self read
- org-admin/owner/developer management
- controlled bootstrap insert
- no unrestricted client-side membership creation

### organization_invitations
Allow:
- create/revoke by owner/admin/developer
- read by inviters/admins and invited email owner
- no direct client bypass of acceptance checks

### organization_modules
Allow:
- read by active org members when needed for runtime
- write only by allowed operator roles

### organization_subscriptions
Allow:
- read by owner/billing_admin/developer
- restricted writes through controlled billing services

### organization_integrations
Allow:
- sanitized read for allowed operator roles
- sensitive fields server-only
- writes only through controlled service paths

### organization_credit_ledger
Allow:
- read by owner/billing_admin/developer
- writes through server-side billing/credit services only

### workflow tables
Allow:
- read/write only inside tenant boundary
- role restrictions where relevant
- write helpers must stamp audit fields

### canonical entity tables
Allow:
- read/write only inside tenant boundary
- never expose cross-organization entity leakage

### analysis tables
Allow:
- read/write only inside tenant boundary
- result-linked analysis must stay within same organization

---

## 6. Hard Rules

Do not:
- use global open policies on org-owned business tables
- assume UI hiding is enough
- expose secret_ref or secret-like values in client-readable policies
- let pages decide security
