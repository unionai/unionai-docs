---
title: FastPackageOptions
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FastPackageOptions

**Package:** `flytekit.tools.fast_registration`

FastPackageOptions is used to set configuration options when packaging files.


```python
class FastPackageOptions(
    ignores: list[Ignore],
    keep_default_ignores: bool,
    copy_style: Optional[CopyFileDetection],
    show_files: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ignores` | `list[Ignore]` | |
| `keep_default_ignores` | `bool` | |
| `copy_style` | `Optional[CopyFileDetection]` | |
| `show_files` | `bool` | |

