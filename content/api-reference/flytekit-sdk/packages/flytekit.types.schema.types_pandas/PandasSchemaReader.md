---
title: PandasSchemaReader
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PandasSchemaReader

**Package:** `flytekit.types.schema.types_pandas`

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes


```python
class PandasSchemaReader(
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

## Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`iter()`](#iter) |  |


### all()

```python
def all(
    kwargs,
) -> T
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### iter()

```python
def iter(
    kwargs,
) -> typing.Generator[T, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `column_names` |  |  |
| `from_path` |  |  |

