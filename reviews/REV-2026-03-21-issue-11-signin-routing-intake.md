# Review — Issue #11 Sign-in Routing Intake (2026-03-21)

## Source
GitHub issue: `NajafiIB/documentations_Musahama#11` — "[CR] The signin process is not working correcty".

## Problem Statement (normalized)
After successful login, users are being routed to a mock dashboard path/state instead of deterministic post-login routing based on organization context.

## Expected Routing Contract
Post-login routing must follow documented auth rules:
1. no session -> `/login`
2. session + no active organization context -> `/onboarding`
3. session + active organization context -> `/dashboard`

## Suspected Owning Layer
Primary: `auth` + `services` + server routing/bootstrap boundary.

## Why this is architecture-critical
If post-login routing is decided by page-local/mocked UI logic, implementation drifts from canonical auth + organization bootstrap behavior.

## Recommended Execution Mode
- Create bounded implementation task in implementation repo.
- Prohibit mock-dashboard fallback in post-login flow.
- Enforce deterministic server-first redirect behavior.
