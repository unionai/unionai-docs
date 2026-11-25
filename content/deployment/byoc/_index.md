---
title: Union-Managed deployment
description: Union.ai builds and manages the data plane infrastructure inside your cloud account; you supply the account.
icon: cloud-check
weight: 2
variants: -flyte +union
---

# Union-Managed deployment

In a Union-Managed deployment (formerly BYOC, Bring Your Own Cloud), Union.ai manages the data plane infrastructure in your cloud account.
You provide the cloud account; Union.ai builds the network and Kubernetes cluster in it and handles cluster operations, upgrades, and monitoring.

Your code, container images, logs, and runtime task inputs and outputs remain in your data plane.
The Union.ai control plane orchestrates workflow execution and stores orchestration metadata.
This metadata includes task, run, app, and reusable-environment definitions, run state, and error messages.
Definitions can contain default input values, environment variables, and app inputs as plain text.
Error messages may include data from Python tracebacks.
See [Data privacy](../platform-architecture#data-privacy) and [Where your data lives](../../user-guide/get-started/core-concepts/where-data-lives) for details.

## Getting started

1. Review the [platform architecture](../platform-architecture) to understand the control plane and data plane split.
2. Set up your data plane with the **Add a cluster** wizard in the Union.ai console. See the page for your cloud:
   - [AWS](./data-plane-setup-on-aws)
   - [GCP](./data-plane-setup-on-gcp)
   - [Azure](./data-plane-setup-on-azure)

## Additional configuration

- [Data retention policy](./data-retention-policy) for controlling stored data lifecycle
- [Single sign-on setup](./single-sign-on-setup/_index) for OAuth2/OIDC-based authentication
- [Multi-cluster and multi-cloud](./multi-cluster) for running several clusters, in different accounts or clouds

{{< subpage-cards >}}
