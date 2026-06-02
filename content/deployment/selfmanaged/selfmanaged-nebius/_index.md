---
title: Data plane setup on Nebius
weight: 9
variants: -flyte +union
---

# Data plane setup on Nebius

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
You can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](../architecture/_index) page.

If you already have a Nebius Managed Kubernetes (MK8s) cluster and Nebius Object Storage (bucket, service account, access key) configured, skip directly to [Deploy the dataplane](./deploy-dataplane).

Otherwise, start with [Prepare infrastructure](./prepare-infra) to set up the required Nebius resources.
