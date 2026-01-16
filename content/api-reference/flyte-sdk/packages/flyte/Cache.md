---
title: Cache
version: 2.0.0b48
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Cache

**Package:** `flyte`

Cache configuration for a task.


```python
class Cache(
    behavior: typing.Literal['auto', 'override', 'disable'],
    version_override: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flyte._cache.cache.CachePolicy], flyte._cache.cache.CachePolicy, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `behavior` | `typing.Literal['auto', 'override', 'disable']` | The behavior of the cache. Can be "auto", "override" or "disable". |
| `version_override` | `typing.Optional[str]` | The version of the cache. If not provided, the version will be generated based on the cache policies :type version_override: Optional[str] |
| `serialize` | `bool` | Boolean that indicates if identical (ie. same inputs) instances of this task should be executed in serial when caching is enabled. This means that given multiple concurrent executions over identical inputs, only a single instance executes and the rest wait to reuse the cached results. :type serialize: bool |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` | A tuple of input names to ignore when generating the version hash. :type ignored_inputs: Union[Tuple[str, ...], str] |
| `salt` | `str` | A salt used in the hash generation. :type salt: str |
| `policies` | `typing.Union[typing.List[flyte._cache.cache.CachePolicy], flyte._cache.cache.CachePolicy, NoneType]` | A list of cache policies to generate the version hash. :type policies: Optional[Union[List[CachePolicy], CachePolicy]] |

## Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |
| [`is_enabled()`](#is_enabled) | Check if the cache policy is enabled. |


### get_ignored_inputs()

```python
def get_ignored_inputs()
```
### get_version()

```python
def get_version(
    params: typing.Optional[flyte._cache.cache.VersionParameters],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `params` | `typing.Optional[flyte._cache.cache.VersionParameters]` | |

### is_enabled()

```python
def is_enabled()
```
Check if the cache policy is enabled.


