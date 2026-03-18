# View Framework

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define the reusable page/view system used across the product.

The UI must use repeatable patterns rather than building every page from scratch.

---

## 2. Core View Types

Every major feature/module must support three base view types:

- inline
- detail
- form

---

## 3. Inline Variants

Inline views may render as:
- table
- cards
- chart
- compact-list

The correct choice depends on the module’s use case, but the pattern should stay consistent.

---

## 4. Placement Modes

Views may appear in these placements:
- sidebar
- main
- embedded
- modal
- drawer
- hidden

These placements should be treated as standard framework options, not ad hoc page inventions.

---

## 5. Folder Structure for Views

```text
src/views/
  framework/
  inline/
  detail/
  form/
