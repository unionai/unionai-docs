---
title: VLLMAppEnvironment
version: 2.0.0
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# VLLMAppEnvironment

**Package:** `flyteplugins.vllm`

App environment backed by vLLM for serving large language models.

This environment sets up a vLLM server with the specified model and configuration.



```python
class VLLMAppEnvironment(
    name: str,
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    args: *args,
    command: Optional[Union[List[str], str]],
    requires_auth: bool,
    scaling: Scaling,
    domain: Domain | None,
    links: List[Link],
    include: List[str],
    parameters: List[Parameter],
    cluster_pool: str,
    image: str | Image | Literal['auto'],
    type: str,
    port: int | Port,
    extra_args: str | list[str],
    model_path: str | RunOutput,
    model_hf_path: str,
    model_id: str,
    stream_model: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the application. |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Secrets that are requested for application. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables to set for the application. |
| `resources` | `Optional[Resources]` | |
| `interruptible` | `bool` | |
| `args` | `*args` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | Whether the public URL requires authentication. |
| `scaling` | `Scaling` | Scaling configuration for the app environment. |
| `domain` | `Domain \| None` | Domain to use for the app. |
| `links` | `List[Link]` | |
| `include` | `List[str]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | The target cluster_pool where the app should be deployed. |
| `image` | `str \| Image \| Literal['auto']` | |
| `type` | `str` | Type of app. |
| `port` | `int \| Port` | Port application listens to. Defaults to 8000 for vLLM. |
| `extra_args` | `str \| list[str]` | Extra args to pass to `vllm serve`. See https://docs.vllm.ai/en/stable/configuration/engine_args or run `vllm serve --help` for details. |
| `model_path` | `str \| RunOutput` | Remote path to model (e.g., s3 |
| `model_hf_path` | `str` | Hugging Face path to model (e.g., Qwen/Qwen3-0.6B). |
| `model_id` | `str` | Model id that is exposed by vllm. |
| `stream_model` | `bool` | Set to True to stream model from blob store to the GPU directly. If False, the model will be downloaded to the local file system first and then loaded into the GPU. |

## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add a dependency to the environment. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) | Return the container arguments for vLLM. |
| [`container_cmd()`](#container_cmd) |  |
| [`get_port()`](#get_port) |  |
| [`on_shutdown()`](#on_shutdown) | Decorator to define the shutdown function for the app environment. |
| [`on_startup()`](#on_startup) | Decorator to define the startup function for the app environment. |
| [`server()`](#server) | Decorator to define the server function for the app environment. |


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
    depends_on: Optional[list[Environment]],
    description: Optional[str],
    interruptible: Optional[bool],
    kwargs: **kwargs,
) -> VLLMAppEnvironment
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | |
| `resources` | `Optional[Resources]` | |
| `env_vars` | `Optional[dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `depends_on` | `Optional[list[Environment]]` | |
| `description` | `Optional[str]` | |
| `interruptible` | `Optional[bool]` | |
| `kwargs` | `**kwargs` | |

### container_args()

```python
def container_args(
    serialization_context: SerializationContext,
) -> list[str]
```
Return the container arguments for vLLM.


| Parameter | Type | Description |
|-|-|-|
| `serialization_context` | `SerializationContext` | |

### container_cmd()

```python
def container_cmd(
    serialize_context: SerializationContext,
    parameter_overrides: list[Parameter] | None,
) -> List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `SerializationContext` | |
| `parameter_overrides` | `list[Parameter] \| None` | |

### get_port()

```python
def get_port()
```
### on_shutdown()

```python
def on_shutdown(
    fn: Callable[..., None],
) -> Callable[..., None]
```
Decorator to define the shutdown function for the app environment.

This function is called after the server function is called.

This decorated function can be a sync or async function, and accepts input
parameters based on the Parameters defined in the AppEnvironment
definition.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[..., None]` | |

### on_startup()

```python
def on_startup(
    fn: Callable[..., None],
) -> Callable[..., None]
```
Decorator to define the startup function for the app environment.

This function is called before the server function is called.

The decorated function can be a sync or async function, and accepts input
parameters based on the Parameters defined in the AppEnvironment
definition.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[..., None]` | |

### server()

```python
def server(
    fn: Callable[..., None],
) -> Callable[..., None]
```
Decorator to define the server function for the app environment.

This decorated function can be a sync or async function, and accepts input
parameters based on the Parameters defined in the AppEnvironment
definition.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[..., None]` | |

