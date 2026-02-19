---
title: PluginOverrides
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PluginOverrides

**Package:** `flytekit.models.matchable_resource`

```python
class PluginOverrides(
    overrides,
)
```
Alternate plugin implementations for designated task types.



| Parameter | Type | Description |
|-|-|-|
| `overrides` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `overrides` | `None` | :rtype: list[PluginOverride] |

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
:rtype: flyteidl.admin.matchable_resource_pb2.PluginOverrides


