---
title: flytekit.types.iterator
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.iterator


Flytekit Iterator Type
======================

.. currentmodule:: flytekit.types.iterator

.. autosummary::
   :nosignatures:
   :toctree: generated/

   FlyteIterator
   JSON

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteIterator`](.././flytekit.types.iterator#flytekittypesiteratorflyteiterator) |  |

## flytekit.types.iterator.FlyteIterator

```python
class FlyteIterator(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[~T],
    length: int,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[~T]` |
| `length` | `int` |

