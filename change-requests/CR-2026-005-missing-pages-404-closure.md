# CR-2026-005

Title: Finalize designed workspace pages and remove remaining 404 entry points  
Status: draft  
Priority: P1  
Type: feature  
Owner: Platform Architect  
Requested By: missing-pages intake  
Last Updated: 2026-03-23

Related GitHub Issue: TBD  
Related Implementation Guide: implementation-guides/IMP-2026-005-missing-pages-404-closure.md  
Related Tasks: tasks/TASK-2026-005-01-route-inventory-and-gap-map.md; tasks/TASK-2026-005-02-add-thin-pages-for-missing-modules.md; tasks/TASK-2026-005-03-wire-dashboard-mandate-button.md; tasks/TASK-2026-005-04-route-availability-flip-and-verification.md  
Related Review: reviews/REV-2026-03-23-missing-pages-404-intake.md  
Target Repo: NajafiIB/Implementation_Musahama

## Summary
Close remaining 404s by ensuring all designed canonical module routes and dashboard entry actions resolve to implemented pages.

## Problem
Some module pages/buttons are designed but not fully wired in implementation, resulting in broken navigation and 404 UX.

## Expected Behavior
- No user-facing 404 for canonical module routes.
- Dashboard mandate button routes to an implemented mandates entry/detail surface.
- Route availability flags mirror actual route readiness.

## Constraints
- Keep canonical module keys unchanged.
- Keep pages thin (no scattered access/business logic).
- Use services for data reads; avoid page-level direct DB queries.

## Acceptance Criteria
1. Canonical module route map has no unresolved page routes in workspace.
2. Dashboard mandate button navigates to valid mandate route.
3. Route availability metadata equals real implementation state.
4. PR evidence includes full SHAs, URLs, lint/typecheck/build outputs, and route-check matrix.

## Risks
- Rushing page scaffolds can introduce duplicated logic.
- Route metadata drift if toggles are not co-maintained with page creation.

## Final Decision
- pending implementation
