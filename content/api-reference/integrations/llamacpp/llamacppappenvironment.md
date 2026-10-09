---
title: LlamaCppAppEnvironment
description: "App environment backed by llama.cpp (llama-server) for serving GGUF models."
icon: braces
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# LlamaCppAppEnvironment

**Package:** `flyteplugins.llamacpp`

App environment backed by llama.cpp (llama-server) for serving GGUF models.

This environment serves an OpenAI-compatible endpoint (under `/v1`) plus the llama.cpp
Web UI, with the specified GGUF model and configuration. llama.cpp shines where vLLM and
SGLang don't fit: quantized GGUF weights, partial CPU offload of models larger than VRAM,
and CPU-only serving.



## Parameters

```python
class LlamaCppAppEnvironment(
    name: str,
    depends_on: List[Environment] = <factory>,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    description: Optional[str] = None,
    secrets: Optional[SecretRequest] = None,
    env_vars: Optional[Dict[str, str]] = None,
    resources: Optional[Resources] = None,
    interruptible: bool = False,
    include: Tuple[str, ...] = <factory>,
    service_account: Optional[str] = None,
    args: Optional[Union[List[str], str]] = None,
    command: Optional[Union[List[str], str]] = None,
    requires_auth: bool = True,
    scaling: Scaling = <factory>,
    domain: Domain | None = <factory>,
    links: List[Link] = <factory>,
    parameters: List[Parameter] = <factory>,
    cluster_pool: str = 'default',
    cluster: str | None = None,
    timeouts: Timeouts = <factory>,
    image: str | Image | Literal['auto'] = Image(base_image='ghcr.io/flyteorg/flyte:py3.12-v2.11.2', dockerfile=None, registry=None, name='llama-cpp-app-image', platform=('linux/amd64', 'linux/arm64'), python_version=(3, 12), extendable=True, _is_cloned=True, _ref_name=None, _layers=(AptPackages(git='build-essential'), Commands(wget https://developer.download.nvidia.com/compute/cuda/repos/debian12/x86_64/cuda-keyring_1.1-1_all.deb='dpkg -i cuda-keyring_1.1-1_all.deb'), Commands(wget -q https://nodejs.org/dist/v22.12.0/node-v22.12.0-linux-x64.tar.xz -O /tmp/node.tar.xz='mkdir -p /opt/node && tar -xJf /tmp/node.tar.xz -C /opt/node --strip-components=1 && rm /tmp/node.tar.xz'), Env(env_vars=(('PATH', '/opt/llama.cpp/build/bin:/usr/local/cuda-12.8/bin:$PATH'), ('LLAMA_CACHE', '/tmp/llama.cpp/cache'), ('CUDA_HOME', '/usr/local/cuda-12.8'))), PipPackages(pre=True, packages=('flyteplugins-llamacpp',))), _tag=None, _image_registry_secret=None),
    type: str = 'llama.cpp',
    port: int | Port = 8080,
    extra_args: str | list[str] = '',
    model_path: str | RunOutput | ArtifactValue = '',
    model_hf_path: str = '',
    model_id: str = '',
    draft_model_path: str | RunOutput | ArtifactValue = '',
    draft_model_hf_path: str = '',
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
| `include` | `Tuple[str, ...]` | |
| `service_account` | `Optional[str]` | |
| `args` | `Optional[Union[List[str], str]]` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | Whether the public URL requires authentication. |
| `scaling` | `Scaling` | Scaling configuration for the app environment. |
| `domain` | `Domain \| None` | Domain to use for the app. |
| `links` | `List[Link]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | The target cluster_pool where the app should be deployed. |
| `cluster` | `str \| None` | |
| `timeouts` | `Timeouts` | |
| `image` | `str \| Image \| Literal['auto']` | |
| `type` | `str` | Type of app. |
| `port` | `int \| Port` | Port the application listens on. Defaults to 8080. |
| `extra_args` | `str \| list[str]` | Extra args to pass to `llama-server`, e.g. `"--ctx-size 32768 --jinja"`. Run `llama-server --help` or see https://github.com/ggml-org/llama.cpp/tree/master/tools/server for details. |
| `model_path` | `str \| RunOutput \| ArtifactValue` | Remote path to the GGUF weights -- a directory containing `.gguf` file(s) or a direct path to one (e.g. s3://bucket/path/to/model), or a `RunOutput`/`ArtifactValue` resolved at deploy time. The weights are downloaded into the container and the served `.gguf` is located at startup (for sharded models, the `-00001-of-` shard is picked; llama-server finds the rest). |
| `model_hf_path` | `str` | Hugging Face GGUF repo, optionally with a quant tag (e.g. `ggml-org/gemma-3-4b-it-GGUF:Q4_K_M`). Passed to llama-server as `--hf-repo`, which downloads the weights at startup. |
| `model_id` | `str` | Model id exposed by the server (llama-server's `--alias`). |
| `draft_model_path` | `str \| RunOutput \| ArtifactValue` | Remote path to the draft model GGUF used for speculative decoding, or a `RunOutput`/`ArtifactValue` resolved at deploy time. Downloaded alongside the target model and passed as `--model-draft`. Tune the speculation via `extra_args` (`--draft-max`, `--draft-min`, `--gpu-layers-draft`, ...). |
| `draft_model_hf_path` | `str` | Hugging Face GGUF repo for the draft model, as an alternative to `draft_model_path`. Passed as `--hf-repo-draft`. |

## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) | Return the container arguments for llama.cpp. |
| [`container_cmd()`](#container_cmd) |  |
| [`get_port()`](#get_port) |  |
| [`on_shutdown()`](#on_shutdown) | Decorator to define the shutdown function for the app environment. |
| [`on_startup()`](#on_startup) | Decorator to define the startup function for the app environment. |
| [`server()`](#server) | Decorator to define the server function for the app environment. |


### add_dependency()

```python
def add_dependency(
    *env: Environment,
)
```
Add one or more environment dependencies so they are deployed together.

When you deploy this environment, any environments added via
`add_dependency` will also be deployed. This is an alternative to
passing `depends_on=[...]` at construction time, useful when the
dependency is defined after the environment is created.

Duplicate dependencies are silently ignored. An environment cannot
depend on itself.



| Parameter | Type | Description |
|-|-|-|
| `*env` | `Environment` | One or more `Environment` instances to add as dependencies. |

### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]] = None,
    resources: Optional[Resources] = None,
    env_vars: Optional[dict[str, str]] = None,
    secrets: Optional[SecretRequest] = None,
    depends_on: Optional[list[Environment]] = None,
    description: Optional[str] = None,
    interruptible: Optional[bool] = None,
    **kwargs: Any,
) -> LlamaCppAppEnvironment
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
| `**kwargs` | `Any` | |

### container_args()

```python
def container_args(
    serialization_context: SerializationContext,
) -> list[str]
```
Return the container arguments for llama.cpp.


| Parameter | Type | Description |
|-|-|-|
| `serialization_context` | `SerializationContext` | |

### container_cmd()

```python
def container_cmd(
    serialize_context: SerializationContext,
    parameter_overrides: list[Parameter] | None = None,
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
    fn: F,
) -> F
```
Decorator to define the shutdown function for the app environment.

This function is called after the server function is called.

This decorated function can be a sync or async function, and accepts input
parameters based on the Parameters defined in the AppEnvironment
definition.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `F` | |

### on_startup()

```python
def on_startup(
    fn: F,
) -> F
```
Decorator to define the startup function for the app environment.

This function is called before the server function is called.

The decorated function can be a sync or async function, and accepts input
parameters based on the Parameters defined in the AppEnvironment
definition.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `F` | |

### server()

```python
def server(
    fn: F,
) -> F
```
Decorator to define the server function for the app environment.

This decorated function can be a sync or async function, and accepts input
parameters based on the Parameters defined in the AppEnvironment
definition.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `F` | |

