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

## Acceptance criteria
What must be true when done?

## Status
pending-review
