---
title: Identifier
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Identifier

**Package:** `flytekit.models.core.identifier`

```python
class Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
)
```
| Parameter | Type | Description |
|-|-|-|
| `resource_type` |  | |
| `project` |  | |
| `domain` |  | |
| `name` |  | |
| `version` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

### resource_type_name()

```python
def resource_type_name()
```
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
:rtype: flyteidl.core.identifier_pb2.Identifier


## Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `project` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `resource_type` |  | {{< multiline >}}enum value from ResourceType
:rtype: int
{{< /multiline >}} |
| `version` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

