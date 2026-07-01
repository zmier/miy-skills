# External PDF-to-Markdown Skill Evaluation

Last checked: 2026-06-18

## Verdict

Do not replace `scholar-pdf-markdown-restoration` with an external GitHub Skill.

Use a hybrid approach:

- Borrow `pdf2md-skill`'s vision-first restoration rules.
- Borrow `doc2md`'s pipeline/QC ideas selectively.
- Borrow `claude-skill-pdf-to-markdown`'s lightweight fast-mode extraction pattern only as an optional rough extraction layer.
- Keep our own workflow constraints as the authority: section-split restored Markdown, `[para N]`定位, Obsidian embeds, back-matter Figure/Table回填, Markdown table transclusion, and project-local restoration QC.

## Candidate: `yuhaoliu7456/pdf2md-skill`

Source: https://github.com/yuhaoliu7456/pdf2md-skill

Type: single-file Claude Code / Cursor Skill.

Useful ideas:

- Render PDF pages as images and let the LLM read pages visually.
- Use semantic heading hierarchy rather than font size alone.
- Treat figures and tables as floats and place them after their first textual reference.
- Reconstruct formulas as LaTeX display math and preserve equation numbering.
- Cross-check page boundaries for split paragraphs and dropped sentences.

Why not directly use:

- It outputs a single Markdown file, not our project/TASK structure.
- It does not provide `[para N]`全文定位.
- It does not enforce Obsidian `![[...]]` embeds.
- It does not distinguish正文插入位置 from文末实际 Figure/Table 位置 in the way our review workflow needs.
- It has no project-local restoration QC ledger.

Adopt into our Skill:

- Vision-first restoration as the preferred manual/model repair mode.
- Cross-page continuity check.
- Semantic heading hierarchy check.
- Float placement as a conceptual rule, adapted to our `insertion position` + `actual location` convention.

## Candidate: `neoncapy/doc2md`

Source: https://github.com/neoncapy/doc2md

Type: large conversion pipeline with a Claude Code Skill.

Useful ideas:

- Multi-tool routing and fallback: Marker, PyMuPDF, pymupdf4llm, pdfplumber, Docling, MinerU, Tesseract.
- Structural QC as a hard gate.
- Image inventory / manifest thinking.
- Repeat fix-and-rerun QC loops.

Why not directly use:

- The Skill is large and project-opinionated.
- Its scripts are a full platform, not a small project-local helper.
- It includes many document types and office workflows outside our current scope.
- It is designed for generic high-fidelity conversion, not审稿底稿 with paragraph anchors and Obsidian-native assets.

Adopt into our Skill:

- Keep a tool-router mindset: fast extractor first, model restoration/QC second, heavier fallback only when justified.
- Add structure/QC checks before downstream manuscript review.
- Consider a lightweight manifest for figures/tables if repeated projects need it.

## Candidate: `aliceisjustplaying/claude-skill-pdf-to-markdown`

Source: https://github.com/aliceisjustplaying/claude-skill-pdf-to-markdown

Type: lightweight Skill with Python scripts.

Useful ideas:

- `pymupdf4llm.to_markdown(..., table_strategy="text", write_images=True)` as fast mode.
- Optional Docling mode for complex tables.
- Persistent cache keyed by source PDF and extraction mode.
- Image extraction and Markdown image summaries.

Local EMFT fast-mode trial:

- Ran on `EMFT-2026-0709_Proof_hi.pdf` using Writer `.venv`.
- Completed 43 pages in about 6 seconds.
- Output was useful as a rough extraction reference, but not acceptable as final review Markdown:
  - page line numbers and headers leaked into正文;
  - paragraphs were duplicated or merged at page boundaries;
  - formulas remained noisy inline text rather than clean `$$...$$`;
  - tables were often collapsed or malformed;
  - figures were not restored as precise Obsidian-linked objects.

Why not directly use:

- It optimizes "load whole PDF into context", not faithful审稿底稿.
- It does not solve paragraph anchors, formula restoration, or back-matter figure/table回填.
- Docling is not currently installed in Writer `.venv`; adding it should be a deliberate optional experiment, not a default dependency.

Adopt into our Skill:

- Add an optional rough-extraction backend based on `pymupdf4llm` fast mode.
- Use caching only if repeated extraction becomes costly.
- Do not treat its Markdown output as restored Markdown.

## Candidate: Marker / Nutrient / Other Extractors

These are better understood as extraction tools or tool-backed Skills, not replacements for this workflow.

Use only as optional rough extraction layers when:

- the manuscript is long;
- the current PyMuPDF/pymupdf4llm extraction is poor;
- formula/table density makes a second extractor useful for comparison;
- the project can tolerate extra dependency setup.

Do not use them to bypass model-assisted restoration and PDF visual verification.

## Decision Rule

For this workflow, choose in this order:

1. Project-local extraction script with existing Writer `.venv` dependencies.
2. Manual/model restoration against PDF page images.
3. Optional fast-mode alternative extraction with `pymupdf4llm` if it gives useful cross-check material.
4. Optional heavy extractor experiment, such as Docling/Marker/MinerU, only when a TASK explicitly calls for it.

External Skills are references and optional tool sources. The authoritative workflow remains `scholar-pdf-markdown-restoration`.
