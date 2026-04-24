---
title: AppEnvironment
version: 2.1.10.dev6+ga8f3f9bfa
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
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto'], None],
    include: Tuple[str, ...],
    type: Optional[str],
    port: int | Port,
    args: *args,
    command: Optional[Union[List[str], str]],
    requires_auth: bool,
    scaling: Scaling,
    domain: Domain | None,
    links: List[Link],
    parameters: List[Parameter],
    cluster_pool: str,
    timeouts: Timeouts,
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
| `type` | `Optional[str]` | App type identifier (e.g., `"streamlit"`, `"fastapi"`). When set, the platform may apply framework-specific defaults. |
| `port` | `int \| Port` | Port for the app server. Default `8080`. Ports 8012, 8022, 8112, 9090, and 9091 are reserved and cannot be used. Can also be a `Port` object for advanced configuration. |
| `args` | `*args` | Arguments passed to the app process. Can be a list of strings or a single string. Used for script-based apps (e.g., Streamlit's `["--server.port", "8080"]`). |
| `command` | `Optional[Union[List[str], str]]` | Full command to run in the container. Alternative to `args` — use when you need to override the container's entrypoint entirely. |
| `requires_auth` | `bool` | Whether the app endpoint requires authentication. Default `True`. Set to `False` for public endpoints. |
| `scaling` | `Scaling` | `Scaling` object controlling replicas and autoscaling behavior. Default is `Scaling()` (scale-to-zero, max 1 replica). |
| `domain` | `Domain \| None` | `Domain` object for custom domain configuration. |
| `links` | `List[Link]` | List of `Link` objects for connecting to other environments. |
| `parameters` | `List[Parameter]` | List of `Parameter` objects for app inputs. Use `RunOutput` to connect app parameters to task outputs, or `AppEndpoint` to reference other app endpoints. |
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
    env: Environment,
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
| `env` | `Environment` | One or more `Environment` instances to add as dependencies. |

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

