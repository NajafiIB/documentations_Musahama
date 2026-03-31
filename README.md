# Musahama Developer Documentation

This repository is the canonical developer documentation home for the Musahama platform.

It documents the **current implemented platform**:

- platform kernel and workspace shell
- auth and authorization rules
- module catalog and grouped navigation
- shared company and contact entities
- reusable capabilities
- module runtime plane
- paid data packs and dataset bindings
- service boundaries
- developer workflow and documentation rules

It also contains the canonical delivery artifacts used to move work from issue intake through implementation, QA, and closure:

- `change-requests/`
- `implementation-guides/`
- `tasks/`
- `reviews/`
- `cases/`

## Current Official Top-Level Areas

The live platform is organized into these top-level areas:

- `dashboard`
- `approvals`
- `activity`
- `origination_match`
- `partner_match`
- `negotiator`
- `compliance_guardian`
- `funding_orchestrator`
- `companies`
- `contacts`
- `integrations`
- `data_packs`
- `billing`
- `settings`

Legacy workflow routes still exist for compatibility:

- `mandates`
- `research`
- `results`

The legacy `crm_opportunities` module remains in the catalog for compatibility history, but it is not currently an active workspace route.

## Read Order

Developers and coding agents should read the docs in this order:

1. `docs/architecture/overview.md`
2. `docs/auth/`
3. `docs/authorization/`
4. `docs/feature-system/module-catalog.md`
5. `docs/platform-runtime/runtime-plane.md`
6. `docs/database/source-of-truth-rules.md`
7. `docs/frontend/workspace-shell.md`
8. `docs/services/services-foundation.md`
9. `docs/dev-guides/start-here.md`

## Site Tooling

This docs set is published as a standalone docs site using:

- MkDocs
- MkDocs Material
- GitHub Pages

Core entrypoints:

- `mkdocs.yml`
- `docs/`
- `specs/`

## Source-of-Truth Rule

The order of truth is:

1. current implementation
2. synced docs and specs
3. change requests and implementation guides
4. tasks, reviews, and case manifests
5. conversations

If the implementation and docs disagree, update one of them explicitly. Do not leave the mismatch unresolved.
