---
title: flytekitplugins.mmcloud.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.mmcloud.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`MMCloudAgent`](.././flytekitplugins.mmcloud.agent#flytekitpluginsmmcloudagentmmcloudagent) | This is the base class for all async agents. |
| [`MMCloudMetadata`](.././flytekitplugins.mmcloud.agent#flytekitpluginsmmcloudagentmmcloudmetadata) |  |

## flytekitplugins.mmcloud.agent.MMCloudAgent

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def MMCloudAgent()
```
### Methods

| Method | Description |
|-|-|
| [`async_login()`](#async_login) | Log in to Memory Machine Cloud OpCenter. |
| [`create()`](#create) | Submit a Flyte task as MMCloud job to the OpCenter, and return the job UID for the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs on success. |


#### async_login()

```python
def async_login()
```
Log in to Memory Machine Cloud OpCenter.


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
) -> flytekitplugins.mmcloud.agent.MMCloudMetadata
```
Submit a Flyte task as MMCloud job to the OpCenter, and return the job UID for the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.mmcloud.agent.MMCloudMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.mmcloud.agent.MMCloudMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.mmcloud.agent.MMCloudMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs on success.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.mmcloud.agent.MMCloudMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.mmcloud.agent.MMCloudMetadata

```python
class MMCloudMetadata(
    job_id: str,
)
```
| Parameter | Type |
|-|-|
| `job_id` | `str` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


#### decode()

```python
def decode(
    data: bytes,
) -> ResourceMeta
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


