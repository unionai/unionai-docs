---
title: Annotations
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Annotations

**Package:** `flytekit.models.common`

```python
class Annotations(
    values,
)
```
Annotation values to be applied to a workflow execution resource.



| Parameter | Type | Description |
|-|-|-|
| `values` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _common_pb2. |


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
:rtype: _common_pb2.Annotations


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `values` |  |  |

