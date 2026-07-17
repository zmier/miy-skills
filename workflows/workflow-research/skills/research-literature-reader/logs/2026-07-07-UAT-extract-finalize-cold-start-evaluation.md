# UAT Evaluation: extract -> finalize cold-start

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Source material: `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`
- SubAgent: Gauss
- UAT type: black-box
- Raw output file: `2026-07-07-UAT-extract-finalize-cold-start-raw-output.md`

## Prompt Leakage Check

Clean.

Prompt only provided:

- UAT constraint Skill path;
- top-level tested Skill path;
- source markdown path;
- realistic user request asking for final citable note before co-reading;
- isolation rules;
- generic output shell.

Prompt did not provide:

- `paper-finalize` name;
- expected routing answer;
- expected claim statuses;
- expected P1/P2 content;
- known quality concerns.

## Expected Behavior

Hidden criteria:

- Natural route should be `paper-extract -> paper-finalize`.
- If no co-read exists, mark `cold-start finalization`.
- Do not read existing outputs or logs.
- Produce final-note style output rather than a co-reading orientation card.
- Distinguish:
  - `verified-citable`;
  - `verified-understanding`;
  - `needs-source-check`;
  - inferred / not citable.
- Avoid upgrading table-derived exact coefficients, t-stats, R2, observations, formula details, or precise economic magnitudes to fully citable without PDF / restored table check.
- Include file-side draft for final literature note.

## Actual Behavior

Routing: PASS.

The subAgent naturally:

- identified the mode as `cold-start finalization`;
- skipped co-reading;
- produced a final literature note style output;
- separated citable statements, understanding-only statements, and needs-check statements;
- flagged exact table coefficients, t-stats, R2, observations, and formulas as requiring PDF / table verification;
- included design claim levels such as descriptive association, predictive relation, and exclusion-enhanced explanation;
- warned that causal claims should not be overstated.

Quality issues:

1. Precise annual performance range was over-upgraded.
   - It marked the `1.1%-2.8% per year` performance gap as `verified-citable` because the range appears in abstract/conclusion paragraphs.
   - This is defensible for quoting the authors' textual summary, but risky under the strict `paper-finalize` rule that precise economic magnitudes should be table/PDF checked before citation.
   - Better status should be:
     - `verified-understanding` or `verified-citable-text-summary`;
     - with `table-magnitude needs-source-check` for model-specific citation.

2. The output did not produce separate `verified-claims.md` and `source-check-log.md` drafts.
   - It produced a good final note draft.
   - It did not separately draft `verified-claims.md` or `source-check-log.md`, though the Skill says default outputs include all three.
   - This may be acceptable for a first UAT response, but not ideal for full compliance.

3. Source-check log is implicit, not explicit.
   - The note lists statuses and source anchors.
   - It does not include a dedicated claim-by-claim source-check log table.

4. It did not explicitly state that no `automatic-extraction.md` existed and it performed first-pass extract internally.
   - The user request asked for extract then finalize.
   - The output jumps into finalization without showing the intermediate automatic-extraction artifact.
   - This is acceptable for dialogue compactness, but the pipeline evidence would be stronger if it named the generated first-pass extraction as an internal prerequisite.

## Pass / Fail

Targeted route test: PASS.

Full `paper-finalize` artifact compliance: PARTIAL PASS.

The new routing works under black-box conditions:

```text
final citable note before co-reading -> cold-start finalization
```

The main remaining issue is stricter source-check status taxonomy for textual economic magnitudes and requiring separate source-check artifacts.

## Where It Generalized

- It inferred cold-start finalization without being told the route name.
- It used finalization vocabulary naturally.
- It avoided claiming a clean causal design.
- It correctly downgraded table coefficients and formulas to `needs-source-check`.

## Regression Risk

Moderate:

- The model may mark values stated in abstract/conclusion as `verified-citable` even when they summarize table-derived results.
- This could lead to prematurely citable quantitative claims.

Low:

- Routing failure risk appears low.
- Co-read vs finalize distinction worked.

## Patch Recommendation

Recommended patch:

1. Add a status distinction:

```text
verified-citable-text-summary:
  The authors state the claim in prose, but underlying table values still need PDF/table check for precise empirical citation.
```

2. Strengthen numerical magnitude rule:

```text
Any exact percentage, annualized gap, coefficient, t-stat, R2, observation count, or formula detail derived from empirical results must not be plain verified-citable unless the original table/PDF has been checked.
If the number appears in abstract/conclusion prose, mark it verified-citable-text-summary + table-value-needs-check.
```

3. Strengthen output completeness:

```text
If finalization is requested, output or draft all three:
final-literature-note.md；
verified-claims.md；
source-check-log.md。
If only one is shown due to length, explicitly say the other two are pending.
```

No need to rework the routing architecture; the path itself is working.
