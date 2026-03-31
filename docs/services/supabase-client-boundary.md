# Supabase Client Boundary

Owner: Platform Architect
Last Updated: 2026-03-31
Version: 1.1
Status: Approved

## 1. Purpose

Define the mandatory Supabase client boundary for the frontend and backend architecture.

## 2. Centralized Client Rule

Use centralized Supabase clients only.

Required structure:

```text
services/
  supabase/
    client.ts
    server.ts
    middleware.ts
```

No ad hoc client initialization is allowed across pages, components, random hooks, or utility files.

## 3. Client Types

### `client.ts`

Browser-safe Supabase client for authenticated UI interactions.

### `server.ts`

Server-only client for secure reads, secure writes, and data shaping.

### `middleware.ts`

Session refresh and auth-path boundary handling for routing.

user-triggered browser-safe reads

light client interactions already approved by architecture

server.ts

Server-side Supabase client.

Use for:

SSR data loading

protected reads

secure mutation helpers

sensitive joins

organization bootstrap

runtime state assembly

middleware.ts

Middleware/session helper integration.

Use for:

coarse auth route protection

session refresh support

protected/public route separation

4. Hard Rules

Never initialize Supabase directly inside page files

Never initialize Supabase inside random UI components

Never use browser clients for secret or sensitive reads

Never expose server-only config through client services

Never bypass middleware/session helper conventions

5. Server-Only Rule

These must stay server-side:

integration secret handling

provider auth configuration

secret_ref reads

billing summary assembly with sensitive joins

provider-backed resolution needing private config

any service that may expose restricted organization internals

6. Response Rule

Client-readable service responses must be sanitized.

Do not return:

raw secrets

full provider credentials

internal billing-provider references unless explicitly safe

secret-like global configuration values

7. Final Rule

If a service needs secrets, privileged joins, or SSR bootstrap context, it belongs on the server client path.
