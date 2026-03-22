# CR-2026-002

Title: Fix sign-in post-login routing to canonical org bootstrap behavior  
Status: draft  
Priority: P1  
Type: bug  
Owner: Platform Architect  
Requested By: Issue #11 intake  
Last Updated: 2026-03-21

Related GitHub Issue: https://github.com/NajafiIB/documentations_Musahama/issues/11  
Related Implementation Guide: implementation-guides/IMP-2026-002-signin-routing-canonical-bootstrap.md  
Related Tasks: tasks/TASK-2026-002-01-fix-post-login-routing.md  
Related Review: reviews/REV-2026-03-21-issue-11-signin-routing-intake.md  
Target Repo: NajafiIB/Implementation_Musahama

## Summary
Ensure login success routes users deterministically by session + organization context; eliminate mock-dashboard fallback behavior.

## Problem
Users are authenticated but can land on a mock dashboard path/state rather than canonical destination based on organization membership/context.

## Expected Behavior
After login:
- unauthenticated -> `/login`
- authenticated without org context/membership -> `/onboarding`
- authenticated with active org context -> `/dashboard`

## Owning Layer
- Auth/session resolution: auth/services (server-side)
- Org context resolution: services/bootstrap
- Redirect enforcement: middleware + workspace/server layout

## Affected Area
Modules: dashboard, settings, billing (entry visibility affected)  
Workflow: authentication -> organization bootstrap -> workspace entry

## Source-of-Truth Check
Routing decision must consume canonical auth + org context services, not mock UI state.

## Constraints
- Do not add client-only redirect hacks.
- Do not hardcode role checks in page components.
- Do not bypass existing feature-system/runtime boundaries.

## Acceptance Criteria
1. Successful login never routes to mock dashboard state.
2. Redirect outcomes strictly follow session/org context contract.
3. Middleware and/or server layout enforce deterministic behavior.
4. Evidence includes diff, test/build outputs, and route verification steps.

## Risks
- Regression risk around multi-organization selection path.
- Duplicate redirect logic between middleware and client providers.

## Final Decision
- pending implementation
