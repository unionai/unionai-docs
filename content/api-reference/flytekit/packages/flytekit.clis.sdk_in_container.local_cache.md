---
title: flytekit.clis.sdk_in_container.local_cache
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.local_cache

## Directory

### Classes

| Class | Description |
|-|-|
| [`LocalTaskCache`](.././flytekit.clis.sdk_in_container.local_cache#flytekitclissdk_in_containerlocal_cachelocaltaskcache) | This class implements a persistent store able to cache the result of local task executions. |

## flytekit.clis.sdk_in_container.local_cache.LocalTaskCache

This class implements a persistent store able to cache the result of local task executions.


### Methods

| Method | Description |
|-|-|
| [`clear()`](#clear) | None |
| [`get()`](#get) | None |
| [`initialize()`](#initialize) | None |
| [`set()`](#set) | None |


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
):
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
):
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `cache_version` | `str` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |
| `value` | `flytekit.models.literals.LiteralMap` |

