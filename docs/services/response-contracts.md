# Response Contracts

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how services should shape outputs so pages and features can consume them safely.

---

## 2. DTO Rule

Service responses should be stable DTOs, not raw unbounded table payloads.

Common DTO shapes:
- list item DTO
- detail DTO
- summary DTO
- select option DTO
- mutation result DTO

---

## 3. Common Result Shapes

Recommended patterns:

```ts
type ServiceSuccess<T> = {
  ok: true
  data: T
}

type ServiceFailure = {
  ok: false
  code: string
  message: string
}

type ServiceResult<T> = ServiceSuccess<T> | ServiceFailure
```
4. List Contract

List services should return:

items

totalCount if needed

pagination cursor or page info if needed

applied filters summary if needed

Example:

type ListResult<T> = {
  items: T[]
  totalCount?: number
  nextCursor?: string | null
}
5. Detail Contract

Detail services should return a domain-safe shape.

Example:

result detail DTO should expose:

result summary

canonical company summary

canonical contact summary

evidence list

psych profile summary

fit analysis summary

dossier summary

action metadata if needed

It should not require the page to reconstruct all of that from raw rows.

6. Error Contract

Use consistent service error codes.

Examples:

not_found

forbidden

invalid_input

organization_required

inactive_membership

integration_unavailable

billing_unavailable

internal_error

These are service-level operation errors, not feature-state reason codes.

7. Separation Rule

Do not confuse:

service operation errors
with

feature-system availability reason codes

Example:

service error: not_found

feature-state reason: missing_entitlement

They are not the same thing.

8. Final Rule

Pages and features should consume stable service contracts, not raw table assumptions.


