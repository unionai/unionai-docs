---
title: Caching
weight: 140
variants: +flyte +serverless +byoc +selfmanaged
---

# Caching

Flyte 2 provides intelligent **task output caching** that automatically avoids redundant computation by reusing previously computed task results.

> [!NOTE]
> Caching works at the task level and caches complete task outputs.
> For function-level checkpointing and resumption *within tasks*, see [Traces](../task-programming/traces).

## Overview

By default, caching is disabled.

If caching is enabled for a task, then Flyte determines a **cache key** for the task.
When the task runs, Flyte checks if a cache entry exists for that key.
If found, the cached result is returned immediately instead of re-executing the task.

The cache key is either generated automatically based on the task's inputs and configuration, or specified explicitly in the code as a version string.

Key benefits of caching:

- **Faster iteration**: Skip expensive recomputation during development.
- **Cost optimization**: Reduce compute costs by avoiding redundant work.
- **Reliability**: Consistent results for identical inputs across executions.
- **Development efficiency**: Focus on changing code without waiting for unchanged dependencies.

## Basic caching usage



### Enabling caching with default behavior

The simplest way to enable caching is using the `"auto"` behavior:

```python
import flyte
from flyte import Cache

env = flyte.TaskEnvironment(name="caching_example")

@env.task(cache=Cache(behavior="auto"))
async def expensive_computation(data: str, iterations: int) -> str:
    # This function's results will be cached automatically
    print(f"Performing expensive computation on {data}")
    # Simulate expensive work
    result = process_data_expensively(data, iterations)
    return result
```

With `behavior="auto"`, the cache version is automatically generated based on the function's source code. If you change the function implementation, the cache is automatically invalidated.

### Using string shorthand

For convenience, you can use string values for common cache behaviors:

```python
@env.task(cache="auto")  # Equivalent to Cache(behavior="auto")
async def auto_cached_task(x: int) -> int:
    return x * x

@env.task(cache="disable")  # Equivalent to Cache(behavior="disable")
async def never_cached_task(x: int) -> int:
    return x * x
```

## Cache behaviors

Flyte 2 supports three main cache behaviors:

### `"auto"` - Automatic versioning

```python
@env.task(cache=Cache(behavior="auto"))
async def auto_versioned_task(data: str) -> str:
    # Cache version automatically generated from function source code
    return transform_data(data)
```

<!-- TODO:
Figure out what this refers to:

> Ketan Umare
> you can specifiy version along with "auto" as well
-->

- **When to use**: Development and most production scenarios.
- **Cache invalidation**: Automatic when function code changes.
- **Benefits**: Zero-maintenance caching that "just works".

### `"override"`

```python
@env.task(cache=Cache(behavior="override", version_override="v1.2"))
async def manually_versioned_task(data: str) -> str:
    # Cache only invalidated when version_override changes
    return transform_data(data)
```

- **When to use**: When you need explicit control over cache invalidation.
- **Cache invalidation**: Manual, by changing `version_override`.
- **Benefits**: Stable caching across code changes that don't affect logic.

### `"disable"` - No caching

```python
@env.task(cache=Cache(behavior="disable"))
async def always_fresh_task(data: str) -> str:
    # Never cached - always executes
    return get_current_timestamp() + data
```

- **When to use**: Non-deterministic functions, side effects, or always-fresh data
- **Cache invalidation**: N/A - never cached
- **Benefits**: Ensures execution every time

**This is the default.**

## Advanced caching configuration

### Ignoring specific inputs

Sometimes you want to cache based on some inputs but not others:

```python
@env.task(cache=Cache(
    behavior="override",
    version_override="v1",
    ignored_inputs=("debug_flag", "logging_level")
))
async def selective_caching(data: str, debug_flag: bool, logging_level: str) -> str:
    # Cache key only includes 'data', ignores debug_flag and logging_level
    if debug_flag:
        print(f"Debug: processing {data}")
    return process_data(data)
```

This is useful for:
- Debug flags that don't affect computation
- Logging levels or output formats
- Metadata that doesn't impact results

### Cache serialization

Cache serialization ensures that only one instance of a task runs at a time for identical inputs:

```python
@env.task(cache=Cache(
    behavior="auto",
    serialize=True
))
async def expensive_model_training(dataset: str, params: dict) -> str:
    # Only one instance trains the model; others wait and reuse results
    model = train_large_model(dataset, params)
    return save_model(model)
```

**When to use serialization**:
- Very expensive computations (model training, large data processing)
- Shared resources that shouldn't be accessed concurrently
- Operations where multiple parallel executions provide no benefit

**How it works**:
1. First execution acquires a reservation and runs normally
2. Concurrent executions with identical inputs wait for the first to complete
3. Once complete, all waiting executions receive the cached result
4. If the running execution fails, another waiting execution takes over

### Salt for cache key variation

Use salt to vary cache keys without changing function logic:

```python
@env.task(cache=Cache(
    behavior="override",
    version_override="v1",
    salt="experiment_2024_q4"
))
async def experimental_analysis(data: str) -> dict:
    # Same code but different cache namespace
    return run_analysis(data)
```

Salt is useful for:
- A/B testing with identical code
- Temporary cache namespaces for experiments
- Environment-specific cache isolation

## Cache policies

For automatic versioning, Flyte 2 uses cache policies to generate version hashes:

### Function body policy (default)

The default `FunctionBodyPolicy` generates cache versions from the function's source code:

```python
from flyte import Cache
from flyte._cache import FunctionBodyPolicy

@env.task(cache=Cache(
    behavior="auto",
    policies=[FunctionBodyPolicy()]  # This is the default
))
async def code_sensitive_task(data: str) -> str:
    # Cache automatically invalidated when this function changes
    return data.upper()
```

