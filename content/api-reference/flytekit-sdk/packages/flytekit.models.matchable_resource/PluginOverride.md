---
title: PluginOverride
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PluginOverride

**Package:** `flytekit.models.matchable_resource`

```python
class PluginOverride(
    task_type,
    plugin_id,
    missing_plugin_behavior,
)
```
Alternate plugin implementations requested for a specific task type.



| Parameter | Type | Description |
|-|-|-|
| `task_type` |  | |
| `plugin_id` |  | |
| `missing_plugin_behavior` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`string_to_enum()`](#string_to_enum) |  |
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


### string_to_enum()

```python
def string_to_enum(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.matchable_resource_pb2.PluginOverride


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `missing_plugin_behavior` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `plugin_id` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |
| `task_type` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

