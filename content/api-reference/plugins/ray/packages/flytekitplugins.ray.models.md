---
title: flytekitplugins.ray.models
version: 0.0.0+develop
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
| Parameter | Type |
|-|-|
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` |
| `k8s_pod` | `typing.Optional[flytekit.models.task.K8sPod]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: HeadGroupSpec
```
| Parameter | Type |
|-|-|
| `proto` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `k8s_pod` |  | {{< multiline >}}Additional pod specs for the head node pod.
:rtype: K8sPod
{{< /multiline >}} |
| `ray_start_params` |  | {{< multiline >}}The ray start params of head node group.
:rtype: typing.Dict[str, str]
{{< /multiline >}} |

## flytekitplugins.ray.models.RayCluster

Define RayCluster spec that will be used by KubeRay to launch the cluster.


```python
class RayCluster(
    worker_group_spec: typing.List[flytekitplugins.ray.models.WorkerGroupSpec],
    head_group_spec: typing.Optional[flytekitplugins.ray.models.HeadGroupSpec],
    enable_autoscaling: bool,
)
```
| Parameter | Type |
|-|-|
| `worker_group_spec` | `typing.List[flytekitplugins.ray.models.WorkerGroupSpec]` |
| `head_group_spec` | `typing.Optional[flytekitplugins.ray.models.HeadGroupSpec]` |
| `enable_autoscaling` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: RayCluster
```
| Parameter | Type |
|-|-|
| `proto` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `enable_autoscaling` |  | {{< multiline >}}Whether to enable autoscaling.
:rtype: bool
{{< /multiline >}} |
| `head_group_spec` |  | {{< multiline >}}The head group configuration.
:rtype: HeadGroupSpec
{{< /multiline >}} |
| `is_empty` |  |  |
| `worker_group_spec` |  | {{< multiline >}}The worker group configurations.
:rtype: typing.List[WorkerGroupSpec]
{{< /multiline >}} |

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
| Parameter | Type |
|-|-|
| `ray_cluster` | `flytekitplugins.ray.models.RayCluster` |
| `runtime_env` | `typing.Optional[str]` |
| `runtime_env_yaml` | `typing.Optional[str]` |
| `ttl_seconds_after_finished` | `typing.Optional[int]` |
| `shutdown_after_job_finishes` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.plugins.ray_pb2.RayJob,
)
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.plugins.ray_pb2.RayJob` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `ray_cluster` |  |  |
| `runtime_env` |  |  |
| `runtime_env_yaml` |  |  |
| `shutdown_after_job_finishes` |  |  |
| `ttl_seconds_after_finished` |  |  |

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
| Parameter | Type |
|-|-|
| `group_name` | `str` |
| `replicas` | `int` |
| `min_replicas` | `typing.Optional[int]` |
| `max_replicas` | `typing.Optional[int]` |
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` |
| `k8s_pod` | `typing.Optional[flytekit.models.task.K8sPod]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: WorkerGroupSpec
```
| Parameter | Type |
|-|-|
| `proto` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `group_name` |  | {{< multiline >}}Group name of the current worker group.
:rtype: str
{{< /multiline >}} |
| `is_empty` |  |  |
| `k8s_pod` |  | {{< multiline >}}Additional pod specs for the worker node pods.
:rtype: K8sPod
{{< /multiline >}} |
| `max_replicas` |  | {{< multiline >}}Max replicas of the worker group.
:rtype: int
{{< /multiline >}} |
| `min_replicas` |  | {{< multiline >}}Min replicas of the worker group.
:rtype: int
{{< /multiline >}} |
| `ray_start_params` |  | {{< multiline >}}The ray start params of worker node group.
:rtype: typing.Dict[str, str]
{{< /multiline >}} |
| `replicas` |  | {{< multiline >}}Desired replicas of the worker group.
:rtype: int
{{< /multiline >}} |

