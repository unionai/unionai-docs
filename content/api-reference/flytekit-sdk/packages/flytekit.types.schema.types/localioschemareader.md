---
title: LocalIOSchemaReader
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LocalIOSchemaReader

**Package:** `flytekit.types.schema.types`

```python
class LocalIOSchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
)
```
| Parameter | Type | Description |
|-|-|-|
| `from_path` | `str` | |
| `cols` | `typing.Optional[typing.Dict[str, type]]` | |
| `fmt` | `SchemaFormat` | |

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

