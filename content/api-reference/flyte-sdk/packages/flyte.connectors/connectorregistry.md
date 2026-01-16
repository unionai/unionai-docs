---
title: ConnectorRegistry
version: 2.0.0b48
variants: +flyte +byoc +selfmanaged +serverless
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
    task_type_version: int,
) -> flyte.connectors._connector.AsyncConnector
```
| Parameter | Type | Description |
|-|-|-|
| `task_type_name` | `str` | |
| `task_type_version` | `int` | |

### register()

```python
def register(
    connector: flyte.connectors._connector.AsyncConnector,
    override: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `connector` | `flyte.connectors._connector.AsyncConnector` | |
| `override` | `bool` | |

