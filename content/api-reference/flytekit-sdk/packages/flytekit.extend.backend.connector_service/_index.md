---
title: flytekit.extend.backend.connector_service
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extend.backend.connector_service

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncConnectorService`](../flytekit.extend.backend.connector_service/asyncconnectorservice) |  |
| [`ConnectorMetadataService`](../flytekit.extend.backend.connector_service/connectormetadataservice) |  |
| [`SyncConnectorService`](../flytekit.extend.backend.connector_service/syncconnectorservice) |  |

### Methods

| Method | Description |
|-|-|
| [`record_connector_metrics()`](#record_connector_metrics) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `create_operation` | `str` |  |
| `delete_operation` | `str` |  |
| `do_operation` | `str` |  |
| `get_operation` | `str` |  |
| `metric_prefix` | `str` |  |

## Methods

#### record_connector_metrics()

```python
def record_connector_metrics(
    func: typing.Callable,
)
```
| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable` | |

