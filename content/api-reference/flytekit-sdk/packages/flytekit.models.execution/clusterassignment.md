---
title: ClusterAssignment
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ClusterAssignment

**Package:** `flytekit.models.execution`

```python
class ClusterAssignment(
    cluster_pool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cluster_pool` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `cluster_pool` | `None` | :rtype: Text |
| `is_empty` | `None` |  |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin._cluster_assignment_pb2.ClusterAssignment


