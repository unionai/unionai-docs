---
title: flytekit.core.resources
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.core.resources

## Directory

### Classes

| Class | Description |
|-|-|
| [`ResourceSpec`](./flytekit.core.resources#flytekitcoreresourcesresourcespec) |  |
| [`Resources`](./flytekit.core.resources#flytekitcoreresourcesresources) | This class is used to specify both resource requests and resource limits. |

### Methods

| Method | Description |
|-|-|
| [`construct_extended_resources()`](#construct_extended_resources) | Convert public extended resources to idl. |
| [`convert_resources_to_resource_model()`](#convert_resources_to_resource_model) | Convert flytekit ``Resources`` objects to a Resources model. |
| [`pod_spec_from_resources()`](#pod_spec_from_resources) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `SHARED_MEMORY_MOUNT_NAME` | `str` |  |
| `SHARED_MEMORY_MOUNT_PATH` | `str` |  |
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### construct_extended_resources()

```python
def construct_extended_resources(
    accelerator: typing.Optional[flytekit.extras.accelerators.BaseAccelerator] = None,
    shared_memory: typing.Union[typing.Literal[True], str, NoneType] = None,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Convert public extended resources to idl.



| Parameter | Type | Description |
|-|-|-|
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` | The accelerator to use for this task. |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | If True, then shared memory will be attached to the container where the size is equal to the allocated memory. If str, then the shared memory is set to that size. |

#### convert_resources_to_resource_model()

```python
def convert_resources_to_resource_model(
    requests: typing.Optional[flytekit.core.resources.Resources] = None,
    limits: typing.Optional[flytekit.core.resources.Resources] = None,
) -> flytekit.models.task.Resources
```
Convert flytekit ``Resources`` objects to a Resources model



| Parameter | Type | Description |
|-|-|-|
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | Resource requests. Optional, defaults to ``None`` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | Resource limits. Optional, defaults to ``None`` |

**Returns:** The given resources as requests and limits

#### pod_spec_from_resources()

```python
def pod_spec_from_resources(
    primary_container_name: typing.Optional[str] = None,
    requests: typing.Optional[flytekit.core.resources.Resources] = None,
    limits: typing.Optional[flytekit.core.resources.Resources] = None,
    k8s_gpu_resource_key: str = 'nvidia.com/gpu',
) -> V1PodSpec
```
| Parameter | Type | Description |
|-|-|-|
| `primary_container_name` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `k8s_gpu_resource_key` | `str` | |

## flytekit.core.resources.ResourceSpec

### Parameters

```python
class ResourceSpec(
    requests: flytekit.core.resources.Resources,
    limits: flytekit.core.resources.Resources,
)
```
| Parameter | Type | Description |
|-|-|-|
| `requests` | `flytekit.core.resources.Resources` | |
| `limits` | `flytekit.core.resources.Resources` | |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_multiple_resource()`](#from_multiple_resource) | Convert Resources that represent both a requests and limits into a ResourceSpec. |
| [`to_dict()`](#to_dict) |  |


#### from_dict()

```python
def from_dict(
    d,
    dialect = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

#### from_multiple_resource()

```python
def from_multiple_resource(
    resource: flytekit.core.resources.Resources,
) -> ResourceSpec
```
Convert Resources that represent both a requests and limits into a ResourceSpec.


| Parameter | Type | Description |
|-|-|-|
| `resource` | `flytekit.core.resources.Resources` | |

#### to_dict()

```python
def to_dict()
```
## flytekit.core.resources.Resources

This class is used to specify both resource requests and resource limits.

```python
Resources(cpu="1", mem="2048")  # This is 1 CPU and 2 KB of memory
Resources(cpu="100m", mem="2Gi")  # This is 1/10th of a CPU and 2 gigabytes of memory
Resources(cpu=0.5, mem=1024) # This is 500m CPU and 1 KB of memory

# For Kubernetes-based tasks, pods use ephemeral local storage for scratch space, caching, and for logs.
# This allocates 1Gi of such local storage.
Resources(ephemeral_storage="1Gi")
```
When used together with `@task(resources=)`, you a specific the request and limits with one object.
When the value is set to a tuple or list, the first value is the request and the
second value is the limit. If the value is a single value, then both the requests and limit is
set to that value. For example, the `Resource(cpu=("1", "2"), mem=1024)` will set the cpu request to 1, cpu limit to 2,
mem limit and request to 1024.

> [!NOTE]
> Persistent storage is not currently supported on the Flyte backend.

Please see the `User Guide` for detailed examples.
Also refer to the [`K8s conventions.`](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes)


### Parameters

```python
class Resources(
    cpu: typing.Union[str, int, float, list, tuple, NoneType] = None,
    mem: typing.Union[str, int, list, tuple, NoneType] = None,
    gpu: typing.Union[str, int, list, tuple, NoneType] = None,
    ephemeral_storage: typing.Union[str, int, NoneType] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cpu` | `typing.Union[str, int, float, list, tuple, NoneType]` | |
| `mem` | `typing.Union[str, int, list, tuple, NoneType]` | |
| `gpu` | `typing.Union[str, int, list, tuple, NoneType]` | |
| `ephemeral_storage` | `typing.Union[str, int, NoneType]` | |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`to_dict()`](#to_dict) |  |


#### from_dict()

```python
def from_dict(
    d,
    dialect = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

#### to_dict()

```python
def to_dict()
```
