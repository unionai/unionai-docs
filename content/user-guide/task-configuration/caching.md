---
title: Caching
weight: 4
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
The key is composed of the following:

* Final inputs: The set of inputs after removing any specified in the `ignored_inputs`.
* Task name: The fully-qualified name of the task.
* Interface hash: A hash of the task's input and output types.
* Cache version: The cache version string.

If the cache behavior is set to `"auto"`, the cache version is automatically generated using a hash of the task's source code (or according to the custom policy if one is specified).
If the cache behavior is set to `"override"`, the cache version can be specified explicitly using the `version_override` parameter.

When the task runs, Flyte checks if a cache entry exists for the key.
If found, the cached result is returned immediately instead of re-executing the task.

## Basic caching usage

Flyte 2 supports three main cache behaviors:

### `"auto"` - Automatic versioning

```python
@env.task(cache=Cache(behavior="auto"))
async def auto_versioned_task(data: str) -> str:
    return transform_data(data)
```

With `behavior="auto"`, the cache version is automatically generated based on the function's source code.
If you change the function implementation, the cache is automatically invalidated.

- **When to use**: Development and most production scenarios.
- **Cache invalidation**: Automatic when function code changes.
- **Benefits**: Zero-maintenance caching that "just works".

You can also use the direct string shorthand:

```python
@env.task(cache="auto")
async def auto_cached_task(x: int) -> int:
    return transform_data(data)
```

### `"override"`

With `behavior="override"`, you can specify a custom cache key in the `version_override` parameter.
Since the cache key is fixed as part of the code, it can be manually changed when you need to invalidate the cache.

```python
@env.task(cache=Cache(behavior="override", version_override="v1.2"))
async def manually_versioned_task(data: str) -> str:
    return transform_data(data)
```

- **When to use**: When you need explicit control over cache invalidation.
- **Cache invalidation**: Manual, by changing `version_override`.
- **Benefits**: Stable caching across code changes that don't affect logic.

### `"disable"` - No caching

To explicitly disable caching, use the `"disable"` behavior.
**This is the default behavior.**

```python
@env.task(cache=Cache(behavior="disable"))
async def always_fresh_task(data: str) -> str:
    return get_current_timestamp() + data
```

- **When to use**: Non-deterministic functions, side effects, or always-fresh data.
- **Cache invalidation**: N/A - never cached.
- **Benefits**: Ensures execution every time.

You can also use the direct string shorthand:

```python
@env.task(cache="disable")
async def auto_cached_task(x: int) -> int:
    return transform_data(data)
```

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
    if debug_flag:
        print(f"Debug: processing {data}")
    return process_data(data)
```

**This is useful for**:
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
    model = train_large_model(dataset, params)
    return save_model(model)
```

**When to use serialization**:
- Very expensive computations (model training, large data processing)
- Shared resources that shouldn't be accessed concurrently
- Operations where multiple parallel executions provide no benefit

**How it works**:
1. First execution acquires a reservation and runs normally.
2. Concurrent executions with identical inputs wait for the first to complete.
3. Once complete, all waiting executions receive the cached result.
4. If the running execution fails, another waiting execution takes over.

### Salt for cache key variation

Use `salt` to vary cache keys without changing function logic:

```python
@env.task(cache=Cache(
    behavior="override",
    version_override="v1",
    salt="experiment_2024_q4"
))
async def experimental_analysis(data: str) -> dict:
    return run_analysis(data)
```

**`salt` is useful for**:
- A/B testing with identical code.
- Temporary cache namespaces for experiments.
- Environment-specific cache isolation.

## Cache policies

For `behavior="auto"`, Flyte uses cache policies to generate version hashes.

### Function body policy (default)

The default `FunctionBodyPolicy` generates cache versions from the function's source code:

```python
from flyte import Cache
from flyte._cache import FunctionBodyPolicy

@env.task(cache=Cache(
    behavior="auto",
    # policies=[FunctionBodyPolicy()]  <-- This is the default. Does not actually need to be specified.
))
async def code_sensitive_task(data: str) -> str:
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

## Caching configuration at different levels

You can configure caching at three levels: `TaskEnvironment` definition, `@env.task` decorator, and task invocation.

### `TaskEnvironment` Level

You can configure caching at the `TaskEnvironment` level.
This will set the default cache behavior for all tasks defined using that environment.
For example:

```python
env = flyte.TaskEnvironment(
    name="cached_environment",
    cache=Cache(behavior="auto")  # Default for all tasks
)

@env.task  # Inherits auto caching from environment
async def inherits_caching(data: str) -> str:
    return process_data(data)
```

### `@env.task` decorator level

By setting the cache parameter in the `@env.task` decorator, you can override the environment's default cache behavior for specific tasks:

```python
@env.task(cache=Cache(behavior="disable"))  # Override environment default
async def overrides_caching(data: str) -> str:
    return get_timestamp()
```

### `task.override` level

By setting the cache parameter in the `task.override` method, you can override the cache behavior for specific task invocations:

```python
@env.task
async def main(data: str) -> str :
    return override_caching_on_call(data).override(cache=Cache(behavior="disable"))
```

## Runtime cache control

You can also force cache invalidation for a specific run:

```python
# Disable caching for this specific execution
run = flyte.with_runcontext(overwrite_cache=True).run(my_cached_task, data="test")
```

## Checking cache status

Tasks can access cache information through the execution context:

```python
@env.task(cache=Cache(behavior="auto"))
async def cache_aware_task(data: str) -> str:
    ctx = flyte.ctx()
    # Access cache-related context if needed
    return process_data(data)
```

## Project and domain cache isolation

Caches are automatically isolated by:
- **Project**: Tasks in different projects have separate cache namespaces.
- **Domain**: Development, staging, and production domains maintain separate caches.

## Local development caching

When running locally, Flyte maintains a local cache:

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
- Pure functions with deterministic outputs.
- Expensive computations (model training, data processing).
- External API calls with stable responses.
- File processing operations.

**Avoid caching for**:
- Functions with side effects (logging, file writes)
- Non-deterministic functions (random generation, timestamps).
- Functions that interact with external state.
- Very fast operations where caching overhead exceeds benefits.

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

This pipeline efficiently caches expensive operations while ensuring fresh outputs where needed, demonstrating the flexibility and power of Flyte's caching system.
