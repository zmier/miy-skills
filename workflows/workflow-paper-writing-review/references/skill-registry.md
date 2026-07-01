# Paper Workflow Skill Registry

## Purpose

This registry keeps the paper-writing-review workflow from becoming either a purely linear review checklist or an overbuilt set of empty Skills without project evidence.

It records the intended capability map, current implementation status, and provenance discipline for writing, review, revision, and pre-submission audit workflows.

## Core Architecture

```text
workflow-paper-writing-review
├── shared quality system
├── orchestrators
├── infrastructure Skills
├── reconstruction / positioning Skills
├── shared audit Skills
├── assembly / submission Skills
├── references
├── templates
└── tests
```

Writing and reviewing share the same quality ladder:

```text
Writing = forward construction
research question -> literature -> gap -> theory/mechanism -> hypotheses
-> identification/data -> results -> narrative -> submission

Reviewing = reverse validation
finished manuscript -> claimed contribution chain
-> gap/mechanism/identification/data/results/narrative validation
-> revision request or rejection rationale
```

## Status Labels

- `implemented`: Skill exists and is connected to the workflow.
- `seed`: Skill or reference exists but needs more project regression.
- `candidate`: capability is named but not yet implemented as a Skill.
- `external`: capability currently lives outside this workflow and should be called, not copied.
- `defer`: useful idea, but insufficient evidence or no near-term use.

## Implemented / Seed Skills

| Skill | Status | Layer | Direction | Role | Provenance |
|---|---|---|---|---|---|
| `paper-workflow-orchestrator` | seed | orchestrator | writing / review / revision / audit | top-level routing over paper quality system | workflow seed |
| `scholar-pdf-markdown-restoration` | seed | infrastructure | review / self-audit / writing analysis | create faithful Markdown reading base from PDF | EMFT review project |
| `scholar-docx-markdown-restoration` | seed | infrastructure | review / self-audit / writing analysis | create faithful `[para N]` Markdown reading base from DOCX, including media, footnotes/endnotes, figure QC, and restoration QC | Piqiu engineering manuscript / DOCX review need |
| `manuscript-quick-reconstruction` | seed | reconstruction | review / self-audit | reconstruct author's claimed contribution chain and Step 4 literature branch seeds | EMFT review project |
| `manuscript-literature-genealogy` | seed | positioning | review / self-audit / writing | reconstruct high-quality literature genealogy, benchmark papers, gap status, and Mermaid knowledge tree | EMFT review project |
| `manuscript-causal-identification-audit` | seed | method audit | review / self-audit / writing | translate observed relationships into causal claims, audit DAG backdoors/frontdoors/IV/controls/FE/robustness in plain language | EMFT review project |
| `manuscript-variable-data-measurement-audit` | seed | data measurement audit | review / self-audit / writing | audit construct-to-variable validity, data sources, sample, merge, code matching, timing, measurement error, and external validity | EMFT review project |
| `manuscript-results-narrative-consistency` | seed | results narrative audit | review / self-audit / writing | audit whether theory/mechanism, model/formula, data/method, results, mechanisms, heterogeneity, robustness, extensions, and conclusions form a coherent evidence chain | EMFT review project |
| `manuscript-review-material-assembly` | seed | review assembly | review / self-audit | assemble reviewer-owned contribution summary, major/minor issues, actionable author requests, editor-facing rationale notes, and provisional recommendation | EMFT review project |
| `manuscript-final-review-drafting` | seed | final drafting orchestrator | review | orchestrate priority synthesis, final drafting, optional multi-agent QA, post-flight verification, and ScholarOne field mapping | EMFT review project + external skill benchmarking |
| `review-issue-priority-synthesizer` | seed | final drafting / issue synthesis | review / self-audit | deduplicate and rank issue ledger, review materials, and QA findings into CRITICAL / MAJOR / MINOR final-review-ready issue clusters | EMFT review project + AI-research-feedback pattern |
| `multi-agent-academic-review-qa` | seed | final QA / cross-role review | writing / review / revision / self-audit | use cold reader, technical clarity, evidence boundary, and actionability roles to QA academic final drafts and expose context-blind spots before vNext | EMFT review project + repeated workflow need |
| `post-flight-review-verifier` | seed | final verification | review / self-audit / revision | verify final review drafts for evidence grounding, evidence boundary, reader bridge, actionability, paste-ready boundary, and bilingual parity before submission | EMFT review project + claude-code-my-workflow pattern |

## External Scholar-Kit Skills

These are called by this workflow but remain owned by scholar-kit.

