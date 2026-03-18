# Role Model

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the official role model for the platform.

Use this document for:
- UI visibility
- action visibility
- feature gating
- service-level validation
- route and module rules

Database RLS remains the final source of truth.

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

### 3.1 Platform Operator Roles
These roles can manage technical/platform-level configuration.

- owner
- billing_admin
- developer

They can manage:
- integrations
- provider/API configuration
- billing
- subscription
- platform/module configuration
- technical setup

### 3.2 Workflow Roles
These roles operate the business workflow.

- owner
- admin
- manager
- analyst
- member
- developer
- billing_admin (optional broader visibility)

They can access:
- crm_opportunities
- mandates
- research
- results
- companies
- contacts

---

## 4. Interpretation Rules

### owner
Full control over organization, workflow, billing, integrations, and configuration.

### admin
Business/workflow admin.
Not automatically a technical platform operator.

### manager
Operational workflow manager.
Can manage workflow operations but not platform configuration by default.

### analyst
Research operator.

### member
Basic product user with limited mutation abilities depending on feature design.

### billing_admin
Billing/platform operations role.
Can manage billing and platform-level operational setup.
May optionally view workflow pages, but must not be treated as a workflow operator by default.

### developer
Technical operator role.
Can access both workflow and platform configuration where needed.

---

## 5. Hard Rules

1. `admin` is not a platform admin by default
2. `billing_admin` is not a workflow operator by default
3. `developer` is allowed in both platform and workflow zones
4. `owner` spans both platform and workflow control
5. Role interpretation must be centralized, not duplicated across components

---

## 6. Suggested UI Enforcement

### Always visible to workflow roles
- dashboard
- crm opportunities
- mandates
- research
- results
- companies
- contacts

### Restricted to platform operator roles
- integrations
- billing
- provider/API setup
- module/platform configuration

### Optional shared areas
- settings may vary by sub-section
- billing_admin may see workflow pages in read-only mode if explicitly enabled
