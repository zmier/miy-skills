# UAT Evaluation: extract -> finalize after claim-ledger upgrade

- Date: 2026-07-07
- UAT type: black-box / gray-box
- Tested route: `paper-extract -> paper-finalize`
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Raw output: `2026-07-07-UAT-extract-finalize-after-claim-ledger-upgrade-raw-output.md`

## Whether The UAT Was Clean

PASS.

The prompt did not disclose the expected proposition structure, known previous bug, exact claim-status fix, or desired answer. It only provided:

- tested Skill entry path;
- original manuscript path;
- realistic user task;
- isolation rules;
- output shell.

The SubAgent reported that it did not read `logs/`, existing outputs, or prior artifacts.

## Expected Behavior

The upgraded `paper-finalize` should:

- keep output language Chinese by default, with necessary English terms retained or bracketed;
- produce the three-artifact finalization shape: `final-literature-note.md`, `verified-claims.md`, `source-check-log.md`;
- distinguish author textual summaries, method descriptions, directional table results, exact table values, and agent reconstructions;
- avoid treating precise percentages, coefficients, t-stats, R2, sample sizes, and table-derived values as plain `verified-citable` unless PDF/table source has been checked;
- preserve proposition-branch reading from `paper-extract` while upgrading claim status and source-check discipline;
- make `source-check-log.md` a claim-by-claim ledger rather than a generic summary;
- correctly mark cold-start finalization because `paper-co-read` was not performed.

## Actual Behavior

The SubAgent output:

- Chinese-oriented finalization output with necessary English terms and variable names retained.
- A route-consistent result: `paper-extract -> paper-finalize`, no `paper-co-read`.
- A clear cold-start note: `discussion-outline.md` was not generated.
- Drafts for:
  - `automatic-extraction.md`;
  - `final-literature-note.md`;
  - `verified-claims.md`;
  - `source-check-log.md`.
- Claim statuses including:
  - `verified-citable-text-summary`;
  - `verified-citable-method-description`;
  - `verified-citable-directional-result`;
  - `verified-understanding`;
  - `needs-source-check`.
- A correct warning that Markdown table leakage means exact coefficients, t-stat, R2, sample size, and similar values require PDF/table source checks.
- The precise `1.1%-2.8%` statement was not upgraded to `verified-citable-table-value`; it was marked as text-summary with table-value risk.
- Agent reconstructions such as design strength and transfer-to-project were marked `verified-understanding`, not author-citable claims.
- `source-check-log.md` was claim-by-claim and includes checked source, action, status, remaining risk, and next check.

## Pass / Fail

PASS, with minor improvement opportunities.

This UAT demonstrates that the latest `paper-finalize` upgrade fixed the important previous failure mode: the agent no longer treats exact numerical performance differences and table-derived values as ordinary citable facts merely because they appear in prose or leaked Markdown table text.

## Where It Generalized

- It correctly separated:
  - author textual summaries;
  - methods descriptions;
  - directional empirical results;
  - exact table/PDF values;
  - agent reconstructions.
- It handled cold-start finalization without requiring `paper-co-read`.
- It carried the proposition-branch structure from extraction into finalization without collapsing everything into one global X/Y.
- It produced a source-check ledger that is usable for later PDF verification.

## Where It Only Followed Prompt

The prompt required output drafts for the three finalization files, so producing those artifacts is not by itself evidence of generalization. The stronger evidence is the internal claim-status discipline and the source-check ledger, which were not specified in the prompt.

## Regression Risk

Low to medium.

The route and claim-status behavior now look usable. Remaining risks:

- The raw UAT output is still a draft, not an actual source-verified final note; it did not open the PDF.
- Some statements remain too close to "verified" wording even when they rely on paragraph-level table summaries. The file mitigates this by marking remaining risk, but future agents may still quote them too confidently.
- The generated `automatic-extraction.md` is long and may still include table-derived directional conclusions before finalization status is applied; this is acceptable for extraction, but the handoff boundary must stay clear.
- Formula checks remain weak because `manuscript_paragraphs.md` has OCR / parsing noise.

## Next Patch

No immediate patch is required.

Optional future hardening:

- Add a small "finalization quote rule": citation-ready statements with exact numbers must include an inline caution such as `table-value-needs-check` until PDF/table verification.
- Add a "PDF-required final mode" variant for true publication-grade notes.
- Add a "source anchor density" requirement: every citation-ready claim should include at least one source anchor and a source type, e.g. `abstract`, `intro`, `method`, `table`, `conclusion`.

## Overall Verdict

The upgraded `paper-finalize` is now basically usable for the `extract -> finalize` route.

It has clear information gain over pure `paper-extract`: pure extraction organizes the argument and variables; finalization upgrades it into a claim-status-aware, source-checkable, library-ready note with explicit boundaries between citable claims, understanding-only reconstructions, and PDF/table checks still needed.
