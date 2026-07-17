---
name: miy-git
description: Git 仓库治理与长期运维 Skill。用于检查和清理脏工作树、按主题提交、治理 .gitignore、识别应提交/应忽略文件、维护轻量父仓与 submodule、读取 alib 工作区子仓登记表、决定何时 commit/push、验证 gitlink 远端可达、设计 pre-commit/pre-push 守门、创建或迁移 Gitee/GitHub 子仓、控制仓库体积并规划安全历史重建。适用于用户要求“治理 git”“弄干净仓库”“提交 push”“拆 submodule”“维护总库和子库”“有哪些子仓”“设计 hook”“创建新仓库”“接入 Gitee MCP”“仓库体积治理”“不要漏 add logs”等场景。
---

# Miy Git

Use this Skill to turn messy Git state into a clear, reproducible repository state. Prefer small, explainable commits and never hide uncertainty behind a forced cleanup.

## Core Rules

- Inspect before acting: run `git status --short`, `git status -sb`, `git diff --stat`, `git diff --cached --stat`, and submodule checks before staging.
- Do not use destructive commands such as `git reset --hard`, `git clean -fd`, or `git checkout --` unless the user explicitly asks for that exact operation.
- Separate unrelated work into separate commits. Do not mix workflow edits, vendor/submodule updates, generated caches, and project artifacts in one commit.
- Treat ignored files as a governance surface. Check whether ignored Markdown logs, TASK records, QC reports, or provenance files should be tracked.
- Push submodule commits before pushing the parent repository that points at those commits.
- A parent repository is an orchestrator, not an owner of child-internal work. Child code, dependencies, tests, and local history belong to the child repository.
- Never publish a parent gitlink that points to a child commit which is only local. Remote reachability is a hard gate.
- Commit and push are event-driven, not timer-driven: commit a coherent accepted unit; push it in the same work session when it becomes a recovery point or a dependency of another repository.
- Hooks may reject unsafe operations or print diagnostics. They must not auto-add, auto-commit, auto-push, auto-pull submodules, rewrite history, or delete files.
- Record what was pushed and what remains intentionally ignored.
- In the `alib` workspace, read [alib-submodule-registry.md](references/alib-submodule-registry.md) before changing repository boundaries, then reconcile it against live `.gitmodules`, parent gitlinks, and child remotes.

## Repository Roles

For a large parent + submodule workspace, classify each boundary before acting:

- `parent/orchestrator`: indexes, shared governance, lightweight cross-project docs, `.gitmodules`, and gitlinks;
- `child/owner`: project or tool source, tests, dependency declarations, release history, and child-local docs;
- `local-asset`: ignored PDF/data/generated output kept in the working tree and backed up outside Git;
- `legacy/archive`: old remote or bundle retained for history lookup, never used for routine pushes;
- `recovery-anchor`: remote clone, verified bundle, or external file backup used before destructive governance.

Do not infer ownership only from the physical directory name. A project under `Sources/` or `Assets/` may still be an independent child repository.

## Workspace Inventory

The Skill does not treat a hard-coded commit list as truth. For the `alib` workspace, use three layers:

1. [alib-submodule-registry.md](references/alib-submodule-registry.md): stable path, remote, ownership role, branch policy, and known exception;
2. parent `.gitmodules` plus `160000` tree entries: current declared topology and exact gitlinks;
3. child remote refs: current reachability and branch facts.

The registry currently covers all 18 top-level `alib-main` submodules. OIDs, dirty state, initialized state, and ahead/behind are deliberately discovered live because they change during normal work.

Treat drift as a governance finding:

- live submodule missing from the registry: classify and register it before closing the task;
- registry entry missing from `.gitmodules` or the parent tree: mark stale and repair or retire it;
- path, URL, branch policy, or ownership changed: update the registry in the same parent transaction;
- ordinary child commit/gitlink movement: do not rewrite the registry unless stable metadata changed.

## Standard Workflow

1. Map repository state:
   - current branch and upstream;
   - unstaged, staged, untracked, ignored files;
   - submodule status and nested dirtiness;
   - ahead/behind for parent and changed submodules.
