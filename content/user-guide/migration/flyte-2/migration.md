---
title: Migration
weight: 3
variants: +flyte +union
---

# Migration from Flyte 1 to Flyte 2

This section walks through the Flyte 1 workload patterns you already know — data ETL, model training, hyperparameter sweeps, batch inference — and their Flyte 2 equivalents. Every pattern is a complete, runnable v1↔v2 example pair in the [`unionai-examples`](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/migration/flyte-2) repository.

## Terminology and concept mapping

Several Flyte 1 concepts were renamed or reshaped in Flyte 2. The table below maps the ones you'll meet most often, so you can recognize the Flyte 2 equivalent of a term you already know.

| Flyte 1 | Flyte 2 | Notes |
|---|---|---|
| `flytekit` (package) | `flyte` (package) | The Python SDK was renamed; imports change from `import flytekit` to `import flyte`. |
| `pyflyte` (CLI) | `flyte` (CLI) | The command-line tool was renamed. |
| `@task` / `@workflow` / `@dynamic` | `@env.task` | A single task decorator off a `flyte.TaskEnvironment`. Workflows and dynamic tasks are no longer distinct constructs: everything is a task, and orchestration is plain Python. |
| `map_task()` | `flyte.map()` | Plus `asyncio.gather()` for async fan-out. |
| `conditional()` | native `if` / `elif` / `else` | Branching is now ordinary Python control flow, not a DSL. |
| `ImageSpec` | `flyte.Image` | Container image definition. |
| `current_context()` | `flyte.ctx()` | Runtime context access. |
| `FlyteFile` / `FlyteDirectory` | `flyte.io.File` / `flyte.io.Dir` | Offloaded file and directory references. |
| `StructuredDataset` | `flyte.io.DataFrame` | Offloaded tabular data. |
| `LaunchPlan` | `flyte.Trigger` | Scheduling and parameterized entry points. |
| `CronSchedule` | `flyte.Cron` | Cron-based scheduling, used with a `flyte.Trigger`. |
| Decks (`enable_deck=True`) | Reports (`report=True`) | Custom HTML rendered in the UI during/after a run. See [Reports](../../task-programming/reports). |

## Package imports

The most visible change is the package rename from `flytekit` to `flyte`, along with the disappearance of the workflow/dynamic/map_task imports.

