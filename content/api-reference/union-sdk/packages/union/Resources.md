---
title: Resources
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Resources

**Package:** `union`

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
| Parameter | Type | Description |
|-|-|-|
| `cpu` | `typing.Union[str, int, float, list, tuple, NoneType]` | |
| `mem` | `typing.Union[str, int, list, tuple, NoneType]` | |
| `gpu` | `typing.Union[str, int, list, tuple, NoneType]` | |
| `ephemeral_storage` | `typing.Union[str, int, NoneType]` | |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` | |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` | |
| `from_dict_kwargs` | `typing.Any` | |

### to_dict()

```python
def to_dict()
```
### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type | Description |
|-|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` | |
| `to_dict_kwargs` | `typing.Any` | |

