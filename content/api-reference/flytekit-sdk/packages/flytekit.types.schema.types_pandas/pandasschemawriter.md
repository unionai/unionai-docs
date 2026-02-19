---
title: PandasSchemaWriter
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PandasSchemaWriter

**Package:** `flytekit.types.schema.types_pandas`

```python
class PandasSchemaWriter(
    local_dir: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: <enum 'SchemaFormat'>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `local_dir` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `<enum 'SchemaFormat'>` | |

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

