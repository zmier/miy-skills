# External Peer Review Orchestration

## Purpose

This reference fixes the reusable orchestration pattern for external manuscript review projects.

It coordinates project intake, manuscript restoration, contribution-chain reconstruction, literature positioning, method and variable audit, result consistency checks, and review-material assembly. It does not generate the final review report on behalf of the reviewer.

## Review As Knowledge Expansion

External review is not merely error hunting. In this workflow, review is treated as a way to enter a research field, update the reviewer's own knowledge system, and then conduct a disciplined scholarly conversation with the manuscript's authors.

Use the manuscript as an entry point:

```text
manuscript as guide
-> reconstruct the field's knowledge tree
-> clarify concepts, benchmark papers, methods, variables, and open controversies
-> locate the manuscript's actual position in that tree
-> turn the resulting understanding into constructive peer dialogue
```

The manuscript author may be treated as a talkative travel companion through the field: listen first, map the terrain, then respond with evidence. This principle should shape the tone of every module, especially literature positioning, variable audit, and final review-material assembly.

Tone principle:

```text
Be grateful for the landscape the author brings;
be serious about calibrating the map.
```

This means review materials should be generous about the question and learning opportunity, but precise about conceptual slippage, literature overclaiming, measurement problems, identification weaknesses, and narrative overreach.

## Core Boundary

```text
Workflow / Skill layer:
  reusable process, quality dimensions, ledgers, routing, and evidence boundaries

Project / TASK layer:
  specific manuscript files, paragraph-level notes, journal-system captures,
  confidential comments, author-facing comments, and final recommendation
```

Do not move confidential manuscript text, author identity, ScholarOne links, login URLs, or final review comments into this workflow reference.

## Ten Modules

Cross-module rule:

During the review conversation, questions raised by the user are part of the review evidence stream. If a question identifies a possible weakness in literature positioning, construct validity, measurement, identification, data, results, narrative, or presentation, update the project-level `notes/review-issue-ledger.md` immediately. Do not leave such concerns only in chat history.

For empirical manuscripts, also use `references/empirical-paper-component-coverage.md` as a crosswalk between the author's chapter logic and this review workflow:

```text
author structure:
theory/mechanism -> model/formula -> data/method -> results

review validation:
contribution chain -> literature positioning -> identification -> measurement -> results narrative -> review assembly
```

The crosswalk is a coverage check, not a replacement for the eight modules.

Argument-validity checks are maintained by a separate shared workflow:

```text
../../workflow-argument-validity/
```

When a review task asks whether evidence supports a claim, whether the actual observed finding matches the elevated contribution, or whether a review paragraph explains the inferential gap clearly, call:

```text
../../workflow-argument-validity/skills/academic-review-argument-audit/SKILL.md
```

This reference should not duplicate the general fallacy taxonomy or course-derived notes.

### 1. Project Intake and Archiving

Goal: establish the review project as a reproducible local workspace.

Typical outputs:

- review project README;
- source-material index;
- submission-form notes;
- deadline and status tracking;
- sensitive-information boundary note.

Key question:

```text
What is this review task, where are the materials, and how will it be submitted?
```

### 2. Manuscript Text Grounding

Goal: create a stable, citable reading base before substantive judgement.

Typical outputs:

- PDF or HTML to Markdown TASK;
- paragraph-numbered manuscript;
- extraction log;
- back-matter separation;
- human QC checklist for equations, tables, page boundaries, headings, and paragraph splits.

Key question:

```text
How do we point reliably to the exact paragraph, table, claim, or formula under discussion?
```

### 3. Fast Manuscript Reconstruction

Goal: reconstruct what the paper claims to do before evaluating it.

Recommended Skill:

- `skills/manuscript-quick-reconstruction/SKILL.md`

Checklist:

- research question;
- theory or conceptual frame;
- core variables;
- data and sample;
- identification or research design;
- headline results;
- claimed contributions;
- actual observed finding versus claimed finding;
- paper structure.

