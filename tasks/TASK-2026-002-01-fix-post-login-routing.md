# TASK-2026-002-01

Title: Fix post-login routing to canonical destination contract  
Status: queued  
Parent Change Request: CR-2026-002  
Parent Implementation Guide: IMP-2026-002  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/signin-routing-canonical-bootstrap  
Layer: auth | services | frontend  
Module: dashboard  
Last Updated: 2026-03-21

## Objective
Ensure successful login routes users only to canonical destinations based on authoritative session + organization context, never to mock-dashboard behavior.

## Read First
- `docs/auth/routes.md`
- `docs/auth/auth-implementation-rules.md`
- `docs/services/implementation-rules.md`
- `change-requests/CR-2026-002-signin-routing-canonical-bootstrap.md`
- `implementation-guides/IMP-2026-002-signin-routing-canonical-bootstrap.md`

## Allowed Files To Change
(implementation repo)
- `middleware.ts`
- `app/(workspace)/layout.tsx`
- `src/services/auth/**`
- `src/services/organizations/**`
- `src/components/providers/app-provider.tsx` (non-authoritative fallback constraints only)

## Forbidden Files To Change
(implementation repo)
- database migrations
- feature-system catalog/permissions (unless truly required and justified)
- unrelated module components

## Acceptance Criteria
Task is complete only when:
1. login success never redirects to mock dashboard,
2. route contract holds (`/login`, `/onboarding`, `/dashboard` based on state),
3. redirect logic is server-authoritative,
4. PR includes route verification evidence and command outputs.
5. multi-org fallback selection is deterministic when current-org cookie is absent.

## Output Required From Implementer
1. changed files + commit SHA(s)
2. summary of changes
3. command outputs (lint/typecheck/build/tests if present)
4. blockers
5. risks
6. PR URL + branch name
7. deterministic multi-org fallback verification note
