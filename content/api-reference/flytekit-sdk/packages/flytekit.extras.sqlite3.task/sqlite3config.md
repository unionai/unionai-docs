---
title: SQLite3Config
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SQLite3Config

**Package:** `flytekit.extras.sqlite3.task`

Use this configuration to configure if sqlite3 files that should be loaded by the task. The file itself is
considered as a database and hence is treated like a configuration
The path to a static sqlite3 compatible database file can be

-  within the container
- or from a publicly downloadable source



```python
class SQLite3Config(
    uri: str,
    compressed: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | default FlyteFile that will be downloaded on execute |
| `compressed` | `bool` | Boolean that indicates if the given file is a compressed archive. Supported file types are [zip, tar, gztar, bztar, xztar] |

