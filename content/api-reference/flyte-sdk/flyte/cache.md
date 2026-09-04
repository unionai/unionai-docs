---
title: Cache
description: "Cache configuration for a task."
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# Cache

**Package:** `flyte`

Cache configuration for a task.

Three cache behaviors are available:

- `"auto"` — Cache version is computed automatically from cache policies
  (default: `FunctionBodyPolicy`, which hashes the function source code).
  Any change to the function body invalidates the cache.
- `"override"` — You provide an explicit `version_override` string.
  Cache is only invalidated when you change the version.
- `"disable"` — Caching is disabled; task always re-executes.

Set via `TaskEnvironment(cache=...)`, `@env.task(cache=...)`, or
`task.override(cache=...)`.



## Parameters

```python
class Cache(
    behavior: typing.Literal['auto', 'override', 'disable'],
    version_override: typing.Optional[str] = None,
    serialize: bool = False,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str] = <factory>,
    salt: str = '',
    policies: typing.Union[typing.List[flyte._cache.cache.CachePolicy], flyte._cache.cache.CachePolicy, NoneType] = None,
    max_age: datetime.timedelta | int | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `behavior` | `typing.Literal['auto', 'override', 'disable']` | Cache behavior — `"auto"`, `"override"`, or `"disable"`. |
| `version_override` | `typing.Optional[str]` | Explicit cache version string. Only used when `behavior="override"`. |
| `serialize` | `bool` | If `True`, concurrent executions with identical inputs will be serialized — only one runs and the rest wait for and reuse the cached result. Default `False`. |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` | Input parameter names to exclude from the cache key. Useful when some inputs (e.g., timestamps) shouldn't affect caching. |
| `salt` | `str` | Additional salt for cache key generation. Use to create separate cache namespaces (e.g., `salt="v2"` to invalidate all existing caches). |
| `policies` | `typing.Union[typing.List[flyte._cache.cache.CachePolicy], flyte._cache.cache.CachePolicy, NoneType]` | Cache policies for version generation. Defaults to `[FunctionBodyPolicy()]` when `behavior="auto"`. Provide a custom `CachePolicy` implementation for alternative versioning strategies. |
| `max_age` | `datetime.timedelta \| int \| None` | Maximum age of a cached result this task will reuse, as a `timedelta` or an integer number of seconds. `None` uses the platform default, zero disables age-based expiration, and negative values are invalid. |

## Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |
| [`is_enabled()`](#is_enabled) | Check if the cache policy is enabled. |


### get_ignored_inputs()

```python
def get_ignored_inputs()
```
### get_version()

```python
def get_version(
    params: typing.Optional[flyte._cache.cache.VersionParameters] = None,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `params` | `typing.Optional[flyte._cache.cache.VersionParameters]` | |

### is_enabled()

```python
def is_enabled()
```
Check if the cache policy is enabled.


