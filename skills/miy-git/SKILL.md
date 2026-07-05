---
name: miy-git
description: Git 仓库治理 Skill。用于检查和清理脏工作树、拆分提交、治理 .gitignore、识别应提交/应忽略文件、处理 submodule gitlink 与内部提交、push 前检查远端状态、为 Gitee/GitHub 仓库创建远端仓库或迁移 submodule 设计安全步骤。适用于用户要求“治理 git”“弄干净仓库”“提交 push”“拆 submodule”“创建新仓库”“接入 mcp-gitee/Gitee MCP”“仓库体积治理”“不要漏 add logs”等场景。
---

# Miy Git

Use this Skill to turn messy Git state into a clear, reproducible repository state. Prefer small, explainable commits and never hide uncertainty behind a forced cleanup.

## Core Rules

- Inspect before acting: run `git status --short`, `git status -sb`, `git diff --stat`, `git diff --cached --stat`, and submodule checks before staging.
- Do not use destructive commands such as `git reset --hard`, `git clean -fd`, or `git checkout --` unless the user explicitly asks for that exact operation.
- Separate unrelated work into separate commits. Do not mix workflow edits, vendor/submodule updates, generated caches, and project artifacts in one commit.
- Treat ignored files as a governance surface. Check whether ignored Markdown logs, TASK records, QC reports, or provenance files should be tracked.
- Push submodule commits before pushing the parent repository that points at those commits.
- Record what was pushed and what remains intentionally ignored.

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
   - verify `git submodule status --recursive`.
6. Push safely:
   - push submodules before parent repo;
   - verify clean `git status -sb` after push;
   - report branch names and commit hashes.

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
8. Document how to update the submodule.

## Red Flags

Stop and ask before continuing when:

- a file looks like a secret or credential;
- a large binary or dataset appears newly tracked;
- the cleanup requires force push or history rewriting;
- submodule commits are local-only and remote push fails;
- Gitee repo creation requires a namespace, visibility, or enterprise target that cannot be inferred;
- there are unrelated user changes in files you would need to edit.

## Reporting

Final reports should include:

- what was committed and pushed;
- what remains ignored and why;
- submodule commits and parent gitlinks if relevant;
- any operations not performed, especially force push, history rewrite, repo creation, or Gitee MCP setup.
