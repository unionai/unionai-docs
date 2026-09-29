---
title: User guide
description: Everything you need to build, run, and operate workloads on Flyte, from first task to production deployment.
icon: book
weight: 1
variants: +flyte +union
top_menu: true
site_root: true
---

{{< variant flyte >}}
{{< markdown >}}

# Flyte OSS

Flyte 2 is the durable AI runtime, in open source.
You write training, serving, and agent workloads in plain Python, and Flyte can recover them from failure, whether your code raised an error or the infrastructure failed under it with an OOM kill or a preempted node.
Flyte is Apache 2.0 licensed and a Linux Foundation AI & Data project, and you run it yourself on your own Kubernetes cluster.

> [!TIP] Try Flyte on Union.ai, free for 30 days
> [Union.ai]({{< docs_home union v2 >}}) is the commercial platform built on Flyte.
> Subscribe to Union Team on AWS Marketplace and try it free for 30 days.
> See [Setup from Marketplace]({{< docs_home union v2 >}}/deployment/marketplace/).

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

# {{% key product_name %}}

{{< key product_name >}} is the durable AI runtime your team owns.
Your workloads run in your own cloud, and your data and code never leave it: they never traverse the {{< key product_name >}} control plane.
On it, you build model factories, production agents, and model serving in plain Python, as durable steps that can recover from failure.

{{< key product_name >}} is enterprise-grade [Flyte]({{< docs_home flyte v2 >}}), open source at the core.
See [Platform deployment]({{< docs_home union v2 >}}/deployment/) for the ways to run it.

> [!TIP] Try Union.ai free for 30 days
> Subscribe to Union Team on AWS Marketplace and set up {{< key product_name >}} yourself, free for the first 30 days.
> See [Setup from Marketplace]({{< docs_home union v2 >}}/deployment/marketplace/).

{{< /markdown >}}
{{< /variant >}}

## Basics

Learn the basics of Flyte, covering all the core concepts around tasks, apps, agents, and typed model calls.

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

{{< link-card target="triggers" icon="alarm" title="Triggers" >}}
Run tasks automatically on a schedule or in reaction to new data, or save named launch configurations to fire on demand.
{{< /link-card >}}

{{< link-card target="agents" icon="robot" title="Agents" >}}
Durable, self-healing agents built from tasks and apps, with sandboxing and MCP.
{{< /link-card >}}

{{< link-card target="system-one-types" icon="sliders" title="System one types" >}}
Answer many typed questions in one call, with calibrated confidence, and decide what happens next in code.
{{< /link-card >}}

{{< /grid >}}

{{< variant union >}}

{{< markdown >}}

## Artifacts and factories

Name and version the datasets and models your tasks produce, trace where they came from, and build them on demand with factories.

{{< /markdown >}}

{{< grid >}}

{{< link-card target="artifacts" icon="box-seam" title="Artifacts" >}}
Register task outputs and uploads as named, versioned artifacts, trigger runs on new versions, mount them into apps, and trace lineage.
{{< /link-card >}}

{{< link-card target="factories" icon="diagram-3" title="Factories" >}}
Declare how artifacts are made from other artifacts, then ask for any artifact for a partition or a range and let Union build only what is missing or stale.
{{< /link-card >}}

{{< /grid >}}

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
