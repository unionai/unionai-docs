---
title: LessThan
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LessThan

**Package:** `flytekit.models.filters`

```python
class LessThan(
    key,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `value` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


### from_flyte_idl()

```python
def from_flyte_idl()
```
### from_python_std()

```python
def from_python_std(
    string,
)
```
| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

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
For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params.
:rtype: Text


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

