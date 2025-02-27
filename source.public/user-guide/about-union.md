# About Union

Union builds on [Flyte](http://flyte.org), the emerging open-source standard for orchestrating machine learning and data processing workflows,
Union offers all the features of Flyte while adding many additional capabilities.
There are two deployment options for Union: **Serverless** and **BYOC** (Bring Your Own Cloud).

## Flyte

Flyte is free and open source. You are responsible for setting up and managing your own infrastructure. All your data and workflow code is stored there.
Flyte provides a full suite of powerful features for orchestrating AL, ML, and data processing workflows:

* Reusable, immutable tasks and workflows
* Declarative task-level resource provisioning
* GitOps-style versioning and branching
* Strongly-typed interfaces between tasks enabling more reliable code
* Caching, intra-task checkpointing, and spot instance provisioning
* Task parallelism at scale with *map tasks*
* Dynamic workflows created at runtime for process flexibility

## Union Serverless

[Union Serverless](https://docs.union.ai/serverless) is a turn-key solution that provides a fully managed cloud environment for running your workflows.
There is zero infrastructure to manage, and you pay only for the resources you use.
Your Data and workflow code stored safely and securely in Union's cloud infrastructure.
Union Serverless provide all the features of Flyte, plus:

* Granular, task-level resource monitoring
* Fine-grained role-based access control (RBAC)
* Faster performance:
    * Launch plan caching: Cache launch plans, 10-100x speed-up
    * Optimized Propeller: more than 10 core optimizations
    * Faster cache: Revamped caching subsystem for 10x faster performance
    * Accelerated datasets: Retrieve repeated datasets and models faster
    * Faster launchplan resolution
    * Reusable containers (do not pay the pod spin-up penalty)
* Interactive tasks:
    * Edit, debug and run tasks right in the pod through VSCode in the browser
* Artifacts discovery and lineage
* Reactive workflows:
    * Launch plans trigger (and kick off workflows) on artifact creation
* Smart defaults and automatic linking
* UI based Workflow Builder

## Union BYOC

[Union BYOC](https://docs.union.ai/byoc) (Bring Your own Cloud) let's you keep your data and workflow code on your infrastructure, while Union takes care of the management.
Union BYOC provides all the features of Flyte and Union Serverless, plus:

* Accelerators and GPUs (including fractional GPUs)
* Managed Ray and Spark
* Multi-cluster and multi-cloud
* Single sign-on (SSO)
* SOC-2 Type 2 compliance.
