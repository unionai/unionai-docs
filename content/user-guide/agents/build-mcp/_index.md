---
title: Build an MCP
description: Serve Model Context Protocol servers for AI assistants to interact with, hosted on {{< key product_name >}}.
icon: code
weight: 2
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

- `GET /health`: Liveness/readiness check (`{"status": "healthy"}`)
- `POST {mcp_mount_path}/mcp` or `{mcp_mount_path}/sse`: MCP protocol endpoint (default: `/mcp` for generic, `/flyte-mcp` for Flyte)

## Quickstart

The fastest way to try Flyte MCP is locally (no deployment needed):

```bash
uvx --from "flyte[mcp]>=2.5.18" flyte-mcp --transport stdio
```

`--transport stdio` is required when a client launches the server as a subprocess. The CLI defaults to `streamable-http`, which starts an HTTP listener instead.

For client setup, tool selection, allowlists, and remote deployment, see [Flyte MCP server](./flyte_mcp_server).

{{< subpage-cards >}}
