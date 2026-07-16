# Git Hook Policy

Hooks should turn known repository policy into fast, deterministic rejection. They are not workflow robots.

## Recommended Layers

| Layer | Purpose | Mutates worktree? | Default |
|---|---|---:|---|
| `pre-commit` | Secret, binary, data-size, and general-size guard | No | Required |
| `pre-push` | Remote role and gitlink reachability guard | No | Recommended for parent repos |
| `commit-msg` | Message convention | No | Optional |
| `post-checkout` / `post-merge` | Submodule diagnostics | No | Optional, warning only |
| Server branch protection | Collaboration/review policy | No | Recommended when collaborators join |

Never use hooks to run `git add`, create commits, push, pull, update submodules, delete files, or rewrite refs.

## Pre-Commit Contract

Inspect the staged snapshot, not arbitrary working-tree files. A useful parent policy blocks:

- `.env` and high-confidence credential patterns;
- PDF/Office/images/media/archives that belong in external asset backup;
- CSV/TSV/JSONL above the repository's small-fixture threshold;
- any ordinary file above the general tracked-file threshold;
- generated plugin/theme bundles or other locally rebuilt artifacts.

Rules must support explicit, reviewed exceptions. Do not encode “ignore every file larger than N” in `.gitignore`; Git ignore patterns cannot express file size. Size belongs in the staged-file hook.

## Parent Pre-Push Contract

The hook should receive the destination remote name and URL and reject when:

1. the destination is classified as `legacy/archive`, unless an explicit emergency override is present;
2. a pushed parent commit introduces or changes a mode `160000` gitlink whose OID is not reachable from the child repository's configured remote;
3. `.gitmodules` contains an absolute local path, missing URL, or invalid mapping for a published gitlink;
4. the push attempts a non-fast-forward update without an explicit high-risk workflow.

The hook may warn, but should not normally block, when unrelated child working trees are dirty while their published gitlinks remain unchanged.

Remote verification should inspect changed gitlinks in the commits being pushed, not every child on every push. Cache/fetch carefully so a docs-only push remains fast.

## Installation And Portability

Version hook definitions and their scripts in the repository. Use the `pre-commit` framework when practical:

```bash
pre-commit install --hook-type pre-commit --hook-type pre-push
pre-commit run --all-files
```

The generated `.git/hooks/*` files are machine-local and should not be committed. A generated hook may contain a machine-specific Python path, but it must have a portable fallback and every new machine must rerun the install command.

## Bypass Policy

`--no-verify` is an emergency mechanism, not a normal workflow. When bypass is genuinely necessary:

- state which hook is wrong or unavailable;
- record the reason in the task/commit evidence;
- run the equivalent manual checks;
- repair the hook instead of normalizing bypass.

For a legacy-remote emergency override, prefer a narrowly named environment flag and require an explicit remote name. Never make the override the default shell environment.

## What Not To Add Yet

- Commit-message enforcement for a single-user knowledge repository with readable existing history.
- Full test suites that take many minutes on every tiny docs commit; use path-aware or task-specific checks.
- Automatic submodule update after checkout/merge; it can overwrite the intended local child context.
- Automatic push after commit; it removes the remote-reachability decision point.
