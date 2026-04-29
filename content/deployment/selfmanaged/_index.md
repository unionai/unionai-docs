---
title: Self-managed deployment
weight: 2
variants: -flyte +union
llm_readable_bundle: true
---

# Self-managed deployment

{{< llm-bundle-note >}}

In a self-managed deployment, you operate the data plane on your own Kubernetes infrastructure.
Union.ai runs the control plane, but you manage the cluster, upgrades, and operational aspects of the data plane yourself.
Union.ai has no access to your cluster, providing the highest level of data isolation.

## Getting started

1. Review the [architecture](./architecture/_index) to understand the control plane, data plane operators, and security model.
2. Check the [cluster recommendations](./cluster-recommendations) for Kubernetes version, networking, and IP planning requirements.
3. Set up your data plane on your cloud provider:
   - [Generic Kubernetes](./selfmanaged-generic/_index) (on-premise or any S3-compatible environment)
   - [AWS](./selfmanaged-aws/_index)
   - [GCP](./selfmanaged-gcp/_index)
   - [Azure](./selfmanaged-azure/_index)
   - [OCI](./selfmanaged-oci/_index)

## Configuration

After initial setup, configure platform features on your cluster:

- [Authentication](./configuration/authentication)
- [Image builder](./configuration/image-builder)
- [Multi-cluster](./configuration/multi-cluster)
- [Node pools](./configuration/node-pools)
- [Monitoring](./configuration/monitoring)
- [Persistent logs](./configuration/persistent-logs)
- [Data retention](./configuration/data-retention)
- [Namespace mapping](./configuration/namespace-mapping)
- [Secrets management](./configuration/union-secrets)

## Reference

- [Helm chart reference](./helm-chart-reference/_index) for available chart values
- [Kubernetes access controls](./architecture/kubernetes-rbac) for RBAC configuration details
