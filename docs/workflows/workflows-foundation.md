# Workflows Foundation

## Current Workflow Model

Musahama now has two workflow layers:

- the shared platform runtime model
- retained legacy origination workflow surfaces

That means the product should not be documented as one single top-level workflow chain anymore.

## Shared Runtime Workflow

Across modules, the platform increasingly standardizes on:

1. create a module case
2. run execution steps
3. generate artifacts
4. request approval for side effects when needed
5. execute approved actions

This applies conceptually to current and future modules.

## Current Origination Bridge

The most mature operational workflow is still `Origination Match`.

Its bridge path remains:

1. optional CRM opportunity intake
2. mandate definition
3. research execution
4. strategy and evidence generation
5. result review
6. promotion into shared entities and artifacts

That workflow still matters, but it now sits **inside** a larger platform architecture.

## Rule

When documenting workflows:

- describe the shared runtime vocabulary first
- describe module-specific bridges second
- label legacy routes explicitly as compatibility surfaces
