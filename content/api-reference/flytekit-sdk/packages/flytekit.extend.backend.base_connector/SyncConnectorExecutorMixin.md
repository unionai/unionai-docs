---
title: SyncConnectorExecutorMixin
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SyncConnectorExecutorMixin

**Package:** `flytekit.extend.backend.base_connector`

This mixin class is used to run the sync task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the connector.

Synchronous tasks run quickly and can return their results instantly.
Sending a prompt to ChatGPT and getting a response, or retrieving some metadata from a backend system.


## Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) |  |


### execute()

```python
def execute(
    kwargs,
) -> flytekit.models.literals.LiteralMap
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

