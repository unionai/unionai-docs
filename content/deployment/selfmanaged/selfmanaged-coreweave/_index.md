---
title: Data plane setup on CoreWeave
weight: 7
variants: -flyte +union
---

# Data plane setup on CoreWeave

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
You can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](../architecture/_index) page.

If you already have a CoreWeave Kubernetes Service (CKS) cluster and CoreWeave AI Object Storage (bucket, access keys, access policy) configured, skip directly to [Deploy the dataplane](./deploy-dataplane).

Otherwise, start with [Prepare infrastructure](./prepare-infra) to set up the required CoreWeave resources.
