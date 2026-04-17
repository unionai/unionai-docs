---
title: Secrets backends
weight: 1
variants: -flyte +union
---

# Secrets backends

The data plane supports four configurable secrets backends:

| Backend | Storage Location | Default? |
| --- | --- | --- |
| Kubernetes Secrets | K8s `etcd` on the customer cluster | Yes (default for self-managed) |
| AWS Secrets Manager | AWS-managed service | Optional |
| GCP Secret Manager | GCP-managed service | Optional |
| Azure Key Vault | Azure-managed service | Optional |

In all cases, secrets are stored within the customer's infrastructure.
The choice of backend is a deployment configuration on the data plane operator.

> [!NOTE]
> In BYOC deployments, the default secrets backend is a cloud-native secrets service (AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault) rather than Kubernetes Secrets. All four backends remain available as options regardless of deployment model. See [Deployment models and BYOC differences: Secrets management](../architecture/deployment-models#secrets-management).
