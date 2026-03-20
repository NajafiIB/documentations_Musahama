# TASK-2026-001-01

Title: Implement workspace bootstrap contract and remove hardcoded module access duplication  
Status: queued  
Parent Change Request: CR-2026-001  
Parent Implementation Guide: IMP-2026-001  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: feature/workspace-bootstrap-contract  
Layer: auth | authorization | services | feature-system | frontend  
Module: cross-module  
Last Updated: 2026-03-20

## Objective
Implement one reusable bootstrap contract for authenticated workspace context and use it as the single source for module visibility and route access decisions.

## Read First
- `docs/auth/auth-implementation-rules.md`
- `docs/authorization/implementation-rules.md`
- `docs/feature-system/implementation-rules.md`
- `docs/services/implementation-rules.md`
- `docs/frontend/frontend-foundation.md`
- `docs/workflows/implementation-rules.md`
- `change-requests/CR-2026-001-workspace-bootstrap-boundary-alignment.md`
- `implementation-guides/IMP-2026-001-workspace-bootstrap-boundary-alignment.md`

## Allowed Files To Change
(implementation repo)
- `src/services/**`
- `src/feature-system/**`
- `src/components/providers/**`
- `src/components/shell/**`
- `middleware.ts`

## Forbidden Files To Change
(implementation repo)
- `database/migrations/**`
- unrelated feature module files outside bootstrap scope
- route/module additions not in canonical module catalog

## Acceptance Criteria
The task is complete only when:
1. bootstrap DTO is defined and consumed consistently,
2. sidebar/module visibility is resolver-driven,
3. route access checks are no longer maintained as duplicated hardcoded lists,
4. no direct DB queries are added to page components,
5. output includes changed files, blockers, risks, and mismatches.

## Output Required From Implementer
1. changed files
2. summary of changes
3. blockers
4. risks
5. follow-up tasks if needed
