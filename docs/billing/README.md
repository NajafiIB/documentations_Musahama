# Billing Documentation

This folder defines the canonical billing surface for Musahama.

Its purpose is to stop billing behavior from being implemented as scattered UI-only patches.

## This folder covers

- pricing and plans
- credits as the current spendable balance model
- transaction recording and status
- payment-flow integrity rules
- billing architecture boundaries

## Core rules

- `billing` is the product module
- pricing and plan selection belong to the billing surface
- Stripe is a provider, not a top-level product concept
- client checkout state is never the source of truth
- verified canonical database state is the source of truth

## Documents

- `pricing-and-plans.md`

## Read this folder when

- adding or changing a pricing page
- changing visible plan/package offerings
- changing credit purchase behavior
- changing transaction status handling
- reviewing whether billing logic is in the correct layer
