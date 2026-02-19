---
title: FlyteArrayNode
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteArrayNode

**Package:** `flytekit.remote.entities`

```python
class FlyteArrayNode(
    flyte_node: FlyteNode,
    parallelism: int,
    min_successes: int,
    min_success_ratio: float,
)
```
TODO: docstring


| Parameter | Type | Description |
|-|-|-|
| `flyte_node` | `FlyteNode` | |
| `parallelism` | `int` | |
| `min_successes` | `int` | |
| `min_success_ratio` | `float` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `flyte_node` | `None` |  |
| `is_empty` | `None` |  |
| `node` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.ArrayNode,
    flyte_node: FlyteNode,
) -> FlyteArrayNode
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `_workflow_model.ArrayNode` | |
| `flyte_node` | `FlyteNode` | |

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
