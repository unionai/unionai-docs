---
title: Labels
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Labels

**Package:** `flytekit.models.common`

```python
class Labels(
    values,
)
```
Label values to be applied to a workflow execution resource.



| Parameter | Type | Description |
|-|-|-|
| `values` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `values` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: dict[Text, Text]. |


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
:rtype: dict[Text, Text]


