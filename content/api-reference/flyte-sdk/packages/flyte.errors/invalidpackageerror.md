---
title: InvalidPackageError
version: 2.1.3.dev1+ge23e739d5
variants: +flyte +union
layout: py_api
---

# InvalidPackageError

**Package:** `flyte.errors`

Raised when an invalid system package is detected during image build.


## Parameters

```python
class InvalidPackageError(
    package_name: str,
    original_error: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `package_name` | `str` | |
| `original_error` | `str` | |

