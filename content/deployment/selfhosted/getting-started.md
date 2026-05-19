---
title: Getting started
weight: 1
variants: -flyte +union
---

# Getting started

This guide walks you through installing a {{< key product_name >}} self-hosted deployment end-to-end. It covers the **intra-cluster topology** — control plane and data plane in the same Kubernetes cluster — because it has the simplest substrate requirements and is the topology the chart's bundled `values.{aws,gcp}.selfhosted-intracluster.yaml` targets. Separate-cluster topology is also supported; see [Self-hosted deployment → Topologies](./_index#topologies) for the options.

It assumes your cloud substrate (VPC, Kubernetes cluster, database, object storage, identity bindings) is already provisioned. For what to provision and how to size it, see [Infrastructure requirements](./infrastructure-requirements).

> [!NOTE]
> Self-hosted intra-cluster deployment is officially supported on **AWS**. **GCP** support is in preview; additional cloud providers are coming. The walkthrough below uses tabs to switch between cloud-specific details where they differ.

## Prerequisites

Before starting, confirm you have:

1. A Kubernetes cluster meeting [Infrastructure requirements](./infrastructure-requirements) — sufficient capacity for both control plane and data plane, identity bindings for workload access to cloud resources, and a TLS-terminating ingress path.
2. Cloud resources provisioned: a PostgreSQL database (RDS or Cloud SQL), object storage buckets, and a managed secrets store. See [Infrastructure requirements](./infrastructure-requirements).
3. An OIDC provider (Okta, Entra ID, Auth0, or any OIDC-compliant IdP) for user authentication. See [Authentication](./authentication).
4. Registry credentials for the {{< key product_name >}} control-plane image registry, provided by your {{< key product_name >}} contact.
5. Local tools: [`helm`](https://helm.sh/docs/intro/install/) 3.18+, `kubectl` configured against your cluster, and `openssl` for TLS certificate generation (or `cert-manager` already installed in the cluster).

Two notes on conventions used below:

- Replace `<controlplane-namespace>` and `<dataplane-namespace>` with the Kubernetes namespaces where you intend to install each chart.
- The walkthrough overrides only the values that must be set per environment. For everything else, the chart's default `values.{aws,gcp}.selfhosted-intracluster.yaml` is sufficient. Avoid copying chart values into your overrides file — they drift quickly. Reference the chart's published values files in the [Helm chart repository](https://github.com/unionai/helm-charts) when you need to inspect a default.

## Deployment overview

1. Add Helm repositories and install ScyllaDB CRDs.
2. Create namespaces and the registry image pull secret.
3. Generate TLS certificates.
4. Create the database password secret.
5. Author your environment overrides file.
6. Install the control plane.
7. Install data plane CRDs.
8. Install the data plane.
9. Verify the installation.

## Step 1: Helm repositories and CRDs

Add the chart repositories:

```shell
helm repo add unionai https://unionai.github.io/helm-charts/
helm repo add flyte https://helm.flyte.org
helm repo update
```

If you plan to use the embedded ScyllaDB (default), install its CRDs:

```shell
cd helm-charts/charts/controlplane
./scripts/install-scylla-crds.sh
```

## Step 2: Namespaces and registry pull secret

Create the control plane namespace and the registry pull secret:

```shell
kubectl create namespace <controlplane-namespace>

kubectl create secret docker-registry union-registry-secret \
  --docker-server="registry.unionai.cloud" \
  --docker-username="<REGISTRY_USERNAME>" \
  --docker-password="<REGISTRY_PASSWORD>" \
  -n <controlplane-namespace>
```

> [!NOTE]
> Registry usernames typically follow the format `robot$<org-name>`. When passing the username on a shell, escape the `$` (`robot\$<org-name>`). Contact {{< key product_name >}} support if you have not received credentials.

## Step 3: TLS certificates

The control plane's NGINX ingress terminates gRPC over HTTP/2, which requires TLS. The chart references a Kubernetes TLS secret by name (`controlplane-tls-cert` in this walkthrough) — it neither generates nor requires any particular certificate source. Populate that secret with whatever certificate fits your trust model.

The chart's base `values.yaml` lists both the external `UNION_HOST` and the in-cluster `controlplane-nginx-controller.<namespace>.svc.cluster.local` on the same cert — one TLS secret serves both call paths. The secret name is wired into your overrides file in [Step 5](#step-5-environment-overrides).

Three common ways to source the certificate:

{{< tabs >}}
{{< tab "Existing certificate" >}}
{{< markdown >}}

If your organization already issues certificates (corporate CA, ACM, GCP Certificate Manager, etc.), load the PEM-encoded cert and key directly:

```shell
kubectl create secret tls controlplane-tls-cert \
  --key path/to/tls.key \
  --cert path/to/tls.crt \
  -n <controlplane-namespace>
```

The certificate's SANs should include your `UNION_HOST` DNS name. For intra-cluster topology, also include the in-cluster `controlplane-nginx-controller.<namespace>.svc.cluster.local` hostname.

{{< /markdown >}}
{{< /tab >}}
{{< tab "cert-manager" >}}
{{< markdown >}}

If cert-manager runs in the cluster, define a `Certificate` resource that writes to the secret name. Point the `issuerRef` at your organization's CA or a public ACME provider (Let's Encrypt):

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: controlplane-tls-cert
  namespace: <controlplane-namespace>
spec:
  secretName: controlplane-tls-cert
  dnsNames:
    - <UNION_HOST>
  issuerRef:
    name: <your-issuer>
    kind: ClusterIssuer
```

See the [cert-manager documentation](https://cert-manager.io/docs/usage/certificate/) for `Issuer`/`ClusterIssuer` setup.

{{< /markdown >}}
{{< /tab >}}
{{< tab "OpenSSL self-signed" >}}
{{< markdown >}}

For lab and evaluation environments where only trusted internal workloads reach the control plane:

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout controlplane-tls.key \
  -out controlplane-tls.crt \
  -subj "/CN=<UNION_HOST>"

kubectl create secret tls controlplane-tls-cert \
  --key controlplane-tls.key \
  --cert controlplane-tls.crt \
  -n <controlplane-namespace>
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Step 4: Database password secret

```shell
kubectl create secret generic <controlplane-secrets> \
  --from-literal=pass.txt='<YOUR_DB_PASSWORD>' \
  -n <controlplane-namespace>
```

> [!NOTE]
> The secret must contain a key named `pass.txt`. The default secret name is configurable in your Helm values.

## Step 5: Environment overrides

Author your own overrides file with the environment-specific values for your deployment — pick any filename you like (this guide uses `my-overrides.yaml`). The chart's `values.{aws,gcp}.selfhosted-intracluster.yaml` covers everything else.

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

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
  TLS_SECRET_NAMESPACE: "<controlplane-namespace>"
  TLS_SECRET_NAME: "controlplane-tls-cert"

ingress-nginx:
  controller:
    extraArgs:
      default-ssl-certificate: "<controlplane-namespace>/controlplane-tls-cert"
```

For the full list of available keys, see [`values.aws.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.aws.selfhosted-intracluster.yaml). To enable authentication, add the OIDC stanza per [Authentication](./authentication).

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

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
  TLS_SECRET_NAMESPACE: "<controlplane-namespace>"
  TLS_SECRET_NAME: "controlplane-tls-cert"

ingress-nginx:
  controller:
    extraArgs:
      default-ssl-certificate: "<controlplane-namespace>/controlplane-tls-cert"
```

For the full list of available keys, see [`values.gcp.selfhosted-intracluster.yaml`](https://github.com/unionai/helm-charts/blob/main/charts/controlplane/values.gcp.selfhosted-intracluster.yaml). To enable authentication, add the OIDC stanza per [Authentication](./authentication).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Step 6: Install the control plane

Download the chart's intracluster values file, then install with your overrides layered on top:

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/controlplane/values.aws.selfhosted-intracluster.yaml

helm upgrade --install unionai-controlplane unionai/controlplane \
  --namespace <controlplane-namespace> \
  --create-namespace \
  -f values.aws.selfhosted-intracluster.yaml \
  -f my-overrides.yaml \
  --timeout 15m --wait
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/controlplane/values.gcp.selfhosted-intracluster.yaml

helm upgrade --install unionai-controlplane unionai/controlplane \
  --namespace <controlplane-namespace> \
  --create-namespace \
  -f values.gcp.selfhosted-intracluster.yaml \
  -f my-overrides.yaml \
  --timeout 15m --wait
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

**Values file layering (applied in order):**

1. The chart's `values.{aws,gcp}.selfhosted-intracluster.yaml` — cloud infrastructure defaults (database, storage, networking, registry secret references).
2. Your `my-overrides.yaml` — environment-specific overrides.

The registry image pull secret created in Step 2 (`union-registry-secret`) is referenced by the chart's default `imagePullSecrets` — no separate registry values file is required.

## Step 7: Install data plane CRDs

```shell
helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds \
  --namespace <dataplane-namespace> \
  --create-namespace
```

## Step 8: Install the data plane

Author a data plane overrides file `dataplane-overrides.yaml`:

{{< tabs >}}
{{< tab "AWS" >}}
{{< markdown >}}

```yaml
global:
  CLUSTER_NAME: "prod-us-east-1"
  ORG_NAME: "my-company"
  METADATA_BUCKET: "my-company-dp-metadata"
  FAST_REGISTRATION_BUCKET: "my-company-dp-metadata"
  AWS_REGION: "us-east-1"
  BACKEND_IAM_ROLE_ARN: "arn:aws:iam::123456789012:role/union-backend"
  WORKER_IAM_ROLE_ARN: "arn:aws:iam::123456789012:role/union-worker"
  CONTROLPLANE_INTRA_CLUSTER_HOST: "<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local"
  QUEUE_SERVICE_HOST: "<queue-service>.<controlplane-namespace>.svc.cluster.local:80"
  CACHESERVICE_ENDPOINT: "<cacheservice>.<controlplane-namespace>.svc.cluster.local:89"
```

Then install:

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.aws.selfhosted-intracluster.yaml

helm upgrade --install unionai-dataplane unionai/dataplane \
  --namespace <dataplane-namespace> \
  --create-namespace \
  -f values.aws.selfhosted-intracluster.yaml \
  -f dataplane-overrides.yaml \
  --timeout 10m --wait
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP" >}}
{{< markdown >}}

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

Then install:

```shell
curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.gcp.selfhosted-intracluster.yaml

helm upgrade --install unionai-dataplane unionai/dataplane \
  --namespace <dataplane-namespace> \
  --create-namespace \
  -f values.gcp.selfhosted-intracluster.yaml \
  -f dataplane-overrides.yaml \
  --timeout 10m --wait
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

If authentication is enabled on the control plane, also set `AUTH_CLIENT_ID` in your overrides file. See [Authentication](./authentication).

## Step 9: Verify the installation

```shell
# Control plane pods
kubectl get pods -n <controlplane-namespace>

# Data plane pods
kubectl get pods -n <dataplane-namespace>

# Service endpoints
kubectl get svc -n <controlplane-namespace>
kubectl get svc -n <dataplane-namespace>

# Data plane → control plane connectivity
kubectl exec -n <dataplane-namespace> deploy/unionai-dataplane-operator -- \
  nslookup <controlplane-ingress>.<controlplane-namespace>.svc.cluster.local
```

All pods should reach `Running` state and service DNS resolution should succeed. To smoke-test the full path, trigger a hello-world run via `uctl` and confirm it reaches `SUCCEEDED`.

## Key configuration

A few values are worth understanding because they affect the deployment's identity and security posture.

### Single-tenant mode

Self-hosted deployments operate in single-tenant mode with an explicit organization name:

```yaml
global:
  UNION_ORG: "my-company"
```

### Service discovery

Control plane services discover each other via Kubernetes DNS:

- **Admin service**: `<admin-service>.<controlplane-namespace>.svc.cluster.local:81`
- **NGINX ingress**: `<controlplane-ingress>.<controlplane-namespace>.svc.cluster.local`
- **Data plane (for dataproxy)**: `<dataplane-ingress>.<dataplane-namespace>.svc.cluster.local`

## Key differences from a self-managed deployment

The defining difference between [self-managed](../selfmanaged/_index) and self-hosted is **who operates the control plane**. Everything else — topology, networking, certificate sources — follows from that choice and varies independently.

| Aspect | Self-managed | Self-hosted |
| --- | --- | --- |
| Control plane operator | {{< key product_name >}} | You |
| Control plane location | {{< key product_name >}}-managed infrastructure | Your Kubernetes cluster(s) |
| Authentication setup | Automated via `uctl selfserve` | OIDC configuration in your identity provider, with {{< key product_name >}} support — see [Authentication](./authentication) |
| Customization surface | Configurable within {{< key product_name >}}-supported parameters | Full Helm chart access |

## Next steps

- [Authentication](./authentication) — configure OIDC/OAuth2 for users and clients.
- [Authorization](./authorization) — pick an authorization mode (Noop, External, or built-in RBAC).
- [Image builder](./image-builder) — enable automatic task-image builds.
- [Operations](./operations/_index) — day-2 guidance: CI/CD integration, key rotation.
- [Operations → Troubleshooting](./operations/troubleshooting) — installation and runtime troubleshooting.
- [Operations → Monitoring](./operations/monitoring/_index) — observability stack setup and metrics reference.
