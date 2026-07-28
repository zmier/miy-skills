# alib Submodule Registry

Use this reference only for `/Users/narra/Documents/alib` or a clone of `azen/alib-main`. It records stable repository boundaries, not live commit state.

## Authority

```text
stable ownership and exceptions -> this registry
declared path/URL/branch        -> parent .gitmodules
exact pinned commit            -> parent 160000 gitlink
reachability/default branch    -> child remote refs
dirty/ahead/behind             -> live child repository
```

Never rely on the snapshot table alone for a push decision. Reconcile it against the live repository first.

## Parent Repositories

| Role | Remote | Policy |
|---|---|---|
| active parent | `git@gitee.com:azen/alib-main.git` | routine parent commits and gitlink updates |
| legacy archive | `git@gitee.com:azen/alib.git` | read-only history lookup; never routine push |

## Top-Level Registry

Snapshot: 2026-07-28, 19 top-level entries. An omitted `.gitmodules` branch means “follow the child repository's governed default/upstream”; do not guess `main` or `master` from the omission.

| Path | Remote | Role | Branch policy / note |
|---|---|---|---|
| `ALink/Lib/ALMet` | `git@gitee.com:azen/ALMethod.git` | first-party library | path and remote name intentionally differ |
| `ALink/.obsidian/plugins/ALPlugin` | `git@gitee.com:azen/alplugin.git` | first-party plugin | child default/upstream |
| `Writer/.obsidian/plugins/note-merger` | `git@github.com:zmier/note-merger.git` | external/forked plugin | treat child policy as authoritative |
| `Writer/.pytools/paper-bot/src` | `git@github.com:zmier/PyPaperBot.git` | embedded external/forked source | do not absorb into parent |
| `Writer/00 信息/工具/RIME` | `git@gitee.com:azen/mine-rime.git` | first-party config tool | child default/upstream |
| `Writer/00 信息/工具/CLI_config` | `git@gitee.com:azen/cli_config.git` | first-party config tool | child default/upstream |
| `Writer/.obsidian/plugins/advanced-canvas` | `git@github.com:zmier/obsidian-advanced-canvas.git` | external/forked plugin | treat child policy as authoritative |
| `Writer/00 信息/miy-skills` | `git@github.com:zmier/miy-skills.git` | first-party Skill/workflow library | current governed working branch is discovered live |
| `Writer/02 Sources/SMK` | `git@gitee.com:azen/SMK.git` | first-party stock/data engineering project | independent project despite living under Sources; contains the read-only ALTock snapshot migrated under `J-260717`; the legacy ALTock remote is retained for rollback |
| `Writer/03 Projects/260521-投顾研究` | `git@github.com:zmier/PRO-Inv-Adv-marketing.git` | first-party project | child default/upstream |
| `Writer/03 Projects/260521-基金经理研究` | `git@gitee.com:azen/fund-manager-research.git` | first-party research project | `.gitmodules` pins branch `main`; ongoing but currently paused; licensed data and binary assets stay local + miku |
| `Writer/03 Projects/2026-学位/MPA` | `git@gitee.com:azen/mpa.git` | first-party project | child default/upstream |
| `Writer/03 Projects/2026-学位/市场营销` | `git@gitee.com:azen/marketing.git` | first-party project | child default/upstream |
| `Writer/03 Projects/J-260128-重大结项` | `git@gitee.com:azen/j-260128-major-project.git` | first-party project | `.gitmodules` pins branch `main` |
| `Writer/03 Projects/260715-微课` | `git@gitee.com:azen/ai-video-microcourse.git` | first-party active video production project | `.gitmodules` pins branch `main`; code, documents, manifests, and checks stay in Git; source and generated binary assets stay local + miku |
| `Writer/03 Projects/冒险者工会/PROJECT-靶JS系列逆向` | `git@gitee.com:azen/js-reverse-target-series.git` | first-party project | `.gitmodules` pins branch `main`; closed target-JS reverse project; large raw traces and long submission screenshots stay in external local archive |
| `Writer/.pytools/scholar-kit` | `git@gitee.com:azen/scholar-kit.git` | first-party tool | `.gitmodules` pins branch `main` |
| `Writer/99 Assets/Apps/刷题系统` | `git@gitee.com:azen/quiz-bank-system.git` | first-party app | `.gitmodules` pins branch `main`; independent owner despite Assets path |
| `Writer/00 信息/工具/alib-miku-sync` | `git@gitee.com:azen/alib-miku-sync.git` | first-party macOS tool | `.gitmodules` pins branch `main`; generated apps/config stay local + miku |

## Live Reconciliation

From the parent root:

```bash
git config -f .gitmodules --get-regexp '^submodule\..*\.(path|url|branch)$'
git ls-tree -r HEAD
git submodule status --recursive
git submodule foreach --recursive 'git status --short --branch'
```

For each gitlink that may be published:

```bash
git -C "<child-path>" remote -v
git -C "<child-path>" rev-parse HEAD
git -C "<child-path>" branch -r --contains HEAD
git ls-remote "<child-remote>"
```

Count top-level parent gitlinks from the committed tree, not from directory discovery:

```bash
git ls-tree -r HEAD | awk '$1 == "160000" { count += 1 } END { print count + 0 }'
```

Nested submodules belong to their immediate child repository. Discover them with recursive commands, but do not promote them into this top-level registry unless `alib-main` directly owns the gitlink.

## Update Contract

Update this registry when a top-level submodule is added, removed, renamed, changes remote, changes stable branch policy, or changes ownership class. Publish in this order:

```text
child commit/push and OID verification
-> parent .gitmodules/gitlink + registry update
-> parent commit/push
-> isolated clone or targeted submodule UAT
```

Do not add volatile OIDs, dirty counts, local paths inside `.git/modules`, or temporary migration directories to the registry.