2. Classify files:
   - `track`: source, Skill, workflow, reference, template, Markdown logs, provenance, task docs;
   - `ignore`: `.DS_Store`, caches, `.venv`, `__pycache__`, build artifacts, downloaded binaries, runtime tmp;
   - `submodule-internal`: changes that must be committed inside the submodule first;
   - `needs-decision`: secrets, large data, binary artifacts, generated deliverables, ambiguous exports.
3. Fix ignore rules narrowly:
   - prefer root-scoped ignores such as `/logs/` when only the root runtime folder is noise;
   - do not use broad patterns that hide workflow evidence such as `workflows/**/logs/*.md`;
   - use negative rules only when simpler scoping is not enough.
4. Stage by topic, not by convenience:
   - use explicit pathspecs;
   - verify `git diff --cached --stat`;
   - commit with a message that names the governance action.
5. Handle submodules:
   - inspect inner status with `git -C <submodule> status -sb`;
   - commit and push inner changes first;
   - stage the parent gitlink after the inner commit is reachable remotely;
   - verify `git diff --cached --submodule=log` and `git submodule status --recursive`.
6. Push safely:
   - fetch before deciding whether a branch is ahead/behind; do not hide divergence with a forced pull;
   - push submodules before parent repo;
   - verify the pushed OID with `git ls-remote` or a fresh fetch;
   - refuse routine pushes to a remote classified as `legacy/archive`;
   - verify clean `git status -sb` after push;
   - report branch names and commit hashes.
7. Preserve recovery evidence:
   - before repo splits, history rewrite, GC, or remote replacement, verify a remote/bundle/file-backup anchor;
   - compare the user worktree before and after a high-risk operation;
   - run fresh-clone or isolated UAT before deleting old refs or migration copies.

## Commit And Push Policy

Commit when the change is a coherent, explainable, reversible unit and its minimum relevant checks pass. Good triggers:

- a Task or bug fix reaches an accepted checkpoint;
- a child commit must become the target of a parent gitlink;
- before a risky migration, context switch, long pause, or handoff;
- a governance decision, runbook, or recovery artifact becomes authoritative.

Do not commit every file save, and do not wait for the entire composite workspace to become clean. A large workspace may remain globally dirty while one explicit topic is safely committed.

Push when the commit should become a remote recovery point or be consumed by another repository:

- push an accepted child commit before staging its parent gitlink;
- push an accepted parent commit in the same work session after all referenced child OIDs are remotely reachable;
- push before switching machines or ending work on an important accepted checkpoint;
- keep exploratory/WIP work local or on a dedicated branch until it has a clear recovery meaning.

Never auto-push after every commit. Never batch unrelated child commits and parent docs merely to reduce push count, except when a remote quota or explicit migration plan requires one documented transaction.

For the full parent-child transaction, read [parent-submodule-operations.md](references/parent-submodule-operations.md).

## Branch Policy

- Low-risk personal docs and governance updates may commit directly to the governed default branch when hooks and local checks pass.
- Child code follows the child repository's own branch/PR policy.
- `.gitmodules` rewiring, repo splits, remote replacement, and history rewriting use a dedicated branch or repository-external clone.
- Never merge or rebase an archived old parent history into a newly initialized parent repository with an unrelated root.

## Hook Policy

Recommended minimum:

1. `pre-commit`: block secrets, forbidden binary assets, oversized data, and unexpectedly large files from the staged snapshot.
2. `pre-push` on the parent: block routine pushes to legacy remotes and reject parent gitlinks whose child OIDs are not reachable from configured child remotes.
3. Optional diagnostic-only `post-checkout`/`post-merge`: warn about uninitialized or mismatched submodules; do not update them automatically.

Do not require a commit-message hook for a personal knowledge repository unless commit history has become genuinely hard to search. Server-side branch protection or PR review is more suitable when collaborators join.

Read [hook-policy.md](references/hook-policy.md) before adding or changing hooks.

