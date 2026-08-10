---
title: ConnectorRegistry
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# ConnectorRegistry

**Package:** `flyte.connectors`

This is the registry for all connectors.
The connector service will look up the connector registry based on the task type and version.


## Methods

| Method | Description |
|-|-|
| [`get_connector()`](#get_connector) |  |
| [`register()`](#register) |  |


### get_connector()

```python
def get_connector(
    task_type_name: str,
    task_type_version: int = 0,
) -> AsyncConnector[Any]
```
| Parameter | Type | Description |
|-|-|-|
| `task_type_name` | `str` | |
| `task_type_version` | `int` | |

### register()

```python
def register(
    connector: flyte.connectors._connector.AsyncConnector[typing.Any],
    override: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `connector` | `flyte.connectors._connector.AsyncConnector[typing.Any]` | |
| `override` | `bool` | |

