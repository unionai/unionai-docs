---
title: ConcurrencyError
version: 2.4.0
variants: +flyte +union
layout: py_api
---

# ConcurrencyError

**Package:** `flyte.ai.agents`

Raised when an ``expected_sha`` precondition does not match the current state.


## Parameters

```python
class ConcurrencyError(
    path: str,
    expected_sha: str,
    actual_sha: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `expected_sha` | `str` | |
| `actual_sha` | `str` | |

