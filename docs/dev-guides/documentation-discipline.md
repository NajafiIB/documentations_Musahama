# Documentation Discipline

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how the repository documentation stays current and trustworthy.

---

## 2. Core Rule

GitHub is the source of truth for platform documentation.
Conversations are not the source of truth.
Random notes are not the source of truth.
Uncommitted local files are not the source of truth.

---

## 3. What Must Be Documented

Update docs when changing:
- auth flow
- onboarding flow
- invitation logic
- role rules
- module list
- feature keys
- service contracts
- workflow structure
- database schema assumptions
- source-of-truth rules
- folder boundaries
- implementation order

---

## 4. Required Documentation Behavior

- docs live in the repo
- docs must be updated in the same change when architecture changes
- docs must reflect real implementation, not aspiration only
- new developers and AI agents must be able to read docs and understand the system

---

## 5. Folder Rule

The following folders must stay aligned:

- docs/auth/
- docs/authorization/
- docs/database/
- docs/feature-system/
- docs/services/
- docs/frontend/
- docs/workflows/
- docs/dev-guides/

---

## 6. Review Rule

Reviewers must ask:
- is the implementation still aligned with the documented architecture?
- did the PR update docs where required?
- is a repo reader still able to understand the system after this change?

---

## 7. Final Rule

The moment docs and implementation diverge, the team starts accumulating invisible debt.
