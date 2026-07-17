# UAT: paper-extract / paper-co-read 黑箱复测

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Raw material: `RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`
- SubAgent: Hubble
- UAT type: black-box rerun

## Prompt Leakage Check

Clean.

Prompt only provided:

- top-level tested Skill path;
- revised manuscript markdown path;
- realistic user request: use interactive reading and start first-round orientation;
- isolation rules: do not read existing discussion-outline / automatic-extraction / design-extraction / route-map / logs;
- no file modification;
- output shell: dialogue response and file-side draft content.

Prompt did not provide:

- `paper-extract` / `paper-co-read` names;
- expected A01-A08 structure;
- P1/P2 answer;
- A04/A05 block-design answer;
- previous UAT failure points.

## Expected Behavior

Hidden criteria:

- Route through the new pipeline from top-level entry.
- Recognize automatic extraction as upstream and discussion outline as co-reading workspace.
- Avoid promoting mechanism / exclusion / robustness into core proposition.
- Keep A02 as theory-level as possible, with empirical proxy moved to A03.
- Preserve A01-A08 structure.
- Preserve A04/A05 Pi-R / design block organization.
- Mark rough / source-check boundaries for table-heavy empirical details.

## Actual Behavior

PARTIAL PASS, much improved.

What improved:

- Correctly treated the task as `paper-extract -> paper-co-read`.
- Correctly proposed two file-side drafts:
  - `TASK01-automatic-extraction.md`;
  - `TASK01-discussion-outline.md`.
- Correctly marked `manuscript_paragraphs.md` as rough / needs-source-check and avoided citing precise table coefficients.
- Did not repeat the previous P4 error. Alternative explanations were treated as support branches rather than core proposition.
- File-side draft retained A01-A08.
- A04/A05 explicitly stated they should be organized by `A04-P1-R / A04-P2-R / A04-P3-R` and matching Pi-R blocks, not global variable lists.

Remaining issues:

1. A01/P1 still too proxy-heavy in the dialogue card.
   - It wrote `P1: 媒体覆盖影响基金经理交易`.
   - The better theory-level proposition should be closer to `有限注意力影响基金经理交易行为`, with `media coverage` moved to A03 as attention-trigger proxy.

2. P2 may be over-promoted.
   - It wrote `P2: 基金之间存在稳定的买媒体股倾向`.
   - This may be a supporting / measurement-persistence branch for the performance proposition rather than an independent core proposition, depending on how the final A01 is framed.

3. File-side automatic extraction draft preserved A01-A08 but did not show the Chinese template tables.
   - It did mention A04/A05 block organization, so this is not a full regression.
   - Still, if we want stronger compliance, `paper-co-read` can require that a displayed file-side draft include the table skeleton for A04/A05, not only prose bullets.

## Verdict

PARTIAL PASS.

Architecture and routing are now working under black-box conditions. The main remaining risk is not routing, but theory/proxy separation in A01/A02 and strictness of file-side template preservation.

## Patch Recommendation

Optional but useful:

- Strengthen `paper-co-read` Orientation Card rules:
  - proposition branch labels must remain theory-level;
  - empirical proxy may appear in a separate `可观察对象 / proxy` line, not as the proposition itself.
- Strengthen file-side draft requirement:
  - if showing `automatic-extraction.md` draft, include at least A01/A02/A03 and A04/A05 table skeleton or explicit block rows.

