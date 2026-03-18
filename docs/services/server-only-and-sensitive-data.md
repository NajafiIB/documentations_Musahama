# Server-Only and Sensitive Data

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define which service logic must remain server-only.

---

## 2. Server-Only Areas

The following must stay in server-side services or controlled APIs/functions:

- provider secret handling
- organization_integrations.secret_ref access
- provider auth config resolution
- billing-provider interaction
- credit ledger write orchestration
- provider-backed capability checks needing private config
- sensitive organization bootstrap and secure joins
- any logic using service-role privileges

---

## 3. Sanitized Read Rule

Client-readable responses may include:

- connection status
- provider label
- enabled capability summary
- last sync timestamp
- safe error state
- safe billing summary
- safe plan/module summary

Client-readable responses must not include:
- raw credentials
- raw secret references
- provider private tokens
- internal secret config payloads
- unrestricted billing-provider payloads

---

## 4. Billing Rule

Billing reads often require assembly across:
- plans
- organization_subscriptions
- organization_modules
- organization_credit_ledger

If sensitive or multi-source, perform them server-side and return a sanitized DTO.

---

## 5. Integration Rule

Integrations may expose:
- status
- health
- enabled capabilities
- last error summary

They must not expose:
- connection secrets
- private auth configuration
- raw secret-like objects

---

## 6. Global Config Rule

Do not build client services around secret-like values in global_config.
Move secret handling to proper secret infrastructure and server-side access patterns.

---

## 7. Final Rule

If the data would be harmful to expose directly, it does not belong in a client-readable service response.
