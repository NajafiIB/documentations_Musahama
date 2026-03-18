# role-matrix.md

This document defines the practical role matrix for the platform.

Use this matrix for:
- UI visibility
- action visibility
- feature gating
- service-level validation
- developer implementation guidance

Database RLS remains the final source of truth for data access.

---

# Roles

- owner
- admin
- manager
- analyst
- member
- billing_admin
- developer

---

# Role Groups

## Platform operator roles
- owner
- billing_admin
- developer

## Workflow roles
- owner
- admin
- manager
- analyst
- member
- developer
- billing_admin (optional broader visibility)

---

# Access Matrix

| Capability | owner | admin | manager | analyst | member | billing_admin | developer |
|-----------|:-----:|:-----:|:-------:|:-------:|:------:|:-------------:|:---------:|
| View dashboard | yes | yes | yes | yes | yes | yes | yes |
| View CRM opportunities | yes | yes | yes | yes | yes | optional | yes |
| Create/edit CRM opportunities | yes | yes | yes | yes | limited | no | yes |
| View mandates | yes | yes | yes | yes | yes | optional | yes |
| Create/edit mandates | yes | yes | yes | yes | limited | no | yes |
| View research | yes | yes | yes | yes | yes | optional | yes |
| Create/edit research | yes | yes | yes | yes | limited | no | yes |
| View strategies | yes | yes | yes | yes | yes | optional | yes |
| View results | yes | yes | yes | yes | yes | optional | yes |
| Shortlist/export results | yes | yes | yes | yes | limited | no | yes |
| View companies | yes | yes | yes | yes | yes | optional | yes |
| Edit companies | yes | yes | yes | yes | limited | no | yes |
| View contacts | yes | yes | yes | yes | yes | optional | yes |
| Edit contacts | yes | yes | yes | yes | limited | no | yes |
| View integrations | yes | no | no | no | no | yes | yes |
| Manage integrations | yes | no | no | no | no | yes | yes |
| View billing | yes | no | no | no | no | yes | yes |
| Manage billing | yes | no | no | no | no | yes | yes |
| View module configuration | yes | no | no | no | no | yes | yes |
| Manage module/platform features | yes | no | no | no | no | yes | yes |
| Manage org settings | yes | yes | limited | no | no | limited | yes |
| Manage members | yes | yes | limited | no | no | no | yes |

---

# Interpretation Rules

## owner
Full control over organization, workflow, billing, integrations, and configuration.

## admin
Business/workflow admin, not technical platform admin.

## manager
Operational manager with workflow control but not platform admin control.

## analyst
Research operator.

## member
Basic product user with limited mutation abilities depending on feature design.

## billing_admin
Billing/platform operations role.
Can manage billing and platform-level operational setup.
May optionally view workflow pages, but should not be treated as a workflow operator by default.

## developer
Technical operator role.
Can access both workflow and platform configuration where needed.

---

# Suggested UI Enforcement

## Always visible to workflow roles
- dashboard
- crm opportunities
- mandates
- research
- results
- companies
- contacts

## Restricted to platform operator roles
- integrations
- billing
- provider/API setup
- module/platform configuration

## Optional shared areas
- settings may vary by sub-section
- billing_admin may see workflow pages in read-only mode if desired

---

# Final rule

If there is any doubt:
- workflow business functions -> workflow roles
- billing/integrations/platform configuration -> platform operator roles
- database access is still controlled by RLS
