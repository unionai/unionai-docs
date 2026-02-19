---
title: Directory
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Directory

**Package:** `flytekit.core.utils`

```python
class Directory(
    path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | :rtype: Text |

## Methods

| Method | Description |
|-|-|
| [`list_dir()`](#list_dir) | The list of absolute filepaths for all immediate sub-paths. |


### list_dir()

```python
def list_dir()
```
The list of absolute filepaths for all immediate sub-paths
:rtype: list[Text]


