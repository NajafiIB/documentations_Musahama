# TASK-2026-002-02

Title: Harden forgot/reset password flow and middleware public-route handling  
Status: blocked  
Parent Change Request: CR-2026-002  
Parent Implementation Guide: IMP-2026-002  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/signin-routing-canonical-bootstrap  
Layer: auth | frontend  
Module: settings  
Last Updated: 2026-03-23

## Objective
Ensure forgot/reset password flow is deterministic and user-safe across link validation, middleware routing, and reset completion UX.

## Read First
- `reviews/REV-2026-03-23-forgot-password-flow-audit.md`
- `reviews/REV-2026-03-23-forgot-password-closure-recheck.md`
- `reviews/REV-2026-03-23-latest-implementation-recheck.md`
- `change-requests/CR-2026-002-signin-routing-canonical-bootstrap.md`
- `implementation-guides/IMP-2026-002-signin-routing-canonical-bootstrap.md`
- `docs/auth/routes.md`

## Allowed Files To Change
(implementation repo)
- `app/forgot-password/page.tsx`
- `app/reset-password/page.tsx`
- `middleware.ts`
- `app/auth/callback/route.ts` (only if recovery path normalization is needed)

## Forbidden Files To Change
(implementation repo)
- unrelated workspace module pages
- database migrations

## Acceptance Criteria
Task is complete only when:
1. `/reset-password` is treated as a valid public recovery route,
2. invalid/expired recovery links show explicit user guidance,
3. successful reset reliably leads user to login with a clear success message,
4. end-to-end reset flow is verified with Supabase template + redirect config,
5. PR includes full SHA, PR/compare URL, and lint/typecheck/build outputs.

## Output Required From Implementer
1. changed files + full SHA(s)
2. PR URL + compare URL
3. criterion-to-diff mapping
4. command outputs
5. blockers
6. risks


## Blocker
Live code still needs explicit recovery-session validation UX before password update, plus auditable PR evidence.
