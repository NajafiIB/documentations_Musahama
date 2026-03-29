# Database Implementation Rules

## Purpose

These are the practical implementation rules for touching the Musahama database from app code.

## Core Rules

1. Pages should not scatter direct Supabase queries
2. Use centralized Supabase clients
3. Treat `supabase/migrations` as the schema change log
4. Keep `supabase/schema.sql` and `src/types/database.types.ts` synced after remote apply
5. Prefer shared entities and runtime tables over ad hoc transitional payload reads

## Current Naming Rule

Keep these distinct:

- module keys: snake_case
- routes: kebab-case
- tables: existing canonical table names

Examples:

- module key: `origination_match`
- route: `/origination-match`
- runtime table: `module_cases`
- bridge table: `research_results`

## Current Change Rule

Any schema change should update:

- the migration
- the linked remote database
- `supabase/schema.sql`
- `src/types/database.types.ts`
- relevant docs and specs

See:

- `database/CONTRACT.md`
