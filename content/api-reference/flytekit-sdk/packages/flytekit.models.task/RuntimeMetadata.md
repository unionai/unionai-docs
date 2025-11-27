---
title: RuntimeMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RuntimeMetadata

**Package:** `flytekit.models.task`

```python
class RuntimeMetadata(
    type,
    version,
    flavor,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` |  | |
| `version` |  | |
| `flavor` |  | |

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
:rtype: flyteidl.core.tasks_pb2.RuntimeMetadata


## Properties

| Property | Type | Description |
|-|-|-|
| `flavor` |  | {{< multiline >}}Optional extra information about runtime environment (e.g. Python, GoLang, etc.)
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `type` |  | {{< multiline >}}Enum type from RuntimeMetadata.RuntimeType
:rtype: int
{{< /multiline >}} |
| `version` |  | {{< multiline >}}Version string for SDK version.  Can be used for metrics or managing breaking changes in Admin or Propeller
:rtype: Text
{{< /multiline >}} |

