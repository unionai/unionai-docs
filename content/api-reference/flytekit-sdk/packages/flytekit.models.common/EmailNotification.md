---
title: EmailNotification
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# EmailNotification

**Package:** `flytekit.models.common`

```python
class EmailNotification(
    recipients_email,
)
```
| Parameter | Type | Description |
|-|-|-|
| `recipients_email` |  | |

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
:rtype: flyteidl.admin.common_pb2.EmailNotification


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `recipients_email` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |

