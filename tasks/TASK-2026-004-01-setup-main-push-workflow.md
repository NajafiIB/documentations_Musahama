# TASK-2026-004-01

Title: Set up push-to-main automatic deployment workflow  
Status: queued  
Parent Change Request: CR-2026-004  
Parent Implementation Guide: IMP-2026-004  
Owner: Platform Architect  
Assigned To: AI Studio  
Target Repo: NajafiIB/Implementation_Musahama  
Target Branch: main  
Layer: devops  
Module: cross-module  
Last Updated: 2026-03-23

## Objective
Enable automatic deploy on every `main` push with mandatory verify checks beforehand.

## Read First
- `reviews/REV-2026-03-23-implementation-cicd-intake.md`
- `change-requests/CR-2026-004-main-branch-auto-deploy-pipeline.md`
- `implementation-guides/IMP-2026-004-main-push-auto-deploy.md`

## Allowed Files To Change
(implementation repo)
- `.github/workflows/**`
- deployment helper scripts
- `README.md` (deployment section)

## Forbidden Files To Change
(implementation repo)
- application business logic
- database schema/migrations
- any plaintext secret files

## Acceptance Criteria
Task is complete only when:
1. workflow runs on `push` to `main`,
2. verify stage (lint/typecheck/build) gates deployment,
3. deploy stage executes only after verify success,
4. environment secrets/identity setup is documented,
5. one successful run link is attached in evidence.

## Output Required From Implementer
1. changed files + full SHA(s)
2. PR URL + compare URL
3. workflow run link (success)
4. verify command outputs
5. blockers
6. risks
