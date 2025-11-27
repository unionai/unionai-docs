---
title: AutoDeletingTempDir
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AutoDeletingTempDir

**Package:** `flytekit.core.utils`

Creates a posix safe tempdir which is auto deleted once out of scope


```python
class AutoDeletingTempDir(
    working_dir_prefix,
    tmp_dir,
    cleanup,
)
```
| Parameter | Type | Description |
|-|-|-|
| `working_dir_prefix` |  | |
| `tmp_dir` |  | |
| `cleanup` |  | |

## Methods

| Method | Description |
|-|-|
| [`force_cleanup()`](#force_cleanup) |  |
| [`get_named_tempfile()`](#get_named_tempfile) |  |
| [`list_dir()`](#list_dir) | The list of absolute filepaths for all immediate sub-paths. |


### force_cleanup()

```python
def force_cleanup()
```
### get_named_tempfile()

```python
def get_named_tempfile(
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` |  | |

### list_dir()

```python
def list_dir()
```
The list of absolute filepaths for all immediate sub-paths
:rtype: list[Text]


## Properties

| Property | Type | Description |
|-|-|-|
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

