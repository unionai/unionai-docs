---
title: HiveQuery
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# HiveQuery

**Package:** `flytekit.models.qubole`

```python
class HiveQuery(
    query,
    timeout_sec,
    retry_count,
)
```
Initializes a new HiveQuery.



| Parameter | Type | Description |
|-|-|-|
| `query` |  | |
| `timeout_sec` |  | |
| `retry_count` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _qubole. |


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
:rtype: _qubole.HiveQuery


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `query` |  | {{< multiline >}}The query string.
:rtype: str
{{< /multiline >}} |
| `retry_count` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `timeout_sec` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |

