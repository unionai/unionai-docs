---
title: CachePolicy
version: 2.1.7
variants: +flyte +union
layout: py_api
---

# CachePolicy

**Package:** `flyte`

Protocol for custom cache version strategies.

Implement `get_version(salt, params) -&gt; str` to define how cache versions
are computed. The default implementation is `FunctionBodyPolicy`, which
hashes the function source code.

Example custom policy:

```python
class GitHashPolicy:
    def get_version(self, salt: str, params: VersionParameters) -> str:
        import subprocess
        git_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        return hashlib.sha256(f"{salt}{git_hash}".encode()).hexdigest()
```


```python
protocol CachePolicy()
```
## Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) |  |


### get_version()

```python
def get_version(
    salt: str,
    params: flyte._cache.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | |
| `params` | `flyte._cache.cache.VersionParameters` | |

