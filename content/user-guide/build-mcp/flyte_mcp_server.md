---
title: Flyte MCP servers with FlyteMCPAppEnvironment
weight: 2
variants: +flyte +union
---

# Build a Flyte MCP server

`FlyteMCPAppEnvironment` exposes Flyte operations as standardized MCP tools. This allows AI assistants to interact with your Flyte cluster programmatically.

## Basic example

{{< code file="/unionai-examples/v2/user-guide/build-mcp/flyte_mcp_app.py" fragment=flyte-mcp-all-tools lang=python >}}

This deploys an MCP server with all tools enabled. The default mount path is `/flyte-mcp`, so the MCP endpoint is `/flyte-mcp/mcp`.

## Tool groups

Tools are organized into groups. Enable specific groups or individual tools:

```python
mcp_env = FlyteMCPAppEnvironment(
    name="restricted-mcp",
    tool_groups=["task", "run", "script"],  # Only these groups
)
```

Available tool groups:

| Group | Tools |
|-------|-------|
| `all` | All tools (default when omitted) |
| `core` | No tools (only HTTP routes) |
| `task` | `run_task`, `get_task`, `list_tasks` |
| `run` | `get_run`, `get_run_io`, `abort_run`, `list_runs`, `wait_for_run` |
| `app` | `get_app`, `activate_app`, `deactivate_app` |
| `trigger` | `activate_trigger`, `deactivate_trigger` |
| `build` | `build_image` |
| `script` | `build_uv_script_image_remote`, `run_uv_script_remote`, `flyte_uv_script_format`, `flyte_uv_script_example` |
| `search` | `search_flyte_sdk_examples`, `search_flyte_docs_examples`, `search_full_docs` |

## Allowlists

Restrict which resources can be accessed:

```python
mcp_env = FlyteMCPAppEnvironment(
    name="restricted-mcp",
    task_allowlist=[
        "production/my-project/allowed-task",
        "my-project/another-task",
        "any-domain-task",  # Matches any domain
    ],
    app_allowlist=["my-app", "another-app"],
)
```

## Search paths

Search tools require filesystem paths to search. Bake them into the image:

```python
image = (
    flyte.Image.from_debian_base()
    .with_apt_packages("git", "curl")
    .with_pip_packages("mcp", "starlette", "uvicorn")
    .with_commands([
        "git clone --depth 1 https://github.com/flyteorg/flyte-sdk.git /root/flyte-sdk",
        "git clone --depth 1 https://github.com/unionai/unionai-examples.git /root/unionai-examples",
        # Download the full documentation index for search
    ])
)

mcp_env = FlyteMCPAppEnvironment(
    name="search-mcp",
    image=image,
    sdk_examples_path="/root/flyte-sdk/examples",
    docs_examples_path="/root/unionai-examples/v2",
    full_docs_path="/root/llms.txt",
    tool_groups=["search"],
)
```

## Filtered example

{{< code file="/unionai-examples/v2/user-guide/build-mcp/flyte_mcp_app_filtered.py" fragment=flyte-mcp-filtered lang=python >}}

## MCP tools reference

| Tool | Description |
|------|-------------|
| `run_task` | Run a task with inputs, return run URL and name |
| `get_task` | Get task metadata (type, required args, cache settings) |
| `list_tasks` | List tasks in a project/domain |
| `get_run` | Get run status by name |
| `wait_for_run` | Poll until run completes |
| `get_run_io` | Get run inputs and outputs |
| `abort_run` | Abort a running run |
| `list_runs` | List runs for a task |
| `get_app` | Get app metadata |
| `activate_app` | Activate an app |
| `deactivate_app` | Deactivate an app |
| `activate_trigger` | Activate a trigger |
| `deactivate_trigger` | Deactivate a trigger |
| `build_image` | Build a container image remotely |
| `build_uv_script_image_remote` | Build UV script image remotely |
| `run_uv_script_remote` | Run UV script remotely |
| `flyte_uv_script_format` | Get UV script template format |
| `flyte_uv_script_example` | Get UV script example |
| `search_flyte_sdk_examples` | Search Flyte SDK examples |
| `search_flyte_docs_examples` | Search Union examples |
| `search_full_docs` | Search full documentation |
