---
title: JSONIterator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# JSONIterator

**Package:** `flytekit.types.iterator.json_iterator`

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
class JSONIterator(
    reader: jsonlines.jsonlines.Reader,
)
```
| Parameter | Type | Description |
|-|-|-|
| `reader` | `jsonlines.jsonlines.Reader` | |