| Skill | Status | Used By | Role |
|---|---|---|---|
| `scholar-kit-literature-search` | external | `manuscript-literature-genealogy` | umbrella routing across OpenAlex, WoS, and CNKI |
| `scholar-kit-wos-search` | external | `manuscript-literature-genealogy` | WoS searches with FT50/UTD24 or venue constraints |
| `scholar-kit-openalex-search` | external | `manuscript-literature-genealogy` | open international literature search and abstract collection |
| `scholar-kit-cnki-search` | external | `manuscript-literature-genealogy` | Chinese literature search |
| `scholar-kit-ebsco-search` | external | `manuscript-literature-genealogy` | EBSCO / Business Source result and abstract support |
| `scholar-kit-cnki-cited-by` | external | `manuscript-literature-genealogy` | CNKI cited-by tracing around key papers |
| `scholar-kit-cnki-sentence-search` | external | `manuscript-literature-genealogy` | Chinese sentence / paragraph concept co-occurrence |
| `reference-audit` | external | citation / literature audit | reference quality and citation checks |
| `publication-grade-citation-enrichment` | external | writing / revision | publication-grade citation supplementation |

## External Argument-Validity Workflow

通用论证有效性能力由独立 workflow 维护，本 workflow 只在审稿场景调用其学术适配层，不复制课程资料、谬误库或通用行文规则。

| Capability | Status | Used By | Role |
|---|---|---|---|
| `../../workflow-argument-validity/skills/academic-review-argument-audit` | external | quick reconstruction / literature genealogy / identification / measurement / results narrative / review assembly / final drafting | audit whether manuscript evidence, methods, variables, and results support the author's claimed contribution chain; draft clear reviewer concern paragraphs |

## Candidate Shared Audit Skills

These are the shared paper-quality audit modules. They should become Skills only when at least one real project produces stable inputs, outputs, and failure modes.

| Candidate Skill | Status | Writing Direction | Review Direction | Likely Inputs | Likely Outputs |
|---|---|---|---|---|---|
| `audit-research-question` | candidate | generate, narrow, and position research question | judge importance, clarity, and researchability | contribution chain; intro; abstract | research-question-audit.md |
| `audit-literature-gap` | candidate | construct and phrase literature gap | test whether gap is real, important, and not already covered | literature genealogy; introduction; references | literature-gap-audit.md |
| `audit-theory-mechanism` | candidate | build theory and mechanism chain | detect conceptual jumps, mechanism overlap, and hypothesis mismatch | theory section; hypotheses; results | theory-mechanism-audit.md |
| `audit-identification-strategy` | seed via `manuscript-causal-identification-audit` | design identification and robustness strategy | test endogeneity, exclusion restrictions, fixed effects, robustness, clustering | method section; tables; appendix; issue ledger | causal-identification-audit.md |
| `audit-data-measurement` | seed via `manuscript-variable-data-measurement-audit` | construct variables, samples, and measurement plan | test construct validity, sample restrictions, data merge, timing, missingness | data/variables section; codebook; tables; issue ledger | variable-data-measurement-audit.md |
| `audit-results-narrative` | seed via `manuscript-results-narrative-consistency` | write disciplined results story | test whether results, mechanisms, heterogeneity, extensions, and conclusions cohere | results sections; tables; figures | results-narrative-consistency-audit.md |
| `audit-contribution-positioning` | candidate | phrase contribution without overclaiming | judge novelty, distinctiveness, and overlap with benchmark papers | quick read; literature genealogy | contribution-positioning-audit.md |
| `audit-citation-quality` | candidate | add accurate and necessary references | find missing, mismatched, weak, or decorative citations | references; claims; literature matrix | citation-quality-audit.md |
| `audit-academic-expression` | candidate | improve scholarly prose and structure | detect report style, AI-like phrasing, unstable terms, and structural breaks | manuscript text | academic-expression-audit.md |
| `technical-reasoning-clarity-audit` | candidate | explain technical claims, variables, methods, and statistics with visible reasoning | test whether comments explain claimed definition, expected assumption/value, observed evidence, mismatch, implication, and requested fix | draft review text; paper sections; tables; issue ledger | technical-reasoning-clarity-audit.md |
| `multi-agent-academic-review-qa` | seed | cross-check final writing with independent roles before submission or circulation | cross-check review drafts with cold reader, technical clarity, evidence boundary, and actionability perspectives | final draft; issue ledger; review materials; human gate | multi-agent-review-qa.md; revised draft plan |
| `review-issue-priority-synthesizer` | seed | synthesize review findings into prioritized revision requests | synthesize issue ledger and review materials into final-review-ready CRITICAL / MAJOR / MINOR clusters | issue ledger; review materials; audit outputs; QA findings | final-review-issue-priority-plan.md |
| `post-flight-review-verifier` | seed | verify final author/editor-facing text before circulation or submission | verify each major comment and recommendation rationale against evidence, reader bridge, paste-ready boundary, and bilingual parity | final draft; issue ledger; review materials; human gate | final-review-post-flight-verification.md |
| `review-material-assembly` | seed via `manuscript-review-material-assembly` | prepare revision request framing | assemble contribution, major issues, minor issues, and recommendation rationale | audit outputs; issue ledger | review-materials.md |
| `review-pre-submission-gate` | seed via workflow gate | confirm human responsibility before submission | verify key evidence, live ScholarOne page, journal policy notices, COI/ethics boundaries, author/editor-facing separation, and final recommendation ownership | review materials; manuscript; journal policy | human-submission-checklist.md or review materials checklist |
| `final-review-drafting` | seed via `manuscript-final-review-drafting` | draft final review text and field mapping | draft Comments to Author, optional Confidential Comments to Editors, recommendation rationale, and ScholarOne field mapping after gate review | review materials; human gate; issue ledger; form capture | final-review-draft.md |

