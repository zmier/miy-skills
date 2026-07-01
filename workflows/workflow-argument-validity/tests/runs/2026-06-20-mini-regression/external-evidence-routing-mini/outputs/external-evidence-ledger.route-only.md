# External Evidence Ledger

mode: route-only smoke-regression
search_status: not-executed

This ledger records routing decisions only. It is not a final external-evidence ledger and must not be used as evidence that searches or source checks were completed.

| request_id | target_arrow | requested evidence | required route | search_status | what_can_be_concluded | what_cannot_be_concluded |
|---|---:|---|---|---|---|---|
| MR01 | A006 | Whether the claimed peer disclosure literature gap is real | `scholar-kit-literature-search`; English route should include OpenAlex and WoS consideration because FT50/UTD24 is in scope; CNKI should be considered if Chinese scholarship is relevant | route-only / not-executed | The correct route is scholarly database routing through scholar-kit, not generic web search. | Whether the literature gap is real; whether OpenAlex, WoS, or CNKI contains supporting/contradicting literature; whether results are true zero or insufficient. |
| MR02 | A042 | Whether a specific citation/nearby literature supports contribution positioning | scholar-kit plus DOI, journal page, publisher metadata, and cited-paper source | route-only / not-executed | The correct route is citation verification with metadata/fulltext distinction, not a broad web search. | Whether the Seo 2021 citation exists; whether metadata or fulltext supports the claim; whether manual verification is needed. |
| MR03 | A043 | Whether the policy recommendation has official regulatory support | official policy/regulatory source route: regulator, government, exchange, legal/regulatory primary documents | route-only / not-executed | The correct route is official-source verification; secondary summaries cannot be final evidence. | Whether CSRC or other official documents support the policy claim; whether legal interpretation is valid. |
| MR04 | A030 | Whether Table 11 value/text conflict comes from extraction or author error | restored manuscript/PDF/DOCX source QC with model vision or manual inspection | route-only / not-executed | The correct route is source QC, not external web search. | Whether Table 11 was extracted incorrectly; whether the manuscript text is wrong; whether the underlying result is significant. |

## Missing Required Route Notes

Because this is a route-only smoke regression, every required route is intentionally unexecuted.

| request_id | missing_required_route | why_route_not_completed | follow-up needed for full audit |
|---|---|---|---|
| MR01 | OpenAlex/WoS/CNKI scholarly search through scholar-kit | Contract forbids full database searches for this test | Run selected scholar-kit child routes and record separate statuses/results. |
| MR02 | DOI/journal/publisher/cited-paper verification | Contract limits work to route identification | Verify metadata first, then fulltext/source support where accessible. |
| MR03 | Official regulator/government/source-document retrieval | Contract limits work to route identification | Retrieve official policy/regulatory documents and keep legal interpretation conservative. |
| MR04 | PDF/DOCX source QC with model vision/manual inspection | Contract limits work to route identification | Inspect restored manuscript and original table/figure source; do not use web evidence for extraction conflicts. |
