---
title: Flyte agent plugins
weight: 5
variants: +flyte +union
---

# Flyte agent plugins

[`flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins) is an
**agent harness plugin for Flyte** — a portable bundle of **agent skills** and two
**MCP servers** that teach an AI coding agent to scaffold workflows, build and serve
apps, run and inspect executions, migrate Flyte 1 code to Flyte 2, and deploy Flyte
clusters, grounded in the Flyte SDK, the documentation, and (optionally) your own
cluster.

It's harness-agnostic: the same skills run in **Claude Code, Codex, Hermes,
OpenCode, Pi, and other agent harnesses**. In Claude Code the bundled MCP servers
are wired up for you automatically; in other harnesses you configure them manually.

## Compatibility

| Harness | Skills | MCP servers |
|---------|--------|-------------|
| Claude Code | All | Both, configured automatically |
| Codex | All | Manual setup |
| Hermes | Per-skill | Manual setup |
| OpenCode | All | Manual setup |
| Pi | All | Manual setup |

Support extends to other harnesses that load agent skills and MCP servers; see the
repository README for the current list and per-harness setup notes.

> [!NOTE]
> This is a community/open-source toolkit maintained in the
> [`flyteorg/flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins)
> repository. See the repository README for the authoritative, up-to-date list of
> harnesses, skills, tools, and installation options.

## Installation

Installation loads all of the skills into your harness. In **Claude Code** the two
bundled MCP servers (`flyte-docs` and `flyte-cluster`) are wired up automatically;
in every other harness you load the skills the same way, then configure the MCP
servers manually. Select your harness below.

{{< tabs "install" >}}
{{< tab "Claude Code" >}}
{{< markdown >}}
Add the marketplace and install the `flyte` plugin:

```bash
/plugin marketplace add flyteorg/flyte-agent-plugins
/plugin install flyte@flyte-agent-plugins
```

To pin a version, add the marketplace from a git reference:

```bash
/plugin marketplace add https://github.com/flyteorg/flyte-agent-plugins.git#<tag-or-branch>
/plugin install flyte@flyte-agent-plugins
```

To switch versions later, remove and re-add the marketplace with a different
reference. Both MCP servers are configured automatically from the plugin's
`.mcp.json`, so no further setup is required.
{{< /markdown >}}
{{< /tab >}}

{{< tab "Codex" >}}
{{< markdown >}}
Add the marketplace, then browse and install with `/plugins` inside Codex:

```bash
codex plugin marketplace add flyteorg/flyte-agent-plugins
```

Add `--ref <tag-or-branch>` to pin a specific version.

Codex does not bundle the MCP servers. To add the hosted `flyte-docs` server,
edit `~/.codex/config.toml`:

```toml
# ~/.codex/config.toml
[mcp_servers.flyte-docs]
url = "https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp"
```

For `flyte-cluster`, point Codex at the local launcher script using an absolute
path (Codex does not expand environment variables such as
`${CLAUDE_PLUGIN_ROOT}`).
{{< /markdown >}}
{{< /tab >}}

{{< tab "Hermes" >}}
{{< markdown >}}
Install individual skills by their repository path:

```bash
hermes skills install flyteorg/flyte-agent-plugins/plugins/flyte/skills/<skill-name>
```

For example:

```bash
hermes skills install flyteorg/flyte-agent-plugins/plugins/flyte/skills/flyte-deploy-aws
```

Hermes installs from the default branch only (no version pinning). Refresh
installed skills with `hermes skills check` or `hermes skills update`.

To add the hosted `flyte-docs` server, edit `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  flyte-docs:
    url: "https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp"
```
{{< /markdown >}}
{{< /tab >}}

{{< tab "OpenCode" >}}
{{< markdown >}}
The simplest approach uses the `skills` CLI, which reads the marketplace manifest:

```bash
npx skills add flyteorg/flyte-agent-plugins
npx skills add flyteorg/flyte-agent-plugins@<ref>
```

Alternatively, copy skill folders directly into the skills directory:

```bash
cp -r plugins/flyte/skills/flyte-deploy-aws ~/.config/opencode/skills/
```

OpenCode discovers `SKILL.md` folders in `.opencode/skills/` (project) and
`~/.config/opencode/skills/` (global).

To add the hosted `flyte-docs` server, edit `opencode.json`:

```json
{ "mcp": { "flyte-docs": { "type": "remote",
  "url": "https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp",
  "enabled": true } } }
```
{{< /markdown >}}
{{< /tab >}}

{{< tab "Pi" >}}
{{< markdown >}}
Install from the default branch or pin a specific tag/commit:

```bash
pi install https://github.com/flyteorg/flyte-agent-plugins
pi install git:github.com/flyteorg/flyte-agent-plugins@<tag>
```

Alternatively, clone the repository into `~/.pi/agent/skills/` — Pi discovers
nested `SKILL.md` folders recursively.

