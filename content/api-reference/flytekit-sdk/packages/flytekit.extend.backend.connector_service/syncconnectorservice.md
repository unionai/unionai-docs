---
title: SyncConnectorService
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SyncConnectorService

**Package:** `flytekit.extend.backend.connector_service`

## Methods

| Method | Description |
|-|-|
| [`ExecuteTaskSync()`](#executetasksync) | ExecuteTaskSync streams the create request and inputs to the agent service and streams the outputs back. |


### ExecuteTaskSync()

```python
def ExecuteTaskSync(
    request_iterator: typing.AsyncIterator[flyteidl.admin.agent_pb2.ExecuteTaskSyncRequest],
    context: grpc.ServicerContext,
) -> typing.AsyncIterator[flyteidl.admin.agent_pb2.ExecuteTaskSyncResponse]
```
ExecuteTaskSync streams the create request and inputs to the agent service and streams the outputs back.
        


| Parameter | Type | Description |
|-|-|-|
| `request_iterator` | `typing.AsyncIterator[flyteidl.admin.agent_pb2.ExecuteTaskSyncRequest]` | |
| `context` | `grpc.ServicerContext` | |

