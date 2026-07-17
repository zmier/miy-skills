# UAT: collaborative-reading 社会研究方法锚点

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/skills/collaborative-reading/SKILL.md`
- Raw material: `RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/tasks/TASK01-PDF转分章Markdown/outputs/manuscript_raw.md`
- SubAgent: Euler
- UAT type: black-box leaning gray-box

## Prompt Leakage Check

Clean enough.

Prompt only provided:

- tested Skill path;
- raw paper markdown path;
- realistic user request: use interactive reading and start first-round orientation;
- isolation rules: do not read existing outline/logs/assets; do not modify files;
- output shell: dialogue response and discussion-outline draft.

Prompt did not provide:

- expected P1/P2 answer;
- prior bug;
- repair intent;
- social-research-methods mapping;
- required keywords or hidden evaluation criteria.

## Expected Behavior

Hidden evaluation criteria:

- A01 should be a proposition / hypothesis-level core claim, not a topic or proxy-level result.
- A01 should identify whether the claim is simple or compound, and assign stable proposition IDs if compound.
- A02 should stay at the theory layer: concepts / constructs / theoretical relation / literature basis.
- A02 should not treat `media coverage`, `PROPENSITY_BUY_MEDIA`, alpha, tables, or statistics as first-level theoretical objects.
- A03 should follow A02 and map each `Pi-X`, `Pi-Y`, and `Pi-R` into empirical proxy / measure / empirical relation.
- A03 should discuss proxy credibility and remaining threats, while deferring data construction and empirical design details to later agenda.

## Actual Behavior

PASS with minor residual risks.

Strengths:

- A01 was naturally written as a compound proposition:
  - `P1`: professional fund managers are affected by limited attention.
  - `P2`: stronger attention-driven tendency predicts worse future performance.
- It explicitly recognized that `media coverage` and `PROPENSITY_BUY_MEDIA` are proxy / operationalization, not the theoretical core claim.
- A02 outline table stayed mostly theoretical:
  - P1-X = limited attention / search cost.
  - P1-Y = fund trading behavior.
  - P1-R = limited attention shapes trades.
  - P1-KB = prior work shows attention affects individual investors; professional managers remain open.
  - P2-X = degree of attention-driven trading.
  - P2-Y = future fund performance.
  - P2-R = stronger attention-driven trading predicts worse performance.
  - P2-KB = prior fund literature and public-information reliance; media-attention propensity is new.
- A03 included proxy bridges and threats:
  - limited attention -> mass media coverage;
  - trading behavior -> inferred buys/sells from holdings changes;
  - attention-driven propensity -> `PROPENSITY_BUY_MEDIA`;
  - future performance -> alpha / performance measures.
- It correctly deferred flow-catering, RPI, tone/content, turnover, and alternative explanations to A07-like discussion.

Residual risks:

1. In the dialogue card's `P1` explanation, it wrote:
   `如果媒体把股票推入基金经理注意力集合，那么基金交易会更集中于被媒体覆盖的股票...`
   This is substantively reasonable, but it lets `media coverage` enter a proposition-branch explanation before the A03 proxy bridge. The later outline corrects this, but the first-round card still risks blending A02 and A03.

2. In the `Agenda Details > A03` proxy table, it listed `A03-P1-X`, `A03-P1-Y`, `A03-P2-X`, and `A03-P2-Y`, but omitted explicit `A03-P1-R` and `A03-P2-R` rows. Earlier in the Orientation Card it did include `A03-P1-R` and `A03-P2-R`, so this is a template-compliance gap rather than total misunderstanding.

3. The first-round dialogue included a concrete performance estimate. This is useful for orientation, but it is evidence-level material and should be handled carefully so it does not crowd out the claim/proxy/design sequence.

## Whether The UAT Was Clean

Clean.

The subAgent was not given the expected answer. Its output appears to come from reading the tested Skill and paper material, not from prompt leakage.

## Verdict

PASS, with small patch recommended.

The social research methods enhancement worked: the Skill now naturally pushes the reader from:

```text
A01 proposition / hypothesis
-> A02 concepts / constructs / theoretical relation / literature basis
-> A03 operationalization / proxy bridge
```

The remaining patch should make two guardrails more explicit:

- In the first-round card, proposition-branch explanations should keep theory relation and proxy bridge visibly separate.
- A03 detail tables must include `A03-Pi-R` whenever `Pi-R` exists, not only `Pi-X` and `Pi-Y`.

