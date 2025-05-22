---
title: flytekitplugins.openai.batch.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.openai.batch.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`BatchEndpointAgent`](.././flytekitplugins.openai.batch.agent#flytekitpluginsopenaibatchagentbatchendpointagent) | This is the base class for all async agents. |
| [`BatchEndpointMetadata`](.././flytekitplugins.openai.batch.agent#flytekitpluginsopenaibatchagentbatchendpointmetadata) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `OPENAI_API_KEY` | `str` |  |

## flytekitplugins.openai.batch.agent.BatchEndpointAgent

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def BatchEndpointAgent()
```
### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases. |


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekitplugins.openai.batch.agent.BatchEndpointMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.openai.batch.agent.BatchEndpointMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.openai.batch.agent.BatchEndpointMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.openai.batch.agent.BatchEndpointMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.openai.batch.agent.BatchEndpointMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.openai.batch.agent.BatchEndpointMetadata

```python
class BatchEndpointMetadata(
    openai_org: str,
    batch_id: str,
)
```
| Parameter | Type |
|-|-|
| `openai_org` | `str` |
| `batch_id` | `str` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


#### decode()

```python
def decode(
    data: bytes,
) -> BatchEndpointMetadata
```
Decode the resource meta from bytes.


| Parameter | Type |
|-|-|
| `data` | `bytes` |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


