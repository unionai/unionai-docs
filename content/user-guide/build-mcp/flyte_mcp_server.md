---
title: Flyte MCP server
weight: 2
variants: +flyte +union
---

# Flyte MCP server

`FlyteMCPAppEnvironment` exposes {{< key product_name >}} operations as standardized [MCP](https://modelcontextprotocol.io) tools, so AI assistants and LLM clients can drive your cluster programmatically — running tasks, monitoring runs, managing apps and triggers, building images, running UV scripts, and searching the SDK and docs.

Unlike [`MCPAppEnvironment`](./mcp_server), where you supply your own tools, this environment ships a curated set of Flyte tools out of the box. You decide which of them to expose and what they're allowed to touch.

## When to use it

Use a Flyte MCP server when you want an assistant to *act on your cluster on your behalf*. Common scenarios:

- **Agentic development loops**: Let Claude Code or OpenCode run a task, wait for it, read its outputs, and iterate — without you copy-pasting commands.
- **Conversational operations**: Ask an assistant to list recent runs, check a run's status, or abort a stuck run.
- **Docs- and example-aware coding**: Enable the `search` tools so an assistant can ground its answers in the Flyte SDK examples and Union documentation.
- **Self-service automation**: Give a trusted internal agent a tightly-scoped server (a few allowlisted tasks, no destructive tools) to perform a narrow job.

If you only need to expose custom, non-Flyte tools, use [`MCPAppEnvironment`](./mcp_server) instead.

## How to run it

There are two ways to run a Flyte MCP server, suited to different stages:

| Mode | When to use |
|------|-------------|
| **Local (stdio)** | Local development and quick experiments. The client launches the server as a subprocess on your machine, using your local Flyte config. |
| **Remote (HTTP)** | Shared or production use. The server runs as a deployed app with a stable, authenticated URL that any client can connect to. |

### Running locally with `uvx`

The `flyte[mcp]` extra ships a `flyte-mcp` CLI entrypoint. Run it with [`uvx`](https://docs.astral.sh/uv/guides/tools/) — no global install required:

```bash
uvx --from "flyte[mcp]" flyte-mcp
```

`uvx` downloads `flyte[mcp]` into an isolated environment, runs `flyte-mcp`, and exits cleanly when you're done. The server reads your active Flyte config (the same one used by the `flyte` CLI or `flyte.init_from_config()`), so whichever project and cluster you're pointed at is what the tools operate on.

> [!TIP]
> Pin to a specific SDK version: `uvx --from "flyte[mcp]==2.4.0" flyte-mcp`

Once running, register it with your client as a **stdio** transport — the client manages the process lifetime. See the [connecting a client](#connecting-a-client) section below.

### Deploying remotely

Deploy a `FlyteMCPAppEnvironment` as a long-running app to get a stable, shared HTTP endpoint:

```python
flyte.init_from_config()
handle = flyte.serve(mcp_env)
handle.activate(wait=True)
print(f"MCP endpoint: {handle.endpoint}/flyte-mcp/mcp")
```

See [Serve and deploy apps](../serve-and-deploy-apps/_index) for how deployment, activation, and scaling work in general.

## Basic example

This deploys a remote server with **all** tools enabled:

{{< code file="/unionai-examples/v2/user-guide/build-mcp/flyte_mcp_app.py" fragment=flyte-mcp-all-tools lang=python >}}

The default mount path is `/flyte-mcp`, so with the default `streamable-http` transport the MCP endpoint is `/flyte-mcp/mcp`.

> [!TIP] Set `instructions`
> The `instructions` string is sent to the LLM as guidance on what the server is for and how to use its tools. A clear, specific instruction string measurably improves how reliably the assistant picks the right tool.

## Scoping the server

A server with every tool enabled and no restrictions is convenient for trusted local use, but for anything shared you should narrow it down. There are three layers of control, from coarse to fine.

### 1. Tool groups

Tools are organized into groups. Pass `tool_groups` to enable only the groups you need:

```python
mcp_env = FlyteMCPAppEnvironment(
    name="restricted-mcp",
    tool_groups=["task", "run", "script"],  # Only these groups
)
```

| Group | Tools | Typical use |
|-------|-------|-------------|
| `all` | All tools (default when both `tool_groups` and `tools` are omitted) | Trusted local development |
| `core` | No tools (only HTTP routes) | Health-check-only / building up explicitly |
| `task` | `run_task`, `get_task`, `list_tasks` | Launching and inspecting tasks |
| `run` | `get_run`, `get_run_io`, `abort_run`, `list_runs`, `wait_for_run` | Monitoring and controlling runs |
| `app` | `get_app`, `activate_app`, `deactivate_app` | Managing deployed apps |
| `trigger` | `activate_trigger`, `deactivate_trigger` | Managing triggers |
| `build` | `build_image` | Building container images remotely |
| `script` | `build_uv_script_image_remote`, `run_uv_script_remote`, `flyte_uv_script_format`, `flyte_uv_script_example` | Running standalone UV scripts |
| `search` | `search_flyte_sdk_examples`, `search_flyte_docs_examples`, `search_full_docs` | Grounding answers in SDK/docs |

### 2. Individual tools

For the tightest control, pass `tools` with an explicit list of tool names instead of `tool_groups` (pass one or the other, not both):

```python
mcp_env = FlyteMCPAppEnvironment(
    name="read-only-mcp",
    tools=["get_run", "list_runs", "get_run_io"],  # No run_task, no abort_run
)
```

This is the way to build, for example, a strictly read-only server.

### 3. Allowlists

Even with a tool enabled, you can restrict *which resources* it may target. Allowlists are the safest way to expose `run_task` or app/trigger management to an agent:

```python
mcp_env = FlyteMCPAppEnvironment(
    name="restricted-mcp",
    task_allowlist=[
        "production/my-project/allowed-task",  # domain/project/task
        "my-project/another-task",             # project/task (any domain)
        "any-domain-task",                     # task only (any project/domain)
    ],
    app_allowlist=["my-app", "another-app"],
    trigger_allowlist=["nightly-retrain"],
)
```

When an allowlist is set, calls targeting anything outside it are rejected. Omitting an allowlist leaves that resource type unrestricted.

## Enabling the search tools

The `search` tools need a corpus to scan, so you must point them at filesystem paths that exist *inside the app image*:

- `sdk_examples_path` — Flyte SDK examples (powers `search_flyte_sdk_examples`)
- `docs_examples_path` — Union examples (powers `search_flyte_docs_examples`)
- `full_docs_path` — the docs `llms.txt` index (powers `search_full_docs`)

The default image already clones the flyte-sdk and unionai-examples repos and downloads `llms.txt` into `/root` for you. If you supply a custom `image`, bake the corpora in yourself and pass matching paths:

```python
image = (
    flyte.Image.from_debian_base()
    .with_apt_packages("ca-certificates", "git", "curl")
    .with_pip_packages("mcp", "starlette", "uvicorn")
    .with_commands([
        "git clone --depth 1 https://github.com/flyteorg/flyte-sdk.git /root/flyte-sdk",
        "git clone --depth 1 https://github.com/unionai/unionai-examples.git /root/unionai-examples",
        # Also download llms.txt to /root/llms.txt for full-docs search
    ])
)

mcp_env = FlyteMCPAppEnvironment(
    name="search-mcp",
    image=image,
    tool_groups=["search"],
    sdk_examples_path="/root/flyte-sdk/examples",
    docs_examples_path="/root/unionai-examples/v2",
    full_docs_path="/root/llms.txt",
)
```

## Putting it together: a filtered server

This example combines tool groups, an allowlist, search paths, and instructions to build a scoped, production-ready server:

{{< code file="/unionai-examples/v2/user-guide/build-mcp/flyte_mcp_app_filtered.py" fragment=flyte-mcp-filtered lang=python >}}

## Connecting a client

### Claude Code — local (stdio)

Registers the `flyte-mcp` process as a locally managed stdio server. Claude Code starts and stops the `uvx` process automatically:

```bash
claude mcp add --transport stdio flyte-mcp -- uvx --from "flyte[mcp]" flyte-mcp
```

### Claude Code — remote (HTTP)

For a deployed server with a public URL:

```bash
claude mcp add --transport http \
  --header "Authorization: Bearer $TOKEN" \
  flyte-mcp-remote https://<YOUR_HOST>/flyte-mcp/mcp
```

### OpenCode — local

OpenCode spawns the `uvx` command for you:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "flyte-mcp": {
      "type": "local",
      "command": ["uvx", "--from", "flyte[mcp]", "flyte-mcp"],
      "enabled": true
    }
  }
}
```

### OpenCode — remote

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

1. **Start broad locally, scope down for sharing**: Run with `all` tools via `uvx` while exploring, then enable only the groups or tools you need before deploying a shared server.
2. **Always allowlist mutating tools**: If `run_task`, `abort_run`, or app/trigger management is enabled on a shared server, set the corresponding allowlist so an agent can't touch arbitrary resources.
3. **Prefer `tools` over `tool_groups` for read-only servers**: An explicit allowlist of read tools is the clearest way to guarantee an agent can't change anything.
4. **Write specific `instructions`**: Describe what the server does and any constraints (e.g. "only allowlisted tasks can be run"). This guides tool selection and reduces wasted calls.
5. **Keep auth on**: Leave `requires_auth=True` so only authenticated clients can reach a deployed server.

## MCP tools reference

| Tool | Group | Description |
|------|-------|-------------|
| `run_task` | `task` | Run a task with inputs; returns run URL and name |
| `get_task` | `task` | Get task metadata (type, required args, cache settings) |
| `list_tasks` | `task` | List tasks in a project/domain |
| `get_run` | `run` | Get run status by name |
| `wait_for_run` | `run` | Poll until a run completes |
| `get_run_io` | `run` | Get a run's inputs and outputs |
| `abort_run` | `run` | Abort a running run |
| `list_runs` | `run` | List runs for a task |
| `get_app` | `app` | Get app metadata |
| `activate_app` | `app` | Activate an app |
| `deactivate_app` | `app` | Deactivate an app |
| `activate_trigger` | `trigger` | Activate a trigger |
| `deactivate_trigger` | `trigger` | Deactivate a trigger |
| `build_image` | `build` | Build a container image remotely |
| `build_uv_script_image_remote` | `script` | Build a UV script image remotely |
| `run_uv_script_remote` | `script` | Run a UV script remotely |
| `flyte_uv_script_format` | `script` | Get the UV script template format |
| `flyte_uv_script_example` | `script` | Get a UV script example |
| `search_flyte_sdk_examples` | `search` | Search Flyte SDK examples |
| `search_flyte_docs_examples` | `search` | Search Union examples |
| `search_full_docs` | `search` | Search the full documentation |
