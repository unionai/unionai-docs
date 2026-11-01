---
title: flyte.extend
icon: box-seam
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# flyte.extend

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncFunctionTaskTemplate`](../flyte.extend/asyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |
| [`ImageBuildEngine`](../flyte.extend/imagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`RuntimeTaskTemplate`](../flyte.extend/runtimetasktemplate) | Task template for Python-runtime tasks that execute through the Flyte task entrypoint. |
| [`SessionAddress`](../flyte.extend/sessionaddress) | Where a session can be reached, as its worker reported it. |
| [`SessionRoutingInfo`](../flyte.extend/sessionroutinginfo) | Where in the platform a session is served: the pod its worker serves it from, and the cluster. |
| [`TaskTemplate`](../flyte.extend/tasktemplate) | Task template is a template for a task that can be executed. |

### Protocols

| Protocol | Description |
|-|-|
| [`ImageBuilder`](../flyte.extend/imagebuilder) |  |
| [`ImageChecker`](../flyte.extend/imagechecker) |  |

### Methods

| Method | Description |
|-|-|
| [`download_code_bundle()`](#download_code_bundle) | Downloads the code bundle if it is not already downloaded. |
| [`get_proto_extended_resources()`](#get_proto_extended_resources) | TODO Implement partitioning logic string handling for GPU. |
| [`get_proto_resources()`](#get_proto_resources) | Get main resources IDL representation from the resources object. |
| [`is_initialized()`](#is_initialized) | Check if the system has been initialized. |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |
| [`new_session()`](#new_session) | Start a session as a child action of the running task. |
| [`pod_spec_from_resources()`](#pod_spec_from_resources) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `PRIMARY_CONTAINER_DEFAULT_NAME` | `str` |  |
| `TaskPluginRegistry` | `_Registry` |  |

## Methods

#### download_code_bundle()

```python
def download_code_bundle(
    code_bundle: flyte.models.CodeBundle,
) -> flyte.models.CodeBundle
```
Downloads the code bundle if it is not already downloaded.



| Parameter | Type | Description |
|-|-|-|
| `code_bundle` | `flyte.models.CodeBundle` | The code bundle to download. |

**Returns:** The code bundle with the downloaded path.

#### get_proto_extended_resources()

```python
def get_proto_extended_resources(
    resources: flyte._resources.Resources | None,
) -> typing.Optional[flyteidl2.core.tasks_pb2.ExtendedResources]
```
TODO Implement partitioning logic string handling for GPU



| Parameter | Type | Description |
|-|-|-|
| `resources` | `flyte._resources.Resources \| None` | |

#### get_proto_resources()

```python
def get_proto_resources(
    resources: flyte._resources.Resources | None,
) -> typing.Optional[flyteidl2.core.tasks_pb2.Resources]
```
Get main resources IDL representation from the resources object



| Parameter | Type | Description |
|-|-|-|
| `resources` | `flyte._resources.Resources \| None` | User facing Resources object containing potentially both requests and limits |

**Returns:** The given resources as requests and limits

#### is_initialized()

```python
def is_initialized()
```
Check if the system has been initialized.



**Returns:** True if initialized, False otherwise

#### lazy_module()

```python
def lazy_module(
    fullname,
)
```
This function is used to lazily import modules.  It is used in the following way:

```python
from flyte._utils.lazy_module import lazy_module

sklearn = lazy_module("sklearn")
sklearn.svm.SVC()
```



| Parameter | Type | Description |
|-|-|-|
| `fullname` |  | The full name of the module to import |

#### new_session()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await new_session.aio()`.
```python
def new_session(
    name: str,
    task: TaskTemplate,
    ready_timeout: float = 30.0,
    queue: Optional[str] = None,
) -> _Session
```
Start a session as a child action of the running task. Returns once it is enqueued; call `wait` for its
address.

Warning: Experimental feature: alpha — APIs may change without notice.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the session. |
| `task` | `TaskTemplate` | The task the session runs. |
| `ready_timeout` | `float` | Seconds `wait` allows for the session to become addressable. |
| `queue` | `Optional[str]` | Optional queue to run the session in. |

**Raises**

| Exception | Description |
|-|-|
| `RuntimeError` | Outside a task. |

#### pod_spec_from_resources()

```python
def pod_spec_from_resources(
    primary_container_name: str = 'primary',
    requests: typing.Optional[flyte._resources.Resources] = None,
    limits: typing.Optional[flyte._resources.Resources] = None,
    k8s_gpu_resource_key: str = 'nvidia.com/gpu',
) -> V1PodSpec
```
| Parameter | Type | Description |
|-|-|-|
| `primary_container_name` | `str` | |
| `requests` | `typing.Optional[flyte._resources.Resources]` | |
| `limits` | `typing.Optional[flyte._resources.Resources]` | |
| `k8s_gpu_resource_key` | `str` | |

