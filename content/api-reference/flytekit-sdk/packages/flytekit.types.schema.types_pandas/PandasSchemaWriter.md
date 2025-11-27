---
title: PandasSchemaWriter
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PandasSchemaWriter

**Package:** `flytekit.types.schema.types_pandas`

Abstract base class for generic types.

A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::

  class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.

This class can then be used as follows::

  def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default


```python
class PandasSchemaWriter(
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
| [`write()`](#write) |  |


### write()

```python
def write(
    dfs,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `dfs` |  | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `column_names` |  |  |
| `to_path` |  |  |

