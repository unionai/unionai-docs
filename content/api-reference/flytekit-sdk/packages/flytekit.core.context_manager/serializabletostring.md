---
title: SerializableToString
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SerializableToString

**Package:** `flytekit.core.context_manager`

This protocol is used by the Artifact create_from function. Basically these objects are serialized when running,
and then added to a literal's metadata.



```python
protocol SerializableToString()
```
## Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |


### serialize_to_string()

```python
def serialize_to_string(
    ctx: FlyteContext,
    variable_name: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `variable_name` | `str` | |

