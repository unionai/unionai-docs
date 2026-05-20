---
title: Troubleshooting
weight: 2
variants: -flyte +union
---

# Troubleshooting

Common issues encountered during and after a {{< key product_name >}} self-hosted deployment. Commands assume `kubectl` is configured against the cluster and that you've replaced `<controlplane-namespace>` / `<dataplane-namespace>` with the namespaces you used during install.

## Control plane

### Pods not starting

```shell
kubectl describe pod -n <controlplane-namespace> <pod-name>
kubectl top nodes
kubectl get secret -n <controlplane-namespace>
```

Check the pod's events for image-pull errors (registry pull secret), resource shortages (node capacity), or missing secrets (`controlplane-tls-cert`, the database password secret).

### TLS / certificate errors

```shell
# Inspect the TLS secret
kubectl get secret controlplane-tls-cert -n <controlplane-namespace>
kubectl get secret controlplane-tls-cert -n <controlplane-namespace> \
  -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -text -noout

# Ingress controller logs
kubectl logs -n <controlplane-namespace> deploy/<controlplane-ingress>
```

### Database connection failures

```shell
# Verify the password secret is decoded correctly
kubectl get secret <controlplane-secrets> -n <controlplane-namespace> \
  -o jsonpath='{.data.pass\.txt}' | base64 -d

# Test connectivity from inside the cluster
kubectl run -n <controlplane-namespace> test-db --image=postgres:14 --rm -it -- \
  psql -h <DB_HOST> -U <DB_USER> -d <DB_NAME>
```

If the secret exists but flyteadmin still cannot connect, confirm the DB host is reachable from the cluster — managed Postgres instances commonly require VPC peering or private connectivity.

## Data plane ↔ control plane

### Data plane cannot resolve control plane services

```shell
# DNS resolution from the data plane namespace
kubectl run -n <dataplane-namespace> test-dns --image=busybox --rm -it -- \
  nslookup <controlplane-ingress>.<controlplane-namespace>.svc.cluster.local

# Confirm the control plane service exists
kubectl get svc -n <controlplane-namespace> | grep nginx-controller
```

### Connection refused between data plane and control plane

```shell
# Control plane services and pods
kubectl get svc -n <controlplane-namespace>
kubectl get pods -n <controlplane-namespace>

# Network policies on both sides
kubectl get networkpolicies -n <dataplane-namespace>
kubectl get networkpolicies -n <controlplane-namespace>
```

Common causes: network policies blocking cross-namespace traffic, control plane pods not yet `Ready`, or `CONTROLPLANE_INTRA_CLUSTER_HOST` misconfigured in the data plane overrides file.

### Certificate verification errors

If you used self-signed certificates, the data plane chart's `values.{aws,gcp}.selfhosted-intracluster.yaml` already sets `insecureSkipVerify: true` for intra-cluster calls. Verify that `_U_INSECURE_SKIP_VERIFY` is present as an environment variable in task pods:

```shell
kubectl get pod <task-pod> -n <task-namespace> -o yaml | grep -A1 _U_INSECURE_SKIP_VERIFY
```

### Service endpoints

```shell
kubectl get svc -n <controlplane-namespace> | grep -E 'admin|nginx-controller'
```

## Cloud-specific

### AWS — IRSA authentication

If pods cannot access AWS resources (S3, RDS), verify the IAM Role for Service Account (IRSA) wiring:

```shell
# Confirm the service account has the role ARN annotation
kubectl get sa -n <controlplane-namespace> <service-account-name> -o yaml | grep eks.amazonaws.com/role-arn

# Verify the IAM trust policy permits the SA
aws iam get-role --role-name <ROLE_NAME>
```

### GCP — Workload Identity

```shell
# Service account annotation links GSA to KSA
kubectl get sa -n <controlplane-namespace> -o yaml | grep iam.gke.io/gcp-service-account

# IAM binding on the GSA permits the KSA to impersonate
gcloud iam service-accounts get-iam-policy <SERVICE_ACCOUNT_EMAIL>

# Pod can reach the metadata server
kubectl exec -n <controlplane-namespace> deploy/<admin-service> -- \
  curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email
```

### GCP — GCS access

```shell
# Bucket exists and is in the right project
gsutil ls -b gs://<METADATA_BUCKET>

# IAM bindings on the bucket
gsutil iam get gs://<METADATA_BUCKET>
```

Backend service accounts need `roles/storage.objectAdmin` (or equivalent) on the metadata bucket.

## Authentication

See the [Authentication troubleshooting](../authentication#troubleshooting) section.

## CRD install fails with `metadata.annotations: Too long: may not be more than 262144 bytes`

Several operator CRDs bundled with the control plane (`prometheuses.monitoring.coreos.com`, `alertmanagerconfigs.monitoring.coreos.com`, `scylladbclusters.scylla.scylladb.com`, several `gateway.networking.k8s.io` and `gateway.envoyproxy.io` types) have OpenAPI v3 schemas larger than Kubernetes' 256 KiB per-annotation limit. Applying them with a default `kubectl apply` or `helm install` writes the entire spec into `kubectl.kubernetes.io/last-applied-configuration` and the API server rejects the request.

The fix is to apply these CRDs with **server-side apply**, which tracks ownership via `metadata.managedFields` instead and never constructs the oversized annotation:

```shell
kubectl apply --server-side --force-conflicts -f helm-charts/crds/kube-prometheus-stack/
kubectl apply --server-side --force-conflicts -f helm-charts/crds/scylla-operator/
kubectl apply --server-side --force-conflicts -f helm-charts/crds/envoy-gateway/
```

Then `helm install`/`upgrade` the control plane and data plane charts with `--skip-crds` so Helm does not try to re-apply the bundled copies client-side. See [Getting started → Step 1](../getting-started#step-1-helm-repositories-and-crds) for the full sequence.
