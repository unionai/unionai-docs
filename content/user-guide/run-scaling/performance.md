---
title: Scale your workflows
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Scale your workflows

Performance optimization in Flyte involves understanding the interplay between task execution overhead, data transfer, and concurrency. This guide helps you identify bottlenecks and choose the right patterns for your workload.

## Understanding performance dimensions

Performance optimization focuses on two key dimensions:

### Latency

**Goal**: Minimize end-to-end execution time for individual workflows.

**Characteristics**:
- Fast individual actions (milliseconds to seconds)
- Total action count typically less than 1,000
- Critical for interactive applications and real-time processing
- Multi-step inference, with reusing model or data in memory (use reusable containers with @alru.cache)

**Recommended approach**:
- Use tasks for orchestration and parallelism
- Use [traces](../task-programming/traces) for fine-grained checkpointing
- Model as much parallelism as needed
- Leverage [reusable containers](../task-configuration/reusable-containers) to eliminate startup overhead

### Throughput

**Goal**: Maximize the number of items processed per unit time.

**Characteristics**:
- Processing large datasets (millions of items)
- High total action count (10k to 50k actions)
- Batch processing, Large scale batch inference and ETL workflows

**Recommended approach**:
- Batch workloads to reduce overhead
- Limit fanout to manage system load
- Use reusable containers with concurrency for maximum utilization
- Balance task granularity with overhead

## Task execution overhead

Understanding task overhead is critical for performance optimization. When you invoke a task, several operations occur:

| Operation | Symbol | Description |
|-----------|--------|-------------|
| **Upload data** | `u` | Time to upload input data to object store |
| **Download data** | `d` | Time to download input data from object store |
| **Enqueue task** | `e` | Time to enqueue task in Queue Service |
| **Create instance** | `t` | Time to create task container instance |

**Total overhead per task**: `2u + 2d + e + t`

This overhead includes:
- Uploading inputs from the parent task (`u`)
- Downloading inputs in the child task (`d`)
- Uploading outputs from the child task (`u`)
- Downloading outputs in the parent task (`d`)
- Enqueuing the task (`e`)
- Creating the container instance (`t`)

### The overhead principle

For efficient execution, task overhead should be much smaller than task runtime:

```
Total overhead (2u + 2d + e + t) << Task runtime
```

If task runtime is comparable to or less than overhead, consider:
1. **Batching**: Combine multiple work items into a single task
2. **Traces**: Use traces instead of tasks for lightweight operations
3. **Reusable containers**: Eliminate container creation overhead (`t`)
4. **Local execution**: Run lightweight operations within the parent task

## System architecture and data flow

To optimize performance, understand how tasks flow through the system:

1. **Control plane to data plane**: Tasks flow from the control plane (Run Service, Queue Service) to the data plane (Executor Service).
2. **Data movement**: Data moves between tasks through object storage. See [Data flow](data-flow) for details.
3. **State replication**: Queue Service reliably replicates state back to Run Service for visualization. The Run Service may be slightly behind actual execution.

For a detailed walkthrough of task execution, see [Life of a run](life-of-a-run).

## Optimization strategies

### 1. Use reusable containers for concurrency

[Reusable containers](../task-configuration/reusable-containers) eliminate the container creation overhead (`t`) and enable concurrent task execution:

```python
import flyte
from datetime import timedelta

# Define reusable environment
env = flyte.TaskEnvironment(
    name="high-throughput",
    reuse_policy=flyte.ReusePolicy(
        replicas=(2, 10),           # Auto-scale from 2 to 10 replicas
        concurrency=5,              # 5 tasks per replica = 50 max concurrent
        scaledown_ttl=timedelta(minutes=10),
        idle_ttl=timedelta(hours=1)
    )
)

@env.task
async def process_item(item: dict) -> dict:
    # Process individual item
    return {"processed": item["id"]}
```

**Benefits**:
- Eliminates container startup overhead (`t ≈ 0`)
- Supports concurrent execution (multiple tasks per container)
- Auto-scales based on demand
- Reuses Python environment and loaded dependencies

**Limitations**:
- Concurrency is limited by CPU and I/O resources in the container
- Memory requirements scale with total working set size
- Best for I/O-bound tasks or async operations

### 2. Batch workloads to reduce overhead

For high-throughput processing, batch multiple items into a single task:

