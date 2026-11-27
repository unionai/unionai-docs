---
title: Legacy setup
description: The earlier Union-Managed setup instructions for AWS, GCP, and Azure, for data planes that weren't created with the Add a cluster wizard.
icon: archive
weight: 10
variants: -flyte +union
---

# Legacy setup

These are the earlier setup instructions for a Union-Managed data plane on AWS, GCP, and Azure.
You grant Union.ai access to your cloud account by hand, send the Union.ai team your infrastructure requirements, and the Union.ai team provisions the data plane.

Use them for a data plane that was set up this way.
To create a data plane, use the **Add a cluster** wizard instead: see the setup page for [AWS](../data-plane-setup-on-aws), [GCP](../data-plane-setup-on-gcp), or [Azure](../data-plane-setup-on-azure).

## Set up the data plane

1. Grant Union.ai access to your cloud account:
   - [AWS](./data-plane-setup-on-aws)
   - [GCP](./data-plane-setup-on-gcp)
   - [Azure](./data-plane-setup-on-azure)
2. [Configure your data plane](./configuring-your-data-plane): the regions, node groups, and networking to send to the Union.ai team.

## Connect cloud resources

Give your tasks access to cloud services in your account:

- [AWS resources](./enabling-aws-resources/_index): S3, ECR, and Secrets Manager
- [GCP resources](./enabling-gcp-resources/_index): Cloud Storage, Artifact Registry, Secret Manager, and BigQuery
- [Azure resources](./enabling-azure-resources/_index): Blob Storage, Container Registry, and Key Vault

{{< subpage-cards >}}
