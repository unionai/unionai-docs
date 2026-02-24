---
title: Local development
weight: 4
variants: +flyte
sidebar_expanded: true
---

# Local AI Development with Flyte

Flyte gives you a local development toolkit for ML pipelines and AI agents. Cache expensive operations, generate HTML reports, perform lightweight experiment tracking, trace sub-task execution, and serve models — all from `pip install flyte`. No Flyte cluster or Docker needed.

When you're ready to scale, the same code runs on a remote Flyte cluster with GPUs. No rewrites.

[image placeholder: graphic showing local terminal TUI]

---

## Getting Started

To run the terminal user interface (TUI) you'll also need an additional Python package installed along with the Flyte SDK.

```bash
pip install 'flyte>=2.0[tui]'
```

To enable run persistence so you can browse past runs, set local persistence to true in the Flyte config:

```yaml
# .flyte/config.yaml
local:
  persistence: true
```

That's it. Every feature below works with just these two steps.

---

## Features at a Glance

| Feature | What You Get | Key API |
|---------|-------------|---------|
| [TUI](#terminal-ui) | Live terminal dashboard with task tree, logs, and details | `--tui` flag |
| [Tracing](#tracing) | Sub-task visibility in the TUI | `@flyte.trace` |
| [Experiment tracking](#lightweight-experiment-tracking) | Browse and compare past runs | `flyte start tui` |
| [Caching](#caching) | Skip recomputation on repeated inputs | `cache="auto"` |
| [Reports](#reports) | HTML and markdown dashboards generated from tasks | `report=True` |
| [Serving](#serving) | Run tasks as local API endpoints or apps | `flyte.with_servecontext()` |
| [Plugins](#plugins) | Integrate external tools like Weights & Biases | `@wandb_init` |
| [Secrets](#managing-secrets-locally) | Managing API keys locally and remotely | `flyte.Secret` |

---

## TaskEnvironment

Every Flyte task runs inside a [`TaskEnvironment`](../core-concepts/task-environment) that defines its image, compute resources, and secrets. Locally, the image, resources, and secrets are ignored — tasks run in your local Python environment. On a cluster, Flyte builds the container and schedules the work.

This makes it easy to switch between local development and remote runs.

```python
import flyte

image = flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
    "torch", "torchvision", "matplotlib",
)

env = flyte.TaskEnvironment(
    name="ml_pipeline",
    image=image,
    resources=flyte.Resources(cpu=2, memory="4Gi", gpu=1),
    secrets=flyte.Secret(key="my_api_key", as_env_var="API_KEY"),
)

@env.task
async def my_task(x: int) -> int:
    return x * 2
```

Write your environment config once and it works everywhere — your laptop, CI, and production cluster.

---

## Running tasks

Run any task locally from the command line:

```bash
# Basic execution
flyte run --local my_pipeline.py my_task --arg value

# With the interactive TUI
flyte run --local --tui my_pipeline.py my_task --arg value
```

Drop `--local` to run on a remote cluster:

```bash
flyte run my_pipeline.py my_task --arg value
```

---

## Terminal UI

The TUI is an interactive split-screen dashboard. Task tree on the left, details and logs on the right.

```bash
flyte run --local --tui my_pipeline.py pipeline --epochs 5
```

[image placeholder: TUI screenshot showing task tree with load_data (cached), train (running), evaluate (pending) on left; live training logs on right]

This is useful for tracking ML training pipelines and AI agents with a lot of tool calls and sub-agents.

[image placeholder: Agent TUI run]

What you see:

- **Task tree** with live status: `●` running, `✓` done, `✗` failed
- **Cache indicators**: `$` cache hit, `~` cache enabled but missed
- **Live logs**: `print()` output streams in real time
- **Details panel**: inputs, outputs, timing, report paths
- **Traced sub-tasks**: child nodes for `@flyte.trace` decorated functions

**Keyboard shortcuts:**

| Key | Action |
|-----|--------|
| `q` | Quit |
| `d` | Details tab |
| `l` | Logs tab |

### Tracing

[`@flyte.trace`](../task-programming/traces) gives sub-task visibility. Traced functions show up as child nodes in the TUI with their own timing, inputs, and outputs.

```python
@flyte.trace
async def search(query: str) -> str:
    """Shows up as a child node under the parent task."""
    return await do_search(query)

@env.task
async def agent(request: str) -> str:
    results = await search(request)    # Traced — visible in TUI
    answer = await summarize(results)   # Also traced if decorated
    return answer
```

[image placeholder: TUI screenshot showing agent task with search and summarize as indented child nodes, each with their own timing]

For agents, trace your tool functions to see exactly which tools were called. For ML, trace preprocessing steps or feature engineering.

---

## Caching

`cache="auto"` stores task outputs in local SQLite, keyed on task name + inputs. Same inputs = instant results, no recomputation.

Commonly used to skip rerunning tasks, such as downloading and pre-processing data.

It's also useful for developing longer agentic runs where you want to iterate further down the tree without re-running earlier agent tasks.

```python
@env.task(cache="auto")
async def load_data(data_dir: str = "./data") -> str:
    """Downloads once, then returns instantly on subsequent runs."""
    # ... expensive download ...
    return data_dir
```

```bash
# First run — downloads data, trains model
flyte run --local --tui my_pipeline.py pipeline --epochs 5

# Second run — load_data cached ($), only training re-runs
flyte run --local --tui my_pipeline.py pipeline --epochs 10
```

[image placeholder: TUI screenshot showing load_data with $ cache indicator, train running]

On a remote cluster, the same `cache="auto"` uses the cluster's distributed cache store — no code changes.

---

## Reports

`report=True` lets any task generate an HTML file — charts, tables, images — saved alongside the output. See [Reports](../task-programming/reports) for the full API.

This is useful for experiment tracking and creating easy-to-read documents.

```python
import flyte.report

@env.task(report=True)
async def evaluate(model_file: File, test_data: str) -> str:
    # ... run evaluation ...

    await flyte.report.replace.aio(
        f"<h2>Training Report</h2>"
        f"<h3>Training Curves</h3>{charts_html}"
        f"<h3>Test Results</h3>"
        f"<p>Accuracy: {accuracy:.4f}</p>"
    )
    await flyte.report.flush.aio()

    return f"Accuracy: {accuracy:.4f}"
```

[image placeholder: browser showing rendered HTML report with training loss/accuracy curves and hyperparameter table]

Locally, reports are saved as HTML files — the TUI shows the path. On a cluster, they render in the Flyte UI.

---

## Lightweight experiment tracking

Every local run is persisted (inputs, outputs, duration, status) in SQLite. Browse and compare past runs in the TUI:

```bash
# Run experiments with different hyperparameters
flyte run --local my_pipeline.py pipeline --epochs 5 --lr 0.001
flyte run --local my_pipeline.py pipeline --epochs 10 --lr 0.001
flyte run --local my_pipeline.py pipeline --epochs 5 --lr 0.01

# Browse all runs
flyte start tui
```

[image placeholder: TUI explore mode showing a table of past runs with columns for task name, status, start time, duration, and inputs]

| Key | Action |
|-----|--------|
| `Enter` | View run details |
| `s` | Cycle sort order |
| `r` | Refresh |
| `d` | Delete run |

---

## Serving

Serve tasks as local API endpoints or Gradio apps using Flyte's app framework. See [Serve and deploy apps](../serve-and-deploy-apps) for more details.

### FastAPI (model serving)

```python
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI(title="My Model")

serving_env = FastAPIAppEnvironment(
    name="my-model",
    app=app,
    image=image,
    resources=flyte.Resources(cpu=1, memory="4Gi"),
)

@app.get("/predict")
async def predict(input: str) -> dict:
    return {"result": app.state.model.predict(input)}

if __name__ == "__main__":
    # Serve locally
    local_app = flyte.with_servecontext(mode="local").serve(serving_env)
    local_app.activate(wait=True)
```

```bash
# Local
python serve_model.py

# Remote
flyte deploy serve_model.py serving_env
```

### Gradio (agent UI)

```python
import flyte.app

serving_env = flyte.app.AppEnvironment(
    name="my-agent-ui",
    image=image,
    port=7860,
)

@serving_env.server
def app_server():
    create_demo().launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    create_demo().launch()
```

```bash
# Local
python agent_app.py

# Remote
flyte deploy agent_app.py serving_env
```

### Kicking off tasks from apps

Apps can trigger Flyte tasks and stream results back to the UI:

```python
def run_query(request: str):
    result = flyte.with_runcontext(mode=RUN_MODE).run(agent, request=request)
    result.wait()
    return result.outputs()[0]
```

This enables three development modes:

1. **Fully local** — `RUN_MODE=local python app.py`
2. **Local app, remote task** — `python app.py` (default)
3. **Full remote** — `flyte deploy app.py serving_env`

---

## Plugins

Flyte's plugin system integrates external tools. Plugins add decorators and context functions that work in both local and remote execution.

### Weights & Biases

The `flyteplugins-wandb` package adds W&B experiment tracking with a single decorator:

```python
from flyteplugins.wandb import wandb_init, get_wandb_run

@wandb_init(project="my-project")
@env.task
async def train(epochs: int = 5) -> str:
    run = get_wandb_run()
    for epoch in range(epochs):
        # ... training ...
        if run:
            run.log({"loss": epoch_loss, "acc": epoch_acc})
    return "done"
```

Key features:

- `@wandb_init` on the parent task creates a W&B run
- Child tasks with `@wandb_init` automatically share the parent's run
- `get_wandb_run()` returns the active run for logging
- `flyte.Secret(key="wandb_api_key", as_env_var="WANDB_API_KEY")` for authentication

```bash
# Local
WANDB_API_KEY=your-key flyte run --local --tui wandb_pipeline.py pipeline

# Remote
flyte create secret wandb_api_key <your-key>
flyte run wandb_pipeline.py pipeline
```

---

## Managing secrets locally

Flyte doesn't manage your local secrets. Use environment variables or a `.env` file for local development.

**Locally:** use `.env` files or environment variables.

```bash
# .env
OPENAI_API_KEY=sk-...
WANDB_API_KEY=...
```

**On the cluster:** create secrets and reference them in your task environments.

```bash
flyte create secret MY_API_KEY <value>
```

```python
env = flyte.TaskEnvironment(
    name="my_env",
    secrets=flyte.Secret(key="MY_API_KEY", as_env_var="API_KEY"),
)
```

The `flyte.Secret` declaration is used for remote deployment. Locally, the SDK reads from your environment.

---

## Local to remote

The same code runs in both environments. Here's what changes:

| Feature | Local | Remote |
|---------|-------|--------|
| **Run pipeline** | `flyte run --local` | `flyte run` |
| **TUI** | `--tui` flag | Dashboard in Flyte UI |
| **Caching** | `cache="auto"` — local SQLite | `cache="auto"` — cluster cache |
| **Reports** | `report=True` — local HTML file | `report=True` — in Flyte UI |
| **Serving** | `python serve.py` | `flyte deploy serve.py env` |
| **Model loading in app2** | Falls back to local file | `RunOutput` resolves from pipeline |
| **Secrets** | `.env` / environment variables | `flyte create secret` / `flyte.Secret` |
| **W&B plugin** | `@wandb_init` + env var | `@wandb_init` + `flyte.Secret` |
| **Compute** | Your CPU/GPU | `Resources(cpu=2, memory="4Gi", gpu=1)` |

The [`TaskEnvironment`](../core-concepts/task-environment) is the bridge. Locally, image and resources are ignored. On the cluster, Flyte builds containers and allocates compute from the same definition.

[image placeholder: diagram showing TaskEnvironment definition in the center, with arrows to "Local: runs in your Python env" on left and "Remote: builds container, allocates GPU" on right]

---

## Next steps

For full end-to-end walkthroughs with complete code examples:

| Guide | What you'll build |
|-------|-------------------|
| [ML pipeline development](ml-pipelines) | Train ResNet18 on MNIST with caching, reports, TUI, model serving, and W&B tracking |
| [Agent development](agents) | Build a LangGraph research agent with tool tracing, Gradio UI, and three deployment modes |