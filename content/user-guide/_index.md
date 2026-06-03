---
title: User guide
weight: 1
variants: +flyte +union
top_menu: true
site_root: true
---

{{< variant flyte >}}
{{< markdown >}}

# Flyte OSS

Flyte is a free and open source platform that provides a full suite of powerful features for orchestrating AI workflows.
Flyte empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.
You deploy and manage Flyte yourself, on your own cloud infrastructure.

> [!NOTE]
> These are the Flyte **2.0** docs.
> To switch to [version 1.0]({{< docs_home flyte v1 >}}) or to the commercial product, [**Union.ai**]({{< docs_home union v2 >}}), use the selectors above.

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

# {{< key product_name >}}

{{< key product_name >}} empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With {{< key product_name >}} your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

{{< key product_name >}} is built on top of the leading open-source workflow orchestrator, [Flyte]({{< docs_home flyte v2 >}}).

{{< key product_name >}} provides all the features of Flyte, plus much more, in an environment where you keep your data and workflow code on your own infrastructure. {{< key product_name >}} is available as [BYOC]({{< docs_home union v2 >}}/deployment/byoc/_index) (Bring Your Own Cloud), where Union.ai manages the infrastructure for you, or [Self-managed]({{< docs_home union v2 >}}/deployment/selfmanaged/_index), where you manage the data plane yourself.

> [!NOTE]
> These are the Union.ai **2.0** docs.
> To switch to [version 1.0]({{< docs_home union v1 >}}) or to another product variant, use the selectors above.

{{< /markdown >}}
{{< /variant >}}

## Basics

Learn the basics of Flyte, covering all the core concepts around tasks and apps.

{{< grid >}}

{{< link-card target="overview" icon="lightbulb" title="Flyte 2" >}}
Build AI workflows in pure Python with built-in durability, reproducibility, and recovery.
{{< /link-card >}}

{{< link-card target="quickstart" icon="123" title="Quickstart" >}}
Install the SDK and run your first workflow locally in a few minutes.
{{< /link-card >}}

{{< link-card target="core-concepts" icon="book" title="Core concepts" >}}
The building blocks of every Flyte program: TaskEnvironments, tasks, runs, actions, and apps.
{{< /link-card >}}

{{< link-card target="run-modes" icon="play-circle" title="Run modes" >}}
Run the same task code locally, on a devbox, or on a remote cluster.
{{< /link-card >}}

{{< /grid >}}

## Tasks

Build durable, scalable, and reproducible batch workloads.

{{< grid >}}

{{< link-card target="task-configuration" icon="gear" title="Configure tasks" >}}
Define `TaskEnvironment`s for container images, resources, secrets, caching, retries, and more; use triggers for schedules.
{{< /link-card >}}

{{< link-card target="task-programming" icon="code" title="Build tasks" >}}
Compose tasks with fanout, parallelism, error handling, traces, files, and DataFrames.
{{< /link-card >}}

{{< link-card target="task-deployment" icon="rocket" title="Run and deploy tasks" >}}
Use `flyte run` for iteration or `flyte deploy` to register a stable task version.
{{< /link-card >}}

{{< /grid >}}

## Apps

Create long-running services to host dashboards, APIs, and model endpoints.

{{< grid >}}

{{< link-card target="configure-apps" icon="gear" title="Configure apps" >}}
Define `AppEnvironment`s with ports, autoscaling, custom domains, and authentication.
{{< /link-card >}}

{{< link-card target="build-apps" icon="code" title="Build apps" >}}
Build dashboards, REST APIs, and model endpoints with FastAPI, Streamlit, vLLM, and more.
{{< /link-card >}}

{{< link-card target="native-app-integrations" icon="code" title="Native app integrations" >}}
Use pre-built environments for popular frameworks like Streamlit, FastAPI, vLLM, and SGLang.
{{< /link-card >}}

{{< link-card target="serve-and-deploy-apps" icon="rocket" title="Serve and deploy apps" >}}
Use `flyte serve` for fast iteration or `flyte deploy` for production deployments.
{{< /link-card >}}

{{< /grid >}}

## Agents

Build durable, self-healing agents using tasks and apps as building blocks.

{{< grid >}}

{{< link-card target="build-agent" icon="robot" title="Build agents" >}}
Implement ReAct, Plan-and-Execute, and other agent patterns with full observability.
{{< /link-card >}}

{{< link-card target="sandboxing" icon="box" title="Sandboxing" >}}
Safely execute LLM-generated code with workflow sandboxes or ephemeral containers.
{{< /link-card >}}

{{< link-card target="build-mcp" icon="code" title="Build an MCP" >}}
Serve Model Context Protocol servers for AI assistants to interact with, hosted on {{< key product_name >}}.
{{< /link-card >}}

{{< /grid >}}

{{< variant union >}}

{{< markdown >}}

## Access and identity

How to authenticate and manage user permissions on your Union cluster.

{{< /markdown >}}

{{< grid >}}

{{< link-card target="authenticating" icon="key" title="Authenticating" >}}
Authenticate with Union.ai using OAuth2, API keys, and service accounts.
{{< /link-card >}}

{{< link-card target="user-management" icon="person" title="User management" >}}
Manage users, roles, and policies for your Union cluster.
{{< /link-card >}}

{{< /grid >}}

{{< /variant >}}

## Advanced Guides

Organize your codebase, optimize performance for production, and migrate from
other workflow orchestrators.

{{< grid >}}

{{< link-card target="project-patterns" icon="folder" title="Project patterns" >}}
Patterns for BYO images, monorepos with uv, CI/CD, and multi-team resource management.
{{< /link-card >}}

{{< link-card target="run-scaling" icon="box" title="Run scaling" >}}
Tune task overhead, batching, reusable containers, and fanout to scale your workflows.
{{< /link-card >}}

{{< link-card target="advanced-project" icon="rocket" title="Advanced project" >}}
An advanced guide for building an LLM reporting agent on Flyte.
{{< /link-card >}}

{{< link-card target="migration" icon="arrow-right" title="Migration" >}}
Port a Flyte 1 codebase to Flyte 2, or map Airflow concepts to their Flyte 2 equivalents.
{{< /link-card >}}

{{< /grid >}}
