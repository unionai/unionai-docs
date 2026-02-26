---
title: Local development
weight: 4
variants: +flyte +byoc +selfmanaged
sidebar_expanded: true
---

# Local AI Development with Flyte

Flyte gives you a local development toolkit for ML pipelines and AI agents. Cache expensive operations, generate HTML reports, perform lightweight experiment tracking, trace sub-task execution, and serve models, all from `pip install flyte`. No Flyte cluster or Docker needed.

When you're ready to scale, the same code runs on a remote Flyte cluster with GPUs. No rewrites.

![TUI agent run](../../_static/images/user-guide/local/tui_agent_run.png)

---

## Getting started

To run the terminal user interface (TUI) you'll also need an additional Python package installed along with the Flyte SDK.

```bash
pip install "flyte[tui]>=2.0"
```

To enable run persistence so you can browse past runs, set local persistence to true in the Flyte config:

```yaml
# .flyte/config.yaml
local:
  persistence: true
```

That's it. Every feature below works with just these two steps.

---

## `TaskEnvironment`

Even when running locally, every Flyte task must be defined within a [`TaskEnvironment`](../core-concepts/task-environment). This is what enables local features like caching, reporting, and the TUI. Locally, settings like image, compute resources, and secrets are ignored and tasks run in your local Python environment. See [`TaskEnvironment`](../core-concepts/task-environment) for full details.

---

## Running tasks

Use the `flyte run` CLI with the `--local` flag to execute tasks in your local Python environment. Add `--tui` to launch the interactive Terminal UI for real-time monitoring.

```bash
# Basic execution
flyte run --local my_pipeline.py my_task --arg value

# With the interactive TUI
flyte run --local --tui my_pipeline.py my_task --arg value
```

You can also run tasks programmatically with `flyte.run()`. See [Run and deploy tasks](../task-deployment/_index) for details.

Drop `--local` to run on a remote cluster if one is configured:

```bash
flyte run my_pipeline.py my_task --arg value
```

---

## Terminal UI

The TUI is an interactive split-screen dashboard. Task tree on the left, details and logs on the right.

```bash
flyte run --local --tui my_pipeline.py pipeline --epochs 5
```

This is useful for tracking ML training pipelines and AI agents with a lot of tool calls and sub-agents.

![TUI agent run](../../_static/images/user-guide/local/tui_agent_run.png)

What you see:

- **Task tree** with live status: `●` running, `✓` done, `✗` failed
- **Cache indicators**: `$` cache hit, `~` cache enabled but missed
- **Live logs**: `print()` output streams in real time
- **Details panel**: inputs, outputs, timing, report paths
- **Traced sub-tasks**: child nodes for `@flyte.trace` decorated functions

Flyte persists the inputs and outputs of every task run locally, so you can always go back and inspect what a task received and produced. Combined with [reports](../task-programming/reports), which generate HTML summaries of metrics, charts, and results, this gives you a lightweight experiment management system.

**Keyboard shortcuts:**

| Key | Action |
|-----|--------|
| `q` | Quit |
| `d` | Details tab |
| `l` | Logs tab |

### Exploring past runs

You can also launch the TUI on its own to browse past runs, compare inputs and outputs, and review reports:

```bash
flyte start tui
```

### Tracing

Unlike `@env.task`, which defines an independent unit of work that Flyte schedules, caches, and tracks on its own, [`@flyte.trace`](../task-programming/traces) is for functions that run *inside* a task. A traced function must be called from within a task and can't run on its own. It gives you visibility into the internal steps of a task without the overhead of making each step a separate task.

Traced functions show up as child nodes under their parent task in the TUI, each with their own timing, inputs, and outputs.

```python
@flyte.trace
async def search(query: str) -> str:
    """Shows up as a child node under the parent task."""
    return await do_search(query)

@env.task
async def agent(request: str) -> str:
    results = await search(request)    # Traced, visible in TUI
    answer = await summarize(results)   # Also traced if decorated
    return answer
```

This is particularly useful for AI agents where you want to see exactly which tools were called, and for ML pipelines where you want to trace preprocessing or feature engineering steps within a larger task. See [Traces](../task-programming/traces) for full details.

---

## Features that work locally

These Flyte features work the same way locally as they do on a remote cluster. The links below point to their full documentation.

- **[Caching](../task-configuration/caching)**: Add `cache="auto"` to any task and Flyte stores its outputs in a local SQLite database, keyed on task name and inputs. Same inputs means instant results with no recomputation. On a remote cluster, the same setting uses the cluster's distributed cache store.

- **[Reports](../task-programming/reports)**: Add `report=True` to a task and it can generate an HTML report (charts, tables, images) saved alongside the task output. Locally, reports are saved as HTML files and the TUI shows the path. On a cluster, they render in the Flyte UI.

- **[Serving](../serve-and-deploy-apps/_index)**: Flyte's app framework lets you serve tasks as local API endpoints or interactive UIs (FastAPI, Gradio) during development, then deploy the same code to a remote cluster with no changes.

- **[Plugins](../../integrations/_index)**: Flyte's plugin system integrates external tools like Weights & Biases, OpenAI, Spark, Ray, and more. Plugins work identically in local and remote execution.

- **[Secrets](../task-configuration/secrets)**: Locally, Flyte reads secrets from your environment variables or `.env` file. On a cluster, define secrets with `flyte.Secret` and Flyte manages them for you. The same code works in both environments.

---

## Local to remote

The same code runs in both environments. Here's what changes:

| Feature | Local | Remote |
|---------|-------|--------|
| **Run pipeline** | `flyte run --local` | `flyte run` |
| **TUI** | `--tui` flag | Dashboard in Flyte UI |
| **Caching** | `cache="auto"`, local SQLite | `cache="auto"`, cluster cache |
| **Reports** | `report=True`, local HTML file | `report=True`, in Flyte UI |
| **Serving** | `python serve.py` | `flyte deploy serve.py env` |
| **Secrets** | `.env` / environment variables | `flyte create secret` / `flyte.Secret` |
| **Compute** | Your CPU/GPU | `Resources(cpu=2, memory="4Gi", gpu=1)` |

The [`TaskEnvironment`](../core-concepts/task-environment) is the bridge. Locally, image and resources are ignored. On the cluster, Flyte builds containers and allocates compute from the same definition.

---

## Next steps

When you're ready to run on a remote Flyte cluster, see [Local setup](../local-setup) to configure the CLI and SDK to connect to your cluster.
