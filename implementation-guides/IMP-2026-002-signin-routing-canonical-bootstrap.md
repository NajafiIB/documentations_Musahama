# IMP-2026-002

Title: Implement canonical post-login routing and remove mock-dashboard fallback  
Status: in_review  
Status: draft  
Parent Change Request: CR-2026-002  
Owner: Platform Architect  
Prepared For: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/signin-routing-canonical-bootstrap  
Last Updated: 2026-03-23

Related Review: reviews/REV-2026-03-21-issue-11-signin-routing-intake.md; reviews/REV-2026-03-23-forgot-password-flow-audit.md; reviews/REV-2026-03-23-forgot-password-closure-recheck.md; reviews/REV-2026-03-23-signup-existing-user-message-audit.md  
Related Tasks: tasks/TASK-2026-002-01-fix-post-login-routing.md; tasks/TASK-2026-002-02-harden-forgot-reset-password-flow.md; tasks/TASK-2026-002-03-signup-existing-user-message.md  
Last Updated: 2026-03-21

Related Review: reviews/REV-2026-03-21-issue-11-signin-routing-intake.md  
Related Tasks: tasks/TASK-2026-002-01-fix-post-login-routing.md  
Related PRs: TBD

## Goal
Make post-login routing deterministic and canonical by session + organization bootstrap context; remove any mock-dashboard routing outcome.

## Read First
1. `docs/auth/routes.md`
2. `docs/auth/auth-implementation-rules.md`
3. `docs/services/implementation-rules.md`
4. `docs/authorization/implementation-rules.md`
5. `docs/frontend/frontend-foundation.md`
6. `docs/workflows/implementation-rules.md`
7. `change-requests/CR-2026-002-signin-routing-canonical-bootstrap.md`

## Problem Summary
Issue #11 indicates authenticated users can be forwarded to mock dashboard behavior. Routing must instead be resolved server-first from canonical auth + org context state.

## Architecture Rules To Respect
- session/org resolution is server-side authoritative,
- pages remain thin,
- no capability logic in random components,
- no client-only routing hacks for security behavior.

## Allowed Files To Change
(implementation repo)
- `middleware.ts`
- `app/(workspace)/layout.tsx`
- `src/services/auth/**`
- `src/services/organizations/**`
- `src/components/providers/app-provider.tsx` (only if fallback logic must be constrained)

## Forbidden Files / Areas
- database schema/migrations
- unrelated module feature files
- introducing new top-level module routes

## Target Design
- Single authoritative decision tree for post-login destination.
- If multi-org selection exists, handle it explicitly and deterministically.
- No path should route to mock dashboard on successful auth.

## Implementation Plan
1. Trace current login success redirect path(s).
2. Centralize destination decision in server bootstrap/middleware path.
3. Remove mock-dashboard fallback logic.
4. Keep client fallback non-authoritative.
5. Add route verification checklist in PR.

## Validation Checklist
- login with no valid session -> `/login`
- login with valid session but missing org/membership -> `/onboarding`
- login with active org context -> `/dashboard`
- no mock-dashboard route/state is reachable from login success path
- reset-password recovery link flow has explicit success/error handling
- signup existing-user outcome avoids misleading confirmation-email success copy

## Required Output From Coding Agent
1. changed files
2. what changed
3. blockers
4. risks
5. command outputs (lint/typecheck/build)
6. route verification proof (manual or automated)
7. docs mismatch if any
