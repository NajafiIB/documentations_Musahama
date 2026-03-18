# Provider Model

Owner: Platform Architect
Last Updated: 2026-03-18
Version: 1.0
Status: Approved

---

## 1. Purpose

Define how providers fit into the feature system.

Providers are dependencies.
They are not modules.
They are not feature names.
They are not product sections.

---

## 2. Provider Role in the System

Providers enable certain capabilities, for example:
- person enrichment
- AI generation
- CRM sync
- external company search
- content extraction

A provider is only one possible implementation for a capability.

---

## 3. Examples

### provider examples
- OpenAI
- Lusha
- CRM connector
- search provider

### capability examples
- contacts.enrich_person
- research.generate_strategies
- crm.sync.import
- companies.search_external_source

The capability is the product-facing concept.
The provider is the runtime dependency beneath it.

---

## 4. Provider Requirement Rule

Provider requirements belong in:
- feature_provider_requirements
- organization_integrations
- provider capability resolution
- runtime provider-state logic

They do not belong in:
- feature keys
- module names
- page names
- button names

---

## 5. Example Mapping

Feature:
- contacts.enrich_person

Possible providers:
- Lusha with capability person_enrichment
- another enrichment provider with capability person_enrichment

The feature remains the same even if the provider changes.

---

## 6. Provider State Questions

The runtime layer must be able to answer:

- is a provider connected?
- is it active?
- does it support the required capability?
- is it the default provider for this capability?
- does it have required credentials/config?
- is the provider currently healthy?
- what reason should be shown if unavailable?

---

## 7. Suggested Provider State Contract

```ts
type ProviderStateReason =
  | "ok"
  | "missing_integration"
  | "integration_disconnected"
  | "missing_capability"
  | "missing_api_key"
  | "provider_unavailable"
  | "system_disabled"

type ProviderState = {
  providerKey: string
  capabilityKey: string
  connected: boolean
  enabled: boolean
  reason: ProviderStateReason
}


8. UI Rule

The UI should show actions like:

Enrich Contact

Generate Strategy

Sync CRM

Export Dossier

The UI should not lead with:

Lusha Action

OpenAI Strategy Button

CRM Vendor Export Button

9. Security Rule

Sensitive provider configuration is server-side only.
The client should receive only sanitized provider state needed for UI/runtime decisions.
