---
title: Data plane setup on Azure
weight: 5
variants: -flyte +union
---

# Data plane setup on Azure

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
You can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](../architecture/_index) page.

If you already have an AKS cluster, Storage Account with Data Lake Gen2, Managed Identities, and Workload Identity configured, skip directly to [Deploy the dataplane](./deploy-dataplane).

Otherwise, start with [Prepare infrastructure](./prepare-infra) to set up the required Azure resources.
