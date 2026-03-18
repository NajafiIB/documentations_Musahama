# Mandates Workflow

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how mandates are created, refined, and handed off into research.

---

## 2. Role in the Product

A mandate is the formal search or target definition for the organization.

It is the bridge between:
- opportunity intake
and
- research execution

---

## 3. Mandate Origins

A mandate may be created from:

- CRM opportunity conversion
- manual creation
- future approved service flows

---

## 4. Main Flow

### Step 1 — Create mandate
Create a `mandates` record.

### Step 2 — Define objective
Set the mandate goal, scope, and targeting intent.

### Step 3 — Add context
Attach:
- files
- notes
- business context
- supporting documents

### Step 4 — Add constraints
Define exclusions, constraints, or rules that shape research.

### Step 5 — Review readiness
Confirm the mandate is ready to execute.

### Step 6 — Start research
Launch one or more research runs from the mandate.

---

## 5. Expected UI Surface

### Archive/List
- mandate table/list
- filters
- create new mandate

### Detail
- mandate summary
- attached files
- constraints/exclusions
- linked research runs
- actions:
  - edit
  - archive
  - start research

---

## 6. Data Touchpoints

Primary tables:
- mandates
- mandate_files
- research_constraints

Downstream linked tables:
- research
- strategies
- research_results

---

## 7. Relationship to Research

A mandate is not the research run itself.

A mandate defines the target and context.
Research executes against that mandate.

One mandate may lead to:
- zero research runs yet
- one active research run
- multiple research runs over time

---

## 8. Hard Rules

1. mandate files belong to mandate context, not directly to research results
2. constraints must not live only inside prompt text or UI state
3. research must be linked to a mandate
4. mandate detail must show linked research runs
5. manual and CRM-origin mandates must converge into the same workflow model

---

## 9. Output of This Workflow Stage

The output is:
- a research-ready mandate
- and then one or more research runs launched from that mandate
