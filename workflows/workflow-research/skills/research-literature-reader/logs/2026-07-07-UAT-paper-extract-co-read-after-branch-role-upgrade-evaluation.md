# UAT Evaluation: paper-extract / paper-co-read branch-role upgrade

## UAT Setup

- Date: 2026-07-07
- UAT Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/miy-uat/SKILL.md`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Source material: `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`
- SubAgent: Faraday
- UAT type: black-box
- Raw output file: `2026-07-07-UAT-paper-extract-co-read-after-branch-role-upgrade-raw-output.md`

## Prompt Leakage Check

Clean.

Prompt only provided:

- UAT constraint Skill path;
- top-level tested Skill path;
- revised manuscript markdown path;
- realistic user request;
- isolation rules;
- generic output shell.

Prompt did not provide:

- the expected P1/P2 answer;
- the instruction to downgrade buys-vs-sells to a diagnostic branch;
- branch-role tests;
- prior UAT failures;
- hidden pass criteria.

## Expected Behavior

Hidden criteria after the branch-role upgrade:

- Route through `paper-extract -> paper-co-read`.
- Preserve theory/proxy separation.
- Keep only true core claims as P1/P2/P3.
- Treat mechanism, diagnostic implication, boundary condition, exclusion, robustness, and proxy support as `S-Pi-*` unless they pass core proposition tests.
- Preserve important supporting branches instead of dropping them.
- In co-reading, show `Core Proposition Branches` separately from `Supporting / Diagnostic Branches`.
- Save raw output separately from evaluation.

## Actual Behavior

Verdict: PASS on the targeted branch-role upgrade; PARTIAL PASS as full extraction artifact.

Strong improvements:

- The previous over-promotion issue was corrected under black-box conditions.
- SubAgent produced:
  - `P1: 有限注意力会系统性影响职业基金经理的交易选择`;
  - `P2: 受这种注意力驱动越强的基金经理，未来投资表现越差`;
  - `S-P1-diagnostic: 买入端应强于卖出端`;
  - `S-P2-exclusion: flow / news content / public-information reliance explanations`.
- The co-reading draft explicitly separates:
  - `Core Proposition Branches`;
  - `Supporting / Diagnostic Branches`.
- It preserved the important buys-vs-sells pattern, but no longer forced it into P3.
- It retained theory/proxy separation in the dialogue card.
- It flagged table / source-check boundaries.

Remaining issues:

1. File-side `automatic-extraction.md` draft became too compressed.
   - It preserved A01-A08 headings, but not the full Chinese template tables.
   - It did not include the `核心命题准入测试` table, even though the template now asks for it.
   - This is a template-compliance weakness, not a branch-role failure.

2. A03 proxy bridge is less structured than the upgraded template.
   - It uses bullets rather than the table with `代理资格 / warrant` and `支持证据 / 诊断 / 排除检验`.
   - It still answers part of the logic, but loses comparability across papers.

3. A04/A05 remain concise.
   - They use Pi-R IDs, which is good.
   - But they do not fully unpack `linked A03 bridges`, `design-support measures`, and `design function`.

4. The dialogue one-sentence finding still includes empirical implementation.
   - It says media coverage pushes stocks into attention and predicts worse performance.
   - This is acceptable as an orientation sentence, but the pure theory-layer sentence would be sharper:
     `基金经理受有限注意力影响；且受影响越强，未来表现越差。`

## Pass / Fail

Branch-role upgrade: PASS.

Full first-pass extraction artifact: PARTIAL PASS.

The specific prior bug has been fixed:

```text
diagnostic / boundary pattern no longer automatically becomes P3.
```

The new bottleneck is stricter template preservation:

```text
when showing file-side automatic-extraction draft,
subAgent may compress the template into prose/bullets instead of preserving required tables.
```

## Where It Generalized

- The branch-role rule generalized from Skill instructions without being leaked in the prompt.
- The agent kept the diagnostic branch visible and useful rather than deleting it.
- The co-reading output now better reflects the distinction between core claims and supporting claims.

## Regression Risk

Low for the targeted P3 over-promotion issue.

Moderate for file artifact quality:

- Future black-box runs may continue to produce acceptable dialogue cards but weaker file drafts.
- If downstream assets depend on table-preserved `automatic-extraction.md`, `paper-extract` / `paper-co-read` may need stronger wording: file-side draft must preserve the template tables when the user asks to show or create file drafts.

## Patch Recommendation

Optional next patch:

- Strengthen `paper-co-read` file-side draft rule:
  - If displaying `automatic-extraction.md` draft, preserve the required template sections and tables, including `核心命题准入测试`.
  - If only giving a dialogue card, compression is acceptable.
- Strengthen `paper-extract` completion standard:
  - A01 must include `核心命题准入测试` table whenever the paper has multiple candidate branches.

No urgent patch is required before continuing the substantive paper discussion; the cognitive target of this upgrade is working.
