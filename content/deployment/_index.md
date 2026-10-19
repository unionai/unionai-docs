---
title: Platform deployment
description: Deploy Union.ai as a self-managed or BYOC deployment, or set it up yourself from the Union.ai UI.
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

## The fastest way to get started: set it up yourself from the Union.ai UI

The quickest route to a working Union.ai deployment is to set it up yourself, without waiting on anyone. You create your organization in the Union.ai UI, and you don't need a cluster to try it: as soon as your organization exists, you can run a workflow on your own machine and follow it in the UI. When you are ready to run workloads on your own infrastructure, you provision a cluster in your own cloud account and connect it, and Union.ai installs the data plane into it. The agent connects outwards, so you never open a port, expose an endpoint, or hand over cluster credentials. The result is a self-managed deployment.

How you subscribe depends on where your data plane runs:

- **AWS: subscribe on AWS Marketplace.** Buy **Union Team** on AWS Marketplace, so the charges appear on your existing AWS bill with no separate procurement process. New subscriptions start with a 30-day free trial. Then sign up, provision your AWS resources, and connect your cluster. Start at [AWS Marketplace](./marketplace/aws-marketplace).
- **GCP or Azure: subscribe through Union.ai.** There is no GCP or Azure marketplace listing, so contact Union.ai for a subscription. Then sign up, provision your GCP or Azure resources, and connect your cluster. Start at [Sign up for Union.ai](./marketplace/sign-up).

[Setup from Marketplace](./marketplace/_index) has the full path for both.

If your data plane runs somewhere Setup from Marketplace doesn't cover, such as OCI, a neocloud provider, or on-premises, or you want Union.ai to run your data plane for you, see the [manual self-managed setup](./selfmanaged/_index) or [BYOC deployment](./byoc/_index).

{{< subpage-cards >}}
