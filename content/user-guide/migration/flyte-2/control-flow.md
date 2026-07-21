---
title: Control flow
weight: 7
variants: +flyte +union
---

# Control flow

Flyte 1 expressed branching, dynamic fan-out, and failure handling through DSL constructs (`conditional()`, `@dynamic`, `@workflow(on_failure=...)`). In Flyte 2 these are all ordinary Python, because orchestration runs as real Python at runtime. See [Migration](./overview) for the overall approach.

## Conditional execution

The `conditional()` DSL becomes ordinary Python `if` / `elif` / `else` — for example, choosing a model based on dataset size.

{{< tabs "migration-conditional" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/conditional_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/conditional_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Dynamic workflows

`@dynamic` existed so a task could generate a variable number of subtask calls at runtime (e.g. one per data partition discovered at runtime). In Flyte 2 every task can do this natively, so `@dynamic` simply disappears — loop over runtime data in an ordinary `@env.task`.

{{< tabs "migration-dynamic" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/dynamic_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/dynamic_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Error handling

Flyte 1's `@workflow(on_failure=...)` handler becomes ordinary Python `try` / `except` — catch a failed training run, run cleanup, and recover or re-raise.

{{< tabs "migration-error-handling" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/error_handling_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/error_handling_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

Flyte 2 also exposes typed errors, so you can catch a specific failure and retry with more resources — a common need for memory-hungry training jobs:

```python
try:
    return await train_fold(sample_size)
except flyte.errors.OOMError:
    # Retry the same task with a larger memory request.
    return await train_fold.override(
        resources=flyte.Resources(memory="16Gi")
    )(sample_size)
```

See [Error handling](../../task-programming/error-handling) for more.

## Next

- [Parallelism and fan-out](./parallelism) — running many tasks in parallel
- [ML workloads](./ml-workloads) — training, HPO, and inference
