---
title: GCS
version: 2.0.0b55
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GCS

**Package:** `flyte.storage`

Any GCS specific configuration.


```python
class GCS(
    retries: int,
    backoff: datetime.timedelta,
    enable_debug: bool,
    attach_execution_metadata: bool,
    gsutil_parallelism: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `retries` | `int` | |
| `backoff` | `datetime.timedelta` | |
| `enable_debug` | `bool` | |
| `attach_execution_metadata` | `bool` | |
| `gsutil_parallelism` | `bool` | |

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
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type | Description |
|-|-|-|
| `anonymous` | `bool` | |
| `kwargs` | `**kwargs` | |

