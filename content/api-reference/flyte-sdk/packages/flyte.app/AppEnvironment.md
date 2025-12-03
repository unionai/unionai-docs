---
title: AppEnvironment
version: 2.0.0b34
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AppEnvironment

**Package:** `flyte.app`

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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the environment |
| `depends_on` | `List[Environment]` | Environment dependencies to hint, so when you deploy the environment, the dependencies are also deployed. This is useful when you have a set of environments that depend on each other. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject into the environment. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables to set for the environment. |
| `resources` | `Optional[Resources]` | Resources to allocate for the environment. |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto']]` | Docker image to use for the environment. If set to "auto", will use the default image. |
| `type` | `typing.Optional[str]` | |
| `port` | `int \| flyte.app._types.Port` | |
| `args` | `*args` | |
| `command` | `typing.Union[typing.List[str], str, NoneType]` | |
| `requires_auth` | `bool` | |
| `scaling` | `flyte.app._types.Scaling` | |
| `domain` | `flyte.app._types.Domain \| None` | |
| `links` | `typing.List[flyte.app._types.Link]` | |
| `include` | `typing.List[str]` | |
| `inputs` | `typing.List[flyte.app._input.Input]` | |
| `cluster_pool` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) |  |
| [`container_cmd()`](#container_cmd) |  |
| [`get_port()`](#get_port) |  |


### add_dependency()

```python
def add_dependency(
    env: Environment,
)
```
Add a dependency to the environment.


| Parameter | Type | Description |
|-|-|-|
| `env` | `Environment` | |

### clone_with()

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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | |
| `resources` | `Optional[Resources]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `depends_on` | `Optional[List[Environment]]` | |
| `description` | `Optional[str]` | |
| `kwargs` | `**kwargs` | |

### container_args()

```python
def container_args(
    serialize_context: flyte.models.SerializationContext,
) -> typing.List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `flyte.models.SerializationContext` | |

### container_cmd()

```python
def container_cmd(
    serialize_context: flyte.models.SerializationContext,
) -> typing.List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `flyte.models.SerializationContext` | |

### get_port()

```python
def get_port()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |

