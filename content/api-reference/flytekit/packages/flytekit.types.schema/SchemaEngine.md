---
title: SchemaEngine
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SchemaEngine

**Package:** `flytekit.types.schema`

This is the core Engine that handles all schema sub-systems. All schema types needs to be registered with this
to allow direct support for that type in FlyteSchema.
e.g. of possible supported types are Pandas.DataFrame, Spark.DataFrame, Vaex.DataFrame, etc.


## Methods

### get_handler()

```python
def get_handler(
    t: Type,
):
```
| Parameter | Type |
|-|-|
| `t` | `Type` |
### register_handler()

```python
def register_handler(
    h: SchemaHandler,
):
```
Register a new handler that can create a SchemaReader and SchemaWriter for the expected type.


| Parameter | Type |
|-|-|
| `h` | `SchemaHandler` |
