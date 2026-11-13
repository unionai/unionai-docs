---
title: FileEntry
description: "One entry from `FileSystem.ls` or `FileSystem.stat`."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# FileEntry

**Package:** `flyteplugins.union.sandbox`

One entry from `FileSystem.ls` or `FileSystem.stat`.


## Parameters

```python
class FileEntry(
    name: str,
    path: str,
    type: FileType,
    size: int,
    mode: int,
    modified_unix_ms: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `path` | `str` | |
| `type` | `FileType` | |
| `size` | `int` | |
| `mode` | `int` | |
| `modified_unix_ms` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_dir` | `bool` |  |

