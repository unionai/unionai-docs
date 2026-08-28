---
title: SGLangAppEnvironment
version: 2.6.10
variants: +flyte +union
layout: py_api
---

# SGLangAppEnvironment

**Package:** `flyteplugins.sglang`

App environment backed by SGLang for serving large language models.

This environment sets up an SGLang server with the specified model and configuration.



## Parameters

```python
class SGLangAppEnvironment(
    name: str,
    depends_on: List[Environment] = <factory>,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    description: Optional[str] = None,
    secrets: Optional[SecretRequest] = None,
    env_vars: Optional[Dict[str, str]] = None,
    resources: Optional[Resources] = None,
    interruptible: bool = False,
    include: Tuple[str, ...] = <factory>,
    args: Optional[Union[List[str], str]] = None,
    command: Optional[Union[List[str], str]] = None,
    requires_auth: bool = True,
    scaling: Scaling = <factory>,
    domain: Domain | None = <factory>,
    links: List[Link] = <factory>,
    parameters: List[Parameter] = <factory>,
    cluster_pool: str = 'default',
    timeouts: Timeouts = <factory>,
    image: str | Image | Literal['auto'] = Image(base_image='ghcr.io/flyteorg/flyte:py3.12-v2.6.10', dockerfile=None, registry=None, name='sglang-app-image', platform=('linux/amd64', 'linux/arm64'), python_version=(3, 12), extendable=True, _is_cloned=True, _ref_name=None, _layers=(AptPackages(libnuma-dev='wget'), Commands(wget https://developer.download.nvidia.com/compute/cuda/repos/debian12/x86_64/cuda-keyring_1.1-1_all.deb='dpkg -i cuda-keyring_1.1-1_all.deb'), Commands("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && . $HOME/.cargo/env"), Env(env_vars=(('CUDA_HOME', '/usr/local/cuda-13.0'), ('PATH', '/root/.cargo/bin:/usr/local/cuda-13.0/bin:$PATH'))), PipPackages(pre=True, packages=('flyteplugins-sglang',)), PipPackages(pre=True, packages=('sglang==0.5.16',)), PipPackages(pre=True, packages=('sglang-router==0.3.2',))), _tag=None, _image_registry_secret=None),
    type: str = 'SGLang',
    port: int | Port = 8080,
    extra_args: str | list[str] = '',
    model_path: str | RunOutput | ArtifactValue = '',
    model_hf_path: str = '',
    model_id: str = '',
    stream_model: bool = True,
    draft_model_path: str | RunOutput | ArtifactValue = '',
    draft_model_hf_path: str = '',
    speculative_config: Optional[dict[str, Any]] = None,
    router: bool = False,
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
| `args` | `Optional[Union[List[str], str]]` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | Whether the public URL requires authentication. |
| `scaling` | `Scaling` | Scaling configuration for the app environment. |
| `domain` | `Domain \| None` | Domain to use for the app. |
| `links` | `List[Link]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | The target cluster_pool where the app should be deployed. |
| `timeouts` | `Timeouts` | |
| `image` | `str \| Image \| Literal['auto']` | |
| `type` | `str` | Type of app. |
| `port` | `int \| Port` | Port application listens to. Defaults to 8000 for SGLang. |
| `extra_args` | `str \| list[str]` | Extra args to pass to `python -m sglang.launch_server`. See https://docs.sglang.io/advanced_features/server_arguments.html for details. |
| `model_path` | `str \| RunOutput \| ArtifactValue` | Remote path to model (e.g., s3://bucket/path/to/model), or a `RunOutput`/`ArtifactValue` resolved at deploy time. |
| `model_hf_path` | `str` | Hugging Face path to model (e.g., Qwen/Qwen3-0.6B). |
| `model_id` | `str` | Model id that is exposed by SGLang. |
| `stream_model` | `bool` | When `model_path` is set, use True to stream weights from object storage to the GPU (Flyte loader integration). Ignored for `model_hf_path`-only apps, which use SGLang's normal Hugging Face download path. If False with `model_path`, the model is downloaded to the local filesystem first, then loaded. Also ignored when a draft model is configured, or when `router` is True -- see below. |
| `draft_model_path` | `str \| RunOutput \| ArtifactValue` | Remote path to the draft model (speculator) used for speculative decoding, or a `RunOutput`/`ArtifactValue` resolved at deploy time. The weights are downloaded alongside the target model and passed as `--speculative-draft-model-path`. Requires `speculative_config`. |
| `draft_model_hf_path` | `str` | Hugging Face path to the draft model, as an alternative to `draft_model_path` (e.g., Qwen/Qwen3-0.6B). |
| `speculative_config` | `Optional[dict[str, Any]]` | SGLang speculative decoding configuration. Each key becomes a `--speculative-<key>` server arg, so `{"algorithm": "EAGLE3", "num_draft_tokens": 16}` renders as `--speculative-algorithm EAGLE3 --speculative-num-draft-tokens 16`. The draft model path is filled in from `draft_model_path`/`draft_model_hf_path` and must not be set here. Note that SGLang auto-selects `num_steps`, `eagle_topk` and `num_draft_tokens` per model family; override them only after reading acceptance length off `/metrics`. See https://docs.sglang.io/advanced_features/speculative_decoding.html. |
| `router` | `bool` | Serve behind SGLang's cache-aware router (`sglang_router.launch_server`), which runs data-parallel workers in one process and routes each request to the worker most likely to already hold its prefix. Worker counts and routing policy are ordinary server args, e.g. `extra_args=["--dp-size", "4", "--router-policy", "cache_aware"]`. |

## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) | Return the container arguments for SGLang. |
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
) -> SGLangAppEnvironment
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
Return the container arguments for SGLang.


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

