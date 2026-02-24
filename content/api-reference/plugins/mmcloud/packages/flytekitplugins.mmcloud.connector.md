---
title: flytekitplugins.mmcloud.connector
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.mmcloud.connector

## Directory

### Classes

| Class | Description |
|-|-|
| [`MMCloudConnector`](.././flytekitplugins.mmcloud.connector#flytekitpluginsmmcloudconnectormmcloudconnector) |  |
| [`MMCloudMetadata`](.././flytekitplugins.mmcloud.connector#flytekitpluginsmmcloudconnectormmcloudmetadata) |  |

## flytekitplugins.mmcloud.connector.MMCloudConnector

```python
def MMCloudConnector()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` | `None` |  |
| `task_category` | `None` | task category that the connector supports |

### Methods

| Method | Description |
|-|-|
| [`async_login()`](#async_login) | Log in to Memory Machine Cloud OpCenter. |
| [`create()`](#create) | Submit a Flyte task as MMCloud job to the OpCenter, and return the job UID for the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs on success. |
| [`get_logs()`](#get_logs) | Return the metrics for the task. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


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
) -> flytekitplugins.mmcloud.connector.MMCloudMetadata
```
Submit a Flyte task as MMCloud job to the OpCenter, and return the job UID for the task.


| Parameter | Type | Description |
|-|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` | |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `kwargs` | `**kwargs` | |

#### delete()

```python
def delete(
    resource_meta: flytekitplugins.mmcloud.connector.MMCloudMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.mmcloud.connector.MMCloudMetadata` | |
| `kwargs` | `**kwargs` | |

#### get()

```python
def get(
    resource_meta: flytekitplugins.mmcloud.connector.MMCloudMetadata,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs on success.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekitplugins.mmcloud.connector.MMCloudMetadata` | |
| `kwargs` | `**kwargs` | |

#### get_logs()

```python
def get_logs(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

#### get_metrics()

```python
def get_metrics(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type | Description |
|-|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` | |
| `kwargs` | `**kwargs` | |

## flytekitplugins.mmcloud.connector.MMCloudMetadata

```python
class MMCloudMetadata(
    job_id: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `job_id` | `str` | |

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


| Parameter | Type | Description |
|-|-|-|
| `data` | `bytes` | |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


