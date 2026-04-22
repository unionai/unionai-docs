---
title: Control plane on AWS
weight: 1
variants: -flyte +union
---

# Control plane on AWS

This guide covers deploying the {{< key product_name >}} control plane in an AWS environment as part of a [self-hosted deployment](./_index).

## Prerequisites

In addition to the [general prerequisites](./_index#prerequisites), you need:

1. **Amazon RDS** PostgreSQL instance (12+)
2. **S3 buckets** for control plane metadata and artifacts storage
3. **IAM roles** configured with [IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) for control plane services and artifacts

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

Create the registry secret in the control plane namespace:

```shell
kubectl create namespace <controlplane-namespace>

kubectl create secret docker-registry union-registry-secret \
  --docker-server="registry.unionai.cloud" \
  --docker-username="<REGISTRY_USERNAME>" \
  --docker-password="<REGISTRY_PASSWORD>" \
  -n <controlplane-namespace>
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
  -subj "/CN=<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local"

kubectl create secret tls controlplane-tls-cert \
  --key controlplane-tls.key \
  --cert controlplane-tls.crt \
  -n <controlplane-namespace>
```

{{< /tab >}}
{{< tab "cert-manager (recommended)" >}}

For production deployments, use cert-manager with a self-signed `ClusterIssuer` or your organization's CA. See the `extraObjects` section in [`values.aws.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.aws.selfhosted-intracluster.yaml) for an example configuration.

{{< /tab >}}
{{< /tabs >}}

### Step 4: Create database password secret

```shell
kubectl create secret generic <controlplane-secrets> \
  --from-literal=pass.txt='<YOUR_DB_PASSWORD>' \
  -n <controlplane-namespace>
```

> [!NOTE]
> The secret must contain a key named `pass.txt` with the database password.
> The default secret name is set in your Helm values.

### Step 5: Download values files

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/controlplane/values.aws.selfhosted-intracluster.yaml

curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/controlplane/values.registry.yaml
```

Create an overrides file `values.aws.selfhosted-overrides.yaml`:

```yaml
global:
  AWS_REGION: "us-east-1"
  DB_HOST: "my-rds-instance.abcdef.us-east-1.rds.amazonaws.com"
  DB_NAME: "unionai"
  DB_USER: "unionai"
  BUCKET_NAME: "my-company-cp-flyte"
  ARTIFACTS_BUCKET_NAME: "my-company-cp-artifacts"
  ARTIFACT_IAM_ROLE_ARN: "arn:aws:iam::123456789012:role/union-artifacts"
  FLYTEADMIN_IAM_ROLE_ARN: "arn:aws:iam::123456789012:role/union-flyteadmin"
  UNION_ORG: "my-company"
```

To enable authentication, add the OIDC configuration to this file. See the [Authentication](./authentication) guide.

### Step 6: Install control plane

```shell
helm upgrade --install unionai-controlplane unionai/controlplane \
  --namespace <controlplane-namespace> \
  --create-namespace \
  -f values.aws.selfhosted-intracluster.yaml \
  -f values.registry.yaml \
  -f values.aws.selfhosted-overrides.yaml \
  --timeout 15m \
  --wait
```

**Values file layers (applied in order):**

1. [`values.aws.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.aws.selfhosted-intracluster.yaml) — AWS infrastructure defaults (database, storage, networking)
2. [`values.registry.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.registry.yaml) — Registry configuration and image pull secrets
3. `values.aws.selfhosted-overrides.yaml` — Your environment-specific overrides

### Step 7: Verify installation

```shell
# Check pod status
kubectl get pods -n <controlplane-namespace>

# Verify services are running
kubectl get svc -n <controlplane-namespace>

# Check admin service logs
kubectl logs -n <controlplane-namespace> deploy/<admin-service> --tail=50

# Test internal connectivity
kubectl exec -n <controlplane-namespace> deploy/<admin-service> -- \
  curl -k https://<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local
```

All pods should be in `Running` state and internal connectivity should succeed.

> [!NOTE]
> Replace `<controlplane-namespace>` with your Helm release namespace (the namespace you used during `helm install`). Replace `<admin-service>` and `<controlplane-ingress>` with the actual deployment names from `kubectl get deploy -n <controlplane-namespace>`.

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
  TLS_SECRET_NAMESPACE: "<controlplane-namespace>"
  TLS_SECRET_NAME: "controlplane-tls-cert"

ingress-nginx:
  controller:
    extraArgs:
      default-ssl-certificate: "<controlplane-namespace>/controlplane-tls-cert"
```

### Service discovery

Control plane services discover each other via Kubernetes DNS:

- **Admin service**: `<admin-service>.<controlplane-namespace>.svc.cluster.local:81`
- **NGINX Ingress**: `<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local`
- **Data plane** (for dataproxy): `<dataplane-ingress>.<dataplane-namespace>.svc.cluster.local`

## Next steps

1. [Deploy the data plane](./data-plane-aws)
2. [Configure authentication](./authentication)

## Troubleshooting

### Control plane pods not starting

```shell
kubectl describe pod -n <controlplane-namespace> <pod-name>
kubectl top nodes
kubectl get secret -n <controlplane-namespace>
```

### TLS/Certificate errors

```shell
kubectl get secret controlplane-tls-cert -n <controlplane-namespace>
kubectl get secret controlplane-tls-cert -n <controlplane-namespace> \
  -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -text -noout
kubectl logs -n <controlplane-namespace> deploy/<controlplane-ingress>
```

### Database connection failures

```shell
# Verify credentials
kubectl get secret <controlplane-secrets> -n <controlplane-namespace> \
  -o jsonpath='{.data.pass\.txt}' | base64 -d

# Test connectivity
kubectl run -n <controlplane-namespace> test-db --image=postgres:14 --rm -it -- \
  psql -h <DB_HOST> -U <DB_USER> -d <DB_NAME>
```

### Data plane cannot connect to control plane

```shell
# Verify service endpoints
kubectl get svc -n <controlplane-namespace> | grep -E 'admin\|nginx-controller'

# Test DNS resolution from data plane namespace
kubectl run -n <dataplane-namespace> test-dns --image=busybox --rm -it -- \
  nslookup <controlplane-ingress>.<controlplane-namespace>.svc.cluster.local

# Check network policies
kubectl get networkpolicies -n <controlplane-namespace>
kubectl get networkpolicies -n <dataplane-namespace>
```
