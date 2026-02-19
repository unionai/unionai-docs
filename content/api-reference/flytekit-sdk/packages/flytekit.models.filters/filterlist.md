---
title: FilterList
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FilterList

**Package:** `flytekit.models.filters`

```python
class FilterList(
    filter_list,
)
```
| Parameter | Type | Description |
|-|-|-|
| `filter_list` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | For supporting the auto-generated REST API, filters must be dumped to a string for representation as GET params. |


### from_flyte_idl()

```python
def from_flyte_idl()
```
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


