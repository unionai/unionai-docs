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

## Terminology and concept mapping

Several Flyte 1 concepts were renamed or reshaped in Flyte 2. The table below maps the ones you'll meet most often, so you can recognize the Flyte 2 equivalent of a term you already know.

| Flyte 1 | Flyte 2 | Notes |
|---|---|---|
| `flytekit` (package) | `flyte` (package) | The Python SDK was renamed; imports change from `import flytekit` to `import flyte`. |
| `pyflyte` (CLI) | `flyte` (CLI) | The command-line tool was renamed. |
| `@task` / `@workflow` / `@dynamic` | `@env.task` | A single task decorator off a `flyte.TaskEnvironment`. Workflows and dynamic tasks are no longer distinct constructs — everything is a task, and orchestration is plain Python. |
| `map_task()` | `flyte.map()` | Plus `asyncio.gather()` for async fan-out. |
| `conditional()` | native `if` / `elif` / `else` | Branching is now ordinary Python control flow, not a DSL. |
| `ImageSpec` | `flyte.Image` | Container image definition. |
| `current_context()` | `flyte.ctx()` | Runtime context access. |
| `LaunchPlan` | `flyte.Trigger` | Scheduling and parameterized entry points. |
| `CronSchedule` | `flyte.Cron` | Cron-based scheduling, used with a `flyte.Trigger`. |
| Decks (`enable_deck=True`) | Reports (`report=True`) | Custom HTML rendered in the UI during/after a run. See [Reports](../../task-programming/reports). |

For the full API-level mapping — every import, parameter, and signature change with side-by-side examples — see [Migration from Flyte 1](../../../api-reference/migration/_index) in the Reference section.

You can migrate from Flyte 1 to Flyte 2 by following the steps below:

### 1. Move task configuration to a `TaskEnvironment` object

Instead of configuring the image, hardware resources, and so forth, directly in the task decorator. You configure it in `TaskEnvironment` object. For example:

```python
env = flyte.TaskEnvironment(name="my_task_env")
```

### 2. Replace workflow decorators

Then, you replace the `@workflow` and `@task` decorators with `@env.task` decorators.

{{< tabs "migration" >}}

{{< tab "Flyte 1" >}}
{{< markdown >}}
Here's a simple hello world example with fanout.

```python
import flytekit

@flytekit.task
def hello_world(name: str) -> str:
    return f"Hello, {name}!"

@flytekit.workflow
def main(names: list[str]) -> list[str]:
    return flytekit.map(hello_world)(names)
```
{{< /markdown >}}
{{< /tab >}}

{{< tab "Flyte 2 Sync" >}}
{{< markdown >}}
Change all the decorators to `@env.task` and swap out `flytekit.map` with `flyte.map`.
Notice that `flyte.map` is a drop-in replacement for Python's built-in `map` function.

```diff
-@flytekit.task
+@env.task
def hello_world(name: str) -> str:
    return f"Hello, {name}!"

-@flytekit.workflow
+@env.task
def main(names: list[str]) -> list[str]:
    return flyte.map(hello_world, names)
```
{{< /markdown >}}

{{< note >}}
Note that the reason our task decorator uses `env` is simply because that is the variable to which we assigned the `TaskEnvironment` above.
{{< /note >}}

{{< /tab >}}
{{< tab "Flyte 2 Async" >}}
{{< markdown >}}
To take advantage of full concurrency (not just parallelism), use Python async
syntax and the `asyncio` standard library to implement fa-out.

```diff
+import asyncio

@env.task
-def hello_world(name: str) -> str:
+async def hello_world(name: str) -> str:
    return f"Hello, {name}!"

@env.task
-def main(names: list[str]) -> list[str]:
+async def main(names: list[str]) -> list[str]:
-    return flyte.map(hello_world, names)
+    return await asyncio.gather(*[hello_world(name) for name in names])
```
{{< /markdown >}}

{{< note >}}
To use Python async syntax, you need to:
- Use `asyncio.gather()` or `flyte.map()` for parallel execution
- Add `async`/`await` keywords where you want parallelism
- Keep existing sync task functions unchanged

Learn more about about the benefits of async in the [Asynchronous Model](./async) guide.
{{< /note >}}

{{< /tab >}}
{{< /tabs >}}
