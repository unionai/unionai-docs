---
title: AppEnvironment
version: 2.0.0b38
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
    type: Optional[str],
    port: int | Port,
    args: *args,
    command: Optional[Union[List[str], str]],
    requires_auth: bool,
    scaling: Scaling,
    domain: Domain | None,
    links: List[Link],
    include: List[str],
    inputs: List[Input],
    cluster_pool: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the app environment |
| `depends_on` | `List[Environment]` | Environment dependencies to hint, so when you deploy the environment, the dependencies are also deployed. This is useful when you have a set of environments that depend on each other. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject into the environment. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables to set for the environment. |
| `resources` | `Optional[Resources]` | Resources to allocate for the environment. |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto']]` | Docker image to use for the environment. If set to "auto", will use the default image. |
| `type` | `Optional[str]` | Type of the environment. |
| `port` | `int \| Port` | Port to use for the app server. |
| `args` | `*args` | Arguments to pass to app. |
| `command` | `Optional[Union[List[str], str]]` | Command to run in the app. |
| `requires_auth` | `bool` | Whether the app requires authentication. |
| `scaling` | `Scaling` | Scaling configuration for the app environment. |
| `domain` | `Domain \| None` | Domain to use for the app. |
| `links` | `List[Link]` | Links to other environments. |
| `include` | `List[str]` | Files to include in the environment to run the app. |
| `inputs` | `List[Input]` | Inputs to pass to the app environment. |
| `cluster_pool` | `str` | Cluster pool to use for the app environment. |

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
    env_vars: Optional[dict[str, str]],
    secrets: Optional[SecretRequest],
    depends_on: Optional[List[Environment]],
    description: Optional[str],
    interruptible: Optional[bool],
    kwargs: **kwargs,
) -> AppEnvironment
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | |
| `resources` | `Optional[Resources]` | |
| `env_vars` | `Optional[dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `depends_on` | `Optional[List[Environment]]` | |
| `description` | `Optional[str]` | |
| `interruptible` | `Optional[bool]` | |
| `kwargs` | `**kwargs` | |

### container_args()

```python
def container_args(
    serialize_context: SerializationContext,
) -> List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `SerializationContext` | |

### container_cmd()

```python
def container_cmd(
    serialize_context: SerializationContext,
    input_overrides: list[Input] | None,
) -> List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `SerializationContext` | |
| `input_overrides` | `list[Input] \| None` | |

### get_port()

```python
def get_port()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |

