# External Evidence Request Mini

mode: full-evidence-audit
test_scope: route-only smoke test

| request_id | target_arrow | current_status | why_external_evidence_needed | search_type | source_priority | query_seed | expected_route |
|---|---|---|---|---|---|---|---|
| MR01 | A006 | needs-external-evidence | 判断作者声称的 peer disclosure literature gap 是否真实 | literature-gap-search | FT50/UTD24; OpenAlex/WoS; CNKI if Chinese literature relevant | peer effects corporate disclosure decisions voluntary disclosure misconduct | scholar-kit-literature-search; OpenAlex/WoS; consider CNKI |
| MR02 | A042 | needs-external-evidence | 核验一条具体引用/相邻文献是否支持作者贡献定位 | citation-verification | DOI/journal/publisher metadata; scholar-kit | Seo 2021 peer effects corporate disclosure decisions | scholar-kit / DOI / journal metadata |
| MR03 | A043 | needs-external-evidence | 判断政策建议是否有官方监管依据 | policy-document-check | official regulator/government/source documents | CSRC disclosure regulation active disclosure penalty discretion | official policy/regulatory source route |
| MR04 | A030 | needs-qc | 表11数值/正文冲突是否来自原稿表格抽取或作者正文错误 | table-figure-numeric-conflict | restored manuscript source QC | Table 11 PosCAR NegCAR significance conflict | do not web-search; return to PDF/DOCX source QC with model vision |

