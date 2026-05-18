---
title: AgentChatAppEnvironment
version: 2.3.2
variants: +flyte +union
layout: py_api
---

# AgentChatAppEnvironment

**Package:** `flyte.ai.chat.app`

An :class:`~flyte.app.AppEnvironment` that spins up a FastAPI chat
interface backed by any object satisfying the :class:`Agent` protocol.

Parameters
----------
agent:
    Any object implementing the :class:`Agent` protocol.
title:
    Title displayed in the UI header and browser tab. Defaults to
    the environment *name*.
subtitle:
    Optional short subtitle displayed below the title in the
    header area.  Use it to explain what the agent does.
prompt_nudges:
    Optional list of prompt-nudge cards shown before the first
    message.  Each entry is a dict with ``"label"`` (short card
    title) and ``"prompt"`` (the query text sent when clicked).
theme:
    Optional :class:`CustomTheme` instance that controls the UI
    accent colors via human-readable attributes.  When provided,
    the theme CSS is generated automatically and prepended to any
    *custom_css*.
custom_css:
    Optional CSS string appended **after** the default styles
    (and after theme CSS, if a *theme* is provided).  Use this
    for fine-grained overrides beyond what :class:`CustomTheme`
    exposes.
logo_url:
    Optional URL to an image displayed to the left of the title
    in the header bar.  When ``None`` (default), no logo is shown.
additional_buttons:
    Optional list of action-button dicts rendered to the right of
    the *Send* button.  Each dict must have ``"button_text"`` and
    ``"button_url"`` keys.  The first entry is displayed as a
    prominent primary button; any extra entries appear in a
    drop-up menu accessed via a chevron.
passthrough_auth:
    When ``True``, the FastAPI app initializes ``flyte.init_passthrough`` at
    startup and adds ``FastAPIPassthroughAuthMiddleware`` so incoming
    ``Authorization`` / cookie headers are forwarded to Flyte remote calls.
    Enable this when using ``CodeModeAgent`` with ``@env.task`` tools —
    nested task execution needs caller credentials (same pattern as
    ``FlyteWebhookAppEnvironment``).
passthrough_auth_excluded_paths:
    Paths skipped by passthrough middleware. When omitted, defaults include
    the HTML shell (``/``), ``/api/tools``, ``/api/nudges``, health, and docs
    routes so the sidebar and nudges load without ``Authorization`` headers;
    ``/api/chat`` still requires credentials. Only used when ``passthrough_auth``
    is ``True``.
task_entrypoint:
    Optional Flyte task used as the chat handler entrypoint.

    When set, ``/api/chat`` calls the task (via ``task_entrypoint.aio``)
    instead of calling ``agent.run`` directly. This is useful for agents
    whose tool calls must run under a parent task context (e.g. a
    ``CodeModeAgent`` using durable ``@env.task`` tools). When streaming
    chat (``stream: true``), progress lines use :meth:`~flyte.remote.Run.watch`
    on the returned run (first ``RUNNING`` → ``generating_code``, next →
    ``executing``). Fine-grained codemode phases still require
    ``agent.run`` in the web process, or future worker-side signaling.

    The entrypoint may accept either:

    - ``(message: str, history: list[dict[str, str]])``; or
    - ``(message: str)``.

    The return value may be an :class:`~flyte.ai.agents.protocol.AgentResult`,
    a dict with keys like ``summary``/``charts``/``code``, or a plain string
    (treated as ``summary``).


## Parameters

```python
class AgentChatAppEnvironment(
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
    type: str,
    agent: Any,
    title: str | None,
    subtitle: str | None,
    prompt_nudges: list[dict[str, str]],
    theme: CustomTheme | None,
    custom_css: str,
    logo_url: str | None,
    additional_buttons: list[dict[str, str]],
    passthrough_auth: bool,
    passthrough_auth_excluded_paths: frozenset[str] | None,
    task_entrypoint: Any | None,
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
| `image` | `Union[str, Image, Literal['auto'], None]` | |
| `include` | `Tuple[str, ...]` | |
| `port` | `int \| Port` | |
| `args` | `*args` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | |
| `scaling` | `Scaling` | |
| `domain` | `Domain \| None` | |
| `links` | `List[Link]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | |
| `timeouts` | `Timeouts` | |
| `type` | `str` | |
| `agent` | `Any` | |
| `title` | `str \| None` | |
| `subtitle` | `str \| None` | |
| `prompt_nudges` | `list[dict[str, str]]` | |
| `theme` | `CustomTheme \| None` | |
| `custom_css` | `str` | |
| `logo_url` | `str \| None` | |
| `additional_buttons` | `list[dict[str, str]]` | |
| `passthrough_auth` | `bool` | |
| `passthrough_auth_excluded_paths` | `frozenset[str] \| None` | |
| `task_entrypoint` | `Any \| None` | |
| `_caller_frame` | `inspect.FrameInfo \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`build_fastapi_app()`](#build_fastapi_app) | Construct the FastAPI application (routes, HTML shell, optional auth). |
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

### build_fastapi_app()

```python
def build_fastapi_app()
```
Construct the FastAPI application (routes, HTML shell, optional auth).

Useful for tests and advanced mounting; the deployed server uses this via
:meth:`_fastapi_server`.


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

