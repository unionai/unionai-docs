---
title: Platform deployment
description: Deploy the Union platform as a self-managed or BYOC.
icon: server
weight: 5
variants: -flyte +union
top_menu: true
mermaid: true
secondary_topnav: -flyte +union
---

# Platform deployment

You can deploy Union.ai on all major cloud providers, on neocloud providers, and on-premises on any Kubernetes cluster. You can also choose between two deployment models, depending on how much of the data plane you want to manage yourself:

* **[Self-managed deployment](./selfmanaged/_index)**: You run the data plane on infrastructure you control, and you manage the cluster, upgrades, and all operational aspects. Union.ai support has no access to your cluster, giving you the highest level of data isolation. Supported on AWS, GCP, Azure and OCI; on neocloud providers including CoreWeave, Crusoe, and Nebius; and on any generic Kubernetes environment.
* **[BYOC deployment](./byoc/_index)**: Union.ai manages the data plane for you, but it still runs in your cloud account. You manage your cloud account and its resources; Union.ai handles the cluster, upgrades, and monitoring. To do this, Union.ai support has some access to your cluster, strictly for upgrades, provisioning, and maintaining cluster health, but never to your object storage or logs. Supported on AWS, GCP, and Azure.

In both cases, the control plane runs in Union.ai's cloud account, but due to Union's [Zero Trust architecture](../security/_index), your data and code never traverse the control plane. Your code, data, container images, secrets and logs stay in the data plane in your own cloud account. See [Two-plane separation](../security/architecture/two-plane-separation) for how the split works.

## The fastest way to get started: Union.ai Teams on AWS Marketplace

The quickest route to a working Union.ai deployment is **Union.ai Teams**, a self-managed deployment you buy through AWS Marketplace and set up yourself, without waiting on anyone:

1. **Subscribe on AWS Marketplace.** The charges appear on your existing AWS bill, so there is no separate procurement process.
2. **Create your organization in the console.** You can run a workflow straight away, even before setting up your cluster.
3. **Provision your AWS resources.** Create an EKS cluster, an S3 bucket, an ECR repository and two IAM roles with the AWS CLI and `eksctl`.
4. **Connect your Kubernetes cluster.** Install the agent in your cluster and Union.ai installs the data plane into it. The agent connects outwards, so you never open a port, expose an endpoint, or hand over cluster credentials.

See [Self-service setup](./self-service/_index) for the step-by-step path.

If you need a platform AWS Marketplace doesn't cover, or you want Union.ai to run your data plane for you, see the [manual self-managed setup](./selfmanaged/_index) or [BYOC deployment](./byoc/_index).

{{< subpage-cards >}}
