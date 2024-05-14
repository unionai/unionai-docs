# Union and Flyte

The Union AI platform was created by the team behind [Flyte](http://flyte.org). Union's intuitive end-to-end platform was developed with the Flyte open-source orchestration system at its core.
All workflows and tasks built for Flyte are seamlessly portable to Union's platform.
Union is Kubernetes native and runs in your infrastructure, so you can run it on the cloud platform of your choosing.

## Union includes Flyte

Union includes all the features and advantages of Flyte:

* Reusable, immutable tasks and workflows
* Declarative task-level resource provisioning
* GitOps-style versioning and branching
* Strongly-typed interfaces between tasks enabling more reliable code
* Caching, intra-task checkpointing, and spot instance provisioning
* Mass task parallelism ("map tasks")
* Dynamic workflows created at runtime for process flexibility

## Union adds further capabilities

In addition to the features of Flyte, Union adds the following features:

* Your infrastructure managed by Union
    * Your data and workflow code stays on your infrastructure (and all processing happens there) but it is all managed by Union.
* Granular, task-level resource monitoring
* Fine-grained role-based access control (RBAC)
* Faster performance
    * Launch plan caching: Cache launch plans, 10-100x speed-up
    * Optimized Propeller: more than 10 core optimizations
    * Faster cache: Revamped caching subsystem for 10x faster performance
    * Accelerated datasets: Retrieve repeated datasets and models faster
    * Faster launchplan resolution
    * Reusable containers (do not pay the pod spin-up penalty)
* Interactive tasks
    * Edit, debug and run tasks right in the pod through VSCode in the browser
* Artifacts discovery and lineage
* Reactive workflows
    * Launch plans trigger (and kick off workflows) on artifact creation
* Smart defaults and automatic linking
* Accelerators and GPUs (including fractional GPUs)
* Managed Ray and Spark
* UI based Workflow Builder
* Multi-cluster and multi-cloud
* Single sign-on (SSO)
* SOC-2 Type 2 compliance.

## Moving from Flyte to Union

Moving your project from a self-hosted Flyte setup to Union is easy.
All you have to do is change the deployment target of your project.
See [Setting up the project on Union](getting-started/setting-up-the-project-on-union).
