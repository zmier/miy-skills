# Large Repository Maintenance

Use this reference after a composite workspace has been converted to a lightweight parent plus child repositories.

## Maintenance Cadence

| Trigger | Checks |
|---|---|
| Every accepted commit | staged diff, hook result, relevant tests |
| Every child release/pointer change | child push, remote OID, parent gitlink, parent push |
| End of meaningful work session | fetch/ahead-behind, push accepted recovery points |
| Monthly or abnormal growth | object counts, largest tracked blobs, `.git/modules`, remote quota |
| Before migration/history work | external backup, refs snapshot, isolated clone, rollback plan |
| After migration | fresh clone, submodule init, tests, asset recovery UAT, retained archive |

Useful read-only measurements:

```bash
git count-objects -vH
du -sh .git .git/objects .git/modules 2>/dev/null
git for-each-ref --format='%(refname) %(objectname)'
git submodule status --recursive
git fsck --full
```

Measure parent `.git/objects` separately from `.git/modules`. A large `.git/modules` usually represents legitimate child history; deleting it as “parent bloat” breaks initialized submodules.

## Asset Boundary

- Git: source, Markdown, config, dependency declarations, small fixtures, reproducible metadata.
- Local + external backup: PDF/Office/media, complete datasets, generated outputs, runtime state.
- `.venv`: rebuild from `pyproject.toml`/lock/requirements; do not sync as an asset.

`.gitignore` only prevents new untracked files from being added accidentally. It does not remove already tracked blobs or shrink history. Use a separate tracked-file or history-governance task for that.

## History Rewrite And New Parent Repositories

History rewrite is exceptional:

1. finish planned submodule splits first;
2. snapshot refs, status, staged/unstaged patches, and backup state;
3. work in a repository-external clone, never the live worktree;
4. freeze a filter policy and run secret/size/tree/submodule tests;
5. perform a fresh-clone UAT;
6. update remote refs only through an explicit human Gate;
7. clean local refs/reflog and GC only after remote acceptance.

If an old remote cannot accept the cleaned history because of quota or platform behavior, a new lightweight parent repository may be safer than clearing the old one. Preserve the old remote as read-only archive. New and old parent repositories with unrelated roots must never be merged/rebased together.

## Recovery Anchors

Use different anchors for different failure classes:

- Git remote: tracked source and accepted history;
- child remotes: each submodule's reproducible OID;
- verified Git bundle: local-only legacy refs before GC;
- external file backup: ignored assets and working files;
- fresh-clone UAT: proof that the published graph is actually recoverable.

An external non-delete file mirror may contain stale ordinary files and old `.git` data. Restore into a new clone through an explicit missing + ignored allowlist, not an unconditional directory overlay.

## Retention And Deletion

Do not delete the old remote, migration clone, bundle, or asset backup in the same transaction that creates the replacement. Keep a defined retention period and require separate authorization after:

- the new parent and child remotes remain reachable;
- at least one fresh-clone UAT passes;
- external asset recovery passes;
- the user worktree is proven unchanged;
- the new state has reached the external backup.

Routine `git gc` is acceptable after unreachable refs are deliberately archived and removed. Avoid repeated aggressive GC without a measured reason.
