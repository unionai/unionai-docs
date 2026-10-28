---
title: Self-managed deployment
description: Run the data plane on your own Kubernetes cluster, owning the cluster and its upgrades while Union.ai runs the control plane.
icon: server
weight: 2
variants: -flyte +union
---

# Self-managed deployment

In a self-managed deployment, you operate the data plane on your own Kubernetes infrastructure.
Union.ai runs the control plane, but you manage the cluster, upgrades, and operational aspects of the data plane yourself.
Union.ai has no access to your cluster, providing the highest level of data isolation.

## AWS, GCP, and Azure: set up from the Union.ai UI

Before you start, [subscribe and sign up](../sign-up/_index). Then:

1. Provision your cloud resources, using the page for your provider:
   - [AWS](./aws/_index)
   - [GCP](./gcp/_index)
   - [Azure](./azure/_index)
2. [Connect your cluster](./connect-a-cluster). You enter your resources' details in the Union.ai UI and install the agent it gives you, and the agent installs the data plane. You skip the Helm install below.

Each provider's page has a **Legacy steps** page under it: the earlier instructions, which install the data plane yourself with Helm. They remain for deployments that were set up that way. For a new deployment on AWS, GCP, or Azure, use the steps above.

## Other providers: set up with Helm

The UI flow covers AWS, GCP, and Azure today. On OCI, CoreWeave, Crusoe, and Nebius, and on generic Kubernetes (on-premises or any other environment), you provision the infrastructure and install the data plane with Helm yourself. Existing AWS, GCP, and Azure deployments that were set up with Helm follow this path too:

1. Review the [architecture](./architecture/_index) to understand the control plane, data plane operators, and security model.
2. Review the [infrastructure recommendations](./infrastructure-recommendations/_index) for the sizing model, networking and IP planning, identity, and the [scaling constraints](./infrastructure-recommendations/scaling-constraints) to plan around.
3. Provision your infrastructure using the page for your provider:
   - [OCI](./infrastructure-recommendations/oci)
   - [Generic Kubernetes](./infrastructure-recommendations/generic) (on-premise or any S3-compatible environment)
   - [CoreWeave](./infrastructure-recommendations/coreweave)
   - [Crusoe](./infrastructure-recommendations/crusoe)
   - [Nebius](./infrastructure-recommendations/nebius)
4. [Deploy the data plane](./deploy/_index) once your infrastructure is ready. CoreWeave, Crusoe, and Nebius have their deploy steps on their own pages.
5. [Upgrade the data plane](./upgrade) when a new chart version is released. You own the chart version, its CRDs, and your values file.

## Configuration

After initial setup, configure platform features on your cluster. Where a page sets values on the `dataplane` Helm chart, it is for a data plane installed with Helm: on one connected from the Union.ai UI, the agent manages the chart and its values (see [Configuration](./configuration/_index)).

- [Image builder](./configuration/image-builder)
- [Multi-cluster](./configuration/multi-cluster)
- [Node pools](./configuration/node-pools)
- [Monitoring](./configuration/monitoring)
- [Persistent logs](./configuration/persistent-logs)
- [Data retention](./configuration/data-retention)
- [Namespace mapping](./configuration/namespace-mapping)
- [Secrets management](./configuration/union-secrets)

## Reference

- [Helm chart reference](./helm-chart-reference/_index) for the chart values available when you install with Helm
- [Kubernetes access controls](./architecture/kubernetes-rbac) for RBAC configuration details

{{< subpage-cards >}}
