---
title: User-defined MCP server
weight: 1
variants: +flyte +union
---

# User-defined MCP server

`MCPAppEnvironment` deploys any [FastMCP](https://modelcontextprotocol.io) instance as a long-running {{< key product_name >}} app, serving its tools over HTTP. Use it when you want to expose your *own* custom tools to AI assistants and LLM clients, rather than the built-in Flyte operations covered in [Flyte MCP server](./flyte_mcp_server).

## When to use it

Reach for `MCPAppEnvironment` when:

- You have domain-specific logic (database lookups, internal APIs, business rules, retrieval over your own corpus) that you want to package as MCP tools.
- You want an LLM client like Claude Code, Claude Desktop, or OpenCode to call those tools over a stable, authenticated HTTP endpoint.
- You want the tool server to run on {{< key product_name >}} infrastructure, with the same image, secrets, resources, and autoscaling story as any other app.

If instead you want assistants to *operate your {{< key product_name >}} cluster* (run tasks, inspect runs, build images, search docs), use [`FlyteMCPAppEnvironment`](./flyte_mcp_server) — it ships those tools for you. The two can also run side by side as separate apps.

## How it works

You build a `FastMCP` instance and register tools on it with the `@mcp.tool()` decorator. `MCPAppEnvironment` wraps that instance in a Starlette + Uvicorn server and deploys it as an app. Every tool you defined on the instance is exposed automatically — there is no extra registration step.

## Basic example

{{< code file="/unionai-examples/v2/user-guide/build-mcp/basic_mcp_app.py" fragment=basic-mcp lang=python >}}

Deploying with `flyte.serve(env)` activates the app and prints its public endpoint. See [Serve and deploy apps](../serve-and-deploy-apps/_index) for how deployment, activation, and scaling work in general.

## HTTP layout

The MCP ASGI app is mounted at `mcp_mount_path` (default `/mcp`). The resulting endpoints are:

```
GET  /health        # Liveness/readiness check -> {"status": "healthy"}
POST /mcp/mcp       # Streamable HTTP session endpoint (default transport)
GET  /mcp/sse       # SSE endpoint (only when transport="sse")
```

The session path is `{mcp_mount_path}/mcp` for `streamable-http` and `{mcp_mount_path}/sse` for `sse`. To get a cleaner URL such as `/mcp`, set `mcp_mount_path="/"`.

## Choosing a transport

| Transport | Session endpoint | When to use |
|-----------|------------------|-------------|
| `streamable-http` (default) | `{mcp_mount_path}/mcp` | The right choice for almost all remote deployments. Works with Claude Code, Claude Desktop, and OpenCode. |
| `sse` | `{mcp_mount_path}/sse` | Only when a client specifically requires a Server-Sent Events stream. Being phased out across the MCP ecosystem. |

```python
env = MCPAppEnvironment(
    name="my-mcp",
    mcp=mcp,
    transport="streamable-http",  # or "sse"
)
```

## Connecting a client

User-defined MCP servers are always deployed as remote HTTP apps — there is no local CLI equivalent. Once `flyte.serve(env)` prints your endpoint, register it with your client.

The session URL depends on your `mcp_mount_path` (default `/mcp`) and transport (default `streamable-http`), so the full endpoint is `https://<YOUR_HOST>/mcp/mcp`.

### Claude Code

```bash
claude mcp add --transport http \
  --header "Authorization: Bearer $TOKEN" \
  my-mcp https://<YOUR_HOST>/mcp/mcp
```

### OpenCode

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-mcp": {
      "type": "remote",
      "url": "https://<YOUR_HOST>/mcp/mcp",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer $TOKEN"
      }
    }
  }
}
```

Replace `<YOUR_HOST>` with the hostname from `handle.endpoint`. If you deployed with a custom `mcp_mount_path`, adjust the path accordingly.

## Configuration tips

- **Resources**: Tool servers are typically I/O-bound and lightweight. `flyte.Resources(cpu=1, memory="512Mi")` is a good starting point; raise it only if a tool does heavy in-process work.
- **Secrets**: If your tools call external APIs, pass credentials with `secrets=...` rather than baking them into the image. See [secret-based authentication](../build-apps/secret-based-authentication).
- **Custom dependencies**: Add the libraries your tools need to the app `image`. Remember to include `mcp`, `starlette`, and `uvicorn` (these come from `pip install 'flyte[mcp]'`).
- **Extra files**: If your tools import local helper modules, use the `include` parameter so they ship with the app. See [including additional files](../configure-apps/including-additional-files).

## Best practices

1. **Write clear docstrings**: The docstring on each `@mcp.tool()` function is what the LLM sees when deciding whether and how to call it. Treat it as the tool's API contract — describe the purpose, arguments, and return value.
2. **Use precise type hints**: FastMCP derives the tool's input schema from your function signature, so accurate types lead to better-formed tool calls.
3. **Keep tools focused**: Prefer several small, single-purpose tools over one tool with many modes. LLMs select narrowly-scoped tools more reliably.
4. **Require auth in production**: Keep `requires_auth=True` (the default) so only authenticated clients can reach your tools.
5. **Right-size resources**: Start small (1 CPU, 512Mi) and scale up only if profiling shows you need to.
