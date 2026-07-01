---
type: reference
name: empirical-paper-component-coverage
status: seed
---

# Empirical Paper Component Coverage

Use this reference when reviewing empirical manuscripts whose author-facing structure is:

```text
theory/mechanism -> model/formula -> data/method -> results
```

The paper-writing-review workflow uses a different review-facing structure:

```text
contribution chain -> literature positioning -> identification -> measurement -> results narrative -> review assembly
```

This reference prevents gaps between the two structures.

## Coverage Matrix

| Author-Facing Component | What Authors Usually Do | Review Workflow Coverage | Main Audit Question | Gap Risk |
|---|---|---|---|---|
| Research question / contribution | Name the puzzle, contribution, and target audience. | Step 3 quick reconstruction; Step 4 literature genealogy; Step 8 review assembly. | Is the question important, and is the claimed contribution real? | Contribution rhetoric may survive even when gap is weak. |
| Theory / mechanism | Explain why X should affect Y; derive hypotheses or channels. | Step 3 initial reconstruction; Step 5 frontdoor/mechanism logic; Step 7 result narrative consistency. | Does the mechanism chain actually connect X, mediator, Y, and hypotheses without jumps? | Mechanism can be plausible prose but unsupported by design or results. |
| Mathematical / empirical model | Formalize the relationship with equations, fixed effects, controls, error terms, or structural assumptions. | Step 5 causal identification; Step 6 variable/data audit; Step 7 model-result alignment. | Does the formula match the claimed estimand and variables? Are controls/FE/timing coherent? | Equations may look technical but hide unclear estimand, bad controls, or unmatched variable definitions. |
| Data and variables | Define sample, data sources, core variables, merges, and measurement choices. | Step 6 variable-data-measurement audit. | Do variables and data measure the constructs? | Proxy variables, code crosswalks, sample attrition, and timing may be under-explained. |
| Research method / identification | Justify OLS, FE, IV, DiD, PSM, RDD, structural model, or other designs. | Step 5 causal identification; statistical table reference. | Does the method block the relevant DAG threats? | Authors may report many methods without addressing the real threat. |
| Baseline results | Present main coefficient or pattern. | Step 5 statistical evidence audit; Step 7 results narrative consistency. | Is the main result statistically and economically interpretable? | Significant coefficients may be tiny, unstable, or not interpretable because scale is unclear. |
| Mechanism results | Show channels, mediators, or auxiliary outcomes. | Step 5 frontdoor/mechanism; Step 7 mechanism narrative. | Are mechanisms proved, or only consistent with the story? | Authors may overstate correlation as mediation. |
| Heterogeneity / extensions | Split samples, add outcomes, or broaden scope. | Step 7 result narrative consistency. | Do extensions support the core contribution, or just stack significant results? | Result pile-up can blur the main claim. |
| Robustness | Alternative variables, samples, models, FE, clustering, placebo, pre-trends. | Step 5 statistical evidence; Step 6 measurement where variables change; Step 7 narrative. | Which threat does each robustness check address? | Robustness may change estimand or only test minor issues. |
| Conclusion / implications | Translate evidence into contribution and policy/theory claims. | Step 7 result narrative; Step 8 review assembly. | Does the conclusion stay within evidence strength? | Final claims often outrun identification and measurement. |

## Use Discipline

- Do not replace the workflow modules with the author-facing order.
- Use the matrix as a coverage check: every author-facing component should be consumed by at least one workflow module.
- If theory/mechanism or model/formula issues recur across projects, promote them from Step 7 reference checks into dedicated child Skills.
- For current seed stage, keep theory/mechanism and model/formula checks inside Step 7 unless the user explicitly asks for a standalone audit.

## Red Flags

- Hypotheses contain mediators not later tested.
- Equations include controls that are also mechanisms.
- The model uses same-year X, Y, and controls while causal language implies temporal order.
- Variable definitions in formulas differ from table labels or narrative prose.
- Baseline results support a narrow observed relation, while conclusion claims a broad theoretical mechanism.
- Heterogeneity is interpreted without testing differences across groups.
- Robustness checks change the outcome, treatment, sample, or estimand without saying so.

