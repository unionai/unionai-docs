---
title: flytekit.core.cache
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.cache

## Directory

### Classes

| Class | Description |
|-|-|
| [`Cache`](.././flytekit.core.cache#flytekitcorecachecache) | Cache configuration for a task. |
| [`VersionParameters`](.././flytekit.core.cache#flytekitcorecacheversionparameters) | Parameters used for version hash generation. |

### Protocols

| Protocol | Description |
|-|-|
| [`CachePolicy`](.././flytekit.core.cache#flytekitcorecachecachepolicy) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `FuncOut` | `TypeVar` |  |
| `P` | `ParamSpec` |  |

## flytekit.core.cache.Cache

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

### Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |


#### get_ignored_inputs()

```python
def get_ignored_inputs()
```
#### get_version()

```python
def get_version(
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `params` | `flytekit.core.cache.VersionParameters` | |

## flytekit.core.cache.CachePolicy

```python
protocol CachePolicy()
```
### Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) |  |


#### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | |
| `params` | `flytekit.core.cache.VersionParameters` | |

## flytekit.core.cache.VersionParameters

Parameters used for version hash generation.

param func: The function to generate a version for. This is an optional parameter and can be any callable
             that matches the specified parameter and return types.
:type func: Optional[Callable[P, FuncOut]]


```python
class VersionParameters(
    func: typing.Callable[~P, ~FuncOut],
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
    pod_template_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable[~P, ~FuncOut]` | |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` | The container image to generate a version for. This can be a string representing the image name or an ImageSpec object. :type container_image: Optional[Union[str, ImageSpec]] |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` | |
| `pod_template_name` | `typing.Optional[str]` | |

