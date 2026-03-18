# Organization Onboarding

---

## Purpose

Guide new users through creating their first organization.

---

## Flow

1. User signs up
2. User lands on onboarding
3. User enters:
   - organization name
4. System creates:
   - organization
   - membership (owner)
5. Default modules enabled
6. Redirect to dashboard

---

## Rules

- onboarding must run only once
- user cannot skip onboarding without org
- organization name must be unique (optional)

---

## Edge Cases

- user abandons onboarding → block workspace
- user refreshes → resume onboarding
