---
title: Contributing code
weight: 2
variants: +flyte -union
---

# Contributing code

Thank you for your interest in contributing to Flyte 2! This guide walks through
where the code lives, how to set up your development environment, and how to get
your changes reviewed and merged.

> [!NOTE]
> This page covers Flyte 2. If you want to contribute to Flyte 1, switch the
> version selector at the top of the page to **v1**.

## Where the code lives

Flyte 2 is developed across two Apache-2.0 licensed repositories:

| Repo | Purpose | Primary languages |
|------|---------|-------------------|
| [`flyteorg/flyte-sdk`](https://github.com/flyteorg/flyte-sdk) | The Flyte 2 Python SDK: the `flyte` package on [PyPI](https://pypi.org/project/flyte/) for authoring tasks, apps, and plugins | Python (with an optional Rust controller) |
| [`flyteorg/flyte`](https://github.com/flyteorg/flyte) | The Flyte 2 monorepo: backend services, deployment charts, and the shared issue tracker and discussions | Go, Rust, TypeScript |

> [!NOTE]
> The open source backend for Flyte 2 lives in [`flyteorg/flyte`](https://github.com/flyteorg/flyte)
> and is rolling out, so some backend components are still being opened up. To run
> Flyte 2 today you can apply for a [beta preview of the Union backend](https://www.union.ai/beta).
> Most SDK contributions can be developed and tested with a local
> [Flyte Devbox]({{< docs_home flyte v2 >}}/user-guide/get-started/run-modes/running-devbox).

Issues and discussions for **both** repositories are tracked in
[`flyteorg/flyte`](https://github.com/flyteorg/flyte).

## Filing an issue

Before opening a pull request, file an issue (or find an existing one) in the
[`flyteorg/flyte` issue tracker](https://github.com/flyteorg/flyte/issues). This
gives maintainers a chance to discuss the design and avoids duplicated work.

- **Bug reports** and **feature requests**: [open an issue](https://github.com/flyteorg/flyte/issues/new)
  and provide as much context as you can (versions, reproduction steps, expected
  vs. actual behavior).
- **Questions and open-ended ideas**: start a [GitHub Discussion](https://github.com/flyteorg/flyte/discussions)
  or ask in the [`#contribute`](https://flyte-org.slack.com/archives/C04NJPLRWUX)
  channel on [Slack](https://slack.flyte.org/) instead of opening an issue.
- **First-time contributors**: look for issues tagged
  [`good first issue`](https://github.com/flyteorg/flyte/labels/good%20first%20issue).

> [!WARNING] Security issues
> Never report security-related issues, vulnerabilities, or bugs containing
> sensitive information in the public issue tracker. Instead, email
> [security@union.ai](mailto:security@union.ai) or use the *Report a security
> vulnerability* option on the [new-issue page](https://github.com/flyteorg/flyte/issues/new/choose).

## Contributing to the Flyte SDK

The [`flyte-sdk`](https://github.com/flyteorg/flyte-sdk) repository is the most
common starting point for contributors. It uses [`uv`](https://docs.astral.sh/uv/)
for dependency management and a `Makefile` for common tasks.

### Prerequisites

- [`git`](https://git-scm.com/)
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) manages the
  Python toolchain and virtual environment for you
- A running [Docker](https://docs.docker.com/install/) daemon, because the build produces
  a wheel so the default `Image()` picks up your local changes

### Set up your local environment

**1. Fork and clone the repository.**

Fork [`flyteorg/flyte-sdk`](https://github.com/flyteorg/flyte-sdk) to your own
GitHub account, then clone your fork:

``` shell
git clone https://github.com/<your-username>/flyte-sdk.git
cd flyte-sdk

# Add the upstream repo so you can keep your fork in sync
git remote add upstream https://github.com/flyteorg/flyte-sdk.git
```

**2. Install dependencies and build.**

``` shell
uv sync      # Create the virtual environment and install dependencies
make dist    # Build a wheel so the default Image() uses your local changes
```

`uv sync` installs the package in editable mode, so your source edits take effect
immediately. `make dist` requires a running Docker daemon.

### Set up prek pre-commit hooks

The SDK uses [`prek`](https://github.com/j178/prek) (a fast, drop-in
[pre-commit](https://pre-commit.com/) reimplementation) to run formatting, type
checks, and lockfile validation before each commit.

``` shell
# Step 1: Install the prek binary
make prek-install

# Step 2: Install the git hooks into your local clone
prek install
```

Once installed, the hooks run automatically on `git commit`. The configured hooks
each run a `make` target: `fmt`, `mypy`, `ty`, and `uvlock`. To run them across
all files on demand:

``` shell
prek run --all-files
```

### Make your changes

Create a branch off `main` for your work:

``` shell
git checkout -b my-feature-branch
```

As you develop, keep the following in mind. These conventions come from the SDK's
[`CONTRIBUTING.md`](https://github.com/flyteorg/flyte-sdk/blob/main/CONTRIBUTING.md):

- **Keep the core small.** Extensions and extra functionality belong in **plugins**,
  not core, so that module loading stays fast.
- **Respect the module structure.** `flyte.*` is the task-authoring surface,
  `flyte.apps.*` is for apps, and `flyte.io.*` holds the special I/O types.
  Anything under `_internal` (or an underscore-prefixed module) is private.
  Users should never need to import it.
- **Manage the public API** with `__all__` and `__init__.py`, and never expose
  protobuf types to users.
- **Document with examples.** Include code and example snippets in function and
  class docstrings.

Before committing, run the checks and tests locally:

``` shell
make fmt               # Format code with ruff
make mypy              # Type-check with mypy
make ty                # Type-check with ty
make check-docstrings  # Reject reStructuredText and NumPy docstring sections
make unit_test         # Run the unit test suite

# If you changed a plugin, test it too (optionally scope to one plugin):
make unit_test_plugins
# FLYTE_PLUGIN=plugins/bigquery make unit_test_plugins
```

CI runs `fmt`, `mypy`, `ty`, and `check-docstrings` on every pull request, so
running all four locally saves a round trip.

Add unit tests for any new behavior, and make sure the full suite passes before
opening your PR.

### Sign off your commits (DCO)

All commits must be signed off to satisfy the [Developer Certificate of
Origin](https://developercertificate.org/) (DCO) check. Signing off certifies
that you wrote the code (or otherwise have the right to submit it under the
project's license). Use the `-s`/`--signoff` flag:

``` shell
git commit -s -m "Add caching to the local runner"
```

This appends a `Signed-off-by: Your Name <your-email@example.com>` line to the
commit message. The email should match the commit author identity configured in git (your `user.name`/`user.email`).

If you forgot to sign off, amend the most recent commit:

``` shell
git commit --amend -s --no-edit
```

To sign off a series of commits that already exist on your branch, rebase with
the `--signoff` flag:

``` shell
git rebase --signoff upstream/main
```

> [!NOTE]
> Commits created in the GitHub web UI arrive without a sign-off. Accepting a
> review suggestion, committing an edit from the file view, or applying a
> Copilot Autofix all produce an unsigned commit, and the DCO check will fail on
> it. If that commit is not the most recent one, `--amend` cannot reach it: use
> `git rebase --signoff upstream/main` and force-push.

### Commit message guidelines

Clear commit messages help reviewers understand your intent:

- Use the present tense (e.g. "Add retry support", not "Added retry support").
- Keep the summary line to 50 characters or fewer.
- Add extra context in the body when needed.
- Reference related issues (e.g. `Fixes #123`).
- Keep each commit focused on a single logical change.

### Open a pull request

**1. Push your branch to your fork:**

``` shell
git push origin my-feature-branch
```

**2. Open the pull request** against the upstream repository's default branch,
which is `main` in both repositories. On GitHub, choose **Compare across
forks** and select your fork and branch.

**3. Describe the change.** `flyteorg/flyte` provides a PR template; fill it out.
`flyte-sdk` has none, so write a description covering:

- A clear description of what changed and why.
- Links to any related issues (e.g. "Fixes #123").
- Testing steps, screenshots, or output where applicable.
- Notes for reviewers if any part needs special attention.

Keep pull requests focused and reasonably small, so they are easier to review
and merge. Respond to review feedback by pushing additional commits to the same
branch (they'll show up in the PR automatically).

## Contributing with AI agent harnesses

AI coding agents (Claude Code, Cursor, and similar harnesses) are welcome tools
for contributing, but the same quality bar applies to agent-assisted changes as
to any other contribution. When you use an agent to help author a PR:

- **You are responsible for the code.** Read and understand every change before
  submitting. Signing off on a commit (`git commit -s`) certifies *you* stand
  behind it under the DCO. That certification applies regardless of how the code
  was written.
- **Run the checks yourself.** Don't rely on the agent's claims that tests pass.
  Run `make fmt`, `make mypy`, `make ty`, `make check-docstrings`, and
  `make unit_test` locally, and make sure the `prek` hooks succeed before pushing.
- **Keep PRs focused and human-sized.** Avoid submitting large, sprawling,
  machine-generated diffs. Scope each PR to one logical change so reviewers can
  reason about it.
- **Write your own description.** The PR description should reflect your
  understanding of the change and its rationale, not raw agent output.
- **Disclose substantial AI assistance** in the PR description when an agent
  generated a significant portion of the change. This helps reviewers calibrate
  their attention and is a courtesy to maintainers.
- **Don't paste sensitive context.** Never feed secrets, credentials, or private
  data into an agent while working on a contribution.

Low-quality, unreviewed, or untested agent output creates work for maintainers and
may be closed without review.

## Becoming a contributor

As you become more involved, you can grow into committer and maintainer roles.
The [Flyte Contributor Ladder](https://github.com/flyteorg/community/blob/main/GOVERNANCE.md#community-roles-and-path-to-maintainership)
describes the expectations and progression across roles. All participation is
governed by the [Code of Conduct](https://lfprojects.org/policies/code-of-conduct/).

## Resources

- [Slack](https://slack.flyte.org/): chat with the community in
  [`#flyte-support`](https://flyte-org.slack.com/archives/CP2HDHKE1) and
  [`#contribute`](https://flyte-org.slack.com/archives/C04NJPLRWUX)
- [GitHub Discussions](https://github.com/flyteorg/flyte/discussions): ask questions
- [`flyte-sdk` CONTRIBUTING.md](https://github.com/flyteorg/flyte-sdk/blob/main/CONTRIBUTING.md)
- [`flyte` CONTRIBUTING.md](https://github.com/flyteorg/flyte/blob/main/CONTRIBUTING.md)
