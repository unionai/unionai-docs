---
title: Platform deployment
description: Subscribe and sign up, then run Union.ai's data plane in your own cloud account, self-managed or as a BYOC deployment.
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

## Get started

You can set up a self-managed deployment on AWS, GCP, or Azure yourself, from the Union.ai UI, without waiting on anyone:

1. **[Subscribe and sign up](./sign-up/_index).** Create your organization, your team's workspace in Union.ai. How you pay is separate from where your data plane runs: subscribe on AWS Marketplace to have the charges appear on your AWS bill, wherever your cluster is, or sign up directly. New organizations start with a 30-day free trial. You can [run a workflow on your own machine](./sign-up/run-locally) as soon as your organization exists, with no cluster.
2. **Provision your cloud resources** on [AWS](./selfmanaged/aws/_index), [GCP](./selfmanaged/gcp/_index), or [Azure](./selfmanaged/azure/_index). Create the Kubernetes cluster, object store, image registry, and identities the data plane runs on, in your own cloud account.
3. **[Connect your cluster](./selfmanaged/connect-a-cluster).** Enter your resources' details in the Union.ai UI and install the agent it gives you. The agent connects outwards and installs the data plane, so you never open a port, expose an endpoint, or hand over cluster credentials. See [What Union.ai installs in your cluster](./selfmanaged/whats-installed) for what ends up in your cluster and what it costs.

The UI flow covers AWS, GCP, and Azure today. If your data plane runs on OCI or a neocloud provider such as CoreWeave, Crusoe, or Nebius, or on your own Kubernetes cluster, follow the [self-managed setup with Helm](./selfmanaged/_index#other-providers-set-up-with-helm). If you want Union.ai to run your data plane for you, see [BYOC deployment](./byoc/_index).

{{< subpage-cards >}}
