---
title: Caching
weight: 4
variants: +flyte +union
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

### `"auto"` - automatic versioning

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="auto" lang="python" >}}

With `behavior="auto"`, the cache version is automatically generated based on the function's source code.
If you change the function implementation, the cache is automatically invalidated.

- **When to use**: Development and most production scenarios.
- **Cache invalidation**: Automatic when function code changes.
- **Benefits**: Zero-maintenance caching that "just works".

You can also use the direct string shorthand:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="auto-shorthand" lang="python" >}}

### `"override"`

With `behavior="override"`, you can specify a custom cache key in the `version_override` parameter.
Since the cache key is fixed as part of the code, it can be manually changed when you need to invalidate the cache.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="override" lang="python" >}}

- **When to use**: When you need explicit control over cache invalidation.
- **Cache invalidation**: Manual, by changing `version_override`.
- **Benefits**: Stable caching across code changes that don't affect logic.

### `"disable"` - No caching

To explicitly disable caching, use the `"disable"` behavior.
**This is the default behavior.**

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="disable" lang="python" >}}

- **When to use**: Non-deterministic functions, side effects, or always-fresh data.
- **Cache invalidation**: N/A - never cached.
- **Benefits**: Ensures execution every time.

You can also use the direct string shorthand:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="disable-shorthand" lang="python" >}}

## Advanced caching configuration

### Ignoring specific inputs

Sometimes you want to cache based on some inputs but not others:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="ignored" lang="python" >}}

**This is useful for**:

- Debug flags that don't affect computation
- Logging levels or output formats
- Metadata that doesn't impact results

### Cache serialization

Cache serialization ensures that only one instance of a task runs at a time for identical inputs:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="serialize" lang="python" >}}

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

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="salt" lang="python" >}}

**`salt` is useful for**:

- A/B testing with identical code.
- Temporary cache namespaces for experiments.
- Environment-specific cache isolation.

## Caching with `flyte.map`

When you [map a task over a list of inputs](../task-programming/map), each item runs as its own **independent task action** with its own inputs. Caching therefore applies **per element**: configure the cache on the mapped task (via the `@env.task` decorator or the `TaskEnvironment`, exactly as above — there is no separate cache setting on the `flyte.map` call itself), and Flyte computes a cache key for each item individually.

The per-element cache key is that item's mapped input(s) plus the standard components — the task name, interface hash, and cache version. Two consequences follow:

- **Unchanged items are cache hits even when other items change.** If you re-run a map and only some items differ, the unchanged items are served from cache and only the changed ones recompute.
- **Order doesn't matter.** The cache key depends on an item's own inputs, not its position, so reordering the input list (or changing the list's length) doesn't invalidate the items that are still present.

For example, mapping `[1, 2, 3]` and later mapping `[3, 1, 4]` recomputes only the new item `4`; `1`, `2`, and `3` are already cached.

### Excluding a bound argument from the per-element key

When you bind constant arguments with `functools.partial` (see [Binding constant arguments](../task-programming/map#binding-constant-arguments-with-functoolspartial)), those bound values become part of **each element's** cache key. If a bound value changes between runs but does not affect the result — a run ID, a status flag, a timestamp — every element misses the cache. Add such volatile inputs to `ignored_inputs` on the mapped task so they're dropped from the key:

```python
from functools import partial

import flyte

env = flyte.TaskEnvironment(name="map-cache")


@env.task(cache=flyte.Cache(behavior="auto", ignored_inputs=("batch_id",)))
async def score(compound_id: str, batch_id: str) -> str:
    ...


@env.task
async def main(batch_id: str) -> list[str]:
    compounds = [str(i) for i in range(3)]
    scorer = partial(score, batch_id=batch_id)
    # batch_id is bound for every item but ignored for caching, so each
    # element is keyed only on compound_id.
    return list(flyte.map(scorer, compounds))
```

Here `batch_id` is constant across the map yet varies between runs; listing it in `ignored_inputs` keeps each element's cache keyed only on `compound_id`, so the items are reused across runs.

## Content-based caching for DataFrames, files, and directories

When a task input is a DataFrame (`pandas`, `polars`, or `flyte.io.DataFrame`), a `flyte.io.File`, or a `flyte.io.Dir`, the value is passed *by reference* - the cache key is derived from the data's storage location, not its contents. As a result, a downstream task keyed on such an input does **not** get a cache hit when the underlying data is identical but lives at a new path (the common case, since each run writes to a fresh location).

To cache on **content** instead, attach a hash of the data at the point where it is produced. Flyte then uses that content hash when computing the cache key of any downstream consuming task, so identical content produces a cache hit regardless of where it is stored.

> [!NOTE]
> Caching applies only on a remote cluster - local execution does not produce cache hits across runs.

### DataFrames

For a raw `pandas` or `polars` DataFrame, supply a content hash with `flyte.io.HashFunction.from_fn` in a `typing.Annotated` return type. Define the hash function once and reuse the annotated alias:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/content_caching.py" fragment="pandas" lang="python" >}}

The producer's return annotation tells Flyte to compute the content hash; the consumer is cached on it. The same pattern works for `polars`:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/content_caching.py" fragment="polars" lang="python" >}}

For `flyte.io.DataFrame`, pass the `HashFunction` to `DataFrame.from_local` via the `hash_method` parameter instead of annotating the return type:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/content_caching.py" fragment="flyte-dataframe" lang="python" >}}

### Files

A `flyte.io.File` accepts a `hash_method` on `File.from_local` (and on `File.new_remote`). Pass a `HashFunction` that hashes the file's bytes, and the file is cached on its content rather than its remote path:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/content_caching.py" fragment="file" lang="python" >}}

### Directories

`flyte.io.Dir.from_local` does **not** take a `HashFunction` callable. Instead, compute a content key yourself and pass it as the precomputed `dir_cache_key`:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/content_caching.py" fragment="dir" lang="python" >}}

## Cache policies

For details on implementing custom cache policies, see the [`CachePolicy` protocol](../../api-reference/flyte-sdk/packages/flyte/cachepolicy) and [`Cache` class](../../api-reference/flyte-sdk/packages/flyte/cache) API references.

For `behavior="auto"`, Flyte uses cache policies to generate version hashes.

### Function body policy (default)

The default `FunctionBodyPolicy` generates cache versions from the function's source code:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="policy" lang="python" >}}

### Custom cache policies

You can implement custom cache policies by following the `CachePolicy` protocol:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="custom-policy" lang="python" >}}

## Caching configuration at different levels

You can configure caching at three levels: `TaskEnvironment` definition, `@env.task` decorator, and task invocation.

### `TaskEnvironment` level

You can configure caching at the `TaskEnvironment` level.
This will set the default cache behavior for all tasks defined using that environment.
For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="env-level" lang="python" >}}

### `@env.task` decorator level

By setting the cache parameter in the `@env.task` decorator, you can override the environment's default cache behavior for specific tasks:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="decorator-level" lang="python" >}}

### `task.override` level

By setting the cache parameter in the `task.override` method, you can override the cache behavior for specific task invocations:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/caching/caching.py" fragment="override-level" lang="python" >}}

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
