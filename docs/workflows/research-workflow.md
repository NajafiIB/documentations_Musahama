# Research Workflow

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how research runs are created, managed, and executed.

---

## 2. Role in the Product

Research is the execution stage of the workflow.

It takes:
- a mandate
- targeting rules
- exclusions
- supporting context

and produces:
- strategies
- candidate results
- status/progress information

---

## 3. Main Flow

### Step 1 — Create research run
Create a `research` record linked to a mandate.

### Step 2 — Load context
Use:
- mandate objective
- files
- research constraints
- relevant organization context

### Step 3 — Generate or author strategies
Create one or more `strategies` records.

Strategies define the planned search/execution approach.

### Step 4 — Execute research
Run the research process.

### Step 5 — Produce candidate outputs
Write candidate outputs into `research_results`.

### Step 6 — Track progress and status
Keep research and strategy execution state visible to the user.

### Step 7 — Handoff to results review
The user moves into the Results module to inspect and act on produced outputs.

---

## 4. Important Module Boundary

### Research is a top-level module
It owns:
- research archive
- research detail
- strategy generation
- execution progress

### Strategies are not a top-level module
They are a subview of research.

### Results are a separate top-level module
They are the review/action stage after research execution.

---

## 5. Expected UI Surface

### Research archive
- research list
- filters
- create/start research

### Research detail
- goal
- rules
- exclusions
- strategies
- status/progress
- actions:
  - generate strategies
  - re-run
  - stop/cancel if supported

---

## 6. Data Touchpoints

Primary tables:
- research
- strategies
- research_constraints
- research_results

Upstream references:
- mandates
- mandate_files

Downstream references:
- companies
- contacts
- evidence
- psych_profiles
- lmc_fits
- dossiers

---

## 7. Capability Examples

Typical feature keys:
- research.start
- research.generate_strategies
- research.background_processing

These capabilities must still be resolved through the feature-system.

---

## 8. Hard Rules

1. strategies belong inside research, not as a separate module
2. research detail is about execution state, not final result review
3. research results are workflow outputs, not final canonical company/contact records
4. research constraints must remain structured, not hidden only inside freeform text
5. research must remain linked to its originating mandate

---

## 9. Output of This Workflow Stage

The output is:
- completed or in-progress research state
- strategies
- candidate research results

The primary downstream handoff is into the Results workflow.
