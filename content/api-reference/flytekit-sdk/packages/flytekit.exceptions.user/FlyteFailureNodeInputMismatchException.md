---
title: FlyteFailureNodeInputMismatchException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteFailureNodeInputMismatchException

**Package:** `flytekit.exceptions.user`

Assertion failed.


```python
class FlyteFailureNodeInputMismatchException(
    failure_node_node: typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')],
    workflow: WorkflowBase,
)
```
| Parameter | Type | Description |
|-|-|-|
| `failure_node_node` | `typing.Union[ForwardRef('WorkflowBase'), ForwardRef('Task')]` | |
| `workflow` | `WorkflowBase` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

