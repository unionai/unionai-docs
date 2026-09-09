---
title: Quickstart
description: Install the SDK and run your first workflow locally in a few minutes.
icon: '123'
weight: 1
variants: +flyte +union
---

# Quickstart

> [!NOTE] Try it in your browser
> Prefer not to install anything? Follow along with this quickstart in Google Colab.
>
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unionai/unionai-examples/blob/main/v2/user-guide/getting-started/ten_minutes_to_flyte.ipynb)

Let's get you up and running with your first workflow on your local machine.


## What you'll need

- Python 3.10+ in a virtual environment

## Install the SDK

Install the `flyte` package:

```bash
pip install 'flyte[tui]'
```

{{< note >}}
We also install the `tui` extra to enable the terminal user interface.
{{< /note >}}

Verify it worked:

```bash
flyte --version
```

Output:

```bash
Flyte SDK version: 2.*.*
```

{{< note "Run the CLI without installing" >}}
If you have [`uv`](https://docs.astral.sh/uv/) installed, you can run the `flyte` CLI directly with `uvx`, without installing the package into your environment:

```bash
uvx flyte --version
uvx flyte get run
```

{{< /note >}}

## Run something straight away

Before writing anything of your own, you can run a built-in example. It needs no files and no configuration:

```bash
flyte run --local hello
```

Flyte writes the example to a scratch directory, runs it, and prints the path to the source:

```bash
Using the built-in example from /tmp/flyte-hello-<user>/task/hello.py
Copy it into your own project to start editing.
Completed Local Run   Outputs: ActionOutputs(o0=14.0)
```

The example fans a small computation over a list of inputs with `flyte.map` and averages the results. That is enough to see a workflow run. Next, write one of your own.

{{< variant union >}}
{{< markdown >}}

> [!NOTE] Watch it in the console
> Once you have configured an endpoint below, swap `--local` for `--tracked`. The run still executes
> on your machine, but reports its progress to {{< key product_name >}} and appears under
> **Tracked Runs**:
>
> ```bash
> flyte run --tracked hello
> ```
>
> See [Track local runs in the console](./run-modes/running-locally#track-local-runs-in-the-console).

{{< /markdown >}}
{{< /variant >}}

## Configure

Create a config file for local execution. Runs will be persisted locally in a SQLite database.

```bash
flyte create config --local-persistence
```

This creates `.flyte/config.yaml` in your current directory.
{{< variant flyte >}}
{{< markdown >}}
See [Setting up a configuration file](./run-modes/running-devbox#configure) for more options when connecting to a cluster.
{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}
See [Setting up a configuration file](./run-modes/running-remote#configuration-file) for more options.
{{< /markdown >}}
{{< /variant >}}

{{< note >}}
Run `flyte get config` to check which configuration is currently active.
{{< /note >}}

## Write your first workflow

> [!TIP] Author workflows with an AI assistant
> [`flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins) — a
> portable agent harness plugin for Claude Code, Codex, OpenCode, and other
> harnesses — adds skills that scaffold projects and generate tasks, workflows,
> apps, and tests for you, plus MCP servers that ground the agent in the Flyte SDK
> and docs. See [Flyte agent plugins](../../api-reference/agent-plugins) to get started.

This one converts a list of temperature readings and returns the hottest. Create `temperatures.py`:

{{< code file="/unionai-examples/v2/user-guide/getting-started/temperatures.py" lang="python" >}}

Here's what's happening:

- **`TaskEnvironment`** specifies configuration for your tasks (container image, resources, etc.)
- **`@env.task`** turns Python functions into tasks that can run on a cluster
- **`flyte.map`** calls `to_fahrenheit` once per reading, in parallel when running on a cluster
- Both tasks share the same `env`, so they'll have identical configurations

## Run it

Create a project directory and place your files there:

```
.
├── temperatures.py
└── .flyte
    └── config.yaml
```

> [!WARNING]
> Do not run `flyte run` from your home directory. Flyte packages the current directory when running on a cluster, so running from `$HOME` would attempt to bundle your entire home folder. Always work from a dedicated project directory.

Run the workflow, naming the file and the entrypoint task:

```bash
flyte run --local temperatures.py hottest
```

This executes the workflow locally on your machine:

```bash
Completed Local Run
Outputs: ActionOutputs(o0=75.7)
```

## See the results

You can see the run in the TUI by running:

```bash
flyte start tui
```

The TUI will open into the explorer view

![Explorer View](../../_static/images/user-guide/quickstart/explorer-tui.png)

To navigate to the run details, double-click it or press `Enter` to view the run details.

![Run Details View](../../_static/images/user-guide/quickstart/run-tui.png)

## Next steps

Now that you've run your first workflow:

{{< variant flyte >}}
{{< markdown >}}

- [**Core concepts**](./core-concepts/_index): Understand the core concepts of Flyte programming
- [**Run locally**](./run-modes/running-locally): Learn about the TUI, caching, and other features that work locally
- [**Run on the devbox**](./run-modes/running-devbox): Learn about the devbox cluster and how to run workflows on it
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

- [**Core concepts**](./core-concepts/_index): Understand the core concepts of Flyte programming
- [**Run locally**](./run-modes/running-locally): Learn about the TUI, caching, and other features that work locally
- [**Run on the devbox**](./run-modes/running-devbox): Learn about the devbox cluster and how to run workflows on it
- [**Run on a remote cluster**](./run-modes/running-remote): Configure your environment to run on a cluster that is not on your machine
{{< /markdown >}}
{{< /variant >}}
