# Documentation Discipline

## Core Rule

The docs must describe the **current implemented platform first**.

Do not leave the repo in a state where:

- the code says one thing
- the docs say another
- developers are expected to infer which one is real

## What Must Be Updated Together

Update docs and specs whenever you change:

- the module catalog
- navigation groups or route roots
- runtime-plane tables or meanings
- dataset/data-pack catalog behavior
- source-of-truth rules
- service boundaries
- Supabase contract workflow
- approval-gated action behavior

## Required Sync Pattern

For architecture changes:

1. update implementation
2. update prose docs in `docs/`
3. update structured specs in `specs/`
4. update implementation-repo pointers if needed

For database changes:

1. write the migration
2. apply it to the linked remote
3. dump `supabase/schema.sql`
4. regenerate `src/types/database.types.ts`
5. run validation

## Current Platform First Rule

When the product is in transition:

- document the live bridge state clearly
- label legacy paths as compatibility surfaces
- do not present old architecture as if it is still the primary design

That rule is especially important for:

- `crm_opportunities`
- `mandates`
- `research`
- `results`

Those remain important, but they are now part of the `Origination Match` bridge story, not the official top-level product map.

## Reviewer Checklist

Reviewers should ask:

1. does the docs update match the implementation that merged?
2. do the specs still match the prose docs?
3. is the current module model obvious to a new engineer?
4. did the author explain any legacy bridge behavior explicitly?
