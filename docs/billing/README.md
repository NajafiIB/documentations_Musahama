# Billing Documentation

This folder defines the canonical billing surface for Musahama.

Its purpose is to stop billing behavior from being implemented as scattered UI-only patches.

## This folder covers

- pricing and plans
- organization credit wallets and ledger-backed balance
- credit purchases and purchase status
- operation-specific credit costs
- payment-flow integrity rules
- billing architecture boundaries

## Core rules

- `billing` is the product module
- pricing and plan selection belong to the billing surface
- Stripe is a provider, not a top-level product concept
- client checkout state is never the source of truth
- verified canonical wallet, ledger, purchase, and subscription records are the source of truth
- new Free plan workspaces start with 100 credits

## Documents

- `pricing-and-plans.md`

## Read this folder when

- adding or changing a pricing page
- changing visible plan/package offerings
- changing credit purchase behavior
- changing transaction status handling
- reviewing whether billing logic is in the correct layer
