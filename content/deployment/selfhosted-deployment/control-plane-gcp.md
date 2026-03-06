---
title: Control plane on GCP
weight: 2
variants: -flyte -serverless -byoc +selfmanaged
---

# Control plane on GCP

This guide covers deploying the {{< key product_name >}} control plane in a GCP environment as part of a [self-hosted deployment](./_index).

> [!NOTE]
> Self-hosted intra-cluster deployment is currently officially supported on **AWS** only.
> GCP support is in preview and additional cloud providers are coming soon.
> For production deployments, see [Control plane on AWS](./control-plane-aws).

## Prerequisites

In addition to the [general prerequisites](./_index#prerequisites), you need:

1. **Cloud SQL** PostgreSQL instance (12+)
2. **GCS buckets** for control plane metadata and artifacts storage
3. **GCP service accounts** configured with [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) for control plane services and artifacts

## Installation

### Step 1: Install prerequisites

#### Install ScyllaDB CRDs (if using embedded ScyllaDB)

```shell
cd helm-charts/charts/controlplane
./scripts/install-scylla-crds.sh
```

#### Add Helm repositories

```shell
helm repo add unionai https://unionai.github.io/helm-charts/
helm repo add flyte https://helm.flyte.org
helm repo update
```

### Step 2: Create registry image pull secret

Create the registry secret in the `union-cp` namespace:

```shell
kubectl create namespace union-cp

kubectl create secret docker-registry union-registry-secret \
  --docker-server="registry.unionai.cloud" \
  --docker-username="<REGISTRY_USERNAME>" \
  --docker-password="<REGISTRY_PASSWORD>" \
  -n union-cp
```

> [!NOTE]
> The registry username typically follows the format `robot$<org-name>`.
> Note the backslash escape (`\$`) before the `$` character in the username when running in a shell.
> Contact {{< key product_name >}} support if you haven't received your registry credentials.

### Step 3: Generate TLS certificates

gRPC requires TLS for HTTP/2 with NGINX. You can use self-signed certificates for intra-cluster communication.

{{< tabs >}}
{{< tab "OpenSSL (self-signed)" >}}

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout controlplane-tls.key \
  -out controlplane-tls.crt \
  -subj "/CN=controlplane-nginx-controller.union-cp.svc.cluster.local"

kubectl create secret tls controlplane-tls-cert \
  --key controlplane-tls.key \
  --cert controlplane-tls.crt \
  -n union-cp
```

{{< /tab >}}
{{< tab "cert-manager (recommended)" >}}

For production deployments, use cert-manager with a self-signed `ClusterIssuer` or your organization's CA. See the `extraObjects` section in [`values.gcp.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.gcp.selfhosted-intracluster.yaml) for an example configuration.

{{< /tab >}}
{{< /tabs >}}

### Step 4: Create database password secret

```shell
kubectl create secret generic union-controlplane-secrets \
  --from-literal=pass.txt='<YOUR_DB_PASSWORD>' \
  -n union-cp
```

> [!NOTE]
> The secret name `union-controlplane-secrets` is required and should not be changed.
> The secret must contain a key named `pass.txt` with the database password.

### Step 5: Download values files

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/controlplane/values.gcp.selfhosted-intracluster.yaml

curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/controlplane/values.registry.yaml
```

Create an overrides file `values.gcp.selfhosted-overrides.yaml`:

```yaml
global:
  GCP_REGION: "us-central1"
  DB_HOST: "10.247.0.3"
  DB_NAME: "unionai"
  DB_USER: "unionai"
  BUCKET_NAME: "my-company-cp-flyte"
  ARTIFACTS_BUCKET_NAME: "my-company-cp-artifacts"
  ARTIFACT_IAM_ROLE_ARN: "artifacts@my-project.iam.gserviceaccount.com"
  FLYTEADMIN_IAM_ROLE_ARN: "flyteadmin@my-project.iam.gserviceaccount.com"
  UNION_ORG: "my-company"
  GOOGLE_PROJECT_ID: "my-gcp-project"
