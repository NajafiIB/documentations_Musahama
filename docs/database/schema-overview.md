# Schema Overview

## Current Schema Shape

The current schema is no longer best described as one linear workflow schema.

It now contains:

- tenant and billing tables
- module catalog tables
- shared business entities
- retained origination workflow tables
- shared runtime tables
- data-pack catalog tables

## Important Boundary

`Origination Match` still bridges through the older workflow schema, but new cross-module architecture should prefer:

- shared runtime tables for execution state
- shared entity tables for durable business records
- dataset tables for paid data products