Pi uses the same `mcpServers` configuration format as the other harnesses,
defined in `~/.pi/agent/mcp.json`.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

For harnesses other than Claude Code, wire up both MCP servers manually:

- `flyte-docs` (remote HTTP): `https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp`
- `flyte-cluster` (local stdio): configure a local MCP server that runs the launcher script with an absolute path, for example:

    uv run --quiet --no-project /abs/path/to/plugins/flyte/scripts/flyte_mcp_stdio.py

See the upstream `flyte-agent-plugins` README (“Adding the MCP servers elsewhere”) for harness-specific configuration keys.

## Skills

The plugin ships skills across three areas: authoring Flyte 2 workflows and apps,
migrating from Flyte 1, and deploying Flyte clusters.

### SDK & workflow authoring

| Skill | What it helps with |
|-------|--------------------|
| `flyte-sdk-author` | Scaffold projects and generate tasks, workflows, launch plans, and apps from templates. |
| `flyte-sdk-types` | Choose the right types, I/O, and serialization for your data (DataFrames, files, images, HF datasets). |
| `flyte-sdk-ship` | Generate `flyte.Image` specs and Dockerfiles, and manage dependencies and reproducible builds. |
| `flyte-sdk-run` | Run workflows, inspect runs and actions, retrieve logs and outputs, and manage the run lifecycle. |
| `flyte-sdk-eval` | Build evaluation harnesses and unit tests to validate correctness and performance early. |
| `flyte-sdk-optimize` | Improve performance via task granularity, caching, and resource tuning using run metadata. |
| `flyte-sdk-app` | Build and serve apps — FastAPI, Streamlit, vLLM, SGLang, WebSocket, and browser apps. |
| `flyte-sdk-agent` | Build durable agents — ReAct, Plan-and-Execute, LangGraph, PydanticAI, memory, and MCP tools. |
| `flyte-sdk-data` | Author data-engineering patterns: ETL, data-quality checks, fan-out/map tasks, and dynamic workflows. |
| `flyte-sdk-ml` | Author ML workloads: training, hyperparameter optimization, evaluation, and batch/real-time inference. |

### Migration (Flyte 1 → Flyte 2)

| Skill | What it helps with |
|-------|--------------------|
| `flyte-migrate` | Entry-point orchestrator: explains the v1→v2 shift and routes to the sibling migration skills. |
| `flyte-migrate-tasks-workflows` | Convert task and workflow decorators to their Flyte 2 equivalents. |
| `flyte-migrate-config` | Migrate task configuration, images, resources, caching, secrets, scheduling, and CLI usage. |
| `flyte-migrate-control-flow` | Migrate branching, dynamic workflows, failure handling, and fan-out to native Flyte 2 Python. |
| `flyte-migrate-data-io` | Migrate data types and offloaded I/O (`FlyteFile`, `FlyteDirectory`, `StructuredDataset`) to `flyte.io`. |
| `flyte-migrate-ml` | Migrate ML workloads (training, HPO, GPU, batch inference) and adopt net-new v2 patterns. |

### Deployment

| Skill | What it helps with |
|-------|--------------------|
| `flyte-deploy-aws` | Deploy a Flyte v2 cluster on AWS from scratch — EKS + S3 + RDS, behind an ALB, with optional TLS and SSO. |
| `deploy-flyte-kind` | Deploy a Flyte stack on a local [kind](https://kind.sigs.k8s.io/) cluster with hosted PostgreSQL and object storage. |
| `deploy-flyte-kind-vm` | Provision a host (local or a cloud VM) and run the kind-based Flyte deployment on it. |
| `start-dex-local` | Stand up [Dex](https://dexidp.io/) as an in-cluster OIDC provider to test authentication locally. |

> [!NOTE]
> The deployment skills target self-hosted, open-source Flyte — provisioning your
> own EKS or kind cluster. They're most useful for evaluation and self-managed
> deployments; on a fully managed offering, cluster provisioning is handled for you.

## MCP servers

The plugin bundles two [MCP](https://modelcontextprotocol.io) servers that give
an assistant grounded knowledge of Flyte and, optionally, control over your
cluster.

| Server | Tools | Requirements |
|--------|-------|--------------|
| `flyte-docs` | Search tools over the Flyte SDK examples, documentation, and `llms.txt` | None — hosted by Union |
| `flyte-cluster` | Control-plane tools for running tasks, managing executions, and handling apps | `uv` + an authenticated Flyte CLI login |

The hosted `flyte-docs` server works immediately. The `flyte-cluster` server
operates on the cluster your Flyte CLI is logged into; set
`FLYTE_MCP_LOCAL_SEARCH=1` to run search locally instead of sending queries
externally.

> [!TIP]
> The `flyte-cluster` server is the same set of Flyte control-plane tools you can
> expose yourself with a `FlyteMCPAppEnvironment`. See
> [Flyte MCP server](../../user-guide/build-mcp/flyte_mcp_server) for how to build
> and scope your own Flyte MCP server.
