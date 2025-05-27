---
title: flytekit.core.resources
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.resources

## Directory

### Classes

| Class | Description |
|-|-|
| [`ResourceSpec`](.././flytekit.core.resources#flytekitcoreresourcesresourcespec) |  |
| [`Resources`](.././flytekit.core.resources#flytekitcoreresourcesresources) | This class is used to specify both resource requests and resource limits. |

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
    accelerator: typing.Optional[flytekit.extras.accelerators.BaseAccelerator],
    shared_memory: typing.Union[typing.Literal[True], str, NoneType],
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Convert public extended resources to idl.



| Parameter | Type |
|-|-|
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` |

#### convert_resources_to_resource_model()

```python
def convert_resources_to_resource_model(
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
) -> n: The given resources as requests and limits
```
Convert flytekit ``Resources`` objects to a Resources model



| Parameter | Type |
|-|-|
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |

#### pod_spec_from_resources()

```python
def pod_spec_from_resources(
    primary_container_name: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    k8s_gpu_resource_key: str,
) -> V1PodSpec
```
| Parameter | Type |
|-|-|
| `primary_container_name` | `typing.Optional[str]` |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |
| `k8s_gpu_resource_key` | `str` |

## flytekit.core.resources.ResourceSpec

```python
class ResourceSpec(
    requests: flytekit.core.resources.Resources,
    limits: flytekit.core.resources.Resources,
)
```
| Parameter | Type |
|-|-|
| `requests` | `flytekit.core.resources.Resources` |
| `limits` | `flytekit.core.resources.Resources` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_multiple_resource()`](#from_multiple_resource) | Convert Resources that represent both a requests and limits into a ResourceSpec. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### from_multiple_resource()

```python
def from_multiple_resource(
    resource: flytekit.core.resources.Resources,
) -> ResourceSpec
```
Convert Resources that represent both a requests and limits into a ResourceSpec.


| Parameter | Type |
|-|-|
| `resource` | `flytekit.core.resources.Resources` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

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

Please see the :std:ref:`User Guide <cookbook:customizing task resources>` for detailed examples.
Also refer to the [`K8s conventions.`](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes)


```python
class Resources(
    cpu: typing.Union[str, int, float, list, tuple, NoneType],
    mem: typing.Union[str, int, list, tuple, NoneType],
    gpu: typing.Union[str, int, list, tuple, NoneType],
    ephemeral_storage: typing.Union[str, int, NoneType],
)
```
| Parameter | Type |
|-|-|
| `cpu` | `typing.Union[str, int, float, list, tuple, NoneType]` |
| `mem` | `typing.Union[str, int, list, tuple, NoneType]` |
| `gpu` | `typing.Union[str, int, list, tuple, NoneType]` |
| `ephemeral_storage` | `typing.Union[str, int, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

