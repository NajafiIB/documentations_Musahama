# CR-2026-003

Title: Route availability gating to eliminate workspace 404 navigation  
Status: in_review  
Priority: P1  
Type: bug  
Owner: Platform Architect  
Requested By: 404 intake review  
Last Updated: 2026-03-22

Related GitHub Issue: TBD (project table item)  
Related Implementation Guide: implementation-guides/IMP-2026-003-route-availability-404-hardening.md  
Related Tasks: tasks/TASK-2026-003-01-route-availability-gating.md; tasks/TASK-2026-003-02-complete-routeAvailable-enforcement.md; tasks/TASK-2026-003-03-remove-mock-workspace-datasets.md  
Related Review: reviews/REV-2026-03-22-404-navigation-intake.md; reviews/REV-2026-03-22-route-availability-result-review.md; reviews/REV-2026-03-22-task-003-02-compliance-check.md; reviews/REV-2026-03-22-live-code-gap-audit.md; reviews/REV-2026-03-23-live-verification-check.md; reviews/REV-2026-03-23-closure-evidence-recheck.md  
Target Repo: NajafiIB/Implementation_Musahama

## Summary
Prevent users from seeing or reaching module routes that are not yet implemented, while preserving canonical module vocabulary and feature-system boundaries.

## Problem
Current behavior can expose links/routes without implemented pages, causing 404 UX despite healthy auth and bootstrap.

## Expected Behavior
- Sidebar shows only modules that are both:
  1) allowed by runtime capability truth,
  2) marked as implemented/available routes.
- Route guards redirect unsupported workspace routes to a safe canonical page (`/dashboard`) with a clear reason message when appropriate.
- No fake/mock datasets are used to mask missing route implementations.

## Owning Layer
- Route availability policy: feature-system/frontend boundary
- Route enforcement: middleware + workspace layout
- Data truth: services

## Constraints
- Do not rename canonical modules.
- Do not remove modules from catalog as a shortcut.
- Do not use mock rows as a 404 workaround.
- Keep capability truth in `feature-system` and data access in `services`.

## Acceptance Criteria
1. A single route-availability registry (or equivalent) exists and is consumed by sidebar + route guard.
2. Sidebar cannot render links to unavailable module routes.
3. Direct navigation to unavailable module routes is safely redirected.
4. Implemented module routes remain unaffected.
5. Evidence includes PR URL, full SHA(s), diff mapping, and lint/typecheck/build outputs.
6. Mock/demo workspace datasets are removed from user-facing pages.

## Risks
- Over-filtering modules could hide legitimately available pages.
- Divergence risk if route registry is not co-owned with module catalog updates.

## Final Decision
- in_review (pending full TASK-2026-003-02 compliance)
