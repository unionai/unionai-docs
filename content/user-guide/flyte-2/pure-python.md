---
title: Pure Python
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Pure Python

Flyte 2 introduces a new way of writing workflows that is based on pure Python, removing the constraints of a domain-specific language (DSL) and enabling full use of Python's capabilities.

## From `@workflow` DSL to pure Python

| Flyte 1 | Flyte 2 |
| --- | --- |
| `@workflow`-decorated functions are constrained to a subset of Python for defining a static directed acyclic graph (DAG) of tasks. | **No more `@workflow` decorator**: Everything is a `@env.task`, so your top-level “workflow” is simply a task that calls other tasks. |
| `@task`-decorated functions could leverage the full power of Python, but only within individual container executions. | `@env.task`s can call other `@env.task`s and be used to construct workflows with dynamic structures using loops, conditionals, try/except, and any Python construct anywhere. |
| Workflows were compiled into static DAGs at registration time, with tasks as the nodes and the DSL defining the structure. | Workflows are simply tasks that call other tasks. Compile-time safety will be available in the future as `compiled_task`. |

{{< tabs "whats-new-dsl-to-python" >}}
{{< tab "Flyte 1" >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/pure-python/flyte_1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/pure-python/flyte_2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

These fundamental changes bring several transformative benefits:

- **Flexibility**: Harness the complete Python language for workflow definition, including all control flow constructs previously forbidden in workflows.
- **Dynamic workflows**: Create workflows that adapt to runtime conditions, handle variable data structures, and make decisions based on intermediate results.
- **Natural error handling**: Use standard Python `try`/`except` patterns throughout your workflows, making them more robust and easier to debug.
- **Intuitive composability**: Build complex workflows by naturally composing Python functions, following familiar patterns that any Python developer understands.

