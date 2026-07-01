# Fixture: External Evidence Routing Mini

## Purpose

Minimal fixture for testing whether `academic-argument-arrow-audit` full-evidence mode routes external evidence by evidence type.

This fixture does not require running full database searches. It tests routing discipline:

- literature/citation requests must route to scholar-kit / OpenAlex / WoS / CNKI as appropriate;
- official policy/data requests must route to official sources;
- table/figure/numeric conflicts must route back to source QC rather than external web search.

## Files

- `external-evidence-request-mini.md`: tiny request table with four request types.

