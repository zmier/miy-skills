# Field Evidence Learning Templates

## field-learning-request-ledger.md

| learning_request_id | request_type | target_arrow_ids | source_request_ids | learning_question | shared_topic_or_method | priority | must_answer_before | can_merge_with | notes |
|---|---|---|---|---|---|---|---|---|---|
| LR001 | judge-arrow / repair-arrow / field-map |  |  |  |  | high / medium / low | arrow-audit / repair-mapping |  |  |

## field-learning-plan.md

| plan_id | learning_mode | request_ids | reading_depth | abstract_target_count | fulltext_target_count | must_build_domain_map | must_build_repair_menu | must_update_arrow_audit | stop_rule | qc_risks |
|---|---|---|---|---|---|---|---|---|---|---|
| FP001 | quick / standard / deep / 100-paper |  |  |  |  | yes/no | yes/no | yes/no |  |  |

## field-search-strategy.md

| strategy_id | request_ids | literature_search_skill | databases_or_routes | query_blocks | journal_quality_policy | journal_quality_sources | inclusion_criteria | exclusion_criteria | abstract_scan_goal | fulltext_trigger | non_literature_routes | execution_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FS001 |  | scholar-kit-literature-search | OpenAlex / WoS / CNKI |  | field-top / general-top / authoritative-review | WoS/JCR / SJR / seed reviews |  |  |  |  |  | planned-not-executed |

## seed-literature-ledger.md

| source_id | title | year | journal_or_venue | doi_or_url | linked_request_ids | include_or_exclude | include_reason | journal_quality_evidence | verification_level | needs_fulltext | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SL001 |  |  |  |  |  | include / exclude / background-only |  | field-top / Q1-proxy / review / unknown | metadata / abstract / fulltext / manual-needed | yes/no |  |

## fulltext-acquisition-plan.md

| source_id | title_or_doi | why_fulltext_required | route_priority | legal_access_route | requested_materials | fallback_if_unavailable | next_skill_to_call | status |
|---|---|---|---|---|---|---|---|---|
| S001 |  |  | OA / publisher / arXiv / PMC / Unpaywall / OpenAlex OA |  | PDF / HTML / supplement / figures | requires-human-access / no-legal-fulltext-found | paper-fulltext-acquisition | planned |

## fulltext-acquisition-ledger.md

| source_id | title | doi_or_identifier | requested_materials | acquisition_route | access_status | local_path | license_or_access_note | needs_restoration | restoration_skill | human_download_request | notification_status | qc_flags | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S001 |  |  | PDF / HTML / supplement / figures |  | acquired / no-legal-fulltext-found / requires-human-access / login-required / captcha-or-verification-required / technical-failure |  |  | yes/no | scholar-pdf-markdown-restoration / scholar-docx-markdown-restoration / html-restoration | human-download-request.md | not-needed / planned / sent / failed / not-run-dry-run / manual-notification-needed |  |  |

## fulltext-source-inventory.md

| source_id | material_type | local_path | source_url | provenance | used_for | qc_status |
|---|---|---|---|---|---|---|
| S001 | PDF / HTML / supplement / figure |  |  | user-provided / publisher-oa / OpenAlex-OA / Unpaywall / arXiv / PMC | domain-map / judge-arrow / repair-arrow |  |

## handoff-to-fulltext-restoration.md

| source_id | local_path | material_type | target_output | suggested_restoration_skill | priority_reason |
|---|---|---|---|---|---|
| S001 |  | PDF / HTML / supplement | restored markdown / figure notes / supplement ledger | scholar-pdf-markdown-restoration |  |

## human-download-request.md

| request_id | source_id | title | doi_or_url | requested_materials | why_needed | suggested_save_path | deadline_or_priority | notification_status | notification_channel |
|---|---|---|---|---|---|---|---|---|---|
| HDR001 | S001 |  |  | PDF / HTML / supplement | needed for fulltext pattern extraction | sources/fulltext/pdf/ | high / medium / low | planned / sent / failed / not-run-dry-run / manual-notification-needed | feishu-notify |

## external-reading-log.md

| reading_id | source_id | read_level | sections_read | used_for | notes | qc_status |
|---|---|---|---|---|---|---|
| RL001 |  | metadata / abstract / fulltext / figure / supplement |  | domain-map / judge-arrow / repair-arrow |  |  |

## domain-map.md

| field | core_topics | main_methods | main_metrics | common_claims | common_risks | verification_level |
|---|---|---|---|---|---|
|  |  |  |  |  |  | metadata / abstract / fulltext / manual-needed |

## external-evidence-ledger.md

| evidence_id | request_id | target_arrow_id | evidence_type | source | source_quality | finding | effect_on_arrow_status | verification_level | qc_status |
|---|---|---|---|---|---|---|---|---|---|
| EE001 |  |  | judge-arrow |  |  |  |  | metadata / abstract / fulltext / manual-needed |  |

## review-risk-radar.md

| risk_id | related_arrow_ids | field_risk | why_it_matters | suggested_audit_focus | source_basis | verification_level |
|---|---|---|---|---|---|---|
| R001 |  |  |  |  |  | metadata / abstract / fulltext / manual-needed |

## handoff-to-arrow-audit.md

| target_arrow_id | prior_status | external_evidence_summary | recommended_status | remaining_qc |
|---|---|---|---|---|
|  |  |  |  |  |

## handoff-to-repair-mapping.md

| target_arrow_id | break_type | repair_knowledge_status | case_repair_menu_ref | remaining_gap |
|---|---|---|---|---|
|  |  |  |  |  |

## repair-feedback-candidates.md

| candidate_id | source_case_or_sources | candidate_rule | target_reference_or_menu | evidence_basis | scope_conditions | known_exceptions | required_regression_tests | promotion_status |
|---|---|---|---|---|---|---|---|---|
| F001 |  |  |  |  |  |  |  | candidate / hold / reject |

## field-learning-qc.md

| qc_id | related_request_ids | issue_type | status | what_can_be_concluded | what_cannot_be_concluded | next_action |
|---|---|---|---|---|---|---|
| Q001 |  | access / search / quality / fulltext / source | pending / done / technical-failure / requires-human-access |  |  |  |
