---
title: flyte.app
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.app

## Directory

### Classes

| Class | Description |
|-|-|
| [`AppEnvironment`](.././flyte.app#flyteappappenvironment) |  |
| [`Domain`](.././flyte.app#flyteappdomain) |  |
| [`Input`](.././flyte.app#flyteappinput) | Input for application. |
| [`Link`](.././flyte.app#flyteapplink) |  |
| [`Port`](.././flyte.app#flyteappport) |  |
| [`Scaling`](.././flyte.app#flyteappscaling) |  |

## flyte.app.AppEnvironment

```python
class AppEnvironment(
    name: str,
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto']],
    type: typing.Optional[str],
    port: int | flyte.app._types.Port,
    args: *args,
    command: typing.Union[typing.List[str], str, NoneType],
    requires_auth: bool,
    scaling: flyte.app._types.Scaling,
    domain: flyte.app._types.Domain | None,
    links: typing.List[flyte.app._types.Link],
    include: typing.List[str],
    inputs: typing.List[flyte.app._input.Input],
    cluster_pool: str,
)
```
| Parameter | Type |
|-|-|
| `name` | {{< multiline >}}`str`
doc: Name of the environment
{{< /multiline >}} |
| `depends_on` | {{< multiline >}}`List[Environment]`
doc: Environment dependencies to hint, so when you deploy the environment, the dependencies are
also deployed. This is useful when you have a set of environments that depend on each other.
{{< /multiline >}} |
| `pod_template` | `Optional[Union[str, PodTemplate]]` |
| `description` | `Optional[str]` |
| `secrets` | {{< multiline >}}`Optional[SecretRequest]`
doc: Secrets to inject into the environment.
{{< /multiline >}} |
| `env_vars` | {{< multiline >}}`Optional[Dict[str, str]]`
doc: Environment variables to set for the environment.
{{< /multiline >}} |
| `resources` | {{< multiline >}}`Optional[Resources]`
doc: Resources to allocate for the environment.
{{< /multiline >}} |
| `interruptible` | `bool` |
| `image` | {{< multiline >}}`Union[str, Image, Literal['auto']]`
doc: Docker image to use for the environment. If set to "auto", will use the default image.
{{< /multiline >}} |
| `type` | `typing.Optional[str]` |
| `port` | `int \| flyte.app._types.Port` |
| `args` | `*args` |
| `command` | `typing.Union[typing.List[str], str, NoneType]` |
| `requires_auth` | `bool` |
| `scaling` | `flyte.app._types.Scaling` |
| `domain` | `flyte.app._types.Domain \| None` |
| `links` | `typing.List[flyte.app._types.Link]` |
| `include` | `typing.List[str]` |
| `inputs` | `typing.List[flyte.app._input.Input]` |
| `cluster_pool` | `str` |

### Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) |  |
| [`container_cmd()`](#container_cmd) |  |
| [`get_port()`](#get_port) |  |


#### add_dependency()

```python
def add_dependency(
    env: Environment,
)
```
Add a dependency to the environment.


| Parameter | Type |
|-|-|
| `env` | `Environment` |

#### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]],
    resources: Optional[Resources],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    depends_on: Optional[List[Environment]],
    description: Optional[str],
    kwargs: **kwargs,
) -> Environment
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` |
| `resources` | `Optional[Resources]` |
| `env_vars` | `Optional[Dict[str, str]]` |
| `secrets` | `Optional[SecretRequest]` |
| `depends_on` | `Optional[List[Environment]]` |
| `description` | `Optional[str]` |
| `kwargs` | `**kwargs` |

#### container_args()

```python
def container_args(
    serialize_context: flyte.models.SerializationContext,
) -> typing.List[str]
```
| Parameter | Type |
|-|-|
| `serialize_context` | `flyte.models.SerializationContext` |

#### container_cmd()

```python
def container_cmd(
    serialize_context: flyte.models.SerializationContext,
) -> typing.List[str]
```
| Parameter | Type |
|-|-|
| `serialize_context` | `flyte.models.SerializationContext` |

#### get_port()

```python
def get_port()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |

## flyte.app.Domain

```python
class Domain(
    subdomain: typing.Optional[str],
    custom_domain: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `subdomain` | `typing.Optional[str]` |
| `custom_domain` | `typing.Optional[str]` |

## flyte.app.Input

Input for application.



```python
class Input(
    value: str | flyte.io.File | flyte.io.Dir,
    name: Optional[str],
    env_var: Optional[str],
    download: bool,
    mount: Optional[str],
    ignore_patterns: list[str],
)
```
| Parameter | Type |
|-|-|
| `value` | {{< multiline >}}`str \| flyte.io.File \| flyte.io.Dir`
doc: Value for input.
{{< /multiline >}} |
| `name` | {{< multiline >}}`Optional[str]`
doc: Name of input.
{{< /multiline >}} |
| `env_var` | {{< multiline >}}`Optional[str]`
doc: Environment name to set the value in the serving environment.
{{< /multiline >}} |
| `download` | {{< multiline >}}`bool`
doc: When True, the input will be automatically downloaded. This
only works if the value refers to an item in a object store. i.e. `s3://...`
{{< /multiline >}} |
| `mount` | {{< multiline >}}`Optional[str]`
doc: If `value` is a directory, then the directory will be available
at `mount`. If `value` is a file, then the file will be downloaded into the
`mount` directory.
{{< /multiline >}} |
| `ignore_patterns` | {{< multiline >}}`list[str]`
doc: If `value` is a directory, then this is a list of glob
patterns to ignore.
{{< /multiline >}} |

## flyte.app.Link

```python
class Link(
    path: str,
    title: str,
    is_relative: bool,
)
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `title` | `str` |
| `is_relative` | `bool` |

## flyte.app.Port

```python
class Port(
    port: int,
    name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `port` | `int` |
| `name` | `typing.Optional[str]` |

## flyte.app.Scaling

```python
class Scaling(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    metric: typing.Union[flyte.app._types.Scaling.Concurrency, flyte.app._types.Scaling.RequestRate, NoneType],
    scaledown_after: int | datetime.timedelta | None,
)
```
| Parameter | Type |
|-|-|
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` |
| `metric` | `typing.Union[flyte.app._types.Scaling.Concurrency, flyte.app._types.Scaling.RequestRate, NoneType]` |
| `scaledown_after` | `int \| datetime.timedelta \| None` |

### Methods

| Method | Description |
|-|-|
| [`get_replicas()`](#get_replicas) |  |


#### get_replicas()

```python
def get_replicas()
```
