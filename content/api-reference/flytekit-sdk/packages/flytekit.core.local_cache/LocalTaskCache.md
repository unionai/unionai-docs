---
title: LocalTaskCache
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LocalTaskCache

**Package:** `flytekit.core.local_cache`

This class implements a persistent store able to cache the result of local task executions.


## Methods

| Method | Description |
|-|-|
| [`clear()`](#clear) |  |
| [`get()`](#get) |  |
| [`initialize()`](#initialize) |  |
| [`set()`](#set) |  |


### clear()

```python
def clear()
```
### get()

```python
def get(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
) -> typing.Optional[flytekit.models.literals.LiteralMap]
```
| Parameter | Type | Description |
|-|-|-|
| `task_name` | `str` | |
| `cache_version` | `str` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` | |

### initialize()

```python
def initialize()
```
### set()

```python
def set(
    task_name: str,
    cache_version: str,
    input_literal_map: flytekit.models.literals.LiteralMap,
    cache_ignore_input_vars: typing.Tuple[str, ...],
    value: flytekit.models.literals.LiteralMap,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_name` | `str` | |
| `cache_version` | `str` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` | |
| `value` | `flytekit.models.literals.LiteralMap` | |

