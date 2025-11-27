---
title: Entities
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Entities

**Package:** `flytekit.clis.sdk_in_container.run`

NamedTuple to group all entities in a file


## Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`matching_lp()`](#matching_lp) | Returns the variable name of the launch plan in the file. |


### all()

```python
def all()
```
### matching_lp()

```python
def matching_lp(
    lp_name: str,
) -> typing.Optional[str]
```
Returns the variable name of the launch plan in the file


| Parameter | Type | Description |
|-|-|-|
| `lp_name` | `str` | |

