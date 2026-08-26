---
title: Storage
version: 2.6.9
variants: +flyte +union
layout: py_api
---

# Storage

**Package:** `flyte.storage`

Data storage configuration that applies across any provider.


## Parameters

```python
class Storage(
    retries: int = 3,
    backoff: datetime.timedelta = datetime.timedelta(seconds=5),
    enable_debug: bool = False,
    attach_execution_metadata: bool = True,
)
```
| Parameter | Type | Description |
|-|-|-|
| `retries` | `int` | |
| `backoff` | `datetime.timedelta` | |
| `enable_debug` | `bool` | |
| `attach_execution_metadata` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Construct the config object automatically from environment variables. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


### auto()

```python
def auto()
```
Construct the config object automatically from environment variables.


### get_fsspec_kwargs()

```python
def get_fsspec_kwargs(
    anonymous: bool = False,
    **kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type | Description |
|-|-|-|
| `anonymous` | `bool` | |
| `**kwargs` |  | |

