# AGENTS.md — unionai-docs / unionai-docs-infra

For coding agents other than Claude Code: Codex, Cursor, Copilot, Gemini CLI and others. Claude Code
reads `CLAUDE.md` and `.claude/rules/` instead. This file points you at the same files and tells you
what Claude Code gets from them automatically. Like `CLAUDE.md`, it is shared between `unionai-docs`
and its submodule `unionai-docs-infra`.

## Read first

- `CLAUDE.md`: what the repos are, how they build, variants, shortcodes, API docs and redirects.
- `.claude/rules/contributing.md`: the rules for every change, including signing off commits
  (`git commit -s`; "Check DCO" is a required check), the branch each docs line lives on, and the
  submodule pointers.

## With Docsy, changes on GitHub go through Docsy

If Docsy's MCP server is connected (a server named `docsy`, whose tools include `open_pr`, `merge_pr`
and `whoami`), every change on GitHub to `unionai-docs`, `unionai-docs-infra` or `unionai-examples`
goes through its tools, never `gh` or `git push`. That covers opening, pushing to, commenting on and
merging pull requests, and dispatching a cut. Reading is fine (`git fetch`, `gh pr view`). Do the
work itself locally: read from `origin/<branch>`, edit in a worktree, run the checks, then hand
Docsy the finished files. `contributing.md` has the details and the one exception (`redirects.csv`).

Without Docsy, use git and `gh` as usual, following `contributing.md`.

## Before you edit, read the rule for what you're touching

Claude Code loads these by path. Read them yourself before you edit a matching file. Paths are
relative to `unionai-docs`; in `unionai-docs-infra` the infra files are at the repository root.

| When you edit | Read, in `.claude/rules/` |
| --- | --- |
| Pages under `content/` | `style.md` (in `unionai-docs` `main` only), `authoring.md`, `variants-and-versions.md` |
| `layouts/partials/`, `linkmap/` | `authoring.md` |
| `content/api-reference/`, `api-packages.toml`, `linkmap/`, `include/`, `tools/api_generator/` | `generated-content.md` |
| `redirects.csv`, `ROUTING-ARCHITECTURE.md`, `scripts/build_versions.sh` | `routing-redirects.md` |
| `tools/algolia_indexer/`, `layouts/partials/search.html`, `SITEMAPS-AND-SEARCH.md` | `search-indexes.md` |
| `tools/llms_generator/`, `layouts/_default/single.md` or `list.md` | `llm-surface.md` |
| `versions.toml`, `makefile.inc`, `config.union.toml`, `config.flyte.toml` | `variants-and-versions.md` |

Two rules worth knowing before you start:

- **Never hand-edit `content/api-reference/`.** It is generated from docstrings; see
  `generated-content.md`.
- **Read from `origin`, not the working tree.** These repos move weekly, and a fetched but unmerged
  checkout looks current.

## Before you hand over

Run the checks CI runs that apply to your change: `make check-links`, `make check-subpage-cards`,
`make check-api-names`, and markdownlint-cli2 and cspell on the files you changed.
