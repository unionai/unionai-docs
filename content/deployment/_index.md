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

The quickest route to a working Union.ai deployment is **Union.ai Teams**, a self-managed deployment you buy through AWS Marketplace and set up yourself, without waiting on anyone. The charges appear on your existing AWS bill, so there is no separate procurement process, and new subscriptions start with a 30-day free trial.

You don't need a cluster to try it. As soon as your organization exists, you can run a workflow on your own machine and follow it in the Union.ai UI. When you are ready to run workloads on your own infrastructure, you connect a cluster in your AWS account and Union.ai installs the data plane into it. The agent connects outwards, so you never open a port, expose an endpoint, or hand over cluster credentials.

See [Self-serve setup](./self-serve/_index) for the step-by-step path.

If you need a platform AWS Marketplace doesn't cover, or you want Union.ai to run your data plane for you, see the [manual self-managed setup](./selfmanaged/_index) or [BYOC deployment](./byoc/_index).

{{< subpage-cards >}}
