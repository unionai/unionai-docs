---
title: flytekit.models.concurrency
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.concurrency

## Directory

### Classes

| Class | Description |
|-|-|
| [`ConcurrencyLimitBehavior`](.././flytekit.models.concurrency#flytekitmodelsconcurrencyconcurrencylimitbehavior) |  |
| [`ConcurrencyPolicy`](.././flytekit.models.concurrency#flytekitmodelsconcurrencyconcurrencypolicy) | Defines the concurrency policy for a launch plan. |

## flytekit.models.concurrency.ConcurrencyLimitBehavior

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

## flytekit.models.concurrency.ConcurrencyPolicy

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.launch_plan_pb2.ConcurrencyPolicy,
) -> ConcurrencyPolicy
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.launch_plan_pb2.ConcurrencyPolicy` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.launch_plan_pb2.ConcurrencyPolicy


### Properties

| Property | Type | Description |
|-|-|-|
| `behavior` |  | {{< multiline >}}Policy behavior when concurrency limit is reached.
{{< /multiline >}} |
| `is_empty` |  |  |
| `max_concurrency` |  | {{< multiline >}}Maximum number of concurrent workflows allowed.
{{< /multiline >}} |

