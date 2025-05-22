---
title: flytekitplugins.spark.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.spark.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`DatabricksAgent`](.././flytekitplugins.spark.agent#flytekitpluginssparkagentdatabricksagent) | This is the base class for all async agents. |
| [`DatabricksAgentV2`](.././flytekitplugins.spark.agent#flytekitpluginssparkagentdatabricksagentv2) | Add DatabricksAgentV2 to support running the k8s spark and databricks spark together in the same workflow. |
| [`DatabricksJobMetadata`](.././flytekitplugins.spark.agent#flytekitpluginssparkagentdatabricksjobmetadata) |  |

### Methods

| Method | Description |
|-|-|
| [`get_header()`](#get_header) |  |
| [`result_state_is_available()`](#result_state_is_available) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `DATABRICKS_API_ENDPOINT` | `str` |  |
| `DEFAULT_DATABRICKS_INSTANCE_ENV_KEY` | `str` |  |
| `FLYTE_FAIL_ON_ERROR` | `str` |  |

## Methods

#### get_header()

```python
def get_header()
```
#### result_state_is_available()

```python
def result_state_is_available(
    life_cycle_state: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `life_cycle_state` | `str` |

## flytekitplugins.spark.agent.DatabricksAgent

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def DatabricksAgent()
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
) -> flytekitplugins.spark.agent.DatabricksJobMetadata
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
    resource_meta: flytekitplugins.spark.agent.DatabricksJobMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.spark.agent.DatabricksJobMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.spark.agent.DatabricksJobMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.spark.agent.DatabricksJobMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.spark.agent.DatabricksAgentV2

Add DatabricksAgentV2 to support running the k8s spark and databricks spark together in the same workflow.
This is necessary because one task type can only be handled by a single backend plugin.

spark -> k8s spark plugin
databricks -> databricks agent


```python
def DatabricksAgentV2()
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
) -> flytekitplugins.spark.agent.DatabricksJobMetadata
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
    resource_meta: flytekitplugins.spark.agent.DatabricksJobMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.spark.agent.DatabricksJobMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.spark.agent.DatabricksJobMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.spark.agent.DatabricksJobMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.spark.agent.DatabricksJobMetadata

```python
class DatabricksJobMetadata(
    databricks_instance: str,
    run_id: str,
)
```
| Parameter | Type |
|-|-|
| `databricks_instance` | `str` |
| `run_id` | `str` |

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


