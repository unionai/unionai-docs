---
title: WebhookAppEnvironment
description: "Dashboard plus a verified webhook receiver for one or more providers."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# WebhookAppEnvironment

**Package:** `flyte.extras.webhooks`

Dashboard plus a verified webhook receiver for one or more providers.



## Parameters

```python
class WebhookAppEnvironment(
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
    type: str = 'FastAPI',
    app: FastAPI | None = None,
    uvicorn_config: uvicorn.Config | None = None,
    providers: Sequence[Provider] = (),
    scopes: list[str] = <factory>,
    webhook_prefix: str = '/webhook',
    require_signature: bool = True,
    max_recent_events: int = 200,
    event_handlers: list[tuple[str, EventHandler]] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | App environment name, and the app name on the platform. |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | Extra secrets to mount. Each provider's own secret is added automatically from its `default_secret_env`, so it only needs naming here to point it at a secret stored under a different key. |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `resources` | `Optional[Resources]` | |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto'], None]` | |
| `include` | `Tuple[str, ...]` | |
| `service_account` | `Optional[str]` | |
| `port` | `int \| Port` | |
| `args` | `Optional[Union[List[str], str]]` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | |
| `scaling` | `Scaling` | |
| `domain` | `Domain \| None` | |
| `links` | `List[Link]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | |
| `timeouts` | `Timeouts` | |
| `type` | `str` | |
| `app` | `FastAPI \| None` | |
| `uvicorn_config` | `uvicorn.Config \| None` | |
| `providers` | `Sequence[Provider]` | Which providers to accept, by name (`github`, `slack`, `linear`, `clickup`, `jira`). Each gets a route at `{webhook_prefix}/{name}`; anything not listed 404s. |
| `scopes` | `list[str]` | Optional allowlist of repositories / channels / teams / lists / project keys. Events from anywhere else are acknowledged but not dispatched, as are events carrying no scope at all — an allowlist cannot vouch for an event it cannot attribute. |
| `webhook_prefix` | `str` | URL prefix for the receiver routes. |
| `require_signature` | `bool` | Reject deliveries that fail verification. When True and a provider's secret is not mounted, that provider's deliveries are refused with an explanatory error. Set False for local development only. |
| `max_recent_events` | `int` | Size of the in-memory buffer shown on the dashboard. |
| `event_handlers` | `list[tuple[str, EventHandler]]` | Optional initial `(pattern, handler)` list; prefer the `on_event` decorator. |

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
| [`on_event()`](#on_event) | Register an async handler for webhook events. |
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
### on_event()

```python
def on_event(
    event_type: str = '',
) -> Callable[[EventHandler], EventHandler]
```
Register an async handler for webhook events.



| Parameter | Type | Description |
|-|-|-|
| `event_type` | `str` | The event to match. Prefer the typed constants in `flyteplugins.webhooks.events` — `events.github.PullRequest.OPENED` for one action, `events.github.PullRequest.ANY` for every action on that type. Raw strings still work, which is the escape hatch for events the constants do not cover yet. An empty string matches every event from every configured provider. |

**Returns:** A decorator that registers the handler and returns it unchanged.

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

