---
title: flytekit.core.node
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.node

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.core.node#flytekitcorenodeany) | Special type indicating an unconstrained type. |
| [`BaseAccelerator`](.././flytekit.core.node#flytekitcorenodebaseaccelerator) | Base class for all accelerator types. |
| [`Node`](.././flytekit.core.node#flytekitcorenodenode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`PodTemplate`](.././flytekit.core.node#flytekitcorenodepodtemplate) | Custom PodTemplate specification for a Task. |
| [`ResourceSpec`](.././flytekit.core.node#flytekitcorenoderesourcespec) | None. |
| [`Resources`](.././flytekit.core.node#flytekitcorenoderesources) | This class is used to specify both resource requests and resource limits. |

## flytekit.core.node.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.node.BaseAccelerator

Base class for all accelerator types. This class is not meant to be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.core.node.Node

This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like
ID, which from the registration step


```python
def Node(
    id: str,
    metadata: _workflow_model.NodeMetadata,
    bindings: List[_literal_models.Binding],
    upstream_nodes: List[Node],
    flyte_entity: Any,
):
```
| Parameter | Type |
|-|-|
| `id` | `str` |
| `metadata` | `_workflow_model.NodeMetadata` |
| `bindings` | `List[_literal_models.Binding]` |
| `upstream_nodes` | `List[Node]` |
| `flyte_entity` | `Any` |

### Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is typically something we shouldn't do |
| [`with_overrides()`](#with_overrides) | None |


#### runs_before()

```python
def runs_before(
    other: Node,
):
```
This is typically something we shouldn't do. This modifies an attribute of the other instance rather than
self. But it's done so only because we wanted this English function to be the same as the shift function.
That is, calling node_1.runs_before(node_2) and node_1 >> node_2 are the same. The shift operator going the
other direction is not implemented to further avoid confusion. Right shift was picked rather than left shift
because that's what most users are familiar with.


| Parameter | Type |
|-|-|
| `other` | `Node` |

#### with_overrides()

```python
def with_overrides(
    node_name: Optional[str],
    aliases: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    timeout: Optional[Union[int, datetime.timedelta, object]],
    retries: Optional[int],
    interruptible: Optional[bool],
    name: Optional[str],
    task_config: Optional[Any],
    container_image: Optional[str],
    accelerator: Optional[BaseAccelerator],
    cache: Optional[bool],
    cache_version: Optional[str],
    cache_serialize: Optional[bool],
    shared_memory: Optional[Union[L[True], str]],
    pod_template: Optional[PodTemplate],
    resources: Optional[Resources],
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `node_name` | `Optional[str]` |
| `aliases` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `timeout` | `Optional[Union[int, datetime.timedelta, object]]` |
| `retries` | `Optional[int]` |
| `interruptible` | `Optional[bool]` |
| `name` | `Optional[str]` |
| `task_config` | `Optional[Any]` |
| `container_image` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `cache` | `Optional[bool]` |
| `cache_version` | `Optional[str]` |
| `cache_serialize` | `Optional[bool]` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `pod_template` | `Optional[PodTemplate]` |
| `resources` | `Optional[Resources]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| bindings |  |  |
| flyte_entity |  |  |
| id |  |  |
| metadata |  |  |
| name |  |  |
| outputs |  |  |
| run_entity |  |  |
| upstream_nodes |  |  |

## flytekit.core.node.PodTemplate

Custom PodTemplate specification for a Task.


```python
def PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
):
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

## flytekit.core.node.ResourceSpec

```python
def ResourceSpec(
    requests: flytekit.core.resources.Resources,
    limits: flytekit.core.resources.Resources,
):
```
| Parameter | Type |
|-|-|
| `requests` | `flytekit.core.resources.Resources` |
| `limits` | `flytekit.core.resources.Resources` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_multiple_resource()`](#from_multiple_resource) | Convert Resources that represent both a requests and limits into a ResourceSpec |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

## flytekit.core.node.Resources

This class is used to specify both resource requests and resource limits.

.. code-block:: python

Resources(cpu="1", mem="2048")  # This is 1 CPU and 2 KB of memory
Resources(cpu="100m", mem="2Gi")  # This is 1/10th of a CPU and 2 gigabytes of memory
Resources(cpu=0.5, mem=1024) # This is 500m CPU and 1 KB of memory

# For Kubernetes-based tasks, pods use ephemeral local storage for scratch space, caching, and for logs.
# This allocates 1Gi of such local storage.
Resources(ephemeral_storage="1Gi")

When used together with `@task(resources=)`, you a specific the request and limits with one object.
When the value is set to a tuple or list, the first value is the request and the
second value is the limit. If the value is a single value, then both the requests and limit is
set to that value. For example, the `Resource(cpu=("1", "2"), mem=1024)` will set the cpu request to 1, cpu limit to 2,
mem limit and request to 1024.

.. note::

Persistent storage is not currently supported on the Flyte backend.

Please see the :std:ref:`User Guide <cookbook:customizing task resources>` for detailed examples.
Also refer to the `K8s conventions. <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>`__


```python
def Resources(
    cpu: typing.Union[str, int, float, list, tuple, NoneType],
    mem: typing.Union[str, int, list, tuple, NoneType],
    gpu: typing.Union[str, int, list, tuple, NoneType],
    ephemeral_storage: typing.Union[str, int, NoneType],
):
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
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

