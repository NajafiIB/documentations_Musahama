# CR-2026-001

Title: Workspace bootstrap boundary alignment (implementation repo)  
Status: in_review  
Priority: P1  
Type: refactor  
Owner: Platform Architect  
Requested By: Codex review intake  
Last Updated: 2026-03-21

Related GitHub Issue: TBD  
Related Implementation Guide: implementation-guides/IMP-2026-001-workspace-bootstrap-boundary-alignment.md  
Related Tasks: tasks/TASK-2026-001-01-workspace-bootstrap-contract.md; tasks/TASK-2026-001-02-verify-and-harden-bootstrap-implementation.md  
Related Review: reviews/REV-2026-03-20-implementation-musahoma-intake.md; reviews/REV-2026-03-21-aistudio-workspace-bootstrap-validation.md; reviews/REV-2026-03-21-github-verification-of-aistudio-report.md  
Target Repo: NajafiIB/Implementation_Musahama

## Summary
Align implementation bootstrap/auth/module visibility flow with documentation boundaries before expanding module features.

## Problem
Current implementation has signs of hardcoded workspace routing/navigation behavior and static workflow UI slices. This can drift from feature-system resolver truth and service boundaries.

## Expected Behavior
A single bootstrap flow should resolve session, organization context, role, enabled modules, and feature entitlements through services + feature-system runtime. Shell and guards should consume resolved state rather than local hardcoded lists.

## Owning Layer
Cross-layer with clear ownership:
- auth + organization context in services/server bootstrap
- capability truth in feature-system
- rendering in frontend shell/pages

## Affected Area
Modules: cross-module (workspace shell), research (initial impact)  
Workflow stage: platform bootstrap to module access  
Roles: all authenticated roles

## Source-of-Truth Check
- Module and feature runtime truth: `feature-system/`
- Data and auth context reads: `services/`
- UI rendering only: shell/components/pages

## Constraints
- Do not invent new top-level modules.
- Do not move capability decisions into page components.
- Do not add direct DB queries to pages/components.
- Keep RLS/security assumptions intact.

## Acceptance Criteria
1. Workspace bootstrap data contract is defined and used consistently.
2. Sidebar visibility is derived from resolved module state only.
3. Route guard behavior references canonical module/access contract rather than duplicated hardcoded lists.
4. Research page remains module UI only; no architecture logic duplicated there.
5. Docs and implementation guidance remain aligned.

## Risks
- Refactor may temporarily affect redirect behavior.
- If bootstrap contract is underspecified, later tasks can reintroduce drift.

## Final Decision
- in_review (pending evidence from implementation repo and hardening follow-up task)
