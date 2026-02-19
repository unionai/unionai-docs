---
title: ConcurrencyPolicy
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConcurrencyPolicy

**Package:** `flytekit.models.concurrency`

Defines the concurrency policy for a launch plan.



```python
class ConcurrencyPolicy(
    max_concurrency: int,
    behavior: flytekit.models.concurrency.ConcurrencyLimitBehavior,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_concurrency` | `int` | |
| `behavior` | `flytekit.models.concurrency.ConcurrencyLimitBehavior` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `behavior` | `None` | Policy behavior when concurrency limit is reached. |
| `is_empty` | `None` |  |
| `max_concurrency` | `None` | Maximum number of concurrent workflows allowed. |

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
    pb2_object: flyteidl.admin.launch_plan_pb2.ConcurrencyPolicy,
) -> ConcurrencyPolicy
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.launch_plan_pb2.ConcurrencyPolicy` | |

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
:rtype: flyteidl.admin.launch_plan_pb2.ConcurrencyPolicy


