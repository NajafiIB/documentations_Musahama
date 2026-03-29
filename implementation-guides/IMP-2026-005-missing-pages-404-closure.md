# IMP-2026-005

Title: Implement missing workspace pages and dashboard mandate navigation without 404s  
Status: draft  
Parent Change Request: CR-2026-005  
Owner: Platform Architect  
Prepared For: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/missing-pages-404-closure  
Last Updated: 2026-03-23

Related Review: reviews/REV-2026-03-23-missing-pages-404-intake.md  
Related Tasks: tasks/TASK-2026-005-01-route-inventory-and-gap-map.md; tasks/TASK-2026-005-02-add-thin-pages-for-missing-modules.md; tasks/TASK-2026-005-03-wire-dashboard-mandate-button.md; tasks/TASK-2026-005-04-route-availability-flip-and-verification.md  
Related PRs: TBD

## Goal
Finalize missing designed pages and wiring so canonical workspace navigation has no 404s.

## Read First
1. `docs/frontend/frontend-foundation.md`
2. `docs/feature-system/module-catalog.md`
3. `docs/workflows/implementation-rules.md`
4. `docs/services/implementation-rules.md`
5. `change-requests/CR-2026-005-missing-pages-404-closure.md`

## Allowed Files To Change
(implementation repo)
- `app/(workspace)/**` (thin pages/layout composition)
- `src/components/shell/sidebar.tsx`
- `src/feature-system/catalog/module-keys.ts` (routeAvailable metadata only)
- `middleware.ts` (route guard alignment)
- `src/services/**` (if page DTO helpers are required)

## Forbidden Files / Areas
- database migrations (unless separately approved)
- unrelated auth flows
- provider secrets/config exposure

## Implementation Plan
1. Produce canonical route inventory and mark implemented/missing.
2. Add minimal thin pages for each missing canonical route.
3. Wire dashboard mandate button to valid mandates route.
4. Update routeAvailable flags to match real implemented routes.
5. Validate direct URL access and sidebar click flows for all canonical modules.

## Validation Checklist
- every canonical module route opens a non-404 page,
- dashboard mandate button resolves to valid mandates page,
- no page-level direct DB calls added,
- route availability metadata and middleware behavior match reality.

## Required Output From Coding Agent
1. changed files + full SHA(s)
2. PR URL + compare URL
3. route-check matrix (module -> route -> result)
4. lint/typecheck/build outputs
5. blockers/risks
