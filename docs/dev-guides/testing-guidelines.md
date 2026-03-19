# Testing Guidelines

Owner: Platform Architect  
Last Updated: 2026-03-19  
Version: 1.0  
Status: Approved

## Purpose
Define the testing discipline for the Musahama platform.

## Required test levels
- unit tests for pure helpers, DTO mappers, role/module/feature rules
- integration tests for services, org bootstrap, runtime resolvers, mutations, route guards
- e2e tests for login, onboarding, org selection, sidebar visibility, workflow progression, restricted access

## Must be tested
- auth and tenancy
- module visibility by role and organization
- feature disabled states and reason codes
- workflow transitions from CRM to mandate to research to results
- source-of-truth reads from canonical entity and analysis tables
- server-only sanitization for billing and integrations

## Anti-patterns
Do not rely only on:
- snapshots
- single-role tests
- happy-path mocks
- UI-only permission tests

## Final rule
If a feature is role-aware, org-aware, or provider-aware, it needs integration coverage.