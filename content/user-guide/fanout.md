---
title: Fanout
weight: 130
variants: +flyte +serverless +byoc +selfmanaged
---

# Fanout

Flyte is designed to scale effortlessly, allowing you to run workflows with large fan-outs.
When you need to execute many tasks in parallel—such as processing a large dataset or running hyperparameter sweeps—Flyte provides powerful patterns to implement these operations efficiently.

## Understanding fanout patterns

A "fanout" pattern occurs when you spawn multiple tasks concurrently, typically in a loop.
Each task runs in its own container and contributes an output that you later collect.
The most common way to implement this is using the [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) function.

In Flyte terminology, each individual task execution is called an "action"—this represents a specific invocation of a task with particular inputs. When you call a task multiple times in a loop, you create multiple actions.

Here's a basic fanout example:

```python
# fanout.py

import asyncio

import flyte

env = flyte.TaskEnvironment("large_fanout")


@env.task
async def my_task(x: int) -> int:
    return x


@env.task
async def main(r: int):
    results = []
    for i in range(r):
        results.append(my_task(x=i))
    result = await asyncio.gather(*results)

    return result


if __name__ == "__main__":
    flyte.init_from_config("config.yaml")
    run = flyte.run(main, r=50)
    print(run.url)
    run.wait(run)
```

## Fanout execution patterns

### Parallel execution (most common)

The most common fanout pattern is to collect task invocations and execute them in parallel using `asyncio.gather()`:

```python
@env.task
async def parallel_fanout_example(n: int) -> List[str]:
    results = []

    # Collect all task invocations first
    for i in range(n):
        results.append(my_async_task(i))

    # Execute all tasks in parallel
    final_results = await asyncio.gather(*results)

    return final_results
```

### Sequential execution

You can also implement fanout with sequential execution when you need to process tasks one at a time in order:

```python
@env.task
async def sequential_fanout_example(n: int) -> List[str]:
    results = []

    # Execute tasks one at a time in sequence
    for i in range(n):
        result = await my_async_task(i)  # Await each task individually
        results.append(result)

    return results
```

### Mixed patterns

You can combine both parallel and sequential patterns within the same workflow:

```python
@env.task
async def mixed_fanout_example(n: int) -> Tuple[List[str], List[str]]:
    # First: parallel execution
    parallel_tasks = []
    for i in range(n):
        parallel_tasks.append(fast_task(i))
    parallel_results = await asyncio.gather(*parallel_tasks)

    # Second: sequential execution using results from parallel phase
    sequential_results = []
    for result in parallel_results:
        processed = await slow_processing_task(result)
        sequential_results.append(processed)

    return parallel_results, sequential_results
```

## Multi-phase fanout workflows

Complex workflows often involve multiple fanout phases:

```python
@env.task
async def multi_phase_workflow(data_size: int) -> List[int]:
    # First phase: data preprocessing
    preprocessed = []
    for i in range(data_size):
        preprocessed.append(preprocess_task(i))
    phase1_results = await asyncio.gather(*preprocessed)

    # Second phase: main processing
    processed = []
    for result in phase1_results:
        processed.append(process_task(result))
    phase2_results = await asyncio.gather(*processed)

    # Third phase: postprocessing
    postprocessed = []
    for result in phase2_results:
        postprocessed.append(postprocess_task(result))
    final_results = await asyncio.gather(*postprocessed)

    return final_results
```

## Best practices for fanout

1. **Use appropriate parallelism**: Balance between parallelism and resource constraints
   ```python
   # For very large fanouts, consider batching
   batch_size = 100
   for i in range(0, total_items, batch_size):
       batch = items[i:i + batch_size]
       batch_results = []
       for item in batch:
           batch_results.append(process_task(item))
       await asyncio.gather(*batch_results)
   ```

2. **Handle errors gracefully**: Use error handling strategies for large fanouts
   ```python
   # Use return_exceptions=True to handle failures gracefully
   results = await asyncio.gather(*tasks, return_exceptions=True)
   for i, result in enumerate(results):
       if isinstance(result, Exception):
           logger.error(f"Task {i} failed: {result}")
   ```

3. **Consider memory usage**: Large fanouts can consume significant memory
   ```python
   # Process in chunks to manage memory
   chunk_size = 1000
   all_results = []
   for chunk_start in range(0, total_size, chunk_size):
       chunk_tasks = []
       for i in range(chunk_start, min(chunk_start + chunk_size, total_size)):
           chunk_tasks.append(my_task(i))
       chunk_results = await asyncio.gather(*chunk_tasks)
       all_results.extend(chunk_results)
   ```

## When to use fanout

Fanout patterns are particularly valuable for:

- **Large-scale data processing**: Processing datasets with thousands of items
- **Hyperparameter optimization**: Training multiple models with different parameters
- **A/B testing**: Running multiple experimental conditions in parallel
- **Batch inference**: Making predictions on large datasets
- **ETL operations**: Extracting and transforming data from multiple sources
- **Monte Carlo simulations**: Running many independent simulation runs

## Organizing large fanouts

For very large fanouts with hundreds or thousands of parallel tasks, consider using [groups](groups.md) to organize the UI display and make workflows easier to understand and debug.

Fanout is a fundamental pattern in Flyte that enables you to scale your workflows to handle large-scale parallel processing efficiently.
