# Workflow State Models

Owner: Platform Architect
Last Updated: 2026-03-20
Version: 1.0
Status: Approved

## Purpose

Define the recommended lifecycle states for workflow records.

## CRM Opportunities
Recommended statuses:
- imported
- new
- reviewed
- converted
- archived
- sync_error

## Mandates
Recommended statuses:
- draft
- ready
- active
- paused
- completed
- archived

## Research
Recommended statuses:
- draft
- queued
- running
- completed
- failed
- canceled

## Strategies
Recommended statuses:
- draft
- ready
- running
- completed
- failed

## Research Results
Recommended review statuses:
- new
- reviewed
- shortlisted
- dismissed
- exported

## Rules

- workflow status must not live only in UI state
- state transitions must happen through services
- pages must not invent unofficial statuses
