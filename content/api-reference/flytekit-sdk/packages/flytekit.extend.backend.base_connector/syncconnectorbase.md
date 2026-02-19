---
title: SyncConnectorBase
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SyncConnectorBase

**Package:** `flytekit.extend.backend.base_connector`

This is the base class for all sync connectors.
It defines the interface that all connectors must implement.
The connector service is responsible for invoking connectors.
Propeller sends a request to connector service, and gets a response in the same call.

All the connectors should be registered in the ConnectorRegistry.
Connector Service
will look up the connector based on the task type. Every task type can only have one connector.



```python
class SyncConnectorBase(
    task_type_name: str,
    task_type_version: int,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_type_name` | `str` | |
| `task_type_version` | `int` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `task_category` | `None` | task category that the connector supports |

## Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This is the method that the connector will run. |


### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
This is the method that the connector will run.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `output_prefix` | `str` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `kwargs` | `**kwargs` | |

