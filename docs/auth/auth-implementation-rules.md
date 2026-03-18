# Auth Implementation Rules

1. Use centralized Supabase clients only
2. Resolve session server-side
3. Resolve current organization server-side
4. Pages do not own auth logic
5. Navigation does not infer role directly
6. Role and module access belong to feature-system/runtime
7. All auth bugs must be fixed through services/providers/hooks, not page hacks
