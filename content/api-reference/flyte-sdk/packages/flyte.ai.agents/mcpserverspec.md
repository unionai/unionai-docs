---
title: MCPServerSpec
version: 2.5.12
variants: +flyte +union
layout: py_api
---

# MCPServerSpec

**Package:** `flyte.ai.agents`

Declarative spec for a remote MCP server that exposes tools.

The agent connects on startup, lists available tools, and registers each as
a callable tool whose ``execute`` proxies the MCP ``tools/call`` request.

Either ``url`` (for HTTP/SSE/streamable-http transports) or ``command``
(for stdio transports) must be set.

Parameters
----------
name:
    Stable display name for logs and event payloads.
url:
    HTTP(S) URL of the MCP endpoint (e.g. ``https://host/mcp/mcp``).
command:
    Command to launch a stdio MCP server (e.g.
    ``["uvx", "mcp-server-github"]``).
headers:
    Optional HTTP headers (for ``Authorization`` etc.).
env:
    Optional environment variables for stdio launches.
transport:
    Transport hint. ``"auto"`` (default) infers from ``url`` / ``command``.
tool_prefix:
    Optional prefix prepended to each tool name to avoid collisions.
tool_filter:
    Optional allowlist of tool names to expose. ``None`` means all.


## Parameters

```python
class MCPServerSpec(
    name: str,
    url: str | None,
    command: list[str] | None,
    headers: dict[str, str] | None,
    env: dict[str, str] | None,
    transport: Literal['auto', 'http', 'streamable-http', 'sse', 'stdio'],
    tool_prefix: str,
    tool_filter: list[str] | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `url` | `str \| None` | |
| `command` | `list[str] \| None` | |
| `headers` | `dict[str, str] \| None` | |
| `env` | `dict[str, str] \| None` | |
| `transport` | `Literal['auto', 'http', 'streamable-http', 'sse', 'stdio']` | |
| `tool_prefix` | `str` | |
| `tool_filter` | `list[str] \| None` | |

