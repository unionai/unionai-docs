---
title: flytekitplugins.ray.models
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.ray.models

## Directory

### Classes

| Class | Description |
|-|-|
| [`HeadGroupSpec`](.././flytekitplugins.ray.models#flytekitpluginsraymodelsheadgroupspec) |  |
| [`RayCluster`](.././flytekitplugins.ray.models#flytekitpluginsraymodelsraycluster) | Define RayCluster spec that will be used by KubeRay to launch the cluster. |
| [`RayJob`](.././flytekitplugins.ray.models#flytekitpluginsraymodelsrayjob) | Models _ray_pb2. |
| [`WorkerGroupSpec`](.././flytekitplugins.ray.models#flytekitpluginsraymodelsworkergroupspec) |  |

## flytekitplugins.ray.models.HeadGroupSpec

```python
class HeadGroupSpec(
    ray_start_params: typing.Optional[typing.Dict[str, str]],
    k8s_pod: typing.Optional[flytekit.models.task.K8sPod],
)
```
| Parameter | Type | Description |
|-|-|-|
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` | |
| `k8s_pod` | `typing.Optional[flytekit.models.task.K8sPod]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `k8s_pod` | `None` | Additional pod specs for the head node pod. :rtype: K8sPod |
| `ray_start_params` | `None` | The ray start params of head node group. :rtype: typing.Dict[str, str] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.plugins._ray_pb2.HeadGroupSpec


## flytekitplugins.ray.models.RayCluster

Define RayCluster spec that will be used by KubeRay to launch the cluster.



```python
class RayCluster(
    worker_group_spec: typing.List[flytekitplugins.ray.models.WorkerGroupSpec],
    head_group_spec: typing.Optional[flytekitplugins.ray.models.HeadGroupSpec],
    enable_autoscaling: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `worker_group_spec` | `typing.List[flytekitplugins.ray.models.WorkerGroupSpec]` | |
| `head_group_spec` | `typing.Optional[flytekitplugins.ray.models.HeadGroupSpec]` | |
| `enable_autoscaling` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `enable_autoscaling` | `None` | Whether to enable autoscaling. :rtype: bool |
| `head_group_spec` | `None` | The head group configuration. :rtype: HeadGroupSpec |
| `is_empty` | `None` |  |
| `worker_group_spec` | `None` | The worker group configurations. :rtype: typing.List[WorkerGroupSpec] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.plugins._ray_pb2.RayCluster


## flytekitplugins.ray.models.RayJob

Models _ray_pb2.RayJob



```python
class RayJob(
    ray_cluster: flytekitplugins.ray.models.RayCluster,
    runtime_env: typing.Optional[str],
    runtime_env_yaml: typing.Optional[str],
    ttl_seconds_after_finished: typing.Optional[int],
    shutdown_after_job_finishes: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ray_cluster` | `flytekitplugins.ray.models.RayCluster` | |
| `runtime_env` | `typing.Optional[str]` | |
| `runtime_env_yaml` | `typing.Optional[str]` | |
| `ttl_seconds_after_finished` | `typing.Optional[int]` | |
| `shutdown_after_job_finishes` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `ray_cluster` | `None` |  |
| `runtime_env` | `None` |  |
| `runtime_env_yaml` | `None` |  |
| `shutdown_after_job_finishes` | `None` |  |
| `ttl_seconds_after_finished` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.plugins.ray_pb2.RayJob,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.plugins.ray_pb2.RayJob` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekitplugins.ray.models.WorkerGroupSpec

```python
class WorkerGroupSpec(
    group_name: str,
    replicas: int,
    min_replicas: typing.Optional[int],
    max_replicas: typing.Optional[int],
    ray_start_params: typing.Optional[typing.Dict[str, str]],
    k8s_pod: typing.Optional[flytekit.models.task.K8sPod],
)
```
| Parameter | Type | Description |
|-|-|-|
| `group_name` | `str` | |
| `replicas` | `int` | |
| `min_replicas` | `typing.Optional[int]` | |
| `max_replicas` | `typing.Optional[int]` | |
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` | |
| `k8s_pod` | `typing.Optional[flytekit.models.task.K8sPod]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `group_name` | `None` | Group name of the current worker group. :rtype: str |
| `is_empty` | `None` |  |
| `k8s_pod` | `None` | Additional pod specs for the worker node pods. :rtype: K8sPod |
| `max_replicas` | `None` | Max replicas of the worker group. :rtype: int |
| `min_replicas` | `None` | Min replicas of the worker group. :rtype: int |
| `ray_start_params` | `None` | The ray start params of worker node group. :rtype: typing.Dict[str, str] |
| `replicas` | `None` | Desired replicas of the worker group. :rtype: int |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.plugins._ray_pb2.WorkerGroupSpec


