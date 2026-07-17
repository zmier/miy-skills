# UAT Evaluation: paper-extract / paper-co-read template-compliance upgrade

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Source material: `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`
- SubAgent: Plato
- UAT type: black-box
- Raw output file: `2026-07-07-UAT-paper-extract-co-read-after-template-compliance-upgrade-raw-output.md`

## Prompt Leakage Check

Clean.

Prompt only provided:

- UAT constraint Skill path;
- top-level tested Skill path;
- manuscript markdown path;
- realistic user request;
- isolation rules;
- generic output shell.

Prompt did not provide:

- expected P1/P2 answer;
- expected two-version core finding;
- template-table compliance requirements;
- prior UAT failures;
- hidden evaluation criteria.

## Expected Behavior

Hidden criteria after this upgrade:

- Produce both core-finding versions:
  - theory-pure version;
  - reader-guide version.
- Preserve theory/proxy separation.
- Keep diagnostic / exclusion branches as `S-Pi-*`.
- If showing `automatic-extraction.md` draft, preserve A01-A08 and key tables:
  - A01 core proposition admission table;
  - A01 proposition registry;
  - A02 theory relation table;
  - A03 proxy bridge table;
  - A04 measurement block table;
  - A05 design block table;
  - A06 result table;
  - A07 validity threat table;
  - open questions table.
- Preserve `discussion-outline.md` as a distinct co-reading workspace.
- Save raw output separately from evaluation.

## Actual Behavior

Verdict: PASS on the targeted template-compliance and two-version core-finding upgrade.

What worked:

- The dialogue card includes:
  - `一句话核心发现：理论纯净版`;
  - `一句话核心发现：读者导览版`.
- P1/P2 remain theory-level.
- `买入端强于卖出端` remains `S-P1-diagnostic`, not P3.
- `flow-catering`, `RPI`, and news tone are supporting / exclusion branches.
- The `automatic-extraction.md` draft now preserves A01-A08.
- The draft includes the key tables:
  - core proposition admission test;
  - proposition registry;
  - A02 table;
  - A03 proxy bridge table;
  - A04 measurement table;
  - A05 design table;
  - A06 result table;
  - A07 threat table;
  - open questions table.
- The `discussion-outline.md` draft stays distinct from automatic extraction and includes co-reading workspace elements.
- Source-check boundaries are explicit.

Remaining issues:

1. Reader-guide version includes precise performance range.
   - It says annual gap is about `1.1% 到 2.8%`.
   - The response also flags table details as `needs-source-check`, so this is not a serious regression.
   - For stricter behavior, reader-guide sentences could avoid precise numbers until table QC.

2. The file draft is long but still first-pass.
   - Some source anchors are broad paragraph ranges.
   - Some entries are inferred from text and need PDF / table verification.

3. Design strength is marked but not yet standardized.
   - It correctly says predictive / mechanism-consistent rather than full causal.
   - Future improvement could formalize design claim levels.

## Pass / Fail

Targeted upgrade: PASS.

Full scholarly extraction quality: PASS-LEANING first pass, with source-check caveats.

This round fixed the prior bottleneck:

```text
file-side draft no longer collapses into compressed prose;
key tables are preserved under black-box conditions.
```

## Where It Generalized

- The subAgent inferred both core-finding versions from the top-level Skill.
- It preserved table structure without being told the expected table names in the prompt.
- It continued to preserve branch-role classification from the previous upgrade.
- It kept co-reading output separate from automatic extraction output.

## Regression Risk

Low for:

- theory/proxy separation;
- branch-role classification;
- template table preservation.

Moderate for:

- precise empirical numbers appearing in reader-guide text before table QC.

## Patch Recommendation

Optional next patch:

- Add a sentence to reader-guide version rules:
  - if table QC is missing, avoid precise coefficient / annualized gap / t-stat / R2 values in the guide sentence;
  - use qualitative direction unless the value is explicitly verified.
- Add standardized `design claim level` in A05:
  - descriptive association;
  - predictive relation;
  - mechanism-consistent evidence;
  - exclusion-enhanced explanation;
  - quasi-causal / causal claim.

No urgent patch is needed before continuing paper discussion. The current Skill behavior is good enough for a first-pass automatic extraction plus co-reading guide.