```python
@env.task
async def process_batch(items: list[dict]) -> list[dict]:
    """Process a batch of items in a single task."""
    results = []
    for item in items:
        result = await process_single_item(item)
        results.append(result)
    return results

@env.task
async def process_large_dataset(dataset: list[dict]) -> list[dict]:
    """Process 1M items with batching."""
    batch_size = 1000  # Adjust based on overhead calculation
    batches = [dataset[i:i + batch_size] for i in range(0, len(dataset), batch_size)]

    # Process batches in parallel (1000 tasks instead of 1M)
    results = await asyncio.gather(*[process_batch(batch) for batch in batches])

    # Flatten results
    return [item for batch_result in results for item in batch_result]
```

**Benefits**:
- Reduces total number of tasks (e.g., 1000 tasks instead of 1M)
- Amortizes overhead across multiple items
- Lower load on Queue Service and object storage

**Choosing batch size**:
1. Calculate overhead: `overhead = 2u + 2d + e + t`
2. Target task runtime: `runtime > 10 × overhead` (rule of thumb)
3. Adjust batch size to achieve target runtime
4. Consider memory constraints (larger batches require more memory)

### 3. Use traces for lightweight operations

[Traces](../task-programming/traces) provide fine-grained checkpointing with minimal overhead:

```python
@flyte.trace
async def fetch_data(url: str) -> dict:
    """Traced function for API call."""
    response = await http_client.get(url)
    return response.json()

@flyte.trace
async def transform_data(data: dict) -> dict:
    """Traced function for transformation."""
    return {"transformed": data}

@env.task
async def process_workflow(urls: list[str]) -> list[dict]:
    """Orchestrate using traces instead of tasks."""
    results = []
    for url in urls:
        data = await fetch_data(url)
        transformed = await transform_data(data)
        results.append(transformed)
    return results
```

**Benefits**:
- Only storage overhead (no task orchestration overhead)
- Runs in the same Python process with asyncio parallelism
- Provides checkpointing and resumption
- Visible in execution logs and UI

**Trade-offs**:
- No caching (use tasks for cacheable operations)
- Shares resources with the parent task (CPU, memory)
- Storage writes may still be slow due to object store latency

**When to use traces**:
- API calls and external service interactions
- Deterministic transformations that need checkpointing
- Operations taking more than 1 second (to amortize storage overhead)

### 4. Limit fanout for system stability

The UI and system have limits on the number of actions per run:

- **Current limit**: 50k actions per run
- **Recommendation**: Target <40k actions for best performance
- **Future**: Higher limits will be supported (contact the Union team if needed)

**Example: Control fanout with batching**

```python
@env.task
async def process_million_items(items: list[dict]) -> list[dict]:
    """Process 1M items with controlled fanout."""
    # Target 10k tasks, each processing 100 items
    batch_size = 100
    max_fanout = 10000

    batches = [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

    # Use flyte.map for parallel execution
    results = await flyte.map(process_batch, batches)

    return [item for batch in results for item in batch]
```

### 5. Optimize data transfer

Minimize data transfer overhead by choosing appropriate data types:

**Use reference types for large data**:
```python
from flyte.io import File, Directory, DataFrame

@env.task
async def process_large_file(input_file: File) -> File:
    """Files passed by reference, not copied."""
    # Download only when needed
    local_path = input_file.download()

    # Process file
    result_path = process(local_path)

    # Upload result
    return File.new_remote(result_path)
```

**Use inline types for small data**:
```python
@env.task
async def process_metadata(metadata: dict) -> dict:
    """Small dicts passed inline efficiently."""
    return {"processed": metadata}
```

**Guideline**:
- **< 10 MB**: Use inline types (primitives, small dicts, lists)
- **> 10 MB**: Use reference types (File, Directory, DataFrame)
- **Adjust**: Use `max_inline_io` in `TaskEnvironment` to change the threshold

See [Data flow](data-flow) for details on data types and transport.

### 6. Leverage caching

Enable [caching](../task-configuration/caching) to avoid redundant computation:

```python
@env.task(cache="auto")
async def expensive_computation(input_data: dict) -> dict:
    """Automatically cached based on inputs."""
    # Expensive operation
    return result
```

**Benefits**:
- Skips re-execution for identical inputs
- Reduces overall workflow runtime
- Preserves resources for new computations

