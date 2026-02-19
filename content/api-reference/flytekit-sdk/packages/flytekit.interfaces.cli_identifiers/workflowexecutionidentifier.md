---
title: WorkflowExecutionIdentifier
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowExecutionIdentifier

**Package:** `flytekit.interfaces.cli_identifiers`

```python
class WorkflowExecutionIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` |  | |
| `domain` |  | |
| `name` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `domain` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `name` | `None` | :rtype: Text |
| `project` | `None` | :rtype: Text |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
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

### from_python_std()

```python
def from_python_std(
    string,
)
```
Parses a string in the correct format into an identifier


| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

### promote_from_model()

```python
def promote_from_model(
    base_model,
)
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` |  | |

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
:rtype: flyteidl.core.identifier_pb2.WorkflowExecutionIdentifier


