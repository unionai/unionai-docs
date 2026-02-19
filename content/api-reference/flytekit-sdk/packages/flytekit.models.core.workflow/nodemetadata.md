---
title: NodeMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeMetadata

**Package:** `flytekit.models.core.workflow`

```python
class NodeMetadata(
    name,
    timeout,
    retries,
    interruptible: typing.Optional[bool],
    cacheable: typing.Optional[bool],
    cache_version: typing.Optional[str],
    cache_serializable: typing.Optional[bool],
)
```
Defines extra information about the Node.



| Parameter | Type | Description |
|-|-|-|
| `name` |  | |
| `timeout` |  | |
| `retries` |  | |
| `interruptible` | `typing.Optional[bool]` | |
| `cacheable` | `typing.Optional[bool]` | Indicates that cache operations on this node should be serialized. |
| `cache_version` | `typing.Optional[str]` | The version of the cached data. |
| `cache_serializable` | `typing.Optional[bool]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `cache_serializable` | `None` |  |
| `cache_version` | `None` |  |
| `cacheable` | `None` |  |
| `interruptible` | `None` |  |
| `is_empty` | `None` |  |
| `name` | `None` | :rtype: Text |
| `retries` | `None` | :rtype: flytekit.models.literals.RetryStrategy |
| `timeout` | `None` | :rtype: datetime.timedelta |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_pb2.NodeMetadata


