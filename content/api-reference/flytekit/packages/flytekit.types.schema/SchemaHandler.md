---
title: SchemaHandler
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SchemaHandler

**Package:** `flytekit.types.schema`

SchemaHandler(name: 'str', object_type: 'Type', reader: 'Type[SchemaReader]', writer: 'Type[SchemaWriter]', handles_remote_io: 'bool' = False)


```python
def SchemaHandler(
    name: str,
    object_type: Type,
    reader: Type[SchemaReader],
    writer: Type[SchemaWriter],
    handles_remote_io: bool,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `object_type` | `Type` |
| `reader` | `Type[SchemaReader]` |
| `writer` | `Type[SchemaWriter]` |
| `handles_remote_io` | `bool` |
## Methods

