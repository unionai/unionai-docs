# Union overview

Union was created by the team behind [Flyte](http://flyte.org), the emerging standard in AI orchestration.
Union includes all the features and advantages of Flyte, and adds additional capabilities.

## Union includes Flyte

Union includes all the features of Flyte:

* Reusable, immutable tasks and workflows
* Declarative task-level resource provisioning
* GitOps-style versioning and branching
* Strongly-typed interfaces between tasks enabling more reliable code
* Caching, intra-task checkpointing, and spot instance provisioning
* Task parallelism at scale with *map tasks*
* Dynamic workflows created at runtime for process flexibility

## Union deployment options

Union offers two deployment options: Serverless and BYOC (Bring Your Own Cloud).
Both of these options greatly simplify infrastructure management and provide additional features on top of Flyte.

### Union Serverless

Union Serverless is a turnkey solution that takes care of all the infrastructure for you.
All you need to do is sign up through your GitHub account and start running your workflows.
This option gives you:

* All the features of Flyte
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
* UI based Workflow Builder

### Union BYOC

Union BYOC (Bring Your Own Cloud) let's you keep your data and workflow code on your infrastructure,
but has Union manage it for you. It also offers more control over your hardware and other advanced features.
This option gives you:

* All the features of Flyte and Union Serverless
* Your infrastructure managed by Union
    * Your data and workflow code stays on your infrastructure (and all processing happens there) but it is all managed by Union.
* Accelerators and GPUs (including fractional GPUs)
* Managed Ray and Spark
* Multi-cluster and multi-cloud
* Single sign-on (SSO)
* SOC-2 Type 2 compliance.
