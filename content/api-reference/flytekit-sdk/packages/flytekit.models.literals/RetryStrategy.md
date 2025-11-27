---
title: RetryStrategy
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RetryStrategy

**Package:** `flytekit.models.literals`

```python
class RetryStrategy(
    retries: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `retries` | `int` | |

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
:rtype: flyteidl.core.literals_pb2.RetryStrategy


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `retries` |  | {{< multiline >}}Number of retries to attempt on recoverable failures.  If retries is 0, then only one attempt will be made.
:rtype: int
{{< /multiline >}} |

