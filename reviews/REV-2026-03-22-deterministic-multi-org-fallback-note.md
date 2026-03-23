# Review — Deterministic Multi-Org Fallback Ordering Note (2026-03-22)

## Context
Inline feedback requested deterministic active-membership ordering so multi-org fallback does not drift between requests.

## Assessment
The proposed change (`.order("organization_id", { ascending: true })` in active-membership loading) is architecture-aligned and should be retained.

## Why It Matters
Without deterministic ordering, selecting `organizations[0]` for fallback can change across requests, causing tenant context drift (different org entitlements/data surfaced for the same user).

## Required Verification in Implementation PR
1. Query-level deterministic ordering exists in active-membership loader.
2. Fallback selection logic documents why first-result selection is deterministic.
3. Middleware/layout bootstrap behavior remains server-authoritative.
4. Multi-org users route deterministically when current-org cookie is absent.

## Decision
- Accept this fix directionally.
- Keep final acceptance gated on auditable PR evidence (full SHA + URL + diff + command outputs).
