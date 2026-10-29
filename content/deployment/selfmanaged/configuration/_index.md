---
title: Configuration
description: Configure Union features on your own cluster.
icon: sliders
weight: 10
variants: -flyte +union
---

# Advanced configurations

This section covers the configuration of Union.ai features on your data plane cluster.

> [!NOTE] Data planes connected from the Union.ai UI
> Where a page sets values on the `dataplane` Helm chart, it is for a data plane installed with Helm: on OCI,
> CoreWeave, Crusoe, Nebius, or generic Kubernetes, or an existing AWS, GCP, or Azure deployment set up that way. On a
> data plane connected from the Union.ai UI, the agent installs the chart and manages its values, so change those
> settings through Union.ai rather than with `helm upgrade`. Pages that change your cloud resources or cluster, such
> as [data retention](./data-retention), [code viewer](./code-viewer), and [node pools](./node-pools), apply either
> way.

{{< subpage-cards >}}
