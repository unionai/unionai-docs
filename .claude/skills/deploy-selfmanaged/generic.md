# Generic Kubernetes path

Source of truth:
`content/deployment/selfmanaged/selfmanaged-generic/prepare-infra.md`
and `selfmanaged-generic/deploy-dataplane.md`. Use this path for
on-premise Kubernetes or any S3-compatible environment that isn't AWS,
GCP, Azure, OCI, or CoreWeave (those have their own paths).

## Cloud-specific prereqs

The user owns the cluster — the skill cannot create it. Verify it
exists and meets the requirements:

```bash
kubectl config current-context
kubectl get nodes
kubectl version --short            # server version: one of latest 3 minor
kubectl get sc                     # at least one StorageClass
kubectl get pods -n kube-system    # CoreDNS + CNI running
```

Required cluster features (from `prepare-infra.md`):
- Kubernetes version: one of the most recent three minor versions.
- A working CNI plugin (Calico, Flannel, Cilium, ...).
- CoreDNS running.
- A default StorageClass for PVCs.
- An ingress controller or load balancer.

If any of those are missing, halt and tell the user — don't try to
install them from inside this skill.

## Object storage prereqs

The user needs an S3-compatible store with two buckets (or one). The doc
uses MinIO as the example. Confirm the user has:

- Endpoint URL (e.g. `https://minio.example.com`)
- Access key and secret key with read/write on the buckets
- Bucket name(s): metadata + (optional) fast-registration

## Step-by-step deploy

### Phase A — Prepare infra

Already mostly the user's responsibility. The skill verifies:

1. Cluster checks (above) pass.
2. Buckets exist:
   ```bash
   # Example with mc (MinIO client) — adapt for the user's tooling
   mc ls myminio/<METADATA_BUCKET>
   mc ls myminio/<FAST_REG_BUCKET>
   ```

### Phase B — Deploy (`deploy-dataplane.md`)

1. Helm repo:
   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Generate values:
   ```bash
   uctl config init --host=<CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources \
     --clusterName <CLUSTER_NAME> --provider generic
   ```

3. Edit values per `deploy-dataplane.md`:
   - S3 endpoint URL
   - Bucket name(s)
   - Region (set to whatever the S3-compatible store reports — `us-east-1`
     works for most MinIO setups)
   - Path-style: most non-AWS S3 implementations use path-style
     (`s3ForcePathStyle: true`). MinIO defaults to path-style.

   Store credentials as a Kubernetes secret, reference from values:
   ```bash
   kubectl create secret generic union-s3-creds -n union \
     --from-literal=access-key-id=<ACCESS_KEY> \
     --from-literal=secret-access-key=<SECRET_KEY>
   ```

   Show the user the values diff before saving.

4. Install:
   ```bash
   helm upgrade --install union unionai/dataplane \
     -n union --create-namespace \
     -f <org>-values.yaml \
     --wait
   ```

## Verify

Same as other manual paths — `kubectl get pods -n union` plus optional
smoke suite from `scripts/`.

## Teardown

```bash
helm uninstall union -n union
kubectl delete secret union-s3-creds -n union
kubectl delete ns union     # only if no other workloads share the namespace
```

The cluster itself is the user's; do not propose deleting it. Bucket
deletion is the user's call (data may need archiving).

## Generic K8s gotchas

- **No StorageClass** is the most common failure mode — pods get stuck
  Pending on PVC binding. The prereq check above catches this.
- **Path-style vs virtual-hosted** depends on the S3 implementation.
  MinIO and most on-prem stores are path-style; CoreWeave is the
  notable exception (use the CoreWeave path for that).
- **Self-signed TLS on the S3 endpoint** requires either disabling TLS
  verification (not recommended) or mounting a CA bundle into the pods
  via values overrides. Point the user at the helm-chart-reference doc
  if they hit this.
- **Ingress controller** must already be installed — Union's chart
  doesn't bring its own.
