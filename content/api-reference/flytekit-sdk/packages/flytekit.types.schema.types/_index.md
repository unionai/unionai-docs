---
title: flytekit.types.schema.types
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.schema.types

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteSchema`](../flytekit.types.schema.types/flyteschema) |  |
| [`FlyteSchemaTransformer`](../flytekit.types.schema.types/flyteschematransformer) |  |
| [`LocalIOSchemaReader`](../flytekit.types.schema.types/localioschemareader) |  |
| [`LocalIOSchemaWriter`](../flytekit.types.schema.types/localioschemawriter) |  |
| [`SchemaEngine`](../flytekit.types.schema.types/schemaengine) | This is the core Engine that handles all schema sub-systems. |
| [`SchemaFormat`](../flytekit.types.schema.types/schemaformat) | Represents the schema storage format (at rest). |
| [`SchemaHandler`](../flytekit.types.schema.types/schemahandler) |  |
| [`SchemaOpenMode`](../flytekit.types.schema.types/schemaopenmode) |  |
| [`SchemaReader`](../flytekit.types.schema.types/schemareader) | Base SchemaReader to handle any readers (that can manage their own IO or otherwise). |
| [`SchemaWriter`](../flytekit.types.schema.types/schemawriter) |  |

### Methods

| Method | Description |
|-|-|
| [`generate_ordered_files()`](#generate_ordered_files) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `MESSAGEPACK` | `str` |  |
| `T` | `TypeVar` |  |

## Methods

#### generate_ordered_files()

```python
def generate_ordered_files(
    directory: os.PathLike,
    n: int,
) -> typing.Generator[str, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `directory` | `os.PathLike` | |
| `n` | `int` | |

