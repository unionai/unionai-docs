---
title: SchemaHandler
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SchemaHandler

**Package:** `flytekit.types.schema.types`

```python
class SchemaHandler(
    name: str,
    object_type: Type,
    reader: Type[SchemaReader],
    writer: Type[SchemaWriter],
    handles_remote_io: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `object_type` | `Type` | |
| `reader` | `Type[SchemaReader]` | |
| `writer` | `Type[SchemaWriter]` | |
| `handles_remote_io` | `bool` | |

