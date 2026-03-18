# AI Agent Operating Rules

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how AI coding agents such as Codex and AI Studio must operate in this repository.

---

## 2. Core Rule

AI agents are implementers, not architecture inventors.

The repo docs are the source of truth.
AI agents must follow them.

---

## 3. Required Read Order

Before making changes, the agent must read:

1. docs/auth/*
2. docs/authorization/*
3. docs/database/*
4. docs/feature-system/*
5. docs/services/*
6. docs/frontend/*
7. docs/workflows/*
8. docs/dev-guides/*

At minimum, the agent must understand:
- current organization model
- canonical module list
- feature-system ownership
- source-of-truth rules
- workflow sequence
- implementation order

---

## 4. What AI Agents Must Do

- follow existing architecture
- implement through correct boundaries
- update docs when changing contracts or structure
- keep changes scoped to the requested task
- return changed files and key risks
- preserve organization scoping and audit field rules
- prefer explicit file-level changes over broad rewrites

---

## 5. What AI Agents Must Not Do

Do not:
- invent new top-level modules
- bypass services with page-level queries
- bypass feature-system with UI-only checks
- use provider names as product structure
- build final UI from legacy result blobs
- change unrelated files casually
- “fix” bugs by creating duplicate logic in another layer
- let local store become the capability source of truth

---

## 6. Required Task Output

Every implementation response should include:
- files changed
- what changed
- blockers
- risks
- any discovered schema mismatch

---

## 7. Required Change Discipline

Before changing code, the agent must know:
- which files are allowed to change
- which files must not change
- what the acceptance criteria are
- what boundary owns the fix

If those are not explicit, the agent should infer them from the repo docs, not invent a new architecture.

---

## 8. Review Rule

After implementing, the agent must verify:
- correct organization context handling
- correct role/module/feature boundaries
- no ad hoc page-level query sprawl
- no broken source-of-truth usage
- no hidden cross-module side effects

---

## 9. Final Rule

An AI-generated patch is wrong if it solves the immediate symptom but violates the architecture.
