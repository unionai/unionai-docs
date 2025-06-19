---
title: Introduction
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
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

You can try out Flyte in a couple ways:

* To set up a local cluster on your own machine, go to [Getting started](../user-guide/getting-started).
* To try a turn-key cloud service that includes all of Flyte plus additional features, go to [Union.ai Serverless Getting started]({{< docs_home serverless>}}/user-guide/getting-started).

## Flyte in production

For production use, you will need to [deploy and manage Flyte on your own cloud infrastructure](../deployment/_index).

If you prefer a managed solution, have a look at:

* [Union.ai Serverless]({{< docs_home serverless>}}).
* [Union.ai BYOC (Bring Your Own Cloud)]({{< docs_home byoc>}}).

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

{{< key product_name >}} unifies your AI development on a single end-to-end platform, bringing together data, models and compute with workflows of execution on a single pane of glass.

{{< key product_name >}} builds on [Flyte](https://flyte.org), the open-source standard for orchestrating AI workflows.
It offers all the features of Flyte while adding more capability to scale, control costs and serve models.

There are three deployment options for {{< key product_name >}}: **Serverless**, **BYOC** (Bring Your Own Cloud), and **Self-managed**.

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

You can switch to the Flyte docs [here]({{< docs_home flyte >}}).

You can try out Flyte's technology:

* In the cloud with [{{< key product_name >}} Serverless](https://signup.union.ai).
* On your machine with a [local Flyte cluster](./development-cycle/running-in-a-local-cluster).

For production use, you have to [deploy and manage Flyte on your own cloud infrastructure](../deployment).

## {{< key product_name >}} Serverless

[{{< key product_name >}} Serverless]({{< docs_home serverless >}}) is a turn-key solution that provides a fully managed cloud environment for running your workflows.
There is zero infrastructure to manage, and you pay only for the resources you use.
Your data and workflow code is stored safely and securely in {{< key product_name >}}'s cloud infrastructure.

{{< key product_name >}} Serverless provides:

* **All the features of Flyte**
* Granular, task-level resource monitoring
* Fine-grained role-based access control (RBAC)
* Faster performance:
    * Launch plan caching: Cache launch plans, 10-100x speed-up
    * Optimized Propeller: more than 10 core optimizations
    * Faster cache: Revamped caching subsystem for 10x faster performance
    * Accelerated datasets: Retrieve repeated datasets and models more quickly
    * Faster launch plan resolution
    * Reusable containers (do not pay the pod spin-up penalty)
* Interactive tasks:
    * Edit, debug and run tasks right in the pod through VS Code in the browser
* Artifacts discovery and lineage
* Reactive workflows:
    * Launch plans trigger (and kick off workflows) on artifact creation
* Smart defaults and automatic linking
* UI based workflow builder

## {{< key product_name >}} BYOC

[{{< key product_name >}} BYOC]({{< docs_home byoc >}}) (Bring Your Own Cloud) lets you keep your data and workflow code on your infrastructure, while {{< key product_name >}} takes care of the management.

{{< key product_name >}} BYOC provides:

* **All the features of Flyte**
* **All the features of {{< key product_name >}} Serverless**
* Accelerators and GPUs (including fractional GPUs)
* Managed Ray and Spark
* Multi-cluster and multi-cloud
* Single sign-on (SSO)
* SOC-2 Type 2 compliance

## {{< key product_name >}} Self-managed

[{{< key product_name >}} Self-managed]({{< docs_home selfmanaged >}}) lets you keep full control of your data, code, and infrastructure.

{{< key product_name >}} Self-managed provides:

* **All the features of Flyte**
* **All the features of {{< key product_name >}} Serverless**
* **All the features of {{< key product_name >}} BYOC**

The only difference between {{< key product_name >}} BYOC and {{< key product_name >}} Self-managed is that
with Self-managed you are responsible for the system infrastructure, either partially or fully, according to which option you choose:

* Deploy and manage your data plane yourself on your infrastructure while Union.ai manages the control plane on our infrastructure.

* Deploy and manage both your data plane and control plane on your infrastructure with support and guidance from Union.ai.
  This option is suitable for air-gapped deployments.

{{< /markdown >}}
{{< /variant >}}
