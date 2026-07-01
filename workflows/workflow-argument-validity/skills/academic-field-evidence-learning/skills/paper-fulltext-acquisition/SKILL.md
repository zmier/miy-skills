---
name: paper-fulltext-acquisition
description: 学术论文合法全文获取子 Skill。用于 academic-field-evidence-learning 第 4.3 步，在 scholar-kit 检索得到候选文献后，根据 fulltext-acquisition-plan 获取合法开放 PDF、HTML、图表或补充材料；优先 OpenAlex OA、Unpaywall、publisher OA、arXiv、PMC、bioRxiv/medRxiv 和机构/用户已提供文件；不绕过付费墙。
---

# Paper Fulltext Acquisition

## 定位

本 Skill 负责把候选文献从“摘要可见”推进到“可供深读的全文材料”。它不做文献检索，不抽取 repair pattern，不绕过付费墙。

```text
candidate papers
-> legal fulltext acquisition
-> fulltext-acquisition-ledger.md
-> handoff to PDF/HTML restoration
```

当合法 OA 路线失败、需要机构权限、需要用户手动下载 PDF，或需要用户提供补充材料时，本 Skill 必须进入人机交互断点，并调用：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/feishu-notify/SKILL.md
```

通知用户下载或上传 PDF / HTML / Supplement。通知失败不能让主流程失败，但必须写入 `field-learning-qc.md`。

## 输入

- `fulltext-acquisition-plan.md`；
- `field-search-strategy.md`；
- `seed-literature-ledger.md` 或 scholar-kit 检索结果；
- DOI、title、URL、OpenAlex work id、publisher page、arXiv id、PMID/PMCID；
- 项目中用户已提供的 PDF/HTML/Supplement 文件。

## 输出

```text
fulltext-acquisition-ledger.md
fulltext-source-inventory.md
handoff-to-fulltext-restoration.md
human-download-request.md
field-learning-qc.md
```

建议保存位置：

```text
sources/fulltext/pdf/
sources/fulltext/html/
sources/fulltext/supplement/
sources/fulltext/figures/
```

## 合法来源优先级

1. 用户已提供的 PDF、HTML、Word、Supplement；
2. Publisher open access page；
3. OpenAlex OA location / PDF URL；
4. Unpaywall OA location；
5. arXiv / SSRN / working paper repository（按学科适用性判断）；
6. PubMed Central / Europe PMC；
7. bioRxiv / medRxiv；
8. 作者机构主页、项目页、数据/代码仓库中明确开放的版本。

若上述路线都不可用，标记：

```text
no-legal-fulltext-found
requires-human-access
```

不得使用 Sci-Hub、盗版库、绕 paywall、伪造下载链接或复用未授权 cookies。

## 人工下载通知

触发条件：

```text
access_status: requires-human-access
access_status: no-legal-fulltext-found
access_status: login-required
access_status: captcha-or-verification-required
requested_materials 包含 supplement / figure，但自动获取失败
```

触发后输出：

```text
human-download-request.md
```

字段：

```text
request_id
source_id
title
doi_or_url
requested_materials
why_needed
suggested_save_path
deadline_or_priority
notification_status
notification_channel
```

`notification_status` 统一取值：

```text
not-needed
planned
sent
failed
not-run-dry-run
manual-notification-needed
```

飞书通知默认调用：

```bash
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/feishu-notify/scripts/send-notify.sh \
  "需要人工下载论文全文" \
  "请下载 source_id=... 的 PDF/HTML/Supplement，并放到 suggested_save_path。详情见 human-download-request.md" \
  --feishu
```

如果需要按钮确认，可使用 `feishu-notify` 的 `scripts/send-card.py`，但默认不阻塞等待按钮；本 Skill 只记录 `notification_status`。

## Ledger 字段

`fulltext-acquisition-ledger.md`：

```text
source_id
title
doi_or_identifier
requested_materials
acquisition_route
access_status
local_path
license_or_access_note
needs_restoration
restoration_skill
human_download_request
notification_status
qc_flags
notes
```

`handoff-to-fulltext-restoration.md`：

```text
source_id
local_path
material_type
target_output
suggested_restoration_skill
priority_reason
```

## 还原路由

- PDF：优先交给 `scholar-pdf-markdown-restoration`；
- DOCX：交给 `scholar-docx-markdown-restoration`；
- HTML：保存页面或正文后，交给当前项目约定的 HTML/Markdown 还原流程；
- 图表或补充材料：保留原文件路径，并在后续 `repair-knowledge-synthesis` 中标记是否需要视觉 QC。

## 完成标准

- 每个全文获取动作绑定 `source_id`；
- 每个来源都有 `access_status`；
- 成功获取的文件有本地路径；
- 未获取的文件说明失败原因和下一步；
- 需要用户下载时已生成 `human-download-request.md`，并尝试用 `feishu-notify` 通知；
- dry-run / UAT 中若不实际发送通知，必须写 `notification_status: not-run-dry-run`；
- 不把“没有合法全文”写成“该文献不存在”；
- 输出可直接交给 PDF/HTML restoration 和 `repair-knowledge-synthesis`。
