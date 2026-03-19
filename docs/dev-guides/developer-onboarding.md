# Developer Onboarding

Owner: Platform Architect  
Last Updated: 2026-03-19  
Version: 1.0  
Status: Approved

## Purpose
This is the first required read for any human developer, Codex task, or AI Studio implementation flow working on Musahama.

## What the platform is
Musahama is an organization-first, module-driven, feature-gated research and discovery platform.

Core workflow:
- CRM Opportunity
- Mandate
- Research
- Strategy
- Results
- Canonical Promotion
- Export / Sync / Follow-up

## Six-layer model
- Tenancy: organizations, organization_members, profiles
- Platform: plans, modules, subscriptions, integrations, credits
- Feature: features, dependencies, provider requirements, entitlements
- Workflow: crm_opportunities, mandates, research, strategies, research_results
- Canonical Entity: companies, company_domains, contacts, contact_emails, contact_phones
- Analysis: evidence, psych_profiles, lmc_fits, dossiers

## Critical vocabulary
- modules = top-level navigation
- features = capabilities
- providers = dependencies
- entitlements = runtime truth
- workflow tables = orchestration state
- canonical entity and analysis tables = final source of truth for final UI

## Before changing anything, read
1. docs/auth/
2. docs/authorization/
3. docs/database/
4. docs/feature-system/
5. docs/services/
6. docs/frontend/
7. docs/workflows/
8. docs/dev-guides/

## Common mistakes
Do not:
- invent new top-level modules casually
- hardcode sidebar tabs
- scatter Supabase queries through page files
- treat providers as product structure
- build final pages from legacy result blobs
- duplicate permission logic across layers

## Final rule
Before making a change, decide the owning layer, the source-of-truth table(s), and the workflow impact first.