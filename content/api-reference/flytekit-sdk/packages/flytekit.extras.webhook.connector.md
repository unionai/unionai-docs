---
title: flytekit.extras.webhook.connector
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.webhook.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`WebhookConnector`](.././flytekit.extras.webhook.connector#flytekitextraswebhookconnectorwebhookconnector) | WebhookConnector is responsible for handling webhook tasks. |

### Variables

| Property | Type | Description |
|-|-|-|
| `DATA_KEY` | `str` |  |
| `HEADERS_KEY` | `str` |  |
| `METHOD_KEY` | `str` |  |
| `SHOW_DATA_KEY` | `str` |  |
| `SHOW_URL_KEY` | `str` |  |
| `TASK_TYPE` | `str` |  |
| `TIMEOUT_SEC` | `str` |  |
| `URL_KEY` | `str` |  |

## flytekit.extras.webhook.connector.WebhookConnector

WebhookConnector is responsible for handling webhook tasks.

This connector sends HTTP requests based on the task template and inputs provided,
and processes the responses to determine the success or failure of the task.



```python
class WebhookConnector(
    client: typing.Optional[httpx.AsyncClient],
)
```
| Parameter | Type | Description |
|-|-|-|
| `client` | `typing.Optional[httpx.AsyncClient]` | An optional HTTP client to use for sending requests. |

### Properties

| Property | Type | Description |
|-|-|-|
| `task_category` | `None` | task category that the connector supports |

### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This method processes the webhook task and sends an HTTP request. |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
This method processes the webhook task and sends an HTTP request.

It uses asyncio to send the request and process the response using the httpx library.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `output_prefix` | `str` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `kwargs` | `**kwargs` | |

