---
title: Flyte MCP server
description: Expose Flyte operations as MCP tools so an AI assistant can drive your workloads.
icon: plug
weight: 2
variants: +flyte +union
---

# Flyte MCP server

`FlyteMCPAppEnvironment` exposes {{< key product_name >}} operations as standardized [MCP](https://modelcontextprotocol.io) tools, so AI assistants and LLM clients can drive your cluster programmatically: running tasks, monitoring runs, reading logs, inspecting actions, managing apps and triggers, and searching the SDK and docs.

Unlike [`MCPAppEnvironment`](./mcp_server), where you supply your own tools, this environment ships a curated set of Flyte tools out of the box. You decide which of them to expose and what they're allowed to touch.

> [!TIP] There is a prebuilt plugin
> [`flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins) ships these same
> control-plane tools as a `flyte-cluster` MCP server, plus a hosted `flyte-docs` search
> server. See [Flyte agent plugins](../../../api-reference/agent-plugins) for
> harness-specific installation and configuration.
>
> Build your own `FlyteMCPAppEnvironment` below when you need to scope the tools,
> allowlist resources, or deploy a shared server.

## When to use it

Use a Flyte MCP server when you want an assistant to *act on your cluster on your behalf*. Common scenarios:

- **Agentic development loops**: Let Claude Code or OpenCode run a task, wait for it, read its outputs, and iterate, without you copy-pasting commands.
- **Conversational operations**: Ask an assistant to list recent runs, check a run's status, or abort a stuck run.
- **Docs- and example-aware coding**: Enable the `search` tools so an assistant can ground its answers in the Flyte SDK examples and Union documentation.
- **Self-service automation**: Give a trusted internal agent a tightly-scoped server (a few allowlisted tasks, no destructive tools) to perform a narrow job.

If you only need to expose custom, non-Flyte tools, use [`MCPAppEnvironment`](./mcp_server) instead.

## How to run it

There are two ways to run a Flyte MCP server, suited to different stages:

| Mode | When to use |
|------|-------------|
| **Local (stdio)** | One user on one machine. The client launches the server as a subprocess, using your local Flyte config and your existing login. Nothing is deployed, and no data leaves your machine. |
| **Remote (HTTP)** | A whole team, or a client that cannot launch a subprocess (a browser-based assistant, for example). The server runs as a deployed app with a stable, authenticated URL. |

Prefer stdio unless you need one of the two things only HTTP gives you: a single shared server that nobody has to install, or a URL for a client that has no local process.

{{< variant flyte >}}
{{< markdown >}}
> [!NOTE] Remote deployment is not available here
> Deploying the server as a long-running app requires Union.ai apps, which open-source Flyte does not provide. Use the local stdio mode below. Everything else on this page — tool groups, individual tools, and allowlists — applies to both modes.
{{< /markdown >}}
{{< /variant >}}

### Running locally with `uvx`

The `flyte[mcp]` extra ships a `flyte-mcp` CLI entrypoint. Run it with [`uvx`](https://docs.astral.sh/uv/guides/tools/) (no global install required):

```bash
uvx --from "flyte[mcp]>=2.5.18" flyte-mcp --transport stdio
```

`uvx` downloads `flyte[mcp]` into an isolated environment, runs `flyte-mcp`, and exits cleanly when you're done. The server finds its Flyte config with the same search order as the `flyte` CLI, so whichever project and cluster that config points at is what the tools operate on.

Two parts of that command matter:

- **`--transport stdio` is required.** The CLI defaults to `streamable-http`, which starts an HTTP listener instead of speaking JSON-RPC on stdin and stdout. A client that launches the process expecting stdio will not connect without this flag.
- **`>=2.5.18` is the minimum version.** It is the first release that constrains its `mcp` dependency below 2.0. Earlier versions resolve `mcp` 2.0.0, which removed the module the server imports, and the server exits at startup reporting `mcp is not installed`.

> [!TIP]
> Pin to an exact version instead of a floor: `uvx --from "flyte[mcp]==2.5.18" flyte-mcp --transport stdio`

The server starts even when the search order finds no Flyte config. In that case the tools fail when the assistant calls them, rather than the server failing to start. From `flyte` 2.12.2, a `--config` or `FLYTE_MCP_CONFIG` path that doesn't exist does stop the server at startup.

#### Pin the server to a tenant

Requires `flyte` 2.12.2 or later.

The config search prefers `./config.yaml`, `./.flyte/config.yaml`, and the git root's `.flyte/config.yaml` over `FLYTECTL_CONFIG`. An MCP client often launches the server from your project directory, so a config checked into that repo wins, and the tools act on that repo's tenant.

To choose the tenant explicitly, pass `--config`, and optionally `--endpoint` to override the config file's endpoint:

```bash
uvx --from "flyte[mcp]>=2.12.2" flyte-mcp --transport stdio --config ~/.flyte/config.yaml
```

| Option | Environment variable | Effect |
|--------|----------------------|--------|
| `--config` | `FLYTE_MCP_CONFIG` | Flyte config file to initialize from, instead of the search order. |
| `--endpoint` | `FLYTE_MCP_ENDPOINT` | Endpoint to connect to. Overrides the endpoint in the config file. |

Combining either option with `--no-init-from-config` is a usage error.

At startup the server prints the config file and endpoint it resolved, and where each came from, to stderr:

```text
flyte-mcp: config /home/me/.flyte/config.yaml (from --config), endpoint dns:///my-tenant.example.com (from config file)
```

If the search order found the config in the working directory or its git repo, the server also prints a warning naming that file. The `whoami` tool reports the config file as `config_file`, so the assistant can check which tenant it is acting on.

> [!NOTE] Skip the search corpus
> The three `search_*` tools grep a local copy of the Flyte SDK examples, the docs examples, and `llms.txt`. Enabling them makes the CLI clone roughly 120 MB into `~/.flyte/mcp` on first launch. Pass `--tool-groups` without `search` to skip it:
> ```bash
> uvx --from "flyte[mcp]>=2.5.18" flyte-mcp --transport stdio \
>   --tool-groups task,run,action,logs,app,trigger,project,secret,condition,identity
> ```

Once running, register it with your client as a **stdio** transport: the client manages the process lifetime. See the [connecting a client](#connecting-a-client) section below.

{{< variant union >}}
{{< markdown >}}
### Deploying remotely

Deploy a `FlyteMCPAppEnvironment` as a long-running app to get a stable, shared HTTP endpoint:

```python
flyte.init_from_config()
handle = flyte.serve(mcp_env)
handle.activate(wait=True)
print(f"MCP endpoint: {handle.endpoint}/flyte-mcp/mcp")
```

The app is deployed into **your own tenant**, so the server sits in the same trust domain as the data it reads: run metadata, logs, and task inputs and outputs stay inside your account. Set `requires_auth=True` and the endpoint sits behind your organization's SSO, so each call runs as the person driving the agent, with their own permissions.

See [Serve and deploy apps](../../apps/serve-and-deploy-apps/_index) for how deployment, activation, and scaling work in general.

### Let clients sign in through OAuth discovery

Requires `flyte` 2.13.4 or later.

Some MCP clients, such as claude.ai connectors, can't take a pasted bearer token. They sign in by OAuth discovery instead, as the [MCP authorization spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) describes. To support them, set `protected_resource_metadata` and turn off the platform's authentication with `requires_auth=False`:

```python
from flyte.ai.mcp import FlyteMCPAppEnvironment, ProtectedResourceMetadata

mcp_env = FlyteMCPAppEnvironment(
    name="flyte-mcp",
    requires_auth=False,
    protected_resource_metadata=ProtectedResourceMetadata(),
)
```

`requires_auth=False` is required because clients must reach the metadata without a token. The server still requires a bearer token on everything else. It then:

- Serves an [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728) metadata document, without authentication, at `/.well-known/oauth-protected-resource/flyte-mcp/mcp` (with the default mount path) and at the root `/.well-known/oauth-protected-resource`. The document names the MCP endpoint URL and the authorization server that issues its tokens.
- Answers any request without an `Authorization: Bearer` header with `401` and `WWW-Authenticate: Bearer resource_metadata="<metadata URL>"`. `/health` stays open.
- Forwards each request's bearer token to {{< key product_name >}}, so tool calls run as the signed-in user, as with `requires_auth=True`.

`ProtectedResourceMetadata` takes these options:

| Option | Default | Effect |
|--------|---------|--------|
| `authorization_servers` | The issuer your {{< key product_name >}} endpoint advertises | Issuer URLs the metadata advertises as issuing tokens for the server. Each must use HTTPS without a query or fragment. An empty list is rejected. |
| `resource` | The request's scheme and `Host`, plus the MCP endpoint path | The full URL clients use to reach the MCP endpoint. Clients reject metadata whose `resource` doesn't match the URL they connected to. |
| `scopes_supported` | None | OAuth scopes a client should request. Also sent as the `scope` parameter of the `401` challenge. |
| `resource_name` | None | Human-readable server name. Some clients show it on their consent screen. |
| `resource_documentation` | None | URL of documentation for developers using the server. |

Gotchas:

- **The transport must be HTTP.** Setting `protected_resource_metadata` with `transport="stdio"` raises `ValueError`.
- **Set `resource` if a proxy changes the public URL.** If the proxy in front of the app rewrites the host or path, or terminates TLS so the app sees `http`, the derived URL won't match what clients connected to. The server never reads `Forwarded` or `X-Forwarded-Host` headers to build it.
- **If the metadata returns `503`, set `authorization_servers`.** The default looks up the issuer from your {{< key product_name >}} endpoint the first time the metadata is requested. If that lookup fails, the metadata endpoint returns `503`, and the server logs the reason.
- **Your identity provider must allow the client to sign in.** It must support the authorization-code flow with PKCE S256. It must also let the MCP client register: dynamic client registration, an administrator-approved client ID metadata document, or a preregistered client the MCP client supports. If you set `authorization_servers` to a provider you administer, register the client's exact redirect URI there, assign its users, and allow the requested scopes.
- **The server doesn't validate tokens itself.** {{< key product_name >}} validates the token on each call the server makes to it. The `search` tools make no such call, so they answer any bearer value.
- **Audience binding isn't enforced.** Clients send the server's URL as the RFC 8707 `resource` parameter, but the server doesn't check that the token's audience matches it. The token works as long as its audience is one {{< key product_name >}} accepts.
{{< /markdown >}}
{{< /variant >}}

## Basic example

A server with **all** tools enabled. The environment definition is the same for both modes — only the last step differs, since `flyte.serve` deploys it as an app:

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
    tool_groups=["task", "run", "logs"],  # Only these groups
)
```

| Group | Tools | Typical use |
|-------|-------|-------------|
| `all` | All tools (default when both `tool_groups` and `tools` are omitted) | Trusted local development |
| `core` | No tools (only HTTP routes) | Health-check-only / building up explicitly |
| `task` | `run_task`, `get_task`, `list_tasks` | Launching and inspecting tasks |
| `run` | `get_run`, `get_run_io`, `abort_run`, `list_runs`, `wait_for_run`, `rerun_run` | Monitoring and controlling runs |
| `action` | `list_actions`, `get_action`, `abort_action` | Debugging a run step by step: phases, attempts, failure details, timing |
| `logs` | `get_logs` | Reading task logs |
| `app` | `get_app`, `list_apps`, `activate_app`, `deactivate_app` | Managing deployed apps |
| `trigger` | `list_triggers`, `get_trigger`, `activate_trigger`, `deactivate_trigger` | Managing triggers |
| `project` | `list_projects`, `get_project` | Discovering projects and domains |
| `secret` | `list_secrets`, `create_secret`, `delete_secret` | Managing secrets (names only — values are never returned) |
| `condition` | `list_conditions`, `get_condition`, `signal_condition` | Answering human-in-the-loop gates (`get_condition` requires `flyte` 2.13.5 or later) |
| `identity` | `whoami` | Confirming which identity and org the server is acting as, and (for a server started with `flyte-mcp` 2.12.2 or later) which config file it was started from |
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

- `sdk_examples_path`: Flyte SDK examples (powers `search_flyte_sdk_examples`)
- `docs_examples_path`: Union examples (powers `search_flyte_docs_examples`)
- `full_docs_path`: the docs `llms.txt` index (powers `search_full_docs`)

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

## Reading logs

Requires `flyte` 2.13.5 or later. Earlier releases return the first lines of the log as a plain string; from 2.13.5, `get_logs` returns a dict, so update any client code that parses its result.

`get_logs` returns the last `max_lines` lines of an action's log (default 200), oldest first. The response is capped at 2,000 lines and about 100,000 characters, with the oldest lines dropped first. The response includes:

| Field | Meaning |
|-------|---------|
| `logs` | The log lines, joined by newlines |
| `available` | `false` when the action's logs are not up yet. `get_logs` returns right away in that case, unless the call passes `wait_for_logs=true`. |
| `message` | A summary of what was returned, and what to call next |
| `first_line`, `end_line` | The range of lines returned. Lines are numbered from 0 at the start of the log. |
| `has_more_before`, `next_before_line` | Whether older lines exist, and the `before_line` value that reads them |
| `attempt` | The attempt that was read. Pass it back when paging so the numbering stays on the same attempt if a retry starts. |
| `stopped` | Why reading ended: `end_of_stream`, `idle`, `time_limit`, or `before_line` |
| `timeout_s` | The read budget the call used, in seconds |

To page back, call `get_logs` again with `before_line` set to `next_before_line`, and the same `attempt` and `filter_system` as the first call, so the line numbers don't shift. To read from the start of the log, pass `before_line` equal to `max_lines`.

The log service streams from the start of the log, so finding the newest lines means reading the whole stream. A call reads for at most its `timeout_s` (default 30), clamped to between 1 second and the server's ceiling. Once lines are arriving, a gap with no new lines also ends the read. If `stopped` is `time_limit`, newer lines may exist: retry with a larger `timeout_s`.

Two `FlyteMCPAppEnvironment` settings bound the read. Callers can't raise them.

| Setting | Default | Effect |
|---------|---------|--------|
| `log_read_timeout_ceiling_s` | `120` | Upper limit on a call's `timeout_s`. Must be at least 1. |
| `log_idle_timeout_s` | `5` | Seconds without a new line that end the read, once lines are arriving. Must be greater than 0. |

## Putting it together: a filtered server

This example combines an explicit tool list, an allowlist, search paths, and instructions to build a scoped server. It lists its tools instead of using `tool_groups=["task", "run", "search"]` so that it can leave out `abort_run`: the `run` group includes it, and no allowlist covers it, so it would let an agent abort any run its identity has access to, in any project and domain it names. The `task_allowlist` then restricts every task tool and `rerun_run`:

{{< code file="/unionai-examples/v2/user-guide/build-mcp/flyte_mcp_app_filtered.py" fragment=flyte-mcp-filtered lang=python >}}

## Connecting a client

### Claude Code: local (stdio)

Registers the `flyte-mcp` process as a locally managed stdio server. Claude Code starts and stops the `uvx` process automatically:

```bash
claude mcp add --transport stdio flyte-mcp -- \
  uvx --from "flyte[mcp]>=2.5.18" flyte-mcp --transport stdio
```

`--transport stdio` appears twice on purpose. The first tells Claude Code how to talk to the server; the second tells the server which transport to serve. Without the second, the server starts an HTTP listener and the connection fails.

{{< variant union >}}
{{< markdown >}}
### Claude Code: remote (HTTP)

For a deployed server with a public URL:

```bash
claude mcp add --transport http \
  --header "Authorization: Bearer $TOKEN" \
  flyte-mcp-remote https://<YOUR_HOST>/flyte-mcp/mcp
```
{{< /markdown >}}
{{< /variant >}}

### OpenCode: local

OpenCode spawns the `uvx` command for you:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "flyte-mcp": {
      "type": "local",
      "command": ["uvx", "--from", "flyte[mcp]>=2.5.18", "flyte-mcp", "--transport", "stdio"],
      "enabled": true
    }
  }
}
```

{{< variant union >}}
{{< markdown >}}
### OpenCode: remote

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
{{< /markdown >}}
{{< /variant >}}

## Best practices

1. **Start broad locally, scope down for sharing**: Run with `all` tools via `uvx` while exploring, then enable only the groups or tools you need before deploying a shared server.
2. **Always allowlist mutating tools**: If `run_task` or app/trigger management is enabled on a shared server, set the corresponding allowlist so an agent can't touch arbitrary resources. No allowlist applies to `abort_run`, `abort_action`, `create_secret`, `delete_secret`, or `signal_condition`, and each belongs to a group (`run`, `action`, `secret`, `condition`). To keep one from the server's agent, pass an explicit `tools=[...]` list that leaves it out, instead of `tool_groups`.
3. **Prefer `tools` over `tool_groups` for read-only servers**: An explicit allowlist of read tools is the clearest way to guarantee an agent can't change anything.
4. **Write specific `instructions`**: Describe what the server does and any constraints (e.g. "only allowlisted tasks can be run"). This guides tool selection and reduces wasted calls.
5. **Keep auth on**: Leave `requires_auth=True` so only authenticated clients can reach a deployed server. The exception is a server with `protected_resource_metadata` set, which needs `requires_auth=False` and requires a bearer token itself.

## MCP tools reference

| Tool | Group | Description |
|------|-------|-------------|
| `run_task` | `task` | Run a task |
| `get_task` | `task` | Get task details |
| `list_tasks` | `task` | List tasks |
| `get_run` | `run` | Get a run |
| `get_run_io` | `run` | Get run inputs and outputs |
| `abort_run` | `run` | Abort a run |
| `list_runs` | `run` | List runs |
| `wait_for_run` | `run` | Wait for a run to finish |
| `rerun_run` | `run` | Re-run a prior run |
| `list_actions` | `action` | List the actions of a run |
| `get_action` | `action` | Get action details and timing |
| `abort_action` | `action` | Abort a single action |
| `get_logs` | `logs` | Read the newest lines of an action's logs, with a cursor to page back (see [Reading logs](#reading-logs)) |
| `get_app` | `app` | Get an app |
| `list_apps` | `app` | List apps |
| `activate_app` | `app` | Activate an app |
| `deactivate_app` | `app` | Deactivate an app |
| `list_triggers` | `trigger` | List triggers |
| `get_trigger` | `trigger` | Get a trigger |
| `activate_trigger` | `trigger` | Activate a trigger |
| `deactivate_trigger` | `trigger` | Deactivate a trigger |
| `list_projects` | `project` | List projects |
| `get_project` | `project` | Get a project |
| `list_secrets` | `secret` | List secret names |
| `create_secret` | `secret` | Create a secret |
| `delete_secret` | `secret` | Delete a secret |
| `list_conditions` | `condition` | List the conditions of a run, with each condition's `prompt`, `prompt_type`, `description`, and `timeout_s` (from `flyte` 2.13.5). If a condition's details fail to load, those fields are null and its `details_error` says why |
| `get_condition` | `condition` | Get one condition of a run: its prompt, payload type, and timeout. Requires `flyte` 2.13.5 or later |
| `signal_condition` | `condition` | Signal a waiting condition |
| `whoami` | `identity` | Show the caller's identity |
| `search_flyte_sdk_examples` | `search` | Search Flyte SDK examples |
| `search_flyte_docs_examples` | `search` | Search Flyte docs examples |
| `search_full_docs` | `search` | Search the full Flyte docs |
