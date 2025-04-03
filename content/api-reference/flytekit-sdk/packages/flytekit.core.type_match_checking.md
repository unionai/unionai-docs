---
title: flytekit.core.type_match_checking
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.type_match_checking

## Directory

### Methods

| Method | Description |
|-|-|
| [`literal_types_match()`](#literal_types_match) | Returns if two LiteralTypes are the same. |


## Methods

#### literal_types_match()

```python
def literal_types_match(
    downstream: LiteralType,
    upstream: LiteralType,
) -> bool
```
Returns if two LiteralTypes are the same.
Takes into account arbitrary ordering of enums and unions, otherwise just an equivalence check.


| Parameter | Type |
|-|-|
| `downstream` | `LiteralType` |
| `upstream` | `LiteralType` |

