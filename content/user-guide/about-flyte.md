---
title: About Flyte
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
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

## Trying out Flyte

You can try out Flyte in a couple ways:

* To set up a local cluster on your own machine, go to [Getting started](../user-guide/getting-started).
* To try a turn-key cloud service that includes all of Flyte plus additional features, go to [Union.ai Serverless Getting started]({{< docs_home serverless>}}/user-guide/getting-started).

## Flyte in production

For production use, you will need to [deploy and manage Flyte on your own cloud infrastructure](../deployment/_index).

If you prefer a managed solution, have a look at:

* [Union.ai Serverless]({{< docs_home serverless>}}).
* [Union.ai BYOC (Bring Your Own Cloud)]({{< docs_home byoc>}}).
