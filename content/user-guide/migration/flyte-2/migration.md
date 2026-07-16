---
title: Migration
weight: 3
variants: +flyte +union
---

# Migration from Flyte 1 to Flyte 2

{{< note >}}
For comprehensive migration reference with detailed API mappings, parameter tables, and complete examples, see [Migration from Flyte 1](../../../api-reference/migration/_index) in the Reference section.
An LLM-optimized bundle of the full migration reference is available at [`section.md`](../../../api-reference/migration/section.md).
{{< /note >}}

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

For the full API-level mapping (every import, parameter, and signature change with side-by-side examples), see [Migration from Flyte 1](../../../api-reference/migration/_index) in the Reference section.

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

- **[Tasks and workflows](./tasks-and-workflows)** — the structural shift: `@task`/`@workflow` → `@env.task`, sequential ordering, and nested "subworkflows".
- **[Task configuration](./configuration)** — moving image/resources/cache to the `TaskEnvironment`, secrets, and scheduling with triggers.
- **[Control flow](./control-flow)** — `conditional()` and `@dynamic` become plain Python `if`/loops, and `on_failure` becomes `try`/`except`.
- **[Parallelism and fan-out](./parallelism)** — `map_task` → `flyte.map` / `asyncio.gather`, plus a data-backfill example.
- **[Data types and I/O](./data-io)** — `FlyteFile`/`FlyteDirectory` → `flyte.io.File`/`Dir`, `StructuredDataset` → `flyte.io.DataFrame`, dataclasses, and an ETL example.
- **[ML workloads](./ml-workloads)** — small-model training, hyperparameter optimization, deep learning, batch inference, and an end-to-end pipeline.
- **[New in Flyte 2](./new-in-flyte-2)** — patterns that weren't possible in Flyte 1 at all: real-time model serving, apps, and sandboxed code execution.

Two more pages round out the section: **[Considerations](./considerations)** covers the caveats of the new execution model, and **[Hybrid v1 and v2 pipelines](./hybrid-pipelines)** shows how to call between v1 and v2 during the transition.

## Common gotchas

- **`flyte.map` returns a generator.** Wrap it in `list()` to materialize results, unlike `map_task` which returned a list directly.
- **`memory`, not `mem`.** The `Resources` parameter was renamed, and there are no separate `requests`/`limits`.
- **GPUs use a `"T4:1"` string.** Type and count are combined; the separate `accelerator=` argument is gone.
- **Retries no longer have a platform cap.** In Flyte 1 the control plane capped attempts at 3; in Flyte 2 total attempts equal `retries + 1`. Audit any large `retries` values before deploying.
- **You can only `await` async tasks.** Calling a sync task from an async context uses `.aio()`; see the [Asynchronous model](./async) guide.
- **Keep orchestration lightweight.** A task that calls other tasks acts as a driver pod. Avoid heavy CPU work in it — see [Considerations](./considerations).

For the full list, see [Examples and common gotchas](../../../api-reference/migration/examples-and-gotchas) in the reference.
