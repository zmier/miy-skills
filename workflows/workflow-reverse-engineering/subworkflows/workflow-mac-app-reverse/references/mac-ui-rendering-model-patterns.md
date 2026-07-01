# Mac UI Rendering Model Patterns

## Purpose

This reference captures transferable rules for authorized Mac App reverse engineering tasks where the target behavior is produced by dynamic UI rendering: charts, tables, virtual lists, canvases, layers, or third-party plotting frameworks.

It stores workflow rules only. Do not copy target apps, logs, symbols, screenshots, account state, or case-specific evidence into this file.

## Core Rule

Do not treat a View-layer index as business identity unless it has been proven stable.

Dynamic UI frameworks often pass local indices, cells, layers, fills, colors, x positions, or visible rows to rendering methods. These values can change when the app scrolls, zooms, reloads data, completes lazy loading, refreshes caches, or swaps backing arrays.

Prefer this identity ladder:

```text
business key: date / id / code / record key
model item: dictionary / object / row / quote / data record
view-model: parser output / property map / visible offset / axis / range
view: draw call / cell / layer / fill / color / local index
```

## Recommended Route

Use static analysis before dynamic patching:

```text
1. Locate controller, parser, adapter, data source, and renderer selectors.
2. Separate first-party business classes from third-party render framework classes.
3. Identify model containers and visible range fields.
4. Use read-only runtime probes to map business key -> model item -> visible local index.
5. Only then patch behavior, preferably through a model marker.
6. Run UAT across scroll, zoom, reload, lazy loading, data completion, and return-to-target.
```

Directly patching `draw*`, `fillForIndex:`, `cellForRow:`, or layer color can be useful as an oracle, but it is not stable enough for Green unless the patched item can be traced back to a stable model identity.

## Model Marker First Pattern

When the renderer accepts only a local index, use a temporary marker on the model item:

```text
target business key
-> find model item
-> write namespaced marker
-> read visible offset/range from property/view-model layer
-> compute markerLocalIndexes
-> patch render output only when index in markerLocalIndexes
-> keep a nearby control key negative
```

Required evidence:

```text
model marker written or observed
visible offset/range observed
patched local index belongs to markerLocalIndexes
control sample observed with shouldPatch=false
UAT includes scroll/reload/data-completion cases
```

## Common Failure Pattern

Symptom:

```text
The first UAT looks correct, then the color/action drifts to a neighboring item after scroll, reload, or data completion.
```

Likely cause:

```text
The hook patched a visible local index, not the business item.
```

Fix:

```text
Move identity back to model or view-model. Use the render hook only as the final actuator.
```

## Green Level

This pattern is currently `structural-green`: it has reached minimum Green and human UAT Green in one authorized Mac App TASK, but needs forward testing on a second UI-rendering Mac App before being marked `forward-test-green`.

## Promotion Record

What the workflow lacked:

```text
No explicit route for GUI/chart rendering tasks where View-layer local indices drift.
No requirement to prove MVC/MVVM identity before modifying draw/fill/cell methods.
No model-marker checklist for Frida render hooks.
```

Observed Red:

```text
Direct View-layer patching can pass an initial visual smoke but drift after scrolling, reloading, lazy loading, cache refresh, or data completion.
Attach/hook Green does not prove the patched item still corresponds to the target business key.
```

Minimum Green:

```text
Static chain identifies model, view-model/property, and renderer roles.
Runtime probe maps business key to model item and visible local index.
Patch decision is based on a model marker, not a hard-coded View index.
Control sample remains negative through UAT.
```

Abstracted into:

```text
workflow-mac-app-reverse/SKILL.md
skills/mac-app-reverse-orchestrator/SKILL.md
skills/analyze-macho-static/SKILL.md
skills/analyze-objc-swift-runtime/SKILL.md
skills/hook-mac-app-frida/SKILL.md
skills/diagnose-macos-protection/SKILL.md
references/mac-ui-rendering-model-patterns.md
```

Still stays in TASK:

```text
Target app, bundle paths, Mach-O files, IDA databases, Frida scripts with target selectors,
raw JSONL logs, screenshots, stock/date/business IDs, UAT notes, and user confirmations.
```
