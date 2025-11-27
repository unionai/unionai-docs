---
title: ClusterResourceAttributes
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ClusterResourceAttributes

**Package:** `flytekit.models.matchable_resource`

```python
class ClusterResourceAttributes(
    attributes,
)
```
Custom resource attributes which will be applied in cluster resource creation (e.g. quotas).
Dict keys are the *case-sensitive* names of variables in templatized resource files.
Dict values should be the custom values which get substituted during resource creation.



| Parameter | Type | Description |
|-|-|-|
| `attributes` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.ClusterResourceAttributes


## Properties

| Property | Type | Description |
|-|-|-|
| `attributes` |  | {{< multiline >}}Custom resource attributes which will be applied in cluster resource management
:rtype: dict[Text, Text]
{{< /multiline >}} |
| `is_empty` |  |  |

