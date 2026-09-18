# Contributing to the docs repos

Applies to every change in `unionai-docs` and `unionai-docs-infra`.

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
