# TASK-2026-002-03

Title: Fix signup messaging for existing-user outcome  
Status: queued  
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
Prevent misleading "check your email" signup success message when the submitted email already belongs to an existing account.

## Read First
- `reviews/REV-2026-03-23-signup-existing-user-message-audit.md`
- `reviews/REV-2026-03-23-forgot-password-flow-audit.md`
- `change-requests/CR-2026-002-signin-routing-canonical-bootstrap.md`
- `implementation-guides/IMP-2026-002-signin-routing-canonical-bootstrap.md`

## Allowed Files To Change
(implementation repo)
- `app/signup/page.tsx`
- `app/login/page.tsx` (only if message handling needs update)
- `src/services/auth/**` (only if helper extraction is needed)

## Forbidden Files To Change
(implementation repo)
- unrelated workspace module pages
- database migrations

## Acceptance Criteria
Task is complete only when:
1. signup flow distinguishes existing-user outcome from genuine "confirmation email sent" outcome,
2. existing-user path shows non-misleading guidance (e.g., sign in or reset password),
3. success message remains correct for new unconfirmed signups,
4. PR includes full SHA, PR/compare URL, and lint/typecheck/build outputs.

## Output Required From Implementer
1. changed files + full SHA(s)
2. PR URL + compare URL
3. criterion-to-diff mapping
4. command outputs
5. blockers
6. risks
