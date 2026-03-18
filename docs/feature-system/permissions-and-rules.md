
---

## `docs/feature-system/permissions-and-rules.md`

```md
# Permissions and Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how the feature-system interprets roles for module and feature access.

This document does not replace the master authorization docs.
It adapts them into feature-system runtime rules.

---

## 2. Official Roles

- owner
- admin
- manager
- analyst
- member
- billing_admin
- developer

---

## 3. Role Groups

### Platform operator roles
- owner
- billing_admin
- developer

These can manage:
- integrations
- provider/API configuration
- billing
- module/platform features
- technical setup

### Workflow roles
- owner
- admin
- manager
- analyst
- member
- developer
- billing_admin (optional broader visibility)

These can access:
- crm_opportunities
- mandates
- research
- results
- companies
- contacts

---

## 4. Important Interpretation Rules

1. `admin` is a workflow/business admin, not a technical platform operator by default
2. `billing_admin` is not a workflow operator by default
3. `developer` may operate in both workflow and platform areas
4. `owner` spans both platform and workflow control
5. `settings` must use subsection rules, not one flat access rule

---

## 5. Baseline Module Rules

### dashboard
Visible to all active organization members.

### crm_opportunities
Visible to workflow roles.

### mandates
Visible to workflow roles.

### research
Visible to workflow roles.

### results
Visible to workflow roles.

### companies
Visible to workflow roles.

### contacts
Visible to workflow roles.

### integrations
Visible only to platform operator roles.

### billing
Visible only to platform operator roles.

### settings
Subsection-based.

---

## 6. Feature Rule Baseline

A feature may be:
- visible and enabled
- visible and disabled
- hidden entirely

That decision should depend on:
- module state
- role
- feature entitlement
- dependency state
- provider state
- quota/system state

---

## 7. Limited and Optional Access

### limited
Role may use only part of the feature surface.

Example:
- member can view results but not use certain export or mutation actions

### optional
Allowed only if the product configuration explicitly enables broader visibility.

Example:
- billing_admin may optionally see workflow pages in broader read-only mode

These are runtime design decisions, not UI guesses.

---

## 8. Centralization Rule

Role logic must live in:
- role-matrix.ts
- module-rules.ts
- feature-rules.ts

It must not be duplicated across:
- components
- route files
- random hooks
- inline button conditionals
