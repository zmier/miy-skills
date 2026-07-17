# UAT Evaluation: paper-extract / paper-co-read theory-proxy upgrade

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Source material: `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`
- SubAgent: Ohm
- UAT type: black-box
- Raw output file: `2026-07-07-UAT-paper-extract-co-read-after-theory-proxy-upgrade-raw-output.md`

## Prompt Leakage Check

Clean.

Prompt only provided:

- UAT constraint Skill path;
- top-level tested Skill path;
- revised manuscript markdown path;
- realistic user request: interactive reading, first-round automatic extraction, first-round co-reading guide;
- isolation rules: no existing outputs / logs; no file modification;
- output shell: dialogue output and file-side draft.

Prompt did not provide:

- expected P1 / P2 answer;
- theory/proxy separation rule;
- A03 proxy four-question rule;
- known previous failure points;
- the desired evaluation outcome.

## Expected Behavior

Hidden criteria after the upgrade:

- Route through `paper-extract -> paper-co-read`.
- Preserve `automatic-extraction.md` and `discussion-outline.md` as distinct outputs.
- Keep A01 / A02 at theory-layer wherever possible.
- Put empirical proxies into A03 / A04 rather than using them as theory propositions.
- In co-reading card, use theory-layer propositions plus separate empirical implementation / proxy lines.
- In A03, explain proxy credibility, not merely list variables.
- Preserve A04/A05 Pi-R or design block organization.
- Preserve source-check boundaries for rough / table-leak risky markdown.
- Save raw output separately from evaluation.

## Actual Behavior

Overall: PASS-LEANING / not final-perfect.

What improved strongly:

- The response explicitly separated theory layer from empirical implementation in the Orientation Card.
- P1 is now theory-level: `有限注意力影响基金经理的交易行为`.
- P2 is close to theory-level: `有限注意力驱动的交易倾向越强，未来业绩越差`.
- The response did not collapse the paper into one global X/Y pair.
- It preserved `TASK01-automatic-extraction.md` and `TASK01-discussion-outline.md` as separate file-side drafts.
- A03 now uses `代理资格 / warrant` and `支持证据 / 诊断 / 排除检验`, which is a clear improvement over the previous variable-list style.
- A04/A05 are organized by P-level blocks rather than a global controls list.
- It correctly flags the markdown as `reading draft / needs source-check` and avoids treating table details as stable facts.

Remaining issues:

1. P3 may be over-promoted to a core proposition.
   - SubAgent made `买入端应比卖出端更能体现有限注意力` a P3 core proposition.
   - This is defensible as a boundary / diagnostic proposition, but may be better represented as `S-P1-1` or `S-Pall-机制` unless the paper's core finding truly requires it as an independent proposition.
   - Existing Skill says mechanism / boundary default to supporting branches, but the model still upgraded this one.

2. P2 still contains mild empirical/construction flavor.
   - `有限注意力驱动的交易倾向` is much better than `PROPENSITY_BUY_MEDIA`, but it is still closer to the construct-as-estimated than a pure abstract relation.
   - Cleaner theory-layer wording would be: `基金经理受有限注意力影响越大，未来投资表现越差`.

3. A05 could explain design function more explicitly.
   - It names models and threats, but does not fully unpack why each control / FE / decile / lag enters the comparison logic.
   - This is acceptable for first-pass UAT, but not enough for a polished automatic extraction.

4. A03 credibility is improved but still compact.
   - It now has warrant and evidence columns.
   - However, some cells are too compressed to fully answer all four questions, especially for performance measures and manager-turnover diagnostics.

## Pass / Fail

Verdict: PARTIAL PASS, materially improved.

The upgrade succeeded on the main target:

```text
theory/proxy separation improved;
A03 proxy bridge became more argumentative;
UAT evidence now preserves raw output separately.
```

It did not fully solve proposition role classification:

```text
mechanism / boundary / diagnostic claims can still be over-promoted into P3.
```

## Where It Generalized

- SubAgent inferred the pipeline from the top-level Skill without being handed `paper-extract` / `paper-co-read` expected answers.
- It used the revised template columns naturally.
- It produced both dialogue card and file-side drafts.
- It handled source reliability boundaries appropriately.

## Regression Risk

Main residual risk:

```text
The model may treat a strong diagnostic / boundary pattern as an independent core proposition.
```

In this paper, buys-vs-sells is important. But if the Skill lets every important diagnostic become P3, future papers may accumulate too many core proposition branches and blur the difference between:

```text
core proposition;
mechanism;
diagnostic implication;
boundary condition;
robustness / exclusion support.
```

## Patch Needed

Recommended next small patch:

- Strengthen A01 proposition role classification:
  - mechanism / boundary / diagnostic implication defaults to `S-Pi-*`;
  - promote to `P3` only if the one-sentence core finding collapses without it;
  - if unsure, label as `candidate S/P` and ask for confirmation in co-reading.
- In paper-co-read Orientation Card:
  - allow a `Candidate Supporting / Diagnostic Branches` section separate from `Initial Proposition Branches`.
  - This prevents important but non-core patterns from becoming P3 too early.

No emergency patch is needed before continuing the paper discussion; the current output is good enough as a co-reading first pass, with P3 marked for review.
