---
title: flytekit.models.domain
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.domain

## Directory

### Classes

| Class | Description |
|-|-|
| [`Domain`](.././flytekit.models.domain#flytekitmodelsdomaindomain) | Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |

## flytekit.models.domain.Domain

Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments.



```python
def Domain(
    id,
    name,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| id |  |  |
| is_empty |  |  |
| name |  |  |

