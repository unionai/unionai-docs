---
title: flyte.extend
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
sidebar_expanded: true
---

# flyte.extend

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncFunctionTaskTemplate`](../flyte.extend/asyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |
| [`ImageBuildEngine`](../flyte.extend/imagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
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
| [`get_proto_resources()`](#get_proto_resources) | Get main resources IDL representation from the resources object. |
| [`is_initialized()`](#is_initialized) | Check if the system has been initialized. |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |
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
.. code-block:: python
    from flytekit.lazy_import import lazy_module
    sklearn = lazy_module("sklearn")
    sklearn.svm.SVC()


| Parameter | Type | Description |
|-|-|-|
| `fullname` |  | |

#### pod_spec_from_resources()

```python
def pod_spec_from_resources(
    primary_container_name: str,
    requests: typing.Optional[flyte._resources.Resources],
    limits: typing.Optional[flyte._resources.Resources],
    k8s_gpu_resource_key: str,
) -> V1PodSpec
```
| Parameter | Type | Description |
|-|-|-|
| `primary_container_name` | `str` | |
| `requests` | `typing.Optional[flyte._resources.Resources]` | |
| `limits` | `typing.Optional[flyte._resources.Resources]` | |
| `k8s_gpu_resource_key` | `str` | |

