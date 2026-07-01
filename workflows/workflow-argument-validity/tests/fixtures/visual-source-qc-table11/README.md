# Fixture: Visual Source QC Table 11

## Purpose

Minimal fixture for testing whether PDF/DOCX restoration rules force model-vision source QC instead of merely saying "needs visual QC".

## Source

Extracted from CASE-J-260110-xinyuan-review TASK05 restored PDF workflow.

## Files

- `page-19.png`: rendered PDF page containing the start of Table 11.
- `page-20.png`: rendered PDF page containing continuation/tail of Table 11.
- `table-11.restored.md`: restored Markdown reconstruction of Table 11.

## Expected Test Behavior

A clean agent should:

1. use model vision on `page-19.png` and `page-20.png`;
2. compare page images against `table-11.restored.md`;
3. produce `table-visual-qc.md`;
4. explicitly state whether visual QC was performed;
5. not mark `cell-level audited` unless it actually performs cell-level checking;
6. detect or preserve the key risk:

```text
PDF/restored table indicates PosCAR[-10,10] is not significant and NegCAR[-10,10] is significant.
This conflicts with the author prose if the prose claims the opposite.
```

