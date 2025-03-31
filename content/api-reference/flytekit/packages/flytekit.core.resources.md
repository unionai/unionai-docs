---
title: flytekit.core.resources
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.resources

## Directory

### Classes

| Class | Description |
|-|-|
| [`BaseAccelerator`](.././flytekit.core.resources#flytekitcoreresourcesbaseaccelerator) | Base class for all accelerator types. |
| [`DataClassJSONMixin`](.././flytekit.core.resources#flytekitcoreresourcesdataclassjsonmixin) |  |
| [`ResourceSpec`](.././flytekit.core.resources#flytekitcoreresourcesresourcespec) |  |
| [`Resources`](.././flytekit.core.resources#flytekitcoreresourcesresources) | This class is used to specify both resource requests and resource limits. |

### Methods

| Method | Description |
|-|-|
| [`_check_resource_is_singular()`](#_check_resource_is_singular) | Raise a value error if the resource has a tuple. |
| [`_convert_resources_to_resource_entries()`](#_convert_resources_to_resource_entries) |  |
| [`construct_extended_resources()`](#construct_extended_resources) | Convert public extended resources to idl. |
| [`convert_resources_to_resource_model()`](#convert_resources_to_resource_model) | Convert flytekit ``Resources`` objects to a Resources model. |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`fields()`](#fields) | Return a tuple describing the fields of this dataclass. |
| [`pod_spec_from_resources()`](#pod_spec_from_resources) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `SHARED_MEMORY_MOUNT_NAME` | `str` |  |
| `SHARED_MEMORY_MOUNT_PATH` | `str` |  |
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### _check_resource_is_singular()

```python
def _check_resource_is_singular(
    resource: flytekit.core.resources.Resources,
)
```
Raise a value error if the resource has a tuple.


| Parameter | Type |
|-|-|
| `resource` | `flytekit.core.resources.Resources` |

#### _convert_resources_to_resource_entries()

```python
def _convert_resources_to_resource_entries(
    resources: flytekit.core.resources.Resources,
) -> typing.List[flytekit.models.task.Resources.ResourceEntry]
```
| Parameter | Type |
|-|-|
| `resources` | `flytekit.core.resources.Resources` |

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
) -> flytekit.models.task.Resources
```
Convert flytekit ``Resources`` objects to a Resources model



| Parameter | Type |
|-|-|
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

#### fields()

```python
def fields(
    class_or_instance,
)
```
Return a tuple describing the fields of this dataclass.

Accepts a dataclass or an instance of one. Tuple elements are of
type Field.


| Parameter | Type |
|-|-|
| `class_or_instance` |  |

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

## flytekit.core.resources.BaseAccelerator

Base class for all accelerator types. This class is not meant to be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.core.resources.DataClassJSONMixin

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

