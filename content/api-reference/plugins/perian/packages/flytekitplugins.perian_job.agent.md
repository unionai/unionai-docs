---
title: flytekitplugins.perian_job.agent
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.perian_job.agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`PerianAgent`](.././flytekitplugins.perian_job.agent#flytekitpluginsperian_jobagentperianagent) | Flyte Agent for executing tasks on PERIAN Job Platform. |
| [`PerianMetadata`](.././flytekitplugins.perian_job.agent#flytekitpluginsperian_jobagentperianmetadata) | Metadata for PERIAN jobs. |

### Variables

| Property | Type | Description |
|-|-|-|
| `PERIAN_API_URL` | `str` |  |

## flytekitplugins.perian_job.agent.PerianAgent

Flyte Agent for executing tasks on PERIAN Job Platform


```python
def PerianAgent()
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
    output_prefix: typing.Optional[str],
    kwargs,
) -> flytekitplugins.perian_job.agent.PerianMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `output_prefix` | `typing.Optional[str]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.perian_job.agent.PerianMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.perian_job.agent.PerianMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekitplugins.perian_job.agent.PerianMetadata,
    kwargs,
) -> flytekit.extend.backend.base_agent.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekitplugins.perian_job.agent.PerianMetadata` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the agent supports
{{< /multiline >}} |

## flytekitplugins.perian_job.agent.PerianMetadata

Metadata for PERIAN jobs


```python
class PerianMetadata(
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


