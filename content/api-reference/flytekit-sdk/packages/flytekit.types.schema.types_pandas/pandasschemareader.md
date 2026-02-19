---
title: PandasSchemaReader
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PandasSchemaReader

**Package:** `flytekit.types.schema.types_pandas`

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

## Properties

| Property | Type | Description |
|-|-|-|
| `column_names` | `None` |  |
| `from_path` | `None` |  |

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

