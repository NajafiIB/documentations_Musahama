# TASK-2026-003-01

Title: Implement route-availability gating for sidebar and direct workspace routing  
Status: queued  
Parent Change Request: CR-2026-003  
Parent Implementation Guide: IMP-2026-003  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/route-availability-404-hardening  
Layer: feature-system | frontend | auth  
Module: cross-module  
Last Updated: 2026-03-22

## Objective
Remove 404 navigation by exposing only implemented module routes and guarding direct access to unavailable module routes.

## Read First
- `reviews/REV-2026-03-22-404-navigation-intake.md`
- `change-requests/CR-2026-003-route-availability-404-hardening.md`
- `implementation-guides/IMP-2026-003-route-availability-404-hardening.md`
- `docs/frontend/frontend-foundation.md`
- `docs/feature-system/implementation-rules.md`

## Allowed Files To Change
(implementation repo)
- `src/components/shell/sidebar.tsx`
- `middleware.ts`
- `app/(workspace)/layout.tsx`
- `src/feature-system/catalog/**` (availability metadata)
- `src/feature-system/runtime/**` (only if needed)

## Forbidden Files To Change
(implementation repo)
- database migrations
- unrelated module page logic
- services unrelated to routing/navigation

## Acceptance Criteria
Task is complete only when:
1. sidebar renders only modules with `visible && routeAvailable`,
2. direct hit to unavailable module route does not 404 and redirects safely,
3. no mock data is used to fake page readiness,
4. canonical module keys are unchanged,
5. PR includes full SHA(s), URL(s), and lint/typecheck/build outputs.

## Output Required From Implementer
1. changed files + full SHA(s)
2. PR URL + compare URL
3. criterion-to-diff mapping
4. command outputs
5. blockers
6. risks
