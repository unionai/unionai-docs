---
title: FastAPIAppEnvironment
version: 2.0.0b38
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FastAPIAppEnvironment

**Package:** `flyte.app.extras`

```python
class FastAPIAppEnvironment(
    name: str,
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto']],
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
    type: str,
    app: fastapi.FastAPI,
    _caller_frame: inspect.FrameInfo | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `resources` | `Optional[Resources]` | |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto']]` | |
| `port` | `int \| Port` | |
| `args` | `*args` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | |
| `scaling` | `Scaling` | |
| `domain` | `Domain \| None` | |
| `links` | `List[Link]` | |
| `include` | `List[str]` | |
| `inputs` | `List[Input]` | |
| `cluster_pool` | `str` | |
| `type` | `str` | |
| `app` | `fastapi.FastAPI` | |
| `_caller_frame` | `inspect.FrameInfo \| None` | |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) | Generate the container arguments for running the FastAPI app with uvicorn. |
| [`container_cmd()`](#container_cmd) |  |
| [`container_command()`](#container_command) |  |
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
    serialization_context: flyte.models.SerializationContext,
) -> list[str]
```
Generate the container arguments for running the FastAPI app with uvicorn.

Returns:
    A list of command arguments in the format:
    ["uvicorn", "&lt;module_name&gt;:&lt;app_var_name&gt;", "--port", "&lt;port&gt;"]


| Parameter | Type | Description |
|-|-|-|
| `serialization_context` | `flyte.models.SerializationContext` | |

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

### container_command()

```python
def container_command(
    serialization_context: flyte.models.SerializationContext,
) -> list[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialization_context` | `flyte.models.SerializationContext` | |

### get_port()

```python
def get_port()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |

