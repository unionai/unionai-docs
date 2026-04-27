---
title: Data plane on GCP
weight: 4
variants: -flyte +union
---

# Data plane on GCP

This guide covers deploying the {{< key product_name >}} data plane in the same cluster as your control plane, as part of a [self-hosted deployment](./_index).

> [!NOTE]
> Self-hosted intra-cluster deployment is currently officially supported on **AWS** only.
> GCP support is in preview and additional cloud providers are coming soon.
> For production deployments, see [Data plane on AWS](./data-plane-aws).

> [!NOTE]
> Deploy the [control plane](./control-plane-gcp) first before proceeding with data plane installation.

## Prerequisites

In addition to the [general prerequisites](./_index#prerequisites):

1. **{{< key product_name >}} control plane** deployed in the same cluster
2. **GCS buckets** for data plane metadata storage
3. **GCP service accounts** configured with [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) for backend and worker service accounts
4. **Network connectivity** between data plane and control plane namespaces

## Installation

### Step 1: Install data plane CRDs

```shell
helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds \
  --namespace <dataplane-namespace> \
  --create-namespace
```

### Step 2: Download values file

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.gcp.selfhosted-intracluster.yaml
```

Create an overrides file `values.gcp.selfhosted-overrides.yaml`:

```yaml
global:
  CLUSTER_NAME: "prod-us-central1"
  ORG_NAME: "my-company"
  METADATA_BUCKET: "my-company-dp-metadata"
  FAST_REGISTRATION_BUCKET: "my-company-dp-metadata"
  GCP_REGION: "us-central1"
  GOOGLE_PROJECT_ID: "my-gcp-project"
  BACKEND_IAM_ROLE_ARN: "union-backend@my-project.iam.gserviceaccount.com"
  WORKER_IAM_ROLE_ARN: "union-worker@my-project.iam.gserviceaccount.com"
  CONTROLPLANE_INTRA_CLUSTER_HOST: "<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local"
  QUEUE_SERVICE_HOST: "<queue-service>.<controlplane-namespace>.svc.cluster.local:80"
  CACHESERVICE_ENDPOINT: "<cacheservice>.<controlplane-namespace>.svc.cluster.local:89"
```

If authentication is enabled on the control plane, also set `AUTH_CLIENT_ID`. See the [Authentication](./authentication) guide.

### Step 3: Install data plane

```shell
helm upgrade --install unionai-dataplane unionai/dataplane \
  --namespace <dataplane-namespace> \
  --create-namespace \
  -f values.gcp.selfhosted-intracluster.yaml \
  -f values.gcp.selfhosted-overrides.yaml \
  --timeout 10m \
  --wait
```

**Values file layers (applied in order):**

1. [`values.gcp.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/dataplane/values.gcp.selfhosted-intracluster.yaml) — GCP infrastructure defaults (storage, networking, intra-cluster communication)
2. `values.gcp.selfhosted-overrides.yaml` — Your environment-specific overrides

### Step 4: Verify installation

```shell
# Check that data plane pods are running
kubectl get pods -n <dataplane-namespace>

# Verify connectivity to control plane
kubectl logs -n <dataplane-namespace> -l app.kubernetes.io/name=operator --tail=50 | grep "connection"

# Check service DNS resolution
kubectl exec -n <dataplane-namespace> deploy/unionai-dataplane-operator -- \
  nslookup <controlplane-ingress>.<controlplane-namespace>.svc.cluster.local
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
kubectl run -n <dataplane-namespace> test-dns --image=busybox --rm -it -- \
  nslookup <controlplane-ingress>.<controlplane-namespace>.svc.cluster.local

# Verify the service exists
kubectl get svc -n <controlplane-namespace> | grep nginx-controller
```

### Connection refused errors

```shell
# Verify control plane services are running
kubectl get svc -n <controlplane-namespace>
kubectl get pods -n <controlplane-namespace>

# Check network policies
kubectl get networkpolicies -n <dataplane-namespace>
kubectl get networkpolicies -n <controlplane-namespace>
```

### Workload Identity issues

```shell
# Verify service account annotations
kubectl get sa -n <dataplane-namespace> -o yaml | grep iam.gke.io/gcp-service-account

# Check IAM bindings
gcloud iam service-accounts get-iam-policy <BACKEND_SERVICE_ACCOUNT_EMAIL>
gcloud iam service-accounts get-iam-policy <WORKER_SERVICE_ACCOUNT_EMAIL>

# Verify pod can authenticate
kubectl exec -n <dataplane-namespace> deploy/unionai-dataplane-operator -- \
  curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email
```

### GCS access issues

```shell
# Verify bucket exists
gsutil ls -b gs://<METADATA_BUCKET>

# Check bucket IAM permissions
gsutil iam get gs://<METADATA_BUCKET>
```

Backend service accounts need `roles/storage.objectAdmin` or equivalent on the metadata bucket.

### Certificate verification errors

If using self-signed certificates, ensure `insecureSkipVerify: true` is set in `values.gcp.selfhosted-intracluster.yaml`. Verify the `_U_INSECURE_SKIP_VERIFY` environment variable is set in task pods.

### Authentication errors

See the [Authentication troubleshooting](./authentication#troubleshooting) section.
