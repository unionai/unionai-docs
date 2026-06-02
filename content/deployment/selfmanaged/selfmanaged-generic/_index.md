---
title: Data plane setup on generic Kubernetes
weight: 3
variants: -flyte +union
---

# Data plane setup on generic Kubernetes

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
You can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](../architecture/_index) page.

> [!NOTE] These instructions cover installing Union.ai in an on-premise Kubernetes cluster.
> If you are installing at a cloud provider, use the cloud provider specific instructions: [AWS](../selfmanaged-aws/_index), [GCP](../selfmanaged-gcp/_index), [Azure](../selfmanaged-azure/_index), [OCI](../selfmanaged-oci/_index).

If you already have a Kubernetes cluster, S3-compatible object storage, a container registry, and credentials configured, skip directly to [Deploy the dataplane](./deploy-dataplane).

Otherwise, start with [Prepare infrastructure](./prepare-infra) to set up the required resources.
