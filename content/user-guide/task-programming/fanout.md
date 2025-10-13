---
title: Fanout
weight: 160
variants: +flyte +serverless +byoc +selfmanaged
---

# Fanout

Flyte is designed to scale effortlessly, allowing you to run workflows with large fan-outs.
When you need to execute many tasks in parallel—such as processing a large dataset or running hyperparameter sweeps—Flyte provides powerful patterns to implement these operations efficiently.

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
> [!NOTE]
> By default fanouts in Union are limited to a maximum size.
> Adjustment can made to this maximum by consulting with the Union team.
> Full documentation of this aspect of fanout is coming soon.
{{< /markdown >}}
{{< /variant >}}

## Understanding fanout patterns

A "fanout" pattern occurs when you spawn multiple tasks concurrently, typically in a loop.
Each task runs in its own container and contributes an output that you later collect.
The most common way to implement this is using the [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) function.

In Flyte terminology, each individual task execution is called an "action"—this represents a specific invocation of a task with particular inputs. When you call a task multiple times in a loop, you create multiple actions.

Here's a basic fanout example:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="basic" lang="python" >}}

## Fanout execution patterns

### Parallel execution (most common)

The most common fanout pattern is to collect task invocations and execute them in parallel using `asyncio.gather()`:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="parallel" lang="python" >}}

### Sequential execution

You can also implement fanout with sequential execution when you need to process tasks one at a time in order:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="sequential" lang="python" >}}

### Mixed patterns

You can combine both parallel and sequential patterns within the same workflow:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="mixed" lang="python" >}}

## Multi-phase fanout workflows

Complex workflows often involve multiple fanout phases:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="multi-phase" lang="python" >}}

## Best practices for fanout

1. **Use appropriate parallelism**: Balance between parallelism and resource constraint
   {{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="batching" lang="python" >}}

2. **Handle errors gracefully**: Use error handling strategies for large fanouts
    {{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="errors" lang="python" >}}

3. **Consider memory usage**: Large fanouts can consume significant memory
    {{< code file="/external/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="memory" lang="python" >}}

## When to use fanout

Fanout patterns are particularly valuable for:

- **Large-scale data processing**: Processing datasets with thousands of items
- **Hyperparameter optimization**: Training multiple models with different parameters
- **A/B testing**: Running multiple experimental conditions in parallel
- **Batch inference**: Making predictions on large datasets
- **ETL operations**: Extracting and transforming data from multiple sources
- **Monte Carlo simulations**: Running many independent simulation runs

## Organizing large fanouts

For very large fanouts with hundreds or thousands of parallel tasks, consider using [groups](./grouping-actions.md) to organize the UI display and make workflows easier to understand and debug.

Fanout is a fundamental pattern in Flyte that enables you to scale your workflows to handle large-scale parallel processing efficiently.
