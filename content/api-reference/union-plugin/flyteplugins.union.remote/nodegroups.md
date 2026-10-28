---
title: NodeGroups
description: "A cluster's declared node groups, as stored, with the generation they were read at."
icon: braces
version: 0.20.1
variants: -flyte +union
layout: py_api
---

# NodeGroups

**Package:** `flyteplugins.union.remote`

A cluster's declared node groups, as stored, with the generation they were read at.


## Parameters

```python
class NodeGroups(
    pb2: GetNodeGroupsResponse,
    cluster_name: str = '',
    org: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `GetNodeGroupsResponse` | |
| `cluster_name` | `str` | |
| `org` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `generation` | `int` | Change counter the groups were read at. 0 means the server does not track one. |
| `groups` | `list[NodeGroup]` |  |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Read a cluster's declared node groups, with no display filtering. |
| [`set()`](#set) | Replace a cluster's node groups and return the generation after the write. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await NodeGroups.get.aio()`.
```python
def get(
    cls,
    cluster_name: str,
) -> NodeGroups
```
Read a cluster's declared node groups, with no display filtering.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `cluster_name` | `str` | Cluster name. |

### set()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await NodeGroups.set.aio()`.
```python
def set(
    cls,
    cluster_name: str,
    node_groups: list[NodeGroupPb2],
    expected_generation: int | None = None,
) -> int
```
Replace a cluster's node groups and return the generation after the write.

This is a replace, not a merge: the groups sent become the cluster's groups,
and a group left out is deleted. Whether the caller may write this cluster's
groups at all is decided by the server from the caller's identity and the
cluster's type.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `cluster_name` | `str` | Cluster name. |
| `node_groups` | `list[NodeGroupPb2]` | The cluster's complete set of node groups. |
| `expected_generation` | `int \| None` | Generation the caller read. When set, the write is refused if the groups have changed since. 0 means "not tracked" and is not sent. |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

