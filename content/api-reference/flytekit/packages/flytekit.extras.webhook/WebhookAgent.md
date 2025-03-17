---
title: WebhookAgent
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# WebhookAgent

**Package:** `flytekit.extras.webhook`

WebhookAgent is responsible for handling webhook tasks.

This agent sends HTTP requests based on the task template and inputs provided,
and processes the responses to determine the success or failure of the task.



```python
def WebhookAgent(
    client: typing.Optional[httpx.AsyncClient],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `client` | `typing.Optional[httpx.AsyncClient]` |
## Methods

### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
):
```
This method processes the webhook task and sends an HTTP request.

It uses asyncio to send the request and process the response using the httpx library.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |
