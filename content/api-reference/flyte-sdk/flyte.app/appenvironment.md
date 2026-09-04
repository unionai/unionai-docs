---
title: AppEnvironment
description: "Configure a long-running app environment for APIs, dashboards, or model servers."
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# AppEnvironment

**Package:** `flyte.app`

Configure a long-running app environment for APIs, dashboards, or model servers.

```python
app_env = flyte.app.AppEnvironment(
    name="my-api",
    image=flyte.Image.from_debian_base(python="3.12").with_pip_packages("fastapi", "uvicorn"),
    port=8080,
    scaling=flyte.app.Scaling(replicas=(1, 3)),
)
```



## Parameters

```python
class AppEnvironment(
    name: str,
    depends_on: List[Environment] = <factory>,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    description: Optional[str] = None,
    secrets: Optional[SecretRequest] = None,
    env_vars: Optional[Dict[str, str]] = None,
    resources: Optional[Resources] = None,
    interruptible: bool = False,
    image: Union[str, Image, Literal['auto'], None] = 'auto',
    include: Tuple[str, ...] = <factory>,
    service_account: Optional[str] = None,
    type: Optional[str] = None,
    port: int | Port = 8080,
    args: Optional[Union[List[str], str]] = None,
    command: Optional[Union[List[str], str]] = None,
    requires_auth: bool = True,
    scaling: Scaling = <factory>,
    domain: Domain | None = <factory>,
    links: List[Link] = <factory>,
    parameters: List[Parameter] = <factory>,
    cluster_pool: str = 'default',
    timeouts: Timeouts = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the app (required). Must be lowercase alphanumeric with hyphens. Inherited from Environment. |
| `depends_on` | `List[Environment]` | Dependencies on other environments (deployed together). Inherited from Environment. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject. Inherited from Environment. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables. Inherited from Environment. |
| `resources` | `Optional[Resources]` | Compute resources (CPU, memory, GPU). Inherited from Environment. |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto'], None]` | Docker image for the environment. Inherited from Environment. |
| `include` | `Tuple[str, ...]` | |
| `service_account` | `Optional[str]` | |
| `type` | `Optional[str]` | App type identifier (e.g., `"streamlit"`, `"fastapi"`). When set, the platform may apply framework-specific defaults. |
| `port` | `int \| Port` | Port for the app server. Default `8080`. Ports 8012, 8022, 8112, 9090, and 9091 are reserved and cannot be used. Can also be a `Port` object for advanced configuration. |
| `args` | `Optional[Union[List[str], str]]` | Arguments passed to the app process. Can be a list of strings or a single string. Used for script-based apps (e.g., Streamlit's `["--server.port", "8080"]`). |
| `command` | `Optional[Union[List[str], str]]` | Full command to run in the container. Alternative to `args` — use when you need to override the container's entrypoint entirely. |
| `requires_auth` | `bool` | Whether the app endpoint requires authentication. Default `True`. Set to `False` for public endpoints. |
| `scaling` | `Scaling` | `Scaling` object controlling replicas and autoscaling behavior. Default is `Scaling()` (scale-to-zero, max 1 replica). |
| `domain` | `Domain \| None` | `Domain` object for custom domain configuration. |
| `links` | `List[Link]` | List of `Link` objects for connecting to other environments. |
| `parameters` | `List[Parameter]` | List of `Parameter` objects for app inputs. Use `RunOutput` to connect app parameters to task outputs, `ArtifactValue` to resolve a published artifact (e.g. a prefetched model), or `AppEndpoint` to reference other app endpoints. |
| `cluster_pool` | `str` | Cluster pool for scheduling. Default `"default"`. |
| `timeouts` | `Timeouts` | `Timeouts` object for startup/health check timeouts. |

## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |
| [`container_args()`](#container_args) |  |
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
    depends_on: Optional[List[Environment]] = None,
    description: Optional[str] = None,
    interruptible: Optional[bool] = None,
    service_account: Optional[str] = None,
    **kwargs: Any,
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
| `service_account` | `Optional[str]` | |
| `**kwargs` | `Any` | |

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