## Candidate Orchestrators

| Candidate Skill | Status | Role | Notes |
|---|---|---|---|
| `write-paper-orchestrator` | candidate | forward construction from target journal and contribution contract to manuscript plan | split only if writing-side use becomes frequent |
| `review-paper-orchestrator` | candidate | reverse validation from finished manuscript to review materials | current role mostly covered by `paper-workflow-orchestrator` |
| `pre-submission-audit-orchestrator` | candidate | internal review before submission | likely shares most audit Skills |
| `revision-integration-orchestrator` | candidate | integrate reviewer comments, response letter, and manuscript changes | may connect to existing revision Skills |
| `journal-form-submission-helper` | candidate | map review materials into ScholarOne / editorial form fields | must respect journal AI and confidentiality policies |

## Capability Map

```text
Material grounding
  scholar-pdf-markdown-restoration
  scholar-docx-markdown-restoration

Contribution reconstruction
  manuscript-quick-reconstruction

Literature / gap validation
  manuscript-literature-genealogy
  audit-literature-gap [candidate]
  audit-contribution-positioning [candidate]

Theory and mechanism validation
  audit-theory-mechanism [candidate]

Method and evidence validation
  academic-review-argument-audit [external via workflow-argument-validity]
  manuscript-causal-identification-audit
  audit-identification-strategy [seed via manuscript-causal-identification-audit]
  manuscript-variable-data-measurement-audit
  audit-data-measurement [seed via manuscript-variable-data-measurement-audit]
  manuscript-results-narrative-consistency
  audit-results-narrative [seed via manuscript-results-narrative-consistency]

Citation and expression validation
  audit-citation-quality [candidate]
  audit-academic-expression [candidate]
  technical-reasoning-clarity-audit [candidate]

Review assembly
  manuscript-review-material-assembly
  academic-review-argument-audit [external via workflow-argument-validity]
  review-material-assembly [seed via manuscript-review-material-assembly]
  review-pre-submission-gate [seed via workflow gate]
  manuscript-final-review-drafting
  review-issue-priority-synthesizer
  final-review-drafting [seed via manuscript-final-review-drafting]
  multi-agent-academic-review-qa
  post-flight-review-verifier
  journal-form-submission-helper [candidate]
```

## Promotion Rule

A candidate Skill can be promoted to `seed` when a real project supplies:

- repeated trigger conditions;
- stable inputs;
- stable outputs;
- quality criteria;
- at least one failure mode;
- evidence boundary rules;
- at least one template or ledger field.

A seed Skill can be promoted to `implemented` after it is reused outside the originating project or passes an explicit regression check.

## Provenance Discipline

- Project evidence stays in project / TASK folders.
- Workflow layer stores only reusable process, routing, quality criteria, templates, and failure modes.
- Do not encode confidential manuscript content into Skills.
- Do not promote a one-off judgement into a universal rule.
- External Skills should be linked and called, not copied into this workflow.

## Near-Term Build Order

For the current EMFT review practice, likely next candidates are:

1. `audit-identification-strategy`
2. `audit-data-measurement`
3. `audit-results-narrative`
4. `review-material-assembly`
5. external final-drafting pattern regression tests for `review-issue-priority-synthesizer` and `post-flight-review-verifier`

Build them only when the current review reaches those modules and produces concrete patterns worth preserving.
