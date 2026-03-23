# IMP-2026-003

Title: Implement route availability gating to remove workspace 404 navigation  
Status: in_review  
Parent Change Request: CR-2026-003  
Owner: Platform Architect  
Prepared For: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/route-availability-404-hardening  
Last Updated: 2026-03-22

Related Review: reviews/REV-2026-03-22-404-navigation-intake.md; reviews/REV-2026-03-22-route-availability-result-review.md; reviews/REV-2026-03-22-task-003-02-compliance-check.md; reviews/REV-2026-03-22-live-code-gap-audit.md; reviews/REV-2026-03-23-live-verification-check.md; reviews/REV-2026-03-23-closure-evidence-recheck.md  
Related Tasks: tasks/TASK-2026-003-01-route-availability-gating.md; tasks/TASK-2026-003-02-complete-routeAvailable-enforcement.md; tasks/TASK-2026-003-03-remove-mock-workspace-datasets.md  
Related PRs: TBD

## Goal
Eliminate workspace 404s by gating navigation and route access with a deterministic route-availability source that works alongside module entitlement checks.

## Read First
1. `docs/frontend/frontend-foundation.md`
2. `docs/feature-system/implementation-rules.md`
3. `docs/authorization/implementation-rules.md`
4. `docs/auth/routes.md`
5. `docs/services/implementation-rules.md`
6. `change-requests/CR-2026-003-route-availability-404-hardening.md`

## Architecture Rules To Respect
- modules remain canonical and unchanged,
- capability truth remains in `feature-system`,
- data access remains in `services`,
- route availability must not be faked by mock data.

## Allowed Files To Change
(implementation repo)
- `src/components/shell/sidebar.tsx`
- `middleware.ts`
- `app/(workspace)/layout.tsx`
- `src/feature-system/catalog/**` (only for route-availability metadata)
- `src/feature-system/runtime/**` (only if needed for availability composition)

## Forbidden Files / Areas
- database migrations
- unrelated module business UI logic
- provider secrets/auth internals

## Target Design
- Define route availability metadata for workspace modules (implemented vs planned).
- Compose sidebar visible links from:
  1) module visibility resolver output,
  2) route-availability metadata.
- Enforce same availability check in middleware/layout for direct URL hits.
- Redirect unavailable module routes to `/dashboard` (or canonical fallback) without 404.

## Implementation Plan
1. Introduce route-availability metadata near module catalog.
2. Refactor sidebar to use entitlement + availability intersection.
3. Refactor middleware direct-route checks to include availability gate.
4. Add concise empty state/copy for temporarily unavailable modules.
5. Validate no mock datasets were reintroduced.

## Validation Checklist
- clicking sidebar links never opens a 404 for workspace modules,
- direct URL hit to unavailable module route redirects safely,
- available module pages still open normally,
- route/module vocabulary remains canonical.

## Required Output From Coding Agent
1. changed files + full 40-char SHA(s)
2. PR URL + compare URL
3. criterion-to-diff mapping
4. lint/typecheck/build outputs
5. blockers/risks
