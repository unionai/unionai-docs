---
title: flyte.ai.mcp
icon: box-seam
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# flyte.ai.mcp

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteMCPAppEnvironment`](../flyte.ai.mcp/flytemcpappenvironment) | Serve a Flyte-facing MCP server over HTTP (FastMCP + Starlette + Uvicorn). |
| [`MCPAppEnvironment`](../flyte.ai.mcp/mcpappenvironment) | Serve a FastMCP server over HTTP (Starlette + Uvicorn) or over stdio. |

### Methods

| Method | Description |
|-|-|
| [`resolve_tools()`](#resolve_tools) | Return the set of MCP tool names to expose. |


### Variables

| Property | Type | Description |
|-|-|-|
| `ALL_MCP_TOOLS` | `tuple` |  |
| `ALL_MCP_TOOL_GROUPS` | `tuple` |  |
| `READ_ONLY_MCP_TOOLS` | `tuple` |  |
| `TOOL_GROUP_MAPPING` | `dict` |  |

## Methods

#### resolve_tools()

```python
def resolve_tools(
    tool_groups: list[str] | None,
    tools: list[str] | None,
    read_only: bool = False,
) -> set[str]
```
Return the set of MCP tool names to expose.

If both `tool_groups` and `tools` are omitted, all tools are enabled. Otherwise pass
either one (not both). The `core` group selects no tools; only the HTTP routes are served.



| Parameter | Type | Description |
|-|-|-|
| `tool_groups` | `list[str] \| None` | Group names from `TOOL_GROUP_MAPPING` |
| `tools` | `list[str] \| None` | Explicit tool names from `ALL_MCP_TOOLS` |
| `read_only` | `bool` | Drop every tool that is not annotated `readOnlyHint=True` |

**Returns:** The enabled tool names

