---
title: ConnectorMetadataService
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConnectorMetadataService

**Package:** `flytekit.extend.backend.connector_service`

## Methods

| Method | Description |
|-|-|
| [`GetAgent()`](#getagent) | Fetch a :ref:`ref_flyteidl. |
| [`ListAgents()`](#listagents) | Fetch a list of :ref:`ref_flyteidl. |


### GetAgent()

```python
def GetAgent(
    request: flyteidl.admin.agent_pb2.GetAgentRequest,
    context: grpc.ServicerContext,
) -> flyteidl.admin.agent_pb2.GetAgentResponse
```
Fetch a :ref:`ref_flyteidl.admin.Agent` definition.
        


| Parameter | Type | Description |
|-|-|-|
| `request` | `flyteidl.admin.agent_pb2.GetAgentRequest` | |
| `context` | `grpc.ServicerContext` | |

### ListAgents()

```python
def ListAgents(
    request: flyteidl.admin.agent_pb2.ListAgentsRequest,
    context: grpc.ServicerContext,
) -> flyteidl.admin.agent_pb2.ListAgentsResponse
```
Fetch a list of :ref:`ref_flyteidl.admin.Agent` definitions.
        


| Parameter | Type | Description |
|-|-|-|
| `request` | `flyteidl.admin.agent_pb2.ListAgentsRequest` | |
| `context` | `grpc.ServicerContext` | |

