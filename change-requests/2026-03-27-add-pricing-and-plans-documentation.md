# Change Request — Add Pricing and Plans Documentation

## Status
- done

## Problem

The repository already recognizes `billing` as an official top-level module, but pricing, plans, credits, and transaction behavior are not documented as a canonical billing surface.

That gap makes implementation drift likely.

## Expected behavior

The documentation repository must define:

- what the pricing/plans surface is responsible for
- the difference between product concepts and provider concepts
- the canonical source of truth for credits and transactions
- the required payment flow from plan selection to verified credit update
- the architectural ownership boundaries for billing behavior

## Affected layer

- documentation
- billing module definition
- service boundary clarification
- database source-of-truth clarification

## Affected areas

- `docs/billing/`

## Constraints

- keep the billing module as product structure
- do not treat Stripe as the architecture truth
- do not invent full subscription architecture beyond the currently documented credits and transaction model
- keep the rules consistent with existing module, feature-system, service, and database principles

## Acceptance criteria

- `docs/billing/README.md` exists
- `docs/billing/pricing-and-plans.md` exists
- pricing, plans, credits, and transactions are described in canonical terms
- source-of-truth rules are explicit
- the payment/credit flow is explicit
- the anti-patterns are explicit

## Notes

This change is documentation-first. It does not change production billing behavior by itself.
