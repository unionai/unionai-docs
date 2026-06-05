---
title: Autoresearch agent
weight: 1
variants: +flyte +union
---

# Autoresearch agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/autoresearch).

This tutorial wraps an autonomous AI research loop in a single Flyte task. The task spins up a GPU container, installs the [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) CLI, clones a research repository, and points Claude Code at a `program.md` brief. The agent runs experiments to improve a model, writes results to disk, and the task then commits the changes and opens a pull request — with a progress plot rendered both in the PR and in the Flyte UI.

It's an example of using Flyte as durable infrastructure for long-running, autonomous agent work:

- **A GPU `TaskEnvironment`** with the API-key and GitHub secrets the agent needs.
- **`report=True`** to stream a progress plot into the Flyte UI.
- **A reconnecting `run.wait()`** loop in the driver so a dropped client connection doesn't lose track of a multi-hour run.

> [!WARNING]
> This example drives a coding agent that executes arbitrary code and pushes commits to a GitHub repository. Run it against a repository you control, and review the constants described below before launching.

## Define the container image

The image is kept in its own `_image.py` module so edits to the agent logic in `run.py` don't invalidate the image cache. Node.js and the Claude Code CLI are installed at run time (see below) to keep the image small.

{{< code file="/unionai-examples/v2/tutorials/autoresearch/_image.py" fragment=image lang=python >}}

## Define the task environment

The task needs a GPU, a generous disk for the cloned repo and model weights, and two secrets: a GitHub token (to clone and push) and an Anthropic API key (for Claude Code).

{{< code file="/unionai-examples/v2/tutorials/autoresearch/run.py" fragment=env lang=python >}}

The agent targets a specific repository, identity, and branch via module-level constants. Update these to point at your own fork before running:

GITHUB_USERNAME = "<YOUR_GITHUB_USERNAME>"
GITHUB_EMAIL = "you@example.com"
AUTORESEARCH_REPO_URL = "https://github.com/<YOUR_ORG>/<YOUR_REPO>.git"
AUTORESEARCH_REPO_FULL_NAME = "<YOUR_ORG>/<YOUR_REPO>"
```

## Model the result

The task returns a typed result describing the pull request it created.

{{< code file="/unionai-examples/v2/tutorials/autoresearch/run.py" fragment=result lang=python >}}

## The autoresearch task

The task is a long, sequential procedure. It starts by installing Node.js and Claude Code at run time, cloning the repo, configuring git, creating a branch, and loading `program.md` as the prompt:

{{< code file="/unionai-examples/v2/tutorials/autoresearch/run.py" fragment=task lang=python >}}

From there the task:

1. Wraps the `program.md` brief with explicit logging and "write outputs to disk" instructions.
2. Disables the Claude Code sandbox (it conflicts with the Flyte pod's container) and runs the CLI non-interactively, streaming its output to the Flyte logs in real time.
3. Collects the files the agent changed via `git status`, commits them, and force-pushes the branch.
4. Opens (or reuses) a pull request with [PyGithub](https://pygithub.readthedocs.io/).
5. If the agent produced a `results.tsv`, renders a progress plot of validation bits-per-byte, attaches it to the PR, and streams it into the Flyte UI:

{{< code file="/unionai-examples/v2/tutorials/autoresearch/run.py" fragment=main lang=python >}}

The entry point submits the task in `remote` mode and reconnects automatically if the client connection drops during the long run.

## Run the agent

### Create secrets

Get an Anthropic API key from the [Anthropic console](https://console.anthropic.com/) and a [GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with permission to push and open PRs on the target repository.

Register both as Flyte secrets. The key names must match those declared in the `TaskEnvironment`:

```
flyte create secret github_token <YOUR_GITHUB_TOKEN>
flyte create secret internal-anthropic-api-key <YOUR_ANTHROPIC_API_KEY>
```

See [Secrets](../../../user-guide/task-configuration/secrets) for scoping and file-based secrets.

### Prepare the research repository

The target repository must contain a `program.md` at its root describing the research task for the agent. Point `AUTORESEARCH_REPO_URL` / `AUTORESEARCH_REPO_FULL_NAME` (and the git identity constants) at a repo you control.

### Run remotely

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/autoresearch):

```
cd v2/tutorials/autoresearch
python run.py
```

This task runs remotely (it needs a GPU and network access). Follow the printed run URL to watch the agent's logs stream in, and open the run's report panel to see the progress plot once results are available. When the task finishes, the returned `AutoResearchResult` contains the pull request URL.
