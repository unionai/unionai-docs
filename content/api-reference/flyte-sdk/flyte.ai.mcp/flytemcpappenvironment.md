---
title: FlyteMCPAppEnvironment
description: "Serve a Flyte-facing MCP server over HTTP (FastMCP + Starlette + Uvicorn)."
icon: braces
version: 2.14.1
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

**Secrets**

By default `create_secret` and `update_secret` take no value. Anything a tool takes as an
argument is written by the model, so a value passed that way sits in the conversation, the
client's logs and the model provider's context. Instead the tool returns a one-time URL
(`/secret-input/{token}` on this server, valid for 10 minutes) that the human opens in a
browser to type the value into a password field; the value goes from the browser to Flyte
and never passes through the model. Clients that support MCP URL elicitation are sent the
URL as an elicitation request; others get it in the tool result. (`streamable-http` runs
stateless here, so the server never sees the capabilities a client announced at
initialize and always answers in the tool result; elicitation applies to `sse`.) Over stdio there is no
HTTP surface, so the tools point at `flyte create secret`, which prompts with hidden input.

The tokens live in this process's memory: run a single replica, or the URL may be opened on
a replica that did not mint it. Set `allow_inline_secret_values=True` to restore the old
behavior where both tools take a `value` argument (for automation where no human is in the
loop and the model is already trusted with the value).

`generate_secret` covers the other way a secret gets in without passing through the chat:
the server generates an SSH key pair (`ssh-ed25519`, or 4096-bit `ssh-rsa` for hosts that
need it), stores the private half as a secret and returns only the public key and its
fingerprint, for the human to install, for example as a GitHub deploy key. It needs no form,
so it works over stdio too, and it never overwrites an existing secret.

To check a value before it is saved (a bad token otherwise goes unnoticed until a task
fails), register validators with `secret_validators`. Only the owner knows what a value is
for and which hosts this server may call, so there are no built-in ones. A validator returns
an error sentence, or `None` when the value is valid; the model then passes its name as
`validator` to `create_secret`/`update_secret`. The form rejects an invalid value with that
sentence and keeps the link usable so the human can retype it; with
`allow_inline_secret_values` the tool call fails with the sentence instead. A validator that
raises or runs longer than 15 seconds counts as a rejection. The sentence is shown to the
human (and, inline, to the model), so it must not quote the value.

```python
async def token_ok(token: str) -> str | None:
    async with httpx.AsyncClient() as client:
        r = await client.get(WHOAMI_URL, headers={"Authorization": f"Bearer {token}"})
    return None if r.is_success else f"The provider rejected the token (HTTP {r.status_code})."

env = FlyteMCPAppEnvironment(name="flyte-mcp", secret_validators={"example-token": token_ok})
```

**Transport security**

Set `allowed_hosts` / `allowed_origins` (or `FLYTE_MCP_ALLOWED_HOSTS` /
`FLYTE_MCP_ALLOWED_ORIGINS`) to turn on MCP's DNS-rebinding protection. Any deployment
reachable over HTTP wants it. When neither is configured the protection stays off,
preserving the behavior existing deployments were built against.

**Log reads**

`get_logs` reads for at most the caller's `timeout_s` (default 30), clamped to
`[1, log_read_timeout_ceiling_s]` (default 120). Once lines are flowing, a gap of
`log_idle_timeout_s` (default 5) ends the read. Both are server settings; callers cannot
raise them.

**OAuth discovery for MCP clients**

Set `protected_resource_metadata` to let MCP clients that implement the MCP authorization
spec discover how to sign in, per RFC 9728, instead of needing a token pasted into their
configuration. The server then:

- serves the metadata document, without authentication, at
  `/.well-known/oauth-protected-resource{endpoint path}` (for example
  `/.well-known/oauth-protected-resource/flyte-mcp/mcp`) and at the root
  `/.well-known/oauth-protected-resource`, which clients fall back to;
- answers any other request without an `Authorization: Bearer` header with `401` and
  `WWW-Authenticate: Bearer resource_metadata="<metadata URL>"`;
- forwards the bearer token of every other request to Flyte, as with `requires_auth=True`.

Clients can only reach the metadata if the platform ingress lets unauthenticated requests
through, so pair it with `requires_auth=False`. The server still refuses the MCP endpoint
without a bearer token, but it does not validate the token itself: the Flyte endpoint
validates it on every remote call, so a tool that makes none (the `search` group) answers
any bearer value.

```python
env = FlyteMCPAppEnvironment(
    name="flyte-mcp",
    requires_auth=False,
    protected_resource_metadata=ProtectedResourceMetadata(),
)
```

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
    cluster: str | None = None,
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
    allow_inline_secret_values: bool = False,
    secret_validators: dict[str, SecretValidator] | None = None,
    task_allowlist: list[str] | None = None,
    app_allowlist: list[str] | None = None,
    trigger_allowlist: list[str] | None = None,
    allowed_hosts: list[str] | None = None,
    allowed_origins: list[str] | None = None,
    protected_resource_metadata: ProtectedResourceMetadata | None = None,
    sdk_examples_path: str | None = '/root/flyte-sdk/examples',
    docs_examples_path: str | None = '/root/unionai-examples/v2',
    full_docs_path: str | None = '/root/llms.txt',
    log_read_timeout_ceiling_s: float = 120.0,
    log_idle_timeout_s: float = 5.0,
    config_file: str | None = None,
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
| `cluster` | `str \| None` | |
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
| `allow_inline_secret_values` | `bool` | |
| `secret_validators` | `dict[str, SecretValidator] \| None` | |
| `task_allowlist` | `list[str] \| None` | |
| `app_allowlist` | `list[str] \| None` | |
| `trigger_allowlist` | `list[str] \| None` | |
| `allowed_hosts` | `list[str] \| None` | |
| `allowed_origins` | `list[str] \| None` | |
| `protected_resource_metadata` | `ProtectedResourceMetadata \| None` | |
| `sdk_examples_path` | `str \| None` | |
| `docs_examples_path` | `str \| None` | |
| `full_docs_path` | `str \| None` | |
| `log_read_timeout_ceiling_s` | `float` | |
| `log_idle_timeout_s` | `float` | |
| `config_file` | `str \| None` | |

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

