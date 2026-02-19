---
title: RemoteExecutionBase
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RemoteExecutionBase

**Package:** `flytekit.remote.executions`

```python
class RemoteExecutionBase(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `error` | `None` |  |
| `inputs` | `None` |  |
| `is_done` | `None` |  |
| `outputs` | `None` | :return: Returns the outputs LiteralsResolver to the execution :raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error. |

