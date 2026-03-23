# IMP-2026-004

Title: Configure main-push CI/CD workflow for automatic deployment  
Status: draft  
Parent Change Request: CR-2026-004  
Owner: Platform Architect  
Prepared For: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: main  
Last Updated: 2026-03-23

Related Review: reviews/REV-2026-03-23-implementation-cicd-intake.md  
Related Tasks: tasks/TASK-2026-004-01-setup-main-push-workflow.md  
Related PRs: TBD

## Goal
Make deployment fully automatic on `main` pushes with clear pre-deploy checks and simple operational controls.

## Read First
1. `docs/dev-guides/github-ruleset-setup.md`
2. `docs/dev-guides/testing-guidelines.md`
3. `change-requests/CR-2026-004-main-branch-auto-deploy-pipeline.md`

## Target Design
- Workflow file: `.github/workflows/deploy-main.yml`
- Trigger: `on: push` for branch `main`
- Jobs:
  1) `verify` (lint/typecheck/build)
  2) `deploy` (needs `verify`)
- Deployment auth via GitHub OIDC + cloud provider identity (preferred) or encrypted secrets.

## Allowed Files To Change
(implementation repo)
- `.github/workflows/**`
- deployment scripts/config referenced by workflow
- `README.md` deployment section

## Forbidden Files / Areas
- hardcoded cloud credentials
- unrelated feature/business logic

## Implementation Plan
1. Add `deploy-main.yml` with verify and deploy jobs.
2. Configure environment/secrets/identity references.
3. Add concurrency guard to avoid overlapping deploys.
4. Add failure-fast behavior and artifact/log upload.
5. Update README with required secrets and rollback command.

## Validation Checklist
- push to `main` starts workflow automatically,
- failed verify job blocks deploy,
- successful workflow updates deployment,
- logs clearly show image/tag and deployed revision.

## Required Output From Coding Agent
1. changed files + full SHA(s)
2. PR URL + compare URL
3. sample successful workflow run link
4. command outputs for verify steps
5. blockers/risks
