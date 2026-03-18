# Change Request Process

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how bugs, structural fixes, and feature changes should be captured before implementation.

---

## 2. Core Rule

Do not ask the coding agent to “just fix it” without a clear change request.

Every meaningful change should begin with a documented request.

---

## 3. Change Request Template

Use this structure:

```md
# CR-YYYY-NNN
Title: <short clear title>

## Problem
What is wrong?

## Expected behavior
What should happen instead?

## Scope
Which module/workflow/layer is affected?

## Suspected files or areas
List likely files or folders.

## Constraints
What must not change?
What boundaries must be respected?
4. Required Statuses

Recommended statuses:

draft

pending-review

approved

in-progress

blocked

done

rejected

5. When To Create One

Create a change request for:

architecture fixes

auth or org context bugs

role/permission issues

workflow mismatches

data model issues

structural UI fixes

non-trivial feature changes

Minor typo-only changes do not need a full CR.

6. Good Examples

Examples of CR-worthy work:

sidebar shows modules for the wrong role

results detail is reading legacy blobs instead of normalized tables

AI Studio patched a page and bypassed services

integrations page leaks provider-specific logic into UI structure

org onboarding flow conflicts with invitation model

7. Approval Rule

A change request should be reviewed against:

docs/*

current repo structure

workflow impact

security/boundary impact

No implementation should begin until the change is clear.

8. Final Rule

The change request defines the target.
The coding agent implements the target.

## Acceptance criteria
What must be true when done?

## Status
pending-review