Typical output:

- `notes/quick-read-contribution-chain.md`;
- contribution-chain table;
- initial reviewer questions routed to later modules.

Key question:

```text
What does the manuscript say it is doing?
```

### 4. Literature Positioning

Goal: locate the manuscript inside the relevant literature system.

Recommended Skill:

- `skills/manuscript-literature-genealogy/SKILL.md`

Core aim:

- reconstruct the knowledge tree / literature genealogy around the manuscript;
- use high-quality literature as the main trunk: FT50, UTD24, field top journals, comprehensive top journals such as `Nature`, `Science`, and `PNAS`, and Chinese journals at least at the Sichuan University Social Science B level;
- use abstracts and metadata for synthesis, not just search-result listing;
- produce a Mermaid genealogy tree that marks key literature nodes and the manuscript's claimed position.

Common axes:

- primary topic literature;
- method or identification literature;
- data or setting literature;
- theory or mechanism literature;
- closely adjacent outcome-variable literature;
- benchmark papers the manuscript must distinguish itself from.

Typical output:

- literature-positioning matrix with columns for literature stream, representative papers, core finding, manuscript's claimed difference, and reviewer concern.
- Mermaid knowledge genealogy tree with key benchmark papers.

Key question:

```text
Is the claimed gap real, important, and sufficiently distinct from existing work?
```

### 5. Identification and Method Audit

Recommended Skill:

- `skills/manuscript-causal-identification-audit/SKILL.md`

Core aim:

- translate the author's causal language into plain observed X-Y relationships;
- compare actual observed findings with claimed causal findings;
- use DAGs to inspect backdoor paths, possible frontdoor/mechanism logic, IV assumptions, controls, fixed effects, PSM, DiD, and robustness;
- explain the causal logic in plain Chinese rather than reproducing the author's technical phrasing.

Goal: test whether the empirical design supports the paper's causal or interpretive claims.

Checklist:

- endogeneity sources;
- fixed effects and controls;
- instrument relevance and exclusion restriction if IV is used;
- matching, DiD, event-study, or other design assumptions where applicable;
- mechanism-test interpretation;
- robustness checks and placebo logic;
- clustering, standard errors, and sample selection.

Key question:

```text
Can the design support the conclusion, or does the manuscript overclaim?
```

### 6. Variable, Data, and Measurement Audit

Recommended Skill:

- `skills/manuscript-variable-data-measurement-audit/SKILL.md`

Goal: check whether the paper measures what it claims to measure.

Checklist:

- dependent-variable construct validity;
- treatment or core explanatory-variable definition;
- data merge and harmonization rules;
- sample restrictions;
- timing and lag structure;
- missingness and selection;
- external validity boundaries.

Key question:

```text
Do the variables and data operationalize the theory and research question?
```

### 7. Result and Narrative Consistency

Recommended Skill:

- `skills/manuscript-results-narrative-consistency/SKILL.md`

Goal: inspect whether the paper's results, mechanisms, heterogeneity, and extensions form a coherent evidence chain.

Checklist:

- empirical paper component coverage: theory/mechanism, model/formula, data/method, and results;
- theory-to-hypothesis consistency;
- model/formula-to-variable consistency;
- baseline-to-robustness consistency;
- mechanism evidence versus mechanism interpretation;
- heterogeneity explanation versus observed pattern;
- extension analyses versus main contribution;
- conclusions versus evidence strength.

Key question:

```text
Does the manuscript tell a disciplined evidence story, or does it stack significant results?
```

### 8. Review Material Assembly

Recommended Skill:

- `skills/manuscript-review-material-assembly/SKILL.md`

Goal: assemble reviewer-owned materials that can support a human-written review.

Typical outputs:

- contribution summary;
- major concerns;
- minor concerns;
- actionable revision requests;
- evidence references by paragraph, table, or section;
- confidential editor notes, if needed;
- provisional recommendation rationale.

Key question:

```text
What should the reviewer say, to whom, and with what evidence?
```

### 9. Human Pre-Submission Gate

Goal: run a final human-responsibility checkpoint before drafting or submitting the actual review.

This gate is not another substantive audit and does not ask AI to submit the review. It checks whether the reviewer has personally confirmed the evidence and policy boundaries needed to move from reviewer-owned materials to final author-facing and editor-facing text.

Checklist:

- key claims, paragraphs, tables, equations, and statistical results have been manually re-read;
- core variable definitions, model specifications, identification evidence, and result tables have been spot-checked against the manuscript;
- live ScholarOne page, journal policy notices, and confidentiality requirements have been checked;
- conflict of interest has been checked;
- ethics, duplicate-publication, plagiarism, data-fabrication, or image/table-manipulation red flags have been considered;
- author-facing comments and editor-facing/confidential notes are separated;
- provisional recommendation has been converted into a human-owned final recommendation only after the above checks.

Typical outputs:

- final human-gate checklist;
- list of unresolved items that must be checked before submission;
- optional outline for the human-written review report.

Key question:

```text
Is the reviewer ready to take responsibility for the final review text and recommendation?
```

### 10. Final Review Drafting

Recommended Skill:

- `skills/manuscript-final-review-drafting/SKILL.md`
- Priority synthesis Skill: `skills/review-issue-priority-synthesizer/SKILL.md`
- Optional QA Skill: `skills/multi-agent-academic-review-qa/SKILL.md`
- Post-flight verification Skill: `skills/post-flight-review-verifier/SKILL.md`

Goal: convert reviewer-owned materials and the human gate into an editable final review draft through priority synthesis, drafting, optional multi-agent QA, and post-flight verification.

Typical outputs:

- `Comments to the Author` draft;
- optional `Confidential Comments to the Editors` draft;
- recommendation rationale draft;
- ScholarOne field mapping;
- human finalization checklist;
- post-flight verification table.

Key question:

```text
How should the reviewer say the final judgment, to whom, and in what field?
```

Optional multi-agent QA:

Use `multi-agent-academic-review-qa` when the final draft involves complex technical reasoning, bilingual review text, possible reader-background gaps, or a user explicitly asks for multi-Agent / cold-reader review. The QA should separate at least four perspectives: cold reader, technical clarity, evidence boundary, and author-facing actionability. The main agent integrates and decides; subAgent outputs are not submitted directly.

Post-flight verification:

Before treating a draft as paste-ready, use `post-flight-review-verifier` to check that each major comment and recommendation rationale maps to evidence, stays within evidence boundaries, contains enough reader background, and does not include internal workflow notes. A `FIX` or `HUMAN_CHECK` verdict blocks “ready to submit” language.

## Recommended Execution Order

Use this default route unless the user has an urgent narrower need:

```text
1 Project Intake
-> 2 Manuscript Text Grounding
-> 3 Fast Manuscript Reconstruction
-> 4 Literature Positioning
-> 5 Identification and Method Audit
-> 6 Variable, Data, and Measurement Audit
-> 7 Result and Narrative Consistency
-> 8 Review Material Assembly
-> 9 Human Pre-Submission Gate
-> 10 Final Review Drafting
```

Modules 2, 4, 5, and 6 can run in parallel after enough manuscript context exists.

## Status Labels

Use the shared status labels from `paper-quality-system.md` for claims and quality items:

- `unexamined`
- `questioned`
- `supported`
- `weak-supported`
- `unsupported`
- `overclaimed`
- `revision-needed`
- `acceptable`

## AI Assistance Boundary

The workflow may help organize materials, reconstruct claims, prepare matrices, identify possible concerns, and make evidence ledgers.

For external peer review, the reviewer remains responsible for:

- reading the manuscript;
- judging novelty and validity;
- writing the submitted author-facing and editor-facing review text;
- choosing the recommendation;
- satisfying journal policies on AI tool use and confidentiality.
