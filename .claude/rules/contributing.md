# Contributing to the docs repos

Applies to every change in `unionai-docs` and `unionai-docs-infra`.

## With the Docsy plugin, changes on GitHub go through Docsy

If the Docsy plugin is installed (its tools are named `mcp__plugin_docsy_docsy__*`), every change on
GitHub to `unionai-docs`, `unionai-docs-infra` or `unionai-examples` goes through Docsy's tools, never
`gh` or `git push`. That covers opening a PR (`open_pr`), pushing to one (`push_files`, `edit_pr`),
commenting, marking ready, merging (`merge_pr`) and dispatching a cut (`run_workflow`). Docsy acts
with its own GitHub App, signs off its commits, and logs on the PR who directed each action. The
plugin's guard redirects the `gh` and `git push` forms to these tools.

The rest of the work stays local. Read from `origin/<branch>`, edit in a worktree branched off it
(`git worktree add -b <you>/<topic> ../unionai-docs-<topic> origin/main`), and run the checks
there (`make check-links`, markdownlint, cspell). Then hand Docsy the finished files.

Docsy can't edit a file over 1 MB in place, and `redirects.csv` in `unionai-docs-infra` is one.
Ask the person before using `gh` for it.

Without the plugin, use git and `gh` as usual, following the rules below.

## Sign off every commit

`git commit -s`. **"Check DCO" is a required status check on protected `main`** — a commit
without a `Signed-off-by` trailer cannot merge. Repairing after the fact means
`git rebase --signoff <base>` and a force-push, so sign off the first time.

## Target the right branch

`main` carries v2, `v1` carries v1. `block-v1-to-main` exists to catch a v1 PR retargeted at the
wrong line. Never commit directly to either; branch first.

## A local checkout is not evidence until you fetch

These repos move weekly and clones drift silently. Read from `origin/<branch>` —
`git show origin/main:path`, `git grep pat origin/main -- path` — not the working tree. Fetching
alone does not move `HEAD`, so a fetched-but-unmerged checkout looks exactly like a current one.

## Do not sweep the submodule pointers into a commit

`unionai-docs` pins `unionai-docs-infra` and `unionai-examples` by commit. A modified pointer in
`git status` is usually incidental. Stage files explicitly; bumping a pointer is a deliberate act
(it is the promotion gate that ships infra to production), never a side effect.
