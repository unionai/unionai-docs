---
title: MCPServerSpec
version: 2.6.3
variants: +flyte +union
layout: py_api
---

# MCPServerSpec

**Package:** `flyte.ai.agents`

Declarative spec for a remote MCP server that exposes tools.

The agent connects on startup, lists available tools, and registers each as
a callable tool whose `execute` proxies the MCP `tools/call` request.

Either `url` (for HTTP/SSE/streamable-http transports) or `command`
(for stdio transports) must be set.



## Parameters

```python
class MCPServerSpec(
    name: str,
    url: str | None = None,
    command: list[str] | None = None,
    headers: dict[str, str] | None = None,
    env: dict[str, str] | None = None,
    transport: Literal['auto', 'http', 'streamable-http', 'sse', 'stdio'] = 'auto',
    tool_prefix: str = '',
    tool_filter: list[str] | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Stable display name for logs and event payloads. |
| `url` | `str \| None` | HTTP(S) URL of the MCP endpoint (e.g. `https://host/mcp/mcp`). |
| `command` | `list[str] \| None` | Command to launch a stdio MCP server (e.g. `["uvx", "mcp-server-github"]`). |
| `headers` | `dict[str, str] \| None` | Optional HTTP headers (for `Authorization` etc.). |
| `env` | `dict[str, str] \| None` | Optional environment variables for stdio launches. |
| `transport` | `Literal['auto', 'http', 'streamable-http', 'sse', 'stdio']` | Transport hint. `"auto"` (default) infers from `url` / `command`. |
| `tool_prefix` | `str` | Optional prefix prepended to each tool name to avoid collisions. |
| `tool_filter` | `list[str] \| None` | Optional allowlist of tool names to expose. `None` means all. |

