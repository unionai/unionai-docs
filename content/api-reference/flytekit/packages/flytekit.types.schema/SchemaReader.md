---
title: SchemaReader
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SchemaReader

**Package:** `flytekit.types.schema`

Base SchemaReader to handle any readers (that can manage their own IO or otherwise)
Use the simplified base LocalIOSchemaReader for non distributed dataframes


```python
def SchemaReader(
    from_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |
## Methods

### all()

```python
def all(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |
### iter()

```python
def iter(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |
