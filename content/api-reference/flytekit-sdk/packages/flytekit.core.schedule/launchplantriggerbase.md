---
title: LaunchPlanTriggerBase
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LaunchPlanTriggerBase

**Package:** `flytekit.core.schedule`

```python
protocol LaunchPlanTriggerBase()
```
## Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### to_flyte_idl()

```python
def to_flyte_idl(
    args,
    kwargs,
) -> google.protobuf.message.Message
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

