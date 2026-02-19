---
title: SchemaEngine
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SchemaEngine

**Package:** `flytekit.types.schema.types`

This is the core Engine that handles all schema sub-systems. All schema types needs to be registered with this
to allow direct support for that type in FlyteSchema.
e.g. of possible supported types are Pandas.DataFrame, Spark.DataFrame, Vaex.DataFrame, etc.



## Methods

| Method | Description |
|-|-|
| [`get_handler()`](#get_handler) |  |
| [`register_handler()`](#register_handler) | Register a new handler that can create a SchemaReader and SchemaWriter for the expected type. |


### get_handler()

```python
def get_handler(
    t: Type,
) -> SchemaHandler
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type` | |

### register_handler()

```python
def register_handler(
    h: SchemaHandler,
)
```
Register a new handler that can create a SchemaReader and SchemaWriter for the expected type.


| Parameter | Type | Description |
|-|-|-|
| `h` | `SchemaHandler` | |

