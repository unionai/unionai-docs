---
title: Cache
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Cache

**Package:** `flytekit.core.cache`

Cache configuration for a task.



```python
class Cache(
    version: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `version` | `typing.Optional[str]` | The version of the task. If not provided, the version will be generated based on the cache policies. :type version: Optional[str] |
| `serialize` | `bool` | Boolean that indicates if identical (ie. same inputs) instances of this task should be executed in serial when caching is enabled. This means that given multiple concurrent executions over identical inputs, only a single instance executes and the rest wait to reuse the cached results. :type serialize: bool |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` | A tuple of input names to ignore when generating the version hash. :type ignored_inputs: Union[Tuple[str, ...], str] |
| `salt` | `str` | A salt used in the hash generation. :type salt: str |
| `policies` | `typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType]` | A list of cache policies to generate the version hash. :type policies: Optional[Union[List[CachePolicy], CachePolicy]] |

## Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |


### get_ignored_inputs()

```python
def get_ignored_inputs()
```
### get_version()

```python
def get_version(
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `params` | `flytekit.core.cache.VersionParameters` | |

