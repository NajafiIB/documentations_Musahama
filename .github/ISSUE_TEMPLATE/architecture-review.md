---
name: Architecture Review
about: Request a structural review of a proposed or existing implementation
title: "[Review] "
labels: ["architecture-review"]
assignees: []
---

# Summary

What needs to be reviewed?

---

## Review Type

- [ ] proposed design review
- [ ] existing implementation review
- [ ] bug root-cause review
- [ ] repo consistency review
- [ ] docs vs implementation mismatch review

---

## Scope

Which layer(s) are involved?

- [ ] auth
- [ ] authorization
- [ ] database
- [ ] feature-system
- [ ] services
- [ ] frontend
- [ ] workflow
- [ ] integrations
- [ ] billing

---

## Review Goal

What question should be answered?

Examples:
- is the role logic in the correct layer?
- is the results page using the wrong source of truth?
- should this be a module or a feature?
- does this PR violate the service boundary?

---

## Links / References

Add links to:
- branch / PR
- issue
- relevant docs
- screenshots
- files or folders

---

## Suspected Risk

- [ ] wrong source of truth
- [ ] wrong layer ownership
- [ ] duplicated permission logic
- [ ] workflow mismatch
- [ ] provider/product concept confusion
- [ ] page-level query sprawl
- [ ] security / RLS gap
- [ ] new fake module introduced
- [ ] docs drift

---

## Files / Areas to Inspect

List the most relevant files or folders.

---

## Expected Output

The reviewer should answer:

- what is wrong or correct
- which layer owns the fix
- which files should change
- which files must not change
- what docs must be updated
- what risks remain

---

## Acceptance Criteria for Review Completion

- [ ] owning layer identified
- [ ] source-of-truth identified
- [ ] recommended change path identified
- [ ] risk areas called out
- [ ] docs impact identified
