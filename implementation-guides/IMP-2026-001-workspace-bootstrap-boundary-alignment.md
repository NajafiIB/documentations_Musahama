# IMP-2026-001

Title: Implement workspace bootstrap contract and boundary alignment  
Status: in_review  
Parent Change Request: CR-2026-001  
Owner: Platform Architect  
Prepared For: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: main (or feature branch from main)  
Last Updated: 2026-03-21

Related Review: reviews/REV-2026-03-20-implementation-musahoma-intake.md; reviews/REV-2026-03-21-aistudio-workspace-bootstrap-validation.md; reviews/REV-2026-03-21-github-verification-of-aistudio-report.md  
Related Tasks: tasks/TASK-2026-001-01-workspace-bootstrap-contract.md; tasks/TASK-2026-001-02-verify-and-harden-bootstrap-implementation.md; tasks/TASK-2026-001-03-export-and-submit-pr-evidence.md  
Related PRs: TBD

## Goal
Create a single bootstrap contract for authenticated workspace context and consume it consistently across middleware/shell/runtime boundaries.

## Read First
1. `docs/auth/*`
2. `docs/authorization/*`
3. `docs/database/*`
4. `docs/feature-system/*`
5. `docs/services/*`
6. `docs/frontend/*`
7. `docs/workflows/*`
8. `docs/dev-guides/*`
9. `change-requests/CR-2026-001-workspace-bootstrap-boundary-alignment.md`
10. `reviews/REV-2026-03-20-implementation-musahoma-intake.md`

## Problem Summary
Implementation currently risks duplicating capability and routing decisions in multiple places (middleware, shell, provider). A single bootstrap contract is needed so all module visibility and access decisions flow from the correct layers.

## Architecture Rules To Respect
- `feature-system/` owns capability truth.
- `services/` own auth/org reads and DTO shaping.
- pages/routes remain thin and do not become policy engines.
- module list must stay canonical.
- no direct DB access from page components.

## Allowed Files To Change
In implementation repo only:
- `src/services/**` (bootstrap/context service contract)
- `src/feature-system/**` (resolver/runtime consumers only where needed)
- `src/components/shell/**` (consume resolved module state)
- `src/components/providers/**` (bootstrap hydration wiring)
- `middleware.ts` (only to consume central contract safely)

## Forbidden Files / Areas
- database migrations (unless explicitly requested by separate CR)
- unrelated module feature UI files
- adding new top-level modules/routes not in canonical list
- provider secret exposure to client

## Target Design
- One server-side bootstrap DTO with: user/session, org, membership state, role, enabled module keys, enabled feature keys/entitlements.
- Shell and route handling consume this DTO-derived resolver output.
- No duplicated hardcoded module visibility maps.

## Implementation Plan
1. Define/confirm bootstrap DTO contract in services.
2. Centralize module/feature resolver inputs from that contract.
3. Refactor shell navigation to rely on resolved module state only.
4. Refactor middleware checks to reuse canonical workspace route/module mapping logic.
5. Validate no direct capability logic leaks into page components.

## Validation Checklist
- Organization context is resolved correctly.
- Module visibility matches feature-system resolver outcomes.
- No hardcoded duplicate permission logic remains in shell/page layer.
- Redirect behavior remains deterministic and safe.
- No source-of-truth drift introduced.


## Evidence Gate (Required Before Marking Done)
AI Studio must provide:
- implementation repo commit SHA(s)
- full changed file list
- diff proof for each acceptance criterion
- build/typecheck/test command outputs
- explicit note on edge runtime safety for middleware imports

## Required Output From Coding Agent
1. files changed
2. what changed
3. blockers
4. risks
5. schema mismatch if any
6. docs mismatch if any
