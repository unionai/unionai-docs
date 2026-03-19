---
title: Data plane on AWS
weight: 3
variants: -flyte -serverless -byoc +selfmanaged
---

# Data plane on AWS

This guide covers deploying the {{< key product_name >}} data plane in the same cluster as your control plane, as part of a [self-hosted deployment](./_index).

> [!NOTE]
> Deploy the [control plane](./control-plane-aws) first before proceeding with data plane installation.

## Prerequisites

In addition to the [general prerequisites](./_index#prerequisites):

1. **{{< key product_name >}} control plane** deployed in the same cluster (namespace `union-cp`)
2. **S3 buckets** for data plane metadata storage
3. **IAM roles** configured with [IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) for backend and worker service accounts
4. **Network connectivity** between data plane and control plane namespaces

## Installation

### Step 1: Install data plane CRDs

```shell
helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds \
  --namespace union \
  --create-namespace
```

### Step 2: Download values file

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.aws.selfhosted-intracluster.yaml
```

Create an overrides file `values.aws.selfhosted-overrides.yaml`:

```yaml
global:
  CLUSTER_NAME: "prod-us-east-1"
  ORG_NAME: "my-company"
  METADATA_BUCKET: "my-company-dp-metadata"
  FAST_REGISTRATION_BUCKET: "my-company-dp-metadata"
  AWS_REGION: "us-east-1"
  BACKEND_IAM_ROLE_ARN: "arn:aws:iam::123456789012:role/union-backend"
  WORKER_IAM_ROLE_ARN: "arn:aws:iam::123456789012:role/union-worker"
  CONTROLPLANE_INTRA_CLUSTER_HOST: "controlplane-nginx-controller.union-cp.svc.cluster.local"
  QUEUE_SERVICE_HOST: "queue.union-cp.svc.cluster.local:80"
  CACHESERVICE_ENDPOINT: "cacheservice.union-cp.svc.cluster.local:89"
```

If authentication is enabled on the control plane, also set `AUTH_CLIENT_ID`. See the [Authentication](./authentication) guide.

### Step 3: Install data plane

```shell
helm upgrade --install unionai-dataplane unionai/dataplane \
  --namespace union \
  --create-namespace \
  -f values.aws.selfhosted-intracluster.yaml \
  -f values.aws.selfhosted-overrides.yaml \
  --timeout 10m \
  --wait
```

**Values file layers (applied in order):**

1. [`values.aws.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/values.aws.selfhosted-intracluster.yaml) — AWS infrastructure defaults (storage, networking, intra-cluster communication)
2. `values.aws.selfhosted-overrides.yaml` — Your environment-specific overrides

### Step 4: Verify installation

```shell
# Check that data plane pods are running
kubectl get pods -n union

# Verify connectivity to control plane
kubectl logs -n union -l app.kubernetes.io/name=operator --tail=50 | grep "connection"

# Check service DNS resolution
kubectl exec -n union deploy/unionai-dataplane-operator -- \
  nslookup controlplane-nginx-controller.union-cp.svc.cluster.local
```

## Key differences from self-managed deployment

| Feature | Self-managed | Self-hosted (intra-cluster) |
|---|---|---|
| Control plane location | External ({{< key product_name >}}-managed) | Same Kubernetes cluster |
| Network path | Internet or VPN | Kubernetes internal networking |
| Authentication | OAuth2 via `uctl selfserve` | OAuth2 with [manual setup](./authentication) |
| TLS certificates | Trusted CA certificates | Can use self-signed certificates |
| Ingress type | LoadBalancer (external) | ClusterIP (internal) |

## Troubleshooting

### Cannot resolve control plane services

```shell
# Check DNS resolution from data plane namespace
kubectl run -n union test-dns --image=busybox --rm -it -- \
  nslookup controlplane-nginx-controller.union-cp.svc.cluster.local

# Verify the service exists
kubectl get svc -n union-cp | grep nginx-controller
```

### Connection refused errors

```shell
# Verify control plane services are running
kubectl get svc -n union-cp
kubectl get pods -n union-cp

# Check network policies
kubectl get networkpolicies -n union
kubectl get networkpolicies -n union-cp
```

### Certificate verification errors

If using self-signed certificates, ensure `insecureSkipVerify: true` is set in `values.aws.selfhosted-intracluster.yaml`. Verify the `_U_INSECURE_SKIP_VERIFY` environment variable is set in task pods.

### Authentication errors

See the [Authentication troubleshooting](./authentication#troubleshooting) section.
