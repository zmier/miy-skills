# MCP Gitee Integration

Use this reference when `miy-git` needs Gitee operations that ordinary `git` cannot perform, such as creating repositories, listing authorized repos, opening pull requests, or managing issues.

## Current Knowledge

As of 2026-07-05, `oschina/mcp-gitee` is the public Gitee MCP server implementation.

Source references:

- GitHub: `https://github.com/oschina/mcp-gitee`
- Gitee: `https://gitee.com/oschina/mcp-gitee`

The upstream README states that it can manage Gitee repositories, issues, pull requests, notifications, and supports personal, organization, and enterprise operations. It supports configurable API base URLs and dynamic tool enable/disable.

## Local Availability Check

Before using Gitee MCP, check whether the current session exposes tools:

```text
Use tool discovery for "gitee mcp repository create list tools".
```

If no `mcp__gitee...` namespace or Gitee-related tools appear, the current session cannot call Gitee MCP directly.

Also check local command availability:

```bash
command -v mcp-gitee
go version
```

At the time this Skill was created on this machine, `go` and `mcp-gitee` were not installed.

## Installation Options

### Local stdio server

Requires Go 1.23 or higher.

```bash
go install gitee.com/oschina/mcp-gitee@latest
mcp-gitee --version
```

Configure an MCP host with:

```json
{
  "mcpServers": {
    "gitee": {
      "command": "mcp-gitee",
      "env": {
        "GITEE_API_BASE": "https://gitee.com/api/v5",
        "GITEE_ACCESS_TOKEN": "<your personal access token>"
      }
    }
  }
}
```

### Remote streamable endpoint

The upstream README shows an endpoint:

```text
https://api.gitee.com/mcp
```

Example MCP host configuration:

```json
{
  "mcpServers": {
    "gitee": {
      "url": "https://api.gitee.com/mcp",
      "headers": {
        "Authorization": "Bearer <your personal access token>",
        "X-MCP-Enabled-Tools": "list_user_repos,get_file_content,list_repo_issues"
      }
    }
  }
}
```

Use remote MCP only when the host supports streamable HTTP MCP and the user has provided or configured a Gitee personal access token.

## Secret Handling

- Never print `GITEE_ACCESS_TOKEN`.
- Never commit MCP config files containing tokens.
- Prefer environment variables or host secret storage.
- If a token appears in shell history, logs, diffs, or config, stop and treat it as a secret incident.

## Useful Upstream Tools

The upstream tool list includes:

- `list_user_repos`: list authorized repositories;
- `get_file_content`: read repository file content;
- `create_repo`: create a user, organization, or enterprise repository;
- `fork_repository`: fork a repository;
- `create_release`, `list_releases`: release operations;
- `search_open_source_repositories`: search public repos;
- `search_files_by_content`: search files in a repo;
- `compare_branches_tags`: compare refs;
- `list_repo_pulls`, `create_pull`, `update_pull`, `merge_pull`, `get_pull_detail`, `get_diff_files`, `manage_pull_review`: pull request operations;
- `create_issue`, `update_issue`, `get_repo_issue_detail`, `list_repo_issues`: issue operations;
- `create_comment`, `list_comments`: comments;
- `get_user_info`, `search_users`: user operations;
- `list_user_notifications`: notifications.

Tool names are case-sensitive. Upstream supports restricting tools via:

```text
X-MCP-Enabled-Tools
X-MCP-Disabled-Tools
```

For repository creation, prefer a narrow enabled list such as:

```text
get_user_info,list_user_repos,create_repo
```

## Repository Creation Flow

When splitting a submodule or creating a new remote:

1. Confirm namespace:
   - personal user;
   - organization;
   - enterprise.
2. Confirm repository name, visibility, license, default branch, and whether to initialize with README.
3. Prefer `create_repo` via MCP if available.
4. If MCP is unavailable, use one of:
   - Gitee web UI;
   - Gitee OpenAPI with a token;
   - existing CLI/script already configured by the user.
5. After creation, verify remote:

```bash
git ls-remote <remote-url>
```

6. Push the standalone repository before adding or updating the parent submodule gitlink.

## Fallback Without MCP

If Gitee MCP is unavailable:

- ordinary Git operations still work for existing remotes:

```bash
git remote -v
git ls-remote origin
git push origin <branch>
```

- repo creation requires user action or another authenticated route;
- do not pretend a repository was created unless `git ls-remote` or an API call verifies it;
- document the blocked step and the exact repo settings needed.

## Enterprise / Custom API

Use custom API base only when the user identifies an enterprise Gitee instance:

```text
GITEE_API_BASE=<enterprise-api-base>
```

Do not assume `https://gitee.com/api/v5` for enterprise tasks.