```

To enable authentication, add the OIDC configuration to this file. See the [Authentication](./authentication) guide.

### Step 6: Install control plane

```shell
helm upgrade --install unionai-controlplane unionai/controlplane \
  --namespace union-cp \
  --create-namespace \
  -f values.gcp.selfhosted-intracluster.yaml \
  -f values.registry.yaml \
  -f values.gcp.selfhosted-overrides.yaml \
  --timeout 15m \
  --wait
```

**Values file layers (applied in order):**

1. [`values.gcp.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.gcp.selfhosted-intracluster.yaml) — GCP infrastructure defaults (database, storage, networking)
2. [`values.registry.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.registry.yaml) — Registry configuration and image pull secrets
3. `values.gcp.selfhosted-overrides.yaml` — Your environment-specific overrides

### Step 7: Verify installation

```shell
# Check pod status
kubectl get pods -n union-cp

# Verify services are running
kubectl get svc -n union-cp

# Check flyteadmin logs
kubectl logs -n union-cp deploy/flyteadmin --tail=50

# Test internal connectivity
kubectl exec -n union-cp deploy/flyteadmin -- \
  curl -k https://controlplane-nginx-controller.union-cp.svc.cluster.local
```

All pods should be in `Running` state and internal connectivity should succeed.

## Key configuration

### Single-tenant mode

Self-hosted deployments use single-tenant mode with an explicit organization:

```yaml
global:
  UNION_ORG: "my-company"
```

### TLS

Configure the namespace and name of the Kubernetes TLS secret:

```yaml
global:
  TLS_SECRET_NAMESPACE: "union-cp"
  TLS_SECRET_NAME: "controlplane-tls-cert"

ingress-nginx:
  controller:
    extraArgs:
      default-ssl-certificate: "union-cp/controlplane-tls-cert"
```

### Service discovery

Control plane services discover each other via Kubernetes DNS:

- **Flyteadmin**: `flyteadmin.union-cp.svc.cluster.local:81`
- **NGINX Ingress**: `controlplane-nginx-controller.union-cp.svc.cluster.local`
- **Data plane** (for dataproxy): `dataplane-nginx-controller.union.svc.cluster.local`

## Next steps

1. [Deploy the data plane](./data-plane-gcp)
2. [Configure authentication](./authentication)

## Troubleshooting

### Control plane pods not starting

```shell
kubectl describe pod -n union-cp <pod-name>
kubectl top nodes
kubectl get secret -n union-cp
```

### TLS/Certificate errors

```shell
kubectl get secret controlplane-tls-cert -n union-cp
kubectl get secret controlplane-tls-cert -n union-cp \
  -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -text -noout
kubectl logs -n union-cp deploy/controlplane-nginx-controller
```

### Database connection failures

```shell
# Verify credentials
kubectl get secret union-controlplane-secrets -n union-cp \
  -o jsonpath='{.data.pass\.txt}' | base64 -d

# Test connectivity
kubectl run -n union-cp test-db --image=postgres:14 --rm -it -- \
  psql -h <DB_HOST> -U <DB_USER> -d <DB_NAME>
```

### Workload Identity issues

```shell
# Verify service account annotations
kubectl get sa -n union-cp -o yaml | grep iam.gke.io/gcp-service-account

# Check IAM bindings
gcloud iam service-accounts get-iam-policy <SERVICE_ACCOUNT_EMAIL>

# Verify pod can authenticate
kubectl exec -n union-cp deploy/flyteadmin -- \
  curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email
```

### Data plane cannot connect to control plane

```shell
# Verify service endpoints
kubectl get svc -n union-cp | grep -E 'flyteadmin|nginx-controller'

# Test DNS resolution from data plane namespace
kubectl run -n union test-dns --image=busybox --rm -it -- \
  nslookup controlplane-nginx-controller.union-cp.svc.cluster.local

# Check network policies
kubectl get networkpolicies -n union-cp
kubectl get networkpolicies -n union
```
