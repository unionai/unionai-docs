---
title: Flyte agent plugins
weight: 5
variants: +flyte +union
---

# Flyte agent plugins

[`flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins) bundles agent
skills and two MCP servers for Flyte. Install it and your coding agent can scaffold
workflows, build and serve apps, run and inspect executions, migrate Flyte 1 code to
Flyte 2, and deploy clusters, grounded in the Flyte SDK, the documentation, and
optionally your own cluster.

The same skills run in Claude Code, Codex, Hermes, opencode, pi, and any other harness
that supports agent skills. Claude Code and Codex wire up the MCP servers for you;
elsewhere you add them by hand.

## Compatibility

The skills are plain [Agent Skills](https://agentskills.io) (`SKILL.md` plus YAML
frontmatter), so they load in any harness that supports the standard. The MCP servers
are declared in the plugin's `.mcp.json`, which only some harnesses read.

| Harness | Skills | MCP servers | Version pinning |
|---------|--------|-------------|-----------------|
| Claude Code | All 20 | Both, automatically | Yes, git ref |
| Codex CLI | All 20 | Both, automatically | Yes, `--ref` |
| Hermes | Per-skill | Manual | No, default branch only |
| opencode | All 20 | Manual | Yes, tag/branch/commit |
| pi | All 20 | Manual | Yes, tag/commit |

Claude Code reads `.mcp.json` by convention; Codex is pointed at the same file by
`.codex-plugin/plugin.json`. The other three install the skills only. You can still add
the servers by hand; [the snippets are below](#adding-the-mcp-servers-manually).

## Installation

### Claude Code

```bash
/plugin marketplace add flyteorg/flyte-agent-plugins
/plugin install flyte@flyte-agent-plugins
```

To pin a version, add the marketplace from a git reference:

```bash
/plugin marketplace add https://github.com/flyteorg/flyte-agent-plugins.git#<tag-or-branch>
```

### Codex CLI

```bash
codex plugin marketplace add flyteorg/flyte-agent-plugins   # or --ref <tag-or-branch>
```

Then install the plugin from `/plugins` inside Codex. Both MCP servers come with it.

### Hermes

Hermes installs one skill at a time, from the default branch only:

```bash
hermes skills install flyteorg/flyte-agent-plugins/plugins/flyte/skills/<skill-name>
```

`hermes skills check` and `hermes skills update` refresh what you have installed.

### opencode

opencode discovers `SKILL.md` folders in `.opencode/skills/` (project) and
`~/.config/opencode/skills/` (global). The [`skills` CLI](https://github.com/vercel-labs/skills)
reads this repository's marketplace manifest:

```bash
npx skills add flyteorg/flyte-agent-plugins          # interactive selection
npx skills add flyteorg/flyte-agent-plugins@<ref>    # pin a tag/branch/commit
```

You can also copy a skill folder directly into the skills directory.

### pi

pi reads the `pi.skills` manifest in the repository's `package.json`:

```bash
pi install https://github.com/flyteorg/flyte-agent-plugins        # default branch
pi install git:github.com/flyteorg/flyte-agent-plugins@<tag>      # pinned
```

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
| `flyte-sdk-app` | Build and serve apps: FastAPI, Streamlit, vLLM, SGLang, WebSocket, and browser apps. |
| `flyte-sdk-agent` | Build durable agents: ReAct, Plan-and-Execute, LangGraph, PydanticAI, memory, and MCP tools. |
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
| `flyte-deploy-aws` | Deploy a Flyte v2 cluster on AWS from scratch: EKS + S3 + RDS, behind an ALB, with optional TLS and SSO. |
| `deploy-flyte-kind` | Deploy a Flyte stack on a local [kind](https://kind.sigs.k8s.io/) cluster with hosted PostgreSQL and object storage. |
| `deploy-flyte-kind-vm` | Provision a host (local or a cloud VM) and run the kind-based Flyte deployment on it. |
| `start-dex-local` | Stand up [Dex](https://dexidp.io/) as an in-cluster OIDC provider to test authentication locally. |

> [!NOTE]
> The deployment skills target self-hosted, open-source Flyte: they provision your own
> EKS or kind cluster. On a managed offering Union runs the cluster for you, so these
> skills are mainly useful for evaluation and self-managed deployments.

## MCP servers

The plugin bundles two [MCP](https://modelcontextprotocol.io) servers, split so nothing
is duplicated between them.

| Server | Transport | Tools | Needs |
|--------|-----------|-------|-------|
| `flyte-docs` | Hosted HTTP | 3 search tools over Flyte SDK examples, docs examples, `llms.txt` | Nothing |
| `flyte-cluster` | Local stdio | 29 control-plane tools: tasks, runs, actions, logs, apps, triggers, projects, secrets, conditions, identity | `uv`; a Flyte login for the tools to return data |

### What each one does with your data

`flyte-docs` is read-only, unauthenticated, and operated by Union. Search works the
moment you install, with no corpus to download and no `uv` required. Your search queries
do leave your machine.

`flyte-cluster` runs on your machine. It is the SDK's own `flyte-mcp` entry point,
fetched from PyPI at launch:

```bash
uvx --from "flyte[mcp]>=2.5.18" flyte-mcp --transport stdio \
  --tool-groups task,run,action,logs,app,trigger,project,secret,condition,identity
```

Calls go straight from your machine to your control plane, so no cluster data passes
through anything Union operates.

Two things in that command matter:

- `>=2.5.18` is the first release that caps its `mcp` dependency below 2.0. Below it the
  server fails at import.
- The `search` groups are left out. `flyte-docs` already serves them hosted, and enabling
  them here clones roughly 120 MB into `~/.flyte/mcp` on first launch.

To send nothing out at all, drop `flyte-docs` and add `search` to the `flyte-cluster`
groups. You trade the hosted lookup for the local corpus.

### A cluster is optional

`flyte-cluster` is tenant-agnostic: it uses the SDK's normal config discovery, so it acts
on whichever control plane your `flyte` CLI is authenticated against. It starts even with
no Flyte config: the tools register either way and fail only when called. So the plugin
still helps while you are deploying your first cluster.

### Adding the MCP servers manually

Hermes, opencode, and pi support MCP; the plugin does not configure it for them. Both
servers are portable: one is a URL, the other needs no checkout or path. Wiring them up
takes a few lines.

`flyte-docs`:

```toml
# Codex: ~/.codex/config.toml
[mcp_servers.flyte-docs]
url = "https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp"
```

```json
// opencode: opencode.json
{ "mcp": { "flyte-docs": { "type": "remote",
  "url": "https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp",
  "enabled": true } } }
```

```yaml
# Hermes: ~/.hermes/config.yaml
mcp_servers:
  flyte-docs:
    url: "https://flyte-mcp.apps.demo.hosted.unionai.cloud/flyte-mcp/mcp"
```

pi uses the same `mcpServers` shape in `~/.pi/agent/mcp.json`.

`flyte-cluster`:

```toml
# Codex: ~/.codex/config.toml
[mcp_servers.flyte-cluster]
command = "uvx"
args = ["--from", "flyte[mcp]>=2.5.18", "flyte-mcp", "--transport", "stdio",
        "--tool-groups", "task,run,action,logs,app,trigger,project,secret,condition,identity"]
```

```json
// opencode: opencode.json
{ "mcp": { "flyte-cluster": { "type": "local", "enabled": true,
  "command": ["uvx", "--from", "flyte[mcp]>=2.5.18", "flyte-mcp", "--transport", "stdio",
              "--tool-groups",
              "task,run,action,logs,app,trigger,project,secret,condition,identity"] } } }
```

```yaml
# Hermes: ~/.hermes/config.yaml
mcp_servers:
  flyte-cluster:
    command: "uvx"
    args: ["--from", "flyte[mcp]>=2.5.18", "flyte-mcp", "--transport", "stdio",
           "--tool-groups", "task,run,action,logs,app,trigger,project,secret,condition,identity"]
```

### Changing what is served

Edit `args` in the plugin's `.mcp.json`, or in your own config above, to pass
`--tool-groups`, `--tools`, or `--read-only`. Scope the server to one project and domain
with the `FLYTE_MCP_PROJECT` and `FLYTE_MCP_DOMAIN` environment variables.

> [!TIP]
> `flyte-cluster` exposes the same Flyte control-plane tools you can serve yourself with a
> `FlyteMCPAppEnvironment`. See
> [Flyte MCP server](../../user-guide/agents/build-mcp/flyte_mcp_server) for the full tool
> reference, tool groups, and allowlists.
