---
title: AsyncConnectorExecutorMixin
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# AsyncConnectorExecutorMixin

**Package:** `flyte.connectors`

This mixin class is used to run the connector task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the connector.


## Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) |  |


### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