### Custom cache policies

You can implement custom cache policies by following the `CachePolicy` protocol:

```python
from flyte._cache import CachePolicy, VersionParameters

class DatasetVersionPolicy(CachePolicy):
    def get_version(self, salt: str, params: VersionParameters) -> str:
        # Generate version based on custom logic
        dataset_version = get_dataset_version()
        return f"{salt}_{dataset_version}"

@env.task(cache=Cache(
    behavior="auto",
    policies=[DatasetVersionPolicy()]
))
async def dataset_dependent_task(data: str) -> str:
    # Cache invalidated when dataset version changes
    return process_with_current_dataset(data)
```

## Environment-level caching

You can set default cache behavior at the environment level:

```python
env = flyte.TaskEnvironment(
    name="cached_environment",
    cache=Cache(behavior="auto")  # Default for all tasks
)

@env.task  # Inherits auto caching from environment
async def inherits_caching(data: str) -> str:
    return process_data(data)

@env.task(cache=Cache(behavior="disable"))  # Override environment default
async def overrides_caching(data: str) -> str:
    return get_timestamp()
```

## Runtime cache control

### Overriding cache at execution time

Force cache invalidation for a specific run:

```python
# Disable caching for this specific execution
run = flyte.with_runcontext(overwrite_cache=True).run(my_cached_task, data="test")
```

### Checking cache status

Tasks can access cache information through the execution context:

```python
@env.task(cache=Cache(behavior="auto"))
async def cache_aware_task(data: str) -> str:
    ctx = flyte.ctx()
    # Access cache-related context if needed
    return process_data(data)
```

## Cache scope and isolation

### Project and domain isolation

Caches are automatically isolated by:
- **Project**: Tasks in different projects have separate cache namespaces
- **Domain**: Development, staging, and production domains maintain separate caches
- **Task identity**: Each unique task has its own cache space

### Local development caching

When running locally, Flyte 2 maintains a local cache:

```python
# Local execution uses ~/.flyte/local-cache/
flyte.init()  # Local mode
result = flyte.run(my_cached_task, data="test")
```

Local cache behavior:
- Stored in `~/.flyte/local-cache/` directory
- No project/domain isolation (since running locally)
- Can be cleared with `flyte local-cache clear`
- Disabled by setting `FLYTE_LOCAL_CACHE_ENABLED=false`

## Best practices

### When to enable caching

**Good candidates for caching**:
- Pure functions with deterministic outputs
- Expensive computations (model training, data processing)
- External API calls with stable responses
- File processing operations

**Avoid caching for**:
- Functions with side effects (logging, file writes)
- Non-deterministic functions (random generation, timestamps)
- Functions that interact with external state
- Very fast operations where caching overhead exceeds benefits

### Cache configuration strategies

1. **Start with `behavior="auto"`** for most tasks
2. **Use `behavior="override"`** for stable production workflows
3. **Add `serialize=True`** for expensive, parallelizable operations
4. **Configure `ignored_inputs`** for debug/metadata parameters
5. **Use environment-level defaults** to reduce configuration duplication

### Performance considerations

- **Cache hit performance**: Retrieving cached results is orders of magnitude faster than re-execution
- **Cache miss overhead**: Minimal overhead for cache key generation and lookup
- **Storage costs**: Cached outputs consume storage space in your Flyte backend
- **Network transfer**: Large cached objects may have network transfer costs

### Debugging cached executions

When troubleshooting cache behavior:

1. **Check cache configuration**: Verify `behavior`, `version_override`, and `ignored_inputs`
2. **Review function changes**: Auto-cached functions invalidate on source code changes
3. **Inspect input variations**: Even small input changes create new cache keys
4. **Use cache override**: Force fresh execution with `overwrite_cache=True`
5. **Monitor cache hits**: Check execution logs for cache hit/miss information

## Example: Complete caching workflow

Here's a comprehensive example showing different caching patterns:

```python
import flyte
from flyte import Cache

env = flyte.TaskEnvironment(name="ml_pipeline", cache=Cache(behavior="auto"))

@env.task  # Uses environment default (auto caching)
async def load_dataset(dataset_name: str) -> dict:
    # Cached - expensive data loading
    return load_large_dataset(dataset_name)

@env.task(cache=Cache(behavior="override", version_override="v2.1"))
async def preprocess_data(raw_data: dict, config: dict) -> dict:
    # Manual versioning for stable preprocessing logic
    return apply_preprocessing(raw_data, config)

@env.task(cache=Cache(
    behavior="auto",
    serialize=True,
    ignored_inputs=("experiment_name",)
))
async def train_model(data: dict, hyperparams: dict, experiment_name: str) -> str:
    # Serialized expensive training, ignoring experiment name
    model = train_neural_network(data, hyperparams)
    return save_model(model, experiment_name)

@env.task(cache=Cache(behavior="disable"))
async def generate_report(model_path: str, timestamp: str) -> str:
    # Never cached - always generates fresh reports
    return create_timestamped_report(model_path, timestamp)

@env.task
async def ml_pipeline(dataset_name: str, config: dict, hyperparams: dict) -> str:
    # Orchestrator task - benefits from sub-task caching
    raw_data = await load_dataset(dataset_name)
    processed_data = await preprocess_data(raw_data, config)
    model_path = await train_model(processed_data, hyperparams, "exp_001")
    report = await generate_report(model_path, "2024-01-15")
    return report
```

This pipeline efficiently caches expensive operations while ensuring fresh outputs where needed, demonstrating the flexibility and power of Flyte 2's caching system.
