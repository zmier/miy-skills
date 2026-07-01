# Tests

Regression tests should use small fixtures:

```text
fixtures/review-comment-sample.md
fixtures/cn-academic-sample.md
fixtures/foreign-manuscript-sample.qmd
```

Each test should generate:

```text
output.docx
conversion-log.md
style-qc-report.md
```

Green is not only “docx exists”; it must open and pass profile-specific style samples.

