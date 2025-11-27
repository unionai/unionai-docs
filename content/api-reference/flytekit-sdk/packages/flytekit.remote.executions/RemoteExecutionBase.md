---
title: RemoteExecutionBase
version: 1.16.10
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
| `error` |  |  |
| `inputs` |  |  |
| `is_done` |  |  |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |

