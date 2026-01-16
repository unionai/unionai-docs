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

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="auto" lang="python" >}}

With `behavior="auto"`, the cache version is automatically generated based on the function's source code.
If you change the function implementation, the cache is automatically invalidated.

- **When to use**: Development and most production scenarios.
- **Cache invalidation**: Automatic when function code changes.
- **Benefits**: Zero-maintenance caching that "just works".

You can also use the direct string shorthand:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="auto-shorthand" lang="python" >}}

### `"override"`

With `behavior="override"`, you can specify a custom cache key in the `version_override` parameter.
Since the cache key is fixed as part of the code, it can be manually changed when you need to invalidate the cache.

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="override" lang="python" >}}

- **When to use**: When you need explicit control over cache invalidation.
- **Cache invalidation**: Manual, by changing `version_override`.
- **Benefits**: Stable caching across code changes that don't affect logic.

### `"disable"` - No caching

To explicitly disable caching, use the `"disable"` behavior.
**This is the default behavior.**

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="disable" lang="python" >}}

- **When to use**: Non-deterministic functions, side effects, or always-fresh data.
- **Cache invalidation**: N/A - never cached.
- **Benefits**: Ensures execution every time.

You can also use the direct string shorthand:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="disable-shorthand" lang="python" >}}

## Advanced caching configuration

### Ignoring specific inputs

Sometimes you want to cache based on some inputs but not others:


{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="ignored" lang="python" >}}

**This is useful for**:
- Debug flags that don't affect computation
- Logging levels or output formats
- Metadata that doesn't impact results

### Cache serialization

Cache serialization ensures that only one instance of a task runs at a time for identical inputs:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="serialize" lang="python" >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="salt" lang="python" >}}

**`salt` is useful for**:
- A/B testing with identical code.
- Temporary cache namespaces for experiments.
- Environment-specific cache isolation.

## Cache policies

For `behavior="auto"`, Flyte uses cache policies to generate version hashes.

### Function body policy (default)

The default `FunctionBodyPolicy` generates cache versions from the function's source code:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="policy" lang="python" >}}

### Custom cache policies

You can implement custom cache policies by following the `CachePolicy` protocol:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="custom-policy" lang="python" >}}

## Caching configuration at different levels

You can configure caching at three levels: `TaskEnvironment` definition, `@env.task` decorator, and task invocation.

### `TaskEnvironment` Level

You can configure caching at the `TaskEnvironment` level.
This will set the default cache behavior for all tasks defined using that environment.
For example:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="env-level" lang="python" >}}

### `@env.task` decorator level

By setting the cache parameter in the `@env.task` decorator, you can override the environment's default cache behavior for specific tasks:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="decorator-level" lang="python" >}}

### `task.override` level

By setting the cache parameter in the `task.override` method, you can override the cache behavior for specific task invocations:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="override-level" lang="python" >}}

## Runtime cache control

You can also force cache invalidation for a specific run:

```python
# Disable caching for this specific execution
run = flyte.with_runcontext(overwrite_cache=True).run(my_cached_task, data="test")
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
- Disabled by setting `FLYTE_LOCAL_CACHE_ENABLED=false`
