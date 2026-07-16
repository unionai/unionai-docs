---
title: Tasks and workflows
weight: 4
variants: +flyte +union
---

# Tasks and workflows

The biggest structural change in Flyte 2 is that **everything is a task**. The `@task`, `@workflow`, and `@dynamic` decorators all collapse into a single `@env.task` off a `flyte.TaskEnvironment`, and a "workflow" is just a task that calls other tasks. This page covers the basic structure; see [Task configuration](./configuration) for the environment settings and [Migration](./migration) for the big picture.

## Hello world: tasks and workflows

A `@task` plus `@workflow` becomes two `@env.task`s, where the entrypoint task calls the others. Sequential calls are naturally ordered — no `>>` operator required.

{{< tabs "migration-hello-world" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/hello_world_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/hello_world_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Chaining and ordering

In Flyte 1 you sometimes used `>>` to force ordering between tasks with no data dependency. In Flyte 2, sequential (synchronous) calls run in the order they're written, and `await`ing async tasks in sequence does the same. The `>>` operator is gone.

{{< tabs "migration-chained" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/chained_tasks_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/chained_tasks_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Subworkflows

A `@workflow` invoked by another `@workflow` (for example, a reusable preprocessing pipeline) becomes a task that calls other tasks — nest them as deeply as you like.

{{< tabs "migration-subworkflow" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/subworkflow_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/subworkflow_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

For the complete `@task` → `TaskEnvironment` + `@env.task` parameter mapping, see [Tasks and workflows](../../../api-reference/migration/tasks-and-workflows) in the reference.

## Next

- [Task configuration](./configuration) — image, resources, caching, secrets, and scheduling
- [Control flow](./control-flow) — conditionals, dynamic behavior, and error handling
- [Parallelism and fan-out](./parallelism) — running tasks in parallel