{{< tabs "migration-imports" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
import flytekit
from flytekit import task, workflow, dynamic, map_task
from flytekit import ImageSpec, Resources, Secret
from flytekit import current_context, LaunchPlan, CronSchedule
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import flyte
from flyte import TaskEnvironment, Resources, Secret
from flyte import Image, Trigger, Cron
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

| Flyte 1 import | Flyte 2 equivalent | Notes |
|---|---|---|
| `flytekit.task` | `env.task` | Decorator from a `TaskEnvironment` |
| `flytekit.workflow` | `env.task` | Workflows are now tasks |
| `flytekit.dynamic` | `env.task` | All tasks can be dynamic |
| `flytekit.map_task` | `flyte.map` / `asyncio.gather` | Different API |
| `flytekit.ImageSpec` | `flyte.Image` | Different API |
| `flytekit.Resources` | `flyte.Resources` | Similar API |
| `flytekit.Secret` | `flyte.Secret` | Different access pattern |
| `flytekit.current_context()` | `flyte.ctx()` | Different API |
| `flytekit.LaunchPlan` | `flyte.Trigger` | Different concept |
| `flytekit.CronSchedule` | `flyte.Cron` | Used with a `Trigger` |
| `flytekit.conditional` | native `if`/`else` | No longer needed |

## The two mechanical changes behind (almost) every migration

Most of a migration comes down to two moves:

### 1. Move task configuration into a `TaskEnvironment`

Instead of configuring the image, hardware resources, and caching directly on each task decorator, you configure them once on a `flyte.TaskEnvironment` and share it across tasks:

```python
env = flyte.TaskEnvironment(
    name="training",
    image=flyte.Image.from_debian_base().with_pip_packages("scikit-learn", "pandas"),
    resources=flyte.Resources(cpu="2", memory="4Gi"),
    cache="auto",
)
```

### 2. Replace `@task` / `@workflow` / `@dynamic` with `@env.task`

Every decorated function becomes an `@env.task`. There is no separate workflow or dynamic construct: a "workflow" is simply a task that calls other tasks, and orchestration is plain Python.

{{< note >}}
The `env` in `@env.task` is just the variable you assigned your `TaskEnvironment` to. Name it whatever you like.
{{< /note >}}

## In this section

The migration patterns are grouped by theme. Start with **Tasks and workflows**, then jump to whatever your workload needs:

- **[Tasks and workflows](./tasks-and-workflows)** — the structural shift: `@task`/`@workflow` → `@env.task`, sequential ordering, nested "subworkflows", and the `@task` → `TaskEnvironment` parameter mapping.
- **[Task configuration](./configuration)** — moving image/resources/cache to the `TaskEnvironment`, GPUs, secrets, caching, and scheduling with triggers.
- **[CLI and configuration](./cli-and-configuration)** — `pyflyte` → `flyte` command mapping and config-file changes.
- **[Control flow](./control-flow)** — `conditional()` and `@dynamic` become plain Python `if`/loops, and `on_failure` becomes `try`/`except`.
- **[Parallelism and fan-out](./parallelism)** — `map_task` → `flyte.map` / `asyncio.gather`, plus a data-backfill example.
- **[Data types and I/O](./data-io)** — `FlyteFile`/`FlyteDirectory` → `flyte.io.File`/`Dir`, `StructuredDataset` → `flyte.io.DataFrame`, dataclasses, and an ETL example.
- **[ML workloads](./ml-workloads)** — small-model training, hyperparameter optimization, deep learning, batch inference, and an end-to-end pipeline.
- **[New in Flyte 2](./new-in-flyte-2)** — patterns that weren't possible in Flyte 1 at all: real-time model serving, apps, and sandboxed code execution.

Two more pages round out the section: **[Considerations](./considerations)** covers the caveats of the new execution model, and **[Hybrid v1 and v2 pipelines](./hybrid-pipelines)** shows how to call between v1 and v2 during the transition.

## Common gotchas

- **`flyte.map` returns a generator.** Wrap it in `list()` to materialize results, unlike `map_task` which returned a list directly.
- **`memory`, not `mem`.** The `Resources` parameter was renamed, and there are no separate `requests`/`limits` — a single value serves as both.
- **GPUs use a `"T4:1"` string.** Type and count are combined; the separate `accelerator=` argument is gone.
- **Image, resources, and cache live on the `TaskEnvironment`.** Set them once at the env level instead of repeating them on every task decorator.
- **`current_context()` is gone.** Read secrets from environment variables and use `flyte.ctx()` for runtime context.
- **The `>>` ordering operator is gone.** Sequential (sync) calls and sequential `await`s are naturally ordered.
- **Retries no longer have a platform cap.** In Flyte 1 the control plane capped attempts at 3; in Flyte 2 total attempts equal `retries + 1`. Audit any large `retries` values before deploying.
- **You can only `await` async tasks.** Call a sync task from an async context with `.aio()`; see the [Asynchronous model](./async) guide.
- **Pick an entrypoint task name.** There's no `@workflow`, so the top-level task is just a task (commonly `main`); run it with `flyte run module.py main`.
- **Type annotations are more lenient.** Flyte 2 will pickle untyped I/O rather than rejecting it at registration.
- **Keep orchestration lightweight.** A task that calls other tasks acts as a driver pod. Avoid heavy CPU work in it — see [Considerations](./considerations).

## Quick reference

A minimal Flyte 2 module, end to end:

```python
import asyncio
import flyte

# 1. Define an image
image = (
    flyte.Image.from_debian_base(python_version=(3, 11))
    .with_pip_packages("pandas", "numpy")
)

# 2. Create a TaskEnvironment
env = flyte.TaskEnvironment(
    name="my_env",
    image=image,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)

# 3. Define tasks
@env.task
async def process(x: int) -> int:
    return x * 2

# 4. Define the entrypoint task
@env.task
async def main(items: list[int]) -> list[int]:
    results = await asyncio.gather(*[process(x) for x in items])
    return list(results)

# 5. Run it
if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main, items=[1, 2, 3, 4, 5])
    print(run.url)
    run.wait()
```

```bash
# CLI
flyte run my_module.py main --items '[1,2,3,4,5]'   # remote (default)
flyte run --local my_module.py main --items '[1,2,3,4,5]'
flyte deploy my_module.py my_env
```
