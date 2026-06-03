---
title: Build an MCP
weight: 19
variants: +flyte +union
---

# Build an MCP

{{< key product_name >}} supports serving [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers over HTTP.

There are two main MCP environment types:

| Environment | Purpose |
|-------------|---------|
| **`MCPAppEnvironment`** | Serve any FastMCP instance with custom tools |
| **`FlyteMCPAppEnvironment`** | Flyte-specific server that exposes Flyte operations as tools |

See the sub-pages for detailed guides:
- [User-defined MCP servers](./mcp_server): Build and deploy your own FastMCP instances
- [Flyte MCP servers](./flyte_mcp_server): Use Flyte-specific tools to interact with your cluster

## HTTP layout

All MCP app environments expose the same HTTP endpoints:

- `GET /health` — Liveness/readiness check (`{"status": "healthy"}`)
- `POST {mcp_mount_path}/mcp` or `{mcp_mount_path}/sse` — MCP protocol endpoint (default: `/mcp` for generic, `/flyte-mcp` for Flyte)

## Quickstart

The fastest way to try Flyte MCP is locally — no deployment needed:

```bash
uvx --from "flyte[mcp]" flyte-mcp
```

For client setup, tool selection, allowlists, and remote deployment, see [Flyte MCP server](./flyte_mcp_server).
