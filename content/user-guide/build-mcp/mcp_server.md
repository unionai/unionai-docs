---
title: Generic MCP servers with MCPAppEnvironment
weight: 1
variants: +flyte +union
---

# Build a generic MCP server

Use `MCPAppEnvironment` to deploy any FastMCP instance. This is useful when you want to serve custom tools alongside or instead of Flyte operations.

## Basic example

{{< code file="/unionai-examples/v2/user-guide/build-mcp/basic_mcp_app.py" fragment=basic-mcp lang=python >}}

The MCP server exposes all tools defined on the `FastMCP` instance. The HTTP layout is:

```
GET  /health
POST /mcp/mcp      # Streamable HTTP endpoint (default)
GET  /mcp/sse      # SSE endpoint (if transport="sse")
```

## Transport modes

MCP supports different transport protocols:

| Transport | Endpoint | Use case |
|-----------|----------|----------|
| `streamable-http` (default) | `{mcp_mount_path}/mcp` | Most common, works with Claude Code, OpenCode |
| `sse` | `{mcp_mount_path}/sse` | Server-Sent Events stream |

```python
env = MCPAppEnvironment(
    name="my-mcp",
    mcp=mcp,
    transport="streamable-http",  # or "sse"
)
```

## Best practices

1. **Document your tools**: Use docstrings in FastMCP for clear tool descriptions
2. **Set appropriate resources**: MCP servers don't need much CPU/memory (1 CPU, 512Mi is usually sufficient)
3. **Choose the right transport**: `streamable-http` works best with most agent harnesses
