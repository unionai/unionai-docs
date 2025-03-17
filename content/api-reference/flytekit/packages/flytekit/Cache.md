---
title: Cache
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Cache

**Package:** `flytekit`

Cache configuration for a task.



```python
def Cache(
    version: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `version` | `typing.Optional[str]` |
| `serialize` | `bool` |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` |
| `salt` | `str` |
| `policies` | `typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType]` |
## Methods

### get_ignored_inputs()

```python
def get_ignored_inputs()
```
No parameters
### get_version()

```python
def get_version(
    params: flytekit.core.cache.VersionParameters,
):
```
| Parameter | Type |
|-|-|
| `params` | `flytekit.core.cache.VersionParameters` |
