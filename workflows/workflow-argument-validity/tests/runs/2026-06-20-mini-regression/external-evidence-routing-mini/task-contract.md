# Task Contract: External Evidence Routing Mini

## Mode

```text
mode: route-only smoke-regression
```

## Tested Skill

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-arrow-audit/skills/academic-argument-arrow-audit/SKILL.md
```

## Goal

Verify that full-evidence audit uses evidence-type routing:

- literature gap -> scholar-kit / OpenAlex / WoS / CNKI route;
- citation verification -> scholar-kit / DOI / journal metadata;
- policy/regulatory evidence -> official source route;
- table/figure/numeric conflict -> source QC route with model vision, not external web search.

## Input

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/external-evidence-routing-mini/external-evidence-request-mini.md
```

## Required Actions

1. Read the tested Skill and the fixture README.
2. Read `scholar-kit-literature-search/SKILL.md` only enough to identify the correct scholarly route. Do not run full database searches.
3. Produce `outputs/evidence-route-plan.md`.
4. Produce `outputs/external-evidence-ledger.route-only.md`.
5. Produce `outputs/pass-fail.md`.
6. Write `log.md`.

## Forbidden

- Do not run broad web searches.
- Do not claim a route has been completed unless actually executed.
- Do not treat route-only output as final evidence.
- Do not read TASK08/TASK09/TASK10 outputs.

## Pass Criteria

- MR01 routes to `scholar-kit-literature-search`, not generic web.
- MR01 mentions English OpenAlex/WoS and Chinese CNKI consideration.
- MR02 routes to scholar-kit / DOI / journal metadata.
- MR03 routes to official policy/regulatory sources.
- MR04 routes back to PDF/DOCX source QC with model vision.
- Any unexecuted route is marked as route-only / not-executed, not as true-zero-result.

