---
title: flytekit.core.local_cache
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.local_cache

## Directory

### Classes

| Class | Description |
|-|-|
| [`LocalTaskCache`](.././flytekit.core.local_cache#flytekitcorelocal_cachelocaltaskcache) | This class implements a persistent store able to cache the result of local task executions. |

### Variables

| Property | Type | Description |
|-|-|-|
| `CACHE_LOCATION` | `str` |  |

## flytekit.core.local_cache.LocalTaskCache

This class implements a persistent store able to cache the result of local task executions.


### Methods

| Method | Description |
|-|-|
| [`clear()`](#clear) |  |
| [`get()`](#get) |  |
| [`initialize()`](#initialize) |  |
| [`set()`](#set) |  |


#### clear()

```python
def clear()
```
#### get()

```python
def get(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
) -> typing.Optional[flytekit.models.literals.LiteralMap]
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `cache_version` | `str` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |

#### initialize()

```python
def initialize()
```
#### set()

```python
def set(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
    value: flytekit.models.literals.LiteralMap,
)
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `cache_version` | `str` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |
| `value` | `flytekit.models.literals.LiteralMap` |

