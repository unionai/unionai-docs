---
title: ShardConfig
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# ShardConfig

**Package:** `flyte.prefetch`

Configuration for model sharding.



## Parameters

```python
class ShardConfig(
    engine: typing.Literal['vllm'],
    args: *args,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `engine` | `typing.Literal['vllm']` | The sharding engine to use (currently only "vllm" is supported). |
| `args` | `*args` | Arguments for the sharding engine. |

