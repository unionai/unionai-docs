---
title: BYOC deployment
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# BYOC deployment

In a BYOC (Bring Your Own Cloud) deployment, Union.ai manages the data plane infrastructure in your cloud account.
You provide the cloud account and network configuration; Union.ai handles Kubernetes cluster operations, upgrades, and monitoring.

Your code, data, container images, and logs remain entirely in your data plane.
The Union.ai control plane orchestrates workflow execution but has no access to your proprietary data.

## Getting started

1. Review the [platform architecture](./platform-architecture) to understand the control plane and data plane split.
2. Set up your data plane on your cloud provider:
   - [AWS](./data-plane-setup-on-aws)
   - [Azure](./data-plane-setup-on-azure)
   - [GCP](./data-plane-setup-on-gcp)
3. [Configure your data plane](./configuring-your-data-plane) with your specific requirements (regions, node groups, networking).

## Cloud resource integration

Connect your data plane to cloud-native services:

- [AWS resources](./enabling-aws-resources/_index) (S3, ECR, Secrets Manager)
- [Azure resources](./enabling-azure-resources/_index) (Blob Storage, Container Registry, Key Vault)
- [GCP resources](./enabling-gcp-resources/_index) (Cloud Storage, Artifact Registry, BigQuery)

## Additional configuration

- [Single sign-on setup](./single-sign-on-setup/_index) for OAuth2/OIDC-based authentication
- [Multi-cluster and multi-cloud](./multi-cluster) for domain and project isolation
- [Data retention policy](./data-retention-policy) for controlling stored data lifecycle
