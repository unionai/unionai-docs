---
title: OMLXAppEnvironment
description: "App environment backed by [oMLX](https://github.com/jundot/omlx) for serving LLMs on Apple Silicon Macs."
icon: braces
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# OMLXAppEnvironment

**Package:** `flyteplugins.omlx`

App environment backed by [oMLX](https://github.com/jundot/omlx) for serving
LLMs on Apple Silicon Macs.

oMLX is an OpenAI-compatible inference server built on Apple's MLX framework.
It is **macOS + Apple Silicon only**. On a flyte devbox started with
`--apple-silicon`, this environment requests `gpu="AppleSilicon"` by default, so
the devbox's bridge runs `omlx serve` natively on the Mac (in an environment built
from the image's pip packages) and forwards the app's URL, port and logs.

```bash
flyte start devbox --apple-silicon
flyte create config --devbox
python examples/accelerators/omlx_serve.py
```

The user is responsible for installing `omlx` on the host machine:

```bash
brew tap jundot/omlx https://github.com/jundot/omlx && brew install omlx
# or: pip install git+https://github.com/jundot/omlx
```



## Parameters

```python
class OMLXAppEnvironment(
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
    image: str | Image | Literal['auto'] = Image(base_image='ghcr.io/flyteorg/flyte:py3.12-v2.12.1', dockerfile=None, registry=None, name='omlx-app-image', platform=('linux/amd64', 'linux/arm64'), python_version=(3, 12), extendable=True, _is_cloned=True, _ref_name=None, _layers=(PipPackages(pre=True, packages=('flyteplugins-omlx',)),), _tag=None, _image_registry_secret=None),
    type: str = 'oMLX',
    port: int | Port = 8000,
    extra_args: str | list[str] = '',
    model_dir: str = '',
    model_id: str = '',
    api_key: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the application. |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Secrets requested by the app. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables for the server process. |
| `resources` | `Optional[Resources]` | Compute resources. Defaults to `gpu="AppleSilicon"` so the app runs on the Mac's GPU via the devbox bridge; other GPU types are rejected. |
| `interruptible` | `bool` | |
| `include` | `Tuple[str, ...]` | |
| `service_account` | `Optional[str]` | |
| `args` | `Optional[Union[List[str], str]]` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | Whether the public URL requires Flyte auth. |
| `scaling` | `Scaling` | Scaling configuration. |
| `domain` | `Domain \| None` | Custom domain for the deployed app. |
| `links` | `List[Link]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | Target cluster pool. |
| `cluster` | `str \| None` | |
| `timeouts` | `Timeouts` | |
| `image` | `str \| Image \| Literal['auto']` | Container image. oMLX cannot run inside Linux containers, so this mostly describes the pip *packages* that get rebuilt into the Mac's host environment. Leave as default for the devbox workflow; you typically only override it to add pip packages (e.g. `with_pip_packages("omlx @ git+...")`). |
| `type` | `str` | App type tag. |
| `port` | `int \| Port` | Port the oMLX server listens on. Defaults to 8000 (oMLX's own default). |
| `extra_args` | `str \| list[str]` | Extra CLI args appended to `omlx serve`. See `omlx serve --help` for the full list (`--max-model-memory`, `--max-concurrent-requests`, `--paged-ssd-cache-dir`, `--hf-endpoint`, `--log-level`, etc.). |
| `model_dir` | `str` | Local directory of MLX models, passed to `omlx serve --model-dir`. Each subdirectory is exposed as a separate `model_id`. If unset, oMLX falls back to `~/.omlx/models`. |
| `model_id` | `str` | Optional friendly id surfaced in the Flyte UI and usable as the `model` in OpenAI client requests. oMLX derives actual served ids from `--model-dir` subdirectories or HuggingFace repo ids. |
| `api_key` | `str` | Optional API key for the oMLX server (sent through `--api-key`). For real secrets, prefer `secrets` + `env_vars`. |

## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) | Return the container arguments for oMLX. |
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
) -> OMLXAppEnvironment
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
Return the container arguments for oMLX.


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

