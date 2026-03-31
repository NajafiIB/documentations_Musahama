# Module Page Contracts

Owner: Platform Architect
Last Updated: 2026-03-31
Version: 1.1
Status: Approved

## Purpose

Define the baseline page contract for each primary workspace area plus the retained compatibility surfaces that are still part of the live route tree.

## Dashboard
- route: /dashboard
- purpose: overview, summaries, quick actions

## Approvals
- route: /approvals
- purpose: review approval-gated external actions across all modules

## Activity
- route: /activity
- purpose: workspace-wide feed of recent actions, runs, and state changes

## Origination Match
- routes:
  - /origination-match
  - /origination-match/mandates
  - /origination-match/research
  - /origination-match/results
- compatibility routes:
  - /mandates
  - /mandates/[id]
  - /mandates/[id]/strategies/[strategyId]
  - /research
  - /research/[id]
  - /research/search
  - /results
  - /results/[id]
- purpose: own the origination workflow bridge and its report surface

## Supplier Development Program
- routes:
  - /supplier-development-program
  - /supplier-development-program/cases
  - /supplier-development-program/cases/[caseId]
  - /supplier-development-program/catalog
- purpose: manage spend-led supplier prioritization, case operations, and reporting

## Partner Match
- route: /partner-match
- purpose: partner-oriented solution shell

## Negotiator
- route: /negotiator
- purpose: negotiation solution shell

## Compliance Guardian
- route: /compliance-guardian
- purpose: compliance review solution shell

## Funding Orchestrator
- route: /funding-orchestrator
- purpose: funding workflow solution shell

## Mandates
- routes:
  - /mandates
  - /mandates/[id]
- purpose: define and manage mandates

## Research
- routes:
  - /research
  - /research/[id]
- purpose: execute research runs and manage strategies

## Results
- routes:
  - /results
  - /results/[id]
- purpose: review outputs, shortlist, export, inspect linked canonical records

## Companies
- routes:
  - /companies
  - /companies/[id]
- purpose: canonical company archive and detail

## Contacts
- routes:
  - /contacts
  - /contacts/[id]
- purpose: canonical contact archive and detail

## Integrations
- canonical routes:
  - /settings/integrations
  - /settings/integrations/[providerKey]
- compatibility routes:
  - /integrations
  - /integrations/[providerKey]
- purpose: provider configuration, bindings, and connection health

## Data Packs
- canonical route: /settings/data-sources
- compatibility route: /data-packs
- purpose: purchased data readiness and source catalog management

## Billing
- canonical route: /settings/plan-billing
- compatibility route: /billing
- purpose: subscription, module add-ons, and usage-aware billing management

## Settings
- routes:
  - /settings
  - /settings/workspace
  - /settings/solutions
  - /settings/integrations
  - /settings/data-sources
  - /settings/usage
  - /settings/plan-billing
  - /settings/account
- internal operator routes:
  - /settings/view-standard
  - /settings/delivery-orchestrator
- purpose: workspace administration, account settings, and internal operator tooling

## CRM Opportunities
- route: /crm-opportunities
- purpose: hidden legacy catalog entry retained for compatibility history, not an active workspace route

## Rule

Top-level pages must align with canonical module keys and route ownership.
