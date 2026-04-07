---
title: Introduction
weight: 2
variants: +flyte +union
---

# Introduction

{{< variant flyte >}}
{{< markdown >}}

[Flyte](https://flyte.org) is a free and open source platform that provides a full suite of powerful features for orchestrating AI workflows.

## Flyte

Flyte provides the building blocks need for an end-to-end AI platform:

* Reusable, immutable tasks and workflows
* Declarative task-level resource provisioning
* GitOps-style versioning and branching
* Strongly-typed interfaces between tasks enabling more reliable code
* Caching, intra-task checkpointing, and spot instance provisioning
* Task parallelism with *map tasks*
* Dynamic workflows created at runtime for process flexibility

## Trying out Flyte

To set up a local cluster on your own machine, go to [Getting started](../user-guide/getting-started).

## Flyte in production

For production use, you will need to [deploy and manage Flyte on your own cloud infrastructure](../deployment/_index).

If you prefer a managed solution, have a look at [Union.ai BYOC (Bring Your Own Cloud)]({{< docs_home union v1 >}}).

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

{{< key product_name >}} unifies your AI development on a single end-to-end platform, bringing together data, models and compute with workflows of execution on a single pane of glass.

{{< key product_name >}} builds on [Flyte](https://flyte.org), the open-source standard for orchestrating AI workflows.
It offers all the features of Flyte while adding more capability to scale, control costs and serve models.

There are two deployment options for {{< key product_name >}}: **BYOC** (Bring Your Own Cloud) and **Self-managed**.

## Flyte

Flyte provides the building blocks need for an end-to-end AI platform:

* Reusable, immutable tasks and workflows
* Declarative task-level resource provisioning
* GitOps-style versioning and branching
* Strongly-typed interfaces between tasks enabling more reliable code
* Caching, intra-task checkpointing, and spot instance provisioning
* Task parallelism with *map tasks*
* Dynamic workflows created at runtime for process flexibility

Flyte is open source and free to use.

You can switch to the Flyte docs [here]({{< docs_home flyte v1 >}}).

You can try out Flyte's technology:

* On your machine with a [local Flyte cluster](./development-cycle/running-in-a-local-cluster).

For production use, you have to [deploy and manage Flyte on your own cloud infrastructure](../deployment).

## {{< key product_name >}}

{{< key product_name >}} provides all the features of Flyte, plus:

* Accelerators and GPUs (including fractional GPUs)
* Managed Ray and Spark
* Multi-cluster and multi-cloud
* Single sign-on (SSO)
* SOC-2 Type 2 compliance

### BYOC (Bring Your Own Cloud)

[{{< key product_name >}} BYOC]({{< docs_home union v1 >}}) lets you keep your data and workflow code on your infrastructure, while {{< key product_name >}} takes care of the management. Union.ai manages the data plane's Kubernetes cluster in your cloud account.

### Self-managed

[{{< key product_name >}} Self-managed]({{< docs_home union v1 >}}) lets you keep full control of your data, code, and infrastructure. You are responsible for the system infrastructure, either partially or fully:

* Deploy and manage your data plane yourself on your infrastructure while Union.ai manages the control plane on our infrastructure.

* Deploy and manage both your data plane and control plane on your infrastructure with support and guidance from Union.ai.
  This option is suitable for air-gapped deployments.

{{< /markdown >}}
{{< /variant >}}
