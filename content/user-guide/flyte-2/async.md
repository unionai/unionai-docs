---
title: Asynchronous model
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Asynchronous model

## Why we need an async model

The shift to an asynchronous model in Flyte 2 is driven by the need for more efficient and flexible workflow execution.

We believe, in particular, that with the rise of the agentic AI pattern, asynchronous programming has become an essential part of AI/ML engineering and data science toolkit.

With Flyte 2, the entire framework is now written with async constructs, allowing for:

- Seamless overlapping of I/O and independent external operations.
- Composing multiple tasks and external tool invocations within the same Python process.
- Native support of streaming operations for data, observability and downstream invocations.

It is also a natural fit for the expression parallelism in workflows.

### Understanding concurrency vs. parallelism

**Concurrency** means running multiple tasks at once. This can be achieved by interleaving execution on a single thread (switching between tasks when one is waiting) or by true **parallelism**—executing tasks truly simultaneously across multiple cores or machines. Parallelism is a form of concurrency, but concurrency doesn't require parallelism.

### Python's async evolution

Python's asynchronous programming capabilities have evolved significantly:

- **The GIL challenge**: Python's Global Interpreter Lock (GIL) traditionally prevented true parallelism for CPU-bound tasks, limiting threading effectiveness to I/O-bound operations.
- **Traditional solutions**:
  - `multiprocessing`: Created separate processes to sidestep the GIL, effective but resource-intensive
  - `threading`: Useful for I/O-bound tasks where the GIL could be released during external operations
- **The async revolution**: The `asyncio` library introduced cooperative multitasking within a single thread, using an event loop to manage multiple tasks efficiently.

### Parallelism in Flyte 1 vs Flyte 2

| | Flyte 1 | Flyte 2 |
| --- | --- | --- |
| Parallelism | The workflow DSL automatically parallelized tasks that weren't dependent on each other. The `map` operator allowed running a task multiple times in parallel with different inputs. | Leverages Python's `asyncio` as the primary mechanism for expressing parallelism, but with a crucial difference: **the Flyte orchestrator acts as the event loop**, managing task execution across distributed infrastructure. |

### Core async concepts

- **`async def`**: Declares a function as a coroutine. When called, it returns a coroutine object managed by the event loop rather than executing immediately.
- **`await`**: Pauses coroutine execution and passes control back to the event loop.
  In standard Python, this enables other tasks to run while waiting for I/O operations.
  In Flyte 2, it signals where tasks can be executed in parallel.
- **`asyncio.gather`**: The primary tool for concurrent execution.
  In standard Python, it schedules multiple awaitable objects to run concurrently within a single event loop.
  In Flyte 2, it signals to the orchestrator that these tasks can be distributed across separate compute resources.

#### A practical example

Consider this pattern for parallel data processing:

{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="async" lang="python" >}}

In standard Python, this would provide concurrency benefits primarily for I/O-bound operations.
In Flyte 2, the orchestrator schedules each `process_chunk` task on separate Kubernetes pods or configured plugins, achieving true parallelism for any type of work.

### True parallelism for all workloads

This is where Flyte 2's approach becomes revolutionary: **async syntax is not just for I/O-bound operations**.
The `async`/`await` syntax becomes a powerful way to declare your workflow's parallel structure for any type of computation.

When Flyte's orchestrator encounters `await asyncio.gather(...)`, it understands that these tasks are independent and can be executed simultaneously across different compute resources.
This means you achieve true parallelism for:

- **CPU-bound computations**: Heavy mathematical operations, model training, data transformations
- **I/O-bound operations**: Database queries, API calls, file operations
- **Mixed workloads**: Any combination of computational and I/O tasks

The Flyte platform handles the complex orchestration while you express parallelism using intuitive `async` syntax.

## Calling sync tasks from async tasks

### Synchronous task support

Since many existing codebases use synchronous functions, Flyte 2 provides synchronous support:

{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="calling-sync-from-async" lang="python" >}}

Under the hood, Flyte automatically "asyncifies" synchronous functions, wrapping them to participate seamlessly in the async execution model.
You don't need to rewrite existing code—just leverage the `.aio()` method when calling sync tasks from async contexts.

### The `flyte.map` function: Familiar patterns

For scenarios that previously used Flyte 1's `map` operation, Flyte 2 provides `flyte.map` as a direct replacement.
The new `flyte.map` can be used either in synchronous or asynchronous contexts, allowing you to express parallelism without changing your existing patterns.

{{< tabs "whats-new-map-function" >}}
{{< tab "Sync Map" >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="sync-map" lang="python" >}}
{{< /tab >}}
{{< tab "Async Map" >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/async/async.py" fragment="async-map" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

The `flyte.map` function provides:

- **Dual interfaces**: `flyte.map.aio()` for async contexts, `flyte.map()` for sync contexts.
- **Built-in error handling**: `return_exceptions` parameter for graceful failure handling. This matches the `asyncio.gather` interface,
  allowing you to decide how to handle errors.
  If you are coming from Flyte 1, it allows you to replace `min_success_ratio` in a more flexible way.
- **Automatic UI grouping**: Creates logical groups for better workflow visualization.
- **Concurrency control**: Optional limits for resource management.
