# Parent And Submodule Operations

Use this reference for routine maintenance of a lightweight parent repository that coordinates independent child repositories through gitlinks.

## The Transaction

The only safe publication order is:

```text
child work
-> child tests
-> child commit
-> child push
-> verify child OID on remote
-> parent gitlink stage
-> parent commit
-> parent push
```

The parent pointer is a dependency declaration. Publishing it before the dependency exists remotely creates a parent commit that cannot be cloned reproducibly.

## 1. Inspect Before Work

```bash
PARENT="$(git rev-parse --show-toplevel)"
git -C "$PARENT" status -sb
git -C "$PARENT" submodule status --recursive
git -C "$PARENT" fetch origin --prune
git -C "$PARENT" rev-list --left-right --count HEAD...@{upstream}
```

Interpret the first submodule status character:

- space: checked-out child HEAD matches the parent gitlink;
- `-`: submodule is not initialized;
- `+`: child HEAD differs from the parent gitlink;
- `U`: gitlink conflict.

A dirty child working tree may appear as lowercase `m` or `?` in parent porcelain output. Do not treat that as permission to stage the parent path.

## 2. Commit The Child

```bash
CHILD="path/to/child"
git -C "$PARENT/$CHILD" status -sb
git -C "$PARENT/$CHILD" diff --stat
git -C "$PARENT/$CHILD" diff --cached --stat
git -C "$PARENT/$CHILD" fetch origin --prune
```

If the branch is behind or diverged, stop and integrate deliberately under the child repository's policy. Do not run `git submodule foreach git pull`.

Stage only the topic:

```bash
git -C "$PARENT/$CHILD" add -- path/a path/b
git -C "$PARENT/$CHILD" diff --cached --check
git -C "$PARENT/$CHILD" diff --cached --stat
git -C "$PARENT/$CHILD" commit -m "<type>: <child change>"
```

Run the child repository's relevant tests before or during this checkpoint.

## 3. Push And Verify The Child

```bash
git -C "$PARENT/$CHILD" push origin HEAD
CHILD_OID="$(git -C "$PARENT/$CHILD" rev-parse HEAD)"
git -C "$PARENT/$CHILD" fetch origin --prune
git -C "$PARENT/$CHILD" branch -r --contains "$CHILD_OID"
```

The final command must show an expected remote-tracking branch. For stronger evidence, compare against `git ls-remote origin` or a temporary fresh clone.

## 4. Commit The Parent Pointer

First confirm the child HEAD is the intended pointer:

```bash
git -C "$PARENT" diff --submodule=log -- "$CHILD"
git -C "$PARENT" add -- "$CHILD"
git -C "$PARENT" diff --cached --submodule=log
```

Stage `.gitmodules` only when its content intentionally changed. Do not stage child-internal files from the parent.

Commit and push:

```bash
git -C "$PARENT" commit -m "chore: update <child> gitlink"
git -C "$PARENT" push origin HEAD
git -C "$PARENT" status -sb
```

Multiple gitlinks may share one parent commit only when they form one documented release/governance transaction and every child OID is already remote-reachable.

## Parent-Only Changes

For parent docs, indexes, ignore rules, governance scripts, or shared config:

1. inspect the global dirty worktree;
2. stage explicit parent-owned pathspecs only;
3. inspect `git diff --cached`;
4. commit after relevant checks;
5. push the accepted commit in the same work session.

Unrelated dirty children do not need to be cleaned merely to commit an independent parent-owned topic.

## Child Dirty But Pointer Unchanged

If a child contains uncommitted work but remains at the gitlink OID:

- leave it alone;
- do not stage the child path in the parent;
- do not run recursive clean/reset commands;
- report that parent publication excludes the child-internal work.

If the child HEAD moved locally, either complete the child transaction or restore the intended checkout only with explicit user approval. Never conceal the mismatch by staging an unpushed OID.

## Failure Rules

- Child push fails: stop; do not stage or push the parent gitlink.
- Parent push fails after child succeeded: child is safe; retry or repair only the parent.
- Remote child OID cannot be verified: treat the transaction as incomplete.
- Parent points to wrong child OID: create a new parent correction commit; avoid rewriting shared history.
- Need old parent history: use a separate clone/archive; never graft it onto a new unrelated-root parent.
