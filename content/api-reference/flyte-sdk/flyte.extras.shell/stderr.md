---
title: Stderr
description: "Capture the task's stderr as a typed output."
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# Stderr

**Package:** `flyte.extras.shell`

Capture the task's stderr as a typed output. See `flyte.extras.shell.Stdout`.


## Parameters

```python
class Stderr(
    type: Type = flyte.io._file.File,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` | `Type` | |

