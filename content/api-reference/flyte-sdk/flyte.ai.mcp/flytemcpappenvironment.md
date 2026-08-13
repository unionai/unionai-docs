---
title: FlyteMCPAppEnvironment
version: 2.6.0
variants: +flyte +union
layout: py_api
---

# FlyteMCPAppEnvironment

**Package:** `flyte.ai.mcp`

Serve a Flyte-facing MCP server over HTTP (FastMCP + Starlette + Uvicorn).

Use this environment when you want LLM clients to call Flyte operations
(tasks, runs, actions, logs, apps, triggers, projects, secrets, conditions,
docs search) through the Model Context Protocol. Install extras with
`pip install 'flyte[mcp]'`.

**HTTP layout**

- `GET /health` — liveness/readiness JSON `{"status": "healthy"}`.
- The MCP ASGI app is mounted at `mcp_mount_path` (default `/flyte-mcp`). With
  the default `transport="streamable-http"`, the session endpoint is
  `{mcp_mount_path}/mcp` (for example `/flyte-mcp/mcp`). SSE transport uses
  `{mcp_mount_path}/sse` instead.

**Tool selection**

Pass `tool_groups` *or* `tools` to restrict which MCP tools are
registered (not both). Omit both to enable all tools. `read_only=True` then drops
everything that is not annotated `readOnlyHint=True`, so a public deployment gets a
safe surface without maintaining a hand-written tool list. Optional allowlists
limit which tasks, apps, or triggers remote calls may target. Search tools
require `sdk_examples_path`, `docs_examples_path`, and/or
`full_docs_path` when those tools are enabled.

**Project / domain resolution**

Project- and domain-scoped tools take optional `project`/`domain` arguments. They
resolve in this order: the explicit argument, then `FLYTE_MCP_PROJECT` /
`FLYTE_MCP_DOMAIN`, then whatever the initialized config carries. If nothing resolves,
the tool fails with a message telling the caller to pass them explicitly.

**Transport security**

Set `allowed_hosts` / `allowed_origins` (or `FLYTE_MCP_ALLOWED_HOSTS` /
`FLYTE_MCP_ALLOWED_ORIGINS`) to turn on MCP's DNS-rebinding protection. Any deployment
reachable over HTTP wants it. When neither is configured the protection stays off,
preserving the behavior existing deployments were built against.

**Image**

When `image` is omitted (or set to `"auto"`), the environment uses
`DEFAULT_IMAGE`, which preinstalls the MCP/Starlette/Uvicorn stack
and clones the flyte-sdk + unionai-examples repos and the Union docs
`llms.txt` into `/root` so the search tools have content to scan.


## Parameters

```python
class FlyteMCPAppEnvironment(
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
    type: str = 'FlyteMCPApp',
    mcp_mount_path: str = '/flyte-mcp',
    transport: MCPTransport = 'streamable-http',
    uvicorn_config: uvicorn.Config | None = None,
    title: str | None = None,
    instructions: str | None = None,
    tool_groups: list[str] | None = None,
    tools: list[str] | None = None,
    read_only: bool = False,
    task_allowlist: list[str] | None = None,
    app_allowlist: list[str] | None = None,
    trigger_allowlist: list[str] | None = None,
    allowed_hosts: list[str] | None = None,
    allowed_origins: list[str] | None = None,
    sdk_examples_path: str | None = '/root/flyte-sdk/examples',
    docs_examples_path: str | None = '/root/unionai-examples/v2',
    full_docs_path: str | None = '/root/llms.txt',
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
| `mcp_mount_path` | `str` | |
| `transport` | `MCPTransport` | |
| `uvicorn_config` | `uvicorn.Config \| None` | |
| `title` | `str \| None` | |
| `instructions` | `str \| None` | |
| `tool_groups` | `list[str] \| None` | |
| `tools` | `list[str] \| None` | |
| `read_only` | `bool` | |
| `task_allowlist` | `list[str] \| None` | |
| `app_allowlist` | `list[str] \| None` | |
| `trigger_allowlist` | `list[str] \| None` | |
| `allowed_hosts` | `list[str] \| None` | |
| `allowed_origins` | `list[str] \| None` | |
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
| [`resolve_scope()`](#resolve_scope) | Resolve the project/domain a tool call should run against. |
| [`resolved_allowed_hosts()`](#resolved_allowed_hosts) | `Host` header allowlist: the explicit field, else `FLYTE_MCP_ALLOWED_HOSTS`. |
| [`resolved_allowed_origins()`](#resolved_allowed_origins) | `Origin` header allowlist: the explicit field, else `FLYTE_MCP_ALLOWED_ORIGINS`. |
| [`run_stdio()`](#run_stdio) | Blocking wrapper around `MCPAppEnvironment.run_stdio_async`, for use as a process entry point. |
| [`run_stdio_async()`](#run_stdio_async) | Serve MCP over this process's stdin/stdout until the client disconnects. |
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

### resolve_scope()

```python
def resolve_scope(
    project: str | None,
    domain: str | None,
) -> tuple[str, str]
```
Resolve the project/domain a tool call should run against.

Order: the explicit argument, then the server-wide env default, then the initialized
config.



| Parameter | Type | Description |
|-|-|-|
| `project` | `str \| None` | |
| `domain` | `str \| None` | |

**Raises**

| Exception | Description |
|-|-|
| `ToolError` | when neither is resolvable. |

### resolved_allowed_hosts()

```python
def resolved_allowed_hosts()
```
`Host` header allowlist: the explicit field, else `FLYTE_MCP_ALLOWED_HOSTS`.


### resolved_allowed_origins()

```python
def resolved_allowed_origins()
```
`Origin` header allowlist: the explicit field, else `FLYTE_MCP_ALLOWED_ORIGINS`.


### run_stdio()

```python
def run_stdio()
```
Blocking wrapper around `MCPAppEnvironment.run_stdio_async`, for use as a process entry point.


### run_stdio_async()

```python
def run_stdio_async()
```
Serve MCP over this process's stdin/stdout until the client disconnects.

Validates the transport and then delegates to the wrapped `FastMCP`,
whose method of the same name does the actual serving.



**Raises**

| Exception | Description |
|-|-|
| `ValueError` | if `transport` is not `"stdio"`. |

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

