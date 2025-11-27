---
title: Parameter
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Parameter

**Package:** `flytekit.models.interface`

```python
class Parameter(
    var,
    default,
    required,
    artifact_query: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery],
    artifact_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
)
```
Declares an input parameter.  A parameter is used as input to a launch plan and has
    the special ability to have a default value or mark itself as required.


| Parameter | Type | Description |
|-|-|-|
| `var` |  | |
| `default` |  | |
| `required` |  | |
| `artifact_query` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery]` | Specify this to bind to a query instead of a constant. |
| `artifact_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` | When you want to bind to a known artifact pointer. |

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
:rtype: flyteidl.core.interface_pb2.Parameter


## Properties

| Property | Type | Description |
|-|-|-|
| `artifact_id` |  |  |
| `artifact_query` |  |  |
| `behavior` |  | {{< multiline >}}:rtype: T
{{< /multiline >}} |
| `default` |  | {{< multiline >}}This is the default literal value that will be applied for this parameter if not user specified.
:rtype: flytekit.models.literals.Literal
{{< /multiline >}} |
| `is_empty` |  |  |
| `required` |  | {{< multiline >}}If True, this parameter must be specified.  There cannot be a default value.
:rtype: bool
{{< /multiline >}} |
| `var` |  | {{< multiline >}}The variable definition for this input parameter.
:rtype: Variable
{{< /multiline >}} |

