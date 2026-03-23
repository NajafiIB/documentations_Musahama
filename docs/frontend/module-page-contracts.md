# Module Page Contracts

Owner: Platform Architect
Last Updated: 2026-03-20
Version: 1.0
Status: Approved

## Purpose

Define the baseline page contract for each top-level module.

## Dashboard
- route: /dashboard
- purpose: overview, summaries, quick actions

## CRM Opportunities
- route: /crm-opportunities
- purpose: opportunity archive and conversion entry into mandates

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
- route: /integrations
- purpose: provider configuration and health

## Billing
- route: /billing
- purpose: subscription and credits management

## Settings
- route: /settings
- purpose: personal, organization, and administrative settings

## Rule

Top-level pages must align with canonical module keys and route ownership.
