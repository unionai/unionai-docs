---
title: About Flyte
weight: 1
variants: +flyte -serverless -byoc -byok
---

# About Flyte

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

Flyte is open source and free to use.

You can try out Flyte's technology:

* In the cloud with [Union Serverless](https://signup.union.ai).
* On your machine with a [local Flyte cluster]().

<!-- TODO: add link ^ -->

For production use, you have to [deploy and manage Flyte on your own cloud infrastructure](../deployment/_index).


## Union Serverless

[Union Serverless]({{< docs_home serverless >}}) is a turn-key solution that provides a fully managed cloud environment for running your workflows.
There is zero infrastructure to manage, and you pay only for the resources you use.
Your Data and workflow code stored safely and securely in Union's cloud infrastructure.
Union Serverless provide all the features of Flyte, plus:

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


## Union BYOC

[Union BYOC]({{< docs_home byoc >}}) (Bring Your Own Cloud) lets you keep your data and workflow code on your infrastructure, while Union takes care of the management.
Union BYOC provides all the features of Flyte and Union Serverless, plus:

* Accelerators and GPUs (including fractional GPUs)
* Managed Ray and Spark
* Multi-cluster and multi-cloud
* Single sign-on (SSO)
* SOC-2 Type 2 compliance


## Union BYOK

[Union BYOK]({{< docs_home byok >}}) (Bring Your Own Kubernetes) lets you keep your data and workflow code on your infrastructure and under your own management.
Union BYOK provides all the features of BYOC, with the only difference being that you manage your own data plane.
The control plane continues to be located in a Union AWS account and managed by Union.
However, none of your data ever leaves your data plane, ensuring privacy and security.
