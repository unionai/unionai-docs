---
title: Data plane setup on OCI
weight: 6
variants: -flyte -byoc +selfmanaged
sidebar_expanded: true
---

# Data plane setup on OCI

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](../architecture/_index) page.

If you already have an OKE cluster, Object Storage buckets, Container Registry, and IAM access configured, skip directly to [Deploy the dataplane](deploy-dataplane).

Otherwise, start with [Prepare infrastructure](prepare-infra) to set up the required OCI resources.
