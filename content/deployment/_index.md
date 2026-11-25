---
title: Platform deployment
description: Subscribe and sign up, then run Union.ai's data plane in your own cloud account, as a Union-Managed or a Self-Managed deployment.
icon: server
weight: 5
variants: -flyte +union
top_menu: true
mermaid: true
secondary_topnav: -flyte +union
---

# Platform deployment

You can deploy Union.ai on all major cloud providers, on neocloud providers, and on-premises on any Kubernetes cluster. You can also choose between two deployment models, depending on how much of the data plane you want to manage yourself:

* **[Union-Managed deployment](./byoc/_index)** (formerly BYOC): Union.ai runs the data plane for you, in your cloud account. You provide the cloud account; Union.ai builds the cluster in it and handles upgrades and monitoring. To do this, Union.ai support has some access to your cluster, strictly for upgrades, provisioning, and maintaining cluster health, but never to your object storage or logs. Supported on AWS, GCP, and Azure.
* **[Self-Managed deployment](./selfmanaged/_index)**: You run the data plane on infrastructure you control, and you manage the cluster, upgrades, and all operational aspects. Union.ai support has no access to your cluster, giving you the highest level of data isolation. Supported on AWS, GCP, Azure and OCI; on neocloud providers including CoreWeave, Crusoe, and Nebius; and on any generic Kubernetes environment.

In both cases, the control plane runs in Union.ai's cloud account, but due to Union's [Zero Trust architecture](../security/_index), your data and code never traverse the control plane. Your code, data, container images, secrets and logs stay in the data plane in your own cloud account. See [Architecture](../user-guide/get-started/core-concepts/architecture) for what each plane does, [Where your data lives](../user-guide/get-started/core-concepts/where-data-lives) for what data each holds, and [Two-plane separation](../security/architecture/two-plane-separation) for the security model behind the split.

## Get started

You set up either deployment yourself, from the Union.ai UI, without waiting on anyone.

1. **[Subscribe and sign up](./sign-up/_index).** Create your organization, your team's workspace in Union.ai. How you pay is separate from where your data plane runs: subscribe on AWS Marketplace to have the charges appear on your AWS bill, wherever your cluster is, or sign up directly. New organizations start with a 30-day [Team trial](./sign-up/team-trial). You can [run a workflow on your own machine](./sign-up/run-locally) as soon as your organization exists, with no cluster.
2. **Add a cluster.** Select **Connect your cluster** in the Union.ai UI. The **Add a cluster** wizard opens, and its first step asks how Union.ai should run your cluster:
   * **Union-Managed**: Union.ai builds the cluster in your AWS, GCP, or Azure account. See the [setup page for your cloud](./byoc/_index).
   * **Self-Managed**: first [provision your cloud resources](./selfmanaged/_index) on AWS, GCP, or Azure, then select **Self-Managed** and [connect your cluster](./selfmanaged/connect-a-cluster). You install an agent that connects outwards and installs the data plane, so you never open a port, expose an endpoint, or hand over cluster credentials. See [What Union.ai installs in your cluster](./selfmanaged/whats-installed) for what ends up in your cluster and what it costs.

If your data plane runs on OCI or a neocloud provider such as CoreWeave, Crusoe, or Nebius, or on your own Kubernetes cluster, follow the [Self-Managed setup with Helm](./selfmanaged/_index#other-providers-set-up-with-helm) instead.

{{< subpage-cards >}}
