---
title: FlyteExecutionSpan
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteExecutionSpan

**Package:** `flytekit.remote.metrics`

```python
class FlyteExecutionSpan(
    span: flyteidl.core.metrics_pb2.Span,
)
```
| Parameter | Type | Description |
|-|-|-|
| `span` | `flyteidl.core.metrics_pb2.Span` | |

## Methods

| Method | Description |
|-|-|
| [`dump()`](#dump) |  |
| [`explain()`](#explain) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### dump()

```python
def dump()
```
### explain()

```python
def explain()
```
### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

