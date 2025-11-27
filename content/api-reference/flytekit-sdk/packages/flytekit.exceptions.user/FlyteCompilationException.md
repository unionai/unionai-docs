---
title: FlyteCompilationException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteCompilationException

**Package:** `flytekit.exceptions.user`

Common base class for all non-exit exceptions.


```python
class FlyteCompilationException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `fn` | `typing.Callable` | |
| `param_name` | `typing.Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

