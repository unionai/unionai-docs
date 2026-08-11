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

Flyte is a free and open source platform that provides a full suite of features for orchestrating AI workflows.
Flyte enables AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.
You deploy and manage Flyte yourself, on your own cloud infrastructure.

> [!NOTE]
> These are the Flyte **2.0** docs.
> To switch to [version 1.0]({{< docs_home flyte v1 >}}) or to the commercial product, [**Union.ai**]({{< docs_home union v2 >}}), use the selectors above.

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

# {{% key product_name %}}

{{< key product_name >}} enables AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With {{< key product_name >}} your team can:

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

Learn the basics of Flyte, covering all the core concepts around tasks, apps, and agents.

{{< grid >}}

{{< link-card target="get-started" icon="lightbulb" title="Get started" >}}
What Flyte 2 is, how to install it, the core concepts, and the ways to run your code.
{{< /link-card >}}

{{< link-card target="tasks" icon="gear" title="Tasks" >}}
Configure, build, and deploy the durable batch workloads that everything else is made of.
{{< /link-card >}}

{{< link-card target="apps" icon="window" title="Apps" >}}
Long-running services for dashboards, REST APIs, and model endpoints.
{{< /link-card >}}

{{< link-card target="agents" icon="robot" title="Agents" >}}
Durable, self-healing agents built from tasks and apps, with sandboxing and MCP.
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

{{< markdown >}}

## Cluster and workload management

Stand up clusters and govern where your workloads run.

{{< /markdown >}}

{{< grid >}}

{{< link-card target="cluster-workload-management" icon="cloud" title="Clusters and queues" >}}
Group clusters into pools, register clusters, and create queues that route and rate-limit your workloads.
{{< /link-card >}}

{{< /grid >}}

{{< /variant >}}

## Advanced guides

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
