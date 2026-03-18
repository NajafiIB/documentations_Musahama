# Access Matrix

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the practical authorization baseline for module visibility and major capabilities.

This is the implementation matrix for frontend and service-layer access checks.

---

## 2. Access Matrix

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

## 3. Interpretation Notes

### yes
Role can access/use this area normally.

### limited
Role may have constrained mutation or subsection-only access.
This must be defined at the feature or page-subsection level.

### optional
Allowed only if product configuration explicitly permits it.
Do not assume optional visibility by default.

### no
Role must not access/use that area.

---

## 4. Enforcement Rule

This matrix must be enforced in:
- feature-system permissions
- server-side resolver rules
- route/module guards
- service-level validation

It must not exist only as a UI table in documentation.
