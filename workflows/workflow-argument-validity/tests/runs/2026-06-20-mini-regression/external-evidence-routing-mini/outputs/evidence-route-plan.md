# Evidence Route Plan

mode: route-only smoke-regression
fixture: external-evidence-request-mini.md
execution_status: not-executed

This plan only verifies routing discipline for external evidence needs. No database search, broad web search, DOI lookup, official-source retrieval, PDF vision check, or manual verification was executed.

## Routing Basis

- `academic-argument-arrow-audit` requires evidence-type routing in `full-evidence-audit`: literature gaps and citation verification should use scholar-kit routes; policy/regulatory checks should use official sources; table/figure/numeric conflicts should return to PDF/DOCX source QC with model vision or manual inspection.
- `scholar-kit-literature-search` routes English/international literature through OpenAlex by default, uses WoS when FT50/UTD24 or WoS traceability is required, and uses CNKI for Chinese literature or Chinese scholarly evidence. When both English and Chinese evidence are relevant, OpenAlex/WoS and CNKI are complementary routes, not substitutes.

## Request Routes

| request_id | target_arrow | evidence need | route decision | route-only status |
|---|---:|---|---|---|
| MR01 | A006 | literature-gap-search | Route to `scholar-kit-literature-search`; use English scholarly route with OpenAlex and WoS consideration because FT50/UTD24 is listed; consider CNKI if Chinese literature is relevant to the contribution/gap claim. Do not replace this with generic web search. | not-executed |
| MR02 | A042 | citation-verification | Route to citation verification using scholar-kit plus DOI, journal page, publisher metadata, and cited-paper source where available. Distinguish metadata verification from fulltext verification. | not-executed |
| MR03 | A043 | policy-document-check | Route to official policy/regulatory sources, such as regulator, government, exchange, or legal/regulatory source documents. Secondary commentary is not sufficient for final evidence. | not-executed |
| MR04 | A030 | table-figure-numeric-conflict | Do not web-search. Route back to restored manuscript/PDF/DOCX source QC; use model vision or manual table/figure inspection to decide whether the conflict is extraction error or author-text error. | not-executed |

## Non-Execution Guardrails

- No route is marked complete.
- No missing result is treated as a true zero result.
- No request is converted into a final evidence finding.
- Any later full run must record independent status for each route, including technical failure, manual verification needed, insufficient result, or completed verification.
