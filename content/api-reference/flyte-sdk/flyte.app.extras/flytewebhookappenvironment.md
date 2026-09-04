---
title: FlyteWebhookAppEnvironment
description: "A pre-built FastAPI app environment for common Flyte webhook operations."
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# FlyteWebhookAppEnvironment

**Package:** `flyte.app.extras`

A pre-built FastAPI app environment for common Flyte webhook operations.

This environment provides a ready-to-use FastAPI application with endpoints for:
- Running tasks in a specific domain/project/version
- Getting run I/O and metadata
- Aborting runs
- Getting task metadata
- Building images
- Activating/deactivating apps (except itself)
- Getting app status
- Calling other app endpoints
- Activating/deactivating triggers
- Prefetching HuggingFace models (run, status, I/O, abort)

All endpoints use FastAPIPassthroughAuthMiddleware for authentication.



## Parameters

```python
class FlyteWebhookAppEnvironment(
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
    image: flyte.Image = <factory>,
    type: str = 'FlyteWebhookApp',
    uvicorn_config: 'uvicorn.Config | None' = None,
    title: str | None = None,
    endpoint_groups: list[WebhookEndpointGroup] | tuple[WebhookEndpointGroup, ...] | None = None,
    endpoints: list[WebhookEndpoint] | tuple[WebhookEndpoint, ...] | None = None,
    task_allowlist: list[str] | None = None,
    app_allowlist: list[str] | None = None,
    trigger_allowlist: list[str] | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the webhook app environment |
| `depends_on` | `List[Environment]` | Environment dependencies |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | Description for the FastAPI app (optional) |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject into the environment |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `resources` | `Optional[Resources]` | Resources to allocate for the environment |
| `interruptible` | `bool` | |
| `include` | `Tuple[str, ...]` | |
| `service_account` | `Optional[str]` | |
| `port` | `int \| Port` | |
| `args` | `Optional[Union[List[str], str]]` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | Whether the app requires authentication (default: True) |
| `scaling` | `Scaling` | Scaling configuration for the app environment |
| `domain` | `Domain \| None` | |
| `links` | `List[Link]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | |
| `timeouts` | `Timeouts` | |
| `image` | `flyte.Image` | Docker image to use for the environment |
| `type` | `str` | |
| `uvicorn_config` | `'uvicorn.Config \| None'` | |
| `title` | `str \| None` | Title for the FastAPI app (optional) |
| `endpoint_groups` | `list[WebhookEndpointGroup] \| tuple[WebhookEndpointGroup, ...] \| None` | List of endpoint groups to enable. If None (and endpoints is None), all endpoints are enabled. Available groups (see WebhookEndpointGroup type): - "all": All available endpoints - "core": Health check and user info ("health", "me") - "task": Task operations ("run_task", "get_task") - "run": Run operations ("get_run", "get_run_io", "abort_run") - "app": App operations ("get_app", "activate_app", "deactivate_app", "call_app") - "trigger": Trigger operations ("activate_trigger", "deactivate_trigger") - "build": Image build operations ("build_image") - "prefetch": HuggingFace prefetch operations ("prefetch_hf_model",              "get_prefetch_hf_model", "get_prefetch_hf_model_io", "abort_prefetch_hf_model") |
| `endpoints` | `list[WebhookEndpoint] \| tuple[WebhookEndpoint, ...] \| None` | List of individual endpoints to enable. Can be used alone or combined with endpoint_groups. Available endpoints (see WebhookEndpoint type): - "health": Health check endpoint - "me": Get current user info - "run_task": Run a task - "get_task": Get task metadata - "get_run": Get run status - "get_run_io": Get run inputs/outputs - "abort_run": Abort a run - "get_app": Get app status - "activate_app": Activate an app - "deactivate_app": Deactivate an app - "call_app": Call another app's endpoint - "activate_trigger": Activate a trigger - "deactivate_trigger": Deactivate a trigger - "build_image": Build a container image - "prefetch_hf_model": Prefetch a HuggingFace model - "get_prefetch_hf_model": Get prefetch run status - "get_prefetch_hf_model_io": Get prefetch run I/O - "abort_prefetch_hf_model": Abort a prefetch run |
| `task_allowlist` | `list[str] \| None` | List of allowed task identifiers. When set, only tasks matching the allowlist can be accessed via task endpoints. Supports formats: - "domain/project/name" for exact match - "project/name" for project/name match (any domain) - "name" for name-only match (any domain/project) |
| `app_allowlist` | `list[str] \| None` | List of allowed app names. When set, only apps matching the allowlist can be accessed via app endpoints. |
| `trigger_allowlist` | `list[str] \| None` | List of allowed trigger identifiers. When set, only triggers matching the allowlist can be accessed via trigger endpoints. Supports formats: - "task_name/trigger_name" for exact match - "trigger_name" for name-only match (any task) |

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
| [`container_command()`](#container_command) |  |
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

### container_command()

```python
def container_command(
    serialization_context: SerializationContext,
) -> list[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialization_context` | `SerializationContext` | |

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