## Long-Term Maintenance

- Per commit: staged diff, secret/asset/size hook, relevant tests.
- Per parent gitlink update: child commit, child push, remote OID verification, parent pointer commit, parent push.
- Per work session: fetch/ahead-behind check and push accepted recovery points.
- Per `alib` topology change: reconcile `.gitmodules`, parent gitlinks, and `alib-submodule-registry.md`; current OID-only movement is not a topology change.
- Monthly or after abnormal growth: `git count-objects -vH`, parent objects vs `.git/modules`, largest tracked blobs, and remote size review.
- Before structural migration: external backup, isolated clone, fresh-clone UAT, and explicit rollback evidence.
- After migration: retain old remote/bundle/migration copies for a defined period; delete only with separate authorization.

Read [large-repository-maintenance.md](references/large-repository-maintenance.md) for size, backup, GC, history rewrite, and recovery rules.

## When Gitee Is Involved

If the task needs Gitee repository operations beyond normal `git push`, read [mcp-gitee.md](references/mcp-gitee.md). Examples:

- create a new Gitee repo before splitting a submodule;
- list or inspect Gitee repositories;
- create PRs/issues/comments on Gitee;
- use Gitee Enterprise or custom API base URL;
- decide whether to install local `mcp-gitee` or use the remote MCP endpoint.

If `mcp-gitee` tools are not exposed in the current session, say so and use the fallback path in [mcp-gitee.md](references/mcp-gitee.md).

Default repository creation policy:

- When creating a child repository or splitting a directory into a submodule, prefer creating a private repository on Gitee first.
- Use Gitee MCP `create_repo` when available and authenticated.
- Default visibility is private unless the user explicitly asks for public/open-source publication.
- Do not create a GitHub repository for a child/submodule split unless the user asks for GitHub or the existing project governance requires GitHub.
- If namespace, repository name, or visibility cannot be inferred, stop and ask before creating the remote.

## Submodule Split Protocol

Use this when a directory inside a repo should become a separate repository:

1. Confirm the directory should become its own repo and whether history must be preserved.
2. Check for secrets, large files, ignored files, nested Git dirs, and symlinks.
3. Create or identify the remote repository before rewriting local structure. By default, create a private Gitee repository via Gitee MCP when the repository is a child/submodule extracted from the current work.
4. If preserving history, prefer `git filter-repo` or a dedicated clone; if not preserving history, initialize a clean repo from the current directory content.
5. Push the new repo and verify cloneability.
6. Replace the directory in the parent repo with a submodule:
   - `git submodule add <url> <path>` for new paths;
   - for existing paths, remove only from the parent index after the standalone repo is safe.
7. Commit parent `.gitmodules` and gitlink.
8. If this is the `alib` workspace, add or revise its entry in [alib-submodule-registry.md](references/alib-submodule-registry.md) in the same parent transaction.
9. Document how to update the submodule.

After several planned splits, finish all structure changes first and perform at most one parent-history rewrite/GC cycle. Do not rewrite the parent after every child extraction.

## Red Flags

Stop and ask before continuing when:

- a file looks like a secret or credential;
- a large binary or dataset appears newly tracked;
- the cleanup requires force push or history rewriting;
- submodule commits are local-only and remote push fails;
- the parent push would publish a gitlink whose child OID is not present on a configured child remote;
- the selected push remote is a legacy/archive remote;
- old and new parent repositories have unrelated roots and someone proposes merging them;
- Gitee repo creation requires a namespace, visibility, or enterprise target that cannot be inferred;
- there are unrelated user changes in files you would need to edit.

## Reporting

Final reports should include:

- what was committed and pushed;
- what remains ignored and why;
- submodule commits and parent gitlinks if relevant;
- `alib` registry reconciliation when a submodule was added, removed, renamed, or repointed;
- remote-reachability evidence for every published gitlink;
- which hooks ran or were intentionally bypassed;
- backup/bundle/fresh-clone evidence for high-risk operations;
- any operations not performed, especially force push, history rewrite, repo creation, or Gitee MCP setup.
