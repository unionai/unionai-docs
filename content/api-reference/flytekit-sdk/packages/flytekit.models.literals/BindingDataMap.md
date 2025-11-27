---
title: BindingDataMap
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BindingDataMap

**Package:** `flytekit.models.literals`

```python
class BindingDataMap(
    bindings,
)
```
A map of BindingData items.  Can be a recursive structure



| Parameter | Type | Description |
|-|-|-|
| `bindings` |  | |

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
:rtype: flyteidl.core.literals_pb2.BindingDataMap


## Properties

| Property | Type | Description |
|-|-|-|
| `bindings` |  | {{< multiline >}}Map of strings to Bindings
:rtype: dict[string, BindingData]
{{< /multiline >}} |
| `is_empty` |  |  |

