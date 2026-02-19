---
title: Notification
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Notification

**Package:** `flytekit.models.common`

```python
class Notification(
    phases,
    email: flytekit.models.common.EmailNotification,
    pager_duty: flytekit.models.common.PagerDutyNotification,
    slack: flytekit.models.common.SlackNotification,
)
```
Represents a structure for notifications based on execution status.



| Parameter | Type | Description |
|-|-|-|
| `phases` |  | |
| `email` | `flytekit.models.common.EmailNotification` | |
| `pager_duty` | `flytekit.models.common.PagerDutyNotification` | |
| `slack` | `flytekit.models.common.SlackNotification` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `email` | `None` | :rtype: EmailNotification |
| `is_empty` | `None` |  |
| `pager_duty` | `None` | :rtype: PagerDutyNotification |
| `phases` | `None` | A list of phases to which users can associate the notifications. :rtype: list[int] |
| `slack` | `None` | :rtype: SlackNotification |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.common_pb2.Notification


