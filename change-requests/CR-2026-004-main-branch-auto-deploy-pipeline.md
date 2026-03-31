# CR-2026-004

Title: Simplify delivery to main-branch push with automatic deployment  
Status: draft  
Priority: P1  
Type: devops  
Owner: Platform Architect  
Requested By: implementation process intake  
Last Updated: 2026-03-23

Related GitHub Issue: TBD  
Related Implementation Guide: implementation-guides/IMP-2026-004-main-push-auto-deploy.md  
Related Tasks: tasks/TASK-2026-004-01-setup-main-push-workflow.md  
Related Review: reviews/REV-2026-03-23-implementation-cicd-intake.md  
Target Repo: NajafiIB/Implementation_Musahama

## Summary
Enable a simple release flow where changes pushed to `main` automatically run CI and deploy.

## Problem
Deployment currently requires manual handoff/merge/export, and automated workflow execution is not consistently configured.

## Expected Behavior
- A single GitHub Actions workflow triggers on `push` to `main`.
- Workflow runs lint/typecheck/build.
- On success, workflow deploys to target environment (Cloud Run).
- Deployment URL/environment status is visible in GitHub checks.

## Owning Layer
DevOps / delivery automation.

## Constraints
- Keep secrets out of repository.
- Use GitHub Environments/Secrets or workload identity for cloud auth.
- Do not bypass required checks for production deployment.

## Acceptance Criteria
1. The main deploy workflow exists in the implementation repository and runs on `push` to `main`.
2. CI stages (lint/typecheck/build) run before deploy.
3. Deployment stage runs only after CI success.
4. Required secrets/identity are documented.
5. README/ops note explains "how deployment works" and rollback basics.

## Risks
- Direct-to-main flow can deploy broken code if checks are weak.
- Secret misconfiguration can break deployments.

## Final Decision
- pending implementation
