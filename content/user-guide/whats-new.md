---
title: What's new?
weight: 13
variants: +flyte +serverless +byoc +selfmanaged
---

# What's new?

Flyte 2 represents a fundamental shift in how workflows are written and executed.
The most significant change is the move from a constrained domain-specific language to pure Python, combined with the wholehearted adoption of asynchronous programming for expressing parallelism.
This transformation makes Flyte workflows more intuitive, flexible, and powerful than ever before.

## The evolution: From DSL to pure Python

### Flyte 1: The constraints of static workflows

In Flyte 1, there was a clear distinction between workflows and tasks:

- **Workflows** used the `@workflow` decorator and were constrained to a subset of Python syntax —-essentially a domain-specific language (DSL) that defined a static directed acyclic graph (DAG) of tasks.
- **Tasks** used the `@task` decorator and could leverage the full power of Python, but only within individual container executions.

This separation meant that while both appeared to be Python code, only tasks could use loops, conditionals, error handling, and other standard Python features.
Workflows were compiled into static DAGs at registration time, with tasks as the nodes and the DSL defining the structure.

### Flyte 2: True Python freedom

Flyte 2 eliminates this distinction:

- **No more `@workflow` decorator**: Everything is a `@task`.
- **Pure Python everywhere**: Your top-level "workflow" is simply a task that calls other tasks.
- **Dynamic execution**: Workflows are constructed at runtime based on your Python code.
- **Full language support**: Use loops, conditionals, try/except, and any Python construct anywhere.

This change brings several transformative benefits:

- **Flexibility**: Harness the complete Python language for workflow definition, including all control flow constructs previously forbidden in workflows.
- **Dynamic workflows**: Create workflows that adapt to runtime conditions, handle variable data structures, and make decisions based on intermediate results.
- **Natural error handling**: Use standard Python `try`/`except` patterns throughout your workflows, making them more robust and easier to debug.
- **Intuitive composability**: Build complex workflows by naturally composing Python functions, following familiar patterns that any Python developer understands.

## The new parallelism model: Async at the core

### Understanding concurrency vs. parallelism

Before diving into Flyte 2's approach, it's essential to understand the distinction between concurrency and parallelism:

- **Concurrency**: Dealing with multiple tasks at once through interleaved execution, even on a single thread.
  Performance benefits come from allowing the system to switch between tasks when one is waiting for external operations.
- **Parallelism**: Executing multiple tasks truly simultaneously across multiple cores or machines.
  This is a subset of concurrency where tasks run at the same time rather than being interleaved.

### Python's async evolution

Python's asynchronous programming capabilities have evolved significantly:

- **The GIL challenge**: Python's Global Interpreter Lock (GIL) traditionally prevented true parallelism for CPU-bound tasks, limiting threading effectiveness to I/O-bound operations.
- **Traditional solutions**:
  - `multiprocessing`: Created separate processes to sidestep the GIL, effective but resource-intensive
  - `threading`: Useful for I/O-bound tasks where the GIL could be released during external operations
- **The async revolution**: The `asyncio` library introduced cooperative multitasking within a single thread, using an event loop to manage multiple tasks efficiently.

### How Flyte 1 handled parallelism

Flyte 1 achieved parallelism through two mechanisms:

- **Static DAG Structure**: The workflow DSL automatically parallelized tasks that weren't dependent on each other.
- **Map Operations**: The `map` operator allowed running a task multiple times in parallel with different inputs.

### How Flyte 2 transforms parallelism

Flyte 2 leverages Python's `asyncio` as the primary mechanism for expressing parallelism, but with a crucial difference: **the Flyte orchestrator acts as the event loop**, managing task execution across distributed infrastructure.

#### The core async concepts

- **`async def`**: Declares a function as a coroutine. When called, it returns a coroutine object managed by the event loop rather than executing immediately.
- **`await`**: Pauses coroutine execution and passes control back to the event loop.
  In standard Python, this enables other tasks to run while waiting for I/O operations.
  In Flyte 2, it signals where tasks can be executed in parallel.
