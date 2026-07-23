---
title: ConcurrencyError
version: 2.5.12
variants: +flyte +union
layout: py_api
---

# ConcurrencyError

**Package:** `flyte.ai.agents.memory`

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

