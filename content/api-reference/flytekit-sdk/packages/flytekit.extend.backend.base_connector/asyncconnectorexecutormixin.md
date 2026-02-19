---
title: AsyncConnectorExecutorMixin
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AsyncConnectorExecutorMixin

**Package:** `flytekit.extend.backend.base_connector`

This mixin class is used to run the async task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the connector.

Asynchronous tasks are tasks that take a long time to complete, such as running a query.



## Methods

| Method | Description |
|-|-|
| [`connector_signal_handler()`](#connector_signal_handler) |  |
| [`execute()`](#execute) |  |


### connector_signal_handler()

```python
def connector_signal_handler(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    signum: int,
    frame: frame,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `signum` | `int` | |
| `frame` | `frame` | |

### execute()

```python
def execute(
    kwargs,
) -> flytekit.models.literals.LiteralMap
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

