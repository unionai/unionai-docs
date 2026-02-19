---
title: flytekit.core.resources
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.resources

## Directory

### Classes

| Class | Description |
|-|-|
| [`ResourceSpec`](../flytekit.core.resources/resourcespec) |  |
| [`Resources`](../flytekit.core.resources/resources) | This class is used to specify both resource requests and resource limits. |

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



| Parameter | Type | Description |
|-|-|-|
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` | The accelerator to use for this task. |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | If True, then shared memory will be attached to the container where the size is equal to the allocated memory. If str, then the shared memory is set to that size. |

#### convert_resources_to_resource_model()

```python
def convert_resources_to_resource_model(
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
) -> flytekit.models.task.Resources
```
Convert flytekit ``Resources`` objects to a Resources model



| Parameter | Type | Description |
|-|-|-|
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | Resource requests. Optional, defaults to ``None`` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | Resource limits. Optional, defaults to ``None`` :return: The given resources as requests and limits |

#### pod_spec_from_resources()

```python
def pod_spec_from_resources(
    primary_container_name: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    k8s_gpu_resource_key: str,
) -> V1PodSpec
```
| Parameter | Type | Description |
|-|-|-|
| `primary_container_name` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `k8s_gpu_resource_key` | `str` | |

