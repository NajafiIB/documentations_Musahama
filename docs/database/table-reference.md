# Table Reference

## Control and Commerce

- `organizations`
- `organization_members`
- `organization_invitations`
- `plans`
- `plan_modules`
- `organization_subscriptions`
- `modules`
- `organization_modules`
- `organization_entitlements`
- `organization_feature_entitlements`
- `organization_credit_ledger`
- `organization_billing_customers`
- `billing_credit_purchases`
- `organization_billing_preferences`
- `billing_commercial_requests`
- `credit_cost_model_rules`
- `credit_usage_event_costs`
- `credit_cost_daily_rollups`

## Shared Entities

- `companies`
- `industries`
- `company_industries`
- `company_lc_score_history`
- `contacts`
- `contact_emails`
- `contact_phones`
- `evidence`
- `psych_profiles`
- `lmc_fits`
- `dossiers`

## Origination Workflow Bridge

- `crm_opportunities`
- `mandates`
- `research`
- `strategies`
- `research_results`
- `research_result_contacts`
- `research_result_feedback`
- `research_run_logs`

Bridge columns:

- `research.module_case_id`
- `research_run_logs.module_run_id`

## Shared Runtime Plane

- `module_cases`
- `module_case_entities`
- `module_runs`
- `module_run_steps`
- `module_artifacts`
- `module_action_requests`
- `module_action_executions`
- `module_evidence_links`
- `workspace_recent_surfaces`
- `enrichment_runs`
- `enrichment_jobs`

## Supplier Development Program

- `sdp_cases`
- `sdp_program_profiles`
- `sdp_upload_batches`
- `sdp_raw_cost_lines`
- `sdp_batch_supplier_mappings`
- `sdp_approved_spend_facts`
- `sdp_supplier_profiles`
- `sdp_supplier_master`
- `sdp_spend_categories`
- `sdp_spend_subcategories`
- `sdp_score_options`
- `sdp_category_assessments`
- `sdp_supplier_assessments`
- `sdp_category_priority_results`
- `sdp_supplier_shortlist_results`
- `sdp_supplier_priority_results`
- `sdp_sector_lc_benchmarks`
- `sdp_category_major_cost_types`
- `sdp_supplier_resolution_memory`
- `sdp_cost_classification_memory`

## Musahama Strategy Management

- `msm_workspaces`
- `msm_source_reports`
- `msm_kpi_catalog`
- `msm_strategy_runs`
- `msm_strategy_scenarios`
- `msm_strategy_scenario_kpis`
- `msm_strategy_plans`
- `msm_plan_kpis`
- `msm_kpi_measurements`
- `msm_progress_events`
- `msm_alerts`
- `msm_plan_mandates`

## Automations and Support

- `automation_definitions`
- `automation_definition_conditions`
- `automation_definition_steps`
- `automation_trigger_events`
- `automation_runs`
- `automation_run_steps`
- `automation_in_app_notifications`
- `support_bug_reports`

## Platform Admin

- `god_audit.mutation_events`
- `platform_solution_policies`
- `platform_dataset_policies`
- `platform_provider_policies`
- `god_rollout_batches`
- `god_rollout_batch_items`
- `shared_integrations`
- `shared_integration_assignments`
- `shared_integration_secrets`

## Capabilities and Data Packs

- `capabilities`
- `module_capabilities`
- `datasets`
- `dataset_releases`
- `module_dataset_requirements`
- `organization_dataset_entitlements`
- `organization_module_datasets`
- `organization_module_integrations`
