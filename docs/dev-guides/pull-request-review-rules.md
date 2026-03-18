```md
# Pull Request Review Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how pull requests should be reviewed for architectural correctness.

---

## 2. Core Rule

A PR is not reviewed only for whether it works.
It must also be reviewed for whether it belongs in the right layer.

---

## 3. Required Review Questions

Every PR should be checked against these questions:

### Architecture
- Does the change respect folder ownership boundaries?
- Did it keep capability truth in `feature-system/`?
- Did it keep data access in `services/`?
- Did it keep pages thin?

### Data
- Is the read model using canonical source-of-truth tables where appropriate?
- Are mutations organization-scoped?
- Are audit fields applied correctly?

### Access
- Does it respect the role model?
- Does it preserve module-driven navigation?
- Are restricted actions runtime-gated rather than UI-guessed?

### Security
- Does it rely on RLS and proper server-side boundaries?
- Does it avoid exposing sensitive provider or billing data?

### Workflow
- Does it preserve the CRM → Mandate → Research → Results chain?
- Does it keep shortlist/dossier as results actions rather than new modules?

---

## 4. PR Checklist

Every meaningful PR should state:

- what changed
- why it changed
- what files were intentionally modified
- what risks remain
- whether docs were updated
- whether tests were updated

---

## 5. Docs Rule

If a PR changes any of these, docs must be updated:

- auth flow
- role rules
- module list
- feature keys
- service contracts
- workflow sequence
- database schema assumptions
- source-of-truth decisions
- folder structure

---

## 6. Rejection Triggers

Reject or rework a PR if it:
- hardcodes sidebar or role logic in UI pages
- adds random Supabase queries to page components
- uses provider names as product concepts
- builds final views from legacy result blobs
- introduces a new top-level module without design approval
- duplicates access logic across multiple layers
- “fixes” the bug in the wrong layer

---

## 7. Final Rule

A PR that works but increases structural debt is not acceptable.