- **`asyncio.gather`**: The primary tool for concurrent execution.
  In standard Python, it schedules multiple awaitable objects to run concurrently within a single event loop.
  In Flyte 2, it signals to the orchestrator that these tasks can be distributed across separate compute resources.

#### A practical example

Consider this pattern for parallel data processing:

```python
import asyncio
import flyte

env = flyte.TaskEnvironment("data_pipeline")

@env.task
async def process_chunk(chunk_id: int, data: str) -> str:
    # This could be any computational work - CPU or I/O bound
    await asyncio.sleep(1)  # Simulating work
    return f"Processed chunk {chunk_id}: {data}"

@env.task
async def parallel_pipeline(data_chunks: List[str]) -> List[str]:
    # Create coroutines for all chunks
    tasks = []
    for i, chunk in enumerate(data_chunks):
        tasks.append(process_chunk(i, chunk))

    # Execute all chunks in parallel
    results = await asyncio.gather(*tasks)
    return results
```

In standard Python, this would provide concurrency benefits primarily for I/O-bound operations.
In Flyte 2, the orchestrator schedules each `process_chunk` task on separate Kubernetes pods, achieving true parallelism for any type of work.

### True parallelism for all workloads

This is where Flyte 2's approach becomes revolutionary: **async syntax is not just for I/O-bound operations**.
The `async`/`await` syntax becomes a powerful way to declare your workflow's parallel structure for any type of computation.

When Flyte's orchestrator encounters `await asyncio.gather(...)`, it understands that these tasks are independent and can be executed simultaneously across different compute resources.
This means you achieve true parallelism for:

- **CPU-bound computations**: Heavy mathematical operations, model training, data transformations
- **I/O-bound operations**: Database queries, API calls, file operations
- **Mixed workloads**: Any combination of computational and I/O tasks

The Flyte platform handles the complex orchestration while you express parallelism using intuitive `async` syntax.

## Bridging the transition: Sync support and migration tools

### Seamless synchronous task support

Recognizing that many existing codebases use synchronous functions, Flyte 2 provides seamless backward compatibility:

```python
@env.task
def legacy_computation(x: int) -> int:
    # Existing synchronous function works unchanged
    return x * x + 2 * x + 1

@env.task
async def modern_workflow(numbers: List[int]) -> List[int]:
    # Call sync tasks from async context using .aio()
    tasks = []
    for num in numbers:
        tasks.append(legacy_computation.aio(num))

    results = await asyncio.gather(*tasks)
    return results
```

Under the hood, Flyte automatically "asyncifies" synchronous functions, wrapping them to participate seamlessly in the async execution model.
You don't need to rewrite existing code—just leverage the `.aio()` method when calling sync tasks from async contexts.

### The `flyte.map` function: Familiar patterns

For scenarios that previously used Flyte 1's `map` operation, Flyte 2 provides `flyte.map` as a direct replacement:

```python
@env.task
async def async_map_example(n: int) -> List[str]:
    # Async version using flyte.map
    results = []
    async for result in flyte.map.aio(process_item, range(n)):
        if isinstance(result, Exception):
            raise result
        results.append(result)
    return results

@env.task
def sync_map_example(n: int) -> List[str]:
    # Synchronous version for easier migration
    results = []
    for result in flyte.map(process_item, range(n)):
        if isinstance(result, Exception):
            raise result
        results.append(result)
    return results
```

The `flyte.map` function provides:

- **Dual interfaces**: `flyte.map.aio()` for async contexts, `flyte.map()` for sync contexts
- **Built-in error handling**: `return_exceptions` parameter for graceful failure handling
- **Automatic UI grouping**: Creates logical groups for better workflow visualization
- **Concurrency control**: Optional limits for resource management

## Migration strategy

Moving from Flyte 1 to 2 follows these key steps:

