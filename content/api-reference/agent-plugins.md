---
title: Flyte agent plugins
weight: 2
variants: +flyte +union
---

# Flyte agent plugins

[`flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins) is a
Claude Code plugin marketplace for working with Flyte. It bundles a set of
**agent skills** and two **MCP servers** that let an AI coding assistant scaffold
workflows, build and serve apps, run and inspect executions, migrate Flyte 1
code to Flyte 2, and deploy Flyte clusters — grounded in the Flyte SDK, the
documentation, and (optionally) your own cluster.

The skills are portable across several agent harnesses (Claude Code, Codex CLI,
Hermes, opencode, and pi); the MCP servers are configured automatically in
Claude Code and set up manually elsewhere.

> [!NOTE]
> This is a community/open-source toolkit maintained in the
> [`flyteorg/flyte-agent-plugins`](https://github.com/flyteorg/flyte-agent-plugins)
> repository. See the repository README for the authoritative, up-to-date list of
> skills, tools, and installation options.

## Installation

In Claude Code, add the marketplace and install the `flyte` plugin:

```bash
/plugin marketplace add flyteorg/flyte-agent-plugins
/plugin install flyte@flyte-agent-plugins
```

To pin a version, add the marketplace from a git reference:

```bash
/plugin marketplace add https://github.com/flyteorg/flyte-agent-plugins.git#<tag-or-branch>
```

Installing the plugin makes all of the skills available and, in Claude Code,
wires up both bundled MCP servers automatically.

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
> [Flyte MCP server](../user-guide/build-mcp/flyte_mcp_server) for how to build
> and scope your own Flyte MCP server.
