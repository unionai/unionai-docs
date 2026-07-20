---
title: Migration Overview
weight: 1
variants: +flyte +union
---

# Migration Overview

This section walks through the Flyte 1 workload patterns you already know — data ETL, model training, hyperparameter sweeps, batch inference — and their Flyte 2 equivalents. Every pattern is a complete, runnable v1↔v2 example pair in the [`unionai-examples`](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/migration/flyte-2) repository.

Two conceptual shifts motivate almost every change — **pure Python execution** and the **asynchronous model** — after which most migrations come down to a couple of mechanical moves. This page covers both shifts, the terminology mapping, and a quick-reference module.

## Pure Python execution

In Flyte 1, `@workflow` functions were constrained to a DSL subset of Python that compiled to a static DAG. In Flyte 2 there is **no `@workflow` decorator**: everything is a `@env.task`, and a "workflow" is simply a task that calls other tasks. Orchestration runs as real Python at runtime, so loops, conditionals, and `try`/`except` work anywhere.

| Flyte 1 | Flyte 2 |
| --- | --- |
| `@workflow` functions are constrained to a subset of Python defining a static DAG. | **No `@workflow` decorator**: your top-level "workflow" is just a task that calls other tasks. |
| `@task` functions had the full power of Python, but only within a single container execution. | `@env.task`s call other tasks and build dynamic structures with any Python construct, anywhere. |
| Workflows compiled to static DAGs at registration time. | Workflows are tasks calling tasks; compile-time safety is coming via `compiled_task`. |

{{< tabs "whats-new-dsl-to-python" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/flyte-2/pure-python/flyte_1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/flyte-2/pure-python/flyte_2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

This unlocks workflows that adapt to runtime conditions, native `try`/`except` error handling, and the intuitive composition of ordinary Python functions.

## Asynchronous model

Flyte 2 is built on Python's `asyncio`, with a crucial twist: **the Flyte orchestrator acts as the event loop**, scheduling awaited tasks across distributed infrastructure. This makes `async`/`await` the natural way to express parallelism.

| | Flyte 1 | Flyte 2 |
| --- | --- | --- |
| Parallelism | The DSL auto-parallelized independent tasks; the `map` operator ran a task over many inputs. | Python's `asyncio` expresses parallelism, with the Flyte orchestrator acting as the event loop across distributed infrastructure. |

The core async keywords carry Flyte-specific meaning:

- **`async def`** declares a coroutine.
- **`await`** signals where a task can be scheduled in parallel — not just an I/O yield point.
- **`asyncio.gather`** tells the orchestrator that a set of tasks are independent and can be distributed across separate compute resources.

Consider this pattern for parallel data processing:

{{< code file="/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="async" lang="python" >}}

In standard Python this mainly benefits I/O-bound work; in Flyte 2 the orchestrator schedules each `process_chunk` task on its own pod.

### True parallelism for all workloads

Async syntax in Flyte 2 is **not just for I/O-bound operations**. When the orchestrator encounters `await asyncio.gather(...)`, it runs those independent tasks simultaneously across compute resources — achieving true parallelism for CPU-bound work (model training, heavy math), I/O-bound work (queries, API calls), and mixed workloads alike.

### Calling sync tasks from async tasks

You don't need to rewrite existing synchronous code. Flyte automatically "asyncifies" sync functions; just call them from an async context with `.aio()`:

{{< code file="/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="calling-sync-from-async" lang="python" >}}

### The `flyte.map` function: Familiar patterns

For code that used Flyte 1's `map`, `flyte.map` is a direct replacement that works in both sync and async contexts:

{{< tabs "whats-new-map-function" >}}
{{< tab "Sync Map" >}}
{{< code file="/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="sync-map" lang="python" >}}
{{< /tab >}}
{{< tab "Async Map" >}}
{{< code file="/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="async-map" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

It provides dual interfaces (`flyte.map.aio()` and `flyte.map()`), `return_exceptions` for graceful failure handling (a more flexible replacement for Flyte 1's `min_success_ratio`), automatic UI grouping, and optional concurrency limits.

## Terminology and concept mapping

Several Flyte 1 concepts were renamed or reshaped in Flyte 2. The table below maps the ones you'll meet most often.

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

The package is renamed from `flytekit` to `flyte`, and the workflow/dynamic/map_task imports disappear:

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

## The two mechanical changes behind (almost) every migration

Most of a migration comes down to two moves:

### 1. Move task configuration into a `TaskEnvironment`

Instead of configuring the image, resources, and caching on each task decorator, configure them once on a `flyte.TaskEnvironment` and share it across tasks:

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
- **[New in Flyte 2](./new-in-flyte-2)** — patterns that weren't possible in Flyte 1 at all: real-time model serving, batch inference, apps, and sandboxed code execution.
{{< variant union >}}
{{< markdown >}}
- **[Union features](./union-features)** — migrating Union-specific Actors (→ reusable containers) and Apps (→ the Flyte SDK).
{{< /markdown >}}
{{< /variant >}}
- **[Hybrid v1 and v2 pipelines](./hybrid-pipelines)** — calling between v1 and v2 in both directions during the transition.
- **[Gotchas and caveats](./gotchas-and-caveats)** — common gotchas plus the deeper caveats of the new execution model, including non-deterministic behavior and keeping orchestration lightweight.

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
