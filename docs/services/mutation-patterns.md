# Mutation Patterns

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the correct write pattern for the platform.

---

## 2. Write Path

Use this standard pattern:

Form / Action / Mutation Hook  
→ Service  
→ Supabase

Do not let forms write directly to organization-owned tables.

---

## 3. Audit Field Rule

Every mutation helper must automatically apply required ownership/audit fields where appropriate:

- organization_id
- created_by_user_id
- updated_by_user_id

The caller must not be trusted to supply these correctly every time.

---

## 4. Mutation Categories

### Create
Examples:
- create mandate
- create research run
- create research constraint
- create invitation
- connect integration

### Update
Examples:
- update mandate
- update organization settings
- update contact
- update company
- update integration status

### Structured side-effect actions
Examples:
- shortlist result
- export dossier
- accept invitation
- revoke invitation
- disconnect integration

These are still service-level operations even if they are not plain CRUD.

---

## 5. Validation Rule

All service mutations must validate:
- organization context
- required inputs
- ownership compatibility
- allowed mutation shape
- server-only restrictions where relevant

RLS remains the final enforcement layer, but services must still behave defensively.

---

## 6. Upsert Rule

Use upserts carefully.

Allowed:
- canonical entity synchronization where duplicates must be resolved
- integration configuration sync where natural keys exist

Not allowed:
- vague page-level “save whatever is present” patterns that hide data ownership mistakes

---

## 7. Transaction / RPC Rule

Use server-side transactions or RPCs when:
- multiple rows must stay consistent
- membership/invitation acceptance changes multiple tables
- bootstrap onboarding creates org + membership + defaults
- integration connection updates several related records
- billing or credits need atomic ledger updates

---

## 8. Final Rule

A mutation service should express a business action, not just raw SQL intent.
