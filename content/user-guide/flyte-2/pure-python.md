---
title: Pure Python
weight: 10
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
{{< markdown >}}
```python
import flytekit

image = flytekit.ImageSpec(
    name="hello-world-image",
    packages=[...],
)

@flytekit.task(container_image=image)
def mean(data: list[float]) -> float:
    return sum(list) / len(list)

@flytekit.workflow
def main(data: list[float]) -> float:
    output = mean(data)

    # ❌ performing trivial operations in a workflow is not allowed
    # output = output / 100

    # ❌ if/else is not allowed
    # if output < 0:
    #     raise ValueError("Output cannot be negative")

    return output
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}

```python
import flyte

env = flyte.TaskEnvironment(
    "hello_world",
    image=flyte.Image.from_debian_base().with_pip_packages(...),
)

@env.task
def mean(data: list[float]) -> float:
    return sum(list) / len(list)

@env.task
def main(data: list[float]) -> float:
    output = mean(data)

    # ✅ performing trivial operations in a workflow is allowed
    output = output / 100

    # ✅ if/else is allowed
    if output < 0:
        raise ValueError("Output cannot be negative")

    return output
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

These fundamental changes bring several transformative benefits:

- **Flexibility**: Harness the complete Python language for workflow definition, including all control flow constructs previously forbidden in workflows.
- **Dynamic workflows**: Create workflows that adapt to runtime conditions, handle variable data structures, and make decisions based on intermediate results.
- **Natural error handling**: Use standard Python `try`/`except` patterns throughout your workflows, making them more robust and easier to debug.
- **Intuitive composability**: Build complex workflows by naturally composing Python functions, following familiar patterns that any Python developer understands.

## Workflows can still be static when needed

> [!NOTE]
> This feature is coming soon.

The flexibility of dynamic workflows is absolutely needed for many use cases, but there are other scenarios where static workflows are beneficial. For these cases, Flyte 2 will offer compilation of the top-level task of a workflow into a static DAG.

This upcoming feature will provide:

- **Static analysis**: Enable workflow visualization and validation before execution
- **Predictable resources**: Allow precise resource planning and scheduling optimization
- **Traditional tooling**: Support existing DAG-based analysis and monitoring tools
- **Hybrid approach**: Choose between dynamic and static execution based on workflow characteristics

The static compilation system will naturally have limitations compared to fully dynamic workflows:

- **Dynamic fanouts**: Constructs that require runtime data to reify, for example, loops with an iteration-size that depends on intermediate results, will not be compilable.
  - However, constructs whose size and scope *can* be determined at registration time, such as fixed-size loops or maps, *will* be compilable.
- **Conditional branching**: Decision trees whose size and structure depend on intermediate results will not be compilable.
  - However, conditionals with fixed branch size will be compilable.

For the applications that require a predefined workflow graph, Flyte 2 will enable compilability up to the limits implicit in directed acyclic graphs.

