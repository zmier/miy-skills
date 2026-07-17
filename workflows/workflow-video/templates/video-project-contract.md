# Video Project Contract Template

> 将本模板复制到真实项目中填写。不要在 workflow 目录保存项目密钥、原始大文件或任务回执。

## 1. Identity

```yaml
project_id:
title:
project_root:
owner:
mode: design-only | pilot-execution | batch-execution | review-only
status:
current_gate:
```

## 2. Goal and audience

```yaml
audience:
viewer_question:
learning_or_communication_goal:
success_signal:
included_scope:
excluded_scope:
```

## 3. Format

```yaml
episode_or_video_count:
target_duration:
aspect_ratio:
resolution:
frame_rate:
language:
subtitle_requirement:
audio_requirement:
delivery_formats:
```

## 4. Creative contract

```yaml
format_or_genre:
tone:
series_continuity:
character_policy:
visual_style:
text_on_screen_policy:
must_preserve:
must_avoid:
```

## 5. Source of truth

| Semantic owner | Path / URI | Version or state | Notes |
|---|---|---|---|
| content source |  |  |  |
| series / visual bible |  |  |  |
| episode registry |  |  |  |
| scripts |  |  |  |
| shot manifest |  |  |  |
| asset map |  |  |  |
| render jobs |  |  |  |
| review ledger |  |  |  |
| delivery manifest |  |  |  |

## 6. Execution authority

```yaml
allowed_external_tools:
forbidden_external_tools:
public_upload_allowed: false
paid_generation_allowed: false
budget_or_quota_boundary:
credential_handling:
```

## 7. Stage and Gate table

| Stage | Input | Required output | Reviewer | Gate / status |
|---|---|---|---|---|
| Development |  |  |  |  |
| Creative pre-production |  |  |  |  |
| Script & shot design |  |  |  |  |
| Assets |  |  |  |  |
| Pilot render |  |  |  |  |
| Batch render |  |  |  |  |
| Post |  |  |  |  |
| Delivery |  |  |  |  |

## 8. Pilot contract

```yaml
pilot_items:
coverage_reason:
baseline:
green_criteria:
red_criteria:
maximum_attempts_or_cost:
decision_owner:
```

## 9. Review contract

```yaml
technical_checks:
visual_checks:
content_checks:
continuity_checks:
delivery_checks:
independent_reviewer:
awaiting_human_is_allowed: true
```

## 10. Completion for this run

```yaml
completion_standard:
pending_outputs_allowed:
blocked_state_format:
next_gate:
```

## 11. Workflow feedback

```yaml
project_only_findings:
candidate_reusable_rules:
evidence_needed_before_promotion:
change_proposal_path:
```
