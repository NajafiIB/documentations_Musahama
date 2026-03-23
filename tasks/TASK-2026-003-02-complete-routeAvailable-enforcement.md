# TASK-2026-003-02

Title: Complete explicit routeAvailable enforcement for sidebar and direct module route hits  
Status: blocked  
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
Finish 404 hardening by introducing explicit `routeAvailable` metadata in module catalog and enforcing it in both sidebar rendering and middleware direct-hit handling.

## Read First
- `reviews/REV-2026-03-22-route-availability-result-review.md`
- `reviews/REV-2026-03-22-task-003-02-compliance-check.md`
- `reviews/REV-2026-03-22-live-code-gap-audit.md`
- `reviews/REV-2026-03-23-live-verification-check.md`
- `tasks/TASK-2026-003-01-route-availability-gating.md`
- `implementation-guides/IMP-2026-003-route-availability-404-hardening.md`

## Allowed Files To Change
(implementation repo)
- `src/feature-system/catalog/module-keys.ts`
- `src/components/shell/sidebar.tsx`
- `middleware.ts`
- `app/(workspace)/layout.tsx` (only if fallback UX message needed)

## Forbidden Files To Change
(implementation repo)
- database migrations
- unrelated feature pages
- service logic unrelated to routing

## Acceptance Criteria
Task is complete only when:
1. each canonical module has explicit `routeAvailable: boolean` metadata,
2. sidebar enforces `enabled && routeAvailable` before rendering links,
3. middleware redirects authenticated direct hits to unavailable module routes to `/dashboard`,
4. available module routes continue to work,
5. evidence includes full SHA, PR/compare URL, and lint/typecheck/build outputs.

## Output Required From Implementer
1. changed files + full SHA(s)
2. PR URL + compare URL
3. criterion-to-diff mapping
4. command outputs
5. blockers
6. risks


## Blocker
Current implementation evidence still misses routeAvailable enforcement in sidebar and middleware direct-hit guard behavior, and lacks auditable PR/compare URL links.
