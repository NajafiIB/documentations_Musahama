# TASK-2026-003-03

Title: Remove remaining mock datasets from workspace pages and replace with service-backed empty states  
Status: in_progress  
Parent Change Request: CR-2026-003  
Parent Implementation Guide: IMP-2026-003  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/route-availability-404-hardening  
Layer: frontend | services  
Module: dashboard | research | companies  
Last Updated: 2026-03-22

## Objective
Eliminate hardcoded mock arrays from dashboard/research/companies workspace pages and use service-driven data or explicit empty-state UX.

## Read First
- `reviews/REV-2026-03-22-live-code-gap-audit.md`
- `reviews/REV-2026-03-23-live-verification-check.md`
- `implementation-guides/IMP-2026-003-route-availability-404-hardening.md`
- `docs/services/implementation-rules.md`
- `docs/frontend/frontend-foundation.md`

## Allowed Files To Change
(implementation repo)
- `app/(workspace)/dashboard/page.tsx`
- `app/(workspace)/research/page.tsx`
- `app/(workspace)/companies/page.tsx`
- `src/services/**` (only if data helpers are needed)

## Forbidden Files To Change
(implementation repo)
- database migrations
- unrelated modules and auth flows

## Acceptance Criteria
Task is complete only when:
1. no hardcoded mock arrays remain in the three target pages,
2. pages render either service-backed data or explicit empty-state components,
3. no direct Supabase calls are introduced in page components,
4. PR includes full SHA, PR/compare URL, and lint/typecheck/build evidence.

## Output Required From Implementer
1. changed files + full SHA(s)
2. PR URL + compare URL
3. criterion-to-diff mapping
4. command outputs
5. blockers
6. risks
