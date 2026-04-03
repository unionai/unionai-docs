---
title: Data plane setup on GCP
weight: 4
variants: -flyte +union
sidebar_expanded: true
---

# Data plane setup on GKE (GCP)

{{< key product_name >}}'s modular architecture allows for great flexibility and control.
The customer can decide how many clusters to have, their shape, and who has access to what.
All communication is encrypted.  The Union architecture is described on the [Architecture](../architecture/_index) page.

If you already have a GKE cluster, GCS buckets, Artifact Registry repository, and Workload Identity configured, skip directly to [Deploy the dataplane](./deploy-dataplane).

Otherwise, start with [Prepare infrastructure](./prepare-infra) to set up the required GCP resources.
