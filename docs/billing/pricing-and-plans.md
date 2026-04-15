# Pricing, Plans, and Credits

This document defines the canonical pricing and plans model for Musahama.

It exists to prevent a common failure mode:

- a pricing page gets added
- a payment provider widget works visually
- credits appear to change somewhere in the UI
- but there is no clear source-of-truth or architecture rule for what actually happened

That is not acceptable.

---

# 1. Scope

This document covers:

- the pricing surface
- visible plans or packages
- credit purchases
- transaction recording
- post-payment state
- billing-layer ownership
- source-of-truth rules for balance and purchase history

This document describes the current implemented credits, subscriptions, Stripe checkout, and operation-cost model. It replaces older assumptions that used `profiles.credits` and `transactions` as the billing source of truth.

---

# 2. Canonical product concepts

Use these terms precisely.

## Billing module
The official product/module area for pricing, payment state, balances, and transaction history.

## Pricing page
The user-facing surface where available plans or packages are displayed and selected.

## Plans / packages
Commercial offerings shown to the user.

In the current documented model, a plan/package may represent one of these:

- a credit bundle
- a prepaid usage package
- another clearly defined billing offer

Do not leave plan meaning ambiguous in implementation.

## Credits
The spendable balance model used by runtime actions.

## Credit wallet
The organization-scoped current balance.

## Credit ledger
The auditable transaction trail for grants, purchases, reservations, releases, and charges.

## Operation cost
The configured credit price for a specific runtime action.

## Provider
The external payment system.

Example:

- Stripe

Provider is a dependency. It is not the product/module structure.

---

# 3. Current implemented state

The current implemented application state assumes:

- users open billing through `/settings/plan-billing`
- users can buy credit packs through Stripe Checkout
- users can manage subscription plans and module access through Plan & Billing
- the current credit balance is organization-scoped, not profile-scoped
- purchases are tracked through billing purchase records and ledger entries
- runtime usage is charged through operation cost keys and wallet reservations
- credit admin users can inspect wallets, reservations, ledger entries, and pricing rules
- new Free plan workspaces start with 100 credits

---

# 4. Source-of-truth rules

## Final source of truth for current balance

- organization credit wallet and ledger records

## Final source of truth for purchase / billing history

- billing purchase records
- Stripe webhook verified events
- credit ledger records

## Final source of truth for operation pricing

- credit operation catalog configuration in services
- persisted credit cost model rules where available for admin/runtime review

## Not source of truth

These must **not** be treated as canonical truth:

- the client checkout state
- provider UI state
- pricing table embed state
- success-screen rendering alone
- local component state
- sidebar button state
- stale user profile credit fields

A payment provider can report an event.
The product must still resolve canonical truth from the application data model.

---

# 5. Required pricing and payment flow

The canonical flow is:

1. an authenticated user opens the billing/pricing surface
2. the user sees available plans/packages
3. the user selects a plan/package
4. the payment provider checkout flow begins
5. the provider returns a result or triggers a verification path
6. the application verifies the payment outcome in the correct service boundary
7. the application writes or updates purchase records
8. the credit wallet is updated through ledger-backed service logic only after verified success
9. the UI reloads from canonical database state

Do not skip the verification step.

---

# 6. Minimum purchase status model

The minimum expected status vocabulary is:

- `pending`
- `success`
- `failed`

Optional later states may include:

- `cancelled`
- `refunded`

Do not award credits on `pending`.
Do not award credits on `failed`.

---

# 7. Pricing page contract

The pricing surface must make all of these clear:

- offer name
- commercial meaning of the offer
- price
- credit amount or entitlement effect
- checkout action
- payment result state
- path back to the main workspace or billing area

If the page is a dedicated standalone surface, it is still part of the billing module conceptually.

---

# 8. Billing UI requirements

The billing surface should expose, at minimum:

- current credit balance
- available plans/packages
- recent transactions
- transaction status labels
- active subscription state
- module entitlement or add-on state
- credit wallet and usage information

The user should be able to answer these questions without ambiguity:

- What can I buy?
- What does it cost?
- How many credits do I have now?
- Did my payment succeed?
- Where is the record of that payment?

---

# 9. Security and integrity rules

These are non-negotiable.

1. publishable provider keys may render checkout UI, but they do not authorize credit changes
2. credits must never be increased from client-side success rendering alone
3. a verified application-side purchase or ledger update must exist before canonical balance changes
4. users may only read billing data allowed by the application's authorization and RLS model
5. transaction status and balance reads must come from canonical tables, not provider client state

---

# 10. Architecture boundary ownership

## `feature-system/`
Owns:

- whether billing features are visible or enabled
- whether pricing or credit-purchase capability is available at runtime

## `services/`
Own:

- creating billing intents or checkout setup
- verifying provider outcomes
- writing purchase records
- reserving, releasing, and charging operation credits
- updating canonical credit wallet state through ledger-backed flows
- shaping billing DTOs for UI

## `frontend/`
Owns:

- rendering the pricing surface
- rendering the current balance
- rendering purchase history, ledger history, and status
- routing users into and out of the billing flow

## `database/`
Owns:

- organization credit wallet and ledger tables
- billing customers and purchase tables
- subscription and billing preference tables
- operation cost monitoring tables
- constraints and RLS expectations for billing data

## RLS / secure backend logic
Own:

- final enforcement of who can read or mutate billing records

Do not move credit mutation logic into page components for convenience.

---

# 11. Anti-patterns

Do not:

- treat Stripe as the product architecture
- treat an embedded pricing table as business logic
- increment credits directly in page/component code after a UI callback
- read the current balance from the latest checkout response instead of canonical wallet/ledger tables
- duplicate pricing identifiers and offer meaning in multiple unrelated layers without control
- hide billing actions in the UI and pretend that is security
- leave plan/package meaning undocumented while implementation continues
- reintroduce `profiles.credits` as a balance source

---

# 12. Definition of done for pricing / plans changes

A pricing/plans change is done only when:

- the visible offer set is correct
- the payment flow still resolves through the correct service boundary
- transaction status logic is still correct
- canonical balance still resolves from the organization credit wallet and ledger
- canonical history still resolves from billing purchase records and credit ledger records
- documentation in `docs/billing/` is updated if the behavior, data model, or flow changed

A pricing page that looks correct but is not backed by canonical transaction and balance rules is not done.
