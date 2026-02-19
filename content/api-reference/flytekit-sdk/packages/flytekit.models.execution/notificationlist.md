---
title: NotificationList
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NotificationList

**Package:** `flytekit.models.execution`

```python
class NotificationList(
    notifications,
)
```
| Parameter | Type | Description |
|-|-|-|
| `notifications` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `notifications` | `None` | :rtype: list[flytekit.models.common.Notification] |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype:  flyteidl. |


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
:rtype:  flyteidl.admin.execution_pb2.NotificationList


