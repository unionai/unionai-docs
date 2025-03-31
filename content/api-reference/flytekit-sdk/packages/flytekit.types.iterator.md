---
title: flytekit.types.iterator
version: 1.15.4.dev2+g3e3ce2426
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
| [`FlyteIterator`](.././flytekit.types.iterator#flytekittypesiteratorflyteiterator) | None. |

## flytekit.types.iterator.FlyteIterator

```python
def FlyteIterator(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[~T],
    length: int,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `lv` | `flytekit.models.literals.Literal` |
| `expected_python_type` | `typing.Type[~T]` |
| `length` | `int` |

