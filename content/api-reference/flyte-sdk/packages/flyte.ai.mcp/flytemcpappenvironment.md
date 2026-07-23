---
title: FlyteMCPAppEnvironment
version: 2.5.12
variants: +flyte +union
layout: py_api
---

# FlyteMCPAppEnvironment

**Package:** `flyte.ai.mcp`

Serve a Flyte-facing MCP server over HTTP (FastMCP + Starlette + Uvicorn).

Use this environment when you want LLM clients to call Flyte operations
(tasks, runs, apps, triggers, docs search) through the Model Context
Protocol. Install extras with ``pip install 'flyte[mcp]'``.

**HTTP layout**

- ``GET /health`` — liveness/readiness JSON ``{"status": "healthy"}``.
- The MCP ASGI app is mounted at ``mcp_mount_path`` (default ``/flyte-mcp``). With
  the default ``transport="streamable-http"``, the session endpoint is
  ``{mcp_mount_path}/mcp`` (for example ``/flyte-mcp/mcp``). SSE transport uses
  ``{mcp_mount_path}/sse`` instead.

**Tool selection**

Pass ``tool_groups`` *or* ``tools`` to restrict which MCP tools are
registered (not both). Omit both to enable all tools. Optional allowlists
limit which tasks, apps, or triggers remote calls may target. Search tools
require ``sdk_examples_path``, ``docs_examples_path``, and/or
``full_docs_path`` when those tools are enabled.

**Image**

When ``image`` is omitted (or set to ``"auto"``), the environment uses
:data:`DEFAULT_IMAGE`, which preinstalls the MCP/Starlette/Uvicorn stack
and clones the flyte-sdk + unionai-examples repos and the Union docs
``llms.txt`` into ``/root`` so the search tools have content to scan.


## Parameters

```python
class FlyteMCPAppEnvironment(
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
    mcp_mount_path: str,
    transport: Literal['stdio', 'sse', 'streamable-http'],
    uvicorn_config: uvicorn.Config | None,
    title: str | None,
    instructions: str | None,
    tool_groups: list[str] | None,
    tools: list[str] | None,
    task_allowlist: list[str] | None,
    app_allowlist: list[str] | None,
    trigger_allowlist: list[str] | None,
    sdk_examples_path: str | None,
    docs_examples_path: str | None,
    full_docs_path: str | None,
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
| `mcp_mount_path` | `str` | |
| `transport` | `Literal['stdio', 'sse', 'streamable-http']` | |
| `uvicorn_config` | `uvicorn.Config \| None` | |
| `title` | `str \| None` | |
| `instructions` | `str \| None` | |
| `tool_groups` | `list[str] \| None` | |
| `tools` | `list[str] \| None` | |
| `task_allowlist` | `list[str] \| None` | |
| `app_allowlist` | `list[str] \| None` | |
| `trigger_allowlist` | `list[str] \| None` | |
| `sdk_examples_path` | `str \| None` | |
| `docs_examples_path` | `str \| None` | |
| `full_docs_path` | `str \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `enabled_tools` | `set[str]` |  |
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

