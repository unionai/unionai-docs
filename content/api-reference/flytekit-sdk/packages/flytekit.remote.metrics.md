---
title: flytekit.remote.metrics
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.metrics

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteExecutionSpan`](.././flytekit.remote.metrics#flytekitremotemetricsflyteexecutionspan) |  |

### Methods

| Method | Description |
|-|-|
| [`aggregate_reference_span()`](#aggregate_reference_span) |  |
| [`aggregate_spans()`](#aggregate_spans) |  |
| [`print_span()`](#print_span) |  |


## Methods

#### aggregate_reference_span()

```python
def aggregate_reference_span(
    span,
)
```
| Parameter | Type |
|-|-|
| `span` |  |

#### aggregate_spans()

```python
def aggregate_spans(
    spans,
)
```
| Parameter | Type |
|-|-|
| `spans` |  |

#### print_span()

```python
def print_span(
    span,
    indent,
    identifier,
)
```
| Parameter | Type |
|-|-|
| `span` |  |
| `indent` |  |
| `identifier` |  |

## flytekit.remote.metrics.FlyteExecutionSpan

```python
class FlyteExecutionSpan(
    span: flyteidl.core.metrics_pb2.Span,
)
```
| Parameter | Type |
|-|-|
| `span` | `flyteidl.core.metrics_pb2.Span` |

### Methods

| Method | Description |
|-|-|
| [`dump()`](#dump) |  |
| [`explain()`](#explain) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


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
)
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

