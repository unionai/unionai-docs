---
title: Secret
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Secret

**Package:** `union`

See :std:ref:`cookbook:secrets` for usage examples.



```python
class Secret(
    group: typing.Optional[str],
    key: typing.Optional[str],
    group_version: typing.Optional[str],
    mount_requirement: <enum 'MountType'>,
    env_var: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `group` | `typing.Optional[str]` | |
| `key` | `typing.Optional[str]` | |
| `group_version` | `typing.Optional[str]` | |
| `mount_requirement` | `<enum 'MountType'>` | |
| `env_var` | `typing.Optional[str]` | |

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
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.Secret,
) -> Secret
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Secret` | |

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