**When to use**:
- Deterministic tasks (same inputs → same outputs)
- Expensive computations (model training, large data processing)
- Stable intermediate results

### 7. Parallelize with `flyte.map`

Use [`flyte.map`](../task-programming/fanout) for data-parallel workloads:

```python
@env.task
async def process_item(item: dict) -> dict:
    return {"processed": item}

@env.task
async def parallel_processing(items: list[dict]) -> list[dict]:
    """Process items in parallel using map."""
    results = await flyte.map(process_item, items)
    return results
```

**Benefits**:
- Automatic parallelization
- Dynamic scaling based on available resources
- Built-in error handling and retries

**Best practices**:
- Combine with batching to control fanout
- Use with reusable containers for maximum throughput
- Consider memory and resource limits

## Performance tuning workflow

Follow this workflow to optimize your Flyte workflows:

1. **Profile**: Measure task execution times and identify bottlenecks.
2. **Calculate overhead**: Estimate `2u + 2d + e + t` for your tasks.
3. **Compare**: Check if `task runtime >> overhead`. If not, optimize.
4. **Batch**: Increase batch size to amortize overhead.
5. **Reusable containers**: Enable reusable containers to eliminate `t`.
6. **Traces**: Use traces for lightweight operations within tasks.
7. **Cache**: Enable caching for deterministic, expensive tasks.
8. **Limit fanout**: Keep total actions below 50k (target 10k-20k).
9. **Monitor**: Use the UI to monitor execution and identify issues.
10. **Iterate**: Continuously refine based on performance metrics.

## Real-world example: PyIceberg batch processing

For a comprehensive example of efficient data processing with Flyte, see the [PyIceberg parallel batch aggregation example](https://github.com/unionai/flyte-sdk/blob/main/examples/data_processing/pyiceberg_example.py). This example demonstrates:

- **Zero-copy data passing**: Pass file paths instead of data between tasks
- **Reusable containers with concurrency**: Maximize CPU utilization across workers
- **Parallel file processing**: Use `asyncio.gather()` to process multiple files concurrently
- **Efficient batching**: Distribute parquet files across worker tasks

Key pattern from the example:

```python
# Instead of loading entire table, get file paths
file_paths = [task.file.file_path for task in table.scan().plan_files()]

# Distribute files across partitions (zero-copy!)
partition_files = distribute_files(file_paths, num_partitions)

# Process partitions in parallel
results = await asyncio.gather(*[
    aggregate_partition(files, partition_id)
    for partition_id, files in enumerate(partition_files)
])
```

This approach achieves true parallel file processing without loading the entire dataset into memory.

## Example: Optimizing a data pipeline

### Before optimization

```python
@env.task
async def process_item(item: dict) -> dict:
    # Very fast operation (~100ms)
    return {"processed": item["id"]}

@env.task
async def process_dataset(items: list[dict]) -> list[dict]:
    # Create 1M tasks
    results = await asyncio.gather(*[process_item(item) for item in items])
    return results
```

**Issues**:
- 1M tasks created (exceeds UI limit)
- Task overhead >> task runtime (100ms task, seconds of overhead)
- High load on Queue Service and object storage

### After optimization

```python
# Use reusable containers
env = flyte.TaskEnvironment(
    name="optimized-pipeline",
    reuse_policy=flyte.ReusePolicy(
        replicas=(5, 20),
        concurrency=10,
        scaledown_ttl=timedelta(minutes=10),
        idle_ttl=timedelta(hours=1)
    )
)

@env.task
async def process_batch(items: list[dict]) -> list[dict]:
    # Process batch of items
    return [{"processed": item["id"]} for item in items]

@env.task
async def process_dataset(items: list[dict]) -> list[dict]:
    # Create 1000 tasks (batch size 1000)
    batch_size = 1000
    batches = [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

    results = await flyte.map(process_batch, batches)
    return [item for batch in results for item in batch]
```

**Improvements**:
- 1000 tasks instead of 1M (within limits)
- Batch runtime ~100 seconds (100ms × 1000 items)
- Reusable containers eliminate startup overhead
- Concurrency enables high throughput (200 concurrent tasks max)

## When to contact the Union team

Reach out to the Union team if you:

- Need more than 50k actions per run
- Want to use high-performance metastores (Redis, PostgreSQL) instead of object stores
- Have specific performance requirements or constraints
- Need help profiling and optimizing your workflows
