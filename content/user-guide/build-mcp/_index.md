---
title: Build an MCP server
weight: 2
variants: +flyte +union
---

# Build an MCP server

{{< key product_name >}} supports serving [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers over HTTP.

There are two main MCP environment types:

| Environment | Purpose |
|-------------|---------|
| **`MCPAppEnvironment`** | Serve any FastMCP instance with custom tools |
| **`FlyteMCPAppEnvironment`** | Flyte-specific server that exposes Flyte operations as tools |

See the sub-pages for detailed guides:
- [Generic MCP servers](./mcp_server): Build and deploy your own FastMCP instances
- [Flyte MCP servers](./flyte_mcp_server): Use Flyte-specific tools to interact with your cluster

## HTTP layout

All MCP app environments expose the same HTTP endpoints:

- `GET /health` — Liveness/readiness check (`{"status": "healthy"}`)
- `POST {mcp_mount_path}/mcp` or `{mcp_mount_path}/sse` — MCP protocol endpoint (default: `/mcp` for generic, `/flyte-mcp` for Flyte)

## Connection examples

### Claude Code (stdio)

For local usage where `localhost` isn't accessible:

```bash
claude mcp add --transport stdio flyte-mcp -- uvx --with "flyte[mcp]" flyte-mcp
```

### Claude Code (HTTP)

For remote deployments with a public URL:

```bash
claude mcp add --transport http \
  --header "Authorization: Bearer $TOKEN" \
  flyte-mcp-remote https://<YOUR_HOST>/flyte-mcp/mcp
```

### OpenCode

Local MCP process:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "flyte-mcp": {
      "type": "local",
      "command": ["uvx", "--with", "flyte[mcp]", "flyte-mcp"],
      "enabled": true
    }
  }
}
```

Remote HTTP endpoint:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "flyte-mcp-remote": {
      "type": "remote",
      "url": "https://<YOUR_HOST>/flyte-mcp/mcp",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer $TOKEN"
      }
    }
  }
}
```

## Best practices

1. **Use allowlists in production**: Restrict which resources can be accessed
2. **Set appropriate resources**: MCP servers don't need much CPU/memory (1 CPU, 512Mi is usually sufficient)
3. **Choose the right transport**: `streamable-http` works best with most agent harnesses
4. **Document your tools**: Use docstrings in FastMCP for clear tool descriptions
5. **Use instructions**: Set `instructions` on `FlyteMCPAppEnvironment` to guide LLM usage
