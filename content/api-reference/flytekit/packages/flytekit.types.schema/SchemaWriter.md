---
title: SchemaWriter
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SchemaWriter

**Package:** `flytekit.types.schema`

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

class Mapping[KT, VT]:
def __getitem__(self, key: KT) -> VT:
...
# Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
try:
return mapping[key]
except KeyError:
return default


```python
def SchemaWriter(
    to_path: str,
    cols: typing.Optional[typing.Dict[str, type]],
    fmt: SchemaFormat,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `to_path` | `str` |
| `cols` | `typing.Optional[typing.Dict[str, type]]` |
| `fmt` | `SchemaFormat` |
## Methods

### write()

```python
def write(
    dfs,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `dfs` |  |
| `kwargs` | ``**kwargs`` |
