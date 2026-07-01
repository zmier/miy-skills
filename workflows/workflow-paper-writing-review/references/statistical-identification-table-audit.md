---
type: reference
name: statistical-identification-table-audit
status: draft
---

# Statistical Identification Table Audit

Use this reference inside `manuscript-causal-identification-audit` when a manuscript contains regression, IV, DiD, PSM, robustness, mechanism, or heterogeneity tables.

This is not a stand-alone table-format checker. Its job is to connect statistical evidence back to the causal question:

```text
DAG threat -> author's strategy -> table evidence -> remaining concern
```

## Core Rule

Do not read stars mechanically. For each coefficient, F-statistic, R2, balance test, or robustness table, ask:

- Which causal threat is this table supposed to address?
- Does the reported statistic actually address that threat?
- Is the effect statistically significant, economically meaningful, and stable across meaningful specifications?
- Does the table change the estimand, sample, variable definition, or time window?
- Does the author's interpretation stay within what the table proves?

Write the answer in plain Chinese, keeping key terms such as `coefficient`, `standard error`, `first-stage`, `F-statistic`, `weak IV`, `R2`, `clustered standard errors`, and `economic significance`.

## Minimum Checks

### Main Regression Table

Check:

- coefficient sign and significance;
- effect size / economic significance, not only stars;
- whether controls and fixed effects change the coefficient materially;
- sample size changes across columns;
- whether standard errors are clustered at a plausible level;
- whether the outcome and treatment scale are clear enough to interpret the coefficient.

Plain-language prompt:

```text
这张表说明 X 和 Y 有关系。但这个关系有多大？加控制和固定效应后稳不稳？标准误聚类是否匹配识别层级？变量量纲是否足以解释系数？
```

### IV / 2SLS Table

Check:

- endogenous regressor, instrument, outcome, and identifying variation are stated before estimation;
- first-stage coefficient direction and significance;
- first-stage F-statistic or equivalent weak-IV diagnostic;
- second-stage coefficient direction, magnitude, and precision;
- OLS vs IV difference and interpretation;
- whether IV estimates a LATE for compliers rather than a full-sample ATE;
- exclusion restriction evidence, not just first-stage strength.

Plain-language prompt:

```text
第一阶段回答“工具变量能不能推动 X”；第二阶段回答“被这个工具推动的 X 是否影响 Y”。F 值强只说明工具不弱，不说明排除限制成立。
```

### Fixed Effects and Controls

Check:

- which factors each FE absorbs;
- whether important time-varying shocks remain;
- whether controls are pre-treatment or may be post-treatment / bad controls;
- whether additional FE specifications are main evidence or only robustness;
- whether high R2 is driven by FE rather than treatment variation.

### PSM / Matching / Weighting

Check:

- treatment definition;
- covariates are measured before treatment;
- balance before and after matching;
- overlap / common support;
- sensitivity to matching method or caliper;
- whether unobserved confounding remains.

### Robustness Tables

Classify each robustness check:

- measurement robustness: alternative X/Y definitions;
- sample robustness: excluding periods, sectors, regions, policies, or outliers;
- model robustness: extra FE, controls, clustering, functional form;
- identification robustness: placebo, pre-trends, event study, falsification, alternative instrument.

Then judge whether it addresses a real causal threat. Do not treat many robustness rows as cumulative proof if they all test the same minor issue.

### Mechanism and Heterogeneity Tables

Check:

- whether mechanism variables are mediators, outcomes, or proxies;
- whether `X -> M` and `M -> Y` are both shown;
- whether timing supports mechanism;
- whether heterogeneity splits were pre-motivated or exploratory;
- whether subgroup differences are tested directly, not inferred from one significant and one insignificant coefficient.

## Output Table

Use this section inside the causal audit:

```markdown
## Statistical Evidence and Identification Table Audit

| Evidence Table | What It Is Supposed to Prove | Key Statistical Evidence | Does It Support the Causal Claim? | Remaining Concern | Route |
|---|---|---|---|---|---|
|  |  | coefficient / SE / F-stat / R2 / N / balance / robustness | yes / partly / no / unclear |  | issue id or next workflow step |
```

## Escalation Rules

Write or update an issue ledger item when:

- an IV table omits first-stage strength or weak-IV diagnostics;
- the first stage is strong but exclusion restriction is only asserted;
- coefficients are statistically significant but economically tiny or uninterpretable;
- variable scales make coefficient interpretation impossible;
- robustness changes the sample, variable, or estimand without explanation;
- PSM lacks balance/overlap diagnostics;
- standard errors are not clustered at the treatment or shock level when needed;
- the paper infers subgroup differences without testing interaction/difference.

