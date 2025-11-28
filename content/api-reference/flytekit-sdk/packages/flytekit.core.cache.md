---
title: flytekit.core.cache
version: 1.16.10
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
| [`CachePolicy`](.././flytekit.core.cache#flytekitcorecachecachepolicy) | Base class for protocol classes. |

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
| `version` | `typing.Optional[str]` | |
| `serialize` | `bool` | |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` | |
| `salt` | `str` | |
| `policies` | `typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType]` | |

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

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...


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
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` | |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` | |
| `pod_template_name` | `typing.Optional[str]` | |

