# Workflow State Models

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the recommended baseline state model for workflow records.

These state models give developers a stable implementation target.
If schema enums differ, service adapters must keep behavior aligned with these workflow meanings.

---

## 2. CRM Opportunities

Recommended statuses:
- imported
- new
- reviewed
- converted
- archived
- sync_error

Meaning:
- imported/new -> entered the system
- reviewed -> checked and qualified
- converted -> used to create mandate
- archived -> no longer active
- sync_error -> source/import issue exists

---

## 3. Mandates

Recommended statuses:
- draft
- ready
- active
- paused
- completed
- archived

Meaning:
- draft -> being defined
- ready -> prepared for research
- active -> currently in use
- paused -> intentionally stopped
- completed -> work concluded
- archived -> retained but inactive

---

## 4. Research

Recommended statuses:
- draft
- queued
- running
- completed
- failed
- canceled

Meaning:
- draft -> defined but not executing
- queued -> waiting to run
- running -> actively executing
- completed -> execution finished
- failed -> execution failed
- canceled -> intentionally stopped

---

## 5. Strategies

Recommended statuses:
- draft
- ready
- running
- completed
- failed

Meaning:
- draft -> authored/generated but not active
- ready -> approved for execution
- running -> in execution
- completed -> finished
- failed -> failed during execution

---

## 6. Research Results

Recommended review statuses:
- new
- reviewed
- shortlisted
- dismissed
- exported

Meaning:
- new -> produced but not yet reviewed
- reviewed -> seen and evaluated
- shortlisted -> marked as promising
- dismissed -> intentionally not pursued
- exported -> used in export or downstream package flow

Important note:
exported is a workflow convenience state if adopted.
Export action tracking may also live separately if needed.

---

## 7. Constraints

Constraints are usually structured rules rather than heavy lifecycle records.
Keep them simple and explicit.

Examples:
- active
- archived

---

## 8. Hard Rules

1. workflow status must not exist only in local UI state
2. status transitions must happen through services
3. status names should map to real business meaning
4. pages should not invent new unofficial statuses ad hoc
