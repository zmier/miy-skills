# UAT: paper-extract / paper-co-read 黑箱完整验收

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Raw material: `RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/tasks/TASK01-PDF转分章Markdown/outputs/manuscript_raw.md`
- SubAgent: Kuhn
- UAT type: black-box

## Prompt Leakage Check

Clean.

Prompt only provided:

- top-level tested Skill path;
- raw paper markdown path;
- realistic user request: use interactive reading and start first-round orientation;
- isolation rules: do not read existing discussion-outline / automatic-extraction / design-extraction / route-map / logs;
- no file modification;
- output shell: dialogue response and file-side draft content.

Prompt did not provide:

- `paper-extract` / `paper-co-read` names;
- A01-A08 expected structure;
- P1/P2 answer;
- A04/A05 block-design expectation;
- previous bug or repair intent.

## Expected Behavior

Hidden evaluation criteria:

- From top-level `research-literature-reader`, the agent should route to `paper-reading`, then naturally follow `paper-extract -> paper-co-read`.
- It should state or imply that `automatic-extraction.md` is the upstream structured draft and `discussion-outline.md` is the co-reading workspace.
- A01 should keep core propositions narrow and not promote mechanism / exclusion / robustness support into core P branches.
- A02 should stay theoretical, not use empirical proxy as Pi-X / Pi-R.
- A03 should hold proxy bridge.
- A04 should be organized as `A04-Pi-R Measurement / Data Block`, with core measures inherited from A03 and block-specific design-support measures.
- A05 should be organized as `A05-Pi-R Design / Identification Block`, explaining why variables enter the model.
- Output should avoid using table coefficients as source-checked facts without QC.

## Actual Behavior

PARTIAL PASS / FAIL for structure quality.

What worked:

- The agent naturally produced a two-layer file-side plan:
  - `TASK01-automatic-extraction.md`;
  - `TASK01-discussion-outline.md`.
- It correctly treated them as work drafts, not final design extraction or route map.
- It warned that raw markdown / table details need source check.
- It identified many important paper elements: media coverage, buys/sells, propensity measures, performance measures, flow-catering, RPI, signed media coverage, manager turnover.

What failed:

1. Core proposition over-splitting:
   - It created `P4 机制/排除命题`.
   - This violates the rule that mechanism / exclusion / robustness should usually be support branches `S-Pi-*` or `P-all`, not core propositions.

2. Proxy entered A01/A02 too early:
   - It wrote `P1: media coverage -> more fund buying`.
   - It wrote `P1-X: attention-grabbing media coverage`.
   - This keeps the empirical proxy in the theoretical layer, instead of first stating the theory-level object/relation and moving media coverage into A03.

3. A04 did not follow the new block design:
   - It listed global data sources (`Media`, `Funds`, `Stocks`) instead of `A04-Pi-R Measurement / Data Block`.
   - It did not separate core measures from block-specific design-support measures.

4. A05 did not follow the new block design:
   - It listed broad designs and alternative tests, but not `A05-P1-R`, `A05-P2-R` blocks linked to A04 blocks.
   - It did not explicitly distinguish variable measurement from variable design function.

5. The output did not clearly show use of the Chinese `automatic-extraction-template.md`.

## Whether The UAT Was Clean

Clean.

The failure is meaningful: the prompt did not leak expected structure. The result shows that top-level routing worked, but the newly split child skills are not yet forceful enough under black-box use.

## Verdict

FAIL for full black-box acceptance.

The architecture is recognized, but quality controls need strengthening:

```text
paper-extract -> paper-co-read routing: PASS
A01/A02/A04/A05 structure: FAIL / needs patch
```

## Patch Needed

1. In `paper-reading/SKILL.md`, require the agent to read `paper-extract/SKILL.md`, `paper-extract/templates/automatic-extraction-template.md`, `paper-co-read/SKILL.md`, and `paper-co-read/templates/discussion-outline-template.md` before producing first-round co-reading output.
2. In `paper-extract/SKILL.md`, strengthen A01:
   - core propositions only;
   - mechanism / exclusion / robustness become `S-Pi-*` or `P-all`, not P4 by default.
3. In `paper-extract/SKILL.md`, strengthen A02:
   - Pi-X / Pi-Y / Pi-R must stay theoretical;
   - empirical proxies such as media coverage go to A03.
4. In `paper-extract/SKILL.md`, strengthen A04/A05:
   - output must use Pi-R block tables, not freeform global data/design lists.
5. In `paper-co-read/SKILL.md`, require file-side draft to preserve `automatic-extraction-template.md` structure when describing automatic extraction content.