### 1. Replace workflow decorators

```python
# Flyte 1
@workflow
def my_workflow(data: List[str]) -> List[str]:
    return [process_item(item=item) for item in data]

# Flyte 2
@env.task
async def my_workflow(data: List[str]) -> List[str]:
    tasks = [process_item.aio(item) for item in data]
    return await asyncio.gather(*tasks)
```

### 2. Adopt async patterns

- Use `asyncio.gather()` or `flyte.map()` for parallel execution
- Add `async`/`await` keywords where you want parallelism
- Keep existing sync task functions unchanged

### 3. Leverage enhanced capabilities

- Add conditional logic and loops within workflows
- Implement proper error handling with try/except
- Create dynamic workflows that adapt to runtime conditions

## Trade-offs and considerations

### The dynamic nature

Dynamic workflows bring immense flexibility but also some considerations:

- **Debugging complexity**: Since workflow structure emerges at runtime, debugging may require different approaches than static DAG analysis.
- **Testing strategies**: Dynamic workflows benefit from comprehensive unit testing of individual components and integration testing of full workflow paths.
- **Runtime dependencies**: Workflow structure depends on runtime data and decisions, requiring careful consideration of edge cases.

### Learning curve management

The transition to async programming is smoothed by:

- **Gradual adoption**: Start with synchronous tasks and gradually introduce async patterns where parallelism provides benefits.
- **Familiar tools**: `flyte.map()` provides a familiar interface for common parallel patterns.
- **Pure Python**: Developers can leverage existing Python knowledge rather than learning a new DSL.

## The future is pure Python

Flyte 2's transformation represents more than a version upgrade—it's a fundamental reimagining of workflow orchestration. By embracing pure Python and async programming, Flyte 2 delivers:

- **Developer experience**: Intuitive, familiar Python patterns for all workflow needs
- **Scalable parallelism**: True parallel execution for any workload type
- **Operational flexibility**: Dynamic workflows that adapt to real-world requirements
- **Migration path**: Smooth transition tools that respect existing investments

The result is a platform where expressing complex, parallel workflows feels as natural as writing standard Python code, while the underlying infrastructure handles the complexities of distributed execution at scale.

For detailed exploration of specific async patterns, see [Fanout](./fanout.md) for large-scale parallel processing and [Groups](./groups.md) for organizing complex workflows in the UI.

## Looking ahead: Static DAG compilation

While Flyte 2's dynamic execution model provides unprecedented flexibility, the platform recognizes that certain use cases benefit from static analysis and ahead-of-time compilation. Currently under development is a system for "compiling" the top-level task of a Flyte 2 workflow into a static DAG.

### The best of both worlds

This upcoming feature will provide:

- **Static snalysis**: Enable workflow visualization and validation before execution
- **Predictable resources**: Allow precise resource planning and scheduling optimization
- **Traditional tooling**: Support existing DAG-based analysis and monitoring tools
- **Hybrid approach**: Choose between dynamic and static execution based on workflow characteristics

### Compilation constraints and capabilities

The static compilation system will naturally have limitations compared to fully dynamic workflows:

- **Runtime-dependent Logic**: Loops and parallel operations (`asyncio.gather`) that depend on runtime data cannot be statically determined
- **Dynamic fanouts**: Variable-size parallel processing that emerges from data characteristics remains a runtime feature
- **Conditional branching**: Decision trees that depend on intermediate results require dynamic execution

However, for the subset of workflows that are "static-izable"—those with predictable structure and known parallelism patterns—static compilation will provide significant benefits in terms of analysis, optimization, and integration with traditional workflow management tools.

### Migration flexibility

This feature reinforces Flyte 2's commitment to supporting diverse workflow patterns.
Teams can:

- Start with dynamic workflows for maximum flexibility
- Selectively compile stable, predictable workflows to static DAGs
- Maintain hybrid pipelines that leverage both execution models
- Evolve workflows from static to dynamic as requirements change

