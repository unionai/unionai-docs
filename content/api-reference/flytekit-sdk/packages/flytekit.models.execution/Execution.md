---
title: Execution
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Execution

**Package:** `flytekit.models.execution`

```python
class Execution(
    id,
    spec,
    closure,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `spec` |  | |
| `closure` |  | |

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
:rtype: flyteidl.admin.execution_pb2.Execution


## Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: ExecutionClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.WorkflowExecutionIdentifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `spec` |  | {{< multiline >}}:rtype: ExecutionSpec
{{< /multiline >}} |

