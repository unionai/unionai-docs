---
title: VariableMap
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# VariableMap

**Package:** `flytekit.models.interface`

```python
class VariableMap(
    variables,
)
```
A map of Variables



| Parameter | Type | Description |
|-|-|-|
| `variables` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: dict[Text, Variable]. |


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
:rtype: dict[Text, Variable]


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `variables` |  | {{< multiline >}}:rtype: dict[Text, Variable]
{{< /multiline >}} |

