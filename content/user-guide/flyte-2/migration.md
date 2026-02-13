---
title: Migration
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Migration from Flyte 1 to Flyte 2

{{< note >}}
For a comprehensive reference covering imports, secrets, resources, caching, map tasks, async patterns, and more, see the [Flyte v1 to v2 Migration Guide](/flyte-v1-to-v2-migration-guide.md). It's a single-file cheatsheet designed to give an LLM full context for one-shot migrations — useful but not perfect for complex workflows.
{{< /note >}}

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
