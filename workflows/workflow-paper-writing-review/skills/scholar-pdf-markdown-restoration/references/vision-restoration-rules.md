# Vision Restoration Rules

Use this reference when rough PDF extraction is not enough and the restored Markdown must be corrected against rendered PDF pages.

These rules adapt the useful parts of `pdf2md-skill` to the `workflow-paper-writing-review` setting. The goal is not to create a generic single-file PDF conversion. The goal is to produce a review-ready restored Markdown source with section files, `[para N]` anchors, formulas, tables, figures, Obsidian embeds, and a QC ledger.

## Operating Mode

Prefer this order:

1. Use project-local scripts to generate rough Markdown, page images, raw back matter, and table/figure inventories.
2. Open the relevant rendered PDF page image when a paragraph, formula, table, or figure is uncertain.
3. Use the model's visual and semantic understanding to restore the original source faithfully.
4. Write corrections into `outputs/*_manuscript_restored.md` and `outputs/sections-restored/*.md`.
5. Record high-risk fixes and verified ranges in `logs/restoration-qc.md`.

Do not wait for perfect automation when the model can directly restore the text from the PDF image.

## Reading Order

- For two-column pages, read left column first, then right column, top to bottom.
- For single-column pages, preserve vertical order, but remove page headers, footers, line numbers, and peer-review watermarks.
- Full-width objects such as title, abstract, figure, table, or appendix heading should be placed according to the paper's logical flow, not merely by extraction order.
- Never split one PDF natural paragraph into multiple `[para N]` entries just because a line break, column break, or page break occurs.
- Never merge two natural paragraphs merely because the extractor placed them on one line.

## Heading Hierarchy

Do not infer heading level from font size alone.

Use a two-pass check:

1. Page pass: note each heading candidate's text, numbering pattern, and visual weight.
2. Whole-document pass: correct heading levels by semantic nesting and section numbering.

Rules:

- The article title is the only top title.
- Top-level sections such as Abstract, Introduction, Data, Methodology, Results, Conclusion, References, Appendix, or numbered siblings like `1`, `2`, `3` should share the same heading level.
- Subsections such as `3.1`, `3.2` live under their parent section.
- Preserve section numbers only when printed in the PDF.
- Do not let cover-page metadata, running headers, journal names, page labels, or line numbers become headings.

## Metadata And Noise

Remove from ordinary正文:

- page numbers;
- line numbers;
- running headers and footers;
- `For Peer Review` watermarks;
- journal system boilerplate;
- submission metadata unless the project intentionally keeps a cover-page inventory.

If metadata is useful for the project, put it in a project note or front matter, not as numbered正文 paragraphs.

## Paragraph Anchors

- `[para N]` attaches only to natural prose paragraphs.
- Equations, figures, tables, table notes, figure captions, reference entries, and page boilerplate do not receive `[para N]`.
- When a paragraph continues across pages, keep one paragraph anchor.
- When a paragraph contains a first textual reference to a figure/table, keep the reference inside that paragraph, then place the figure/table insertion block immediately after the paragraph unless the manuscript uses an explicit `[Insert ... about here]` placeholder.
- After fixing split/merge errors, renumber paragraphs continuously and update section files consistently.

## Equations

Every displayed equation must be restored as Markdown display math:

```markdown
$$
...
\tag{1}
$$
```

Rules:

- Preserve equation numbering with `\tag{N}` when the PDF prints an equation number.
- Use `aligned`, `split`, or line breaks for multi-line formulas.
- Distinguish Greek letters, subscripts, superscripts, bold vectors, scalars, fixed effects, and error terms from the surrounding variable definitions.
- Check bracket nesting before accepting a formula.
- Do not leave formula fragments as italic inline text if the PDF shows a display equation.
- If the formula is econometric notation, make it readable to an applied economics reviewer, not merely visually similar.

## Figures

Academic figures are floats. In our workflow, distinguish three locations:

- first textual reference in正文;
- explicit insertion placeholder such as `[Insert Figure 1 about here]`;
- actual Figure object location, often in back matter.

Rules:

- If the manuscript contains an explicit insertion placeholder, keep it as the anchor and annotate both `insertion position` and `actual Figure location`.
- If no explicit placeholder exists, place the figure after the paragraph containing the first textual reference.
- Never insert a Figure between two halves of one paragraph.
- Never use a whole PDF page image as the Figure object unless the entire page is the figure.
- Crop the Figure object precisely from its actual PDF location.
- Include Figure title, Alt Text if present, figure body, notes/caption/source, legends, and visible arrows/edges.
- Embed using Obsidian syntax:

```markdown
![[figures-restored/figure-01.png]]
```

## Tables

Academic tables are floats. Apply the same logical placement principles as figures, with this workflow-specific preference:

- restore tables as Markdown table files first;
- embed them by Obsidian transclusion at the insertion location.

Rules:

- Preserve table number, title, PDF page, Alt Text if present, notes, standard error convention, significance legend, observations, and fit statistics.
- Flatten merged or multi-level headers into readable Markdown columns when possible.
- Ensure every Markdown table row has the same number of columns.
- Preserve bolding only when it is visible and meaningful in the PDF.
- Do not use screenshots as the primary table representation unless a table is impossible to reconstruct. If screenshots are used, explain the fallback in QC.

## Cross-Page Continuity

For every page boundary in a high-risk section:

- check whether the last sentence on page N continues on page N+1;
- check whether a top-of-page figure/table caused following text to be dropped;
- check whether a paragraph was duplicated after a page break;
- check whether headers, footers, or line numbers were inserted into正文;
- check whether a sentence mentioning a figure/table lost its continuation.

If a page boundary is fixed, note it in `restoration-qc.md` when the affected paragraph is important for later review.

## Back Matter

Back matter is part of the restored source, even though it is not numbered as正文.

Rules:

- After Conclusion, inspect the remaining PDF pages for Conflict of Interest Statement, References, Data Availability, Funding, Acknowledgments, Appendix, supplemental statements, and author notes.
- Preserve these sections in the main restored manuscript after the final numbered paragraph.
- Create a separate restored section file for back matter when the project uses `outputs/sections-restored/`.
- Do not assign `[para N]` to reference entries, declarations, appendix headings, or figure/table back matter.
- Raw back matter is only verification material; if References are present in raw back matter but absent from the restored manuscript, the restoration is incomplete.
- Use PDF page images for visual verification when line breaks, italics, accents, page continuation, or reference boundaries are unclear.

## Validation Checklist

Before marking a restored range as trusted:

- headings are semantically nested;
- `[para N]` anchors correspond to natural paragraphs;
- no page noise remains in正文;
- displayed formulas are `$$...$$` LaTeX;
- figure/table placeholders and actual object links are separated when needed;
- figures are precise crops, not whole pages;
- tables are Markdown tables unless explicitly downgraded;
- References and other back matter are present in restored Markdown and not only in raw extraction files;
- no paragraph is lost, duplicated, split mid-sentence, or merged across natural boundaries;
- QC states what range was visually verified against PDF pages.
