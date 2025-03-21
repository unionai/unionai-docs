---
title: flytekit.remote.metrics
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.metrics

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteExecutionSpan`](.././flytekit.remote.metrics#flytekitremotemetricsflyteexecutionspan) | None. |
| [`datetime`](.././flytekit.remote.metrics#flytekitremotemetricsdatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |

## flytekit.remote.metrics.FlyteExecutionSpan

```python
def FlyteExecutionSpan(
    span: flyteidl.core.metrics_pb2.Span,
):
```
| Parameter | Type |
|-|-|
| `span` | `flyteidl.core.metrics_pb2.Span` |

### Methods

| Method | Description |
|-|-|
| [`dump()`](#dump) | None |
| [`explain()`](#explain) | None |
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### dump()

```python
def dump()
```
#### explain()

```python
def explain()
```
#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
):
```
| Parameter | Type |
|-|-|
| `pb` |  |

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
| is_empty |  |  |

## flytekit.remote.metrics.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


