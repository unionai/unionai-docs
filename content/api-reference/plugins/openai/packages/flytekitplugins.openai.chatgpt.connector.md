---
title: flytekitplugins.openai.chatgpt.connector
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.openai.chatgpt.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`ChatGPTConnector`](.././flytekitplugins.openai.chatgpt.connector#flytekitpluginsopenaichatgptconnectorchatgptconnector) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `OPENAI_API_KEY` | `str` |  |
| `TIMEOUT_SECONDS` | `int` |  |

## flytekitplugins.openai.chatgpt.connector.ChatGPTConnector

```python
def ChatGPTConnector()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `task_category` | `None` | task category that the connector supports |

### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This is the method that the connector will run. |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
This is the method that the connector will run.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `kwargs` | `**kwargs` | |

