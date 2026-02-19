---
title: SchemaWriter
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SchemaWriter

**Package:** `flytekit.types.schema.types`

```python
class SchemaWriter(
    to_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type | Description |
|-|-|-|
| `to_path` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `SchemaFormat` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `column_names` | `None` |  |
| `to_path` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`write()`](#write) |  |


### write()

```python
def write(
    dfs,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `dfs` |  | |
| `kwargs` | `**kwargs` | |

